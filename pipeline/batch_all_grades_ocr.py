"""
Batch All Grades OCR Runner — Hệ Thống Quét Tự Động Toàn Bộ SGK Các Lớp Còn Lại
Sử dụng Vision Model Qwen2.5-VL 7B chạy 100% Offline trên GPU NVIDIA GeForce RTX 3080.
Hỗ trợ checkpoint lưu tiến độ thời gian thực, resume bất kì lúc nào, tự phục hồi lỗi.
"""
import os
import sys
import json
import base64
import time
import urllib.request
from pathlib import Path
import fitz

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"d:\antigravity_scratch\real_estate_scoring\sql\SGK")
DATA_DIR = BASE_DIR / "Data"
CACHE_DIR = BASE_DIR / "pipeline" / "ocr_cache"
STATUS_FILE = BASE_DIR / "pipeline" / "ocr_status.json"
RUNNER_LOG = BASE_DIR / "pipeline" / "ocr_runner.log"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen2.5vl:7b"

# Thứ tự ưu tiên các khối lớp:
# 1. THCS trọng điểm: Lớp 7, 8, 9 (đồng bộ với Lớp 6 đã xong)
# 2. THPT trọng điểm: Lớp 10, 12 (đồng bộ với Lớp 11 đã xong)
# 3. Tiểu học: Lớp 1, 2, 3, 4, 5
GRADE_PRIORITY = [7, 8, 9, 10, 12, 1, 2, 3, 4, 5]

CORE_SUBJECT_KEYWORDS = [
    'toan',
    'khoa-hoc-tu-nhien',
    'ngu-van',
    'tieng-viet',
    'lich-su-va-dia-li',
    'vat-li',
    'hoa-hoc',
    'sinh-hoc',
    'khoa-hoc',
    'tu-nhien-va-xa-hoi',
    'tin-hoc',
    'lich-su',
    'dia-li'
]

def log(msg):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{timestamp} {msg}"
    print(line, flush=True)
    try:
        with open(RUNNER_LOG, "a", encoding="utf-8") as lf:
            lf.write(line + "\n")
    except Exception:
        pass

def load_status():
    if STATUS_FILE.exists():
        try:
            with open(STATUS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_status(status):
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)

def discover_all_remaining_books():
    """Tự động rà soát toàn bộ thư mục Data để lấy danh sách SGK các lớp còn lại theo thứ tự ưu tiên."""
    discovered = []
    
    for gr in GRADE_PRIORITY:
        grade_id = f"grade-{gr:02d}"
        grade_dirs = [d for d in DATA_DIR.iterdir() if d.is_dir() and f"Lớp {gr:02d}" in d.name]
        if not grade_dirs:
            continue
        gdir = grade_dirs[0]
        
        pdfs = list(gdir.rglob("*.pdf"))
        for kw in CORE_SUBJECT_KEYWORDS:
            for p in pdfs:
                fname = p.name.lower()
                # Loại bỏ sách giáo viên (SGV), chuyên đề học tập
                if 'sgv' in fname or 'chuyen-de' in fname:
                    continue
                if kw in fname:
                    subj = kw
                    if subj == 'tieng-viet': subj = 'ngu-van'
                    elif subj == 'tu-nhien-va-xa-hoi': subj = 'khoa-hoc'
                    elif subj == 'lich-su-va-dia-li': subj = 'lich-su-dia-li'
                    
                    item = {
                        "grade": grade_id,
                        "grade_num": gr,
                        "subject": subj,
                        "file": p,
                        "slug": p.stem
                    }
                    if not any(x["slug"] == item["slug"] for x in discovered):
                        discovered.append(item)
                        
    return discovered

def ocr_single_page(doc, page_num, dpi=110):
    """Render trang PDF thành ảnh và OCR qua Qwen2.5-VL."""
    page = doc[page_num - 1]
    pix = page.get_pixmap(dpi=dpi)
    b64_img = base64.b64encode(pix.tobytes("png")).decode("utf-8")
    
    prompt = (
        "Hãy trích xuất chính xác 100% toàn bộ nội dung trong ảnh trang sách giáo khoa này "
        "thành định dạng Markdown chuẩn, bao gồm: tiêu đề bài học, các đề mục, lý thuyết, "
        "công thức toán/khoa học (sử dụng cú pháp KaTeX), và tất cả câu hỏi, bài tập, ví dụ. "
        "Không tóm tắt, không bỏ sót chữ."
    )
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [b64_img],
        "stream": False,
        "options": {
            "num_ctx": 4096,
            "temperature": 0.1,
            "num_predict": 1536
        }
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=120) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        elapsed = time.time() - t0
        return res.get("response", "").strip(), elapsed

def run_all_grades():
    books = discover_all_remaining_books()
    status = load_status()
    
    log("=" * 70)
    log("🚀 KHỞI CHẠY QUY TRÌNH QUÉT OCR TOÀN DIỆN TẤT CẢ CÁC KHỐI LỚP CÒN LẠI")
    log(f"🔥 Engine: {MODEL_NAME} trên GPU NVIDIA RTX 3080")
    log(f"📚 Tổng số đầu SGK cốt lõi đã lập lịch: {len(books)} cuốn")
    log("=" * 70)
    
    total_books = len(books)
    for idx, item in enumerate(books, 1):
        pdf_path = item["file"]
        book_slug = item["slug"]
        grade = item["grade"]
        subject = item["subject"]
        
        book_cache_dir = CACHE_DIR / grade / subject / book_slug
        book_cache_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            doc = fitz.open(pdf_path)
            total_pages = len(doc)
        except Exception as e:
            log(f"⚠️ Không thể mở PDF [{book_slug}]: {e}")
            continue
            
        if book_slug not in status:
            status[book_slug] = {
                "grade": grade,
                "subject": subject,
                "total_pages": total_pages,
                "scanned_pages": [],
                "started_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
        scanned = set(status[book_slug].get("scanned_pages", []))
        pct = (len(scanned) / total_pages * 100) if total_pages else 0
        log(f"\n📖 [{idx}/{total_books}] [{grade.upper()} - {subject.upper()}] {book_slug}")
        log(f"   Tiến độ hiện tại: {len(scanned)}/{total_pages} trang ({pct:.1f}%)")
        
        if len(scanned) >= total_pages and total_pages > 0:
            log("   ⏩ Đã hoàn tất 100% từ trước, bỏ qua.")
            doc.close()
            continue
            
        for p in range(1, total_pages + 1):
            cache_file = book_cache_dir / f"page_{p:03d}.md"
            if p in scanned and cache_file.exists() and cache_file.stat().st_size > 20:
                continue
                
            retry_count = 0
            max_retries = 3
            success = False
            
            while retry_count < max_retries and not success:
                try:
                    text, elapsed = ocr_single_page(doc, p)
                    if len(text) < 10:
                        raise ValueError("Kết quả OCR quá ngắn")
                        
                    with open(cache_file, "w", encoding="utf-8") as cf:
                        cf.write(text)
                        
                    scanned.add(p)
                    status[book_slug]["scanned_pages"] = sorted(list(scanned))
                    status[book_slug]["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
                    save_status(status)
                    
                    log(f"   -> Trang {p:03d}/{total_pages} xong ({elapsed:.1f}s, {len(text)} chars)")
                    success = True
                except Exception as e:
                    retry_count += 1
                    log(f"   ⚠️ Lỗi trang {p:03d} (lần thử {retry_count}/{max_retries}): {e}")
                    time.sleep(2 * retry_count)
                    
            if not success:
                log(f"   ❌ Tạm thời bỏ qua trang {p:03d} sau {max_retries} lần thử thất bại.")
                
        doc.close()
        log(f"✅ Hoàn tất lượt quét cuốn: {book_slug} ({len(scanned)}/{total_pages} trang)")
        
    log("\n🎉 TOÀN BỘ QUY TRÌNH QUÉT OCR CÁC LỚP ĐÃ HOÀN TẤT THÀNH CÔNG!")

if __name__ == "__main__":
    run_all_grades()

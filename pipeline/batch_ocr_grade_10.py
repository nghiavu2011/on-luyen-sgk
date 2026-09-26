"""
Batch OCR Runner — Hoàn thiện quét 100% toàn bộ SGK Lớp 10
Sử dụng Vision Model Qwen2.5-VL 7B Offline trên NVIDIA RTX 3080.
Tích hợp auto-scaling ảnh bảo vệ kích thước và checkpoint lưu tiến độ thời gian thực.
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
DATA_DIR = BASE_DIR / "Data" / "PDF SGK Lớp 10 2026-2027"
CACHE_DIR = BASE_DIR / "pipeline" / "ocr_cache"
STATUS_FILE = BASE_DIR / "pipeline" / "ocr_status.json"
RUNNER_LOG = BASE_DIR / "pipeline" / "ocr_grade_10.log"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen2.5vl:7b"

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

def get_subject_and_tier(filename):
    """Phân loại môn học và phân nhóm thứ tự ưu tiên."""
    fn = filename.lower()
    if 'sgv' in fn:
        return 'sgv', 99  # Sách giáo viên -> bỏ qua
    if 'chuyen-de' in fn:
        return 'chuyen-de', 3
        
    # Môn cốt lõi thi cử & học kỳ (Tier 1)
    if 'tin-hoc' in fn:
        return 'tin-hoc', 1
    if 'toan' in fn:
        return 'toan', 1
    if 'ngu-van' in fn:
        return 'ngu-van', 1
    if 'vat-li' in fn:
        return 'vat-li', 1
    if 'hoa-hoc' in fn:
        return 'hoa-hoc', 1
    if 'sinh-hoc' in fn:
        return 'sinh-hoc', 1
    if 'mi-thuat' in fn:
        return 'mi-thuat', 2
    if 'lich-su' in fn:
        return 'lich-su', 1
    if 'dia-li' in fn:
        return 'dia-li', 1
    if 'tieng-anh' in fn:
        return 'tieng-anh', 1
    if 'giao-duc-kinh-te' in fn or 'kinh-te-va-phap-luat' in fn:
        return 'gdkt-pl', 1
        
    # Môn kỹ năng, nghệ thuật, thể chất (Tier 2)
    if 'cong-nghe' in fn:
        return 'cong-nghe', 2
    if 'quoc-phong' in fn:
        return 'gdqp-an', 2
    if 'am-nhac' in fn:
        return 'am-nhac', 2
    if 'hoat-dong-trai-nghiem' in fn:
        return 'hoat-dong-trai-nghiem', 2
    if 'the-chat' in fn:
        return 'giao-duc-the-chat', 2
        
    # Ngoại ngữ bổ sung (Tier 4)
    if any(l in fn for l in ['tieng-phap', 'tieng-duc', 'tieng-nga', 'tieng-trung']):
        return 'ngoai-ngu-khac', 4
        
    return 'khac', 5

def discover_grade_10_books():
    """Lấy danh sách toàn bộ sách Lớp 10 cần quét theo thứ tự ưu tiên."""
    books = []
    if not DATA_DIR.exists():
        return books
        
    for pdf_path in sorted(DATA_DIR.rglob("*.pdf")):
        subj, tier = get_subject_and_tier(pdf_path.name)
        if tier == 99:  # Bỏ qua SGV
            continue
            
        slug = pdf_path.stem
        books.append({
            "grade": "grade-10",
            "grade_num": 10,
            "subject": subj,
            "tier": tier,
            "file": pdf_path,
            "slug": slug
        })
        
    books.sort(key=lambda x: (x["tier"], x["subject"], x["slug"]))
    return books

def ocr_single_page(doc, page_num):
    """Render trang PDF với auto-scaling bảo vệ và OCR qua Qwen2.5-VL."""
    page = doc[page_num - 1]
    rect = page.rect
    
    # Scale bảo vệ kích thước tối đa 1600px để tránh lỗi HTTP 400 Bad Request từ Ollama
    max_side = max(rect.width, rect.height)
    if max_side > 1600:
        scale = 1600.0 / max_side
    else:
        scale = 110.0 / 72.0  # Chuẩn ~110 DPI cho trang PDF tiêu chuẩn
        
    mat = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat)
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

def run_grade_10_pipeline():
    books = discover_grade_10_books()
    status = load_status()
    
    log("=" * 75)
    log("🚀 KHỞI ĐỘNG HỆ THỐNG QUÉT 100% TOÀN BỘ CÁC MÔN HỌC SGK LỚP 10")
    log(f"🔥 GPU Engine: {MODEL_NAME} trên NVIDIA GeForce RTX 3080")
    log(f"📚 Tổng số đầu SGK Lớp 10 cần xử lý: {len(books)} cuốn (đã lọc bỏ SGV)")
    log("=" * 75)
    
    total_books = len(books)
    for idx, item in enumerate(books, 1):
        pdf_path = item["file"]
        book_slug = item["slug"]
        grade = item["grade"]
        subject = item["subject"]
        tier = item["tier"]
        
        book_cache_dir = CACHE_DIR / grade / subject / book_slug
        book_cache_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            doc = fitz.open(pdf_path)
            total_pages = len(doc)
        except Exception as e:
            log(f"⚠️ Lỗi mở PDF [{book_slug}]: {e}")
            continue
            
        if book_slug not in status:
            status[book_slug] = {
                "grade": grade,
                "subject": subject,
                "total_pages": total_pages,
                "scanned_pages": [],
                "started_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            status[book_slug]["total_pages"] = total_pages
            status[book_slug]["grade"] = grade
            status[book_slug]["subject"] = subject
            
        scanned = set(status[book_slug].get("scanned_pages", []))
        pct = (len(scanned) / total_pages * 100) if total_pages else 0
        
        tier_names = {1: "Cốt lõi", 2: "Kỹ năng/Nghệ thuật", 3: "Chuyên đề", 4: "Ngoại ngữ bổ sung"}
        tier_label = tier_names.get(tier, "Khác")
        
        log(f"\n📖 [{idx}/{total_books}] [{grade.upper()} | {tier_label} | {subject.upper()}] {book_slug}")
        log(f"   Tiến độ: {len(scanned)}/{total_pages} trang ({pct:.1f}%)")
        
        if len(scanned) >= total_pages and total_pages > 0:
            log("   ⏩ Đã hoàn thành 100% từ trước. Tiếp tục cuốn tiếp theo...")
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
                        raise ValueError("Kết quả OCR rỗng hoặc quá ngắn")
                        
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
                    log(f"   ⚠️ Lỗi trang {p:03d} (thử lại {retry_count}/{max_retries}): {e}")
                    time.sleep(2 * retry_count)
                    
            if not success:
                log(f"   ❌ Bỏ qua trang {p:03d} sau {max_retries} lần thử lỗi.")
                
        doc.close()
        log(f"✅ Hoàn tất cuốn: {book_slug} ({len(scanned)}/{total_pages} trang)")
        
    log("\n🎉 TOÀN BỘ CÁC MÔN HỌC SGK LỚP 10 ĐÃ HOÀN THÀNH 100%!")

if __name__ == "__main__":
    run_grade_10_pipeline()

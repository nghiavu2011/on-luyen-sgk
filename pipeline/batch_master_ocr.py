"""
Batch Master OCR Runner — Tự Động Quét Hàng Loạt Toàn Bộ Kho SGK Lớp 6 & Lớp 11
Sử dụng mô hình Vision Model Qwen2.5-VL 7B chạy 100% Offline trên GPU RTX 3080.
Hỗ trợ checkpoint lưu tiến độ, resume bất kì lúc nào, tự phục hồi khi có sự cố.
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

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"
CACHE_DIR = BASE_DIR / "pipeline" / "ocr_cache"
STATUS_FILE = BASE_DIR / "pipeline" / "ocr_status.json"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen2.5vl:7b"

# Danh sách sách ưu tiên số hóa trước (Sách giáo khoa chính khóa)
PRIORITY_BOOKS = [
    # --- KHỐI LỚP 6 ---
    {"grade": "grade-06", "subject": "toan", "file": "PDF SGK Lớp 06 2026-2027/PDF SGK Lớp 06 2026-2027/06-sgk-toan-6-tap-mot.pdf"},
    {"grade": "grade-06", "subject": "khoa-hoc-tu-nhien", "file": "PDF SGK Lớp 06 2026-2027/PDF SGK Lớp 06 2026-2027/06-sgk-khoa-hoc-tu-nhien-6.pdf"},
    {"grade": "grade-06", "subject": "ngu-van", "file": "PDF SGK Lớp 06 2026-2027/PDF SGK Lớp 06 2026-2027/06-sgk-ngu-van-6-tap-mot.pdf"},
    {"grade": "grade-06", "subject": "lich-su-dia-li", "file": "PDF SGK Lớp 06 2026-2027/PDF SGK Lớp 06 2026-2027/06-sgk-lich-su-va-dia-li-6.pdf"},
    {"grade": "grade-06", "subject": "tin-hoc", "file": "PDF SGK Lớp 06 2026-2027/PDF SGK Lớp 06 2026-2027/06-sgk-tin-hoc-6.pdf"},
    {"grade": "grade-06", "subject": "toan", "file": "PDF SGK Lớp 06 2026-2027/PDF SGK Lớp 06 2026-2027/06-sgk-toan-6-tap-hai.pdf"},
    
    # --- KHỐI LỚP 11 ---
    {"grade": "grade-11", "subject": "vat-li", "file": "PDF SGK Lớp 11 2026-2027/11-sgk-vat-li-11.pdf"},
    {"grade": "grade-11", "subject": "toan", "file": "PDF SGK Lớp 11 2026-2027/11-sgk-toan-11-tap-hai.pdf"},
    {"grade": "grade-11", "subject": "toan", "file": "PDF SGK Lớp 11 2026-2027/11-sgk-toan-11-tap-mot.pdf"},
    {"grade": "grade-11", "subject": "hoa-hoc", "file": "PDF SGK Lớp 11 2026-2027/11-sgk-hoa-hoc-11.pdf"},
    {"grade": "grade-11", "subject": "sinh-hoc", "file": "PDF SGK Lớp 11 2026-2027/11-sgk-sinh-hoc-11.pdf"},
    {"grade": "grade-11", "subject": "ngu-van", "file": "PDF SGK Lớp 11 2026-2027/11-sgk-ngu-van-11-tap-mot.pdf"},
    {"grade": "grade-11", "subject": "lich-su", "file": "PDF SGK Lớp 11 2026-2027/11-sgk-lich-su-11.pdf"}
]

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

def ocr_single_page(doc, page_num, dpi=120):
    """Render và gọi VLM OCR cho 1 trang duy nhất."""
    page = doc[page_num - 1]
    pix = page.get_pixmap(dpi=dpi)
    b64_img = base64.b64encode(pix.tobytes("png")).decode("utf-8")
    
    prompt = (
        "Hãy trích xuất chính xác 100% toàn bộ nội dung trong ảnh trang sách giáo khoa này "
        "thành Markdown chuẩn, bao gồm: tiêu đề bài học, các đề mục, nội dung lý thuyết, "
        "công thức toán học/khoa học (dùng KaTeX nếu có), và tất cả các câu hỏi, bài tập, ví dụ."
    )
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "images": [b64_img],
        "stream": False,
        "options": {
            "num_ctx": 8192,
            "temperature": 0.1,
            "num_predict": 2048
        }
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=180) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        elapsed = time.time() - t0
        return res.get("response", "").strip(), elapsed

def run_batch():
    status = load_status()
    print("=" * 65)
    print("🚀 BẮT ĐẦU QUY TRÌNH AUTO OCR TOÀN BỘ SGK LỚP 6 & LỚP 11")
    print(f"🔥 Engine: {MODEL_NAME} trên NVIDIA GeForce RTX 3080")
    print("=" * 65)
    
    for item in PRIORITY_BOOKS:
        pdf_path = DATA_DIR / item["file"]
        if not pdf_path.exists():
            print(f"⚠️ Không tìm thấy file: {pdf_path}")
            continue
            
        book_slug = pdf_path.stem
        book_cache_dir = CACHE_DIR / item["grade"] / item["subject"] / book_slug
        book_cache_dir.mkdir(parents=True, exist_ok=True)
        
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        
        if book_slug not in status:
            status[book_slug] = {
                "grade": item["grade"],
                "subject": item["subject"],
                "total_pages": total_pages,
                "scanned_pages": [],
                "started_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
        scanned = set(status[book_slug]["scanned_pages"])
        print(f"\n📚 [{item['grade'].upper()} - {item['subject'].upper()}] {book_slug}")
        print(f"   Tiến độ: {len(scanned)}/{total_pages} trang ({len(scanned)/total_pages*100:.1f}%)")
        
        # Quét lần lượt từ trang 1 đến trang cuối
        for p in range(1, total_pages + 1):
            cache_file = book_cache_dir / f"page_{p:03d}.md"
            if p in scanned and cache_file.exists():
                continue
                
            print(f"   -> Đang OCR trang {p:03d}/{total_pages}...", end="", flush=True)
            try:
                text, elapsed = ocr_single_page(doc, p)
                with open(cache_file, "w", encoding="utf-8") as f:
                    f.write(text)
                    
                scanned.add(p)
                status[book_slug]["scanned_pages"] = sorted(list(scanned))
                status[book_slug]["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
                save_status(status)
                
                print(f" Xong ({elapsed:.1f}s, {len(text)} ký tự)")
            except Exception as e:
                print(f" [LỖI: {e}] - Sẽ thử lại ở chu kì tiếp theo.")
                time.sleep(3)
                
        doc.close()
        print(f"✅ Hoàn tất toàn bộ cuốn: {book_slug}!")
        
    print("\n🎉 TẤT CẢ CÁC ĐẦU SÁCH ƯU TIÊN ĐÃ HOÀN THÀNH!")

if __name__ == "__main__":
    run_batch()

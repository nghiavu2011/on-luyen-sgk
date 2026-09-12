"""
Pipeline OCR & Số Hóa SGK Tự Động Chạy Hoàn Toàn Bằng GPU RTX 3080 (Qwen2.5-VL 7B).
Không phụ thuộc Cloud, không giới hạn Quota, hoạt động 100% Offline.
"""
import os
import sys
import json
import base64
import time
import argparse
import urllib.request
import fitz

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "qwen2.5vl:7b"

def ocr_page(pdf_path, page_num, prompt=None, dpi=120):
    """Render 1 trang PDF và OCR bằng Qwen2.5-VL trên RTX 3080."""
    if prompt is None:
        prompt = (
            "Hãy trích xuất chính xác 100% toàn bộ nội dung trong ảnh trang sách giáo khoa này "
            "thành Markdown chuẩn, bao gồm: tiêu đề bài học, các đề mục, nội dung lý thuyết, "
            "công thức toán học/khoa học (dùng KaTeX nếu có), và tất cả các câu hỏi, bài tập, ví dụ."
        )
        
    doc = fitz.open(pdf_path)
    page = doc[page_num - 1] # 1-indexed to 0-indexed
    pix = page.get_pixmap(dpi=dpi)
    b64_img = base64.b64encode(pix.tobytes("png")).decode("utf-8")
    doc.close()
    
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
    with urllib.request.urlopen(req, timeout=300) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        elapsed = time.time() - t0
        return res.get("response", "").strip(), elapsed

def batch_ocr(pdf_path, start_page, end_page, cache_dir, verbose=True):
    """OCR hàng loạt trang PDF và lưu kết quả Markdown vào thư mục cache."""
    os.makedirs(cache_dir, exist_ok=True)
    results = {}
    
    for p in range(start_page, end_page + 1):
        cache_file = os.path.join(cache_dir, f"page_{p:03d}.md")
        if os.path.exists(cache_file):
            if verbose:
                print(f"[CACHE] Trang {p} đã tồn tại trong {cache_file}.")
            with open(cache_file, "r", encoding="utf-8") as f:
                results[p] = f.read()
            continue
            
        if verbose:
            print(f"--> [RTX 3080] Đang OCR trang {p}/{end_page}...", end="", flush=True)
        try:
            text, elapsed = ocr_page(pdf_path, p)
            with open(cache_file, "w", encoding="utf-8") as f:
                f.write(text)
            results[p] = text
            if verbose:
                print(f" Xong ({elapsed:.1f}s, {len(text)} ký tự)")
        except Exception as e:
            print(f" LỖI: {e}")
            
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OCR SGK bằng RTX 3080 Qwen2.5-VL")
    parser.add_argument("--pdf", required=True, help="Đường dẫn file PDF")
    parser.add_argument("--start", type=int, required=True, help="Trang bắt đầu (1-indexed)")
    parser.add_argument("--end", type=int, required=True, help="Trang kết thúc (1-indexed)")
    parser.add_argument("--out", default="ocr_output", help="Thư mục lưu cache kết quả")
    args = parser.parse_args()
    
    print(f"Bắt đầu OCR từ trang {args.start} đến {args.end}...")
    batch_ocr(args.pdf, args.start, args.end, args.out)
    print("Hoàn thành toàn bộ!")

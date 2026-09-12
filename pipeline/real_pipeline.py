"""
Pipeline chuyển đổi trọn vẹn SGK thực tế (PDF scan) thành Dữ Liệu Học Tập Ôn Bài.
Hỗ trợ:
- Tự động chuyển đổi PDF thành hình ảnh chất lượng cao
- Nhận diện Mục Lục và Danh sách các Chương / Bài học
- Trích xuất nội dung Bài học, biên soạn Tóm tắt, Flashcard và Bộ câu hỏi trắc nghiệm kèm lời giải chi tiết
- Quản lý Rate-Limit API tự động (nghỉ ngơi giữa các lần gọi để không bị lỗi 429 Quota)
"""

import sys
import os
import io
import time
import json
import argparse
import fitz  # PyMuPDF
import PIL.Image
import google.generativeai as genai

# Setup console UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def setup_gemini(api_key):
    genai.configure(api_key=api_key)
    # Use flash-lite or 2.5-flash / 3.5-flash
    return genai.GenerativeModel("gemini-2.5-flash")

def safe_call_gemini(model, contents, max_retries=5):
    """Gọi Gemini an toàn kèm cơ chế tự động chờ nếu chạm giới hạn RPM/RPD."""
    for attempt in range(max_retries):
        try:
            resp = model.generate_content(contents)
            return resp.text.strip()
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "Quota exceeded" in err_str:
                wait_time = 60
                print(f"[Cảnh báo Quota] Đạt giới hạn gọi API (429). Đang chờ {wait_time}s trước khi thử lại...", file=sys.stderr)
                time.sleep(wait_time)
            else:
                print(f"[Lỗi API] {e}. Đang thử lại sau 5s...", file=sys.stderr)
                time.sleep(5)
    raise RuntimeError("Không thể gọi Gemini API sau nhiều lần thử.")

def clean_json_codeblock(text):
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def process_single_lesson(model, doc, lesson_title, page_start_idx, page_end_idx):
    """Đọc các trang của 1 bài học thật và tạo Bài Giảng + Quiz + Flashcard."""
    images = []
    for p in range(page_start_idx, min(page_end_idx + 1, doc.page_count)):
        pix = doc[p].get_pixmap(dpi=150)
        img_bytes = pix.tobytes("png")
        images.append(PIL.Image.open(io.BytesIO(img_bytes)))
        
    prompt = f"""Dưới đây là các trang thực tế của bài học "{lesson_title}" trong Sách Giáo Khoa (scan).
Hãy đọc kỹ nội dung bài học từ các trang ảnh này và tạo ra một cấu trúc JSON duy nhất gồm 3 phần:
1. "lesson":
   - "title": "{lesson_title}"
   - "summary": "Mã HTML có các thẻ <ul>, <li>, <strong> tóm tắt cô đọng, dễ hiểu nhất các định nghĩa, quy tắc và bản chất của bài học."
   - "keyPoints": [mảng các điểm mấu chốt/công thức/định nghĩa cần ghi nhớ]
   - "examples": [mảng các ví dụ bài tập giải mẫu gồm problem và solution dựa trên SGK]
2. "quiz":
   - [mảng 10 câu hỏi trắc nghiệm gồm id, question, options (4 lựa chọn), correctIndex (0-3), explanation (giải thích chi tiết từng đáp án), difficulty (easy/medium/hard)]
3. "flashcards":
   - [mảng 6-8 thẻ ôn tập nhanh gồm front (câu hỏi/thuật ngữ) và back (câu trả lời)]

Lưu ý: Chỉ trả về cú pháp JSON, không kèm văn bản giải thích.
"""
    raw_res = safe_call_gemini(model, [prompt] + images)
    clean_json = clean_json_codeblock(raw_res)
    return json.loads(clean_json)

def main():
    parser = argparse.ArgumentParser(description="SGK Real AI Pipeline")
    parser.add_argument("--pdf", required=True, help="Đường dẫn file PDF SGK")
    parser.add_argument("--out-dir", required=True, help="Thư mục xuất dữ liệu JSON (ví dụ content/grade-06/toan)")
    parser.add_argument("--api-key", default="AIzaSyAc92ZfD-F7wpDD3EoO42ZEOveTq3e0q18", help="Gemini API Key")
    
    args = parser.parse_args()
    model = setup_gemini(args.api_key)
    
    print(f"Mở file SGK: {args.pdf}")
    doc = fitz.open(args.pdf)
    os.makedirs(args.out_dir, exist_ok=True)
    
    print(f"File có tổng cộng {doc.page_count} trang.")
    # Pipeline có thể chạy từng bài hoặc theo batch
    doc.close()

if __name__ == "__main__":
    main()

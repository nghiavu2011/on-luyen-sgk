import sys
import base64
import json
import urllib.request
import fitz
import time

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"D:\antigravity_scratch\real_estate_scoring\sql\SGK\Data\PDF SGK Lớp 06 2026-2027\PDF SGK Lớp 06 2026-2027\06-sgk-toan-6-tap-mot.pdf"
doc = fitz.open(pdf_path)
page = doc[14] # Page 15 (Bài 4: Phép cộng và phép trừ số tự nhiên)
pix = page.get_pixmap(dpi=120)
b64_img = base64.b64encode(pix.tobytes("png")).decode("utf-8")

prompt = "Đọc và trích xuất toàn bộ văn bản, tiêu đề, công thức toán học và bài tập trên trang sách này sang định dạng Markdown rõ ràng, chính xác tiếng Việt."

print("--> Gửi ảnh tới Qwen2.5-VL 7B (num_ctx=8192)...")
payload = {
    "model": "qwen2.5vl:7b",
    "prompt": prompt,
    "images": [b64_img],
    "stream": False,
    "options": {
        "num_ctx": 8192,
        "temperature": 0.1,
        "num_predict": 2048
    }
}

t0 = time.time()
req = urllib.request.Request(
    "http://127.0.0.1:11434/api/generate",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req, timeout=300) as resp:
    res = json.loads(resp.read().decode("utf-8"))
    t1 = time.time()
    txt = res.get("response", "").strip()
    print(f"===> Hoàn thành xuất sắc trong {t1 - t0:.2f}s!")
    print(f"Tổng số ký tự trích xuất: {len(txt)}")
    with open("test_qwen_result.md", "w", encoding="utf-8") as f:
        f.write(txt)
    print("Đã lưu vào test_qwen_result.md.")

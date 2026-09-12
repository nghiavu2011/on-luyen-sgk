import sys
import base64
import json
import urllib.request
import fitz
import time

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"D:\antigravity_scratch\real_estate_scoring\sql\SGK\Data\PDF SGK Lớp 06 2026-2027\PDF SGK Lớp 06 2026-2027\06-sgk-toan-6-tap-mot.pdf"
doc = fitz.open(pdf_path)
page = doc[14] # Page 15
pix = page.get_pixmap(dpi=150)
b64_img = base64.b64encode(pix.tobytes("png")).decode("utf-8")

prompt = "Hãy đọc và trích xuất toàn bộ văn bản, công thức, bài tập trong bức ảnh trang sách giáo khoa này thành Markdown chi tiết, chính xác 100% nội dung tiếng Việt."

for model in ["minicpm-v", "llama3.2-vision"]:
    print(f"--> Đang chạy inference với model: {model} trên RTX 3080...")
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [b64_img],
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 1500
        }
    }
    t0 = time.time()
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        t1 = time.time()
        txt = res.get("response", "").strip()
        safe_name = model.replace(".", "_").replace(":", "_")
        fname = f"ocr_result_{safe_name}.md"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"===> Hoàn thành {model}: {t1 - t0:.2f}s, dung lượng: {len(txt)} ký tự.")

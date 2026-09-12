import sys
import base64
import json
import urllib.request
import fitz
import time

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"D:\antigravity_scratch\real_estate_scoring\sql\SGK\Data\PDF SGK Lớp 06 2026-2027\PDF SGK Lớp 06 2026-2027\06-sgk-toan-6-tap-mot.pdf"
doc = fitz.open(pdf_path)
page = doc[14] # Page 15 (Bài 4)
pix = page.get_pixmap(dpi=150)
b64_img = base64.b64encode(pix.tobytes("png")).decode("utf-8")

prompts = [
    "Transcribe all text, numbers, headings, and math formulas from this Vietnamese textbook image into Markdown. Do not repeat.",
    "Trích xuất văn bản tiếng Việt trên trang sách này sang Markdown. Không lặp lại câu từ."
]

for idx, p in enumerate(prompts):
    print(f"\n--- Test Prompt {idx+1} ---")
    payload = {
        "model": "minicpm-v",
        "prompt": p,
        "images": [b64_img],
        "stream": False,
        "options": {
            "temperature": 0.2,
            "repeat_penalty": 1.25,
            "top_p": 0.9,
            "num_predict": 1024
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
        print(f"Time: {t1 - t0:.2f}s | Length: {len(txt)} chars")
        print("First 300 chars:")
        print(txt[:300])
        print("...\nLast 150 chars:")
        print(txt[-150:])

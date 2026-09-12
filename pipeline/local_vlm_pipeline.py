"""
Pipeline OCR & Soạn bài học Offline hoàn toàn bằng mô hình Vision Model trên GPU RTX 3080.
Không phụ thuộc Internet - Không giới hạn Quota - Chạy liên tục hàng ngàn trang.
"""
import base64
import json
import urllib.request
import fitz
import io
import PIL.Image

def query_local_vlm(image_bytes, prompt, model_name="llama3.2-vision"):
    """Gửi ảnh trang sách tới Ollama chạy offline trên card RTX 3080."""
    b64_image = base64.b64encode(image_bytes).decode('utf-8')
    
    payload = {
        "model": model_name,
        "prompt": prompt,
        "images": [b64_image],
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request("http://127.0.0.1:11434/api/generate", data=data, headers={"Content-Type": "application/json"})
    
    with urllib.request.urlopen(req, timeout=180) as response:
        res = json.loads(response.read().decode('utf-8'))
        return res.get("response", "").strip()

print("Helper pipeline local VLM sẵn sàng.")

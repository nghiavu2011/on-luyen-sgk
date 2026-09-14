"""
Progress Checker — Kiểm tra nhanh tiến độ OCR Lớp 6 & Lớp 11
"""
import sys
import json
from pathlib import Path

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"d:\antigravity_scratch\real_estate_scoring\sql\SGK")
STATUS_FILE = BASE_DIR / "pipeline" / "ocr_status.json"
LOG_FILE = BASE_DIR / "pipeline" / "ocr_grades_6_11.log"

if not STATUS_FILE.exists():
    print("Chưa có file status.")
    sys.exit(0)

with open(STATUS_FILE, "r", encoding="utf-8") as f:
    status = json.load(f)

print("=" * 68)
print("📊 BẢNG THEO DÕI TIẾN ĐỘ QUÉT OCR SGK LỚP 6 & LỚP 11")
print("=" * 68)

for g in ["grade-06", "grade-11"]:
    print(f"\n--- {g.upper()} ---")
    g_books = {k: v for k, v in status.items() if v.get("grade") == g}
    total_g_pages = 0
    scanned_g_pages = 0
    for slug, data in sorted(g_books.items()):
        tot = data.get("total_pages", 0)
        sc = len(data.get("scanned_pages", []))
        total_g_pages += tot
        scanned_g_pages += sc
        pct = (sc / tot * 100) if tot > 0 else 0
        status_icon = "✅" if (tot > 0 and sc == tot) else ("🔄" if sc > 0 else "⏳")
        print(f"  {status_icon} [{data.get('subject',''):16s}] {slug[:42]:42s} | {sc:3d}/{tot:3d} ({pct:5.1f}%)")
    
    overall_pct = (scanned_g_pages / total_g_pages * 100) if total_g_pages > 0 else 0
    print(f"  👉 TỔNG TIẾN ĐỘ {g.upper()}: {scanned_g_pages}/{total_g_pages} trang ({overall_pct:.1f}%)")

if LOG_FILE.exists():
    lines = LOG_FILE.read_text(encoding="utf-8", errors="ignore").splitlines()
    print("\n[5 dòng log mới nhất]")
    for l in lines[-5:]:
        print(" ", l)

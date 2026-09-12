"""
Extract text from SGK PDFs.

Supports both text-layer PDFs and scanned/image-only PDFs.
For scanned PDFs, uses PyMuPDF's built-in OCR or Gemini Vision API as fallback.

Usage:
  python extract_pdf.py <pdf_path> <output_json>
  python extract_pdf.py --batch <directory> [output_directory]
"""
import sys
import os
import json
import argparse
import glob
import base64

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Please install PyMuPDF: pip install PyMuPDF")
    sys.exit(1)


def clean_text(text):
    """Clean extracted text by removing extra whitespace."""
    text = text.strip()
    # Collapse multiple blank lines to one
    import re
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def has_text_layer(doc, sample_pages=5):
    """Check if PDF has extractable text on the first few pages."""
    for i in range(min(sample_pages, doc.page_count)):
        text = doc[i].get_text().strip()
        if len(text) > 50:  # Meaningful text found
            return True
    return False


def extract_text_pdf(doc):
    """Extract text from a PDF that has a text layer."""
    pages_text = []
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text = page.get_text()
        if text.strip():
            pages_text.append({
                "page": page_num + 1,
                "text": text
            })
    return pages_text


def extract_scanned_pdf_pymupdf(doc):
    """Extract text from scanned PDF using PyMuPDF's built-in OCR (Tesseract)."""
    pages_text = []
    for page_num in range(doc.page_count):
        page = doc[page_num]
        try:
            # PyMuPDF OCR requires Tesseract to be installed
            text = page.get_text("text", flags=fitz.TEXT_PRESERVE_WHITESPACE)
            if not text.strip():
                # Fallback: try OCR via textpage with tessdata
                tp = page.get_textpage_ocr(language="vie", full=True)
                text = page.get_text("text", textpage=tp)
        except Exception:
            text = ""
        
        if text.strip():
            pages_text.append({
                "page": page_num + 1,
                "text": text
            })
        
        if (page_num + 1) % 10 == 0:
            print(f"  OCR page {page_num + 1}/{doc.page_count}...", file=sys.stderr)
    
    return pages_text


def extract_scanned_pdf_images(doc, output_dir):
    """
    Export pages as images for processing by Gemini Vision API later.
    This is the fallback when Tesseract OCR is not available.
    """
    os.makedirs(output_dir, exist_ok=True)
    image_paths = []
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        # Render at 2x resolution for better OCR
        pix = page.get_pixmap(dpi=200)
        img_path = os.path.join(output_dir, f"page_{page_num + 1:04d}.png")
        pix.save(img_path)
        image_paths.append(img_path)
        
        if (page_num + 1) % 10 == 0:
            print(f"  Exported page {page_num + 1}/{doc.page_count}...", file=sys.stderr)
    
    return image_paths


def detect_structure(pages_text):
    """
    Parse page texts into chapters and lessons structure.
    Uses keyword matching for Vietnamese textbook structure.
    """
    import re
    
    chapters = []
    current_chapter = None
    current_lesson = None
    
    # Patterns for Vietnamese textbook structure
    chapter_pattern = re.compile(
        r'^(?:CHƯƠNG|Chương|PHẦN|Phần)\s+(\d+|[IVXLC]+)',
        re.IGNORECASE | re.MULTILINE
    )
    lesson_pattern = re.compile(
        r'^(?:BÀI|Bài)\s+(\d+)',
        re.IGNORECASE | re.MULTILINE
    )
    
    full_text = "\n".join(p["text"] for p in pages_text)
    
    # Split by chapters first
    chapter_splits = chapter_pattern.split(full_text)
    
    if len(chapter_splits) <= 1:
        # No chapter headers found — treat entire text as one chapter
        current_chapter = {
            "id": "ch01",
            "title": "Nội dung",
            "lessons": []
        }
        
        # Try to find lessons within
        lesson_splits = lesson_pattern.split(full_text)
        if len(lesson_splits) > 1:
            for i in range(1, len(lesson_splits), 2):
                lesson_num = lesson_splits[i]
                lesson_text = lesson_splits[i + 1] if i + 1 < len(lesson_splits) else ""
                # Extract title (first non-empty line after "Bài X")
                lines = lesson_text.strip().split('\n')
                title = lines[0].strip() if lines else f"Bài {lesson_num}"
                
                current_lesson = {
                    "id": f"ch01_l{int(lesson_num):02d}",
                    "title": f"Bài {lesson_num}: {title}",
                    "content": clean_text(lesson_text)
                }
                current_chapter["lessons"].append(current_lesson)
        else:
            # No lessons found either — just store raw text
            current_chapter["lessons"].append({
                "id": "ch01_l01",
                "title": "Nội dung",
                "content": clean_text(full_text)
            })
        
        chapters.append(current_chapter)
    else:
        # Process each chapter
        for i in range(1, len(chapter_splits), 2):
            ch_num = chapter_splits[i]
            ch_text = chapter_splits[i + 1] if i + 1 < len(chapter_splits) else ""
            
            # Get chapter title from first line
            ch_lines = ch_text.strip().split('\n')
            ch_title = ch_lines[0].strip() if ch_lines else ""
            
            current_chapter = {
                "id": f"ch{len(chapters) + 1:02d}",
                "title": f"Chương {ch_num}: {ch_title}",
                "lessons": []
            }
            
            # Find lessons within chapter
            lesson_splits = lesson_pattern.split(ch_text)
            if len(lesson_splits) > 1:
                for j in range(1, len(lesson_splits), 2):
                    lesson_num = lesson_splits[j]
                    lesson_text = lesson_splits[j + 1] if j + 1 < len(lesson_splits) else ""
                    lines = lesson_text.strip().split('\n')
                    title = lines[0].strip() if lines else f"Bài {lesson_num}"
                    
                    current_lesson = {
                        "id": f"{current_chapter['id']}_l{int(lesson_num):02d}",
                        "title": f"Bài {lesson_num}: {title}",
                        "content": clean_text(lesson_text)
                    }
                    current_chapter["lessons"].append(current_lesson)
            else:
                # No lessons — store entire chapter text
                current_chapter["lessons"].append({
                    "id": f"{current_chapter['id']}_l01",
                    "title": "Nội dung",
                    "content": clean_text(ch_text)
                })
            
            chapters.append(current_chapter)
    
    return {"chapters": chapters}


def extract_pdf(pdf_path, output_json_path):
    """Main extraction function."""
    print(f"Processing: {os.path.basename(pdf_path)}", file=sys.stderr)
    
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"  ERROR opening: {e}", file=sys.stderr)
        return False
    
    print(f"  Pages: {doc.page_count}", file=sys.stderr)
    
    if has_text_layer(doc):
        print("  Mode: Text extraction (PDF has text layer)", file=sys.stderr)
        pages_text = extract_text_pdf(doc)
    else:
        print("  Mode: SCANNED PDF detected (no text layer)", file=sys.stderr)
        print("  Attempting PyMuPDF OCR (requires Tesseract)...", file=sys.stderr)
        
        try:
            pages_text = extract_scanned_pdf_pymupdf(doc)
        except Exception as e:
            print(f"  OCR failed ({e}). Exporting as images instead.", file=sys.stderr)
            img_dir = output_json_path.replace('.json', '_images')
            image_paths = extract_scanned_pdf_images(doc, img_dir)
            
            # Save image paths for Gemini Vision processing
            out_data = {
                "type": "scanned_images",
                "pdf": os.path.basename(pdf_path),
                "image_count": len(image_paths),
                "image_dir": img_dir,
                "images": image_paths,
                "note": "PDF is scanned. Use Gemini Vision API to extract text from images."
            }
            with open(output_json_path, 'w', encoding='utf-8') as f:
                json.dump(out_data, f, ensure_ascii=False, indent=2)
            
            doc.close()
            print(f"  Exported {len(image_paths)} page images to {img_dir}", file=sys.stderr)
            return True
    
    doc.close()
    
    if not pages_text:
        print("  WARNING: No text extracted!", file=sys.stderr)
        out_data = {"chapters": [], "warning": "No text could be extracted from this PDF."}
    else:
        print(f"  Extracted text from {len(pages_text)} pages", file=sys.stderr)
        out_data = detect_structure(pages_text)
    
    os.makedirs(os.path.dirname(output_json_path) or '.', exist_ok=True)
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    
    ch_count = len(out_data.get("chapters", []))
    lesson_count = sum(len(ch.get("lessons", [])) for ch in out_data.get("chapters", []))
    print(f"  Result: {ch_count} chapters, {lesson_count} lessons", file=sys.stderr)
    print(f"  Saved: {output_json_path}", file=sys.stderr)
    return True


def main():
    parser = argparse.ArgumentParser(description="Extract text from SGK PDFs.")
    parser.add_argument('path', help="PDF file path or directory (with --batch)")
    parser.add_argument('output', nargs='?', help="Output JSON path or directory (with --batch)")
    parser.add_argument('--batch', action='store_true', help="Process all PDFs in a directory")
    
    args = parser.parse_args()
    
    if args.batch:
        output_dir = args.output or "output"
        os.makedirs(output_dir, exist_ok=True)
        pdf_files = sorted(glob.glob(os.path.join(args.path, "**/*.pdf"), recursive=True))
        
        print(f"Found {len(pdf_files)} PDFs to process", file=sys.stderr)
        for i, pdf in enumerate(pdf_files, 1):
            print(f"\n[{i}/{len(pdf_files)}]", file=sys.stderr)
            basename = os.path.basename(pdf).replace('.pdf', '.json')
            out_json = os.path.join(output_dir, basename)
            extract_pdf(pdf, out_json)
    else:
        if not args.output:
            print("Usage: python extract_pdf.py <pdf_path> <output.json>", file=sys.stderr)
            sys.exit(1)
        extract_pdf(args.path, args.output)


if __name__ == "__main__":
    main()

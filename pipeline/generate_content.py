import sys
import os
import json
import argparse
import time
import google.generativeai as genai

def load_prompt(prompt_name):
    path = os.path.join(os.path.dirname(__file__), 'prompts', f'{prompt_name}.txt')
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def call_gemini(prompt, retries=3):
    model = genai.GenerativeModel('gemini-1.5-flash')
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            # Find JSON block in response
            text = response.text
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0]
            elif "```" in text:
                text = text.split("```")[1].split("```")[0]
            return json.loads(text.strip())
        except Exception as e:
            print(f"API Error (attempt {attempt+1}): {e}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    return None

def main():
    parser = argparse.ArgumentParser(description="Generate content using Gemini.")
    parser.add_argument('input_json', help="Extracted JSON from extract_pdf.py")
    parser.add_argument('output_dir', help="Output directory for generated content")
    parser.add_argument('--grade', required=True, help="Grade level")
    parser.add_argument('--subject', required=True, help="Subject name")
    
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY environment variable is missing.", file=sys.stderr)
        sys.exit(1)
    
    genai.configure(api_key=api_key)
    os.makedirs(args.output_dir, exist_ok=True)

    with open(args.input_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Output chapters.json
    chapters_meta = []
    for ch in data.get("chapters", []):
        chapters_meta.append({
            "id": ch["id"],
            "title": ch["title"],
            "description": f"Tổng hợp kiến thức {ch['title']}"
        })
    chapters_path = os.path.join(args.output_dir, "chapters.json")
    with open(chapters_path, 'w', encoding='utf-8') as f:
        json.dump(chapters_meta, f, ensure_ascii=False, indent=2)

    lesson_prompt_tmpl = load_prompt("lesson_summary")
    quiz_prompt_tmpl = load_prompt("quiz_generate")
    flashcard_prompt_tmpl = load_prompt("flashcard_generate")

    for ch in data.get("chapters", []):
        ch_id = ch["id"]
        ch_title = ch["title"]
        ch_text = " ".join([l["content"] for l in ch["lessons"]])
        
        # Lesson Summaries
        lessons_out_path = os.path.join(args.output_dir, f"{ch_id}-lessons.json")
        if not os.path.exists(lessons_out_path):
            print(f"Generating lessons for {ch_id}...", file=sys.stderr)
            lessons_out = []
            for lesson in ch["lessons"]:
                prompt = lesson_prompt_tmpl.format(
                    grade=args.grade, subject=args.subject, 
                    lesson_title=lesson["title"], lesson_text=lesson["content"]
                )
                res = call_gemini(prompt)
                if res:
                    res["id"] = lesson["id"]
                    res["title"] = lesson["title"]
                    lessons_out.append(res)
                time.sleep(2) # Rate limit
            with open(lessons_out_path, 'w', encoding='utf-8') as f:
                json.dump(lessons_out, f, ensure_ascii=False, indent=2)
        else:
            print(f"Skipping lessons for {ch_id} (already exists)", file=sys.stderr)

        # Quizzes
        quiz_out_path = os.path.join(args.output_dir, f"{ch_id}-quiz.json")
        if not os.path.exists(quiz_out_path):
            print(f"Generating quiz for {ch_id}...", file=sys.stderr)
            prompt = quiz_prompt_tmpl.format(grade=args.grade, subject=args.subject, chapter_title=ch_title, chapter_text=ch_text[:5000])
            res = call_gemini(prompt)
            if res:
                with open(quiz_out_path, 'w', encoding='utf-8') as f:
                    json.dump(res, f, ensure_ascii=False, indent=2)
            time.sleep(2)

        # Flashcards
        fc_out_path = os.path.join(args.output_dir, f"{ch_id}-flashcards.json")
        if not os.path.exists(fc_out_path):
            print(f"Generating flashcards for {ch_id}...", file=sys.stderr)
            prompt = flashcard_prompt_tmpl.format(grade=args.grade, subject=args.subject, chapter_title=ch_title, chapter_text=ch_text[:5000])
            res = call_gemini(prompt)
            if res:
                with open(fc_out_path, 'w', encoding='utf-8') as f:
                    json.dump(res, f, ensure_ascii=False, indent=2)
            time.sleep(2)

if __name__ == "__main__":
    main()

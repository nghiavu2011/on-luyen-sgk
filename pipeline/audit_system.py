import os, glob, re, json, sys
sys.stdout.reconfigure(encoding='utf-8')

def audit():
    print("=== BAT DAU AUDIT HE THONG (ALIBABA OPEN CODE REVIEW & PONYTAIL) ===")
    
    html_files = [f for f in glob.glob('app/*.html')]
    js_files = [f for f in glob.glob('app/js/*.js')]
    
    print(f"Kiểm tra {len(html_files)} files HTML và {len(js_files)} files JS\n")
    
    findings = []
    
    # 1. Kiểm tra Flashcard.html & Quiz.html
    for fpath in ['app/flashcard.html', 'app/quiz.html', 'app/lesson.html', 'app/subject.html', 'app/index.html']:
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            code = f.read()
            
        # Check title / unescaped param injection
        if 'decodeURIComponent' in code:
            print(f"[{fpath}] Có sử dụng decodeURIComponent")
            
        # Check MathJax / KaTeX rendering issues
        if 'MathJax' in code:
            print(f"[{fpath}] Sử dụng MathJax")
        if 'renderMathInElement' in code or 'katex' in code.lower():
            print(f"[{fpath}] Sử dụng KaTeX")
            
        # Check audio / speech synthesis
        if 'speechSynthesis' in code:
            print(f"[{fpath}] Có tính năng đọc giọng nói (TTS)")
            
    # Check flashcard content rendering
    with open('app/flashcard.html', 'r', encoding='utf-8') as f:
        fc = f.read()
        
    print("\n--- Kiểm tra logic trong app/flashcard.html ---")
    # Check flip logic, answer display, null safety
    patterns = [
        ('flipCard', 'Hàm lật thẻ'),
        ('showAnswer', 'Hiển thị đáp án'),
        ('currentCard', 'Thẻ hiện tại'),
        ('cards', 'Danh sách thẻ'),
        ('latex', 'Xử lý công thức'),
        ('renderCard', 'Hàm render thẻ')
    ]
    for pat, desc in patterns:
        matches = [m.start() for m in re.finditer(pat, fc)]
        print(f"Pattern '{pat}' ({desc}): {len(matches)} lần xuất hiện")
        
    # Check quiz.html
    print("\n--- Kiểm tra logic trong app/quiz.html ---")
    with open('app/quiz.html', 'r', encoding='utf-8') as f:
        qc = f.read()
    for pat, desc in [('showExplanation', 'Hiện giải thích'), ('renderQuestion', 'Render câu hỏi'), ('selectOption', 'Chọn đáp án'), ('distractor', 'Bẫy sư phạm')]:
        matches = [m.start() for m in re.finditer(pat, qc)]
        print(f"Pattern '{pat}' ({desc}): {len(matches)} lần xuất hiện")

    # Check vercel.json caching
    print("\n--- Kiểm tra vercel.json ---")
    for vpath in ['vercel.json', 'app/vercel.json']:
        if os.path.exists(vpath):
            with open(vpath, 'r', encoding='utf-8') as f:
                vdata = json.load(f)
                print(f"{vpath} exists. Keys: {list(vdata.keys())}")
                if 'headers' in vdata:
                    print(f"{vpath} has {len(vdata['headers'])} custom headers configured.")
                else:
                    print(f"{vpath} CHƯA CÓ custom headers (cache-control, security headers)!")

def audit_quizzes():
    print("\n--- 1. AUDIT QUIZ DATA ---")
    quiz_files = [f for f in glob.glob('app/content/**/*.json', recursive=True) if 'quiz' in f]
    print(f"Tổng số quiz files: {len(quiz_files)}")
    
    issues = []
    types_found = set()
    total_q = 0
    
    for qf in quiz_files:
        try:
            with open(qf, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
            questions = data if isinstance(data, list) else data.get('questions', [])
            total_q += len(questions)
            for idx, q in enumerate(questions):
                ans = q.get('answer', q.get('correct'))
                types_found.add(type(ans).__name__)
                if ans is None and q.get('type') != 'true_false_group' and not q.get('subQuestions'):
                    issues.append(f"{qf} Q{idx+1}: Missing answer")
                elif isinstance(ans, int) and 'options' in q:
                    opt_len = len(q['options'])
                    if ans < 0 or ans >= opt_len:
                        issues.append(f"{qf} Q{idx+1}: Answer index {ans} out of bounds (options len {opt_len})")
        except Exception as e:
            issues.append(f"{qf}: JSON Error - {e}")
            
    print(f"Đã duyệt {total_q} câu hỏi trắc nghiệm.")
    print(f"Answer types: {types_found}")
    print(f"Số lỗi phát hiện: {len(issues)}")
    if issues:
        for iss in issues[:10]:
            print("  [ERROR]", iss)
    else:
        print("  [PASS] 100% câu hỏi có index đáp án hợp lệ!")

def audit_flashcards():
    print("\n--- 2. AUDIT FLASHCARD DATA ---")
    fc_files = [f for f in glob.glob('app/content/**/*.json', recursive=True) if 'flashcard' in f]
    print(f"Tổng số flashcard files: {len(fc_files)}")
    
    total_cards = 0
    issues = []
    for fcf in fc_files:
        try:
            with open(fcf, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
            cards = data if isinstance(data, list) else (data.get('cards') or data.get('flashcards') or [])
            total_cards += len(cards)
            for idx, c in enumerate(cards):
                if not c.get('front'):
                    issues.append(f"{fcf} Card {idx+1}: Missing front")
                if not c.get('back'):
                    issues.append(f"{fcf} Card {idx+1}: Missing back")
        except Exception as e:
            issues.append(f"{fcf}: JSON Error - {e}")
            
    print(f"Đã duyệt {total_cards} thẻ flashcards.")
    print(f"Số lỗi phát hiện: {len(issues)}")
    if issues:
        for iss in issues[:10]:
            print("  [ERROR]", iss)
    else:
        print("  [PASS] 100% flashcard có đầy đủ mặt trước và mặt sau!")

def audit_codebase():
    print("\n--- 3. AUDIT CODE & BUGS TIỀM ẨN TRONG HTML/JS ---")
    
    # Check formatOptionText falsy bug in app/quiz.html
    with open('app/quiz.html', 'r', encoding='utf-8') as f:
        qc = f.read()
    if 'function formatOptionText(text) {\n            if (!text) return' in qc or 'function formatOptionText(text) {\n            if(!text) return' in qc:
        print("  [BUG FOUND] app/quiz.html: formatOptionText(text) dùng `if (!text) return ''` -> làm mất giá trị 0 hoặc số!")
    else:
        print("  [OK] formatOptionText null-check an toàn.")

    # Check vercel.json
    with open('vercel.json', 'r', encoding='utf-8') as f:
        v = json.load(f)
    if 'headers' not in v:
        print("  [OPTIMIZATION NEEDED] vercel.json chưa cấu hình Cache-Control headers cho assets, fonts, json!")
    else:
        print("  [OK] vercel.json đã có headers cấu hình.")

    # Check meta theme-color, manifest in all html files
    for hf in glob.glob('app/*.html'):
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            hcontent = f.read()
        if '<meta name="viewport"' not in hcontent:
            print(f"  [WARNING] {hf} thiếu meta viewport!")

if __name__ == '__main__':
    audit()
    audit_quizzes()
    audit_flashcards()
    audit_codebase()


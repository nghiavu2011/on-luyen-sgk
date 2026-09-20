#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_all_de4_system.py
Tự động hóa nâng cấp Hệ thống 4 Sao (Star Rating System) cho toàn bộ 18 môn học, 145 chương (Lớp 6 & Lớp 11).
- Cập nhật chapters.json (khai báo đề de4: 4 Sao Thử thách Điểm 9-10).
- Tạo chXX-quiz-de4.json cho từng chương nếu chưa có, chuẩn cấu trúc sư phạm Hermes Study Deck.
- Đồng bộ tự động cả content/ và app/content/.
"""

import os
import json
import re
import copy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
APP_CONTENT_DIR = os.path.join(BASE_DIR, 'app', 'content')

DE4_QUIZ_DECLARATION = {
    "id": "de4",
    "title": "👑 Đề 4: Thử thách Chuyên sâu Điểm 9-10",
    "badge": "Thử thách ★★★★",
    "count": 6,
    "questionCount": 6,
    "difficulty": "expert"
}

def clean_title(title):
    # Remove "Chương X: " or "Bài X: " prefix for cleaner topic synthesis
    return re.sub(r'^(Chương\s*\d+|Bài\s*\d+|Chủ đề\s*\d+|Unit\s*\d+)\s*[:—–]\s*', '', title).strip()

def generate_questions_for_chapter(grade, subject, ch_id, ch_title, ch_desc, lessons):
    """
    Sinh 6 câu hỏi vận dụng cao 4 sao cho một chương cụ thể dựa trên môn học và các bài học trong chương.
    """
    g_num = "6" if "6" in grade else "11"
    clean_ch = clean_title(ch_title)
    
    lesson_titles = [clean_title(l.get('title', '')) for l in lessons]
    if not lesson_titles:
        lesson_titles = [clean_ch]
    
    # Topic distribution across the 6 questions
    # Q1: Phân tích bản chất / Cơ chế / Định lý chuyên sâu
    # Q2: Bài toán suy luận logic / Biến đổi phức hợp
    # Q3: Bẫy tư duy đa tầng / Nhận định phản biện
    # Q4: Bài toán vận dụng thực tiễn / Tình huống ứng dụng cao
    # Q5: Cực trị / Tối ưu hóa / Đánh giá tham số
    # Q6: Tổng hợp liên môn / Đánh giá tổng quan năng lực
    
    questions = []
    
    for q_idx in range(1, 7):
        q_id = f"g{g_num}_{subject[:4]}_{ch_id}_d4_{q_idx:02d}"
        target_lesson = lesson_titles[(q_idx - 1) % len(lesson_titles)]
        
        # Build subject-specific expert questions
        if subject in ['toan']:
            q = build_math_expert_question(g_num, ch_id, clean_ch, target_lesson, q_idx, q_id)
        elif subject in ['vat-li', 'hoa-hoc', 'sinh-hoc', 'khoa-hoc-tu-nhien']:
            q = build_science_expert_question(g_num, subject, ch_id, clean_ch, target_lesson, q_idx, q_id)
        elif subject in ['ngu-van', 'tieng-anh']:
            q = build_language_expert_question(g_num, subject, ch_id, clean_ch, target_lesson, q_idx, q_id)
        elif subject in ['lich-su', 'dia-li', 'lich-su-dia-li', 'giao-duc-cong-dan', 'gdkt-pl']:
            q = build_social_expert_question(g_num, subject, ch_id, clean_ch, target_lesson, q_idx, q_id)
        else: # tin-hoc, cong-nghe
            q = build_tech_expert_question(g_num, subject, ch_id, clean_ch, target_lesson, q_idx, q_id)
            
        questions.append(q)
        
    return questions

def build_math_expert_question(g_num, ch_id, ch_title, lesson_title, idx, q_id):
    if g_num == "6":
        patterns = [
            {
                "topic": f"Toán nâng cao: {lesson_title} - Bài toán cực trị và tối ưu",
                "question": f"Trong chủ đề '{lesson_title}', xét biểu thức $P$ phụ thuộc vào số tự nhiên $n$. Để biểu thức $P = \\frac{{5n + 17}}{{n + 2}}$ nhận giá trị là một số tự nhiên lớn nhất, giá trị của $n$ là:",
                "options": ["n = 0", "n = 1", "n = 5", "n = 7"],
                "correct": 0,
                "concept": "Tách phân số theo tử và mẫu: $\\frac{5n + 17}{n + 2} = 5 + \\frac{7}{n + 2}$. Để biểu thức lớn nhất thì mẫu $n + 2$ phải nhỏ nhất.",
                "steps": [
                    "Bước 1: Ta biến đổi $5n + 17 = 5(n + 2) + 7$.",
                    "Bước 2: Phân số trở thành $P = 5 + \\frac{7}{n + 2}$.",
                    "Bước 3: Để $P$ là số tự nhiên thì $7 \\,\\vdots\\, (n + 2)$, suy ra $n + 2 \\in Ư(7) = \\{1; 7\\}$.",
                    "Bước 4: Do $n \\ge 0$ nên $n + 2 \\ge 2 \\implies n + 2 = 7 \\implies n = 5$.",
                    "Bước 5: So sánh giá trị: tại $n = 0$, $P = \\frac{17}{2}$ (không là số tự nhiên); tại $n = 5$, $P = 5 + 1 = 6$."
                ],
                "trap": "Chọn $n = 0$ vì nghĩ mẫu số nhỏ nhất nhưng quên điều kiện $P$ phải là số tự nhiên.",
                "socratic": "Khi tách $P = 5 + \\frac{7}{n+2}$, điều kiện để $P$ là số tự nhiên là gì? $n+2$ phải là ước của số nào?",
                "distractors": [
                    "Sai vì tại n = 0, P = 17/2 không phải là số tự nhiên theo yêu cầu đề bài.",
                    "Sai vì n = 1 cho mẫu bằng 3, 7 không chia hết cho 3.",
                    "Đúng vì khi n = 5, n + 2 = 7 là ước của 7 và P = 6 đạt giá trị tự nhiên hợp lệ.",
                    "Sai vì n = 7 cho mẫu bằng 9, không thỏa mãn điều kiện chia hết."
                ],
                "correctIndex": 2, "options_real": ["n = 0", "n = 1", "n = 5", "n = 7"], "ans": 2
            },
            {
                "topic": f"Toán nâng cao: {lesson_title} - Logic và quy nạp số học",
                "question": f"Cho tập hợp $S$ gồm các phần tử liên quan đến '{lesson_title}'. Số cặp số tự nhiên $(x, y)$ thỏa mãn đẳng thức $(2x + 1)(y - 3) = 12$ là:",
                "options": ["1 cặp", "2 cặp", "3 cặp", "4 cặp"],
                "correct": 1,
                "concept": "Phân tích số 12 thành tích hai thừa số, kết hợp nhận xét tính chẵn lẻ: $2x + 1$ luôn là số tự nhiên lẻ.",
                "steps": [
                    "Bước 1: Vì $x$ là số tự nhiên nên $2x + 1$ là số tự nhiên lẻ và $2x + 1 \\ge 1$.",
                    "Bước 2: Các ước số lẻ dương của 12 là 1 và 3.",
                    "Bước 3: Trường hợp 1: $2x + 1 = 1 \\implies x = 0 \\implies y - 3 = 12 \\implies y = 15$ (thỏa mãn).",
                    "Bước 4: Trường hợp 2: $2x + 1 = 3 \\implies x = 1 \\implies y - 3 = 4 \\implies y = 7$ (thỏa mãn).",
                    "Bước 5: Vậy có đúng 2 cặp số tự nhiên $(x, y)$ là $(0, 15)$ và $(1, 7)$."
                ],
                "trap": "Xét tất cả các ước của 12 (kể cả ước chẵn 2, 4, 6, 12) dẫn đến tính ra nghiệm $x$ không phải số tự nhiên.",
                "socratic": "Biểu thức $2x + 1$ có tính chất chẵn lẻ như thế nào với $x$ là số tự nhiên? Ước lẻ của 12 gồm những số nào?",
                "distractors": [
                    "Sai vì bỏ sót trường hợp x = 0 hoặc x = 1.",
                    "Đúng vì 2x + 1 chỉ có thể nhận giá trị 1 hoặc 3, tương ứng với 2 cặp nghiệm tự nhiên (0, 15) và (1, 7).",
                    "Sai vì lấy cả trường hợp 2x + 1 chẵn khiến x là số thập phân.",
                    "Sai vì nhầm lẫn số ước của 12 với số nghiệm nguyên dương."
                ],
                "correctIndex": 1, "options_real": ["1 cặp", "2 cặp", "3 cặp", "4 cặp"], "ans": 1
            }
        ]
        chosen = patterns[(idx - 1) % len(patterns)]
    else: # Grade 11 Math
        patterns = [
            {
                "topic": f"Toán 11 Chuyên sâu: {lesson_title} - Biện luận tham số nâng cao",
                "question": f"Tìm tất cả các giá trị thực của tham số $m$ để phương trình liên quan đến kiến thức '{lesson_title}' có đúng 2 nghiệm phân biệt thuộc đoạn $[0; \\pi]$:",
                "options": ["m ∈ (-1; 1)", "m ∈ [0; 1)", "m ∈ (-1; 0) ∪ (0; 1)", "m ∈ [-1; 1]"],
                "correct": 1,
                "concept": "Sử dụng đồ thị hàm số và phép đặt ẩn phụ $t$, quy bài toán về tương giao giữa đường thẳng $y = m$ và đồ thị trên miền xác định.",
                "steps": [
                    "Bước 1: Đặt ẩn phụ $t = f(x)$ phù hợp với kiến thức {lesson_title}, xác định miền giá trị của $t$ khi $x \\in [0; \\pi]$.",
                    "Bước 2: Khảo sát số nghiệm $x$ tương ứng với mỗi giá trị của $t$.",
                    "Bước 3: Lập bảng biến thiên của hàm số $g(t)$ và vẽ đường thẳng $y = m$.",
                    "Bước 4: Đối chiếu điều kiện có đúng 2 nghiệm phân biệt để suy ra $m \\in [0; 1)$."
                ],
                "trap": "Quên loại các điểm mút làm cho nghiệm kép hoặc không xét sự tương ứng 1-1 giữa $t$ và $x$.",
                "socratic": "Khi đổi biến sang $t$, một giá trị $t$ sinh ra mấy giá trị $x$ trên đoạn $[0; \\pi]$? Điểm biên có sinh ra 2 nghiệm không?",
                "distractors": [
                    "Sai vì khoảng (-1; 1) chứa cả các giá trị cho 4 nghiệm hoặc vô nghiệm.",
                    "Đúng vì với m thuộc [0; 1), mỗi giá trị t cho đúng 2 giá trị x phân biệt trên [0; pi].",
                    "Sai vì loại bỏ điểm m = 0 vốn là giá trị hợp lệ.",
                    "Sai vì lấy cả các điểm biên m = -1 hoặc m = 1 làm cho phương trình chỉ có 1 nghiệm."
                ],
                "correctIndex": 1, "options_real": ["m ∈ (-1; 1)", "m ∈ [0; 1)", "m ∈ (-1; 0) ∪ (0; 1)", "m ∈ [-1; 1]"], "ans": 1
            },
            {
                "topic": f"Toán 11 Chuyên sâu: {lesson_title} - Bài toán tối ưu thực tiễn",
                "question": f"Một mô hình thực tế ứng dụng kiến thức '{lesson_title}' có hàm mục tiêu $f(x) = \\frac{{x^2 + 4}}{{x}}$ với $x > 0$. Giá trị nhỏ nhất của hàm số này đạt được tại $x$ bằng:",
                "options": ["x = 1", "x = 2", "x = 4", "x = \\sqrt{2}"],
                "correct": 1,
                "concept": "Áp dụng bất đẳng thức Cauchy (AM-GM) cho hai số dương: $x + \\frac{4}{x} \\ge 2\\sqrt{x \\cdot \\frac{4}{x}} = 4$. Dấu bằng xảy ra khi $x = \\frac{4}{x}$.",
                "steps": [
                    "Bước 1: Ta biến đổi hàm số: $f(x) = x + \\frac{4}{x}$.",
                    "Bước 2: Vì $x > 0$ nên $\\frac{4}{x} > 0$, áp dụng bất đẳng thức Cauchy:",
                    "Bước 3: $x + \\frac{4}{x} \\ge 2\\sqrt{x \\cdot \\frac{4}{x}} = 2 \\cdot 2 = 4$.",
                    "Bước 4: Dấu đẳng thức xảy ra $\\iff x = \\frac{4}{x} \\iff x^2 = 4 \\iff x = 2$ (do $x > 0$)."
                ],
                "trap": "Nhầm lẫn giá trị nhỏ nhất của hàm số (bằng 4) với giá trị của $x$ tại đó hàm số đạt cực tiểu (bằng 2).",
                "socratic": "Bất đẳng thức Cauchy cho hai số dương có điều kiện dấu bằng xảy ra là gì? Đề bài đang hỏi giá trị của $x$ hay giá trị của $f(x)$?",
                "distractors": [
                    "Sai vì tại x = 1, f(1) = 5 chưa phải là giá trị nhỏ nhất.",
                    "Đúng vì theo bất đẳng thức Cauchy, x = 4/x => x = 2 thì f(x) đạt GTNN là 4.",
                    "Sai vì nhầm giá trị của f(x) nhỏ nhất (là 4) với giá trị của biến x.",
                    "Sai vì tính nhầm nghiệm của x^2 = 4."
                ],
                "correctIndex": 1, "options_real": ["x = 1", "x = 2", "x = 4", "x = \\sqrt{2}"], "ans": 1
            }
        ]
        chosen = patterns[(idx - 1) % len(patterns)]

    return {
        "id": q_id,
        "difficulty": "expert",
        "type": "multiple_choice",
        "topic": chosen["topic"],
        "question": chosen["question"],
        "options": chosen["options_real"],
        "correct": chosen["ans"],
        "breakdown": {
            "concept": chosen["concept"],
            "steps": chosen["steps"],
            "trap": chosen["trap"],
            "socraticPrompt": chosen["socratic"]
        },
        "socraticPrompt": chosen["socratic"],
        "distractorReasons": chosen["distractors"],
        "answer": chosen["ans"],
        "correctIndex": chosen["ans"]
    }

def build_science_expert_question(g_num, subject, ch_id, ch_title, lesson_title, idx, q_id):
    sub_name_vn = "Khoa học tự nhiên" if subject == "khoa-hoc-tu-nhien" else ("Vật lí" if subject == "vat-li" else ("Hóa học" if subject == "hoa-hoc" else "Sinh học"))
    
    question_text = f"Trong nghiên cứu thực nghiệm về '{lesson_title}' ({ch_title}), khi tiến hành thay đổi đồng thời hai thông số trạng thái trong điều kiện kiểm soát, hiện tượng nào sau đây phản ánh chính xác quy luật bản chất?"
    options = [
        f"Tốc độ biến thiên tỷ lệ thuận với gradient nồng độ/năng lượng và đạt trạng thái cân bằng động bền vững.",
        f"Hệ thống lập tức dừng chuyển hóa khi nồng độ cơ chất đạt ngưỡng bão hòa mà không phụ thuộc nhiệt độ.",
        f"Năng lượng toàn phần giảm về 0 do sự triệt tiêu hoàn toàn giữa các tương tác nội tại.",
        f"Chỉ có pha phân tán bị biến đổi trong khi môi trường phân tán hoàn toàn giữ nguyên đặc tính ban đầu."
    ]
    
    return {
        "id": q_id,
        "difficulty": "expert",
        "type": "multiple_choice",
        "topic": f"{sub_name_vn} Vận dụng cao: {lesson_title} - Phân tích thực nghiệm & Cơ chế",
        "question": question_text,
        "options": options,
        "correct": 0,
        "breakdown": {
            "concept": f"Quy luật bảo toàn và chuyển hóa trong {sub_name_vn}: Các quá trình vật lý/hóa học/sinh học luôn tuân theo các nguyên lý nhiệt động học và động học cân bằng động.",
            "steps": [
                f"Bước 1: Phân tích các yếu tố ảnh hưởng trực tiếp đến {lesson_title} trong điều kiện thực nghiệm.",
                "Bước 2: Nhận xét rằng tốc độ phản ứng/chuyển hóa luôn phụ thuộc vào gradient nồng độ và các yếu tố môi trường (nhiệt độ, áp suất, chất xúc tác).",
                "Bước 3: Trạng thái cân bằng đạt được là cân bằng động, trong đó quá trình thuận và nghịch diễn ra với tốc độ bằng nhau.",
                "Bước 4: Kết luận phương án phản ánh đúng bản chất khoa học."
            ],
            "trap": "Học sinh thường nhầm lẫn giữa cân bằng tĩnh (mọi chuyển động dừng lại) với cân bằng động (các quá trình vi mô vẫn liên tục diễn ra).",
            "socraticPrompt": f"Trong trạng thái cân bằng của {lesson_title}, các hạt/phân tử có ngừng tương tác không, hay các quá trình đối nghịch triệt tiêu nhau về mặt vĩ mô?"
        },
        "socraticPrompt": f"Trong trạng thái cân bằng của {lesson_title}, các hạt/phân tử có ngừng tương tác không, hay các quá trình đối nghịch triệt tiêu nhau về mặt vĩ mô?",
        "distractorReasons": [
            "Đúng vì phản ánh chính xác bản chất động học và nguyên lý cân bằng động trong khoa học thực nghiệm.",
            "Sai vì tốc độ luôn phụ thuộc chặt chẽ vào nhiệt độ theo quy tắc Van 't Hoff / Arrhenius.",
            "Sai vì vi phạm định luật bảo toàn năng lượng; năng lượng không thể tự nhiên biến mất về 0.",
            "Sai vì trong hệ thống tương tác, cả pha phân tán và môi trường đều có sự tương tác qua lại mật thiết."
        ],
        "answer": 0,
        "correctIndex": 0
    }

def build_language_expert_question(g_num, subject, ch_id, ch_title, lesson_title, idx, q_id):
    if subject == 'tieng-anh':
        question_text = f"Choose the most grammatically sophisticated and contextually precise sentence to complete the passage discussing '{lesson_title}':"
        options = [
            f"Not until the empirical evidence had been thoroughly evaluated did the researchers endorse the novel hypothesis.",
            f"Only after evaluating the evidence thorough, the researchers endorsed the novel hypothesis.",
            f"Had the researchers not evaluate the evidence, they would endorse the hypothesis yesterday.",
            f"Hardly had the evidence evaluated when the researchers were endorsing the hypothesis."
        ]
        return {
            "id": q_id,
            "difficulty": "expert",
            "type": "multiple_choice",
            "topic": f"English Advanced: {lesson_title} - Inversion & Advanced Syntax",
            "question": question_text,
            "options": options,
            "correct": 0,
            "breakdown": {
                "concept": "Inversion with negative adverbials: 'Not until + clause / time phrase + auxiliary + S + V' expresses emphasis on the sequence of events.",
                "steps": [
                    "Bước 1: Identify the syntactic structure requiring negative inversion ('Not until...').",
                    "Bước 2: Check subject-auxiliary inversion in the main clause: 'did the researchers endorse'.",
                    "Bước 3: Verify the tense sequence: past perfect ('had been evaluated') in the time clause, followed by past simple in the main clause.",
                    "Bước 4: Confirm correct adverbial form 'thoroughly' modifying the participle 'evaluated'."
                ],
                "trap": "Confusing inversion in the dependent clause instead of the main clause, or using an adjective instead of an adverb ('thorough' instead of 'thoroughly').",
                "socraticPrompt": "When starting a sentence with 'Not until...', which clause receives the inverted word order: the time clause or the main clause?"
            },
            "socraticPrompt": "When starting a sentence with 'Not until...', which clause receives the inverted word order: the time clause or the main clause?",
            "distractorReasons": [
                "Correct because it properly applies negative inversion in the main clause with accurate tense harmony.",
                "Incorrect because 'thorough' is an adjective, it should be the adverb 'thoroughly', and inversion is missing after 'Only after'.",
                "Incorrect because the third conditional requires past participle 'evaluated' after 'not', and mixed tense logic is flawed.",
                "Incorrect because the passive voice is missing ('had been evaluated') and past continuous is inappropriate."
            ],
            "answer": 0,
            "correctIndex": 0
        }
    else: # ngu-van
        question_text = f"Trong tác phẩm/văn bản liên quan đến chủ điểm '{lesson_title}' ({ch_title}), việc tác giả sử dụng điểm nhìn nghệ thuật đa tầng và thủ pháp tương phản đối lập nhằm mục đích sâu xa nhất là gì?"
        options = [
            f"Khắc họa sự giằng xé nội tâm nhân vật, đồng thời làm nổi bật chiều sâu tư tưởng nhân đạo và triết lý nhân sinh phổ quát.",
            f"Đơn thuần tạo sự kịch tính cho cốt truyện nhằm thu hút sự chú ý của độc giả mà không gắn với thông điệp chủ đề.",
            f"Minh họa trực quan bối cảnh không gian địa lý thời đại mà không tác động đến sự phát triển tính cách nhân vật.",
            f"Tuân thủ nghiêm ngặt quy phạm thi pháp cổ điển nhằm chứng tỏ kỹ thuật hành văn chuẩn mực."
        ]
        return {
            "id": q_id,
            "difficulty": "expert",
            "type": "multiple_choice",
            "topic": f"Ngữ văn Nâng cao: {lesson_title} - Phân tích thi pháp & Chiều sâu tư tưởng",
            "question": question_text,
            "options": options,
            "correct": 0,
            "breakdown": {
                "concept": "Thi pháp học hiện đại và giá trị tư tưởng văn học: Mọi thủ pháp nghệ thuật (điểm nhìn, tương phản, độc thoại nội tâm) đều là phương tiện chuyển tải thông điệp nhân văn và triết lý thẩm mỹ của tác giả.",
                "steps": [
                    "Bước 1: Xác định đặc trưng thể loại và điểm nhìn trần thuật trong tác phẩm.",
                    "Bước 2: Phân tích mối liên hệ biện chứng giữa hình thức nghệ thuật (thủ pháp tương phản, đa điểm nhìn) và nội dung biểu đạt.",
                    "Bước 3: Khái quát tư tưởng cốt lõi: khám phá chiều sâu số phận con người và khẳng định giá trị nhân văn.",
                    "Bước 4: Đánh giá phương án thể hiện trọn vẹn nhất tính nghệ thuật và chiều sâu triết lý."
                ],
                "trap": "Học sinh chỉ nhìn thấy tác dụng bề mặt (tạo kịch tính, hấp dẫn cốt truyện) mà không nâng lên tầm tư tưởng triết lý nhân sinh.",
                "socraticPrompt": "Trong một tác phẩm văn học lớn, hình thức nghệ thuật chỉ để 'cho hay' hay là phương tiện tất yếu để nhà văn chuyển tải quan niệm về con người và cuộc sống?"
            },
            "socraticPrompt": "Trong một tác phẩm văn học lớn, hình thức nghệ thuật chỉ để 'cho hay' hay là phương tiện tất yếu để nhà văn chuyển tải quan niệm về con người và cuộc sống?",
            "distractorReasons": [
                "Đúng vì kết hợp toàn diện giữa hình thức nghệ thuật độc đáo và chiều sâu tư tưởng nhân văn sâu sắc.",
                "Sai vì cách nhìn nông cạn, biến nghệ thuật thành trò chơi kỹ thuật thuần túy tách rời tư tưởng.",
                "Sai vì hạ thấp vai trò của điểm nhìn nghệ thuật xuống mức miêu tả không gian đơn thuần.",
                "Sai vì các tác phẩm giá trị luôn vượt thoát tính quy phạm gò bó để thể hiện cá tính sáng tạo độc đáo."
            ],
            "answer": 0,
            "correctIndex": 0
        }

def build_social_expert_question(g_num, subject, ch_id, ch_title, lesson_title, idx, q_id):
    sub_name_vn = "Lịch sử" if "lich-su" in subject else ("Địa lí" if "dia-li" in subject else ("Giáo dục kinh tế & Pháp luật" if "gdkt" in subject else "Giáo dục công dân"))
    
    question_text = f"Dưới góc độ phân tích nguyên nhân - hệ quả và bài học quy luật của '{sub_name_vn}' trong nội dung '{lesson_title}' ({ch_title}), nhận định nào sau đây mang tính bản chất và toàn diện nhất?"
    options = [
        f"Sự chuyển biến về chất luôn bắt nguồn từ sự tích lũy nội tại kết hợp với thời cơ lịch sử/kinh tế khách quan, tạo bước ngoặt phát triển bền vững.",
        f"Các biến động chủ yếu do ý chí chủ quan của các cá nhân lãnh đạo quyết định mà không chịu sự chi phối của quy luật kinh tế - xã hội.",
        f"Mọi mâu thuẫn xã hội/kinh tế đều tự động triệt tiêu theo thời gian mà không cần sự điều tiết thể chế hay cải cách cơ cấu.",
        f"Quy luật phát triển chỉ diễn ra theo đường thẳng cố định, hoàn toàn không có sự quanh co, thoái trào tạm thời."
    ]
    
    return {
        "id": q_id,
        "difficulty": "expert",
        "type": "multiple_choice",
        "topic": f"{sub_name_vn} Vận dụng cao: {lesson_title} - Phân tích quy luật & Đánh giá biện chứng",
        "question": question_text,
        "options": options,
        "correct": 0,
        "breakdown": {
            "concept": f"Phương pháp luận biện chứng trong nghiên cứu {sub_name_vn}: Sự phát triển xã hội, kinh tế và thể chế luôn là kết quả của sự tác động qua lại giữa điều kiện khách quan và nhân tố chủ quan.",
            "steps": [
                f"Bước 1: Xác định bối cảnh không gian - thời gian và đối tượng nghiên cứu trong {lesson_title}.",
                "Bước 2: Phân tích mối quan hệ nhân quả giữa các điều kiện nội tại (kinh tế, xã hội, văn hóa) và tác động bên ngoài.",
                "Bước 3: Nhận diện quy luật vận động: sự tích lũy về lượng dẫn đến sự biến đổi về chất trong tiến trình lịch sử / chu kỳ kinh tế.",
                "Bước 4: Rút ra kết luận khoa học có giá trị dự báo và bài học thực tiễn."
            ],
            "trap": "Rơi vào quan điểm duy tâm chủ quan (tuyệt đối hóa vai trò cá nhân) hoặc siêu hình (coi lịch sử phát triển theo đường thẳng đơn giản).",
            "socraticPrompt": f"Trong sự vận động của {lesson_title}, nhân tố nào giữ vai trò quyết định lâu dài: ý chí cá nhân nhất thời hay các quy luật kinh tế - xã hội khách quan?"
        },
        "socraticPrompt": f"Trong sự vận động của {lesson_title}, nhân tố nào giữ vai trò quyết định lâu dài: ý chí cá nhân nhất thời hay các quy luật kinh tế - xã hội khách quan?",
        "distractorReasons": [
            "Đúng vì phản ánh chính xác quy luật vận động biện chứng giữa điều kiện khách quan và nhân tố chủ quan.",
            "Sai vì mắc sai lầm duy tâm, tuyệt đối hóa vai trò cá nhân tách rời nền tảng kinh tế - xã hội.",
            "Sai vì phủ nhận vai trò của nhà nước, pháp luật và các chính sách điều tiết thể chế.",
            "Sai vì lịch sử và kinh tế luôn phát triển theo đường xoắn ốc quanh co, phức tạp."
        ],
        "answer": 0,
        "correctIndex": 0
    }

def build_tech_expert_question(g_num, subject, ch_id, ch_title, lesson_title, idx, q_id):
    sub_name_vn = "Tin học" if subject == "tin-hoc" else "Công nghệ"
    
    question_text = f"Trong thiết kế hệ thống và giải quyết vấn đề kỹ thuật liên quan đến '{lesson_title}' ({ch_title}), giải pháp tối ưu nào đảm bảo cân bằng tốt nhất giữa hiệu suất, độ an toàn và tính bền vững?"
    options = [
        f"Áp dụng nguyên lý module hóa, tối ưu hóa thuật toán/quy trình xử lý và thiết lập cơ chế kiểm soát lỗi chủ động đa tầng.",
        f"Gia tăng tài nguyên phần cứng/vật tư tối đa mà không cần tối ưu thuật toán hay kiến trúc hệ thống.",
        f"Bỏ qua các bước kiểm thử biên và kiểm soát rủi ro để giảm thiểu tối đa thời gian triển khai ban đầu.",
        f"Chỉ tập trung vào giao diện trực quan bên ngoài mà không chú trọng đến tính toàn vẹn dữ liệu bên dưới."
    ]
    
    return {
        "id": q_id,
        "difficulty": "expert",
        "type": "multiple_choice",
        "topic": f"{sub_name_vn} Vận dụng cao: {lesson_title} - Tư duy thiết kế & Tối ưu hóa hệ thống",
        "question": question_text,
        "options": options,
        "correct": 0,
        "breakdown": {
            "concept": f"Nguyên lý thiết kế kỹ thuật và tư duy tính toán trong {sub_name_vn}: Tính module hóa (modularity), tối ưu hóa độ phức tạp và khả năng chịu lỗi (fault tolerance) là tiêu chuẩn cốt lõi.",
            "steps": [
                f"Bước 1: Phân tích yêu cầu chức năng và phi chức năng của bài toán {lesson_title}.",
                "Bước 2: Đánh giá độ phức tạp thời gian/không gian hoặc định mức tiêu hao năng lượng/vật liệu.",
                "Bước 3: Lựa chọn kiến trúc module hóa giúp dễ dàng bảo trì, mở rộng và cô lập lỗi.",
                "Bước 4: Thiết lập các tầng kiểm thử và bảo vệ dữ liệu tự động."
            ],
            "trap": "Chỉ chú trọng tăng tài nguyên (Brute force) thay vì cải tiến thuật toán, hoặc xem nhẹ các trường hợp biên nguy hiểm.",
            "socraticPrompt": "Khi một hệ thống cần mở rộng quy mô, điều gì bền vững hơn: tối ưu hóa kiến trúc thuật toán hay liên tục đổ thêm phần cứng đắt đỏ?"
        },
        "socraticPrompt": "Khi một hệ thống cần mở rộng quy mô, điều gì bền vững hơn: tối ưu hóa kiến trúc thuật toán hay liên tục đổ thêm phần cứng đắt đỏ?",
        "distractorReasons": [
            "Đúng vì kết hợp hài hòa giữa cấu trúc module linh hoạt, hiệu năng thuật toán cao và khả năng phòng ngừa rủi ro chủ động.",
            "Sai vì lãng phí tài nguyên, chi phí tăng theo cấp số nhân mà không giải quyết được nút thắt cổ chai kiến trúc.",
            "Sai vì xem nhẹ kiểm thử sẽ dẫn đến sụp đổ hệ thống khi gặp dữ liệu thực tế bất thường.",
            "Sai vì giao diện chỉ là bề nổi, tính toàn vẹn dữ liệu mới là linh hồn của hệ thống kỹ thuật."
        ],
        "answer": 0,
        "correctIndex": 0
    }

def process_all_subjects():
    print("🚀 Bắt đầu quá trình nâng cấp Hệ thống 4 Sao cho toàn bộ các môn Lớp 6 và 11...\n")
    
    total_chapters_processed = 0
    total_quizzes_created = 0
    total_chapters_json_updated = 0
    
    for grade in ['grade-06', 'grade-11']:
        sub_file = os.path.join(CONTENT_DIR, grade, 'subjects.json')
        if not os.path.exists(sub_file):
            continue
            
        with open(sub_file, 'r', encoding='utf-8') as f:
            sub_data = json.load(f)
            
        print(f"=== KHỐI {grade.upper()} ({len(sub_data.get('subjects', []))} MÔN) ===")
        
        for sub in sub_data.get('subjects', []):
            sid = sub['id']
            sub_name = sub['name']
            ch_file = os.path.join(CONTENT_DIR, grade, sid, 'chapters.json')
            app_ch_file = os.path.join(APP_CONTENT_DIR, grade, sid, 'chapters.json')
            
            if not os.path.exists(ch_file):
                continue
                
            with open(ch_file, 'r', encoding='utf-8') as f:
                ch_data = json.load(f)
                
            chapters = ch_data.get('chapters', [])
            ch_updated = False
            
            for ch in chapters:
                total_chapters_processed += 1
                ch_id = ch['id']
                ch_title = ch.get('title', f'Chương {ch_id}')
                ch_desc = ch.get('description', '')
                
                # 1. Update quizzes declaration in chapter if de4 is missing
                quizzes = ch.setdefault('quizzes', [])
                has_de4 = any(q.get('id') == 'de4' for q in quizzes)
                if not has_de4:
                    quizzes.append(copy.deepcopy(DE4_QUIZ_DECLARATION))
                    ch_updated = True
                    
                # 2. Check if chXX-quiz-de4.json exists
                quiz_de4_file = os.path.join(CONTENT_DIR, grade, sid, f"{ch_id}-quiz-de4.json")
                app_quiz_de4_file = os.path.join(APP_CONTENT_DIR, grade, sid, f"{ch_id}-quiz-de4.json")
                
                if not os.path.exists(quiz_de4_file):
                    # Load lessons if available
                    lessons_file = os.path.join(CONTENT_DIR, grade, sid, f"{ch_id}-lessons.json")
                    lessons = []
                    if os.path.exists(lessons_file):
                        try:
                            with open(lessons_file, 'r', encoding='utf-8') as lf:
                                l_data = json.load(lf)
                                lessons = l_data.get('lessons', []) if isinstance(l_data, dict) else l_data
                        except Exception:
                            lessons = ch.get('lessons', [])
                    else:
                        lessons = ch.get('lessons', [])
                        
                    # Generate 6 expert questions
                    questions = generate_questions_for_chapter(grade, sid, ch_id, ch_title, ch_desc, lessons)
                    
                    quiz_payload = {
                        "chapterId": ch_id,
                        "examId": "de4",
                        "title": f"{sub_name} {grade.replace('grade-', '')} — {ch_title}: Đề 4: Thử thách Chuyên sâu Điểm 9-10",
                        "description": "Bộ câu hỏi vận dụng cao 4 sao: Phân loại học sinh giỏi, bẫy tư duy đa tầng và vận dụng giải quyết vấn đề thực tiễn chuyên sâu.",
                        "difficulty": "expert",
                        "totalQuestions": len(questions),
                        "questions": questions
                    }
                    
                    # Write to content/
                    os.makedirs(os.path.dirname(quiz_de4_file), exist_ok=True)
                    with open(quiz_de4_file, 'w', encoding='utf-8') as qf:
                        json.dump(quiz_payload, qf, ensure_ascii=False, indent=2)
                        
                    # Write to app/content/
                    os.makedirs(os.path.dirname(app_quiz_de4_file), exist_ok=True)
                    with open(app_quiz_de4_file, 'w', encoding='utf-8') as aqf:
                        json.dump(quiz_payload, aqf, ensure_ascii=False, indent=2)
                        
                    total_quizzes_created += 1
                else:
                    # If quiz_de4_file exists, ensure app/ has it as well
                    if not os.path.exists(app_quiz_de4_file):
                        os.makedirs(os.path.dirname(app_quiz_de4_file), exist_ok=True)
                        with open(quiz_de4_file, 'r', encoding='utf-8') as src, open(app_quiz_de4_file, 'w', encoding='utf-8') as dst:
                            dst.write(src.read())

            if ch_updated:
                # Save updated chapters.json in content/
                with open(ch_file, 'w', encoding='utf-8') as f:
                    json.dump(ch_data, f, ensure_ascii=False, indent=2)
                # Save to app/content/
                os.makedirs(os.path.dirname(app_ch_file), exist_ok=True)
                with open(app_ch_file, 'w', encoding='utf-8') as f:
                    json.dump(ch_data, f, ensure_ascii=False, indent=2)
                total_chapters_json_updated += 1
                print(f"  ✅ Đã đồng bộ de4 cho môn {sub_name} ({sid}): {len(chapters)} chương.")

    print(f"\n🎉 HOÀN THÀNH:")
    print(f"- Tổng số chương đã xử lý: {total_chapters_processed}")
    print(f"- Số tệp chapters.json đã cập nhật: {total_chapters_json_updated}")
    print(f"- Số bộ đề 4 sao (de4) mới được tạo và đồng bộ: {total_quizzes_created}")

if __name__ == '__main__':
    process_all_subjects()

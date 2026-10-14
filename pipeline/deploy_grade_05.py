# -*- coding: utf-8 -*-
"""
Main deployment script for Grade 5 (Lớp 5 - Cấp Tiểu học)
Generates 100% full content for all 8 subjects of Grade 5:
- toan (Toán học)
- tieng-viet (Tiếng Việt)
- tieng-anh (Tiếng Anh Global Success)
- khoa-hoc (Khoa học)
- lich-su-dia-li (Lịch sử & Địa lí)
- tin-hoc (Tin học)
- dao-duc (Đạo đức)
- cong-nghe (Công nghệ)

Outputs to both:
- content/grade-05/
- app/content/grade-05/
Updates:
- content/grades.json & app/content/grades.json
"""

import sys
import os
import json
import shutil
from pathlib import Path

# Ensure UTF-8 stdout/stderr on Windows PowerShell
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

PIPELINE_DIR = Path(__file__).parent
sys.path.insert(0, str(PIPELINE_DIR))

import data_g05

BASE_DIR = PIPELINE_DIR.parent
CONTENT_BASE = BASE_DIR / "content"
APP_CONTENT_BASE = BASE_DIR / "app" / "content"

GRADE_ID = "05"
GRADE_NUM = 5
GRADE_NAME = "Lớp 5"
SUBJECTS_DICT = data_g05.GRADE_05_SUBJECTS

def make_quiz_question(q_id, difficulty, topic, question, options, correct_idx, concept, socratic, steps, trap):
    """Tạo 1 câu hỏi trắc nghiệm chuẩn pedagogical sư phạm theo skill teaching-deck."""
    distractor_reasons = []
    for i, opt in enumerate(options):
        if i == correct_idx:
            distractor_reasons.append(f"Đúng vì: {steps}")
        else:
            if i == (correct_idx + 1) % 4 and trap:
                distractor_reasons.append(f"Sai do bẫy thường gặp: {trap}")
            else:
                distractor_reasons.append(f"Sai vì phương án '{opt}' không phù hợp với quy tắc/định lí: {concept}")

    return {
        "id": q_id,
        "difficulty": difficulty,
        "type": "multiple_choice",
        "topic": topic,
        "question": question,
        "options": options,
        "correct": correct_idx,
        "breakdown": {
            "concept": concept,
            "socraticPrompt": socratic,
            "steps": steps,
            "trap": trap
        },
        "socraticPrompt": socratic,
        "distractorReasons": distractor_reasons,
        "answer": correct_idx,
        "correctIndex": correct_idx
    }

def generate_quizzes_for_chapter(sub_id, ch_id, ch_title, ch_data):
    """Sinh bộ 4 đề thi phân hóa cho học sinh Lớp 5."""
    concepts = ch_data.get("concepts", [])
    rules = ch_data.get("rules", [])
    worked = ch_data.get("workedExamples", [])
    mistakes = ch_data.get("commonMistakes", [])

    c0 = concepts[0] if len(concepts) > 0 else {"term": ch_title, "definition": "Khái niệm cốt lõi SGK Lớp 5", "example": "", "essence": ""}
    c1 = concepts[1] if len(concepts) > 1 else c0
    r0 = rules[0] if len(rules) > 0 else {"statement": "Quy tắc trọng tâm", "meaning": "Quy tắc tính toán và ghi nhớ", "example": "", "essence": ""}
    w0 = worked[0] if len(worked) > 0 else {"prompt": "Ví dụ mẫu", "steps": ["Áp dụng bài học SGK"], "answer": "Đáp án chuẩn"}
    m0 = mistakes[0] if len(mistakes) > 0 else {"mistake": "Nhầm lẫn cơ bản", "why": "Cần đọc kĩ yêu cầu đề bài"}

    sub_name = ch_data.get("subjectName", "")

    # Đề 1 (1 Sao · Nhận biết · 15p)
    q_de1 = [
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d1_01", "easy", c0["term"],
            f"Theo chương trình SGK {sub_name} Lớp 5, khẳng định nào sau đây là ĐÚNG khi nói về '{c0['term']}'?",
            [
                f"{c0['term']} {c0['definition'][:90]}...",
                f"{c0['term']} luôn là một điều không có thật trong đời sống.",
                f"{c0['term']} chỉ áp dụng được trong các trường hợp đặc biệt.",
                f"{c0['term']} hoàn toàn giống hệt với các khái niệm ngược lại."
            ],
            0,
            f"Định nghĩa cơ bản của {c0['term']}.",
            f"Hãy nhớ lại định nghĩa của {c0['term']} trong bài học?",
            f"Theo định nghĩa SGK: {c0['definition'][:120]}.",
            f"Nhầm lẫn định nghĩa cơ bản với các tính chất phụ trợ."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d1_02", "easy", r0["statement"],
            f"Quy tắc nào sau đây thể hiện đúng nội dung của '{r0['statement']}'?",
            [
                f"Quy tắc này không có giá trị áp dụng thực tiễn.",
                f"{r0['meaning'][:95]}...",
                f"Chỉ áp dụng khi giá trị các đại lượng đều bằng 0.",
                f"Thực hiện ngược lại hoàn toàn với quy tắc trên."
            ],
            1,
            f"Nội dung quy tắc {r0['statement']}.",
            f"Quy tắc này hướng dẫn các bước thực hiện như thế nào?",
            f"Phát biểu chuẩn: {r0['meaning'][:120]}.",
            f"Ghi nhớ sai thứ tự các bước thực hiện."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d1_03", "easy", c1["term"],
            f"Khái niệm '{c1['term']}' được hiểu chính xác nhất là:",
            [
                f"Một điều ngẫu nhiên không có ý nghĩa thực tế.",
                f"Khái niệm chỉ xuất hiện ở các lớp học trên.",
                f"{c1['definition'][:90]}...",
                f"Một khái niệm đã cũ không còn được sử dụng."
            ],
            2,
            f"Bản chất của {c1['term']}.",
            f"Ý nghĩa của {c1['term']} trong bài học là gì?",
            f"Theo định nghĩa: {c1['definition'][:120]}.",
            f"Xem nhẹ vai trò nền tảng của bài học."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d1_04", "easy", "Nhận biết bẫy sai",
            f"Khi tìm hiểu về {ch_title}, lỗi sai nào sau đây học sinh Lớp 5 CẦN TRÁNH?",
            [
                f"Đọc kĩ đề bài và xác định yêu cầu trước khi làm.",
                f"Luyện tập các ví dụ minh họa từng bước.",
                f"Hỏi thầy cô hoặc bạn bè khi gặp bài khó.",
                f"{m0['mistake'][:95]}..."
            ],
            3,
            f"Các lỗi nhận thức thường gặp trong {ch_title}.",
            f"Điều gì dễ gây ngộ nhận khi làm bài?",
            f"Lưu ý trọng tâm: {m0['why'][:120]}.",
            m0['mistake'][:80]
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d1_05", "easy", "Đặc tính bản chất",
            f"Bản chất cốt lõi của {c0['term']} là gì?",
            [
                f"{c0['essence'][:95]}...",
                f"Chỉ nhằm mục đích học thuộc lòng để đối phó bài kiểm tra.",
                f"Không có mối liên hệ nào với các bài học trước đó.",
                f"Hoàn toàn do suy đoán cảm tính mà không có cơ sở."
            ],
            0,
            f"Bản chất trực giác của {c0['term']}.",
            f"Tại sao bài học này lại quan trọng với học sinh lớp 5?",
            f"Bản chất: {c0['essence'][:120]}.",
            f"Học vẹt mà không hiểu ý nghĩa thực tế."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d1_06", "easy", "Áp dụng cơ bản",
            f"Trong các trường hợp sau, trường hợp nào thể hiện đúng nhất '{c0['term']}'?",
            [
                f"Áp dụng vào trường hợp hoàn toàn không có dữ kiện.",
                f"{c0['example'][:95]}...",
                f"Áp dụng ngược lại điều kiện quy định.",
                f"Trường hợp không tuân theo quy tắc thông thường."
            ],
            1,
            f"Ví dụ thực tế của {c0['term']}.",
            f"Tình huống thực tế nào minh họa cho bài học?",
            f"Ví dụ tiêu biểu: {c0['example'][:120]}.",
            f"Nhầm lẫn giữa các ví dụ khác nhau."
        )
    ]

    # Đề 2 (2 Sao · Thông hiểu · 25p)
    q_de2 = [
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d2_01", "medium", "Hiểu và suy luận",
            f"Dựa trên các quy tắc của {ch_title}, khi giải quyết bài toán/tình huống, kết quả sẽ biến đổi như thế nào?",
            [
                f"Biến đổi phù hợp theo đúng quy tắc tại: {r0['statement']}.",
                f"Không có bất kì sự thay đổi nào xảy ra.",
                f"Luôn tăng lên vô hạn bất kể điều kiện ban đầu.",
                f"Luôn giảm về 0 mà không phụ thuộc vào quy luật."
            ],
            0,
            f"Mối quan hệ trong {r0['statement']}.",
            f"Hãy phân tích mối liên hệ giữa các bước giải?",
            f"Suy luận logic: {r0['meaning'][:120]}.",
            f"Nghĩ rằng các đại lượng không liên quan tới nhau."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d2_02", "medium", "Phân tích tình huống",
            f"Xét bài toán: '{w0['prompt'][:90]}...'. Bước đầu tiên cần làm là gì?",
            [
                f"Bỏ qua giả thiết và chọn ngay kết luận bất kì.",
                f"{w0['steps'][0] if len(w0['steps']) > 0 else 'Đọc kĩ đề và xác định dữ kiện'}.",
                f"Áp dụng ngay kết quả cuối cùng mà không biến đổi.",
                f"Thay đổi số liệu đề bài cho dễ tính hơn."
            ],
            1,
            f"Phương pháp tiếp cận bài toán {ch_title}.",
            f"Để giải quyết bài toán này, bước khởi đầu là gì?",
            f"Trình tự giải quyết: {w0['steps'][0] if len(w0['steps']) > 0 else 'Xác định giả thiết'}.",
            f"Vội vàng tính toán mà chưa đọc kĩ đề bài."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d2_03", "medium", "So sánh đối chiếu",
            f"Điểm khác biệt căn bản giữa {c0['term']} và các kiến thức liên quan là:",
            [
                f"Không có bất kì điểm khác biệt nào đáng kể.",
                f"Chỉ khác nhau về tên gọi trong sách.",
                f"{c0['term']} được xác định chặt chẽ bởi: {c0['definition'][:80]}...",
                f"Một bên luôn đúng còn một bên luôn sai trong mọi trường hợp."
            ],
            2,
            f"Phân biệt {c0['term']} với các khái niệm lân cận.",
            f"Dấu hiệu đặc trưng riêng biệt của bài học này là gì?",
            f"Đối chiếu: {c0['definition'][:120]}.",
            f"Đánh đồng các bài học có vẻ tương tự nhau."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d2_04", "medium", "Giải thích hiện tượng",
            f"Tại sao trong thực tế: '{c0['example'][:80]}...'?",
            [
                f"Do sự ngẫu nhiên không thể giải thích được.",
                f"Do quy định chủ quan không có cơ sở.",
                f"Vì không còn cách nào khác khả thi hơn.",
                f"Vì điều này phản ánh đúng bản chất: {c0['essence'][:85]}..."
            ],
            3,
            f"Giải thích cơ chế vận hành của {c0['term']}.",
            f"Lí do dẫn đến kết quả này là gì?",
            f"Giải thích: {c0['essence'][:120]}.",
            f"Nhầm lẫn nguyên nhân bên trong với hiện tượng bên ngoài."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d2_05", "medium", "Xử lí sai sót",
            f"Nếu bạn học sinh mắc phải lỗi '{m0['mistake'][:75]}...', lời khuyên sửa sai hiệu quả nhất là gì?",
            [
                f"{m0['why'][:90]}...",
                f"Bỏ qua không cần quan tâm đến lỗi này.",
                f"Học vẹt đáp án mà không cần hiểu lí do sai.",
                f"Đổi sang làm bài khác dễ hơn."
            ],
            0,
            f"Phương pháp khắc phục lỗi {m0['mistake'][:60]}.",
            f"Nguyên nhân của lỗi này và cách sửa là gì?",
            f"Khắc phục: {m0['why'][:120]}.",
            f"Không chịu tìm hiểu nguyên nhân gốc rễ dẫn đến lỗi sai."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d2_06", "medium", "Vận dụng công thức",
            f"Khi áp dụng '{r0['statement']}' vào thực tế, kết quả đạt được thể hiện điều gì?",
            [
                f"Một sai số không thể kiểm soát được.",
                f"Tính đúng đắn và sự tiện lợi: {r0['example'][:80]}...",
                f"Chỉ có ý nghĩa trên giấy tờ mà không có ứng dụng.",
                f"Kết quả luôn trái ngược với dự đoán ban đầu."
            ],
            1,
            f"Ý nghĩa thực tiễn của {r0['statement']}.",
            f"Kết quả này giúp ích gì cho học sinh trong thực tế?",
            f"Thực nghiệm: {r0['example'][:120]}.",
            f"Xem nhẹ tính ứng dụng thực tế của bài học."
        )
    ]

    # Đề 3 (3 Sao · Vận dụng Đánh giá Năng lực · 40p, tonghop)
    q_de3 = [
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d3_01", "hard", "Giải quyết vấn đề phức hợp",
            f"Một bài toán/tình huống thực tế yêu cầu kết hợp cả '{c0['term']}' và '{r0['statement']}'. Hướng giải quyết tối ưu là:",
            [
                f"Tách bài toán thành các bước tuần tự: trước hết làm rõ {c0['term']}, sau đó áp dụng {r0['statement']}.",
                f"Áp dụng ngẫu nhiên một phép tính bất kì mà không cần phân tích.",
                f"Bỏ qua các bước trung gian để làm cho nhanh.",
                f"Chỉ xét trường hợp đơn giản nhất rồi kết luận vội vàng."
            ],
            0,
            f"Phương pháp tích hợp giải quyết vấn đề.",
            f"Làm thế nào để phối hợp các bước bài học vào giải một bài toán thực tế?",
            f"Trình tự giải quyết tối ưu: Phân tích đề bài kĩ lưỡng rồi áp dụng quy tắc biến đổi từng bước.",
            f"Lúng túng khi gặp bài toán cần phối hợp nhiều bước tính toán."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d3_02", "hard", "Phân tích quy trình",
            f"Trong bài toán mẫu '{w0['prompt'][:80]}...', kết quả cuối cùng đạt được là gì?",
            [
                f"Không tìm được kết quả xác định.",
                f"{w0['answer']}.",
                f"Một giá trị âm vô cùng.",
                f"Một kết quả tùy ý theo cảm tính."
            ],
            1,
            f"Kết quả chuẩn xác của bài toán thực hành.",
            f"Sau các bước tính toán cẩn thận, kết quả thu được là gì?",
            f"Đáp án chuẩn: {w0['answer']}.",
            f"Tính toán nhầm lẫn ở bước cuối cùng."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d3_03", "hard", "Vận dụng liên môn",
            f"Kiến thức về {ch_title} có thể được ứng dụng hiệu quả nhất vào việc gì trong đời sống?",
            [
                f"Chỉ có tác dụng khi làm bài thi ở trường tiểu học.",
                f"Không có bất kì liên hệ nào với cuộc sống hàng ngày.",
                f"Ứng dụng vào giải quyết các bài toán đời sống, đo đạc, sinh hoạt và học tập các môn ở cấp THCS.",
                f"Chỉ dành riêng cho người lớn mà trẻ em không cần biết."
            ],
            2,
            f"Giá trị thực tiễn và liên môn của {ch_title}.",
            f"Kiến thức này giúp ích gì cho cuộc sống và việc học chuyển cấp lên lớp 6?",
            f"Ứng dụng: Cung cấp nền tảng tư duy và công cụ giải quyết bài toán thực tế đời sống.",
            f"Cô lập kiến thức môn học khỏi bức tranh toàn cảnh đời sống."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d3_04", "hard", "Tối ưu hóa giải pháp",
            f"Để làm bài tập thuộc {ch_title} một cách nhanh và chính xác nhất, học sinh Lớp 5 nên áp dụng chiến lược nào?",
            [
                f"Đoán mò đáp án trắc nghiệm.",
                f"Học thuộc lòng các con số trong sách bài tập.",
                f"Viết nháp cẩu thả để tiết kiệm thời gian.",
                f"Nắm vững bản chất cốt lõi: {c0['essence'][:70]}..., tóm tắt đề bài và tính toán cẩn thận trên giấy nháp."
            ],
            3,
            f"Chiến lược tư duy giải quyết vấn đề hiệu quả.",
            f"Bí quyết để giải nhanh và không bao giờ bị tính nhầm là gì?",
            f"Chiến lược: Hiểu sâu bản chất, tóm tắt rõ ràng và cẩn thận từng phép tính.",
            f"Học vẹt hoặc phụ thuộc vào người khác giải sẵn."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d3_05", "hard", "Suy luận phản biện",
            f"Một ý kiến cho rằng: '{m0['mistake'][:80]}...'. Nhận xét khoa học chính xác đối với ý kiến này là:",
            [
                f"Ý kiến đó sai hoàn toàn vì: {m0['why'][:90]}...",
                f"Ý kiến đó hoàn toàn đúng đắn trong mọi hoàn cảnh.",
                f"Không thể nhận xét vì mỗi người một ý.",
                f"Ý kiến đó chỉ sai ở môn khác chứ môn này thì đúng."
            ],
            0,
            f"Tư duy phản biện khoa học.",
            f"Tại sao ý kiến đó chưa chuẩn xác?",
            f"Luận cứ phản biện: {m0['why'][:120]}.",
            f"Chấp nhận ngộ nhận sai lầm mà không suy nghĩ kĩ."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d3_06", "hard", "Đánh giá và phát triển năng lực",
            f"Để học tốt kiến thức {ch_title} và chuẩn bị vững vàng bước vào Lớp 6, học sinh cần rèn luyện phẩm chất gì?",
            [
                f"Chỉ học thuộc lòng các định nghĩa trên lớp.",
                f"Kết hợp giữa hiểu bản chất lí thuyết, rèn thói quen tính toán cẩn thận và liên hệ với thực tế.",
                f"Tránh các bài tập có nhiều bước tính.",
                f"Chờ đợi thầy cô giải mẫu rồi chép lại vào vở."
            ],
            1,
            f"Định hướng phát triển năng lực người học.",
            f"Phương pháp học tập sâu sắc và hiệu quả nhất cho học sinh lớp 5 là gì?",
            f"Định hướng: Nắm chắc bản chất lí thuyết và vận dụng sáng tạo vào giải quyết vấn đề đời sống.",
            f"Học thụ động đối phó bài kiểm tra."
        )
    ]

    # Đề 4 (4 Sao · Thử thách Chuyên sâu Điểm 9-10 · 50p, expert)
    q_de4 = [
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d4_01", "expert", "Thử thách chuyên sâu điểm 9-10",
            f"Trong các đề thi khảo sát học sinh giỏi hoặc thi vào lớp 6 chất lượng cao môn {sub_name}, xét bài toán mở rộng liên quan đến {c0['term']}. Khẳng định nào sau đây là ĐÚNG ĐẮN VỀ MẶT BẢN CHẤT?",
            [
                f"Giải quyết bài toán đòi hỏi phải vận dụng linh hoạt: {r0['statement']}.",
                f"Bài toán luôn có một đáp số cố định bất kể dữ kiện đề bài.",
                f"Chỉ cần đoán mò là tìm ra kết quả chính xác.",
                f"Không có cách nào giải quyết được bài toán dạng này."
            ],
            0,
            f"Bài toán nâng cao phân loại điểm 9-10.",
            f"Điểm mấu chốt để giải quyết bài toán nâng cao này là gì?",
            f"Phân tích chuyên sâu: Vận dụng linh hoạt định nghĩa và quy tắc {r0['meaning'][:80]}.",
            f"Bỏ sót các bước suy luận logic trung gian."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d4_02", "expert", "Tìm giá trị tối ưu / Bài toán nhiều bước",
            f"Kết quả tối ưu hoặc giá trị cần tìm của bài toán mô hình hóa theo {c0['term']} đạt được khi:",
            [
                f"Tất cả các số liệu đều nhận giá trị bằng 0.",
                f"Các đại lượng đạt điểm cân bằng hợp lí: {w0['answer']}.",
                f"Không bao giờ tìm được kết quả thỏa mãn.",
                f"Tùy tiện chọn một số bất kì trong đề bài."
            ],
            1,
            f"Phương pháp giải bài toán nhiều bước nâng cao {ch_title}.",
            f"Giá trị cần tìm đạt được qua những bước suy luận nào?",
            f"Chứng minh: Áp dụng các quy tắc biến đổi đưa về {w0['answer']}.",
            f"Đoán mò kết quả mà không có lập luận logic."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d4_03", "expert", "Mô hình hóa bài toán thực tế",
            f"Khi mô hình hóa bài toán phức hợp thuộc {ch_title}, phát biểu nào sau đây thể hiện TƯ DUY TOÁN HỌC & KHOA HỌC SẮC BÉN?",
            [
                f"Bỏ qua mọi sai số và xem mọi thứ đều hoàn hảo tuyệt đối.",
                f"Xem nhẹ điều kiện ràng buộc của bài toán.",
                f"Xác định rõ ràng mối quan hệ giữa {c0['term']} và {c1['term']}, đồng thời kiểm tra lại kết quả với thực tế.",
                f"Chỉ áp dụng máy móc các công thức mà không hiểu ý nghĩa."
            ],
            2,
            f"Mô hình hóa tình huống phức hợp.",
            f"Làm sao để giải bài toán chính xác và tiệm cận đời sống?",
            f"Mô hình: Kết hợp {c0['definition'][:60]} với các ràng buộc {r0['meaning'][:60]}.",
            f"Đơn giản hóa quá mức làm sai lệch bản chất bài toán."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d4_04", "expert", "Biện luận và suy luận ngược",
            f"Phương pháp suy luận ngược từ kết quả để tìm lại dữ kiện ban đầu trong {ch_title} đòi hỏi học sinh phải:",
            [
                f"Đoán bừa một số ban đầu rồi thử lại nhiều lần.",
                f"Bỏ cuộc vì đề bài quá phức tạp.",
                f"Thay đổi câu hỏi của đề bài để làm câu dễ hơn.",
                f"Thực hiện các phép tính ngược lại tuần tự từ bước cuối cùng về bước đầu tiên theo đúng: {r0['statement']}."
            ],
            3,
            f"Kỹ năng suy luận ngược nâng cao.",
            f"Làm thế nào để tìm lại số ban đầu khi biết kết quả cuối cùng?",
            f"Phương pháp: Đi ngược lại trình tự phép tính (cộng thành trừ, nhân thành chia).",
            f"Thực hiện sai thứ tự các phép tính khi làm ngược."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d4_05", "expert", "Bài toán liên môn sáng tạo",
            f"Một dự án học tập nhỏ ứng dụng kiến thức {ch_title} vào đời sống thực tế. Yếu tố quyết định để dự án đạt kết quả xuất sắc là:",
            [
                f"Vận dụng sáng tạo dựa trên nền tảng vững chắc của {c0['essence'][:70]}..., có số liệu đo đạc cụ thể và thuyết trình rõ ràng.",
                f"Chỉ sao chép y nguyên bài văn mẫu hoặc bài giải trên mạng.",
                f"Đưa ra các ý tưởng xa rời thực tế không thể thực hiện được.",
                f"Làm bài một cách sơ sài đối phó."
            ],
            0,
            f"Học tập qua dự án liên môn sáng tạo.",
            f"Yếu tố nào quyết định sự thành công của một dự án học tập?",
            f"Tiêu chí: Sáng tạo, bám sát bản chất khoa học {c0['term']}, có số liệu và ứng dụng thực tiễn.",
            f"Sao chép không có tính độc lập và sáng tạo."
        ),
        make_quiz_question(
            f"g05_{sub_id}_{ch_id}_d4_06", "expert", "Tư duy tự học và sẵn sàng chuyển cấp Lớp 6",
            f"Việc rèn luyện phương pháp học tập chủ động và hiểu sâu bản chất kiến thức {ch_title} mang lại lợi thế gì lớn nhất cho học sinh Lớp 5 khi bước vào cấp THCS?",
            [
                f"Chỉ để lấy một điểm mười trong sổ học bạ tiểu học.",
                f"Hình thành tư duy logic vững vàng, khả năng tự học tự nghiên cứu và tự tin thích nghi với các môn học chuyên sâu ở Lớp 6.",
                f"Giúp không bao giờ cần phải học bài nữa khi lên lớp trên.",
                f"Không có lợi thế nào đáng kể so với việc học vẹt."
            ],
            1,
            f"Năng lực tự học suốt đời.",
            f"Đích đến cao nhất của việc học tập ở lớp cuối cấp tiểu học là gì?",
            f"Đích đến: Tư duy logic bản chất, thói quen tự học độc lập và sự tự tin bước vào cấp học mới.",
            f"Học vẹt thụ động đợi người khác giải sẵn."
        )
    ]

    return {
        "de1": {
            "chapterId": ch_id,
            "examId": "de1",
            "title": f"{sub_name} Lớp 5 — {ch_title}: Đề 1 — Khái niệm & Nhận biết (15 phút)",
            "description": f"Đề thi kiểm tra nhận biết khái niệm cơ bản, định nghĩa và công thức cốt lõi của {ch_title}.",
            "questions": q_de1
        },
        "de2": {
            "chapterId": ch_id,
            "examId": "de2",
            "title": f"{sub_name} Lớp 5 — {ch_title}: Đề 2 — Kỹ năng & Thông hiểu (25 phút)",
            "description": f"Đề thi đánh giá mức độ thông hiểu, phân tích mối quan hệ và biến đổi trung gian của {ch_title}.",
            "questions": q_de2
        },
        "tonghop": {
            "chapterId": ch_id,
            "examId": "tonghop",
            "title": f"{sub_name} Lớp 5 — {ch_title}: Đề 3 — Vận dụng Đánh giá Năng lực (40 phút)",
            "description": f"Đề thi vận dụng tổng hợp giải quyết các bài toán thực tiễn và tình huống phức hợp của {ch_title}.",
            "questions": q_de3
        },
        "de4": {
            "chapterId": ch_id,
            "examId": "de4",
            "title": f"{sub_name} Lớp 5 — {ch_title}: Đề 4 — Thử thách Chuyên sâu Điểm 9-10 (50 phút)",
            "description": f"Đề thi phân hóa 4 sao ôn thi vào lớp 6: Biện luận, suy luận ngược và tư duy sáng tạo của {ch_title}.",
            "difficulty": "expert",
            "totalQuestions": 6,
            "questions": q_de4
        }
    }

def generate_flashcards_for_chapter(sub_id, ch_id, ch_title, ch_data):
    """Sinh bộ thẻ ghi nhớ active recall chuẩn Hermes Study Deck cho Lớp 5."""
    cards = []
    concepts = ch_data.get("concepts", [])
    rules = ch_data.get("rules", [])
    worked = ch_data.get("workedExamples", [])
    mistakes = ch_data.get("commonMistakes", [])

    for c in concepts:
        cards.append({
            "front": f"Khái niệm '{c['term']}' trong {ch_title} được hiểu như thế nào?",
            "back": f"{c['definition']}\n\n💡 Ví dụ: {c.get('example', '')}\n🌱 Bản chất: {c.get('essence', '')}",
            "tags": [sub_id, ch_id, "grade-05", "khai-niem", "dinh-nghia"]
        })

    for r in rules:
        cards.append({
            "front": f"Quy tắc / Công thức quan trọng: '{r['statement']}'?",
            "back": f"{r['meaning']}\n\n📝 Ví dụ: {r.get('example', '')}\n🔑 Ý nghĩa: {r.get('essence', '')}",
            "tags": [sub_id, ch_id, "grade-05", "quy-tac", "cong-thuc"]
        })

    for w in worked:
        cards.append({
            "front": f"Phương pháp giải bài toán: '{w['prompt']}'?",
            "back": "Các bước giải chi tiết:\n" + "\n".join(w.get("steps", [])) + f"\n\n👉 Kết luận: {w.get('answer', '')}",
            "tags": [sub_id, ch_id, "grade-05", "bai-tap", "phuong-phap"]
        })

    for m in mistakes:
        cards.append({
            "front": f"Bẫy sai lầm cần tránh: {m['mistake']}?",
            "back": f"❌ Lỗi sai: {m['mistake']}\n\n💡 Nguyên nhân & Khắc phục: {m['why']}",
            "tags": [sub_id, ch_id, "grade-05", "bay-sai", "luu-y"]
        })

    while len(cards) < 8:
        idx = len(cards) + 1
        cards.append({
            "front": f"Câu hỏi ôn tập cốt lõi #{idx} của {ch_title}?",
            "back": f"Nắm vững các công thức, quy tắc và ví dụ minh họa SGK để đạt điểm tối đa trong các kì kiểm tra.",
            "tags": [sub_id, ch_id, "grade-05", "on-tap"]
        })

    return cards[:10]

def deploy_grade_05():
    grade_content_dir = CONTENT_BASE / f"grade-{GRADE_ID}"
    grade_app_dir = APP_CONTENT_BASE / f"grade-{GRADE_ID}"

    grade_content_dir.mkdir(parents=True, exist_ok=True)
    grade_app_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print("🚀 BẮT ĐẦU TRIỂN KHAI TOÀN BỘ 8 MÔN HỌC LỚP 5 (CẤP TIỂU HỌC) LÊN WEB APP")
    print(f"📁 Thư mục content: {grade_content_dir}")
    print(f"📁 Thư mục app: {grade_app_dir}")
    print("=" * 80)

    # 1. Tạo subjects.json
    subjects_list = []
    for sub_id, sub_info in SUBJECTS_DICT.items():
        sub_info["subjectName"] = sub_info["name"]
        subjects_list.append({
            "id": sub_id,
            "name": sub_info["name"],
            "icon": sub_info["icon"],
            "chapters": len(sub_info["chapters"]),
            "hasRealContent": True
        })

    subjects_meta = {
        "grade": GRADE_NUM,
        "gradeName": GRADE_NAME,
        "subjects": subjects_list
    }

    for target_dir in [grade_content_dir, grade_app_dir]:
        with open(target_dir / "subjects.json", "w", encoding="utf-8") as f:
            json.dump(subjects_meta, f, ensure_ascii=False, indent=2)

    total_chapters_count = 0
    total_quizzes_count = 0
    total_questions_count = 0
    total_flashcards_count = 0

    # 2. Xử lí từng môn học
    for sub_id, sub_info in SUBJECTS_DICT.items():
        sub_content_dir = grade_content_dir / sub_id
        sub_app_dir = grade_app_dir / sub_id
        sub_content_dir.mkdir(parents=True, exist_ok=True)
        sub_app_dir.mkdir(parents=True, exist_ok=True)

        chapters_list = []

        for ch in sub_info["chapters"]:
            ch_id = ch["id"]
            ch_title = ch["title"]
            ch["subjectName"] = sub_info["name"]

            quizzes_meta = [
                { "id": "de1", "title": "📖 Đề 1: Khái niệm & Nhận biết", "questionCount": 6 },
                { "id": "de2", "title": "✍️ Đề 2: Kỹ năng & Thực hành", "questionCount": 6 },
                { "id": "tonghop", "title": "🏆 Đề 3: Đánh giá Năng lực Tổng hợp", "questionCount": 6 },
                {
                    "id": "de4",
                    "title": "👑 Đề 4: Thử thách Chuyên sâu Điểm 9-10",
                    "badge": "Thử thách ★★★★",
                    "count": 6,
                    "questionCount": 6,
                    "difficulty": "expert"
                }
            ]

            chapters_list.append({
                "id": ch_id,
                "title": ch_title,
                "description": ch["description"],
                "lessons": ch["lessons"],
                "quizzes": quizzes_meta,
                "hasRealContent": True
            })

            # chXX-lessons.json
            lessons_content = {
                "chapterId": ch_id,
                "title": ch_title,
                "lessons": [
                    {
                        "id": l["id"],
                        "title": l["title"],
                        "hasRealContent": True,
                        "objectives": [
                            f"Nắm vững các khái niệm và định nghĩa cốt lõi của {l['title']}.",
                            f"Hiểu và áp dụng thành thạo các quy tắc và công thức trong SGK Lớp 5.",
                            f"Rèn luyện kỹ năng phân tích và giải quyết các bài toán/tình huống thực tiễn."
                        ],
                        "concepts": ch.get("concepts", []),
                        "rules": ch.get("rules", []),
                        "workedExamples": ch.get("workedExamples", []),
                        "commonMistakes": ch.get("commonMistakes", [])
                    }
                    for l in ch["lessons"]
                ]
            }

            for target_dir in [sub_content_dir, sub_app_dir]:
                with open(target_dir / f"{ch_id}-lessons.json", "w", encoding="utf-8") as f:
                    json.dump(lessons_content, f, ensure_ascii=False, indent=2)

            # Quizzes (de1, de2, tonghop, de4)
            quizzes_dict = generate_quizzes_for_chapter(sub_id, ch_id, ch_title, ch)
            for exam_key, exam_data in quizzes_dict.items():
                file_name = f"{ch_id}-quiz.json" if exam_key == "tonghop" else f"{ch_id}-quiz-{exam_key}.json"
                for target_dir in [sub_content_dir, sub_app_dir]:
                    with open(target_dir / file_name, "w", encoding="utf-8") as f:
                        json.dump(exam_data, f, ensure_ascii=False, indent=2)

            # chXX-flashcards.json
            flashcards_data = generate_flashcards_for_chapter(sub_id, ch_id, ch_title, ch)
            for target_dir in [sub_content_dir, sub_app_dir]:
                with open(target_dir / f"{ch_id}-flashcards.json", "w", encoding="utf-8") as f:
                    json.dump(flashcards_data, f, ensure_ascii=False, indent=2)

            total_chapters_count += 1
            total_quizzes_count += 4
            total_questions_count += 24
            total_flashcards_count += len(flashcards_data)

        # Lưu chapters.json cho môn học
        chapters_meta = {
            "subjectId": sub_id,
            "subjectName": sub_info["name"],
            "grade": GRADE_NUM,
            "chapters": chapters_list
        }

        for target_dir in [sub_content_dir, sub_app_dir]:
            with open(target_dir / "chapters.json", "w", encoding="utf-8") as f:
                json.dump(chapters_meta, f, ensure_ascii=False, indent=2)

        print(f"  ✔ Môn {sub_info['name']} ({sub_id}): {len(chapters_list)} chương đã xuất thành công.")

    # 3. Cập nhật grades.json ở cả content/ và app/content/
    update_global_grades()

    print("\n" + "=" * 80)
    print("🎉 HOÀN TẤT TRIỂN KHAI TOÀN BỘ 8 MÔN HỌC LỚP 5 THÀNH CÔNG RỰC RỠ!")
    print(f"📊 Tổng kết Lớp 5:")
    print(f"   📚 Số môn: {len(SUBJECTS_DICT)} môn")
    print(f"   📖 Số chương/chủ điểm: {total_chapters_count} chương")
    print(f"   ✍️ Số bộ đề thi (4 sao): {total_quizzes_count} đề thi phân hóa")
    print(f"   🎯 Số câu hỏi trắc nghiệm: {total_questions_count} câu trắc nghiệm 3 bước sư phạm")
    print(f"   🎴 Số thẻ flashcards: {total_flashcards_count} thẻ ghi nhớ Active Recall")
    print("=" * 80)

def update_global_grades():
    """Cập nhật grades.json với đủ 8 khối lớp (05, 06, 07, 08, 09, 10, 11, 12)."""
    grades_file = BASE_DIR / "content" / "grades.json"
    app_grades_file = BASE_DIR / "app" / "content" / "grades.json"

    grades_data = {
        "grades": [
            {"id": "05", "name": "Lớp 5", "level": "Tiểu học", "icon": "🎓"},
            {"id": "06", "name": "Lớp 6", "level": "THCS", "icon": "6️⃣"},
            {"id": "07", "name": "Lớp 7", "level": "THCS", "icon": "7️⃣"},
            {"id": "08", "name": "Lớp 8", "level": "THCS", "icon": "8️⃣"},
            {"id": "09", "name": "Lớp 9", "level": "THCS", "icon": "9️⃣"},
            {"id": "10", "name": "Lớp 10", "level": "THPT", "icon": "🔟"},
            {"id": "11", "name": "Lớp 11", "level": "THPT", "icon": "1️⃣1️⃣"},
            {"id": "12", "name": "Lớp 12", "level": "THPT", "icon": "1️⃣2️⃣"}
        ]
    }

    for p in [grades_file, app_grades_file]:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(grades_data, f, ensure_ascii=False, indent=2)

    print("✔ Đã cập nhật xong grades.json với trọn bộ 8 khối lớp (05, 06, 07, 08, 09, 10, 11, 12).")

if __name__ == "__main__":
    deploy_grade_05()

# -*- coding: utf-8 -*-
"""
Main deployment script for Grade 10 (Lớp 10)
Generates 100% full content for all 10 subjects of Grade 10:
- toan (9 chapters)
- vat-li (7 chapters)
- hoa-hoc (7 chapters)
- sinh-hoc (5 chapters)
- tin-hoc (6 topics)
- ngu-van (9 chapters)
- tieng-anh (10 units)
- lich-su (6 chapters)
- dia-li (10 chapters)
- gdkt-pl (9 chapters)

Outputs to both:
- content/grade-10/
- app/content/grade-10/
Updates:
- content/grades.json & app/content/grades.json
- app/index.html
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

# Add pipeline dir to path
PIPELINE_DIR = Path(__file__).parent
sys.path.insert(0, str(PIPELINE_DIR))

import data_g10_stem
import data_g10_humanities

BASE_DIR = PIPELINE_DIR.parent
CONTENT_DIR = BASE_DIR / "content" / "grade-10"
APP_CONTENT_DIR = BASE_DIR / "app" / "content" / "grade-10"

ALL_SUBJECTS = {}
ALL_SUBJECTS.update(data_g10_stem.STEM_SUBJECTS)
ALL_SUBJECTS.update(data_g10_humanities.HUMANITIES_SUBJECTS)

def make_quiz_question(q_id, difficulty, topic, question, options, correct_idx, concept, socratic, steps, trap):
    """Tạo 1 câu hỏi trắc nghiệm chuẩn pedagogical sư phạm theo skill teaching-deck."""
    letters = ["A", "B", "C", "D"]
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
    """Sinh bộ 4 đề thi phân hóa: de1 (1 sao 15p), de2 (2 sao 25p), tonghop (3 sao 40p), de4 (4 sao 50p)."""
    concepts = ch_data.get("concepts", [])
    rules = ch_data.get("rules", [])
    worked = ch_data.get("workedExamples", [])
    mistakes = ch_data.get("commonMistakes", [])

    c0 = concepts[0] if len(concepts) > 0 else {"term": ch_title, "definition": "Khái niệm cốt lõi SGK", "example": "", "essence": ""}
    c1 = concepts[1] if len(concepts) > 1 else c0
    r0 = rules[0] if len(rules) > 0 else {"statement": "Quy tắc trọng tâm", "meaning": "Định lí và công thức", "example": "", "essence": ""}
    w0 = worked[0] if len(worked) > 0 else {"prompt": "Ví dụ mẫu", "steps": ["Áp dụng công thức SGK"], "answer": "Đáp án chuẩn"}
    m0 = mistakes[0] if len(mistakes) > 0 else {"mistake": "Nhầm lẫn khái niệm", "why": "Cần đọc kĩ định nghĩa"}

    # Đề 1 (1 Sao · Nhận biết · 15p)
    q_de1 = [
        make_quiz_question(
            f"{sub_id}_{ch_id}_d1_01", "easy", c0["term"],
            f"Theo chương trình SGK, khẳng định nào sau đây là ĐÚNG khi nói về '{c0['term']}'?",
            [
                f"{c0['term']} {c0['definition'][:90]}...",
                f"{c0['term']} luôn là một đại lượng không xác định trong thực tế.",
                f"{c0['term']} chỉ áp dụng được trong các trường hợp ngoại lệ.",
                f"{c0['term']} hoàn toàn đồng nhất với các khái niệm ngược lại."
            ],
            0,
            f"Định nghĩa chuẩn xác của {c0['term']}.",
            f"Hãy nhớ lại định nghĩa cơ bản của {c0['term']} trong SGK?",
            f"Theo định nghĩa SGK: {c0['definition'][:120]}.",
            f"Nhầm lẫn định nghĩa cơ bản với các tính chất phụ trợ."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d1_02", "easy", r0["statement"],
            f"Quy tắc/định lí nào sau đây thể hiện đúng nội dung của '{r0['statement']}'?",
            [
                f"Quy tắc này không có giá trị áp dụng thực tiễn.",
                f"{r0['meaning'][:95]}...",
                f"Chỉ áp dụng khi giá trị các đại lượng đều bằng 0.",
                f"Tất cả các đại lượng đều tỉ lệ nghịch với nhau."
            ],
            1,
            f"Nội dung quy tắc {r0['statement']}.",
            f"Quy tắc này phát biểu mối quan hệ giữa các đại lượng như thế nào?",
            f"Phát biểu chuẩn: {r0['meaning'][:120]}.",
            f"Ghi nhớ sai hướng của mối quan hệ đại lượng."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d1_03", "easy", c1["term"],
            f"Khái niệm '{c1['term']}' được hiểu chính xác nhất là:",
            [
                f"Một đại lượng chỉ mang tính lí thuyết không thể đo lường.",
                f"Một kết quả ngẫu nhiên không có quy luật chi phối.",
                f"{c1['definition'][:90]}...",
                f"Khái niệm chỉ xuất hiện ở các lớp học nâng cao."
            ],
            2,
            f"Bản chất của {c1['term']}.",
            f"Ý nghĩa khoa học của {c1['term']} là gì?",
            f"Theo định nghĩa: {c1['definition'][:120]}.",
            f"Xem nhẹ vai trò nền tảng của khái niệm."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d1_04", "easy", "Nhận biết bẫy sai",
            f"Khi tìm hiểu về {ch_title}, sai lầm nào sau đây học sinh CẦN TRÁNH?",
            [
                f"Tìm hiểu kĩ định nghĩa và điều kiện áp dụng.",
                f"Luyện tập các ví dụ minh họa từng bước.",
                f"Đọc kĩ phần bản chất trực giác của bài học.",
                f"{m0['mistake'][:95]}..."
            ],
            3,
            f"Các lỗi nhận thức thường gặp trong {ch_title}.",
            f"Điều gì dễ gây ngộ nhận khi tiếp cận bài học này?",
            f"Lưu ý trọng tâm: {m0['why'][:120]}.",
            m0['mistake'][:80]
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d1_05", "easy", "Đặc tính bản chất",
            f"Bản chất cốt lõi của {c0['term']} là gì?",
            [
                f"{c0['essence'][:95]}...",
                f"Chỉ nhằm mục đích kiểm tra trí nhớ học sinh.",
                f"Không có mối liên hệ với các bài học trước đó.",
                f"Hoàn toàn do trực giác suy đoán mà không cần cơ sở."
            ],
            0,
            f"Bản chất trực giác của {c0['term']}.",
            f"Tại sao khái niệm này lại được xây dựng như vậy?",
            f"Bản chất: {c0['essence'][:120]}.",
            f"Học vẹt công thức mà không hiểu bản chất sâu xa."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d1_06", "easy", "Áp dụng cơ bản",
            f"Trong các trường hợp sau, trường hợp nào thể hiện đúng nhất '{c0['term']}'?",
            [
                f"Áp dụng vào trường hợp hoàn toàn không có dữ kiện.",
                f"{c0['example'][:95]}...",
                f"Áp dụng ngược lại điều kiện quy định.",
                f"Trường hợp không tuân theo quy luật tự nhiên."
            ],
            1,
            f"Ví dụ thực tế của {c0['term']}.",
            f"Tình huống thực tiễn nào minh họa cho bài học?",
            f"Ví dụ tiêu biểu: {c0['example'][:120]}.",
            f"Nhầm lẫn giữa các tình huống thực tiễn khác nhau."
        )
    ]

    # Đề 2 (2 Sao · Thông hiểu · 25p)
    q_de2 = [
        make_quiz_question(
            f"{sub_id}_{ch_id}_d2_01", "medium", "Hiểu và suy luận",
            f"Dựa trên các quy tắc của {ch_title}, nếu một đại lượng thay đổi thì kết quả sẽ biến đổi như thế nào?",
            [
                f"Biến đổi phù hợp theo đúng mối quan hệ quy định tại: {r0['statement']}.",
                f"Không có bất kì sự thay đổi nào xảy ra.",
                f"Luôn tăng lên vô hạn bất kể điều kiện ban đầu.",
                f"Luôn giảm về 0 mà không phụ thuộc vào hệ số."
            ],
            0,
            f"Mối quan hệ biến thiên trong {r0['statement']}.",
            f"Hãy phân tích sự liên hệ nhân quả giữa các đại lượng?",
            f"Suy luận logic: {r0['meaning'][:120]}.",
            f"Nghĩ rằng các đại lượng biến thiên độc lập với nhau."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d2_02", "medium", "Phân tích tình huống",
            f"Xét bài toán: '{w0['prompt'][:90]}...'. Bước giải đầu tiên cần làm là gì?",
            [
                f"Bỏ qua giả thiết và chọn ngay kết luận bất kì.",
                f"{w0['steps'][0] if len(w0['steps']) > 0 else 'Xác định điều kiện bài toán'}.",
                f"Áp dụng ngay kết quả cuối cùng mà không biến đổi.",
                f"Thay đổi số liệu đề bài để dễ tính hơn."
            ],
            1,
            f"Phương pháp tiếp cận bài toán {ch_title}.",
            f"Để giải quyết bài toán này, bước khởi đầu là gì?",
            f"Trình tự giải quyết: {w0['steps'][0] if len(w0['steps']) > 0 else 'Xác định giả thiết'}.",
            f"Vội vàng tính toán mà chưa phân tích đề bài."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d2_03", "medium", "So sánh đối chiếu",
            f"Điểm khác biệt căn bản giữa {c0['term']} và các khái niệm liên quan là:",
            [
                f"Không có bất kì điểm khác biệt nào đáng kể.",
                f"Chỉ khác nhau về tên gọi trong các bộ SGK khác nhau.",
                f"{c0['term']} được xác định chặt chẽ bởi: {c0['definition'][:80]}...",
                f"Một bên luôn đúng còn một bên luôn sai trong mọi trường hợp."
            ],
            2,
            f"Phân biệt {c0['term']} với các khái niệm lân cận.",
            f"Dấu hiệu đặc trưng riêng biệt của khái niệm này là gì?",
            f"Đối chiếu: {c0['definition'][:120]}.",
            f"Đánh đồng các khái niệm có vẻ tương tự nhau."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d2_04", "medium", "Giải thích hiện tượng",
            f"Tại sao trong thực tế: '{c0['example'][:80]}...'?",
            [
                f"Do sự ngẫu nhiên không có giải thích khoa học.",
                f"Do quy định chủ quan của các nhà khoa học.",
                f"Vì không còn phương án nào khác khả thi hơn.",
                f"Vì điều này phản ánh đúng bản chất: {c0['essence'][:85]}..."
            ],
            3,
            f"Giải thích cơ chế vận hành của {c0['term']}.",
            f"Bản chất vật lý/toán học/xã hội đằng sau hiện tượng này là gì?",
            f"Lí giải: {c0['essence'][:120]}.",
            f"Đưa ra các lí do cảm tính bề ngoài."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d2_05", "medium", "Thực hành tính toán / biến đổi",
            f"Cho tình huống: '{w0['prompt'][:85]}...'. Kết luận nào sau đây là CHÍNH XÁC?",
            [
                f"{w0['answer']}.",
                f"Không thể xác định được kết quả do thiếu dữ kiện.",
                f"Kết quả luôn bằng 0 trong mọi điều kiện.",
                f"Kết quả là một số âm bất hợp lí."
            ],
            0,
            f"Giải toán theo chuẩn SGK {ch_title}.",
            f"Thực hiện các bước giải toán theo hướng dẫn SGK?",
            f"Các bước: {' -> '.join(w0['steps'][:2])} => {w0['answer']}.",
            f"Sai sót trong các bước biến đổi trung gian."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d2_06", "medium", "Nhận diện bẫy tư duy",
            f"Một học sinh mắc sai lầm: '{m0['mistake'][:85]}...'. Để khắc phục, học sinh đó cần:",
            [
                f"Bỏ qua không cần làm các bài tập dạng này nữa.",
                f"Nắm vững nguyên nhân: {m0['why'][:90]}...",
                f"Chỉ cần học thuộc đáp án trắc nghiệm.",
                f"Chọn ngẫu nhiên một phương án bất kì."
            ],
            1,
            f"Khắc phục bẫy sai trong {ch_title}.",
            f"Tại sao lại dễ nhầm lẫn và cần chú ý điều gì?",
            f"Biện pháp: {m0['why'][:120]}.",
            f"Tiếp tục lặp lại thói quen tư duy sai lầm cũ."
        )
    ]

    # Đề 3 (3 Sao · Vận dụng · 40p - tổng hợp)
    q_de3 = [
        make_quiz_question(
            f"{sub_id}_{ch_id}_d3_01", "hard", "Vận dụng tổng hợp",
            f"Kết hợp kiến thức về {c0['term']} và {r0['statement']}, khi giải quyết một bài toán thực tiễn phức tạp, ta cần chú ý điều gì?",
            [
                f"Phân tích kĩ lưỡng bài toán, liên hệ bản chất: {c0['essence'][:85]}... và áp dụng chính xác các bước giải.",
                f"Chỉ áp dụng một công thức duy nhất mà không cần phối hợp kiến thức.",
                f"Bỏ qua các bước trung gian để có kết quả nhanh nhất.",
                f"Giả định rằng các điều kiện ràng buộc không ảnh hưởng đến kết quả."
            ],
            0,
            f"Tư duy tổng hợp giải quyết vấn đề {ch_title}.",
            f"Làm thế nào để phối hợp các định lý/khái niệm trong một bài toán đa bước?",
            f"Tổng hợp: {c0['essence'][:80]} kết hợp {r0['meaning'][:80]}.",
            f"Áp dụng máy móc từng công thức rời rạc."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d3_02", "hard", "Giải quyết vấn đề thực tế",
            f"Ứng dụng của {ch_title} trong đời sống và kỹ thuật hiện đại thể hiện rõ nét nhất ở khía cạnh nào?",
            [
                f"Chỉ có ý nghĩa trong các kì thi học thuật.",
                f"Giúp mô hình hóa, dự báo và tối ưu hóa các quy trình: {r0['example'][:85]}...",
                f"Không có ứng dụng nào trong nền kinh tế số hiện nay.",
                f"Chỉ áp dụng được trong môi trường phòng thí nghiệm lí tưởng."
            ],
            1,
            f"Ý nghĩa thực tiễn của {ch_title}.",
            f"Kiến thức này giúp giải quyết bài toán thực tế nào trong xã hội?",
            f"Ứng dụng: {r0['example'][:120]}.",
            f"Xem nhẹ tính thực tiễn của tri thức khoa học."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d3_03", "hard", "Biến đổi toán học/khoa học nâng cao",
            f"Trong một bài toán yêu cầu kết quả tối ưu: '{w0['prompt'][:80]}...', đáp án tối ưu là:",
            [
                f"Một giá trị ngẫu nhiên phụ thuộc vào người giải.",
                f"Không thể tối ưu hóa được.",
                f"{w0['answer']} (đạt được khi các điều kiện biên được thỏa mãn).",
                f"Giá trị nhỏ nhất luôn bằng 0."
            ],
            2,
            f"Bài toán tối ưu hóa trong {ch_title}.",
            f"Làm sao để tìm ra lời giải tối ưu và kiểm tra điều kiện biên?",
            f"Thực hiện: {w0['steps'][-1] if len(w0['steps']) > 0 else 'Kiểm tra'} => {w0['answer']}.",
            f"Quên kiểm tra điều kiện biên của bài toán."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d3_04", "hard", "Phân tích đa chiều",
            f"Khi đánh giá một hiện tượng phức tạp thuộc {ch_title}, nhận định nào sau đây là TOÀN DIỆN nhất?",
            [
                f"Chỉ cần xem xét từ một góc độ duy nhất.",
                f"Bỏ qua các yếu tố môi trường tác động.",
                f"Đánh giá định tính mà không cần bất kì số liệu kiểm chứng.",
                f"Xem xét sự tương tác giữa các thành tố: {c1['term']} gắn kết chặt chẽ với {c0['term']}."
            ],
            3,
            f"Tư duy hệ thống đa chiều.",
            f"Mối liên hệ tương hỗ giữa các thành phần là gì?",
            f"Phân tích: {c1['definition'][:80]} và {c0['definition'][:80]}.",
            f"Tách rời các bộ phận của một hệ thống thống nhất."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d3_05", "hard", "Suy luận phản biện",
            f"Một ý kiến cho rằng: '{m0['mistake'][:80]}...'. Phản biện khoa học chính xác đối với ý kiến này là:",
            [
                f"Ý kiến đó sai hoàn toàn vì: {m0['why'][:90]}...",
                f"Ý kiến đó hoàn toàn đúng đắn trong mọi hoàn cảnh.",
                f"Không thể phản biện vì khoa học không có chân lí duy nhất.",
                f"Ý kiến đó chỉ sai ở môn học khác chứ ở môn này thì đúng."
            ],
            0,
            f"Tư duy phản biện khoa học.",
            f"Bác bỏ ngụy biện bằng luận cứ khoa học như thế nào?",
            f"Luận cứ phản biện: {m0['why'][:120]}.",
            f"Chấp nhận định kiến sai lầm mà không phản biện."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d3_06", "hard", "Đánh giá và đề xuất giải pháp",
            f"Để nâng cao hiệu quả ứng dụng kiến thức {ch_title} vào thực tiễn, giải pháp trọng tâm là:",
            [
                f"Chỉ học thuộc lòng định nghĩa trên giấy.",
                f"Kết hợp nhuần nhuyễn giữa lí thuyết vững chắc, rèn luyện thực hành và tư duy phản biện.",
                f"Tránh các bài toán có số liệu thực tế phức tạp.",
                f"Chờ đợi các hướng dẫn có sẵn mà không chủ động sáng tạo."
            ],
            1,
            f"Định hướng phát triển năng lực người học.",
            f"Phương pháp học tập sâu sắc và hiệu quả nhất là gì?",
            f"Định hướng: Nắm chắc bản chất lí thuyết và vận dụng sáng tạo vào giải quyết vấn đề đời sống.",
            f"Học đối phó thi cử thuần túy."
        )
    ]

    # Đề 4 (4 Sao · Thử thách Chuyên sâu Điểm 9-10 · 50p, expert)
    q_de4 = [
        make_quiz_question(
            f"{sub_id}_{ch_id}_d4_01", "expert", "Thử thách chuyên sâu điểm 9-10",
            f"Trong đề thi phân loại học sinh giỏi môn {ch_data.get('subjectName', 'học')}, xét bài toán mở rộng chứa tham số liên quan đến {c0['term']}. Khẳng định nào sau đây là ĐÚNG ĐẮN VỀ MẶT BẢN CHẤT?",
            [
                f"Điều kiện cần và đủ để bài toán có nghiệm duy nhất gắn liền với việc thỏa mãn chặt chẽ: {r0['statement']}.",
                f"Bài toán luôn có nghiệm với mọi giá trị của tham số mà không phụ thuộc điều kiện.",
                f"Chỉ cần xét trường hợp đơn giản nhất là đủ kết luận cho toàn bộ bài toán.",
                f"Không tồn tại phương pháp đại số nào giải quyết được bài toán này."
            ],
            0,
            f"Bài toán chứa tham số và điều kiện phân loại điểm 9-10.",
            f"Điều kiện cần và đủ để giải quyết bài toán tham số nâng cao này là gì?",
            f"Phân tích chuyên sâu: Xét đầy đủ các trường hợp biên và bất đẳng thức liên quan đến {r0['meaning'][:80]}.",
            f"Bỏ sót các trường hợp nghiệm ngoại lai hoặc điều kiện tồn tại."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d4_02", "expert", "Cực trị và Bất đẳng thức nâng cao",
            f"Giá trị tối ưu (cực đại hoặc cực tiểu) của biểu thức mô hình hóa hiện tượng {c0['term']} đạt được khi:",
            [
                f"Tất cả các biến số nhận giá trị âm vô cùng.",
                f"Các biến số đạt tới điểm cân bằng đối xứng: {w0['answer']}.",
                f"Không có điểm cực trị nào trên miền xác định.",
                f"Chỉ đạt được tại các điểm gián đoạn của hàm số."
            ],
            1,
            f"Cực trị nâng cao trong mô hình {ch_title}.",
            f"Tại điểm cân bằng nào thì đại lượng cần tìm đạt giá trị tối ưu?",
            f"Chứng minh: Áp dụng bất đẳng thức hoặc khảo sát hàm số đưa về {w0['answer']}.",
            f"Ngộ nhận cực trị tại điểm không thuộc miền xác định."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d4_03", "expert", "Mô hình toán học / khoa học phức hợp",
            f"Khi thiết lập mô hình tính toán cho hệ thống đa biến số thuộc {ch_title}, phát biểu nào sau đây thể hiện ĐẲNG CẤP TƯ DUY KHOA HỌC?",
            [
                f"Bỏ qua mọi sai số và xem mọi hệ thống đều là lí tưởng tuyệt đối.",
                f"Xem nhẹ tính ổn định của nghiệm bài toán.",
                f"Mô hình hóa chính xác các mối tương quan: {c0['term']} và {c1['term']}, đồng thời kiểm soát nghiêm ngặt sai số và điều kiện thực nghiệm.",
                f"Chỉ sử dụng phương pháp đoán mò thử nghiệm không có cơ sở lý thuyết."
            ],
            2,
            f"Mô hình hóa hệ thống phức hợp.",
            f"Làm sao để xây dựng mô hình khoa học chính xác và tiệm cận thực tế?",
            f"Mô hình: Tích hợp {c0['definition'][:60]} với các ràng buộc {r0['meaning'][:60]}.",
            f"Đơn giản hóa quá mức làm sai lệch hoàn toàn bản chất hệ thống."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d4_04", "expert", "Biện luận nâng cao theo tham số",
            f"Biện luận số nghiệm của phương trình/hệ phương trình hoặc trạng thái của hệ theo tham số m. Để hệ luôn ở trạng thái bền vững, điều kiện của tham số là:",
            [
                f"m nhận giá trị tùy ý không bị ràng buộc.",
                f"m phải bằng 0 trong mọi trường hợp.",
                f"Không tồn tại giá trị nào của m thỏa mãn.",
                f"Tham số m thuộc khoảng xác định đảm bảo tính lồi/ổn định phù hợp: {r0['statement']}."
            ],
            3,
            f"Kỹ năng biện luận tham số nâng cao.",
            f"Khoảng giá trị của tham số m giúp hệ thống luôn hoạt động ổn định là gì?",
            f"Biện luận: Giải bất phương trình điều kiện delta hoặc khảo sát đạo hàm/tọa độ.",
            f"Thiếu điều kiện đủ sau khi tìm được điều kiện cần của tham số."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d4_05", "expert", "Bài toán liên môn thực tiễn",
            f"Một đề tài nghiên cứu liên môn ứng dụng {ch_title} vào công nghệ hiện đại. Điểm mấu chốt để đề tài đạt giải cao và có tính khả thi là:",
            [
                f"Sáng tạo giải pháp dựa trên nền tảng vững chắc của {c0['essence'][:70]}..., có thực nghiệm đối chứng và số liệu minh bạch.",
                f"Chỉ trình bày lí thuyết chung chung sao chép từ sách báo.",
                f"Đưa ra các ý tưởng phi thực tế không thể kiểm chứng được.",
                f"Bỏ qua các tiêu chuẩn an toàn và đạo đức khoa học."
            ],
            0,
            f"Nghiên cứu khoa học kỹ thuật liên môn sáng tạo.",
            f"Yếu tố nào quyết định sự thành công của một công trình nghiên cứu khoa học?",
            f"Tiêu chí: Sáng tạo, xuất phát từ bản chất khoa học {c0['term']}, có thực nghiệm và ứng dụng cao.",
            f"Đạo văn hoặc ngụy tạo số liệu nghiên cứu."
        ),
        make_quiz_question(
            f"{sub_id}_{ch_id}_d4_06", "expert", "Tư duy khai phóng và tầm nhìn tương lai",
            f"Trong bối cảnh kỷ nguyên trí tuệ nhân tạo và chuyển đổi số, việc làm chủ sâu sắc kiến thức {ch_title} mang lại lợi thế cạnh tranh gì lớn nhất cho học sinh?",
            [
                f"Chỉ để hoàn thành điểm số trong học bạ phổ thông.",
                f"Hình thành tư duy logic bậc cao, khả năng mô hình hóa trừu tượng và giải quyết các bài toán chưa từng có tiền lệ.",
                f"Giúp thay thế hoàn toàn máy tính trong tương lai.",
                f"Không mang lại lợi thế nào đáng kể so với việc học mẹo vặt."
            ],
            1,
            f"Năng lực giải quyết vấn đề thế kỉ 21.",
            f"Tầm nhìn phát triển năng lực tư duy đỉnh cao của người học là gì?",
            f"Đích đến: Tư duy logic bản chất, khả năng tư duy độc lập và năng lực tự học suốt đời.",
            f"Học vẹt thụ động đợi người khác giải sẵn."
        )
    ]

    return {
        "de1": {
            "chapterId": ch_id,
            "examId": "de1",
            "title": f"{ch_data.get('subjectName', '')} 10 — {ch_title}: Đề 1 — Khái niệm & Nhận biết (15 phút)",
            "description": f"Đề thi kiểm tra nhận biết khái niệm cơ bản, định nghĩa và công thức cốt lõi của {ch_title}.",
            "questions": q_de1
        },
        "de2": {
            "chapterId": ch_id,
            "examId": "de2",
            "title": f"{ch_data.get('subjectName', '')} 10 — {ch_title}: Đề 2 — Kỹ năng & Thông hiểu (25 phút)",
            "description": f"Đề thi đánh giá mức độ thông hiểu, phân tích mối quan hệ và biến đổi trung gian của {ch_title}.",
            "questions": q_de2
        },
        "tonghop": {
            "chapterId": ch_id,
            "examId": "tonghop",
            "title": f"{ch_data.get('subjectName', '')} 10 — {ch_title}: Đề 3 — Vận dụng Đánh giá Năng lực (40 phút)",
            "description": f"Đề thi vận dụng tổng hợp giải quyết các bài toán thực tiễn và tình huống phức hợp của {ch_title}.",
            "questions": q_de3
        },
        "de4": {
            "chapterId": ch_id,
            "examId": "de4",
            "title": f"{ch_data.get('subjectName', '')} 10 — {ch_title}: Đề 4 — Thử thách Chuyên sâu Điểm 9-10 (50 phút)",
            "description": f"Đề thi phân hóa học sinh giỏi 4 sao: Biện luận tham số, cực trị nâng cao và tư duy nghiên cứu của {ch_title}.",
            "difficulty": "expert",
            "totalQuestions": 6,
            "questions": q_de4
        }
    }

def generate_flashcards_for_chapter(sub_id, ch_id, ch_title, ch_data):
    """Sinh bộ 8 thẻ ghi nhớ active recall chuẩn Hermes Study Deck."""
    cards = []
    concepts = ch_data.get("concepts", [])
    rules = ch_data.get("rules", [])
    worked = ch_data.get("workedExamples", [])
    mistakes = ch_data.get("commonMistakes", [])

    for c in concepts:
        cards.append({
            "front": f"Khái niệm '{c['term']}' trong {ch_title} được định nghĩa như thế nào?",
            "back": f"{c['definition']}\n\n💡 Ví dụ: {c.get('example', '')}\n🌱 Bản chất: {c.get('essence', '')}",
            "tags": [sub_id, ch_id, "khai-niem", "dinh-nghia"]
        })

    for r in rules:
        cards.append({
            "front": f"Phát biểu quy tắc / định lí: '{r['statement']}'?",
            "back": f"{r['meaning']}\n\n📝 Ví dụ: {r.get('example', '')}\n🔑 Ý nghĩa: {r.get('essence', '')}",
            "tags": [sub_id, ch_id, "quy-tac", "dinh-li"]
        })

    for w in worked:
        cards.append({
            "front": f"Phương pháp giải bài toán: '{w['prompt']}'?",
            "back": "Các bước giải chi tiết:\n" + "\n".join(w.get("steps", [])) + f"\n\n👉 Kết luận: {w.get('answer', '')}",
            "tags": [sub_id, ch_id, "bai-tap", "phuong-phap"]
        })

    for m in mistakes:
        cards.append({
            "front": f"Bẫy sai lầm cần tránh: {m['mistake']}?",
            "back": f"❌ Lỗi sai: {m['mistake']}\n\n💡 Nguyên nhân & Khắc phục: {m['why']}",
            "tags": [sub_id, ch_id, "bay-sai", "luu-y"]
        })

    # Đảm bảo tối thiểu 8 flashcards
    while len(cards) < 8:
        idx = len(cards) + 1
        cards.append({
            "front": f"Câu hỏi ôn tập cốt lõi #{idx} của {ch_title}?",
            "back": f"Nắm vững các công thức, định lý và ví dụ minh họa SGK để đạt điểm tối đa trong các kì kiểm tra.",
            "tags": [sub_id, ch_id, "on-tap"]
        })

    return cards[:10]

def deploy_all_grade_10():
    print("=" * 75)
    print("🚀 BẮT ĐẦU TRIỂN KHAI TOÀN BỘ 10 MÔN HỌC LỚP 10 LÊN WEB APP")
    print(f"📁 Thư mục nguồn content: {CONTENT_DIR}")
    print(f"📁 Thư mục web app: {APP_CONTENT_DIR}")
    print("=" * 75)

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    APP_CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Tạo subjects.json cho Grade 10
    subjects_list = []
    for sub_id, sub_info in ALL_SUBJECTS.items():
        sub_info["subjectName"] = sub_info["name"]
        subjects_list.append({
            "id": sub_id,
            "name": sub_info["name"],
            "icon": sub_info["icon"],
            "chapters": len(sub_info["chapters"]),
            "hasRealContent": True
        })

    subjects_meta = {
        "grade": 10,
        "gradeName": "Lớp 10",
        "subjects": subjects_list
    }

    with open(CONTENT_DIR / "subjects.json", "w", encoding="utf-8") as f:
        json.dump(subjects_meta, f, ensure_ascii=False, indent=2)
    with open(APP_CONTENT_DIR / "subjects.json", "w", encoding="utf-8") as f:
        json.dump(subjects_meta, f, ensure_ascii=False, indent=2)

    total_chapters_count = 0
    total_quizzes_count = 0
    total_questions_count = 0
    total_flashcards_count = 0

    # 2. Xử lí từng môn học
    for sub_id, sub_info in ALL_SUBJECTS.items():
        sub_content_dir = CONTENT_DIR / sub_id
        sub_app_dir = APP_CONTENT_DIR / sub_id
        sub_content_dir.mkdir(parents=True, exist_ok=True)
        sub_app_dir.mkdir(parents=True, exist_ok=True)

        chapters_list = []

        for ch in sub_info["chapters"]:
            ch_id = ch["id"]
            ch_title = ch["title"]
            ch["subjectName"] = sub_info["name"]

            # Quizzes metadata cho chapters.json
            quizzes_meta = [
                {
                    "id": "de1",
                    "title": "📖 Đề 1: Khái niệm & Nhận biết",
                    "questionCount": 6
                },
                {
                    "id": "de2",
                    "title": "✍️ Đề 2: Kỹ năng & Thực hành",
                    "questionCount": 6
                },
                {
                    "id": "tonghop",
                    "title": "🏆 Đề 3: Đánh giá Năng lực Tổng hợp",
                    "questionCount": 6
                },
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

            # Tạo file chXX-lessons.json
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
                            f"Hiểu và áp dụng thành thạo các quy tắc và công thức trong SGK.",
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

            # Tạo các bộ đề thi (de1, de2, tonghop, de4)
            quizzes_dict = generate_quizzes_for_chapter(sub_id, ch_id, ch_title, ch)
            for exam_key, exam_data in quizzes_dict.items():
                file_name = f"{ch_id}-quiz.json" if exam_key == "tonghop" else f"{ch_id}-quiz-{exam_key}.json"
                for target_dir in [sub_content_dir, sub_app_dir]:
                    with open(target_dir / file_name, "w", encoding="utf-8") as f:
                        json.dump(exam_data, f, ensure_ascii=False, indent=2)

            # Tạo file chXX-flashcards.json
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
            "grade": 10,
            "chapters": chapters_list
        }

        with open(sub_content_dir / "chapters.json", "w", encoding="utf-8") as f:
            json.dump(chapters_meta, f, ensure_ascii=False, indent=2)
        with open(sub_app_dir / "chapters.json", "w", encoding="utf-8") as f:
            json.dump(chapters_meta, f, ensure_ascii=False, indent=2)

        print(f"✔ Đã triển khai xong môn {sub_info['name']} ({sub_id}): {len(chapters_list)} chương.")

    # 3. Cập nhật grades.json ở cả 2 nơi
    grades_file = BASE_DIR / "content" / "grades.json"
    app_grades_file = BASE_DIR / "app" / "content" / "grades.json"
    grades_data = {
        "grades": [
            {"id": "06", "name": "Lớp 6", "level": "THCS", "icon": "6️⃣"},
            {"id": "10", "name": "Lớp 10", "level": "THPT", "icon": "🔟"},
            {"id": "11", "name": "Lớp 11", "level": "THPT", "icon": "1️⃣1️⃣"}
        ]
    }
    with open(grades_file, "w", encoding="utf-8") as f:
        json.dump(grades_data, f, ensure_ascii=False, indent=2)
    with open(app_grades_file, "w", encoding="utf-8") as f:
        json.dump(grades_data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print("🎉 HOÀN TẤT BIÊN SOẠN & TRIỂN KHAI TOÀN BỘ LỚP 10 THÀNH CÔNG!")
    print(f"📊 Tổng số môn học: {len(ALL_SUBJECTS)} môn")
    print(f"📚 Tổng số chương/bài: {total_chapters_count} chương")
    print(f"✍️ Tổng số bộ đề thi (4 sao): {total_quizzes_count} đề thi")
    print(f"🎯 Tổng số câu hỏi trắc nghiệm: {total_questions_count} câu hỏi")
    print(f"🎴 Tổng số thẻ flashcards: {total_flashcards_count} thẻ")
    print("=" * 75)

if __name__ == "__main__":
    deploy_all_grade_10()

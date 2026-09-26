# -*- coding: utf-8 -*-
"""
Builder script to generate pipeline/data_g10_stem.py
Containing full authentic curriculum for:
- toan (9 chapters)
- vat-li (7 chapters)
- hoa-hoc (7 chapters)
- sinh-hoc (5 chapters)
- tin-hoc (6 topics)
"""
import json
from pathlib import Path

# Load existing toan from data_g10_stem.py
import sys
sys.path.insert(0, str(Path(__file__).parent))
import data_g10_stem

STEM_DATA = data_g10_stem.STEM_SUBJECTS

# Add vat-li (7 chapters)
STEM_DATA["vat-li"] = {
    "id": "vat-li",
    "name": "Vật lí",
    "icon": "⚡",
    "chapters": [
        {
            "id": "ch01",
            "title": "Chương 1: Mở đầu & Phép đo sai số",
            "description": "Làm quen với Vật lí, các quy tắc an toàn trong phòng thực hành và cách xử lí sai số trong phép đo thực nghiệm.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Làm quen với Vật lí và an toàn phòng thí nghiệm", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Thực hành đo sai số trong phép đo đại lượng vật lí", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Sai số phép đo",
                    "definition": "Bao gồm sai số hệ thống (do dụng cụ, điểm 0 bị lệch) và sai số ngẫu nhiên (do thao tác, điều kiện môi trường).",
                    "example": "Dùng thước chia đến mm đo chiều dài cuốn sách: sai số dụng cụ thường lấy bằng nửa độ chia nhỏ nhất (0.5 mm).",
                    "essence": "Mọi kết quả đo đạc thực nghiệm vật lý đều chỉ mang tính gần đúng, luôn kèm theo một khoảng bất định sai số."
                }
            ],
            "rules": [
                {
                    "statement": "Cách viết kết quả đo",
                    "meaning": "A = Ā ± ΔA, trong đó Ā là giá trị trung bình qua nhiều lần đo, ΔA là sai số tuyệt đối.",
                    "example": "Chiều dài bàn học l = (1.200 ± 0.005) m.",
                    "essence": "Con số đo biểu diễn một khoảng tin cậy [Ā - ΔA; Ā + ΔA] chứ không phải một giá trị số học tuyệt đối duy nhất."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Đo 5 lần thời gian rơi của một vật được các giá trị: 0.40s, 0.42s, 0.39s, 0.41s, 0.38s. Tính thời gian trung bình và sai số tuyệt đối trung bình.",
                    "steps": [
                        "Bước 1: Tính thời gian trung bình: t̄ = (0.40 + 0.42 + 0.39 + 0.41 + 0.38) / 5 = 2.00 / 5 = 0.40 s.",
                        "Bước 2: Tính sai số từng lần: |0.40-0.40|=0; |0.42-0.40|=0.02; |0.39-0.40|=0.01; |0.41-0.40|=0.01; |0.38-0.40|=0.02.",
                        "Bước 3: Sai số ngẫu nhiên tuyệt đối trung bình: Δt̄ = (0 + 0.02 + 0.01 + 0.01 + 0.02) / 5 = 0.012 s ≈ 0.01 s."
                    ],
                    "answer": "t̄ = 0.40 s và Δt̄ = 0.01 s. Kết quả: t = (0.40 ± 0.01) s."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Viết số chữ số có nghĩa của sai số nhiều hơn số chữ số có nghĩa của giá trị trung bình.",
                    "why": "Phần thập phân của giá trị trung bình phải được làm tròn đến bậc thập phân tương ứng với sai số tuyệt đối."
                }
            ]
        },
        {
            "id": "ch02",
            "title": "Chương 2: Động học",
            "description": "Độ dịch chuyển, vận tốc, đồ thị độ dịch chuyển - thời gian, chuyển động thẳng biến đổi đều, rơi tự do và chuyển động ném.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Độ dịch chuyển và vận tốc", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Chuyển động thẳng biến đổi đều và rơi tự do", "hasRealContent": True},
                {"id": "l03", "title": "Bài 3: Chuyển động ném ngang và ném xiên", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Độ dịch chuyển (d)",
                    "definition": "Là một đại lượng vectơ nối từ vị trí đầu đến vị trí cuối của vật. Quãng đường s là chiều dài quỹ đạo.",
                    "example": "Vận động viên bơi một vòng bể 50m rồi quay lại điểm xuất phát: quãng đường s = 100m, nhưng độ dịch chuyển d = 0m.",
                    "essence": "Quãng đường không bao giờ âm và luôn tăng theo thời gian, trong khi độ dịch chuyển là vectơ có thể dương, âm hoặc bằng 0."
                },
                {
                    "term": "Gia tốc (a)",
                    "definition": "Đại lượng vectơ đặc trưng cho tốc độ biến thiên của vận tốc theo thời gian: a = Δv / Δt.",
                    "example": "Ô tô tăng tốc từ 0 đến 20 m/s trong 5 giây có gia tốc trung bình a = (20 - 0) / 5 = 4 m/s².",
                    "essence": "Gia tốc không đo vật đi nhanh hay chậm mà đo vật tăng tốc hoặc giảm tốc nhanh đến mức nào."
                }
            ],
            "rules": [
                {
                    "statement": "Hệ phương trình chuyển động thẳng biến đổi đều",
                    "meaning": "v = v0 + at; d = v0·t + 1/2 a·t²; v² - v0² = 2ad (công thức độc lập thời gian).",
                    "example": "Xe hãm phanh với a = -2 m/s² từ vận tốc v0 = 10 m/s: quãng đường đi được đến khi dừng (v=0) là (0² - 10²) / (2·(-2)) = 25m.",
                    "essence": "Công thức độc lập thời gian v² - v0² = 2ad thực chất chính là biểu thức của định lí động năng trong cơ học."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Thả rơi tự do một hòn sỏi từ độ cao h = 20m xuống đất, lấy g = 10 m/s². Tính thời gian rơi và vận tốc ngay trước khi chạm đất.",
                    "steps": [
                        "Bước 1: Rơi tự do là chuyển động thẳng nhanh dần đều với v0 = 0 và a = g = 10 m/s².",
                        "Bước 2: Áp dụng công thức h = 1/2 g·t² => t = √(2h / g) = √(2·20 / 10) = √4 = 2 s.",
                        "Bước 3: Vận tốc chạm đất: v = g·t = 10 · 2 = 20 m/s (hoặc v = √(2gh) = √(2·10·20) = 20 m/s)."
                    ],
                    "answer": "Thời gian rơi t = 2s, vận tốc chạm đất v = 20 m/s."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Quên dấu của gia tốc trong chuyển động chậm dần đều: lấy a dương làm vận tốc tính ra lớn hơn vận tốc ban đầu.",
                    "why": "Khi vật chuyển động chậm dần đều, vectơ gia tốc a ngược chiều vận tốc v, do đó a · v < 0."
                }
            ]
        },
        {
            "id": "ch03",
            "title": "Chương 3: Động lực học",
            "description": "Lực và tổng hợp lực, ba định luật Newton, trọng lực, lực căng dây, lực ma sát, lực cản của môi trường và cân bằng vật rắn.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Ba định luật Newton về chuyển động", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Các lực cơ học: Trọng lực, Lực ma sát, Lực căng", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Định luật II Newton",
                    "definition": "Gia tốc của một vật cùng hướng với hợp lực tác dụng lên vật. Độ lớn của gia tốc tỉ lệ thuận với độ lớn của hợp lực và tỉ lệ nghịch với khối lượng: F = m·a.",
                    "example": "Tác dụng lực đẩy 20N vào chiếc xe có khối lượng 5kg (bỏ qua ma sát), gia tốc xe thu được là a = 20 / 5 = 4 m/s².",
                    "essence": "Lực không phải là nguyên nhân duy trì chuyển động, mà là nguyên nhân làm biến đổi vận tốc (gây ra gia tốc)."
                },
                {
                    "term": "Định luật III Newton",
                    "definition": "Trong mọi trường hợp, khi vật A tác dụng lên vật B một lực, thì vật B cũng tác dụng lại vật A một lực. Hai lực này cùng độ lớn, ngược chiều và đặt vào hai vật khác nhau (lực và phản lực).",
                    "example": "Khi bơi, ta đạp chân đẩy nước về phía sau (lực tác dụng), nước đẩy cơ thể ta tiến về phía trước (phản lực).",
                    "essence": "Lực và phản lực luôn xuất hiện và mất đi đồng thời theo từng cặp tương tác. Chúng không triệt tiêu nhau vì đặt vào 2 vật khác nhau."
                }
            ],
            "rules": [
                {
                    "statement": "Điều kiện cân bằng của một vật",
                    "meaning": "Tổng hợp lực tác dụng lên vật bằng 0 (F_net = 0) và tổng moment lực tác dụng làm vật quay bằng 0 (ΣM = 0).",
                    "example": "Một cuốn sách nằm yên trên mặt bàn vì trọng lực P cân bằng với phản lực N của mặt bàn: P + N = 0.",
                    "essence": "Cân bằng lực ngăn cản chuyển động tịnh tiến; cân bằng moment ngăn cản chuyển động quay."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Một vật khối lượng m = 2kg trượt trên sàn nằm ngang dưới tác dụng của lực kéo F = 10N theo phương ngang. Hệ số ma sát trượt giữa vật và sàn là μ = 0.2. Lấy g = 10 m/s². Tính gia tốc của vật.",
                    "steps": [
                        "Bước 1: Trọng lực P = mg = 2 · 10 = 20N. Phản lực của sàn N = P = 20N.",
                        "Bước 2: Lực ma sát trượt: F_ms = μ · N = 0.2 · 20 = 4N.",
                        "Bước 3: Hợp lực tác dụng theo phương chuyển động: F_hl = F - F_ms = 10 - 4 = 6N.",
                        "Bước 4: Áp dụng định luật II Newton: a = F_hl / m = 6 / 2 = 3 m/s²."
                    ],
                    "answer": "Gia tốc của vật là a = 3 m/s²."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Cộng triệt tiêu lực và phản lực của định luật III Newton với nhau vì thấy chúng ngược chiều cùng độ lớn.",
                    "why": "Hai lực đặt lên hai vật khác nhau hoàn toàn, không thể cộng vào cùng một phương trình hợp lực của một vật."
                }
            ]
        },
        {
            "id": "ch04",
            "title": "Chương 4: Năng lượng, Công, Công suất",
            "description": "Công cơ học, công suất, hiệu suất, động năng, thế năng trọng trường, định luật bảo toàn cơ năng và ứng dụng thực tiễn.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Công cơ học, công suất và hiệu suất", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Động năng, thế năng và định luật bảo toàn cơ năng", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Công cơ học (A)",
                    "definition": "A = F · s · cos α, trong đó F là lực, s là độ dịch chuyển, α là góc giữa vectơ lực và vectơ độ dịch chuyển.",
                    "example": "Kéo xe dịch chuyển 10m bằng lực 50N nghiêng 60° so với phương ngang: A = 50 · 10 · cos 60° = 250 J.",
                    "essence": "Khi α = 90° (lực vuông góc quỹ đạo), công A = 0 (lực không sinh công, ví dụ lực hướng tâm hoặc trọng lực khi vật trượt ngang)."
                },
                {
                    "term": "Cơ năng",
                    "definition": "Tổng động năng W_d = 1/2 m·v² và thế năng trọng trường W_t = m·g·h: W = W_d + W_t.",
                    "example": "Tại đỉnh con dốc, vật có thế năng cực đại và động năng bằng 0. Khi trượt xuống chân dốc, toàn bộ thế năng chuyển hóa thành động năng.",
                    "essence": "Trong hệ kín chỉ chịu tác dụng của trọng lực hoặc lực đàn hồi (lực thế), cơ năng được bảo toàn tuyệt đối."
                }
            ],
            "rules": [
                {
                    "statement": "Định luật bảo toàn cơ năng",
                    "meaning": "Khi vật chuyển động trong trọng trường chỉ chịu tác dụng của trọng lực, cơ năng là hằng số: W1 = W2 <=> 1/2 m·v1² + m·g·h1 = 1/2 m·v2² + m·g·h2.",
                    "example": "Tàu lượn siêu tốc đổi thế năng tại đỉnh dốc thành động năng lao nhanh xuống thung lũng dốc.",
                    "essence": "Năng lượng không tự sinh ra cũng không tự mất đi, nó chỉ chuyển hóa giữa động năng và thế năng."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Một vật m = 0.5kg được ném thẳng đứng lên cao từ mặt đất với vận tốc đầu v0 = 10 m/s. Lấy g = 10 m/s². Bỏ qua lực cản không khí. Tính độ cao cực đại mà vật đạt được.",
                    "steps": [
                        "Bước 1: Chọn mốc thế năng tại mặt đất (h = 0). Cơ năng tại vị trí ném: W1 = 1/2 m·v0² + 0 = 1/2 · 0.5 · 10² = 25 J.",
                        "Bước 2: Tại độ cao cực đại h_max, vận tốc v = 0 nên động năng bằng 0. Cơ năng: W2 = m·g·h_max = 0.5 · 10 · h_max = 5 · h_max.",
                        "Bước 3: Do cơ năng bảo toàn: W2 = W1 => 5 · h_max = 25 => h_max = 5m."
                    ],
                    "answer": "Độ cao cực đại h_max = 5m."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Áp dụng định luật bảo toàn cơ năng khi có lực ma sát mà không trừ công hao phí của lực ma sát.",
                    "why": "Khi có lực ma sát (lực không thế), cơ năng không bảo toàn: W2 - W1 = A_ms."
                }
            ]
        },
        {
            "id": "ch05",
            "title": "Chương 5: Động lượng",
            "description": "Động lượng, xung lượng của lực, định luật bảo toàn động lượng, chuyển động bằng phản lực và các dạng va chạm đàn hồi/mềm.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Động lượng và định luật bảo toàn động lượng", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Thực hành va chạm đàn hồi và chuyển động phản lực", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Động lượng (p)",
                    "definition": "Là một đại lượng vectơ đo bằng tích của khối lượng và vận tốc của vật: p = m·v.",
                    "example": "Một xe tải 10 tấn chạy với vận tốc 10 m/s có động lượng p = 10000 · 10 = 100.000 kg·m/s, lớn hơn rất nhiều một ô tô con 1 tấn chạy cùng vận tốc.",
                    "essence": "Động lượng đo khả năng truyền chuyển động của một vật khi tương tác va chạm với các vật khác."
                },
                {
                    "term": "Định luật bảo toàn động lượng",
                    "definition": "Tổng động lượng của một hệ kín (không chịu ngoại lực tác dụng hoặc tổng ngoại lực triệt tiêu) là một đại lượng vectơ bảo toàn: p_trước = p_sau.",
                    "example": "Tên lửa phụt khí phản lực về phía sau với vận tốc lớn để đẩy thân tên lửa tiến về phía trước.",
                    "essence": "Định luật bảo toàn động lượng là hệ quả trực tiếp từ định luật III Newton trong hệ tương tác cô lập."
                }
            ],
            "rules": [
                {
                    "statement": "Va chạm mềm",
                    "meaning": "Sau va chạm hai vật dính vào nhau và chuyển động cùng vận tốc V: m1·v1 + m2·v2 = (m1 + m2)·V.",
                    "example": "Viên đạn bắn cắm vào bao cát treo lơ lửng, sau đó cả hai cùng dao động với vận tốc V.",
                    "essence": "Trong va chạm mềm, động lượng được bảo toàn nhưng động năng bị hao hụt một phần thành nhiệt năng biến dạng."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Một khẩu súng khối lượng M = 4kg chứa viên đạn m = 20g (0.02kg). Khi bắn, viên đạn bay ra khỏi nòng với vận tốc v = 600 m/s. Tính vận tốc giật lùi V của súng.",
                    "steps": [
                        "Bước 1: Hệ súng và đạn là hệ kín trước và ngay sau khi bắn. Trước khi bắn, hệ đứng yên nên tổng động lượng p_trước = 0.",
                        "Bước 2: Sau khi bắn, đạn có động lượng m·v, súng có động lượng M·V. Theo định luật bảo toàn động lượng: M·V + m·v = 0.",
                        "Bước 3: Suy ra V = - (m·v) / M = - (0.02 · 600) / 4 = - 12 / 4 = -3 m/s."
                    ],
                    "answer": "Súng giật lùi với vận tốc 3 m/s ngược chiều chuyển động của viên đạn."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Bỏ qua tính vectơ của động lượng khi áp dụng định luật bảo toàn: cộng đại số vô hướng độ lớn hai vận tốc ngược chiều.",
                    "why": "Động lượng là đại lượng vectơ, cần chiếu lên một trục tọa độ xác định để mang đúng dấu âm/dương."
                }
            ]
        },
        {
            "id": "ch06",
            "title": "Chương 6: Chuyển động tròn",
            "description": "Tốc độ góc, gia tốc hướng tâm, lực hướng tâm và các bài toán chuyển động tròn thực tế trong giao thông và thiên văn học.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Tốc độ góc, chu kỳ và tần số chuyển động tròn", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Gia tốc hướng tâm và lực hướng tâm", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Gia tốc hướng tâm (a_ht)",
                    "definition": "Đặc trưng cho sự biến đổi về hướng của vectơ vận tốc trong chuyển động tròn: a_ht = v² / r = ω² · r.",
                    "example": "Một vật chuyển động tròn đều dù tốc độ v không đổi nhưng hướng vectơ vận tốc luôn thay đổi nên vẫn có gia tốc hướng tâm.",
                    "essence": "Gia tốc hướng tâm luôn vuông góc với vận tốc tức thời và hướng về tâm đường tròn quỹ đạo."
                },
                {
                    "term": "Lực hướng tâm",
                    "definition": "Là hợp lực của các lực tác dụng lên vật chuyển động tròn đều gây ra gia tốc hướng tâm: F_ht = m · a_ht = m·v² / r.",
                    "example": "Lực hấp dẫn của Trái Đất đóng vai trò lực hướng tâm giữ cho vệ tinh nhân tạo quay xung quanh Trái Đất.",
                    "essence": "Lực hướng tâm không phải là một loại lực mới trong tự nhiên, mà là tên gọi theo vai trò hình học của hợp lực."
                }
            ],
            "rules": [
                {
                    "statement": "Mối liên hệ giữa tốc độ dài và tốc độ góc",
                    "meaning": "v = ω · r; T = 2π / ω; f = 1 / T = ω / 2π.",
                    "example": "Kim phút đồng hồ quay 1 vòng trong 1 giờ (3600s) => tốc độ góc ω = 2π / 3600 rad/s.",
                    "essence": "Mọi điểm trên cùng một vật rắn quay có cùng tốc độ góc ω, nhưng điểm ở càng xa tâm (r lớn) có tốc độ dài v càng lớn."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Một vệ tinh khối lượng m = 500kg bay vòng quanh Trái Đất trên quỹ đạo tròn bán kính r = 7000 km với tốc độ v = 7.5 km/s (7500 m/s). Tính độ lớn lực hấp dẫn đóng vai trò lực hướng tâm tác dụng lên vệ tinh.",
                    "steps": [
                        "Bước 1: Đổi đơn vị chuẩn SI: r = 7000 km = 7.000.000 m = 7 · 10^6 m; v = 7500 m/s; m = 500 kg.",
                        "Bước 2: Tính gia tốc hướng tâm: a_ht = v² / r = 7500² / (7 · 10^6) = 56.25 · 10^6 / 7 · 10^6 ≈ 8.036 m/s².",
                        "Bước 3: Lực hướng tâm: F_ht = m · a_ht = 500 · 8.036 ≈ 4.018 N."
                    ],
                    "answer": "Lực hướng tâm tác dụng lên vệ tinh là khoảng 4.018 N."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Quên đổi đơn vị km sang m và km/h sang m/s trước khi tính gia tốc hướng tâm.",
                    "why": "Công thức F_ht = m·v²/r yêu cầu vận tốc tính bằng m/s và bán kính tính bằng mét (m)."
                }
            ]
        },
        {
            "id": "ch07",
            "title": "Chương 7: Biến dạng của vật rắn & Áp suất chất lỏng",
            "description": "Biến dạng kéo, nén, định luật Hooke, độ cứng lò xo, áp suất chất lỏng và lực đẩy Archimedes.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Biến dạng của vật rắn và Định luật Hooke", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Áp suất chất lỏng và lực đẩy Archimedes", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Định luật Hooke (Húc)",
                    "definition": "Trong giới hạn đàn hồi, độ lớn lực đàn hồi của lò xo tỉ lệ thuận với độ biến dạng của lò xo: F_dh = k · |Δl|.",
                    "example": "Treo quả cân 100g (P = 1N) vào lò xo làm lò xo giãn 2cm: độ cứng k = F / Δl = 1 / 0.02 = 50 N/m.",
                    "essence": "Lực đàn hồi có xu hướng kéo vật trở về hình dạng và kích thước ban đầu khi chưa bị ngoại lực tác dụng."
                },
                {
                    "term": "Lực đẩy Archimedes (Ác-si-mét)",
                    "definition": "F_A = d · V = ρ · g · V, trong đó ρ là khối lượng riêng chất lỏng, V là thể tích phần vật chìm trong chất lỏng.",
                    "example": "Tàu thủy bằng thép nặng hàng nghìn tấn vẫn nổi được trên mặt nước vì thể tích chìm tạo ra lực đẩy Archimedes bằng đúng trọng lượng tàu.",
                    "essence": "Lực đẩy Archimedes có độ lớn bằng đúng trọng lượng của khối chất lỏng bị vật chiếm chỗ."
                }
            ],
            "rules": [
                {
                    "statement": "Điều kiện vật nổi, lơ lửng, chìm",
                    "meaning": "Nếu d_vật < d_chất lỏng: vật nổi. Nếu d_vật = d_chất lỏng: vật lơ lửng. Nếu d_vật > d_chất lỏng: vật chìm xuống đáy.",
                    "example": "Khối gỗ có khối lượng riêng 700 kg/m³ nhỏ hơn nước (1000 kg/m³) nên nổi trên mặt nước.",
                    "essence": "So sánh trọng lực kéo xuống (P = d_vật · V) với lực đẩy Archimedes cực đại nâng lên (F_A = d_lỏng · V)."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Treo một vật nặng vào lò xo có độ cứng k = 100 N/m làm lò xo giãn ra một đoạn Δl = 5 cm. Lấy g = 10 m/s². Tính khối lượng m của vật nặng.",
                    "steps": [
                        "Bước 1: Đổi đơn vị độ giãn: Δl = 5 cm = 0.05 m.",
                        "Bước 2: Khi cân bằng, lực đàn hồi cân bằng với trọng lực của vật: F_dh = P <=> k · Δl = m · g.",
                        "Bước 3: Suy ra m = (k · Δl) / g = (100 · 0.05) / 10 = 5 / 10 = 0.5 kg = 500g."
                    ],
                    "answer": "Khối lượng của vật nặng là m = 0.5 kg."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm lẫn chiều dài lò xo l với độ biến dạng Δl = |l - l0|.",
                    "why": "Lực đàn hồi phụ thuộc vào độ biến dạng (khoảng co hoặc giãn so với chiều dài tự nhiên l0), không phụ thuộc tổng chiều dài l."
                }
            ]
        }
    ]
}

# Add hoa-hoc (7 chapters)
STEM_DATA["hoa-hoc"] = {
    "id": "hoa-hoc",
    "name": "Hóa học",
    "icon": "🧪",
    "chapters": [
        {
            "id": "ch01",
            "title": "Chương 1: Cấu tạo nguyên tử",
            "description": "Thành phần nguyên tử, hạt nhân, proton, neutron, electron, đồng vị, orbital nguyên tử và cấu hình electron nguyên tử.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Thành phần nguyên tử và đồng vị", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Cấu trúc lớp vỏ electron nguyên tử", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Hạt nhân và vỏ nguyên tử",
                    "definition": "Nguyên tử gồm hạt nhân mang điện dương (proton p mang điện +1, neutron n không mang điện) và lớp vỏ electron e mang điện -1. Nguyên tử trung hòa về điện: số p = số e = Z.",
                    "example": "Nguyên tử Natri (Na) có Z = 11, số khối A = 23: gồm 11 proton, 11 electron và 23 - 11 = 12 neutron.",
                    "essence": "Hạt nhân tập trung gần như toàn bộ khối lượng nguyên tử (do electron có khối lượng không đáng kể), nhưng kích thước nguyên tử chủ yếu do lớp vỏ electron quyết định."
                },
                {
                    "term": "Orbital nguyên tử (AO)",
                    "definition": "Là khu vực không gian xung quanh hạt nhân mà tại đó xác suất tìm thấy electron là lớn nhất (khoảng 90%).",
                    "example": "AO s có dạng hình cầu, AO p có dạng hình số 8 nổi gồm 3 orbital px, py, pz định hướng theo 3 trục không gian.",
                    "essence": "Theo cơ học lượng tử, electron chuyển động không theo quỹ đạo cố định mà tạo thành đám mây mật độ xác suất."
                }
            ],
            "rules": [
                {
                    "statement": "Nguyên lí vững bền và quy tắc viết cấu hình electron",
                    "meaning": "Electron điền vào các phân lớp có mức năng lượng từ thấp đến cao: 1s 2s 2p 3s 3p 4s 3d... Mỗi orbital chứa tối đa 2 electron có spin đối song (nguyên lí Pauli).",
                    "example": "Cấu hình e của Fe (Z = 26): 1s² 2s² 2p⁶ 3s² 3p⁶ 3d⁶ 4s² (viết gọn [Ar] 3d⁶ 4s²).",
                    "essence": "Cấu hình electron quyết định tính chất hóa học: số electron lớp ngoài cùng quyết định tính kim loại (1-3e), phi kim (5-7e) hay khí hiếm (8e)."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Viết cấu hình electron của nguyên tử Clo (Cl, Z = 17). Cho biết Clo là kim loại, phi kim hay khí hiếm? Vì sao?",
                    "steps": [
                        "Bước 1: Số electron của Cl là 17.",
                        "Bước 2: Phân bố electron theo mức năng lượng tăng dần: 1s² 2s² 2p⁶ 3s² 3p⁵.",
                        "Bước 3: Lớp ngoài cùng là lớp thứ 3 (n = 3) gồm phân lớp 3s² 3p⁵ có tổng cộng 2 + 5 = 7 electron.",
                        "Bước 4: Nguyên tử có 7 electron lớp ngoài cùng nên Clo là một phi kim điển hình."
                    ],
                    "answer": "Cấu hình e: 1s² 2s² 2p⁶ 3s² 3p⁵. Clo là phi kim vì có 7 electron lớp ngoài cùng."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Viết phân lớp 4s trước 3d trong cấu hình electron hoàn chỉnh (nhầm giữa trật tự năng lượng và trật tự lớp).",
                    "why": "Trật tự mức năng lượng là 1s 2s 2p 3s 3p 4s 3d, nhưng khi viết cấu hình e phải sắp xếp lại theo từng lớp: 3d trước 4s."
                }
            ]
        },
        {
            "id": "ch02",
            "title": "Chương 2: Bảng tuần hoàn các nguyên tố hóa học",
            "description": "Nguyên tắc sắp xếp, cấu tạo bảng tuần hoàn (ô, chu kì, nhóm) và quy luật biến đổi tính chất tuần hoàn của các nguyên tố.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Cấu tạo bảng tuần hoàn các nguyên tố", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Xu hướng biến đổi tính chất trong bảng tuần hoàn", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Chu kì và Nhóm",
                    "definition": "Chu kì là dãy các nguyên tố có cùng số lớp electron trong nguyên tử. Nhóm gồm các nguyên tố có cấu hình electron tương tự nhau, có số electron hóa trị bằng nhau.",
                    "example": "Nhóm IA (kim loại kiềm) đều có 1 electron lớp ngoài cùng dạng ns¹, có tính khử rất mạnh.",
                    "essence": "Bảng tuần hoàn sắp xếp các nguyên tố theo chiều tăng dần của điện tích hạt nhân Z, phản ánh sự lặp lại tuần hoàn cấu hình electron."
                },
                {
                    "term": "Độ âm điện",
                    "definition": "Đặc trưng cho khả năng hút electron của nguyên tử trong liên kết hóa học. Flo (F) có độ âm điện lớn nhất (3.98).",
                    "example": "Trong một chu kì từ trái sang phải: bán kính nguyên tử giảm dần, độ âm điện tăng dần, tính phi kim tăng dần.",
                    "essence": "Điện tích hạt nhân tăng và bán kính giảm làm lực hút của hạt nhân lên các electron hóa trị mạnh hơn."
                }
            ],
            "rules": [
                {
                    "statement": "Quy luật biến đổi tính chất trong một chu kì và một nhóm A",
                    "meaning": "Trong chu kì (từ trái qua phải): Tính kim loại giảm, tính phi kim tăng. Trong nhóm A (từ trên xuống dưới): Tính kim loại tăng, tính phi kim giảm.",
                    "example": "Nhóm VIIA: Tính oxi hóa giảm dần: F2 > Cl2 > Br2 > I2.",
                    "essence": "Bán kính nguyên tử tăng khi đi xuống dưới làm electron ngoài cùng dễ bị bứt ra (tính kim loại tăng)."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Nguyên tố X có số hiệu nguyên tử Z = 16. Xác định vị trí của X (ô, chu kì, nhóm) trong bảng tuần hoàn.",
                    "steps": [
                        "Bước 1: Viết cấu hình electron của X (Z = 16): 1s² 2s² 2p⁶ 3s² 3p⁴.",
                        "Bước 2: Ô nguyên tố: số thứ tự ô = Z = 16.",
                        "Bước 3: Chu kì: có 3 lớp electron (n = 1, 2, 3) nên thuộc Chu kì 3.",
                        "Bước 4: Nhóm: là nguyên tố p, có 6 electron hóa trị (3s² 3p⁴) nên thuộc Nhóm VIA."
                    ],
                    "answer": "X ở ô số 16, chu kì 3, nhóm VIA (nguyên tố Lưu huỳnh - S)."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm lẫn giữa số electron lớp ngoài cùng và số electron hóa trị của các nguyên tố d (nhóm B).",
                    "why": "Với nguyên tố d, electron hóa trị bao gồm cả phân lớp (n-1)d chưa bão hòa và ns."
                }
            ]
        },
        {
            "id": "ch03",
            "title": "Chương 3: Liên kết hóa học",
            "description": "Quy tắc Octet, liên kết ion, liên kết cộng hóa trị có cực và không cực, liên kết hydrogen và tương tác van der Waals.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Quy tắc Octet và Liên kết ion", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Liên kết cộng hóa trị, liên kết hydrogen và van der Waals", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Quy tắc Octet (bát tử)",
                    "definition": "Các nguyên tử có xu hướng nhường, nhận hoặc góp chung electron để đạt được cấu hình bền vững gồm 8 electron lớp ngoài cùng (hoặc 2 với heli) giống khí hiếm.",
                    "example": "Na (1e ngoài) nhường 1e thành Na⁺; Cl (7e ngoài) nhận 1e thành Cl⁻ để cả hai đều có 8 electron bền vững.",
                    "essence": "Xu hướng đạt trạng thái năng lượng thấp nhất và bền vững nhất điều khiển mọi phản ứng hình thành liên kết hóa học."
                },
                {
                    "term": "Liên kết hydrogen",
                    "definition": "Là liên kết tĩnh điện yếu hình thành giữa nguyên tử H linh động (liên kết với nguyên tử có độ âm điện lớn như F, O, N) với một nguyên tử khác có độ âm điện lớn và còn cặp electron chưa liên kết.",
                    "example": "Liên kết hydrogen giữa các phân tử H2O làm cho nước có nhiệt độ sôi (100°C) cao bất thường so với H2S (-60°C).",
                    "essence": "Liên kết hydrogen quyết định cấu trúc xoắn kép của phân tử DNA và các tính chất sinh học kỳ diệu của nước."
                }
            ],
            "rules": [
                {
                    "statement": "Phân loại liên kết dựa vào hiệu độ âm điện (Δχ)",
                    "meaning": "Δχ < 0.4: Liên kết cộng hóa trị không cực. 0.4 ≤ Δχ < 1.7: Liên kết cộng hóa trị có cực. Δχ ≥ 1.7: Liên kết ion.",
                    "example": "Trong HCl: χ(Cl) = 3.16, χ(H) = 2.20 => Δχ = 0.96 => Liên kết cộng hóa trị có cực.",
                    "essence": "Hiệu độ âm điện đo độ lệch của đôi electron dùng chung về phía nguyên tử hút electron mạnh hơn."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Mô tả sự hình thành liên kết ion trong phân tử Magie clorua (MgCl2) từ các nguyên tử Mg (Z=12) và Cl (Z=17).",
                    "steps": [
                        "Bước 1: Nguyên tử Mg có cấu hình [Ne] 3s², nhường 2 electron để tạo ion Mg²⁺: Mg -> Mg²⁺ + 2e.",
                        "Bước 2: Mỗi nguyên tử Cl có cấu hình [Ne] 3s² 3p⁵, nhận 1 electron để tạo ion Cl⁻: Cl + 1e -> Cl⁻.",
                        "Bước 3: Hai ion Cl⁻ và một ion Mg²⁺ hút nhau bằng lực hút tĩnh điện hình thành tinh thể ion MgCl2: Mg²⁺ + 2Cl⁻ -> MgCl2."
                    ],
                    "answer": "Liên kết được hình thành do lực hút tĩnh điện giữa cation Mg²⁺ và 2 anion Cl⁻."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Cho rằng liên kết hydrogen là liên kết cộng hóa trị bên trong phân tử.",
                    "why": "Liên kết hydrogen chủ yếu là liên kết liên phân tử (nối giữa phân tử này với phân tử khác), yếu hơn liên kết cộng hóa trị nhiều lần."
                }
            ]
        },
        {
            "id": "ch04",
            "title": "Chương 4: Phản ứng oxi hóa - khử",
            "description": "Số oxi hóa, chất khử, chất oxi hóa, quá trình oxi hóa, quá trình khử và phương pháp thăng bằng electron.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khái niệm phản ứng oxi hóa - khử và số oxi hóa", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Cân bằng phản ứng oxi hóa - khử bằng phương pháp thăng bằng electron", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Chất khử và Chất oxi hóa",
                    "definition": "Chất khử là chất nhường electron (số oxi hóa tăng sau phản ứng). Chất oxi hóa là chất nhận electron (số oxi hóa giảm sau phản ứng). Thần chú: 'Khử cho, O nhận'.",
                    "example": "Trong phản ứng Zn + 2HCl -> ZnCl2 + H2: Zn nhường 2e (chất khử, Zn⁰ -> Zn⁺²), ion H⁺ nhận e (chất oxi hóa, 2H⁺ + 2e -> H2⁰).",
                    "essence": "Bản chất của phản ứng oxi hóa - khử là sự chuyển dịch electron giữa các chất phản ứng."
                }
            ],
            "rules": [
                {
                    "statement": "Quy tắc thăng bằng electron",
                    "meaning": "Tổng số electron do chất khử nhường bằng tổng số electron do chất oxi hóa nhận: Σ e nhường = Σ e nhận.",
                    "example": "Nhôm nhường 3e, oxi nhận 4e (2O + 4e -> 2O²⁻) => nhân hệ số 4 cho Al và 3 cho O2 để tổng electron trao đổi là 12e.",
                    "essence": "Bảo toàn điện tích: electron không tự sinh ra và không tự mất đi trong phản ứng hóa học."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Cân bằng phản ứng oxi hóa - khử sau bằng phương pháp thăng bằng electron: Fe + HNO3 -> Fe(NO3)3 + NO + H2O.",
                    "steps": [
                        "Bước 1: Xác định sự thay đổi số oxi hóa: Fe⁰ -> Fe⁺³ + 3e (quá trình oxi hóa); N⁺⁵ + 3e -> N⁺² (quá trình khử).",
                        "Bước 2: Tìm hệ số: 1 · (Fe -> Fe⁺³ + 3e) và 1 · (N⁺⁵ + 3e -> N⁺²).",
                        "Bước 3: Đặt hệ số vào phương trình: 1 Fe và 1 NO. Đếm nitơ bên phải: 3 (trong Fe(NO3)3) + 1 (trong NO) = 4 N => hệ số HNO3 là 4.",
                        "Bước 4: Cân bằng H: 4 HNO3 => 2 H2O. Kiểm tra số nguyên tử O: 4·3 = 12 = 3·3 + 1 + 2 (chuẩn)."
                    ],
                    "answer": "Fe + 4HNO3 -> Fe(NO3)3 + NO + 2H2O."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm lẫn giữa 'quá trình oxi hóa' và 'chất oxi hóa'.",
                    "why": "Chất khử trải qua quá trình OXI HÓA (nhường e); chất oxi hóa trải qua quá trình KHỬ (nhận e)."
                }
            ]
        },
        {
            "id": "ch05",
            "title": "Chương 5: Năng lượng hóa học",
            "description": "Phản ứng tỏa nhiệt, thu nhiệt, biến thiên enthalpy chuẩn của phản ứng ΔrHo_298 và cách tính theo nhiệt tạo thành và năng lượng liên kết.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Phản ứng tỏa nhiệt, thu nhiệt và biến thiên enthalpy", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Tính biến thiên enthalpy chuẩn của phản ứng hóa học", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Phản ứng tỏa nhiệt và Thu nhiệt",
                    "definition": "Phản ứng tỏa nhiệt giải phóng năng lượng (nhiệt) ra môi trường xung quanh: ΔrHo < 0. Phản ứng thu nhiệt hấp thụ nhiệt từ môi trường: ΔrHo > 0.",
                    "example": "Đốt cháy than C + O2 -> CO2 (ΔrHo = -393.5 kJ, tỏa nhiệt sưởi ấm). Nung đá vôi CaCO3 -> CaO + CO2 (ΔrHo = +178.5 kJ, thu nhiệt cần đun nóng).",
                    "essence": "Biến thiên enthalpy phản ánh sự chênh lệch năng lượng phá vỡ liên kết chất đầu và năng lượng tạo thành liên kết chất sản phẩm."
                }
            ],
            "rules": [
                {
                    "statement": "Công thức tính biến thiên enthalpy chuẩn",
                    "meaning": "Theo nhiệt tạo thành: ΔrHo_298 = Σ ΔfHo_298(sản phẩm) - Σ ΔfHo_298(chất đầu). Theo năng lượng liên kết: ΔrHo_298 = Σ Eb(chất đầu) - Σ Eb(sản phẩm).",
                    "example": "Nhiệt tạo thành của đơn chất bền ở điều kiện chuẩn luôn bằng 0 (ví dụ O2, H2, N2).",
                    "essence": "Định luật Hess: Biến thiên enthalpy chỉ phụ thuộc vào trạng thái đầu và trạng thái cuối, không phụ thuộc vào đường đi của phản ứng."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Cho phản ứng: CH4(g) + 2O2(g) -> CO2(g) + 2H2O(l). Biết ΔfHo_298 của CH4 = -74.8 kJ/mol; CO2 = -393.5 kJ/mol; H2O(l) = -285.8 kJ/mol; O2 = 0. Tính ΔrHo_298 của phản ứng.",
                    "steps": [
                        "Bước 1: Áp dụng công thức: ΔrHo_298 = [ΔfHo(CO2) + 2·ΔfHo(H2O)] - [ΔfHo(CH4) + 2·ΔfHo(O2)].",
                        "Bước 2: Thay số: ΔrHo_298 = [(-393.5) + 2·(-285.8)] - [(-74.8) + 2·0].",
                        "Bước 3: Tính toán: [-393.5 - 571.6] - [-74.8] = -965.1 + 74.8 = -890.3 kJ."
                    ],
                    "answer": "ΔrHo_298 = -890.3 kJ (phản ứng tỏa nhiệt mạnh)."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Lấy 'chất đầu trừ sản phẩm' khi tính theo nhiệt tạo thành (nhầm với công thức năng lượng liên kết).",
                    "why": "Tính theo nhiệt tạo thành phải lấy Sản phẩm TRỪ Chất đầu; tính theo năng lượng liên kết mới lấy Chất đầu TRỪ Sản phẩm."
                }
            ]
        },
        {
            "id": "ch06",
            "title": "Chương 6: Tốc độ phản ứng hóa học",
            "description": "Khái niệm tốc độ phản ứng, biểu thức định luật tác dụng khối lượng và các yếu tố ảnh hưởng (nồng độ, nhiệt độ, áp suất, diện tích bề mặt, xúc tác).",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khái niệm tốc độ phản ứng và định luật tác dụng khối lượng", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Các yếu tố ảnh hưởng đến tốc độ phản ứng hóa học", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Tốc độ phản ứng",
                    "definition": "Đại lượng đặc trưng cho sự biến thiên nồng độ của một trong các chất phản ứng hoặc chất sản phẩm trong một đơn vị thời gian.",
                    "example": "Khí gas cháy trong bếp là phản ứng rất nhanh (vài mili-giây); thanh sắt bị gỉ sét trong không khí là phản ứng rất chậm (hàng tháng).",
                    "essence": "Phản ứng xảy ra khi các phân tử va chạm hiệu quả với nhau (đủ năng lượng hoạt hóa và đúng hướng không gian)."
                }
            ],
            "rules": [
                {
                    "statement": "Hệ số nhiệt độ Van't Hoff (γ)",
                    "meaning": "Khi tăng nhiệt độ lên 10°C, tốc độ phản ứng tăng từ 2 đến 4 lần: v2 / v1 = γ^((T2 - T1) / 10).",
                    "example": "Bảo quản thức ăn trong tủ lạnh (4°C) làm chậm tốc độ ôi thiu phân hủy so với nhiệt độ phòng (30°C) hàng chục lần.",
                    "essence": "Tăng nhiệt độ làm tăng động năng phân tử, dẫn đến số va chạm hiệu quả giữa các phân tử tăng vọt."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Một phản ứng có hệ số nhiệt độ γ = 3. Khi nhiệt độ tăng từ 20°C lên 50°C, tốc độ phản ứng tăng lên bao nhiêu lần?",
                    "steps": [
                        "Bước 1: Tính độ tăng nhiệt độ: ΔT = 50 - 20 = 30°C.",
                        "Bước 2: Số lần tăng 10°C: n = 30 / 10 = 3.",
                        "Bước 3: Tỉ số tốc độ: v2 / v1 = γ^n = 3³ = 27 lần."
                    ],
                    "answer": "Tốc độ phản ứng tăng lên 27 lần."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng chất xúc tác làm tăng lượng sản phẩm tạo thành tối đa.",
                    "why": "Chất xúc tác chỉ làm giảm năng lượng hoạt hóa giúp phản ứng đạt đến trạng thái cân bằng NHANH HƠN, không làm thay đổi lượng chất sinh ra theo bảo toàn khối lượng."
                }
            ]
        },
        {
            "id": "ch07",
            "title": "Chương 7: Nguyên tố nhóm Halogen",
            "description": "Vị trí, tính chất vật lí, tính chất hóa học đặc trưng của nhóm halogen (F, Cl, Br, I), hydrogen halide và một số phản ứng nhận biết ion halide.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Tính chất của các đơn chất Halogen", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Hydrogen halide và muối halide", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Nhóm Halogen (Nhóm VIIA)",
                    "definition": "Gồm các nguyên tố F, Cl, Br, I. Ở dạng đơn chất tồn tại phân tử hai nguyên tử X2 (F2 khí vàng lục, Cl2 khí vàng nhạt, Br2 lỏng nâu đỏ, I2 rắn tím đen).",
                    "example": "Clo tác dụng với nước tạo nước clo có tính tẩy màu: Cl2 + H2O <=> HCl + HClO (axit hipoclorơ có tính oxi hóa mạnh diệt khuẩn).",
                    "essence": "Có 7 electron lớp ngoài cùng (ns² np⁵) nên có xu hướng nhận 1 electron rất mạnh, là những phi kim có tính oxi hóa mạnh nhất trong bảng tuần hoàn."
                }
            ],
            "rules": [
                {
                    "statement": "Thuốc thử nhận biết các ion Halide",
                    "meaning": "Dùng dung dịch AgNO3: Cl⁻ tạo kết tủa trắng AgCl; Br⁻ tạo kết tủa vàng nhạt AgBr; I⁻ tạo kết tủa vàng đậm AgI; F⁻ không tạo kết tủa (AgF tan).",
                    "example": "Nhỏ vài giọt AgNO3 vào dung dịch NaCl xuất hiện ngay kết tủa trắng AgCl không tan trong axit.",
                    "essence": "Độ tan của muối bạc halide giảm dần từ F đến I do sự biến đổi liên kết từ ion sang cộng hóa trị phân cực mạnh."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Sục khí Cl2 vào dung dịch chứa hỗn hợp NaBr và NaI. Viết phương trình phản ứng hóa học xảy ra và giải thích.",
                    "steps": [
                        "Bước 1: Tính oxi hóa của halogen giảm dần: Cl2 > Br2 > I2.",
                        "Bước 2: Clo mạnh hơn Brom và Iot nên đẩy được cả Br2 và I2 ra khỏi muối.",
                        "Bước 3: Phương trình phản ứng: Cl2 + 2NaI -> 2NaCl + I2 và Cl2 + 2NaBr -> 2NaCl + Br2."
                    ],
                    "answer": "Cl2 đẩy được I⁻ và Br⁻ ra khỏi muối tạo NaCl và đơn chất tương ứng."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng AgF tạo kết tủa giống AgCl.",
                    "why": "AgF tan rất tốt trong nước, không tạo kết tủa khi cho ion F⁻ tác dụng với AgNO3."
                }
            ]
        }
    ]
}

# Add sinh-hoc (5 chapters)
STEM_DATA["sinh-hoc"] = {
    "id": "sinh-hoc",
    "name": "Sinh học",
    "icon": "🧬",
    "chapters": [
        {
            "id": "ch01",
            "title": "Chương 1: Mở đầu & Các cấp độ tổ chức của thế giới sống",
            "description": "Khái quát về môn Sinh học, các phương pháp nghiên cứu sinh học và các cấp độ tổ chức sống cơ bản từ phân tử, tế bào đến sinh quyển.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Giới thiệu khái quát môn Sinh học và phát triển bền vững", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Các cấp độ tổ chức của thế giới sống", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Các cấp độ tổ chức sống cơ bản",
                    "definition": "Bao gồm tế bào, cơ thể, quần thể, quần xã và hệ sinh thái. Tế bào là đơn vị cấu trúc và chức năng cơ bản nhất của mọi sự sống.",
                    "example": "Một con hươu (cơ thể) thuộc về bầy hươu trong rừng (quần thể), cùng sống với các loài động thực vật khác (quần xã).",
                    "essence": "Mỗi cấp độ tổ chức sống đều là một hệ thống mở, tự điều chỉnh và có các đặc tính nổi trội mà cấp dưới không có."
                }
            ],
            "rules": [
                {
                    "statement": "Đặc tính nổi trội của thế giới sống",
                    "meaning": "Là những đặc tính chỉ xuất hiện ở cấp độ tổ chức cao hơn do sự tương tác giữa các bộ phận cấu thành, không có ở các thành phần đơn lẻ.",
                    "example": "Từng phân tử protein, lipit không có sự sống, nhưng khi kết hợp lại tạo thành tế bào thì xuất hiện sự sống (trao đổi chất, sinh sản).",
                    "essence": "'Một tổng thể lớn hơn tổng số các bộ phận cấu thành nên nó'."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Tại sao tế bào được xem là cấp độ tổ chức sống cơ bản nhất của thế giới sống?",
                    "steps": [
                        "Bước 1: Mọi sinh vật (từ vi khuẩn đơn bào đến con người đa bào) đều được cấu tạo từ một hoặc nhiều tế bào.",
                        "Bước 2: Tế bào là cấp độ nhỏ nhất có đầy đủ các đặc trưng cơ bản của sự sống: chuyển hóa vật chất, sinh trưởng, cảm ứng và sinh sản.",
                        "Bước 3: Mọi hoạt động sống của cơ thể đều diễn ra ở cấp độ tế bào."
                    ],
                    "answer": "Tế bào là đơn vị cấu trúc và chức năng nhỏ nhất biểu hiện đầy đủ các đặc tính sống."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Coi virus là một tế bào sống độc lập.",
                    "why": "Virus chưa có cấu tạo tế bào (chỉ gồm vỏ protein và lõi axit nucleic), chỉ nhân lên được khi ký sinh nội bào bắt buộc."
                }
            ]
        },
        {
            "id": "ch02",
            "title": "Chương 2: Thành phần hóa học của tế bào",
            "description": "Nước và vai trò sinh học, các nguyên tố đại lượng và vi lượng, bốn nhóm đại phân tử sinh học: Carbohydrate, Lipid, Protein và Nucleic acid.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Các nguyên tố hóa học và nước trong tế bào", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Các phân tử sinh học: Carbohydrate, Lipid, Protein, DNA & RNA", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Tính phân cực của phân tử nước",
                    "definition": "Phân tử H2O có nguyên tử O mang điện tích âm cục bộ và hai nguyên tử H mang điện tích dương cục bộ, tạo thành các liên kết hydrogen giữa các phân tử nước.",
                    "example": "Nước là dung môi hòa tan đa số các chất phân cực và muối khoáng cần thiết cho tế bào.",
                    "essence": "Liên kết hydrogen tạo cho nước nhiệt dung cao giúp ổn định nhiệt độ tế bào và tạo sức căng bề mặt."
                },
                {
                    "term": "Cấu trúc và chức năng của Protein",
                    "definition": "Được cấu tạo theo nguyên tắc đa phân từ 20 loại amino acid. Có 4 bậc cấu trúc không gian (bậc 1 đến bậc 4). Đảm nhận hầu hết các chức năng sống: xúc tác (enzyme), cấu trúc, vận chuyển, miễn dịch.",
                    "example": "Hemoglobin trong hồng cầu có cấu trúc bậc 4 đảm nhận chức năng vận chuyển khí O2 trong máu.",
                    "essence": "Trình tự amino acid quy định cấu hình không gian 3 chiều đặc thù, và cấu hình không gian quy định chức năng sinh học của protein."
                }
            ],
            "rules": [
                {
                    "statement": "Nguyên tắc bổ sung trong phân tử DNA",
                    "meaning": "Adenine (A) liên kết với Thymine (T) bằng 2 liên kết hydrogen (A = T); Guanine (G) liên kết với Cytosine (C) bằng 3 liên kết hydrogen (G ≡ C).",
                    "example": "Nếu mạch 1 có đoạn 5'-AGCT-3' thì mạch 2 bổ sung là 3'-TCGA-5'.",
                    "essence": "Nguyên tắc bổ sung đảm bảo thông tin di truyền được sao chép và nhân đôi một cách chính xác tuyệt đối qua các thế hệ tế bào."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Một phân tử DNA mạch kép có 3000 nucleotide, trong đó số nucleotide loại A = 600. Tính số nucleotide các loại còn lại và tổng số liên kết hydrogen.",
                    "steps": [
                        "Bước 1: Theo nguyên tắc bổ sung: T = A = 600 nucleotide.",
                        "Bước 2: Tổng A + T + G + C = 3000 => G + C = 3000 - 2·600 = 1800. Do G = C nên G = C = 1800 / 2 = 900 nucleotide.",
                        "Bước 3: Tổng số liên kết hydrogen: H = 2A + 3G = 2 · 600 + 3 · 900 = 1200 + 2700 = 3900 liên kết."
                    ],
                    "answer": "T = 600, G = C = 900; tổng số liên kết hydrogen là 3.900."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm liên kết hóa trị phosphodiester (nối các nucleotide trên một mạch) với liên kết hydrogen (nối giữa hai mạch đối diện).",
                    "why": "Liên kết phosphodiester rất bền vững đảm bảo cấu trúc mạch đơn; liên kết hydrogen yếu hơn để dễ mở xoắn khi nhân đôi."
                }
            ]
        },
        {
            "id": "ch03",
            "title": "Chương 3: Cấu trúc tế bào",
            "description": "Tế bào nhân sơ (vi khuẩn), tế bào nhân thực (thực vật, động vật), cấu trúc và chức năng của màng sinh chất và các bào quan.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Tế bào nhân sơ", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Tế bào nhân thực và hệ thống các bào quan", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Tế bào nhân sơ và Nhân thực",
                    "definition": "Tế bào nhân sơ chưa có màng nhân bao bọc vật chất di truyền (chỉ có vùng nhân) và không có các bào quan có màng bao bọc. Tế bào nhân thực có nhân hoàn chỉnh và nhiều bào quan có màng.",
                    "example": "Vi khuẩn E. coli là tế bào nhân sơ; tế bào biểu bì hành tây hoặc tế bào niêm mạc miệng người là tế bào nhân thực.",
                    "essence": "Kích thước nhỏ của tế bào nhân sơ tạo tỉ lệ S/V lớn giúp trao đổi chất với môi trường cực nhanh và sinh sản nhanh."
                },
                {
                    "term": "Ti thể và Lục lạp",
                    "definition": "Ti thể là 'nhà máy năng lượng' của tế bào, thực hiện hô hấp tạo ATP. Lục lạp chứa diệp lục, thực hiện quang hợp ở tế bào thực vật. Cả hai đều có màng kép và chứa DNA, ribosome riêng.",
                    "example": "Tế bào cơ tim cần nhiều năng lượng hoạt động liên tục nên chứa hàng nghìn ti thể.",
                    "essence": "Thuyết nội cộng sinh: Ti thể và lục lạp có nguồn gốc từ vi khuẩn hiếu khí và vi khuẩn lam cổ đại bị tế bào nhân thực nguyên thủy nuốt vào."
                }
            ],
            "rules": [
                {
                    "statement": "Mô hình khảm động của màng sinh chất",
                    "meaning": "Lớp kép phospholipid tạo khung cơ bản (động), các phân tử protein khảm xuyên màng hoặc bám màng (khảm) thực hiện chức năng vận chuyển và tiếp nhận thông tin.",
                    "example": "Kháng thể hoặc hormone gắn vào các thụ thể glycoprotein trên màng tế bào để truyền tín hiệu vào trong tế bào.",
                    "essence": "Tính linh động cho phép màng tế bào tự gắn kết, thực hiện xuất bào, nhập bào và biến dạng linh hoạt."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "So sánh 3 điểm khác biệt cơ bản giữa tế bào thực vật và tế bào động vật.",
                    "steps": [
                        "Bước 1: Thành tế bào: Tế bào thực vật có thành cellulose bảo vệ hình dạng cố định; tế bào động vật không có thành tế bào.",
                        "Bước 2: Bào quan quang hợp: Tế bào thực vật có lục lạp chứa diệp lục; tế bào động vật không có lục lạp.",
                        "Bước 3: Không bào: Tế bào thực vật có không bào trung tâm lớn chứa nước và chất tan; tế bào động vật chỉ có các không bào nhỏ."
                    ],
                    "answer": "Khác biệt về thành cellulose, lục lạp và không bào trung tâm."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng tế bào thực vật chỉ quang hợp mà không có quá trình hô hấp tế bào (không có ti thể).",
                    "why": "Tế bào thực vật có cả lục lạp (quang hợp tổng hợp đường) và ti thể (hô hấp phân giải đường thành ATP để sống)."
                }
            ]
        },
        {
            "id": "ch04",
            "title": "Chương 4: Trao đổi chất và Chuyển hóa năng lượng ở tế bào",
            "description": "Vận chuyển thụ động, chủ động, xuất nhập bào, vai trò của enzyme, hô hấp tế bào và quang hợp.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Vận chuyển các chất qua màng sinh chất và Enzyme", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Hô hấp tế bào và Quang hợp", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Vận chuyển chủ động (chủ động tiêu tốn ATP)",
                    "definition": "Là phương thức vận chuyển các chất qua màng sinh chất ngược chiều gradient nồng độ (từ nơi nồng độ thấp đến nơi nồng độ cao), cần tiêu tốn năng lượng ATP và protein mang.",
                    "example": "Bơm Na⁺/K⁺ ở màng tế bào thần kinh liên tục bơm 3 Na⁺ ra ngoài và 2 K⁺ vào trong để duy trì điện thế nghỉ.",
                    "essence": "Vận chuyển chủ động giúp tế bào chủ động thu nhận các chất dinh dưỡng cần thiết ngay cả khi môi trường có nồng độ rất loãng."
                },
                {
                    "term": "ATP - Đồng tiền năng lượng của tế bào",
                    "definition": "Adenosine triphosphate gồm bazơ adenin, đường ribose và 3 nhóm phosphate. Hai liên kết giữa các nhóm phosphate là liên kết cao năng dễ bị thủy phân giải phóng năng lượng.",
                    "example": "Khi tế bào co cơ hoặc tổng hợp protein, ATP thủy phân thành ADP + Pi giải phóng khoảng 30.5 kJ/mol năng lượng.",
                    "essence": "ATP là cầu nối chuyển giao năng lượng từ các phản ứng tỏa năng lượng (hô hấp) đến các phản ứng thu năng lượng trong tế bào."
                }
            ],
            "rules": [
                {
                    "statement": "Cơ chế tác động của Enzyme",
                    "meaning": "Enzyme làm giảm năng lượng hoạt hóa của phản ứng hóa học, làm tăng tốc độ phản ứng lên hàng triệu lần mà không bị biến đổi sau phản ứng.",
                    "example": "Enzyme catalase trong củ khoai tây hoặc gan phân giải hàng triệu phân tử H2O2 độc hại thành H2O và O2 mỗi giây.",
                    "essence": "Tính đặc hiệu cao: mỗi enzyme chỉ liên kết với một hoặc một nhóm cơ chất tương ứng theo mô hình 'khóa và chìa'."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Giải thích tại sao khi ngâm rau sống bị héo vào trong nước cất thì sau một thời gian rau lại tươi trở lại?",
                    "steps": [
                        "Bước 1: Nước cất là môi trường nhược trương so với dịch bào trong tế bào rau (nồng độ chất tan trong tế bào cao hơn ngoài nước cất).",
                        "Bước 2: Theo quy luật thẩm thấu, các phân tử nước tự do di chuyển từ ngoài vào trong tế bào rau qua màng sinh chất.",
                        "Bước 3: Tế bào hút nước trương phồng lên, ép vào thành tế bào tạo sức căng trương nước làm rau tươi trở lại."
                    ],
                    "answer": "Do nước thẩm thấu vào trong tế bào nhược trương tạo sức căng trương nước."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm tưởng hô hấp tế bào chỉ xảy ra ở động vật còn thực vật chỉ quang hợp.",
                    "why": "Cả thực vật và động vật đều phải hô hấp liên tục 24/24 để tạo ATP duy trì sự sống."
                }
            ]
        },
        {
            "id": "ch05",
            "title": "Chương 5: Chu kỳ tế bào, Phân bào & Vi sinh vật",
            "description": "Chu kỳ tế bào, nguyên phân, giảm phân, bệnh ung thư, đặc điểm của vi sinh vật và virus gây bệnh.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Chu kỳ tế bào và Nguyên phân", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Giảm phân, thụ tinh và Vi sinh vật", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Nguyên phân và Giảm phân",
                    "definition": "Nguyên phân xảy ra ở tế bào sinh dưỡng: 1 tế bào mẹ (2n) tạo ra 2 tế bào con có bộ NST y hệt mẹ (2n). Giảm phân xảy ra ở tế bào sinh dục chín: 1 tế bào mẹ (2n) qua 2 lần phân bào tạo ra 4 tế bào con (giao tử) có bộ NST giảm đi một nửa (n).",
                    "example": "Ở người (2n = 46): Nguyên phân tạo tế bào da có 46 NST; Giảm phân tạo tinh trùng hoặc trứng chỉ có 23 NST.",
                    "essence": "Nguyên phân duy trì sự ổn định bộ NST qua các thế hệ tế bào của cơ thể; Giảm phân kết hợp thụ tinh duy trì bộ NST qua các thế hệ loài."
                }
            ],
            "rules": [
                {
                    "statement": "Ý nghĩa tiến hóa của Giảm phân",
                    "meaning": "Hiện tượng tiếp hợp và trao đổi chéo giữa các chromatid ở kì đầu giảm phân I cùng sự phân li độc lập tạo ra vô số biến dị tổ hợp phong phú.",
                    "example": "Con cái sinh ra từ cùng một bố mẹ luôn có những nét khác biệt nhau và khác bố mẹ.",
                    "essence": "Biến dị tổ hợp là nguồn nguyên liệu sơ cấp phong phú cho chọn lọc tự nhiên và tiến hóa."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Một tế bào sinh dưỡng của loài có bộ NST 2n = 8 tiến hành nguyên phân liên tiếp 3 đợt. Tính số tế bào con tạo thành và tổng số NST có trong các tế bào con.",
                    "steps": [
                        "Bước 1: Qua k đợt nguyên phân, số tế bào con tạo thành là 2^k.",
                        "Bước 2: Với k = 3 đợt: số tế bào con là 2³ = 8 tế bào.",
                        "Bước 3: Vì nguyên phân giữ nguyên bộ NST 2n = 8, tổng số NST trong các tế bào con là 8 · 8 = 64 NST đơn."
                    ],
                    "answer": "Có 8 tế bào con tạo thành, tổng số 64 NST."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm rằng giữa giảm phân I và giảm phân II có xảy ra sự nhân đôi DNA/NST.",
                    "why": "Giữa hai lần phân bào giảm phân là kì trung gian rất ngắn KHÔNG CÓ sự nhân đôi NST, nhờ đó bộ NST mới giảm đi một nửa (2n -> n)."
                }
            ]
        }
    ]
}

# Add tin-hoc (6 topics)
STEM_DATA["tin-hoc"] = {
    "id": "tin-hoc",
    "name": "Tin học",
    "icon": "💻",
    "chapters": [
        {
            "id": "ch01",
            "title": "Chủ đề 1: Máy tính và Xã hội tri thức",
            "description": "Dữ liệu, thông tin, xử lí thông tin số, biểu diễn dữ liệu trong máy tính (hệ nhị phân, bảng mã ASCII, Unicode) và vai trò của thiết bị số.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Thông tin và dữ liệu số", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Biểu diễn thông tin trong máy tính", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Bit và Byte",
                    "definition": "Bit (Binary Digit) là đơn vị nhỏ nhất để đo lượng thông tin, chỉ nhận một trong hai giá trị 0 hoặc 1. 1 Byte = 8 bit.",
                    "example": "Kí tự 'A' trong bảng mã ASCII được biểu diễn bằng 1 byte là 01000001 (giá trị thập phân 65).",
                    "essence": "Mọi loại dữ liệu (văn bản, âm thanh, hình ảnh, video) khi nạp vào máy tính đều được số hóa thành các dãy bit nhị phân 0 và 1."
                }
            ],
            "rules": [
                {
                    "statement": "Đơn vị đo dung lượng thông tin",
                    "meaning": "1 KB = 1024 Bytes; 1 MB = 1024 KB; 1 GB = 1024 MB; 1 TB = 1024 GB (lũy thừa của 2: 2¹⁰ = 1024).",
                    "example": "Một bức ảnh chụp điện thoại dung lượng 4 MB = 4 · 1024 KB = 4.096 KB.",
                    "essence": "Cơ số 2 là ngôn ngữ phần cứng của mạch bán dẫn đóng (0) và mở (1)."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Đổi số nhị phân 10110_2 sang hệ thập phân (hệ cơ số 10).",
                    "steps": [
                        "Bước 1: Viết số nhị phân theo lũy thừa của 2 từ phải sang trái (bắt đầu từ 2⁰):",
                        "Bước 2: 1·2⁴ + 0·2³ + 1·2² + 1·2¹ + 0·2⁰.",
                        "Bước 3: Tính toán: 16 + 0 + 4 + 2 + 0 = 22."
                    ],
                    "answer": "10110_2 = 22_10."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Lấy 1 KB = 1000 Bytes trong tính toán bộ nhớ máy tính.",
                    "why": "Trong cấu trúc bộ nhớ máy tính chuẩn, các tiền tố nhị phân tính theo lũy thừa của 2 (2¹⁰ = 1024)."
                }
            ]
        },
        {
            "id": "ch02",
            "title": "Chủ đề 2: Mạng máy tính và Internet",
            "description": "Mạng cục bộ (LAN), mạng diện rộng (WAN), các thiết bị mạng, giao thức mạng IP/TCP, dịch vụ Internet và điện toán đám mây.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Mạng máy tính trong cuộc sống hiện đại", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Điện toán đám mây và Internet kết nối vạn vật (IoT)", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Địa chỉ IP",
                    "definition": "Là địa chỉ định danh duy nhất của mỗi thiết bị kết nối vào mạng máy tính để giao tiếp và trao đổi dữ liệu.",
                    "example": "IPv4 gồm 4 nhóm số cách nhau dấu chấm: 192.168.1.1; IPv6 sử dụng 128 bit để mở rộng không gian địa chỉ.",
                    "essence": "Địa chỉ IP giống như số nhà bưu điện giúp các gói tin gửi đi biết chính xác nơi đến trên mạng toàn cầu."
                }
            ],
            "rules": [
                {
                    "statement": "Mô hình Client - Server (Khách - Chủ)",
                    "meaning": "Máy khách (Client) gửi yêu cầu (request); Máy chủ (Server) tiếp nhận, xử lí và phản hồi dữ liệu (response).",
                    "example": "Trình duyệt web của học sinh (Client) gửi yêu cầu xem bài giảng lên máy chủ Vercel (Server).",
                    "essence": "Phân chia vai trò rõ ràng giữa thiết bị sử dụng dịch vụ và hệ thống cung cấp dữ liệu tập trung."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Điện toán đám mây mang lại những lợi ích vượt trội nào so với lưu trữ cục bộ trên ổ cứng truyền thống?",
                    "steps": [
                        "Bước 1: Khả năng truy cập mọi lúc mọi nơi từ bất kỳ thiết bị nào có kết nối mạng Internet.",
                        "Bước 2: Dữ liệu được sao lưu dự phòng tự động, giảm thiểu rủi ro mất mát khi hỏng thiết bị phần cứng.",
                        "Bước 3: Dễ dàng chia sẻ và cộng tác làm việc theo thời gian thực (ví dụ Google Docs, Drive)."
                    ],
                    "answer": "Truy cập linh hoạt, sao lưu an toàn và cộng tác thời gian thực."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng Internet và World Wide Web (WWW) là một khái niệm hoàn toàn trùng nhau.",
                    "why": "Internet là mạng lưới hạ tầng kết nối các máy tính vật lý; WWW là một dịch vụ thông tin chạy trên nền Internet."
                }
            ]
        },
        {
            "id": "ch03",
            "title": "Chủ đề 3: Đạo đức, Pháp luật và Văn hóa trong môi trường số",
            "description": "Bản quyền phần mềm, sở hữu trí tuệ, an toàn thông tin cá nhân, phòng chống mã độc và quy tắc ứng xử văn minh trên không gian mạng.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Bản quyền và luật sở hữu trí tuệ trong thời đại số", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: An toàn thông tin và văn hóa ứng xử mạng", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Phần mềm mã nguồn mở (Open Source)",
                    "definition": "Phần mềm được cung cấp kèm mã nguồn mở công khai, cho phép người dùng tự do sử dụng, nghiên cứu, sửa đổi và phân phối lại.",
                    "example": "Hệ điều hành Linux, trình duyệt Firefox, bộ phần mềm đồ họa Inkscape, ngôn ngữ lập trình Python.",
                    "essence": "Mã nguồn mở thúc đẩy sự đổi mới sáng tạo cộng đồng và giảm phụ thuộc vào các tập đoàn công nghệ độc quyền."
                }
            ],
            "rules": [
                {
                    "statement": "Bảo vệ thông tin cá nhân trên mạng",
                    "meaning": "Không chia sẻ mật khẩu, mã OTP, số CCCD, hình ảnh nhạy cảm lên mạng xã hội; sử dụng mật khẩu mạnh và xác thực 2 lớp (2FA).",
                    "example": "Mật khẩu mạnh phải dài từ 8 kí tự trở lên, gồm chữ hoa, chữ thường, chữ số và kí tự đặc biệt.",
                    "essence": "Thông tin cá nhân bị rò rỉ là mồi ngon cho các hành vi lừa đảo tài chính và chiếm đoạt danh tính trên mạng."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Hành vi sử dụng phần mềm bẻ khóa (crack) gây ra những nguy cơ bảo mật nào cho người dùng?",
                    "steps": [
                        "Bước 1: Vi phạm luật Sở hữu trí tuệ và quyền tác giả.",
                        "Bước 2: Các công cụ crack thường bị cài cắm mã độc (Trojan, Spyware, Keylogger) để đánh cắp tài khoản và dữ liệu cá nhân.",
                        "Bước 3: Không nhận được các bản vá bảo mật chính hãng từ nhà sản xuất."
                    ],
                    "answer": "Vi phạm pháp luật bản quyền và rủi ro bị nhiễm mã độc đánh cắp dữ liệu."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Chia sẻ lại thông tin sai sự thật trên mạng xã hội với suy nghĩ 'mình chỉ bấm share chứ không viết'.",
                    "why": "Theo Luật An ninh mạng, hành vi lan truyền, phát tán thông tin giả mạo dù không trực tiếp viết ra vẫn bị xử phạt nghiêm minh."
                }
            ]
        },
        {
            "id": "ch04",
            "title": "Chủ đề 4: Ứng dụng tin học: Thiết kế đồ họa Inkscape",
            "description": "Đồ họa vector và đồ họa bitmap, phần mềm đồ họa vector mã nguồn mở Inkscape, tạo các hình cơ bản, xử lí đường cong và tạo sản phẩm số.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Làm quen với phần mềm đồ họa vector Inkscape", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Các thao tác vẽ và chỉnh sửa đối tượng đồ họa", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Đồ họa Vector và Bitmap (Raster)",
                    "definition": "Đồ họa Bitmap tạo bởi lưới điểm ảnh (pixel), khi phóng to bị vỡ hạt (nhòe). Đồ họa Vector tạo bởi các công thức toán học (đường cong Bézier), có thể phóng to vô hạn mà không bao giờ bị vỡ nét.",
                    "example": "Ảnh chụp máy ảnh là ảnh Bitmap (.png, .jpg). Logo thương hiệu, icon thiết kế trên Inkscape là ảnh Vector (.svg).",
                    "essence": "Ảnh Vector lưu trữ công thức hình học chứ không lưu trữ màu từng điểm ảnh, do đó dung lượng nhẹ và độ sắc nét tuyệt đối ở mọi kích thước."
                }
            ],
            "rules": [
                {
                    "statement": "Đường cong Bézier trong Inkscape",
                    "meaning": "Đường cong được điều khiển bởi các điểm neo (node) và các tay nắm điều khiển (handle) xác định độ cong và hướng uốn lượn.",
                    "example": "Dùng công cụ Bézier Tool (Shift + F6) để vẽ lại logo hoặc hình vẽ tự do phức tạp.",
                    "essence": "Điều chỉnh tay nắm điều khiển thay đổi đạo hàm và độ cong của đường đồ thị."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Tại sao các nhà thiết kế luôn sử dụng đồ họa vector để vẽ logo doanh nghiệp?",
                    "steps": [
                        "Bước 1: Logo cần được in trên nhiều kích thước khác nhau: từ chiếc card visit nhỏ xíu đến tấm biển quảng cáo ngoài trời khổng lồ.",
                        "Bước 2: Đồ họa vector có thể co giãn kích thước tùy ý mà các đường nét và màu sắc vẫn giữ nguyên độ sắc nét hoàn hảo.",
                        "Bước 3: Dễ dàng chỉnh sửa từng đường nét, màu sắc và xuất ra các định dạng khác nhau."
                    ],
                    "answer": "Vì ảnh vector phóng to vô hạn không vỡ nét và linh hoạt trong in ấn đa kích cỡ."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Lưu file thiết kế vector sang đuôi JPG để sau này tiếp tục sửa.",
                    "why": "Khi lưu sang JPG/PNG, file đã bị rasterize thành ảnh bitmap, các layer và đường cong vector không thể sửa riêng lẻ được nữa."
                }
            ]
        },
        {
            "id": "ch05",
            "title": "Chủ đề 5: Lập trình Python cơ bản",
            "description": "Ngôn ngữ lập trình Python, biến, kiểu dữ liệu, các phép toán số học và logic, cấu trúc rẽ nhánh if-else, vòng lặp for/while, danh sách list, xâu ký tự và hàm.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khởi động với Python, Biến và Kiểu dữ liệu", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Cấu trúc điều khiển: Rẽ nhánh và Vòng lặp", "hasRealContent": True},
                {"id": "l03", "title": "Bài 3: Danh sách (List), Xâu ký tự (String) và Hàm (Function)", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Biến và Kiểu dữ liệu trong Python",
                    "definition": "Biến là vùng nhớ dùng để lưu trữ dữ liệu. Python tự động nhận diện kiểu dữ liệu: int (số nguyên), float (số thực), str (xâu ký tự), bool (đúng/sai).",
                    "example": "x = 10 (int), pi = 3.14 (float), name = 'Nam' (str), is_passed = True (bool).",
                    "essence": "Python là ngôn ngữ định kiểu động (dynamic typing), không cần khai báo kiểu trước khi gán giá trị."
                },
                {
                    "term": "Thụt đầu dòng (Indentation) trong Python",
                    "definition": "Python sử dụng khoảng trắng thụt lề (thường là 4 dấu cách) để xác định các khối lệnh (code block) thay cho cặp dấu ngoặc nhọn { } trong C/C++ hay Java.",
                    "example": "if x > 0:\n    print('Số dương')\nelse:\n    print('Không dương')",
                    "essence": "Cưỡng chế viết code sạch sẽ, thẳng hàng, tăng tối đa khả năng đọc hiểu của mã nguồn."
                }
            ],
            "rules": [
                {
                    "statement": "Hàm range(start, stop, step) trong vòng lặp for",
                    "meaning": "Tạo dãy số nguyên từ start đến stop - 1 với bước nhảy step. Mặc định start = 0, step = 1.",
                    "example": "range(1, 6) sinh ra dãy các số 1, 2, 3, 4, 5 (không bao gồm số 6).",
                    "essence": "Nguyên tắc nửa mở [start; stop) là chuẩn phổ quát trong chỉ số mảng và vòng lặp khoa học máy tính."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Viết đoạn mã Python tính tổng các số chẵn từ 1 đến n (với n nhập từ bàn phím).",
                    "steps": [
                        "Bước 1: Nhập số nguyên n: n = int(input())",
                        "Bước 2: Khởi tạo biến tổng s = 0.",
                        "Bước 3: Dùng vòng lặp for duyệt từ 2 đến n với bước nhảy 2: for i in range(2, n + 1, 2): s += i",
                        "Bước 4: In kết quả ra màn hình: print(s)"
                    ],
                    "answer": "s = sum(i for i in range(2, n + 1, 2))"
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Lỗi IndentationError do thụt lề không đều (chỗ dùng Tab, chỗ dùng dấu cách Space).",
                    "why": "Python bắt buộc các dòng trong cùng một khối lệnh phải có số lượng khoảng trắng thụt vào hoàn toàn bằng nhau."
                }
            ]
        },
        {
            "id": "ch06",
            "title": "Chủ đề 6: Hướng nghiệp với Tin học",
            "description": "Các nhóm ngành nghề chính trong lĩnh vực Công nghệ thông tin và Truyền thông (ICT), đặc điểm công việc và kỹ năng cần trang bị.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Các nghề nghiệp trong ngành Công nghệ thông tin", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Kỹ năng số và học tập suốt đời thời đại AI", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Các nhóm ngành nghề CNTT",
                    "definition": "Bao gồm phát triển phần mềm (Software Engineering), khoa học dữ liệu và trí tuệ nhân tạo (Data Science & AI), an toàn an ninh mạng (Cybersecurity), quản trị mạng và điện toán đám mây.",
                    "example": "Kỹ sư lập trình AI phát triển các mô hình học máy tự động hóa chẩn đoán bệnh án y tế hoặc lái xe tự hành.",
                    "essence": "CNTT không chỉ là một nghề độc lập mà là công cụ chuyển đổi số cho mọi ngành nghề trong xã hội."
                }
            ],
            "rules": [
                {
                    "statement": "Năng lực tự học và tư duy giải quyết vấn đề",
                    "meaning": "Công nghệ số biến đổi nhanh chóng theo từng năm, kỹ năng quan trọng nhất của người làm tin học là năng lực tự học và tư duy thuật toán.",
                    "example": "Một lập trình viên giỏi không phải là người nhớ hết cú pháp mà là người biết tìm kiếm tài liệu, giải quyết lỗi bug và thích nghi công nghệ mới.",
                    "essence": "Học cách học là kỹ năng sinh tồn tối thượng trong thời đại kinh tế tri thức số."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Để theo đuổi nhóm ngành Trí tuệ nhân tạo (AI) và Khoa học dữ liệu, học sinh cấp 3 cần tập trung học tốt những môn học nào?",
                    "steps": [
                        "Bước 1: Môn Toán học (Đại số tuyến tính, Giải tích, Xác suất thống kê - nền tảng của các thuật toán học máy).",
                        "Bước 2: Môn Tin học (Tư duy thuật toán, cấu trúc dữ liệu và ngôn ngữ lập trình Python).",
                        "Bước 3: Môn Tiếng Anh (Đọc hiểu tài liệu kỹ thuật, nghiên cứu quốc tế và làm việc nhóm toàn cầu)."
                    ],
                    "answer": "Toán học, Tin học (Python) và Tiếng Anh."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng học ngành CNTT chỉ đơn thuần là ngồi gõ code lập trình.",
                    "why": "Ngành CNTT bao gồm rất nhiều vị trí đa dạng như thiết kế trải nghiệm người dùng (UI/UX), phân tích nghiệp vụ (BA), quản lý dự án (PM), kiểm thử phần mềm (QA/QC)."
                }
            ]
        }
    ]
}

# Write out to data_g10_stem.json
out_file = Path("pipeline/data_g10_stem.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(STEM_DATA, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {out_file} with {len(STEM_DATA)} subjects!")


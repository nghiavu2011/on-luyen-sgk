# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa 5 môn Khoa học Tự nhiên & STEM Lớp 12 SGK Kết nối tri thức 2026-2027:
- Toán học (6 chương: Ứng dụng đạo hàm, Toạ độ vectơ Oxyz, Đo mức độ phân tán số liệu ghép nhóm, Nguyên hàm - Tích phân, Phương pháp toạ độ Oxyz, Xác suất có điều kiện)
- Vật lí (4 chương: Vật lí nhiệt, Khí lí tưởng, Từ trường, Vật lí hạt nhân)
- Hóa học (8 chương: Ester - Lipid, Carbohydrate, Hợp chất Nitrogen, Polymer, Pin điện - Điện phân, Đại cương kim loại, Nhóm IA & IIA, Kim loại chuyển tiếp dãy thứ nhất & Phức chất)
- Sinh học (6 chương: Di truyền phân tử & NST, Di truyền quần thể & người, Ứng dụng di truyền học & CNSH, Tiến hóa, Sinh thái học cá thể & quần thể, Quần xã & Hệ sinh thái)
- Tin học (7 chủ đề: AI trong đời sống, Mạng máy tính & TCP/IP, Văn hóa số, Thiết kế web HTML/CSS, Hướng nghiệp CNTT, Thiết bị mạng & Thiết kế mạng, Học máy & KH Dữ liệu)
"""

true = True
false = False
null = None

STEM_SUBJECTS = {
  "toan": {
    "id": "toan",
    "name": "Toán học",
    "icon": "📐",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị của hàm số",
        "description": "Tính đơn điệu, cực trị, giá trị lớn nhất và nhỏ nhất của hàm số, đường tiệm cận của đồ thị hàm số và ứng dụng khảo sát giải quyết bài toán tối ưu thực tế.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tính đơn điệu và cực trị của hàm số", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Giá trị lớn nhất và giá trị nhỏ nhất của hàm số", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Đường tiệm cận của đồ thị hàm số", "hasRealContent": true },
          { "id": "l04", "title": "Bài 4: Khảo sát sự biến thiên và vẽ đồ thị của hàm số", "hasRealContent": true },
          { "id": "l05", "title": "Bài 5: Ứng dụng đạo hàm để giải quyết một số vấn đề thực tiễn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tính đơn điệu của hàm số",
            "definition": "Cho hàm số y = f(x) có đạo hàm trên khoảng K. Nếu f'(x) ≥ 0 với mọi x thuộc K (dấu bằng chỉ xảy ra tại hữu hạn điểm) thì hàm số đồng biến trên K. Nếu f'(x) ≤ 0 với mọi x thuộc K thì hàm số nghịch biến trên K.",
            "example": "Xét y = x³ - 3x + 1 có y' = 3x² - 3 = 3(x - 1)(x + 1). Hàm số đồng biến trên (-∞; -1) và (1; +∞), nghịch biến trên (-1; 1).",
            "essence": "Dấu của đạo hàm bậc nhất f'(x) quyết định trực tiếp chiều biến thiên dốc lên hay dốc xuống của đồ thị hàm số."
          },
          {
            "term": "Đường tiệm cận của đồ thị hàm số",
            "definition": "Đường thẳng y = y₀ là tiệm cận ngang nếu lim_{x→+∞} f(x) = y₀ hoặc lim_{x→-∞} f(x) = y₀. Đường thẳng x = x₀ là tiệm cận đứng nếu ít nhất một trong các giới hạn một bên khi x tiến về x₀ bằng vô cực (±∞). Đường thẳng y = ax + b (a ≠ 0) là tiệm cận xiên nếu lim_{x→±∞} [f(x) - (ax + b)] = 0.",
            "example": "Đồ thị hàm số y = (2x + 1)/(x - 1) có tiệm cận đứng là x = 1 (mẫu bằng 0) và tiệm cận ngang là y = 2 (tỉ số hệ số bậc cao nhất).",
            "essence": "Tiệm cận mô tả xu thế tiệm cận không giới hạn của quỹ đạo đồ thị khi các biến số tiến ra xa vô tận hoặc chạm vào điểm gián đoạn."
          }
        ],
        "rules": [
          {
            "statement": "Định lý điều kiện cần và đủ của cực trị hàm số",
            "meaning": "Nếu f'(x₀) = 0 (hoặc f'(x₀) không xác định) và f'(x) đổi dấu từ dương sang âm khi qua x₀ thì x₀ là điểm cực đại. Nếu f'(x) đổi dấu từ âm sang dương khi qua x₀ thì x₀ là điểm cực tiểu.",
            "example": "Xét f(x) = x² - 4x + 5 có f'(x) = 2x - 4 = 0 ⇔ x = 2. Khi x qua 2, f'(x) đổi dấu từ âm sang dương, nên x = 2 là điểm cực tiểu với y_CT = 1.",
            "essence": "Cực trị là điểm đảo chiều của xu thế biến thiên, đòi hỏi đạo hàm phải thực sự đổi dấu qua điểm tới hạn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một người nông dân có 120 mét rào lưới thép muốn rào một khu vườn hình chữ nhật sát một bờ sông thẳng (không cần rào bờ sông). Tìm kích thước khu vườn để diện tích rào được là lớn nhất.",
            "steps": [
              "Bước 1: Gọi x (m) là chiều rộng của khu vườn vuông góc với bờ sông (0 < x < 60). Khi đó chiều dài song song với bờ sông là 120 - 2x (m).",
              "Bước 2: Diện tích khu vườn là S(x) = x(120 - 2x) = 120x - 2x² (m²).",
              "Bước 3: Lấy đạo hàm S'(x) = 120 - 4x. Cho S'(x) = 0 ⇔ x = 30 (nhận vì thuộc khoảng (0; 60)).",
              "Bước 4: Vì S''(x) = -4 < 0 nên tại x = 30 diện tích đạt cực đại: S_max = S(30) = 30 · 60 = 1800 m²."
            ],
            "answer": "Kích thước tối ưu: chiều rộng 30 m, chiều dài 60 m; diện tích cực đại đạt 1800 m²."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Kết luận x₀ là điểm cực trị chỉ vì f'(x₀) = 0 mà không kiểm tra f'(x) có đổi dấu qua x₀ hay không.",
            "why": "Điển hình hàm số y = x³ có y' = 3x² = 0 tại x = 0 nhưng y' ≥ 0 với mọi x nên đồ thị luôn đồng biến và không có cực trị."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Toạ độ của vectơ trong không gian",
        "description": "Vectơ và các phép toán trong không gian Oxyz, hệ trục toạ độ không gian, toạ độ của điểm và vectơ, tích vô hướng và ứng dụng tính góc, khoảng cách.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vectơ và các phép toán trong không gian", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hệ toạ độ trong không gian", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Biểu thức toạ độ của các phép toán vectơ", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hệ toạ độ Oxyz trong không gian",
            "definition": "Gồm 3 trục Ox, Oy, Oz vuông góc với nhau từng đôi một tại gốc O. Mỗi điểm M được xác định duy nhất bởi bộ ba số (x; y; z) sao cho vectơ OM = x·i + y·j + z·k với i, j, k là các vectơ đơn vị.",
            "example": "Gốc tọa độ O(0; 0; 0), điểm nằm trên trục Ox có toạ độ (x; 0; 0), điểm thuộc mặt phẳng (Oxy) có toạ độ (x; y; 0).",
            "essence": "Hệ tọa độ Oxyz đại số hóa hình học không gian 3 chiều, chuyển bài toán chứng minh hình học thuần túy thành các phép tính số học chuẩn xác."
          },
          {
            "term": "Tích vô hướng của hai vectơ trong không gian",
            "definition": "Cho u = (x₁; y₁; z₁) và v = (x₂; y₂; z₂). Tích vô hướng u · v = x₁x₂ + y₁y₂ + z₁z₂ = |u| · |v| · cos(u, v).",
            "example": "Nếu u = (1; 2; -2) và v = (2; -1; 0) thì u · v = 1·2 + 2·(-1) + (-2)·0 = 0, suy ra hai vectơ u và v vuông góc với nhau.",
            "essence": "Tích vô hướng là công cụ then chốt để đo góc giữa hai vectơ và kiểm tra điều kiện vuông góc: u ⊥ v ⇔ u · v = 0."
          }
        ],
        "rules": [
          {
            "statement": "Công thức độ dài vectơ và khoảng cách giữa hai điểm",
            "meaning": "Độ dài vectơ u = (x; y; z) là |u| = √(x² + y² + z²). Khoảng cách giữa A(x_A; y_A; z_A) và B(x_B; y_B; z_B) là AB = √[(x_B - x_A)² + (y_B - y_A)² + (z_B - z_A)²].",
            "example": "Khoảng cách từ gốc O(0; 0; 0) đến M(2; 3; 6) là OM = √(2² + 3² + 6²) = √(4 + 9 + 36) = √49 = 7.",
            "essence": "Là định lý Pythagore mở rộng trong không gian ba chiều Euclid."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trong không gian Oxyz, cho A(1; 0; 2), B(2; -1; 3) và C(0; 2; 1). Tính góc giữa hai vectơ AB và AC?",
            "steps": [
              "Bước 1: Tìm toạ độ: AB = (2-1; -1-0; 3-2) = (1; -1; 1); AC = (0-1; 2-0; 1-2) = (-1; 2; -1).",
              "Bước 2: Tính tích vô hướng: AB · AC = 1·(-1) + (-1)·2 + 1·(-1) = -1 - 2 - 1 = -4.",
              "Bước 3: Tính độ dài: |AB| = √(1² + (-1)² + 1²) = √3; |AC| = √((-1)² + 2² + (-1)²) = √6.",
              "Bước 4: Tính cosin: cos(AB, AC) = (AB · AC) / (|AB| · |AC|) = -4 / (√3 · √6) = -4 / (3√2) = -2√2 / 3."
            ],
            "answer": "cos(AB, AC) = -2√2 / 3, góc giữa AB và AC là arccos(-2√2 / 3) ≈ 160.53°."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy toạ độ vectơ ngược thứ tự: lấy toạ độ điểm đầu trừ toạ độ điểm cuối.",
            "why": "Quy tắc chuẩn: Vectơ AB = B - A (toạ độ ngọn trừ toạ độ gốc)."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm",
        "description": "Khoảng biến thiên, khoảng tứ phân vị, phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm; ý nghĩa thực tế trong phân tích rủi ro và đánh giá chất lượng.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khoảng biến thiên và khoảng tứ phân vị của mẫu số liệu ghép nhóm", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Mẫu số liệu ghép nhóm",
            "definition": "Là mẫu số liệu được chia thành các nhóm liên tiếp dạng [a_i; a_{i+1}) cùng với tần số m_i tương ứng với mỗi nhóm.",
            "example": "Thống kê chiều cao 100 học sinh lớp 12: nhóm [150; 155) có 12 em, nhóm [155; 160) có 28 em, nhóm [160; 165) có 35 em...",
            "essence": "Ghép nhóm giúp thu gọn lượng dữ liệu quan sát lớn thành các khoảng đặc trưng dễ tính toán và trực quan hóa phân bố."
          },
          {
            "term": "Phương sai và độ lệch chuẩn của mẫu số liệu ghép nhóm",
            "definition": "Phương sai s² = (1/n) · ∑ m_i · (c_i - x̄)², trong đó c_i là giá trị đại diện (trung điểm) của nhóm thứ i, x̄ là số trung bình, n là kích thước mẫu. Độ lệch chuẩn s = √(s²).",
            "example": "Độ lệch chuẩn điểm thi môn Toán của lớp A là s = 0.8 điểm (điểm đều), trong khi lớp B là s = 1.8 điểm (điểm phân tán mạnh, học lực không đều).",
            "essence": "Độ lệch chuẩn đo lường mức độ phân tán của các số liệu xung quanh giá trị trung bình; độ lệch chuẩn càng nhỏ thì tập dữ liệu càng ổn định và đồng đều."
          }
        ],
        "rules": [
          {
            "statement": "Công thức tính giá trị đại diện của nhóm ghép nhóm",
            "meaning": "Giá trị đại diện của nhóm [a_i; a_{i+1}) là trung bình cộng hai đầu mút: c_i = (a_i + a_{i+1}) / 2.",
            "example": "Nhóm [20; 30) có giá trị đại diện là c = (20 + 30) / 2 = 25.",
            "essence": "Giá trị đại diện thay thế cho toàn bộ các cá thể trong khoảng đó để tính toán số trung bình và phương sai."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho mẫu số liệu ghép nhóm về thời gian tự học (giờ/tuần) của 20 học sinh: [5; 10): 4 học sinh; [10; 15): 10 học sinh; [15; 20): 6 học sinh. Tính số trung bình x̄ và phương sai s²?",
            "steps": [
              "Bước 1: Xác định giá trị đại diện: c₁ = 7.5; c₂ = 12.5; c₃ = 17.5. Kích thước mẫu n = 4 + 10 + 6 = 20.",
              "Bước 2: Tính số trung bình: x̄ = (4·7.5 + 10·12.5 + 6·17.5) / 20 = (30 + 125 + 105) / 20 = 260 / 20 = 13 giờ.",
              "Bước 3: Tính phương sai: s² = [4·(7.5 - 13)² + 10·(12.5 - 13)² + 6·(17.5 - 13)²] / 20 = [4·30.25 + 10·0.25 + 6·20.25] / 20 = [121 + 2.5 + 121.5] / 20 = 245 / 20 = 12.25."
            ],
            "answer": "Số trung bình x̄ = 13 giờ; phương sai s² = 12.25; độ lệch chuẩn s = 3.5 giờ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy nhầm độ dài khoảng thay vì trung điểm làm giá trị đại diện c_i.",
            "why": "Giá trị đại diện là trung bình cộng hai mút (a + b)/2, không phải độ dài khoảng h = b - a."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Nguyên hàm và Tích phân",
        "description": "Nguyên hàm, bảng nguyên hàm cơ bản, phương pháp đổi biến số và từng phần, định nghĩa tích phân, ý nghĩa hình học tính diện tích hình phẳng và thể tích khối tròn xoay.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Nguyên hàm và bảng nguyên hàm cơ bản", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tích phân", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Ứng dụng hình học của tích phân", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Nguyên hàm của hàm số",
            "definition": "Hàm số F(x) được gọi là nguyên hàm của f(x) trên K nếu F'(x) = f(x) với mọi x thuộc K. Họ tất cả các nguyên hàm ký hiệu là ∫ f(x)dx = F(x) + C (C là hằng số).",
            "example": "∫ x² dx = x³/3 + C vì (x³/3 + C)' = 3x²/3 = x²; ∫ e^x dx = e^x + C.",
            "essence": "Nguyên hàm là phép toán ngược lại với phép lấy đạo hàm, khôi phục lại đại lượng gốc từ tốc độ biến thiên."
          },
          {
            "term": "Công thức Newton - Leibniz",
            "definition": "Tích phân từ a đến b của f(x) bằng hiệu số nguyên hàm tại hai mút: ∫_a^b f(x)dx = F(b) - F(a) = F(x)|_a^b.",
            "example": "∫_0^2 2x dx = x²|_0^2 = 2² - 0² = 4.",
            "essence": "Cầu nối vĩ đại giữa giải tích vi phân và tích phân, biến bài toán tính tổng vô hạn các diện tích vô cùng bé thành việc lấy hiệu của hàm nguyên hàm."
          }
        ],
        "rules": [
          {
            "statement": "Ứng dụng hình học tính thể tích khối tròn xoay",
            "meaning": "Thể tích khối tròn xoay tạo thành khi quay hình phẳng giới hạn bởi y = f(x), trục Ox và hai đường thẳng x = a, x = b quanh trục Ox là V = π · ∫_a^b [f(x)]² dx.",
            "example": "Quay hình phẳng giới hạn bởi y = √x, x = 0, x = 4 quanh Ox ta có V = π · ∫_0^4 (√x)² dx = π · ∫_0^4 x dx = π · (x²/2)|_0^4 = 8π.",
            "essence": "Khối tròn xoay được cắt thành các lát đĩa tròn vô cùng mỏng có diện tích π·r² = π·[f(x)]² và tích phân cộng dồn các đĩa này lại."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số parabol y = -x² + 4 và trục hoành Ox.",
            "steps": [
              "Bước 1: Tìm hoành độ giao điểm: Giải -x² + 4 = 0 ⇔ x² = 4 ⇔ x = -2 hoặc x = 2.",
              "Bước 2: Thiết lập tích phân diện tích: S = ∫_{-2}^2 |-x² + 4| dx. Vì trên [-2; 2], -x² + 4 ≥ 0 nên S = ∫_{-2}^2 (4 - x²) dx.",
              "Bước 3: Tìm nguyên hàm: F(x) = 4x - x³/3.",
              "Bước 4: Thay cận: S = [4·2 - 8/3] - [4·(-2) - (-8)/3] = [8 - 8/3] - [-8 + 8/3] = 16/3 - (-16/3) = 32/3."
            ],
            "answer": "Diện tích hình phẳng S = 32/3 (đơn vị diện tích)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên nhân hằng số π khi tính thể tích khối tròn xoay: viết V = ∫ [f(x)]² dx thay vì π∫ [f(x)]² dx.",
            "why": "Lát cắt của khối tròn xoay là hình tròn có diện tích π·r², bắt buộc phải có hệ số π."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Phương pháp toạ độ trong không gian",
        "description": "Phương trình mặt phẳng, vectơ pháp tuyến, phương trình đường thẳng, vectơ chỉ phương, phương trình mặt cầu, khoảng cách và góc trong không gian.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phương trình mặt phẳng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phương trình đường thẳng trong không gian", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Phương trình mặt cầu", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Vectơ pháp tuyến và phương trình tổng quát của mặt phẳng",
            "definition": "Vectơ n ≠ 0 vuông góc với mặt phẳng (P) gọi là vectơ pháp tuyến của (P). Mặt phẳng đi qua M₀(x₀; y₀; z₀) nhận n = (A; B; C) làm VTPT có phương trình A(x - x₀) + B(y - y₀) + C(z - z₀) = 0 hay Ax + By + Cz + D = 0 với A² + B² + C² > 0.",
            "example": "Mặt phẳng đi qua M(1; 2; -1) nhận n = (2; -3; 1) làm VTPT có pt: 2(x - 1) - 3(y - 2) + 1(z + 1) = 0 ⇔ 2x - 3y + z + 5 = 0.",
            "essence": "Một mặt phẳng hoàn toàn được định vị trong không gian khi biết một điểm nó đi qua và một phương trực giao (pháp tuyến) với nó."
          },
          {
            "term": "Phương trình mặt cầu trong không gian",
            "definition": "Mặt cầu (S) có tâm I(a; b; c) và bán kính R có phương trình chính tắc: (x - a)² + (y - b)² + (z - c)² = R². Dạng tổng quát: x² + y² + z² - 2ax - 2by - 2cz + d = 0 với điều kiện a² + b² + c² - d > 0 và R = √(a² + b² + c² - d).",
            "example": "Mặt cầu (x - 1)² + (y + 2)² + z² = 16 có tâm I(1; -2; 0) và bán kính R = 4.",
            "essence": "Mặt cầu là quỹ tích các điểm trong không gian cách đều tâm I một khoảng cách cố định bằng bán kính R."
          }
        ],
        "rules": [
          {
            "statement": "Công thức khoảng cách từ điểm đến mặt phẳng",
            "meaning": "Khoảng cách từ điểm M(x₀; y₀; z₀) đến mặt phẳng (P): Ax + By + Cz + D = 0 là d(M, (P)) = |Ax₀ + By₀ + Cz₀ + D| / √(A² + B² + C²).",
            "example": "Khoảng cách từ gốc O(0; 0; 0) đến (P): 2x - 2y + z - 9 = 0 là d = |-9| / √(2² + (-2)² + 1²) = 9 / √9 = 9/3 = 3.",
            "essence": "Độ dài hình chiếu vuông góc của đoạn OM lên phương vectơ pháp tuyến của mặt phẳng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Viết phương trình mặt phẳng (P) đi qua điểm A(1; 2; 3) và song song với mặt phẳng (Q): 2x - y + 2z - 5 = 0.",
            "steps": [
              "Bước 1: Vì (P) // (Q) nên (P) nhận cùng vectơ pháp tuyến của (Q) là n = (2; -1; 2).",
              "Bước 2: Phương trình (P) có dạng: 2(x - 1) - 1(y - 2) + 2(z - 3) = 0.",
              "Bước 3: Rút gọn: 2x - 2 - y + 2 + 2z - 6 = 0 ⇔ 2x - y + 2z - 6 = 0.",
              "Bước 4: Kiểm tra điều kiện không trùng: -6 ≠ -5 nên (P) song song hoàn toàn với (Q)."
            ],
            "answer": "Phương trình mặt phẳng (P): 2x - y + 2z - 6 = 0."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn dấu tọa độ tâm khi đọc từ phương trình chính tắc: ví dụ (x + 3)² đọc nhầm tâm là a = 3 thay vì a = -3.",
            "why": "Công thức có dạng (x - a)², nên số hạng (x + 3) tương ứng a = -3."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Xác suất có điều kiện",
        "description": "Xác suất có điều kiện, quy tắc nhân xác suất, công thức xác suất toàn phần và công thức Bayes; ứng dụng trong chẩn đoán y khoa và đánh giá rủi ro thực tiễn.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Xác suất có điều kiện", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Công thức xác suất toàn phần và công thức Bayes", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Xác suất có điều kiện",
            "definition": "Xác suất của biến cố A khi biết biến cố B đã xảy ra (với P(B) > 0) ký hiệu là P(A|B), tính bởi công thức: P(A|B) = P(A ∩ B) / P(B).",
            "example": "Gieo con xúc xắc 6 mặt. Biết rằng số chấm xuất hiện là số chẵn (B = {2, 4, 6}). Xác suất số chấm lớn hơn 3 (A = {4, 5, 6}) là P(A|B) = 2/3 (các kết quả {4, 6}).",
            "essence": "Thông tin phụ B làm thu hẹp không gian mẫu ban đầu Ω xuống còn không gian con B."
          },
          {
            "term": "Công thức Bayes",
            "definition": "Cho hệ đầy đủ các biến cố B₁, B₂,..., B_n và biến cố A. Khi biến cố A đã xảy ra, xác suất có điều kiện của B_k là P(B_k|A) = [P(B_k) · P(A|B_k)] / ∑ [P(B_i) · P(A|B_i)].",
            "example": "Cập nhật xác suất một người thực sự mắc bệnh sau khi nhận kết quả xét nghiệm dương tính dựa trên tỷ lệ mắc bệnh nền trong cộng đồng.",
            "essence": "Công thức Bayes cập nhật niềm tin xác suất tiền nghiệm thành xác suất hậu nghiệm khi có thêm bằng chứng thực tế quan sát được."
          }
        ],
        "rules": [
          {
            "statement": "Công thức xác suất toàn phần",
            "meaning": "Nếu {B₁, B₂,..., B_n} là một nhóm biến cố xung khắc từng đôi và hợp thành biến cố chắc chắn (hệ đầy đủ), thì với mọi biến cố A: P(A) = ∑ P(B_i) · P(A|B_i).",
            "example": "Tỷ lệ sản phẩm hỏng của toàn nhà máy bằng tổng xác suất sản phẩm do từng phân xưởng sản xuất nhân với tỷ lệ phế phẩm tương ứng của phân xưởng đó.",
            "essence": "Phân rã một biến cố phức tạp thành tổng các kịch bản bộ phận độc lập để tính toán đơn giản hóa."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Có hai hộp bi: Hộp 1 có 3 bi trắng và 2 bi đen; Hộp 2 có 4 bi trắng và 1 bi đen. Chọn ngẫu nhiên một hộp rồi rút ngẫu nhiên 1 viên bi. Tính xác suất để viên bi rút ra là màu trắng?",
            "steps": [
              "Bước 1: Gọi B₁ là biến cố chọn Hộp 1, B₂ là biến cố chọn Hộp 2. Ta có P(B₁) = P(B₂) = 0.5. Hệ {B₁, B₂} là hệ đầy đủ.",
              "Bước 2: Gọi A là biến cố rút được bi trắng. Xác suất có điều kiện: P(A|B₁) = 3/5 = 0.6; P(A|B₂) = 4/5 = 0.8.",
              "Bước 3: Áp dụng công thức xác suất toàn phần: P(A) = P(B₁)·P(A|B₁) + P(B₂)·P(A|B₂) = 0.5·0.6 + 0.5·0.8 = 0.3 + 0.4 = 0.7."
            ],
            "answer": "Xác suất rút được bi màu trắng là P(A) = 0.7 (70%)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa P(A|B) (xác suất của A khi biết B) và P(B|A) (xác suất của B khi biết A).",
            "why": "Hai xác suất này hoàn toàn khác nhau về bản chất và chỉ bằng nhau khi P(A) = P(B)."
          }
        ]
      }
    ]
  },
  "vat-li": {
    "id": "vat-li",
    "name": "Vật lí",
    "icon": "⚡",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Vật lí nhiệt",
        "description": "Cấu trúc của chất và sự chuyển thể, nội năng và Định luật I của nhiệt động lực học, thang nhiệt độ và nhiệt kế, nhiệt dung riêng, nhiệt nóng chảy riêng và nhiệt hoá hơi riêng.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cấu trúc của chất. Sự chuyển thể", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Nội năng. Định luật I của nhiệt động lực học", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Nhiệt độ. Thang nhiệt độ – nhiệt kế", "hasRealContent": true },
          { "id": "l04", "title": "Bài 4: Nhiệt dung riêng", "hasRealContent": true },
          { "id": "l05", "title": "Bài 5: Nhiệt nóng chảy riêng", "hasRealContent": true },
          { "id": "l06", "title": "Bài 6: Nhiệt hoá hơi riêng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Nội năng và sự biến thiên nội năng",
            "definition": "Nội năng của một vật là tổng động năng của chuyển động nhiệt hỗn loạn của các phân tử và thế năng tương tác giữa các phân tử cấu tạo nên vật: U = E_đ + E_t.",
            "example": "Khi cọ xát hai bàn tay vào nhau, cơ năng chuyển hóa thành nội năng làm bàn tay nóng lên.",
            "essence": "Nội năng phụ thuộc vào nhiệt độ (quyết định động năng phân tử) và thể tích (quyết định khoảng cách và thế năng tương tác)."
          },
          {
            "term": "Nhiệt dung riêng",
            "definition": "Là nhiệt lượng cần truyền cho 1 kg chất đó để nhiệt độ của nó tăng thêm 1 K (hoặc 1 °C), ký hiệu là c, đơn vị là J/(kg·K). Công thức nhiệt lượng: Q = m·c·ΔT.",
            "example": "Nhiệt dung riêng của nước c_nước ≈ 4180 J/(kg·K), rất lớn so với kim loại (c_đồng ≈ 380 J/(kg·K)), nên nước là chất làm mát và điều hòa khí hậu lý tưởng.",
            "essence": "Đặc trưng cho quán tính nhiệt của chất: chất có nhiệt dung riêng càng lớn thì càng khó nóng lên nhưng cũng giữ nhiệt được lâu hơn."
          }
        ],
        "rules": [
          {
            "statement": "Định luật I của nhiệt động lực học",
            "meaning": "Độ biến thiên nội năng của một hệ bằng tổng công và nhiệt lượng mà hệ nhận được: ΔU = A + Q. Quy ước dấu: Q > 0 khi hệ nhận nhiệt lượng, Q < 0 khi hệ truyền nhiệt lượng; A > 0 khi hệ nhận công, A < 0 khi hệ thực hiện công.",
            "example": "Chất khí trong xilanh nhận nhiệt lượng 100 J và giãn nở thực hiện công 40 J đẩy pittông thì ΔU = 100 - 40 = 60 J (nội năng tăng 60 J).",
            "essence": "Định luật I chính là định luật bảo toàn và chuyển hóa năng lượng áp dụng cho các quá trình nhiệt và cơ học."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một khối nước đá có khối lượng 2 kg ở 0 °C. Biết nhiệt nóng chảy riêng của nước đá là λ = 3.34 · 10⁵ J/kg. Tính nhiệt lượng cần cung cấp để làm nóng chảy hoàn toàn khối nước đá này ở 0 °C?",
            "steps": [
              "Bước 1: Xác định công thức nhiệt lượng nóng chảy: Q = λ · m.",
              "Bước 2: Thay số: m = 2 kg; λ = 3.34 · 10⁵ J/kg.",
              "Bước 3: Tính toán: Q = 3.34 · 10⁵ · 2 = 6.68 · 10⁵ J = 668 kJ."
            ],
            "answer": "Nhiệt lượng cần cung cấp để làm tan chảy hoàn toàn khối nước đá là Q = 668 kJ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng khi chất rắn kết tinh đang nóng chảy, nhiệt độ của nó tiếp tục tăng lên do nhận thêm nhiệt.",
            "why": "Trong suốt quá trình chuyển thể từ rắn sang lỏng, nhiệt độ giữ không đổi; toàn bộ nhiệt lượng nhận vào dùng để phá vỡ mạng tinh thể (tăng thế năng tương tác phân tử)."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Khí lí tưởng",
        "description": "Mô hình động học phân tử chất khí, định luật Boyle (đẳng nhiệt), định luật Charles (đẳng áp), phương trình trạng thái khí lí tưởng pV = nRT và áp suất chất khí theo động năng phân tử.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Mô hình động học phân tử chất khí", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Định luật Boyle", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Định luật Charles", "hasRealContent": true },
          { "id": "l04", "title": "Bài 4: Phương trình trạng thái của khí lí tưởng", "hasRealContent": true },
          { "id": "l05", "title": "Bài 5: Áp suất khí theo mô hình động học phân tử", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chất khí lí tưởng",
            "definition": "Là chất khí giả định trong đó các phân tử khí được coi là những chất điểm không có kích thước và chỉ tương tác với nhau khi va chạm đàn hồi hoàn toàn.",
            "example": "Không khí ở điều kiện nhiệt độ phòng và áp suất khí quyển thông thường tuân theo gần đúng mô hình khí lí tưởng.",
            "essence": "Mô hình hóa lý tưởng đơn giản hóa các phép toán nhiệt động lực học trong khi vẫn giữ nguyên bản chất vật lý vĩ mô."
          },
          {
            "term": "Nhiệt độ tuyệt đối (Thang Kelvin)",
            "definition": "Nhiệt độ đo trong thang Kelvin có gốc T = 0 K (độ không tuyệt đối, tại đó chuyển động nhiệt của các phân tử hoàn toàn dừng lại). Liên hệ: T(K) = t(°C) + 273.15.",
            "example": "Nhiệt độ phòng 27 °C tương ứng với T = 27 + 273 = 300 K.",
            "essence": "Nhiệt độ tuyệt đối tỉ lệ thuận với động năng tịnh tiến trung bình của các phân tử khí: E_đ = (3/2)·k·T."
          }
        ],
        "rules": [
          {
            "statement": "Phương trình trạng thái của khí lí tưởng (Clapeyron - Mendeleev)",
            "meaning": "Đối với một lượng khí xác định: (p · V) / T = hằng số, hay p·V = n·R·T = (m/M)·R·T, trong đó R ≈ 8.31 J/(mol·K) là hằng số khí lí tưởng.",
            "example": "Khi nén đẳng nhiệt (T = hằng số), nếu thể tích giảm một nửa thì áp suất khí tăng gấp đôi (Định luật Boyle p₁V₁ = p₂V₂).",
            "essence": "Thống nhất ba thông số trạng thái vĩ mô: Áp suất p, Thể tích V và Nhiệt độ tuyệt đối T của một lượng khí."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một khối khí lí tưởng có thể tích 10 lít ở áp suất 1 atm và nhiệt độ 27 °C. Nén khối khí đến thể tích 5 lít ở nhiệt độ 127 °C. Tính áp suất của khối khí sau khi nén?",
            "steps": [
              "Bước 1: Trạng thái 1: p₁ = 1 atm; V₁ = 10 l; T₁ = 27 + 273 = 300 K.",
              "Bước 2: Trạng thái 2: V₂ = 5 l; T₂ = 127 + 273 = 400 K; p₂ = ?.",
              "Bước 3: Áp dụng phương trình trạng thái: (p₁·V₁)/T₁ = (p₂·V₂)/T₂ ⇒ p₂ = (p₁·V₁·T₂) / (V₂·T₁).",
              "Bước 4: Thay số: p₂ = (1 · 10 · 400) / (5 · 300) = 4000 / 1500 = 8/3 ≈ 2.67 atm."
            ],
            "answer": "Áp suất của khối khí sau khi nén là p₂ = 8/3 atm ≈ 2.67 atm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Sử dụng trực tiếp nhiệt độ độ Celsius t (°C) vào phương trình trạng thái thay vì nhiệt độ tuyệt đối T (K).",
            "why": "Các định luật khí lí tưởng chỉ có quan hệ tỉ lệ thuận tuyến tính khi tính theo thang đo nhiệt độ tuyệt đối Kelvin."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Từ trường",
        "description": "Từ trường và đường sức từ, cảm ứng từ B, lực từ tác dụng lên dây dẫn mang dòng điện (Định luật Laplace), từ thông và hiện tượng cảm ứng điện từ (Faraday, Lenz), máy phát điện xoay chiều và sóng điện từ.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Từ trường và cảm ứng từ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Lực từ tác dụng lên dây dẫn mang dòng điện", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Từ thông và Hiện tượng cảm ứng điện từ", "hasRealContent": true },
          { "id": "l04", "title": "Bài 4: Máy phát điện xoay chiều", "hasRealContent": true },
          { "id": "l05", "title": "Bài 5: Điện từ trường và Sóng điện từ", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Cảm ứng từ và Lực từ",
            "definition": "Cảm ứng từ B là đại lượng vectơ đặc trưng cho từ trường về mặt tác dụng lực. Lực từ tác dụng lên đoạn dây dẫn có chiều dài L mang dòng điện I đặt trong từ trường đều B: F = I · L · B · sin α (α = (L, B)). Hướng lực xác định theo quy tắc bàn tay trái.",
            "example": "Đoạn dây 0.2 m mang dòng điện 5 A đặt vuông góc với từ trường B = 0.1 T chịu lực từ F = 5 · 0.2 · 0.1 · sin 90° = 0.1 N.",
            "essence": "Từ trường tác dụng lực lên các hạt mang điện chuyển động và dây dẫn mang dòng điện, tạo nền tảng cho động cơ điện."
          },
          {
            "term": "Từ thông và Hiện tượng cảm ứng điện từ",
            "definition": "Từ thông qua diện tích S là Φ = B · S · cos θ (θ là góc giữa vectơ B và vectơ pháp tuyến n). Khi từ thông biến thiên theo thời gian thì trong mạch kín xuất hiện dòng điện cảm ứng.",
            "example": "Khi đưa nam châm lại gần cuộn dây, từ trường qua cuộn dây tăng làm xuất hiện dòng điện cảm ứng trong cuộn dây làm lệch kim điện kế.",
            "essence": "Biến đổi năng lượng từ cơ năng sang điện năng thông qua sự biến thiên của từ thông qua mạch dẫn."
          }
        ],
        "rules": [
          {
            "statement": "Định luật cảm ứng điện từ Faraday và Định luật Lenz",
            "meaning": "Suất điện động cảm ứng có độ lớn tỉ lệ thuận với tốc độ biến thiên của từ thông qua mạch: e_c = -dΦ/dt. Định luật Lenz: Dòng điện cảm ứng xuất hiện có chiều sao cho từ trường do nó sinh ra có tác dụng chống lại sự biến thiên của từ thông sinh ra nó.",
            "example": "Khi nam châm tiến vào cuộn dây (từ thông tăng), cuộn dây sinh ra từ trường ngược chiều để đẩy nam châm ra xa.",
            "essence": "Tính bảo toàn năng lượng trong hiện tượng điện từ: chống lại sự biến đổi gây ra nó."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một khung dây phẳng có diện tích S = 100 cm² gồm 200 vòng dây đặt vuông góc với các đường sức từ của từ trường đều B = 0.05 T. Trong khoảng thời gian 0.02 giây, từ trường giảm đều về 0. Tính suất điện động cảm ứng xuất hiện trong khung?",
            "steps": [
              "Bước 1: Diện tích S = 100 cm² = 0.01 m². Vì khung vuông góc đường sức từ nên góc θ = 0°, cos θ = 1.",
              "Bước 2: Từ thông ban đầu qua 200 vòng dây: Φ₁ = N·B₁·S = 200 · 0.05 · 0.01 = 0.1 Wb.",
              "Bước 3: Từ thông lúc sau: Φ₂ = 0. Độ biến thiên: ΔΦ = 0 - 0.1 = -0.1 Wb.",
              "Bước 4: Suất điện động cảm ứng: |e_c| = |ΔΦ / Δt| = |-0.1 / 0.02| = 5 V."
            ],
            "answer": "Suất điện động cảm ứng sinh ra trong khung dây có độ lớn bằng 5 V."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm góc θ giữa vectơ B và vectơ pháp tuyến n với góc giữa vectơ B và mặt phẳng khung dây.",
            "why": "Nếu đề cho góc giữa B và mặt phẳng khung là α thì góc θ trong công thức từ thông phải là θ = 90° - α."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Vật lí hạt nhân",
        "description": "Cấu trúc hạt nhân nguyên tử, độ hụt khối và năng lượng liên kết, các loại phản ứng hạt nhân, hiện tượng phóng xạ (alpha, beta, gamma), chu kỳ bán rã và ứng dụng công nghiệp hạt nhân an toàn.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cấu trúc hạt nhân", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phản ứng hạt nhân và Năng lượng liên kết", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Hiện tượng phóng xạ", "hasRealContent": true },
          { "id": "l04", "title": "Bài 4: Công nghiệp hạt nhân và An toàn bức xạ", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Độ hụt khối và Năng lượng liên kết hạt nhân",
            "definition": "Độ hụt khối Δm = [Z·m_p + (A - Z)·m_n] - m_hn > 0. Năng lượng liên kết: E_lk = Δm · c². Năng lượng liên kết riêng E_lkr = E_lk / A đặc trưng cho độ bền vững của hạt nhân (hạt nhân có số khối 50 < A < 80 bền vững nhất).",
            "example": "Hạt nhân Sắt ⁵⁶Fe có năng lượng liên kết riêng lớn nhất xấp xỉ 8.8 MeV/nucleon nên là một trong những hạt nhân bền vững nhất trong tự nhiên.",
            "essence": "Khối lượng của hạt nhân luôn nhỏ hơn tổng khối lượng của các nucleon tự do tạo nên nó; phần khối lượng hụt đi chuyển hóa thành năng lượng liên kết gắn kết các nucleon."
          },
          {
            "term": "Định luật phóng xạ và Chu kỳ bán rã",
            "definition": "Phóng xạ là quá trình tự phân rã tự phát của hạt nhân không bền vững phát ra các tia phóng xạ. Số hạt nhân còn lại sau thời gian t tuân theo định luật: N(t) = N₀ · 2^(-t/T) = N₀ · e^(-λt) với T là chu kỳ bán rã.",
            "example": "Đồng vị phóng xạ Iod-131 có chu kỳ bán rã T = 8 ngày. Sau 24 ngày (3 chu kỳ), lượng phóng xạ còn lại là (1/2)³ = 1/8 so với ban đầu.",
            "essence": "Quá trình phóng xạ mang tính xác suất thống kê lượng tử ngẫu nhiên, không phụ thuộc vào các điều kiện hóa học hay nhiệt độ, áp suất bên ngoài."
          }
        ],
        "rules": [
          {
            "statement": "Các định luật bảo toàn trong phản ứng hạt nhân",
            "meaning": "Trong mọi phản ứng hạt nhân luôn tuân thủ 4 định luật bảo toàn: Bảo toàn điện tích (Z), Bảo toàn số khối (A hay số nucleon), Bảo toàn động lượng và Bảo toàn năng lượng toàn phần (không có định luật bảo toàn khối lượng nghỉ).",
            "example": "Trong phản ứng: ¹⁰₅B + n → ⁷₃Li + ⁴₂He, tổng số khối hai vế: 10 + 1 = 7 + 4 = 11; tổng điện tích: 5 + 0 = 3 + 2 = 5.",
            "essence": "Số lượng các proton và neutron không bị mất đi mà chỉ được tái sắp xếp lại tạo ra cấu trúc hạt nhân mới."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Đồng vị Cacbon ¹⁴C có chu kỳ bán rã T = 5730 năm. Phân tích một mẫu gỗ cổ thấy lượng ¹⁴C còn lại bằng 25% lượng ¹⁴C có trong mẫu gỗ tươi cùng loại. Xác định tuổi của mẫu gỗ cổ?",
            "steps": [
              "Bước 1: Áp dụng định luật phóng xạ: N(t) / N₀ = 2^(-t/T).",
              "Bước 2: Theo đề bài, tỉ lệ còn lại là 25% = 1/4 = 2^(-2).",
              "Bước 3: Suy ra: 2^(-t/T) = 2^(-2) ⇔ t/T = 2 ⇔ t = 2 · T.",
              "Bước 4: Thay T = 5730 năm: t = 2 · 5730 = 11460 năm."
            ],
            "answer": "Tuổi của mẫu gỗ cổ là 11.460 năm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng khối lượng được bảo toàn trong phản ứng hạt nhân: tổng khối lượng trước phản ứng bằng tổng khối lượng sau phản ứng.",
            "why": "Khối lượng nghỉ KHÔNG bảo toàn; độ chênh lệch khối lượng nghỉ ΔM = M_trước - M_sau chuyển hóa thành năng lượng tỏa ra hoặc thu vào theo hệ thức E = ΔM·c²."
          }
        ]
      }
    ]
  },
  "hoa-hoc": {
    "id": "hoa-hoc",
    "name": "Hóa học",
    "icon": "🧪",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Ester – Lipid. Xà phòng và chất giặt rửa",
        "description": "Cấu tạo và tính chất este, lipid, chất béo triglixerit, phản ứng thủy phân trong môi trường axit và môi trường kiềm (xà phòng hóa), cơ chế tẩy rửa của xà phòng.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Ester và Lipid", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Xà phòng và chất giặt rửa tổng hợp", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Ester và Phản ứng ester hóa",
            "definition": "Khi thay thế nhóm -OH ở nhóm carboxyl (-COOH) của acid carboxylic bằng nhóm -OR' thì thu được ester: RCOOH + R'OH ⇌ RCOOR' + H₂O (xúc tác H₂SO₄ đặc, đun nóng).",
            "example": "CH₃COOH + C₂H₅OH ⇌ CH₃COOC₂H₅ (ethyl acetate có mùi thơm hoa quả) + H₂O.",
            "essence": "Phản ứng ester hóa là phản ứng thuận nghịch; ester có nhiệt độ sôi thấp hơn axit và ancol tương ứng do không tạo được liên kết hydro liên phân tử."
          },
          {
            "term": "Chất béo (Triglyceride)",
            "definition": "Là triester của glycerol với các acid béo (acid béo mạch dài, không phân nhánh, số C chẵn như stearic C₁₇H₃₅COOH, oleic C₁₇H₃₃COOH, palmitic C₁₅H₃₁COOH).",
            "example": "Chất béo lỏng (dầu thực vật) chứa nhiều gốc axit béo không no (chứa nối đôi C=C), chất béo rắn (mỡ động vật) chứa chủ yếu gốc axit béo no.",
            "essence": "Chất béo nhẹ hơn nước, không tan trong nước nhưng tan nhiều trong dung môi hữu cơ không phân cực."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc phản ứng xà phòng hóa chất béo",
            "meaning": "Chất béo khi đun nóng với dung dịch kiềm (NaOH hoặc KOH) bị thủy phân hoàn toàn một chiều tạo ra glycerol và muối của các acid béo (thành phần chính của xà phòng).",
            "example": "(C₁₇H₃₅COO)₃C₃H₅ + 3NaOH → 3C₁₇H₃₅COONa (xà phòng) + C₃H₅(OH)₃ (glycerol).",
            "essence": "Muối natri/kali của axit béo có đầu phân cực ưa nước và đuôi hidrocacbon kị nước giúp bao vây và nhũ tương hóa vết dầu mỡ."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xà phòng hóa hoàn toàn 8.9 gam tristearin (C₁₇H₃₅COO)₃C₃H₅ bằng dung dịch NaOH vừa đủ. Tính khối lượng glycerol thu được sau phản ứng?",
            "steps": [
              "Bước 1: Tính khối lượng mol tristearin: M = 3·(283) + 41 = 890 g/mol.",
              "Bước 2: Tính số mol tristearin: n = 8.9 / 890 = 0.01 mol.",
              "Bước 3: Phương trình phản ứng: (C₁₇H₃₅COO)₃C₃H₅ + 3NaOH → 3C₁₇H₃₅COONa + C₃H₅(OH)₃. Theo pt: n_glycerol = n_tristearin = 0.01 mol.",
              "Bước 4: Khối lượng glycerol: m = 0.01 · 92 = 0.92 gam."
            ],
            "answer": "Khối lượng glycerol thu được là 0.92 gam."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn phản ứng thủy phân este trong môi trường axit (thuận nghịch) với môi trường kiềm (một chiều hoàn toàn).",
            "why": "Trong môi trường kiềm, axit sinh ra phản ứng ngay với kiềm tạo muối nên không thể đảo ngược phản ứng."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Carbohydrate",
        "description": "Phân loại carbohydrate: monosaccharide (glucose, fructose), disaccharide (saccharose, maltose), polysaccharide (tinh bột, cellulose); cấu trúc hóa học và các phản ứng đặc trưng.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Glucose và Fructose", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Saccharose và Maltose", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Tinh bột và Cellulose", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Glucose và Fructose",
            "definition": "Đều có CTPT C₆H₁₂O₆ (đồng phân của nhau). Glucose là polyhydroxyaldehyde chứa 5 nhóm -OH kề nhau và 1 nhóm -CHO. Fructose là polyhydroxyketone chứa 5 nhóm -OH và 1 nhóm C=O.",
            "example": "Glucose có nhiều trong nho chín, mật ong và trong máu người nồng độ ổn định khoảng 0.1% (4.4 - 7.2 mmol/L).",
            "essence": "Glucose tác dụng với Cu(OH)₂ ở nhiệt độ thường cho dung dịch xanh lam và phản ứng tráng bạc khi đun nóng với thuốc thử Tollens."
          },
          {
            "term": "Tinh bột và Cellulose",
            "definition": "Đều có công thức tổng quát (C₆H₁₀O₅)_n nhưng không phải đồng phân của nhau (do hệ số polime hóa n khác nhau). Tinh bột gồm amylose và amylopectin liên kết α-glucoside; Cellulose gồm các mắt xích β-glucose liên kết β-1,4-glucoside kéo dài thành sợi.",
            "example": "Tinh bột cho màu xanh tím đặc trưng với dung dịch iot. Cellulose tan trong nước Svayze [Cu(NH₃)₄](OH)₂ để sản xuất tơ đồng - amoniac.",
            "essence": "Cấu trúc không gian khác biệt: Tinh bột cuộn xoắn giữ hạt iot, trong khi cellulose dạng sợi duỗi thẳng không phân nhánh tạo nên thành tế bào thực vật bền chắc."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc phản ứng thủy phân carbohydrate",
            "meaning": "Disaccharide và Polysaccharide khi đun nóng trong môi trường acid vô cơ loãng hoặc có xúc tác enzyme sẽ bị thủy phân thành các monosaccharide cấu thành.",
            "example": "Thủy phân tinh bột hoặc cellulose: (C₆H₁₀O₅)_n + nH₂O → nC₆H₁₂O₆ (glucose). Thủy phân saccharose thu được 1 glucose + 1 fructose.",
            "essence": "Sự cắt đứt liên kết glucoside nhờ phân tử nước tái tạo các nhóm hidroxyl ban đầu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho 18 gam glucose C₆H₁₂O₆ phản ứng hoàn toàn với lượng dư dung dịch AgNO₃ trong NH₃. Tính khối lượng bạc kim loại kết tủa thu được?",
            "steps": [
              "Bước 1: Tính mol glucose: n = 18 / 180 = 0.1 mol.",
              "Bước 2: Phương trình tráng bạc: 1 mol glucose chứa 1 nhóm -CHO tạo ra 2 mol Ag: C₆H₁₂O₆ + 2[Ag(NH₃)₂]OH → 2Ag↓.",
              "Bước 3: Số mol Ag: n_Ag = 2 · n_glucose = 2 · 0.1 = 0.2 mol.",
              "Bước 4: Khối lượng Ag: m_Ag = 0.2 · 108 = 21.6 gam."
            ],
            "answer": "Khối lượng bạc thu được là 21.6 gam."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng tinh bột và xenlulozơ là đồng phân của nhau vì đều viết dạng (C₆H₁₀O₅)_n.",
            "why": "Hệ số polymer hóa n của cellulose lớn hơn rất nhiều so với tinh bột, nên khối lượng phân tử khác biệt hoàn toàn."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Hợp chất chứa Nitrogen",
        "description": "Amine (bậc amine, tính base, phản ứng với acid nitrous), Amino acid (tính lưỡng tính, điểm đẳng điện), Peptide và Protein (liên kết peptit, phản ứng màu biuret, đông tụ protein).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Amine", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Amino acid", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Peptide và Protein", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Amine và Bậc của amine",
            "definition": "Amine là dẫn xuất khi thay thế nguyên tử H trong NH₃ bằng gốc hydrocarbon. Bậc của amine là số gốc hydrocarbon liên kết trực tiếp với nguyên tử nitrogen (bậc 1: RNH₂, bậc 2: R-NH-R', bậc 3: R-N(R')-R'').",
            "example": "Methylamine CH₃NH₂ (bậc 1), Dimethylamine (CH₃)₂NH (bậc 2), Aniline C₆H₅NH₂ (amine thơm bậc 1).",
            "essence": "Đôi electron tự do trên nguyên tử N mang lại tính base cho amine; amine no có tính base mạnh hơn amoniac, amine thơm có tính base rất yếu."
          },
          {
            "term": "Amino acid và Tính chất lưỡng tính",
            "definition": "Amino acid là hợp chất hữu cơ tạp chức chứa đồng thời nhóm amino (-NH₂) và nhóm carboxyl (-COOH). Phân tử tồn tại chủ yếu ở dạng ion lưỡng cực H₃N⁺-R-COO⁻.",
            "example": "Glycine H₂N-CH₂-COOH phản ứng được với cả HCl (nhờ nhóm -NH₂) và dung dịch NaOH (nhờ nhóm -COOH).",
            "essence": "Tính lưỡng tính xuất phát từ sự hiện diện của cả nhóm mang tính base (-NH₂) và nhóm mang tính axit (-COOH) trong cùng phân tử."
          }
        ],
        "rules": [
          {
            "statement": "Đặc trưng phản ứng màu Biuret của peptide và protein",
            "meaning": "Những hợp chất chứa từ 2 liên kết peptide trở lên (tripeptide trở lên và protein) phản ứng với Cu(OH)₂ trong môi trường kiềm tạo phức chất màu tím đặc trưng.",
            "example": "Lòng trắng trứng (albumin) hoặc tripeptide Gly-Ala-Val cho phản ứng màu tím với Cu(OH)₂/NaOH; dipeptide Gly-Ala KHÔNG có phản ứng này.",
            "essence": "Phức chất phối trí tạo thành giữa ion Cu²⁺ với các nguyên tử N của các liên kết peptit lân cận."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho 7.5 gam glycine H₂N-CH₂-COOH tác dụng vừa đủ với dung dịch NaOH. Tính khối lượng muối thu được sau khi cô cạn?",
            "steps": [
              "Bước 1: Tính mol glycine: M = 75 g/mol ⇒ n = 7.5 / 75 = 0.1 mol.",
              "Bước 2: Phương trình phản ứng: H₂N-CH₂-COOH + NaOH → H₂N-CH₂-COONa + H₂O.",
              "Bước 3: Theo phương trình: n_muối = n_glycine = 0.1 mol.",
              "Bước 4: Khối lượng muối natri glycinat: M_muối = 75 - 1 + 23 = 97 g/mol ⇒ m = 0.1 · 97 = 9.7 gam."
            ],
            "answer": "Khối lượng muối thu được là 9.7 gam."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng tất cả các peptide đều cho phản ứng màu biuret.",
            "why": "Dipeptide chỉ có 1 liên kết peptit nên không tham gia phản ứng màu biuret; phản ứng đòi hỏi tối thiểu 2 liên kết peptit."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Polymer",
        "description": "Khái niệm và danh pháp polymer, phản ứng trùng hợp và trùng ngưng, các loại vật liệu polymer ứng dụng thực tế: chất dẻo, tơ tổng hợp, cao su và keo dán sinh học.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đại cương về polymer", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Vật liệu polymer", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Phản ứng trùng hợp và Trùng ngưng",
            "definition": "Trùng hợp là quá trình kết hợp nhiều phân tử nhỏ giống nhau hoặc tương tự nhau tạo thành phân tử lớn (yêu cầu monome có liên kết đôi C=C hoặc vòng kém bền). Trùng ngưng là quá trình kết hợp nhiều monome có ít nhất 2 nhóm chức phản ứng giải phóng phân tử nhỏ (thường là H₂O).",
            "example": "Trùng hợp ethylene CH₂=CH₂ tạo ra PE. Trùng ngưng axit terephthalic và ethylene glycol tạo tơ lapsan giải phóng H₂O.",
            "essence": "Hai cơ chế cơ bản để tổng hợp đại phân tử mạch dài từ các đơn phân nhỏ."
          },
          {
            "term": "Cao su và Quá trình lưu hóa cao su",
            "definition": "Cao su là vật liệu polymer có tính đàn hồi cao. Quá trình lưu hóa (đun nóng cao su thiên nhiên với lưu huỳnh) tạo ra các cầu nối disunfua -S-S- nối các mạch thẳng thành mạng không gian 3D bền nhiệt và đàn hồi hơn.",
            "example": "Cao su buna-S chế tạo lốp xe ô tô có độ chịu mài mòn vượt trội so với cao su chưa lưu hóa.",
            "essence": "Biến đổi cấu trúc từ mạch thẳng trượt lên nhau thành mạng lưới không gian có khả năng phục hồi hình dạng ban đầu sau khi biến dạng."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc nhận diện tơ bán tổng hợp (tơ nhân tạo)",
            "meaning": "Tơ bán tổng hợp có nguồn gốc từ polymer thiên nhiên (thường là cellulose) được chế biến bằng con đường hóa học.",
            "example": "Tơ visco và tơ cellulose acetate là tơ bán tổng hợp; tơ nilon-6,6 và tơ lapsan là tơ tổng hợp hoàn toàn; tơ tằm và bông là tơ thiên nhiên.",
            "essence": "Phân loại rõ ràng nguồn gốc để đánh giá tính chất cơ lý và phương pháp tái chế."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trùng hợp hoàn toàn 2.8 tấn ethylene CH₂=CH₂ thu được polyethylene (PE) với hiệu suất 90%. Tính khối lượng màng nhựa PE thu được?",
            "steps": [
              "Bước 1: Phương trình phản ứng: n CH₂=CH₂ → (-CH₂-CH₂-)_n.",
              "Bước 2: Theo bảo toàn khối lượng lý thuyết: m_PE (lý thuyết) = m_ethylene = 2.8 tấn.",
              "Bước 3: Vì hiệu suất đạt 90% nên khối lượng thực tế: m_thực tế = 2.8 · (90 / 100) = 2.52 tấn."
            ],
            "answer": "Khối lượng PE thu được là 2.52 tấn."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Xếp tơ nilon-6,6 vào nhóm tơ bán tổng hợp.",
            "why": "Nilon-6,6 được điều chế từ hexamethylenediamine và axit adipic (hóa chất hoàn toàn nhân tạo), nên nó là tơ tổng hợp."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Pin điện và Điện phân",
        "description": "Thế điện cực chuẩn E°(Mⁿ⁺/M), pin điện hóa Galvani, phản ứng oxi hóa - khử tự phát sinh dòng điện, quá trình điện phân dung dịch và điện phân nóng chảy, ứng dụng mạ điện và tinh luyện kim loại.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Thế điện cực chuẩn và Pin điện hóa", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Điện phân dung dịch và ứng dụng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Pin điện hóa Galvani (Zn - Cu)",
            "definition": "Thiết bị biến đổi hóa năng thành điện năng nhờ phản ứng oxi hóa - khử tự phát. Tại cực âm (anode) xảy ra quá trình oxi hóa kim loại hoạt động mạnh hơn (Zn → Zn²⁺ + 2e). Tại cực dương (cathode) xảy ra quá trình khử (Cu²⁺ + 2e → Cu).",
            "example": "Sức điện động chuẩn của pin Zn-Cu: E°_pin = E°(Cu²⁺/Cu) - E°(Zn²⁺/Zn) = 0.34 - (-0.76) = 1.10 V.",
            "essence": "Dòng electron chạy từ cực âm sang cực dương ở mạch ngoài tạo ra dòng điện liên tục."
          },
          {
            "term": "Hiện tượng điện phân",
            "definition": "Là quá trình oxi hóa - khử xảy ra trên bề mặt các điện cực dưới tác dụng của dòng điện một chiều đi qua chất điện li nóng chảy hoặc dung dịch chất điện li.",
            "example": "Điện phân dung dịch NaCl có màng ngăn sinh ra NaOH, khí Cl₂ ở anode và khí H₂ ở cathode.",
            "essence": "Cưỡng bức các phản ứng oxi hóa - khử không tự phát xảy ra bằng cách cung cấp năng lượng điện trường."
          }
        ],
        "rules": [
          {
            "statement": "Thứ tự phóng điện tại các điện cực khi điện phân dung dịch",
            "meaning": "Tại cathode (cực âm): Cation có tính oxi hóa mạnh hơn phóng điện trước (kim loại từ Al trở về trước không bị khử trong nước mà H₂O phóng điện sinh H₂). Tại anode (cực dương): Anion có tính khử mạnh hơn phóng điện trước (anion chứa oxi như SO₄²⁻, NO₃⁻ không bị oxi hóa mà H₂O phóng điện sinh O₂).",
            "example": "Điện phân dung dịch CuSO₄ với điện cực trơ: Cu²⁺ bị khử tại cathode tạo Cu; H₂O bị oxi hóa tại anode tạo O₂ và ion H⁺ (dung dịch mang tính axit).",
            "essence": "Mức năng lượng điện cực quyết định thứ tự ưu tiên nhận hoặc nhường electron."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Điện phân hoàn toàn 200 ml dung dịch Cu(NO₃)₂ 0.5M với điện cực trơ. Tính thể tích khí O₂ (đktc) thoát ra ở anode?",
            "steps": [
              "Bước 1: Số mol Cu(NO₃)₂: n = 0.2 · 0.5 = 0.1 mol ⇒ n_Cu²⁺ = 0.1 mol.",
              "Bước 2: Phản ứng tại cathode: Cu²⁺ + 2e → Cu (số mol e trao đổi: n_e = 0.1 · 2 = 0.2 mol).",
              "Bước 3: Phản ứng tại anode: 2H₂O → 4H⁺ + O₂ + 4e. Theo bảo toàn e: n_O₂ = n_e / 4 = 0.2 / 4 = 0.05 mol.",
              "Bước 4: Thể tích khí O₂ ở đktc: V = 0.05 · 22.4 = 1.12 lít (hoặc 0.05 · 24.79 = 1.2395 lít theo chuẩn 25 °C, 1 bar)."
            ],
            "answer": "Thể tích O₂ thoát ra là 1.12 lít (đktc) tương ứng 1.24 lít (đkc)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm tên cực: Trong pin điện hóa cực âm là Anode, nhưng trong bình điện phân cực âm là Cathode.",
            "why": "Quy ước chuẩn thế giới: Anode luôn là nơi xảy ra quá trình oxi hóa (nhường e), Cathode luôn là nơi xảy ra quá trình khử (nhận e)."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Đại cương về kim loại",
        "description": "Cấu tạo nguyên tử và tinh thể kim loại, liên kết kim loại, tính chất vật lí và hóa học chung, dãy điện hóa kim loại, hiện tượng ăn mòn kim loại và các phương pháp bảo vệ kim loại.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cấu tạo và tính chất của kim loại", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Dãy điện hóa của kim loại", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Ăn mòn kim loại và bảo vệ kim loại", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tính chất vật lý chung của kim loại",
            "definition": "Gồm 4 tính chất: Tính dẻo, tính dẫn điện, tính dẫn nhiệt và ánh kim. Tất cả đều do các electron tự do chuyển động hỗn loạn trong mạng tinh thể kim loại gây ra.",
            "example": "Bạc (Ag) dẫn điện và dẫn nhiệt tốt nhất; Vàng (Au) có tính dẻo nhất (có thể dát mỏng đến 0.0001 mm); Wolfram (W) có nhiệt độ nóng chảy cao nhất.",
            "essence": "Mô hình mạng tinh thể kim loại gồm các ion dương dao động quanh nút mạng và đám mây electron tự do di chuyển tự do khắp khối kim loại."
          },
          {
            "term": "Ăn mòn điện hóa học",
            "definition": "Là sự phá hủy kim loại hoặc hợp kim do tác dụng của dung dịch chất điện li và phát sinh dòng điện (yêu cầu 3 điều kiện: hai điện cực khác chất, tiếp xúc nhau và cùng tiếp xúc với dung dịch chất điện li).",
            "example": "Vỏ tàu biển bằng thép gắn những khối kẽm (Zn) để bảo vệ: Zn đóng vai trò anode bị ăn mòn hy sinh bảo vệ vỏ thép không bị gỉ.",
            "essence": "Kim loại có tính khử mạnh hơn trở thành cực âm (anode) và bị oxi hóa hòa tan, bảo vệ kim loại yếu hơn ở cực dương."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc Alpha (α) trong phản ứng oxi hóa - khử của dãy điện hóa",
            "meaning": "Chất oxi hóa mạnh hơn phản ứng với chất khử mạnh hơn tạo ra chất oxi hóa yếu hơn và chất khử yếu hơn: Fe + Cu²⁺ → Fe²⁺ + Cu.",
            "example": "Cho đinh sắt vào dung dịch CuSO₄, đinh sắt tan dần và có lớp đồng màu đỏ bám ngoài mặt vì tính khử Fe > Cu và tính oxi hóa Cu²⁺ > Fe²⁺.",
            "essence": "Quy luật tự phát dịch chuyển electron từ chất có thế điện cực thấp sang chất có thế điện cực cao."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nhúng một lá sắt có khối lượng 50 gam vào 200 ml dung dịch CuSO₄ 1M. Sau một thời gian lấy lá sắt ra rửa sạch làm khô cân lại thấy khối lượng tăng thêm 0.8 gam. Tính khối lượng Cu đã bám lên lá sắt?",
            "steps": [
              "Bước 1: Phương trình phản ứng: Fe + Cu²⁺ → Fe²⁺ + Cu↓.",
              "Bước 2: Cứ 1 mol Fe phản ứng tan ra (56g) thì có 1 mol Cu bám vào (64g) ⇒ Khối lượng lá sắt tăng: Δm = 64 - 56 = 8 gam.",
              "Bước 3: Gọi số mol Fe phản ứng là x: Khối lượng tăng thực tế là 8x = 0.8 gam ⇒ x = 0.1 mol.",
              "Bước 4: Khối lượng Cu bám vào lá sắt: m_Cu = 0.1 · 64 = 6.4 gam."
            ],
            "answer": "Khối lượng Cu bám lên lá sắt là 6.4 gam."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy khối lượng tăng (0.8g) chính là khối lượng đồng bám vào.",
            "why": "Khối lượng tăng là hiệu số giữa lượng đồng bám vào và lượng sắt tan ra (m_tăng = m_Cu - m_Fe_tan)."
          }
        ]
      },
      {
        "id": "ch07",
        "title": "Chương 7: Nguyên tố nhóm IA và nhóm IIA",
        "description": "Kim loại kiềm (Li, Na, K), kim loại kiềm thổ (Mg, Ca, Ba), các hợp chất quan trọng như NaHCO₃, Na₂CO₃, Ca(OH)₂, hiện tượng nước cứng và các phương pháp làm mềm nước cứng trong sinh hoạt và công nghiệp.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Kim loại kiềm và một số hợp chất của kim loại kiềm", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Kim loại kiềm thổ và một số hợp chất của kim loại kiềm thổ", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Nước cứng và cách làm mềm nước cứng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Kim loại kiềm (Nhóm IA)",
            "definition": "Gồm Li, Na, K, Rb, Cs; có cấu hình e lớp ngoài cùng ns¹; tính khử rất mạnh tăng dần từ Li đến Cs. Bảo quản kim loại kiềm bằng cách ngâm chìm trong dầu hỏa khan.",
            "example": "Na phản ứng mãnh liệt với nước ngay ở nhiệt độ thường tỏa nhiều nhiệt và sinh khí H₂: 2Na + 2H₂O → 2NaOH + H₂↑.",
            "essence": "Năng lượng ion hóa thấp nhất trong bảng tuần hoàn, dễ dàng mất 1e ngoài cùng để đạt cấu hình khí hiếm bền vững."
          },
          {
            "term": "Nước cứng và Phân loại nước cứng",
            "definition": "Nước cứng là nước chứa nhiều ion Ca²⁺ và Mg²⁺. Gồm: Nước cứng tạm thời (chứa Ca(HCO₃)₂, Mg(HCO₃)₂), Nước cứng vĩnh cửu (chứa muối Cl⁻, SO₄²⁻ của Ca²⁺, Mg²⁺) và Nước cứng toàn phần.",
            "example": "Đun sôi nước ấm lâu ngày có cặn trắng bám đáy ấm do Ca(HCO₃)₂ nhiệt phân: Ca(HCO₃)₂ → CaCO₃↓ + CO₂↑ + H₂O.",
            "essence": "Nước cứng làm giảm bọt xà phòng, gây tắc nghẽn ống dẫn nhiệt nồi hơi và hư hại sợi vải khi giặt giũ."
          }
        ],
        "rules": [
          {
            "statement": "Phương pháp làm mềm nước cứng",
            "meaning": "Để làm mềm nước cứng, cần kết tủa hoặc trao đổi các ion Ca²⁺ và Mg²⁺ ra khỏi dung dịch. Phương pháp kết tủa: đun sôi (chỉ làm mềm nước cứng tạm thời); dùng Ca(OH)₂ vừa đủ; hoặc dùng Na₂CO₃, Na₃PO₄ (làm mềm được mọi loại nước cứng).",
            "example": "Cho Na₂CO₃ vào nước cứng vĩnh cửu: Ca²⁺ + CO₃²⁻ → CaCO₃↓; Mg²⁺ + CO₃²⁻ → MgCO₃↓.",
            "essence": "Tách loại ion Ca²⁺ và Mg²⁺ tự do bằng cách chuyển chúng về dạng kết tủa không tan hoặc hấp phụ vào hạt nhựa trao đổi cation."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Hòa tan hoàn toàn 4.6 gam kim loại Na vào 100 gam nước cất. Tính nồng độ phần trăm (%) của dung dịch NaOH thu được?",
            "steps": [
              "Bước 1: Tính mol Na: n = 4.6 / 23 = 0.2 mol.",
              "Bước 2: Phương trình phản ứng: 2Na + 2H₂O → 2NaOH + H₂↑. Số mol NaOH = 0.2 mol; số mol H₂ = 0.1 mol.",
              "Bước 3: Khối lượng NaOH sinh ra: m_NaOH = 0.2 · 40 = 8.0 gam.",
              "Bước 4: Khối lượng dung dịch sau phản ứng: m_dd = m_Na + m_H₂O - m_H₂ = 4.6 + 100 - (0.1 · 2) = 104.4 gam.",
              "Bước 5: Nồng độ %: C% = (8.0 / 104.4) · 100% ≈ 7.66%."
            ],
            "answer": "Nồng độ phần trăm của dung dịch NaOH thu được là 7.66%."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên trừ khối lượng khí H₂ bay đi khi tính khối lượng dung dịch sau phản ứng.",
            "why": "Khối lượng dung dịch bằng tổng khối lượng các chất thêm vào trừ đi kết tủa và khí bay ra."
          }
        ]
      },
      {
        "id": "ch08",
        "title": "Chương 8: Kim loại chuyển tiếp dãy thứ nhất và Phức chất",
        "description": "Đại cương kim loại chuyển tiếp (Fe, Cu, Cr), số oxi hóa biến đổi, phức chất hoá học, nguyên tử trung tâm và phối tử, liên kết phối trí và ứng dụng phức chất trong phân tích và y sinh.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Kim loại chuyển tiếp dãy thứ nhất", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Đại cương về phức chất", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Cấu tạo và liên kết trong phức chất", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Kim loại chuyển tiếp dãy thứ nhất",
            "definition": "Là các nguyên tố từ Sc (Z=21) đến Cu (Z=29) có phân lớp d đang được điền electron (3d¹⁻¹⁰4s¹⁻²). Đặc điểm: nhiều trạng thái oxi hóa khác nhau, ion thường có màu và khả năng tạo phức chất cao.",
            "example": "Sắt có số oxi hóa +2 và +3 (Fe²⁺ dung dịch màu xanh lục nhạt, Fe³⁺ dung dịch màu vàng nâu), Crom có các số oxi hóa +2, +3, +6.",
            "essence": "Các electron ở phân lớp 3d và 4s có mức năng lượng gần nhau nên đều có thể tham gia vào liên kết hóa học."
          },
          {
            "term": "Phức chất (Coordination compound)",
            "definition": "Là hợp chất gồm nguyên tử trung tâm (thường là ion kim loại chuyển tiếp) liên kết với các phối tử (phân tử hoặc anion có đôi electron tự do) bằng liên kết cho - nhận (liên kết phối trí).",
            "example": "Phức chất [Cu(NH₃)₄]²⁺ có ion trung tâm là Cu²⁺, 4 phối tử NH₃ liên kết với ion đồng tạo dung dịch màu xanh lam thẫm.",
            "essence": "Sự xen phủ giữa orbital trống của ion kim loại chuyển tiếp với orbital chứa cặp electron chưa liên kết của phối tử."
          }
        ],
        "rules": [
          {
            "statement": "Đặc trưng hình học của phức chất",
            "meaning": "Số phối trí của ion trung tâm quyết định cấu trúc hình học của phức chất: Số phối trí 2 thường có dạng đường thẳng [Ag(NH₃)₂]⁺; số phối trí 4 có dạng tứ diện hoặc vuông phẳng; số phối trí 6 có dạng bát diện đều như [Fe(CN)₆]³⁻.",
            "example": "Phức chất [Pt(NH₃)₂Cl₂] (thuốc chống ung thư cisplatin) có cấu trúc vuông phẳng.",
            "essence": "Sự sắp xếp không gian tối ưu để giảm thiểu lực đẩy giữa các đám mây electron của các phối tử xung quanh tâm."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho phức chất [Co(NH₃)₆]Cl₃. Xác định nguyên tử trung tâm, phối tử, số phối trí của Co và số oxi hóa của Coban trong phức chất?",
            "steps": [
              "Bước 1: Cầu ngoại là 3 ion Cl⁻, mỗi ion có điện tích -1. Suy ra điện tích của cầu nội [Co(NH₃)₆] là +3.",
              "Bước 2: Phối tử là các phân tử trung hòa NH₃ (điện tích bằng 0).",
              "Bước 3: Do đó số oxi hóa của nguyên tử trung tâm Coban (Co) là +3.",
              "Bước 4: Có 6 phối tử NH₃ liên kết trực tiếp với ion Co³⁺ nên số phối trí của Co bằng 6."
            ],
            "answer": "Nguyên tử trung tâm là Co³⁺, phối tử là NH₃, số phối trí là 6, số oxi hóa của Co là +3."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm số phối trí với hóa trị thông thường của kim loại.",
            "why": "Số phối trí là số liên kết cho - nhận giữa ion trung tâm với các phối tử, ví dụ Cu²⁺ có hóa trị 2 nhưng số phối trí trong [Cu(NH₃)₄]²⁺ là 4."
          }
        ]
      }
    ]
  },
  "sinh-hoc": {
    "id": "sinh-hoc",
    "name": "Sinh học",
    "icon": "🧬",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Di truyền phân tử và Di truyền nhiễm sắc thể",
        "description": "Cơ chế di truyền ở cấp độ phân tử: nhân đôi DNA, phiên mã, dịch mã, điều hòa hoạt động gen; đột biến gen; cơ chế di truyền cấp độ tế bào: cấu trúc NST, các dạng đột biến NST.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Gen, mã di truyền và quá trình nhân đôi DNA", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phiên mã và Dịch mã", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Điều hòa biểu hiện gen", "hasRealContent": true },
          { "id": "l04", "title": "Bài 4: Đột biến gen", "hasRealContent": true },
          { "id": "l05", "title": "Bài 5: Nhiễm sắc thể và đột biến nhiễm sắc thể", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Mã di truyền và Đặc điểm của mã di truyền",
            "definition": "Mã di truyền là mã bộ ba: cứ 3 nucleotide liền kề trên mARN mã hóa cho 1 axit amin. Có 4 đặc điểm: Tính liên tục (đọc từ 1 điểm xác định không gối lên nhau), Tính phổ biến (hầu hết sinh vật dùng chung), Tính đặc hiệu (1 bộ ba chỉ mã hóa 1 axit amin) và Tính thoái hóa (nhiều bộ ba cùng mã hóa 1 axit amin).",
            "example": "Mã mở đầu 5'-AUG-3' quy định axit amin Methionine ở sinh vật nhân thực; 3 mã kết thúc: 5'-UAA-3', 5'-UAG-3', 5'-UGA-3'.",
            "essence": "Mã hóa thông tin cấu trúc protein từ trình tự nucleotide trong axit nucleic."
          },
          {
            "term": "Mô hình Operon Lac ở vi khuẩn E. coli",
            "definition": "Là cụm các gen cấu trúc có liên quan về chức năng được điều hòa bởi một vùng chỉ huy operator (O) duy nhất. Gồm: Vùng khởi động P, vùng chỉ huy O và các gen cấu trúc Z, Y, A quy định enzyme phân giải lactose.",
            "example": "Khi môi trường có lactose: Lactose liên kết với protein ức chế làm nó biến đổi cấu hình không gắn được vào O, ARN polymerase bám vào P tiến hành phiên mã tạo enzyme.",
            "essence": "Tiết kiệm năng lượng cho tế bào: chỉ tổng hợp protein khi môi trường có cơ chất cần chuyển hóa."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc bán bảo tồn và bổ sung trong nhân đôi DNA",
            "meaning": "Trong mỗi phân tử DNA con tạo thành có 1 mạch cũ của DNA mẹ và 1 mạch mới được tổng hợp theo nguyên tắc bổ sung: A liên kết với T bằng 2 liên kết hydro, G liên kết với C bằng 3 liên kết hydro.",
            "example": "Từ 1 phân tử DNA mẹ ban đầu mang phóng xạ ¹⁵N, sau 3 thế hệ nhân đôi trong môi trường ¹⁴N thu được 8 phân tử DNA con, trong đó có đúng 2 phân tử mang phóng xạ lai ¹⁴N-¹⁵N.",
            "essence": "Đảm bảo thông tin di truyền được truyền đạt chính xác nguyên vẹn qua các thế hệ tế bào và cá thể."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một phân tử DNA ở sinh vật nhân sơ có chiều dài 4080 Å và có 3120 liên kết hydro. Tính số lượng từng loại nucleotide (A, T, G, C) của phân tử DNA này?",
            "steps": [
              "Bước 1: Tổng số nucleotide của DNA: N = (2 · L) / 3.4 = (2 · 4080) / 3.4 = 2400 nucleotide.",
              "Bước 2: Hệ phương trình: (1) 2A + 2G = 2400 (do A = T và G = C); (2) 2A + 3G = 3120 (tổng liên kết H).",
              "Bước 3: Lấy phương trình (2) trừ phương trình (1): G = 3120 - 2400 = 720 nucleotide.",
              "Bước 4: Thay G vào (1): 2A = 2400 - 2·720 = 2400 - 1440 = 960 ⇒ A = 480 nucleotide."
            ],
            "answer": "A = T = 480 nucleotide; G = C = 720 nucleotide."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên chiều của mạch tổng hợp: ARN polymerase di chuyển dọc theo mạch khuôn theo chiều 3' → 5' nhưng tổng hợp mạch mới theo chiều 5' → 3'.",
            "why": "Enzyme polymer hóa chỉ có thể kéo dài đầu 3'-OH tự do của chuỗi nucleotide mới."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Di truyền quần thể và Di truyền học người",
        "description": "Cấu trúc di truyền quần thể tự phối và ngẫu phối, định luật trạng thái cân bằng di truyền Hardy - Weinberg, di truyền học người và phương pháp phả hệ.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cấu trúc di truyền của quần thể", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Định luật Hardy – Weinberg", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Di truyền học người và tư vấn di truyền", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tần số alen và Cấu trúc di truyền của quần thể",
            "definition": "Vốn gen của quần thể đặc trưng bởi tần số các alen và tần số các kiểu gen. Với gen có 2 alen A và a: Tần số alen p(A) = x + y/2; q(a) = z + y/2 với cấu trúc x AA + y Aa + z aa = 1 (p + q = 1).",
            "example": "Quần thể có cấu trúc 0.36 AA : 0.48 Aa : 0.16 aa có tần số alen p(A) = 0.36 + 0.24 = 0.6 và q(a) = 0.4.",
            "essence": "Quần thể là đơn vị tiến hóa cơ sở, sự biến đổi tần số alen qua các thế hệ phản ánh tiến trình tiến hóa."
          },
          {
            "term": "Định luật Hardy – Weinberg về cân bằng di truyền",
            "definition": "Trong một quần thể ngẫu phối kích thước lớn, không có đột biến, không có di - nhập gen và không có chọn lọc tự nhiên thì tần số alen và thành phần kiểu gen duy trì không đổi qua các thế hệ: p² AA + 2pq Aa + q² aa = 1.",
            "example": "Nếu p = 0.7 và q = 0.3 thì ở trạng thái cân bằng: 0.49 AA + 0.42 Aa + 0.09 aa = 1.",
            "essence": "Giải thích tại sao trong tự nhiên các đột biến lặn có hại vẫn tồn tại ổn định trong quần thể dưới dạng dị hợp tử."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm di truyền của quần thể tự thụ phấn qua các thế hệ",
            "meaning": "Qua các thế hệ tự thụ phấn hoặc giao phối cận huyết: Tỉ lệ kiểu gen dị hợp tử giảm dần đi một nửa sau mỗi thế hệ: Tỉ lệ Aa = (1/2)ⁿ; tỉ lệ đồng hợp tử tăng dần.",
            "example": "Từ 100% Aa ban đầu, sau 3 thế hệ tự thụ: tỉ lệ Aa = (1/2)³ = 1/8 (12.5%), tỉ lệ đồng hợp AA = aa = (1 - 1/8) / 2 = 7/16 (43.75%).",
            "essence": "Tự phối làm phân hóa quần thể thành các dòng thuần chủng, dễ làm bộc lộ các gen lặn có hại dẫn đến thoái hóa giống."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một quần thể người ở trạng thái cân bằng di truyền có 9% số người mắc bệnh bạch tạng (do gen lặn a nằm trên NST thường quy định). Tính tỉ lệ phần trăm người bình thường mang gen gây bệnh (kiểu gen Aa) trong quần thể?",
            "steps": [
              "Bước 1: Quần thể cân bằng nên tỉ lệ người bạch tạng aa = q² = 0.09 ⇒ Tần số alen q(a) = √0.09 = 0.3.",
              "Bước 2: Tần số alen A: p(A) = 1 - q = 1 - 0.3 = 0.7.",
              "Bước 3: Tỉ lệ người bình thường mang gen gây bệnh (Aa): 2pq = 2 · 0.7 · 0.3 = 0.42 = 42%."
            ],
            "answer": "Tỉ lệ người bình thường mang gen bệnh (Aa) trong quần thể là 42%."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy luôn tỉ lệ người bệnh (0.09) làm tần số alen q.",
            "why": "Tỉ lệ kiểu hình lặn aa bằng q bình phương (q²); muốn tìm tần số alen q phải lấy căn bậc hai của tỉ lệ kiểu hình lặn."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Ứng dụng di truyền học và Công nghệ sinh học",
        "description": "Các phương pháp chọn tạo giống truyền thống, ưu thế lai, công nghệ tế bào thực vật và động vật, công nghệ DNA tái tổ hợp và tạo sinh vật biến đổi gen (GMO).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Chọn tạo giống cây trồng và vật nuôi", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Công nghệ tế bào và ứng dụng", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Công nghệ gen và sinh vật biến đổi gen", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Công nghệ DNA tái tổ hợp",
            "definition": "Là quy trình kĩ thuật chuyển một đoạn DNA mang gen mong muốn từ tế bào cho sang tế bào nhận nhờ thể truyền (plasmid hoặc virus). Cần 2 enzyme chính: Enzyme cắt giới hạn Restrictase và enzyme nối Ligase.",
            "example": "Sản xuất insulin người chữa bệnh tiểu đường bằng cách chuyển gen insulin của người vào vi khuẩn E. coli.",
            "essence": "Biến vi sinh vật thành những nhà máy sinh học sản xuất protein quý của người và động vật với giá thành rẻ và quy mô công nghiệp."
          },
          {
            "term": "Ưu thế lai",
            "definition": "Hiện tượng con lai F1 có sức sống, năng suất, khả năng chống chịu vượt trội so với cả hai dạng bố mẹ thuần chủng.",
            "example": "Lai ngô dòng A với dòng B thu được ngô lai F1 bắp to, hạt chắc, kháng sâu bệnh tốt dùng để gieo trồng thu hoạch thương phẩm.",
            "essence": "Thuyết siêu trội: Các alen ở trạng thái dị hợp tử AaBb có tác dụng tương tác bổ sung mang lại kiểu hình vượt trội so với đồng hợp tử."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc sử dụng con lai F1 trong sản xuất nông nghiệp",
            "meaning": "Con lai F1 có ưu thế lai cao nhất chỉ dùng vào mục đích kinh tế (thương phẩm), tuyệt đối không dùng làm giống cho vụ sau.",
            "example": "Nếu lấy hạt ngô F1 đem gieo vụ sau, con lai F2 sẽ phân li kiểu gen làm tỉ lệ dị hợp giảm, đồng hợp tăng dẫn đến thoái hóa giống nghiêm trọng.",
            "essence": "Quy luật phân li Menđen làm giảm sút kiểu gen dị hợp qua sinh sản hữu tính."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày 3 bước cơ bản trong quy trình tạo giống vi khuẩn E. coli sản xuất hoocmôn insulin của người bằng công nghệ gen.",
            "steps": [
              "Bước 1: Tách chiết thể truyền (plasmid của vi khuẩn) và tách chiết đoạn DNA mang gen mã hóa insulin từ tế bào người.",
              "Bước 2: Dùng cùng một loại enzyme cắt Restrictase để cắt mở vòng plasmid và cắt gen insulin; sau đó dùng enzyme nối Ligase tạo phân tử DNA tái tổ hợp.",
              "Bước 3: Chuyển DNA tái tổ hợp vào tế bào vi khuẩn E. coli; nuôi cấy trong môi trường nhân tạo để vi khuẩn nhân lên và biểu hiện gen sản xuất insulin tinh khiết."
            ],
            "answer": "Quy trình gồm 3 bước: Tạo DNA tái tổ hợp -> Đưa DNA tái tổ hợp vào tế bào nhận -> Phân lập dòng tế bào chứa DNA tái tổ hợp và thu hồi sản phẩm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng enzyme cắt restrictase có thể cắt ngẫu nhiên ở vị trí bất kỳ.",
            "why": "Mỗi loại restrictase chỉ nhận biết và cắt đứt liên kết photphodieste tại các trình tự nucleotide đối xứng đặc hiệu xác định (vùng palindrome)."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Tiến hóa",
        "description": "Các bằng chứng tiến hóa (giải phẫu so sánh, phôi sinh học, sinh học phân tử), học thuyết tiến hóa hiện đại, các nhân tố tiến hóa (đột biến, di nhập gen, chọn lọc tự nhiên, phiêu bạt di truyền, giao phối không ngẫu nhiên), sự hình thành loài mới.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Các bằng chứng tiến hóa", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các nhân tố tiến hóa trong thuyết tiến hóa hiện đại", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Quá trình hình thành loài mới", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Cơ quan tương đồng và Cơ quan tương tự",
            "definition": "Cơ quan tương đồng là những cơ quan bắt nguồn từ cùng một nguồn gốc phôi thai nhưng biến đổi thích nghi với chức năng khác nhau (phản ánh tiến hóa phân li). Cơ quan tương tự có nguồn gốc khác nhau nhưng đảm nhiệm chức năng tương tự nhau (phản ánh tiến hóa đồng quy).",
            "example": "Cánh dơi và tay người là cơ quan tương đồng (cùng nguồn gốc chi trước động vật có vú). Cánh chim và cánh bướm là cơ quan tương tự (đều dùng để bay nhưng nguồn gốc khác nhau).",
            "essence": "Chứng cứ giải phẫu so sánh chứng minh mối quan hệ họ hàng phát sinh giữa các loài sinh vật."
          },
          {
            "term": "Chọn lọc tự nhiên (CLTN)",
            "definition": "Là nhân tố tiến hóa có hướng duy nhất: tác động trực tiếp lên kiểu hình, qua đó gián tiếp làm biến đổi tần số alen và thành phần kiểu gen của quần thể theo hướng thích nghi.",
            "example": "Bướm sâu đo bạch dương ở vùng công nghiệp có màu cánh đen chiếm ưu thế so với bướm cánh trắng nhờ ngụy trang trên thân cây bị bám muội than tránh chim ăn thịt.",
            "essence": "Giữ lại và nhân rộng các biến dị có lợi, đào thải các biến dị có hại đối với sinh vật trong điều kiện môi trường sống cụ thể."
          }
        ],
        "rules": [
          {
            "statement": "Tác động của các yếu tố ngẫu nhiên (Phiêu bạt di truyền)",
            "meaning": "Các biến cố ngẫu nhiên (thiên tai, dịch bệnh, núi lửa) có thể làm thay đổi đột ngột tần số alen của quần thể không theo hướng xác định; một alen có lợi có thể bị đào thải hoàn toàn và alen có hại có thể trở nên phổ biến.",
            "example": "Một trận bão làm chết ngẫu nhiên 90% cá thể của một đàn hươu trên đảo nhỏ, làm mất hoàn toàn alen hiếm A trong quần thể.",
            "essence": "Yếu tố ngẫu nhiên tác động mạnh nhất đối với các quần thể có kích thước cá thể nhỏ."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao đột biến gen được coi là nguyên liệu sơ cấp của tiến hóa, mặc dù phần lớn đột biến gen là có hại cho thể đột biến?",
            "steps": [
              "Bước 1: Đột biến gen liên tục phát sinh qua các thế hệ với số lượng gen rất lớn trong quần thể, tạo ra nguồn alen mới phong phú.",
              "Bước 2: Phần lớn đột biến là lặn, ở trạng thái dị hợp tử không biểu hiện ra kiểu hình nên không bị chọn lọc tự nhiên đào thải ngay lập tức.",
              "Bước 3: Giá trị thích nghi của đột biến thay đổi tùy thuộc vào tổ hợp gen và điều kiện môi trường sống; một đột biến có hại ở môi trường này có thể trở nên có lợi khi môi trường thay đổi."
            ],
            "answer": "Đột biến gen cung cấp nguồn alen mới duy nhất cho tiến hóa, được bảo lưu dưới dạng dị hợp tử và cung cấp tiềm năng thích nghi to lớn khi hoàn cảnh sống thay đổi."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng chọn lọc tự nhiên tạo ra các biến dị thích nghi mới cho sinh vật.",
            "why": "CLTN không tạo ra biến dị; đột biến và giao phối tạo ra biến dị, CLTN chỉ làm nhiệm vụ sàng lọc và giữ lại những biến dị đã có sẵn."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Sinh thái học cá thể và Quần thể",
        "description": "Môi trường và các nhân tố sinh thái, giới hạn sinh thái, ổ sinh thái, các đặc trưng cơ bản của quần thể sinh vật (mật độ, tỉ lệ giới tính, nhóm tuổi, phân bố cá thể), biến động số lượng cá thể.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Môi trường sống và các nhân tố sinh thái", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Quần thể sinh vật và các đặc trưng cơ bản", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Biến động số lượng cá thể của quần thể", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Giới hạn sinh thái và Ổ sinh thái",
            "definition": "Giới hạn sinh thái là khoảng giá trị xác định của một nhân tố sinh thái mà ở đó sinh vật có thể tồn tại và phát triển. Ổ sinh thái là một 'không gian sinh thái' bao gồm tập hợp tất cả các giới hạn sinh thái của các nhân tố cho phép loài tồn tại và phát triển lâu dài.",
            "example": "Cá rô phi ở Việt Nam có giới hạn nhiệt độ từ 5.6 °C đến 42 °C, điểm cực thuận là 30 °C. Dưới 5.6 °C và trên 42 °C cá rô phi sẽ chết.",
            "essence": "Ổ sinh thái thể hiện cách thức thích nghi và vị trí sinh thái của một loài trong mối tương quan với các loài khác."
          },
          {
            "term": "Mật độ cá thể của quần thể",
            "definition": "Là số lượng cá thể sinh vật trên một đơn vị diện tích hay thể tích của quần thể. Mật độ là đặc trưng cơ bản và quan trọng nhất của quần thể sinh vật.",
            "example": "Mật độ cây thông là 1000 cây/ha; mật độ cá mè là 2 con/m³ nước ao.",
            "essence": "Mật độ chi phối mức độ sử dụng nguồn sống, mức độ sinh sản và tỉ lệ tử vong của các cá thể trong quần thể."
          }
        ],
        "rules": [
          {
            "statement": "Cơ chế tự điều chỉnh số lượng cá thể của quần thể",
            "meaning": "Khi mật độ cá thể tăng quá cao dẫn đến thiếu thức ăn và nơi ở, cạnh tranh gay gắt làm tăng tỉ lệ tử vong và xuất cư, giảm tỉ lệ sinh sản, đưa số lượng cá thể trở về mức cân bằng phù hợp với sức chứa của môi trường.",
            "example": "Hiện tượng tỉa thưa tự nhiên ở thực vật khi cây non mọc quá dày: các cây yếu thế bị che khuất ánh sáng sẽ chết dần.",
            "essence": "Khả năng tự cân bằng nội tại đảm bảo sự tồn tại bền vững của quần thể trước áp lực sinh thái."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân biệt biến động số lượng cá thể theo chu kỳ và biến động số lượng không theo chu kỳ. Cho ví dụ cụ thể cho mỗi dạng.",
            "steps": [
              "Bước 1: Biến động theo chu kỳ là biến động số lượng xảy ra do những thay đổi có chu kỳ của điều kiện môi trường (chu kỳ ngày đêm, chu kỳ mùa, chu kỳ nhiều năm). Ví dụ: Ếch nhái sinh sản nhiều vào mùa mưa; số lượng cáo Bắc Cực biến động theo chu kỳ 3 - 4 năm theo số lượng chuột lemmut.",
              "Bước 2: Biến động không theo chu kỳ là biến động số lượng cá thể tăng hoặc giảm đột ngột do những thay đổi bất thường của điều kiện tự nhiên hoặc hoạt động con người. Ví dụ: Rừng tràm bị cháy làm chết hàng loạt chim muông; dịch tả lợn châu Phi làm giảm đột ngột số lượng đàn lợn."
            ],
            "answer": "Biến động theo chu kỳ gắn với quy luật thời gian định kỳ của môi trường; biến động không theo chu kỳ do tác nhân đột xuất, bất thường gây ra."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đồng nhất khái niệm 'Nơi ở' với 'Ổ sinh thái'.",
            "why": "Nơi ở chỉ là địa chỉ cư trú vật lý của loài; ổ sinh thái là toàn bộ vai trò sinh thái và cách loài đó tương tác, khai thác tài nguyên trong nơi ở."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Quần xã sinh vật và Hệ sinh thái",
        "description": "Cấu trúc và mối quan hệ sinh thái trong quần xã, diễn thế sinh thái, hệ sinh thái và chuỗi - lưới thức ăn, tháp sinh thái, chu trình sinh địa hóa và bảo vệ sinh quyển.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Quần xã sinh vật và diễn thế sinh thái", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hệ sinh thái và các chu trình sinh địa hóa", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Sinh thái học phục hồi và bảo tồn thiên nhiên", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chuỗi thức ăn và Lưới thức ăn",
            "definition": "Chuỗi thức ăn gồm nhiều loài sinh vật có quan hệ dinh dưỡng với nhau, mỗi loài là một mắt xích. Tập hợp các chuỗi thức ăn có mắt xích chung tạo thành một lưới thức ăn phức tạp trong hệ sinh thái.",
            "example": "Chuỗi thức ăn trên cạn: Cỏ (SV sản xuất) → Châu chấu (SV tiêu thụ bậc 1) → Ếch (SV tiêu thụ bậc 2) → Rắn (SV tiêu thụ bậc 3) → Vi sinh vật phân giải.",
            "essence": "Mô tả đường đi và dòng luân chuyển của vật chất và năng lượng qua các bậc dinh dưỡng trong tự nhiên."
          },
          {
            "term": "Hiệu suất sinh thái và Quy luật tháp năng lượng",
            "definition": "Là tỉ lệ phần trăm chuyển hóa năng lượng giữa các bậc dinh dưỡng liên tiếp trong hệ sinh thái. Năng lượng qua mỗi bậc dinh dưỡng bị thất thoát trung bình khoảng 90% (qua hô hấp, bài tiết, tỏa nhiệt), chỉ khoảng 10% được tích lũy lên bậc tiếp theo.",
            "example": "Nếu sinh vật sản xuất tích lũy 10⁶ kcal thì sinh vật tiêu thụ bậc 1 chỉ nhận được khoảng 10⁵ kcal, và sinh vật tiêu thụ bậc 2 nhận khoảng 10⁴ kcal.",
            "essence": "Chuỗi thức ăn trong tự nhiên thường ngắn (không quá 4 - 5 mắt xích) do sự hao hụt năng lượng khổng lồ qua từng bậc chuyển hóa."
          }
        ],
        "rules": [
          {
            "statement": "Quy luật dòng năng lượng trong hệ sinh thái",
            "meaning": "Dòng năng lượng trong hệ sinh thái đi theo một chiều duy nhất từ năng lượng ánh sáng mặt trời -> Sinh vật sản xuất -> Các bậc sinh vật tiêu thụ -> Thất thoát vào môi trường dưới dạng nhiệt (không tuần hoàn tái sử dụng).",
            "example": "Trái ngược với chu trình vật chất (C, N, H₂O) tuần hoàn khép kín, năng lượng bị phân tán hoàn toàn vào vũ trụ.",
            "essence": "Hệ sinh thái cần liên tục được cung cấp năng lượng mặt trời để duy trì sự sống."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trong một hệ sinh thái đồng cỏ, giả sử cỏ tích lũy được 5 · 10⁶ kcal năng lượng. Biết hiệu suất sinh thái giữa bậc dinh dưỡng cấp 1 và cấp 2 là 10%, giữa cấp 2 và cấp 3 là 12%. Tính năng lượng tích lũy ở sinh vật tiêu thụ bậc 2?",
            "steps": [
              "Bước 1: Bậc dinh dưỡng cấp 1 là sinh vật sản xuất (cỏ): E₁ = 5 · 10⁶ kcal.",
              "Bước 2: Bậc dinh dưỡng cấp 2 (sinh vật tiêu thụ bậc 1): E₂ = E₁ · 10% = 5 · 10⁶ · 0.10 = 5 · 10⁵ kcal.",
              "Bước 3: Bậc dinh dưỡng cấp 3 (sinh vật tiêu thụ bậc 2): E₃ = E₂ · 12% = 5 · 10⁵ · 0.12 = 6 · 10⁴ kcal."
            ],
            "answer": "Năng lượng tích lũy ở sinh vật tiêu thụ bậc 2 là 6 · 10⁴ kcal."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa 'bậc dinh dưỡng' và 'sinh vật tiêu thụ'.",
            "why": "Sinh vật sản xuất là bậc dinh dưỡng cấp 1; do đó sinh vật tiêu thụ bậc 1 thuộc bậc dinh dưỡng cấp 2, sinh vật tiêu thụ bậc 2 thuộc bậc dinh dưỡng cấp 3."
          }
        ]
      }
    ]
  },
  "tin-hoc": {
    "id": "tin-hoc",
    "name": "Tin học",
    "icon": "💻",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Máy tính và Xã hội tri thức",
        "description": "Khái niệm và lịch sử phát triển của Trí tuệ nhân tạo (AI), các ứng dụng nổi bật của AI trong khoa học kĩ thuật, y tế, giáo dục và các vấn đề xã hội liên quan.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Làm quen với Trí tuệ nhân tạo", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Trí tuệ nhân tạo trong khoa học và đời sống", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Trí tuệ nhân tạo (AI - Artificial Intelligence)",
            "definition": "Là khả năng của máy tính hoặc hệ thống kỹ thuật số thực hiện các nhiệm vụ thường đòi hỏi trí thông minh của con người như học tập, suy luận logic, giải quyết vấn đề, nhận dạng tiếng nói và thị giác máy tính.",
            "example": "Hệ thống nhận diện khuôn mặt mở khóa điện thoại, trợ lý ảo Siri/Google Assistant, xe tự hành Tesla.",
            "essence": "Mô phỏng các năng lực trí tuệ nhận thức của não bộ người thông qua các mô hình toán học và giải thuật máy tính."
          },
          {
            "term": "AI hẹp (Narrow AI) và AI tổng quát (AGI)",
            "definition": "AI hẹp được thiết kế và huấn luyện chuyên sâu để thực hiện một nhiệm vụ cụ thể duy nhất (như chơi cờ, chẩn đoán ảnh X-quang). AGI là hệ thống có trí tuệ toàn diện tương đương con người, có khả năng tự học và giải quyết mọi tác vụ nhận thức.",
            "example": "AlphaGo đánh bại kiện tướng cờ vây thế giới là AI hẹp; hệ thống AGI vẫn đang trong giai đoạn nghiên cứu lý thuyết.",
            "essence": "Phần lớn các hệ thống AI ứng dụng trong đời sống hiện nay đều thuộc loại AI hẹp."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc đạo đức khi phát triển và sử dụng AI",
            "meaning": "Việc sử dụng công nghệ AI phải tuân thủ tính minh bạch, bảo vệ quyền riêng tư dữ liệu cá nhân của người dùng, không tạo ra định kiến phân biệt đối xử và con người phải luôn giữ quyền kiểm soát tối hậu.",
            "example": "Không sử dụng deepfake giả mạo hình ảnh, giọng nói người khác để lừa đảo hoặc bôi nhọ danh dự.",
            "essence": "Công nghệ phục vụ con người một cách nhân văn, có trách nhiệm và tuân thủ pháp luật."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích 2 ứng dụng tiêu biểu của AI trong y tế hiện đại và nêu 1 thách thức đạo đức cần lưu ý.",
            "steps": [
              "Bước 1: Ứng dụng chẩn đoán hình ảnh: AI thị giác máy tính phân tích ảnh chụp cắt lớp CT/MRI để phát hiện sớm các khối u với độ chính xác cao.",
              "Bước 2: Ứng dụng phát triển thuốc mới: Các mô hình học sâu mô phỏng cấu trúc protein (như AlphaFold) giúp rút ngắn thời gian thiết kế thuốc từ hàng năm xuống vài tuần.",
              "Bước 3: Thách thức đạo đức: Vấn đề bảo mật hồ sơ bệnh án cá nhân của bệnh nhân và trách nhiệm pháp lý khi AI đưa ra chẩn đoán sai lệch."
            ],
            "answer": "AI hỗ trợ đắc lực trong chẩn đoán hình ảnh và tổng hợp dược phẩm; cần bảo đảm bí mật dữ liệu y tế và trách nhiệm giám sát của bác sĩ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng AI có cảm xúc và ý thức tự chủ độc lập như con người.",
            "why": "AI hiện đại hoạt động dựa trên các thuật toán thống kê xác suất và nhận dạng mẫu từ dữ liệu lớn, hoàn toàn không có cảm xúc hay ý thức sinh học."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Mạng máy tính và Internet",
        "description": "Các thiết bị mạng thông dụng (Switch, Router, Access Point), mô hình và giao thức mạng TCP/IP, địa chỉ IP và subnet mask, chia sẻ tài nguyên an toàn trên mạng nội bộ LAN.",
        "lessons": [
          { "id": "l01", "title": "Bài 3: Một số thiết bị mạng thông dụng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 4: Giao thức mạng", "hasRealContent": true },
          { "id": "l03", "title": "Bài 5: Thực hành chia sẻ tài nguyên trên mạng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bộ định tuyến (Router) và Bộ chuyển mạch (Switch)",
            "definition": "Switch hoạt động ở tầng liên kết dữ liệu (Data Link), kết nối các thiết bị trong cùng một mạng LAN nội bộ bằng địa chỉ MAC. Router hoạt động ở tầng mạng (Network), định tuyến các gói tin giữa các mạng khác nhau bằng địa chỉ IP.",
            "example": "Switch kết nối các máy tính trong phòng thực hành tin học; Router kết nối toàn bộ mạng trường học với nhà cung cấp dịch vụ Internet (ISP).",
            "essence": "Switch mở rộng phạm vi kết nối nội bộ, còn Router định hướng đường truyền dữ liệu xuyên biên giới mạng."
          },
          {
            "term": "Bộ giao thức TCP/IP",
            "definition": "Là bộ quy tắc truyền thông chuẩn trên Internet. IP (Internet Protocol) chịu trách nhiệm đánh địa chỉ và chuyển phát gói tin đến đúng đích. TCP (Transmission Control Protocol) đảm bảo truyền dữ liệu tin cậy, không mất gói tin và đúng thứ tự.",
            "example": "Khi tải tệp tin, TCP tự động kiểm tra mã kiểm lỗi và yêu cầu gửi lại các gói tin bị mất trên đường truyền.",
            "essence": "Ngôn ngữ chung cho phép hàng tỉ máy tính có phần cứng và hệ điều hành khác nhau giao tiếp đồng bộ với nhau."
          }
        ],
        "rules": [
          {
            "statement": "Cấu trúc địa chỉ IPv4",
            "meaning": "Địa chỉ IPv4 gồm 32 bit nhị phân, biểu diễn thành 4 số thập phân từ 0 đến 255 ngăn cách nhau bởi dấu chấm (dotted decimal notation), chia thành phần định danh mạng (NetID) và phần định danh máy (HostID) nhờ Subnet Mask.",
            "example": "Địa chỉ 192.168.1.1 với Subnet Mask 255.255.255.0 có NetID là 192.168.1.0 và HostID là 1.",
            "essence": "Hệ thống định danh duy nhất cho từng giao diện mạng trong không gian địa chỉ toàn cầu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho biết dải địa chỉ IP riêng (Private IP) thông dụng trong mạng LAN gia đình và giải thích vai trò của NAT (Network Address Translation)?",
            "steps": [
              "Bước 1: Các dải IP riêng chuẩn: Lớp A: 10.0.0.0/8; Lớp B: 172.16.0.0/12; Lớp C: 192.168.0.0/16 (phổ biến nhất cho gia đình).",
              "Bước 2: Vai trò của NAT: Công nghệ biên dịch cho phép nhiều thiết bị dùng IP riêng trong mạng LAN cùng chia sẻ một địa chỉ IP công cộng (Public IP) duy nhất để truy cập Internet.",
              "Bước 3: Lợi ích: Tiết kiệm không gian địa chỉ IPv4 toàn cầu và tăng cường bảo mật cho các thiết bị nội bộ."
            ],
            "answer": "Dải IP riêng phổ biến là 192.168.x.x; NAT giúp chia sẻ một IP công cộng cho nhiều thiết bị nội bộ và bảo vệ an ninh mạng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa địa chỉ IP (địa chỉ logic thay đổi theo mạng) và địa chỉ MAC (địa chỉ vật lý cố định ghi trong chip card mạng).",
            "why": "Địa chỉ MAC do nhà sản xuất gán cứng; khi chuyển sang mạng khác, địa chỉ IP thay đổi nhưng MAC vẫn giữ nguyên."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Đạo đức, pháp luật và văn hoá trong môi trường số",
        "description": "Giao tiếp văn minh trên không gian mạng, ứng xử có trách nhiệm, giữ gìn tính nhân văn, bảo vệ thông tin cá nhân và phòng tránh bẫy lừa đảo trực tuyến.",
        "lessons": [
          { "id": "l01", "title": "Bài 6: Giao tiếp và ứng xử trong không gian mạng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Văn hóa ứng xử trên không gian mạng (Netiquette)",
            "definition": "Là tập hợp các chuẩn mực đạo đức, thái độ tôn trọng, ngôn từ chuẩn mực và hành vi văn minh khi tham gia tương tác, bình luận, chia sẻ thông tin trên môi trường mạng số.",
            "example": "Không sử dụng ngôn từ kích động, xúc phạm người khác; kiểm chứng độ xác thực của thông tin trước khi chia sẻ lên mạng xã hội.",
            "essence": "Môi trường ảo nhưng nhân cách và trách nhiệm pháp lý là hoàn toàn có thật."
          },
          {
            "term": "Bảo vệ dấu chân số (Digital Footprint)",
            "definition": "Là toàn bộ các vết tích dữ liệu mà một người để lại khi sử dụng Internet như lịch sử duyệt web, thông tin cá nhân, bài đăng mạng xã hội và bình luận trực tuyến.",
            "example": "Không công khai số CCCD, tài khoản ngân hàng, vị trí thời gian thực trên các diễn đàn công cộng.",
            "essence": "Dấu chân số có thể tồn tại vĩnh viễn và ảnh hưởng trực tiếp đến uy tín cá nhân và sự nghiệp tương lai."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc kiểm chứng thông tin trực tuyến (S.T.O.P)",
            "meaning": "Khi tiếp cận tin tức giật gân: Dừng lại (Stop), Tìm hiểu nguồn gốc (Track source), Tìm kiếm góc nhìn đối chứng (Other sources) và Kiểm tra bối cảnh (Perspective) trước khi tin tưởng hoặc bấm chia sẻ.",
            "example": "Không lan truyền các tin tức cắt ghép hình ảnh sai sự thật nhằm câu tương tác hoặc gây hoang mang dư luận.",
            "essence": "Tư duy phản biện là bức tường lửa bảo vệ nhận thức người dùng trong thời đại bùng nổ tin giả."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 3 biện pháp thiết thực để học sinh lớp 12 tự bảo vệ tài khoản mạng xã hội trước nguy cơ bị đánh cắp (hack)?",
            "steps": [
              "Bước 1: Đặt mật khẩu mạnh (trên 12 ký tự, kết hợp chữ hoa, chữ thường, chữ số và ký tự đặc biệt) và không dùng chung mật khẩu cho nhiều tài khoản.",
              "Bước 2: Bật tính năng xác thực hai yếu tố (2FA - Two-Factor Authentication) qua ứng dụng tạo mã (Google Authenticator) thay vì chỉ dùng SMS.",
              "Bước 3: Tuyệt đối không bấm vào các đường liên kết lạ (phishing link) gửi qua tin nhắn messenger hoặc email yêu cầu đăng nhập lại tài khoản."
            ],
            "answer": "3 biện pháp then chốt: Mật khẩu mạnh riêng biệt, Bật xác thực 2 bước (2FA), và Cảnh giác không bấm vào liên kết lạ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng việc ẩn danh trên mạng xã hội sẽ giúp người dùng không bị phát hiện khi có hành vi vi phạm pháp luật.",
            "why": "Mọi hoạt động trên không gian mạng đều lưu trữ địa chỉ IP và nhật ký truyền thông; cơ quan an ninh mạng hoàn toàn có thể truy vết chính xác thủ phạm."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Thiết kế trang web với HTML và CSS",
        "description": "Ngôn ngữ HTML: cấu trúc thẻ, định dạng văn bản, hình ảnh, bảng, siêu liên kết, biểu mẫu form; Ngôn ngữ định dạng CSS: bộ chọn, màu sắc, phông chữ, mô hình hộp (box model) và bố cục trang web.",
        "lessons": [
          { "id": "l01", "title": "Bài 7: HTML và cấu trúc trang web", "hasRealContent": true },
          { "id": "l02", "title": "Bài 8: Định dạng văn bản", "hasRealContent": true },
          { "id": "l03", "title": "Bài 9: Tạo danh sách, bảng", "hasRealContent": true },
          { "id": "l04", "title": "Bài 10: Tạo liên kết", "hasRealContent": true },
          { "id": "l05", "title": "Bài 11: Chèn tệp tin đa phương tiện và khung nội tuyến", "hasRealContent": true },
          { "id": "l06", "title": "Bài 12: Tạo biểu mẫu", "hasRealContent": true },
          { "id": "l07", "title": "Bài 13: Khái niệm, vai trò của CSS", "hasRealContent": true },
          { "id": "l08", "title": "Bài 14: Định dạng văn bản bằng CSS", "hasRealContent": true },
          { "id": "l09", "title": "Bài 15: Tạo màu cho chữ và nền", "hasRealContent": true },
          { "id": "l10", "title": "Bài 16: Định dạng khung", "hasRealContent": true },
          { "id": "l11", "title": "Bài 17: Các mức ưu tiên của bộ chọn", "hasRealContent": true },
          { "id": "l12", "title": "Bài 18: Thực hành tổng hợp thiết kế trang web", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "HTML (HyperText Markup Language)",
            "definition": "Là ngôn ngữ đánh dấu siêu văn bản định nghĩa cấu trúc cơ bản của trang web bằng các thẻ (tags) lồng nhau. Cấu trúc chuẩn gồm: <!DOCTYPE html>, <html>, <head> (chứa tiêu đề và metadata) và <body> (chứa nội dung hiển thị).",
            "example": "<h1>Tiêu đề chính</h1>, <p>Đoạn văn</p>, <a href='https://example.com'>Liên kết</a>, <img src='logo.png' alt='Logo'>.",
            "essence": "HTML là khung xương chịu lực quy định nội dung của trang web."
          },
          {
            "term": "CSS và Mô hình hộp (CSS Box Model)",
            "definition": "CSS (Cascading Style Sheets) quy định cách hiển thị trực quan thẩm mĩ của các phần tử HTML. Mô hình hộp gồm 4 lớp từ trong ra ngoài: Nội dung (Content) -> Đệm (Padding) -> Viền (Border) -> Lề ngoài (Margin).",
            "example": "p { padding: 10px; border: 1px solid #ccc; margin: 15px; }.",
            "essence": "Tách bạch nội dung (HTML) khỏi phần trình bày trang trí giao diện (CSS) giúp dễ bảo trì và tối ưu trải nghiệm người dùng."
          }
        ],
        "rules": [
          {
            "statement": "Độ ưu tiên của bộ chọn CSS (Specificity)",
            "meaning": "Khi có nhiều luật CSS xung đột áp dụng cho cùng một phần tử, độ ưu tiên tăng dần theo thứ tự: Bộ chọn thẻ (Type selector) < Bộ chọn lớp (Class selector .class) < Bộ chọn mã định danh (ID selector #id) < Kiểu nội dòng (Inline style). Thuộc tính có !important sẽ ghi đè tất cả.",
            "example": "<div id='main' class='box' style='color: green;'>: Màu xanh lá cây của style nội dòng sẽ được áp dụng thay vì CSS external.",
            "essence": "Hệ thống phân cấp chặt chẽ đảm bảo giải quyết mọi mâu thuẫn phong cách định dạng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Viết mã HTML tạo một bảng thông tin gồm 2 cột: 'Môn học' và 'Điểm số', gồm 2 dòng dữ liệu cho Toán (9.5) và Tin học (10.0).",
            "steps": [
              "Bước 1: Sử dụng thẻ <table> để mở bảng.",
              "Bước 2: Tạo hàng tiêu đề bằng thẻ <tr> và các ô tiêu đề <th>.",
              "Bước 3: Tạo các hàng dữ liệu tiếp theo bằng <tr> và các ô nội dung <td>.",
              "Bước 4: Đóng các thẻ theo đúng thứ tự."
            ],
            "answer": "<table border='1'><tr><th>Môn học</th><th>Điểm số</th></tr><tr><td>Toán</td><td>9.5</td></tr><tr><td>Tin học</td><td>10.0</td></tr></table>"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên thẻ đóng hoặc đóng sai thứ tự các cặp thẻ lồng nhau trong HTML (ví dụ: <b><i>Nội dung</b></i>).",
            "why": "Các thẻ phải tuân thủ nguyên tắc lồng nhau: thẻ nào mở sau cùng thì phải đóng trước tiên (<b><i>Nội dung</i></b>)."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chủ đề 5: Hướng nghiệp với Tin học",
        "description": "Các ngành nghề trong lĩnh vực Công nghệ thông tin, nhóm nghề bảo trì phần cứng và dịch vụ mạng, nhóm nghề quản trị hệ thống và cơ sở dữ liệu, yêu cầu năng lực và lộ trình phát triển bản thân.",
        "lessons": [
          { "id": "l01", "title": "Bài 19: Dịch vụ sửa chữa và bảo trì máy tính", "hasRealContent": true },
          { "id": "l02", "title": "Bài 20: Nhóm nghề quản trị trong ngành Công nghệ thông tin", "hasRealContent": true },
          { "id": "l03", "title": "Bài 21: Hội thảo hướng nghiệp", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Nghề Quản trị hệ thống (System Administrator - SysAdmin)",
            "definition": "Là người chịu trách nhiệm cài đặt, cấu hình, duy trì hoạt động ổn định và bảo mật cho toàn bộ hệ thống máy chủ, mạng và máy trạm của một tổ chức hoặc doanh nghiệp.",
            "example": "Quản trị viên cấu hình máy chủ Windows Server/Linux, thiết lập chính sách sao lưu dữ liệu tự động hàng ngày.",
            "essence": "Đảm bảo tính sẵn sàng cao và an toàn vận hành 24/7 cho hạ tầng công nghệ."
          },
          {
            "term": "Nghề Quản trị cơ sở dữ liệu (Database Administrator - DBA)",
            "definition": "Chuyên gia thiết kế, quản lý, tối ưu hóa truy vấn và bảo mật cơ sở dữ liệu (SQL Server, Oracle, PostgreSQL, MySQL) nhằm phục vụ các ứng dụng kinh doanh.",
            "example": "Tối ưu hóa bảng chỉ mục (index) để truy vấn hàng triệu đơn hàng trong vài mili-giây trên sàn thương mại điện tử.",
            "essence": "Bảo vệ tài sản dữ liệu cốt lõi và tối đa hóa hiệu năng truy xuất thông tin của doanh nghiệp."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc phát triển nghề nghiệp trong ngành CNTT",
            "meaning": "Ngành CNTT biến đổi cực nhanh; người lao động cần sở hữu nền tảng khoa học máy tính vững chắc (thuật toán, cấu trúc dữ liệu, mạng), năng lực tự học suốt đời, khả năng thích ứng với công nghệ mới và trình độ tiếng Anh chuyên ngành tốt.",
            "example": "Kỹ sư phần mềm liên tục cập nhật công nghệ điện toán đám mây và AI để không bị tụt hậu.",
            "essence": "Năng lực tự học và tư duy giải quyết vấn đề là chìa khóa then chốt cho sự thành công bền vững."
          }
        ],
        "workedExamples": [
          {
            "prompt": "So sánh điểm khác biệt then chốt giữa nhóm nghề Dịch vụ sửa chữa phần cứng và nhóm nghề Quản trị mạng?",
            "steps": [
              "Bước 1: Đối tượng làm việc: Nghề sửa chữa tập trung vào các linh kiện vật lý (mainboard, RAM, nguồn, ổ cứng, màn hình); Nghề quản trị mạng tập trung vào luồng dữ liệu, giao thức, bảo mật và thiết bị mạng (Router, Firewall, Switch).",
              "Bước 2: Mục tiêu: Nghề sửa chữa khắc phục sự cố hỏng hóc cơ học/điện tử của thiết bị đơn lẻ; Nghề quản trị mạng đảm bảo tính thông suốt và an toàn thông tin của cả hệ sinh thái kết nối.",
              "Bước 3: Kỹ năng: Sửa chữa đòi hỏi kỹ năng hàn, đo điện, chẩn đoán lỗi phần cứng; Quản trị mạng đòi hỏi tư duy hệ thống, hiểu biết giao thức mạng và kỹ năng cấu hình phần mềm."
            ],
            "answer": "Sửa chữa xử lý thiết bị phần cứng cụ thể; Quản trị mạng điều phối toàn bộ hệ thống kết nối và an toàn dữ liệu."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng học ngành CNTT chỉ đơn thuần là học lập trình phần mềm (Coding).",
            "why": "CNTT là lĩnh vực rộng lớn bao gồm quản trị mạng, an ninh mạng, phân tích dữ liệu, thiết kế trải nghiệm người dùng, quản trị hệ thống và kinh doanh số."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chủ đề 6: Thiết bị mạng và Thiết kế mạng máy tính",
        "description": "Đặc tính kỹ thuật chuyên sâu của thiết bị mạng, các loại môi trường truyền dẫn (cáp xoắn đôi Cat6, cáp quang, sóng vô tuyến WiFi), quy trình thiết kế và phác thảo sơ đồ mạng LAN trường học và văn phòng.",
        "lessons": [
          { "id": "l01", "title": "Bài 22: Tìm hiểu thiết bị mạng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 23: Đường truyền mạng và ứng dụng", "hasRealContent": true },
          { "id": "l03", "title": "Bài 24: Sơ bộ về thiết kế mạng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Cáp quang (Fiber Optic Cable)",
            "definition": "Đường truyền truyền dẫn tín hiệu bằng xung ánh sáng qua sợi thủy tinh hoặc nhựa trong suốt dựa trên hiện tượng phản xạ toàn phần. Ưu điểm: băng thông siêu lớn, cự ly truyền xa hàng chục km và hoàn toàn không bị nhiễu điện từ.",
            "example": "Tuyến cáp quang biển kết nối mạng Internet giữa Việt Nam và quốc tế.",
            "essence": "Môi trường truyền dẫn tốc độ cao là xương sống của hạ tầng viễn thông hiện đại."
          },
          {
            "term": "Cấu trúc liên kết mạng (Network Topology)",
            "definition": "Cách bố trí hình học các máy tính và thiết bị kết nối trong mạng LAN. Các dạng phổ biến: Hình sao (Star - dùng Switch trung tâm), Hình vòng (Ring), Dạng trục (Bus) và Dạng lưới (Mesh).",
            "example": "Mạng LAN hình sao là tiêu chuẩn thống trị hiện nay vì một máy bị đứt dây cáp không làm ảnh hưởng đến các máy còn lại.",
            "essence": "Lựa chọn cấu trúc liên kết quyết định độ tin cậy, chi phí lắp đặt và khả năng mở rộng của hệ thống mạng."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc thiết kế mạng LAN phân tầng (Hierarchical Network Model)",
            "meaning": "Một mạng doanh nghiệp đạt chuẩn nên phân chia làm 3 tầng chức năng: Tầng lõi (Core layer - chuyển mạch siêu tốc), Tầng phân phối (Distribution layer - định tuyến và kiểm soát bảo mật) và Tầng truy cập (Access layer - kết nối trực tiếp máy người dùng).",
            "example": "Tầng truy cập đặt các Switch kết nối máy tính học sinh; Tầng phân phối kết nối các khối nhà; Tầng lõi đặt tại phòng trung tâm dữ liệu nhà trường.",
            "essence": "Phân tầng giúp dễ quản lý, dễ khoanh vùng sự cố và mở rộng mạng linh hoạt."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Lập kế hoạch thiết kế mạng LAN cho phòng học Tin học gồm 40 máy tính học sinh và 1 máy giáo viên. Hãy chọn thiết bị kết nối và cấu trúc liên kết tối ưu nhất?",
            "steps": [
              "Bước 1: Chọn cấu trúc liên kết: Cấu trúc hình sao (Star Topology) vì tính ổn định cao và dễ phát hiện lỗi đứt cáp.",
              "Bước 2: Chọn thiết bị chuyển mạch: Sử dụng 1 Switch 48 cổng Gigabit (hoặc 2 Switch 24 cổng xếp tầng) có hỗ trợ tốc độ 1000 Mbps.",
              "Bước 3: Chọn môi trường truyền: Cáp mạng xoắn đôi Cat6 chuẩn kết nối RJ-45 (chiều dài mỗi đoạn dây không quá 100m).",
              "Bước 4: Cấu hình: Cài đặt cấp phát địa chỉ IP tự động (DHCP) cùng dải mạng 192.168.10.x để các máy dễ dàng chia sẻ bài giảng."
            ],
            "answer": "Giải pháp tối ưu: Mô hình hình sao sử dụng Switch 48 port Gigabit và cáp mạng Cat6 kết nối về phòng điều khiển trung tâm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Bố trí chiều dài dây cáp mạng xoắn đôi (UTP) vượt quá giới hạn 100 mét mà không có thiết bị khuếch đại lặp (Repeater/Switch).",
            "why": "Tín hiệu điện bị suy hao và biến dạng nghiêm trọng sau cự ly 100m, dẫn đến mất kết nối hoặc tốc độ truyền chập chờn."
          }
        ]
      },
      {
        "id": "ch07",
        "title": "Chủ đề 7: Học máy, Khoa học dữ liệu và Mô phỏng",
        "description": "Làm quen với Học máy (Machine Learning), các bước cơ bản trong Khoa học dữ liệu (Data Science), kỹ thuật trích xuất thông tin từ dữ liệu lớn, mô phỏng giải quyết vấn đề và ứng dụng mô phỏng số trong giáo dục và nghiên cứu.",
        "lessons": [
          { "id": "l01", "title": "Bài 25: Làm quen với Học máy", "hasRealContent": true },
          { "id": "l02", "title": "Bài 26: Làm quen với Khoa học dữ liệu", "hasRealContent": true },
          { "id": "l03", "title": "Bài 27: Máy tính và Khoa học dữ liệu", "hasRealContent": true },
          { "id": "l04", "title": "Bài 28: Thực hành trải nghiệm trích rút thông tin và tri thức", "hasRealContent": true },
          { "id": "l05", "title": "Bài 29: Mô phỏng trong giải quyết vấn đề", "hasRealContent": true },
          { "id": "l06", "title": "Bài 30: Ứng dụng mô phỏng trong giáo dục", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Học máy (Machine Learning) và Các dạng học máy",
            "definition": "Là nhánh của AI cho phép máy tính tự học hỏi và nâng cao hiệu năng thực hiện nhiệm vụ từ dữ liệu mà không cần lập trình tường minh từng quy tắc. Gồm 3 nhóm chính: Học có giám sát (Supervised), Học không giám sát (Unsupervised) và Học tăng cường (Reinforcement Learning).",
            "example": "Học có giám sát: Huấn luyện mô hình nhận diện ảnh chó/mèo bằng hàng vạn bức ảnh đã được dán nhãn sẵn trước đó.",
            "essence": "Tìm kiếm các hàm số xấp xỉ mô phỏng mối tương quan phức tạp ẩn giấu trong tập dữ liệu mẫu lớn."
          },
          {
            "term": "Mô phỏng máy tính (Computer Simulation)",
            "definition": "Là việc sử dụng chương trình máy tính để mô phỏng hành vi của một hệ thống thực tế hoặc hệ thống giả định theo thời gian bằng các mô hình toán học và vật lý.",
            "example": "Mô phỏng đường đi của bão nhiệt đới; mô phỏng va chạm ô tô thử nghiệm độ an toàn túi khí mà không cần phá hủy xe thật.",
            "essence": "Giúp con người nghiên cứu những hiện tượng quá nguy hiểm, quá tốn kém hoặc diễn ra quá nhanh/quá chậm trong thực tế."
          }
        ],
        "rules": [
          {
            "statement": "Quy trình chuẩn trong Khoa học dữ liệu",
            "meaning": "Gồm 5 bước tuần hoàn: (1) Xác định bài toán mục tiêu -> (2) Thu thập dữ liệu -> (3) Làm sạch và tiền xử lý dữ liệu -> (4) Khám phá và xây dựng mô hình phân tích -> (5) Trực quan hóa và diễn giải kết quả hỗ trợ ra quyết định.",
            "example": "Phân tích xu hướng học tập của học sinh dựa trên dữ liệu làm bài kiểm tra trực tuyến để đề xuất lộ trình ôn tập cá nhân hóa.",
            "essence": "Dữ liệu chất lượng (Garbage In - Garbage Out): khâu làm sạch và tiền xử lý quyết định đến 80% thành công của mô hình phân tích."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một trường học muốn áp dụng Học máy để dự đoán nguy cơ học sinh bị hổng kiến thức môn Toán. Hãy đề xuất các bước thu thập dữ liệu và huấn luyện mô hình?",
            "steps": [
              "Bước 1: Thu thập dữ liệu quá khứ: Điểm kiểm tra định kỳ, thời gian tự học, số lượng câu trắc nghiệm làm sai theo từng chuyên đề của các khóa trước.",
              "Bước 2: Gán nhãn dữ liệu: Nhãn 1 (Cần phụ đạo/Hổng kiến thức), Nhãn 0 (Đạt chuẩn).",
              "Bước 3: Tiền xử lý dữ liệu: Loại bỏ giá trị khuyết thiếu, chuẩn hóa thang điểm về cùng thang đo [0; 1].",
              "Bước 4: Huấn luyện mô hình: Sử dụng thuật toán phân loại (như Decision Tree hoặc Logistic Regression) trên 80% tập dữ liệu huấn luyện.",
              "Bước 5: Đánh giá: Thử nghiệm trên 20% tập dữ liệu kiểm tra để đo độ chính xác (Accuracy, F1-score) trước khi đưa vào ứng dụng thực tế."
            ],
            "answer": "Quy trình gồm thu thập dữ liệu bài thi -> làm sạch và gán nhãn -> huấn luyện thuật toán phân loại -> đánh giá và tích hợp cảnh báo sớm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Hiện tượng Quá khớp (Overfitting) trong huấn luyện mô hình học máy.",
            "why": "Mô hình học thuộc lòng quá kỹ dữ liệu huấn luyện (độ chính xác 100%) nhưng dự đoán rất kém khi gặp dữ liệu thực tế mới lạ."
          }
        ]
      }
    ]
  }
}

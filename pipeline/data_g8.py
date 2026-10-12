# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa 8 môn học Lớp 8 SGK Kết nối tri thức với cuộc sống 2026-2027:
- Toán học (6 chương)
- Khoa học tự nhiên (6 chương)
- Ngữ văn (5 bài trọng tâm)
- Lịch sử & Địa lí (5 chương)
- Tiếng Anh (6 units)
- Tin học (4 chủ đề)
- Giáo dục công dân (4 bài)
- Công nghệ (4 chương)
"""

true = True
false = False
null = None

GRADE_08_SUBJECTS = {
  "toan": {
    "id": "toan",
    "name": "Toán học",
    "icon": "📐",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Đa thức nhiều biến",
        "description": "Đơn thức, đa thức nhiều biến, các phép tính cộng, trừ, nhân, chia đơn thức và đa thức nhiều biến.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đơn thức và đa thức nhiều biến", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các phép tính với đa thức nhiều biến", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Đơn thức thu gọn",
            "definition": "Là đơn thức chỉ gồm tích của một số với các biến, mà mỗi biến đã được nâng lên lũy thừa với số mũ nguyên dương và chỉ viết một lần.",
            "example": "-3x^2y^3z là đơn thức thu gọn; hệ số là -3, phần biến là x^2y^3z, bậc là 2 + 3 + 1 = 6.",
            "essence": "Thu gọn đơn thức giúp việc tính toán và so sánh hạng tử đồng dạng trở nên rõ ràng, chuẩn xác."
          },
          {
            "term": "Hai đơn thức đồng dạng",
            "definition": "Là hai đơn thức có hệ số khác 0 và có cùng phần biến.",
            "example": "2x^2y và -5x^2y là hai đơn thức đồng dạng; chúng có thể cộng trừ trực tiếp: 2x^2y - 5x^2y = -3x^2y.",
            "essence": "Chỉ những đơn thức đồng dạng mới có thể gộp chung lại với nhau bằng cách cộng trừ phần hệ số."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc nhân đơn thức với đa thức",
            "meaning": "Muốn nhân một đơn thức với một đa thức, ta nhân đơn thức đó với từng hạng tử của đa thức rồi cộng các tích với nhau: A(B + C) = AB + AC.",
            "example": "2x(x^2 - 3y) = 2x*x^2 - 2x*3y = 2x^3 - 6xy.",
            "essence": "Phép nhân phân phối trên phép cộng bảo toàn giá trị đại số của biểu thức."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rút gọn biểu thức: P = 3xy(x - 2y) - 2x(y^2 - 3xy).",
            "steps": [
              "Bước 1: Khai triển tích thứ nhất: 3xy*x - 3xy*2y = 3x^2y - 6xy^2.",
              "Bước 2: Khai triển tích thứ hai: -2x*y^2 - 2x*(-3xy) = -2xy^2 + 6x^2y.",
              "Bước 3: Nhóm các hạng tử đồng dạng: (3x^2y + 6x^2y) + (-6xy^2 - 2xy^2) = 9x^2y - 8xy^2."
            ],
            "answer": "P = 9x^2y - 8xy^2"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên đổi dấu khi nhân đơn thức có dấu trừ vào đa thức: ví dụ -2x*(y - 3) = -2xy - 6x.",
            "why": "-2x * (-3) phải bằng +6x; quy tắc nhân hai số âm cho ra số dương."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Hằng đẳng thức đáng nhớ và Ứng dụng",
        "description": "7 hằng đẳng thức đáng nhớ, phân tích đa thức thành nhân tử (đặt nhân tử chung, dùng hằng đẳng thức, nhóm hạng tử).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Bảy hằng đẳng thức đáng nhớ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phân tích đa thức thành nhân tử và ứng dụng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hiệu hai bình phương",
            "definition": "A^2 - B^2 = (A - B)(A + B). Hiệu hai bình phương của hai biểu thức bằng tích của hiệu với tổng của chúng.",
            "example": "x^2 - 9 = (x - 3)(x + 3); 101^2 - 1 = (101 - 1)(101 + 1) = 100 * 102 = 10200.",
            "essence": "Hằng đẳng thức giúp biến đổi hiệu thành tích, là công cụ then chốt để phân tích nhân tử và giải phương trình."
          }
        ],
        "rules": [
          {
            "statement": "Bình phương của một tổng và một hiệu",
            "meaning": "(A + B)^2 = A^2 + 2AB + B^2 và (A - B)^2 = A^2 - 2AB + B^2.",
            "example": "(2x + 3y)^2 = 4x^2 + 12xy + 9y^2.",
            "essence": "Luôn có số hạng kép 2AB ở giữa; thiếu 2AB là lỗi sai kinh điển nhất của học sinh."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích đa thức sau thành nhân tử: M = x^2 - 4y^2 + 4x + 4.",
            "steps": [
              "Bước 1: Nhóm các hạng tử tạo thành hằng đẳng thức: M = (x^2 + 4x + 4) - 4y^2.",
              "Bước 2: Biến đổi ngoặc thứ nhất: (x + 2)^2 - (2y)^2.",
              "Bước 3: Áp dụng hằng đẳng thức hiệu hai bình phương: M = (x + 2 - 2y)(x + 2 + 2y)."
            ],
            "answer": "M = (x - 2y + 2)(x + 2y + 2)"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Viết (A + B)^2 = A^2 + B^2 (quên số hạng 2AB).",
            "why": "(A + B)^2 = (A + B)(A + B) = A^2 + AB + BA + B^2 = A^2 + 2AB + B^2."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Tứ giác và Các tứ giác đặc biệt",
        "description": "Hình thang, hình thang cân, hình bình hành, hình chữ nhật, hình thoi, hình vuông và các dấu hiệu nhận biết.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tứ giác, hình thang cân và hình bình hành", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hình chữ nhật, hình thoi và hình vuông", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hình bình hành",
            "definition": "Là tứ giác có các cạnh đối song song. Trong hình bình hành: Các cạnh đối bằng nhau, các góc đối bằng nhau, hai đường chéo cắt nhau tại trung điểm của mỗi đường.",
            "example": "Tứ giác ABCD có AB // CD và AD // BC là hình bình hành.",
            "essence": "Hình bình hành có tâm đối xứng là giao điểm của hai đường chéo."
          },
          {
            "term": "Hình thoi",
            "definition": "Là tứ giác có bốn cạnh bằng nhau. Hai đường chéo của hình thoi vuông góc với nhau và là các đường phân giác của các góc của hình thoi.",
            "example": "Hình bình hành có hai cạnh kề bằng nhau (AB = BC) thì trở thành hình thoi.",
            "essence": "Hình thoi có hai trục đối xứng là hai đường chéo vuông góc."
          }
        ],
        "rules": [
          {
            "statement": "Dấu hiệu nhận biết hình vuông",
            "meaning": "Hình chữ nhật có hai cạnh kề bằng nhau (hoặc hai đường chéo vuông góc) là hình vuông. Hình thoi có một góc vuông (hoặc hai đường chéo bằng nhau) là hình vuông.",
            "example": "Hình vuông hội tụ đầy đủ tất cả các tính chất tuyệt vời của cả hình chữ nhật và hình thoi.",
            "essence": "Hình vuông là đỉnh cao của sự hoàn hảo và đối xứng trong hình học phẳng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho tam giác ABC vuông tại A, đường trung tuyến AM. Gọi D là điểm đối xứng với A qua M. Chứng minh tứ giác ABDC là hình chữ nhật.",
            "steps": [
              "Bước 1: Do M là trung điểm của BC (giả thiết) và M là trung điểm của AD (tính chất đối xứng) nên tứ giác ABDC có hai đường chéo cắt nhau tại trung điểm mỗi đường => ABDC là hình bình hành.",
              "Bước 2: Hình bình hành ABDC có góc BAC = 90 độ (tam giác ABC vuông tại A).",
              "Bước 3: Hình bình hành có một góc vuông là hình chữ nhật => ABDC là hình chữ nhật."
            ],
            "answer": "ABDC là hình chữ nhật."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Kết luận tứ giác là hình thoi khi chỉ biết hai đường chéo vuông góc với nhau.",
            "why": "Hai đường chéo vuông góc chỉ tạo thành hình thoi khi chúng CẮT NHAU TẠI TRUNG ĐIỂM của mỗi đường (tức là hình bình hành có hai đường chéo vuông góc)."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Định lí Thalès trong Tam giác",
        "description": "Đoạn thẳng tỉ lệ, định lí Thalès thuận và đảo, hệ quả của định lí Thalès và tính chất đường phân giác trong tam giác.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Định lí Thalès thuận, đảo và hệ quả", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tính chất đường phân giác của tam giác", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Định lí Thalès",
            "definition": "Nếu một đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn lại thì nó định ra trên hai cạnh đó những đoạn thẳng tương ứng tỉ lệ.",
            "example": "Trong tam giác ABC, nếu DE // BC (D thuộc AB, E thuộc AC) thì AD/AB = AE/AC và AD/DB = AE/EC.",
            "essence": "Song song chuyển hóa thành tỉ lệ thức độ dài giữa các đoạn thẳng."
          }
        ],
        "rules": [
          {
            "statement": "Tính chất đường phân giác trong tam giác",
            "meaning": "Trong tam giác, đường phân giác của một góc chia cạnh đối diện thành hai đoạn thẳng tỉ lệ với hai cạnh kề hai đoạn ấy: DB / DC = AB / AC.",
            "example": "Tam giác ABC có AD là phân giác góc A. Nếu AB = 4 cm, AC = 6 cm thì DB / DC = 4 / 6 = 2/3.",
            "essence": "Tỉ lệ góc chia đôi tạo ra tỉ lệ cạnh tương ứng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho tam giác ABC có AB = 6 cm, AC = 9 cm. Phân giác AD cắt BC tại D. Biết BD = 3 cm, tính độ dài đoạn thẳng DC và BC.",
            "steps": [
              "Bước 1: Áp dụng tính chất đường phân giác: DB / DC = AB / AC.",
              "Bước 2: Thay số: 3 / DC = 6 / 9 = 2 / 3 => DC = (3 * 3) / 2 = 4,5 cm.",
              "Bước 3: Tính BC = BD + DC = 3 + 4,5 = 7,5 cm."
            ],
            "answer": "DC = 4,5 cm; BC = 7,5 cm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lập sai tỉ số cạnh: Viết DB/DC = AC/AB thay vì AB/AC.",
            "why": "Đoạn nào kề với cạnh nào thì phải tương ứng: DB kề với AB, DC kề với AC nên DB/DC = AB/AC."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Phân thức đại số",
        "description": "Định nghĩa phân thức đại số, tính chất cơ bản, rút gọn phân thức và các phép toán cộng, trừ, nhân, chia phân thức.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái niệm và tính chất cơ bản của phân thức đại số", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các phép toán cộng, trừ, nhân, chia phân thức đại số", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Phân thức đại số",
            "definition": "Là một biểu thức có dạng A/B, trong đó A và B là những đa thức và B là đa thức khác đa thức 0. A gọi là tử thức, B gọi là mẫu thức.",
            "example": "(2x + 1) / (x - 3) là một phân thức đại số với điều kiện xác định x khác 3.",
            "essence": "Phân thức đại số là sự mở rộng của khái niệm phân số sang các biểu thức chứa biến."
          }
        ],
        "rules": [
          {
            "statement": "Điều kiện xác định của phân thức đại số",
            "meaning": "Phân thức A/B chỉ có nghĩa (xác định) khi mẫu thức B khác 0: B != 0.",
            "example": "Phân thức 1 / (x^2 - 4) xác định khi x^2 - 4 != 0 <=> x != 2 và x != -2.",
            "essence": "Phép chia cho 0 là không xác định trong toán học; mẫu thức triệt tiêu làm biểu thức vô nghĩa."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rút gọn phân thức: Q = (x^2 - 9) / (2x + 6).",
            "steps": [
              "Bước 1: Tìm điều kiện xác định: 2x + 6 != 0 <=> x != -3.",
              "Bước 2: Phân tích tử thức thành nhân tử: x^2 - 9 = (x - 3)(x + 3).",
              "Bước 3: Phân tích mẫu thức: 2x + 6 = 2(x + 3).",
              "Bước 4: Chia cả tử và mẫu cho nhân tử chung (x + 3): Q = (x - 3) / 2."
            ],
            "answer": "Q = (x - 3) / 2 với x != -3."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Rút gọn phân thức mà quên tìm điều kiện xác định của mẫu thức.",
            "why": "Việc rút gọn làm mất nhân tử ở mẫu có thể dẫn đến việc nhận nhầm các giá trị làm mẫu bằng 0 là nghiệm hợp lệ."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Tam giác đồng dạng",
        "description": "Hai tam giác đồng dạng, các trường hợp đồng dạng c-c-c, c-g-c, g-g và các trường hợp đồng dạng của tam giác vuông.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Định nghĩa hai tam giác đồng dạng và trường hợp c-c-c, c-g-c", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Trường hợp đồng dạng g-g và tam giác vuông đồng dạng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hai tam giác đồng dạng",
            "definition": "Tam giác A'B'C' gọi là đồng dạng với tam giác ABC nếu: Các góc tương ứng bằng nhau (A'=A, B'=B, C'=C) và các cạnh tương ứng tỉ lệ: A'B'/AB = B'C'/BC = C'A'/CA = k (k là tỉ số đồng dạng).",
            "example": "Một bức ảnh thu nhỏ tỉ lệ 1:2 có hình dạng giống hệt cảnh vật thực tế nhưng kích thước bằng một nửa.",
            "essence": "Đồng dạng là sự bảo toàn về hình dạng góc mà không nhất thiết phải bằng nhau về kích thước độ dài."
          }
        ],
        "rules": [
          {
            "statement": "Trường hợp đồng dạng góc - góc (g-g)",
            "meaning": "Nếu hai góc của tam giác này lần lượt bằng hai góc của tam giác kia thì hai tam giác đó đồng dạng với nhau.",
            "example": "Tam giác ABC và tam giác A'B'C' có góc A = góc A' và góc B = góc B' => tam giác A'B'C' đồng dạng với tam giác ABC.",
            "essence": "Đây là trường hợp đồng dạng phổ biến và dễ chứng minh nhất trong hình học THCS."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một cái cây cao đổ bóng dài 8m trên mặt đất. Cùng thời điểm đó, một cọc tiêu cao 2m cắm thẳng đứng đổ bóng dài 1,6m. Tính chiều cao của cây.",
            "steps": [
              "Bước 1: Do các tia nắng mặt trời song song nên góc tạo bởi tia nắng với mặt đất là như nhau.",
              "Bước 2: Hai tam giác vuông tạo bởi (cây, bóng cây) và (cọc, bóng cọc) đồng dạng theo trường hợp g-g.",
              "Bước 3: Lập tỉ số đồng dạng: h_cây / h_cọc = bóng_cây / bóng_cọc => h_cây / 2 = 8 / 1,6 => h_cây = (8 * 2) / 1,6 = 10m."
            ],
            "answer": "Chiều cao của cây là 10 mét."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Viết sai thứ tự đỉnh tương ứng khi kí hiệu hai tam giác đồng dạng.",
            "why": "Kí hiệu tam giác A'B'C' đồng dạng với tam giác ABC đòi hỏi đỉnh A' tương ứng với A, B' với B, C' với C. Nếu viết lộn xộn sẽ dẫn đến việc lập sai các tỉ số cạnh."
          }
        ]
      }
    ]
  },

  "khoa-hoc-tu-nhien": {
    "id": "khoa-hoc-tu-nhien",
    "name": "Khoa học Tự nhiên",
    "icon": "🔬",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Phản ứng hóa học và Biến đổi chất",
        "description": "Biến đổi vật lí và biến đổi hóa học, phản ứng hóa học, định luật bảo toàn khối lượng và phương trình hóa học.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phản ứng hóa học và năng lượng trong phản ứng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Định luật bảo toàn khối lượng và phương trình hóa học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Phản ứng hóa học",
            "definition": "Là quá trình biến đổi từ chất này thành chất khác, trong đó liên kết giữa các nguyên tử bị phá vỡ và liên kết mới được hình thành.",
            "example": "Đốt cháy than (Carbon) trong không khí tạo thành khí Carbon dioxide: C + O2 -> CO2 (kèm tỏa nhiều nhiệt).",
            "essence": "Bản chất của phản ứng hóa học là sự sắp xếp lại trật tự liên kết giữa các nguyên tử, số lượng nguyên tử mỗi loại được bảo toàn."
          }
        ],
        "rules": [
          {
            "statement": "Định luật bảo toàn khối lượng (Lomonosov - Lavoisier)",
            "meaning": "Trong một phản ứng hóa học, tổng khối lượng của các chất sản phẩm bằng tổng khối lượng của các chất tham gia phản ứng: m_tham_gia = m_san_pham.",
            "example": "Nung 100g đá vôi (CaCO3) thu được 56g vôi sống (CaO) và 44g khí CO2: 56 + 44 = 100g.",
            "essence": "Nguyên tử không tự sinh ra và cũng không tự mất đi, chúng chỉ chuyển hóa từ dạng liên kết này sang dạng liên kết khác."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Đốt cháy hoàn toàn 6g kim loại Magnesium (Mg) trong khí Oxygen (O2) thu được 10g hợp chất Magnesium oxide (MgO). Tính khối lượng khí Oxygen đã tham gia phản ứng.",
            "steps": [
              "Bước 1: Viết sơ đồ phản ứng: Magnesium + Oxygen -> Magnesium oxide.",
              "Bước 2: Áp dụng định luật bảo toàn khối lượng: m_Mg + m_O2 = m_MgO.",
              "Bước 3: Thay số: 6 + m_O2 = 10 => m_O2 = 10 - 6 = 4 gam."
            ],
            "answer": "Khối lượng khí Oxygen tham gia phản ứng là 4 gam."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng đốt cháy một thanh củi thành nắm tro tàn nhỏ làm khối lượng bị hao hụt vi phạm định luật bảo toàn.",
            "why": "Vì phần lớn khối lượng củi đã biến thành khí CO2 và hơi nước bay vào không khí; nếu cân cả lượng khí bay đi thì tổng khối lượng hoàn toàn bảo toàn."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Một số Hợp chất vô cơ thông dụng",
        "description": "Khái niệm và tính chất hóa học của Acid, Base, Oxide và Muối; thang pH và bảo vệ môi trường đất, nước.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Acid và Base — Thang pH đo độ chua kiềm", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Oxide và Muối — Phản ứng trao đổi", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thang đo pH",
            "definition": "Là chỉ số đo độ acid hoặc base của một dung dịch trong khoảng từ 0 đến 14: pH < 7 là môi trường acid, pH = 7 là trung tính, pH > 7 là môi trường base.",
            "example": "Nước chanh có pH khoảng 2-3 (axit mạnh), nước cất có pH = 7 (trung tính), xà phòng có pH khoảng 9-10 (kiềm).",
            "essence": "pH quyết định sự tồn tại của các sinh vật và ảnh hưởng trực tiếp đến khả năng hấp thụ dinh dưỡng của rễ cây."
          }
        ],
        "rules": [
          {
            "statement": "Tác dụng của Acid lên chất chỉ thị màu",
            "meaning": "Dung dịch acid làm quỳ tím chuyển sang màu đỏ. Dung dịch base (kiềm) làm quỳ tím chuyển sang màu xanh và làm dung dịch phenolphthalein không màu hóa hồng.",
            "example": "Nhỏ một giọt giấm ăn (chứa acetic acid) lên giấy quỳ tím, quỳ tím lập tức đổi sang màu hồng đỏ.",
            "essence": "Chất chỉ thị màu là công cụ nhanh nhất giúp nhận biết tính chất acid - base mà không cần nếm thử nguy hiểm."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Khi đất trồng trọt bị chua (đất phèn có pH < 5), người nông dân thường bón chất gì để khử chua cải tạo đất? Giải thích.",
            "steps": [
              "Bước 1: Đất chua là đất có nồng độ ion H+ cao (tính acid).",
              "Bước 2: Người nông dân rắc vôi bột (chứa CaO hoặc Ca(OH)2 là chất có tính base) lên mặt ruộng.",
              "Bước 3: Phản ứng trung hòa diễn ra: Base tác dụng với acid trong đất nâng độ pH lên mức 6 - 6,5 thích hợp cho cây trồng phát triển."
            ],
            "answer": "Bón vôi bột (CaO) để trung hòa acid và nâng độ pH của đất."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đổ trực tiếp nước vào cốc chứa axit đặc để pha loãng axit sunfuric (H2SO4).",
            "why": "Cực kỳ nguy hiểm! Axit đặc hút nước tỏa nhiệt mãnh liệt làm nước sôi đột ngột bắn tung tóe axit gây bỏng nặng. Quy tắc đúng: Rót từ từ AXIT VÀO NƯỚC."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Khối lượng riêng và Áp suất",
        "description": "Khái niệm khối lượng riêng D = m/V, áp lực, áp suất p = F/S, áp suất chất lỏng và lực đẩy Archimedes.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khối lượng riêng và phương pháp đo khối lượng riêng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Áp suất, áp suất chất lỏng và lực đẩy Archimedes", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Lực đẩy Archimedes",
            "definition": "Một vật nhúng trong chất lỏng bị chất lỏng tác dụng một lực đẩy hướng thẳng đứng từ dưới lên trên, có độ lớn bằng trọng lượng của phần chất lỏng bị vật chiếm chỗ: F_A = d * V.",
            "example": "Một khúc gỗ nổi trên mặt nước hay tàu thủy bằng thép chở hàng vạn tấn nổi được trên biển nhờ lực đẩy Archimedes cân bằng với trọng lượng tàu.",
            "essence": "Vật chìm hay nổi phụ thuộc vào sự so sánh giữa khối lượng riêng của vật và khối lượng riêng của chất lỏng."
          }
        ],
        "rules": [
          {
            "statement": "Công thức tính áp suất cơ học",
            "meaning": "Áp suất là độ lớn của áp lực trên một đơn vị diện tích bị ép: p = F / S. Muốn tăng áp suất, ta tăng lực F hoặc giảm diện tích S.",
            "example": "Lưỡi dao được mài thật sắc (giảm diện tích tiếp xúc S) để tạo áp suất lớn giúp cắt thái dễ dàng.",
            "essence": "Áp suất đặc trưng cho tác dụng gây biến dạng của lực lên bề mặt tiếp xúc."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một khối sắt có thể tích 0,002 m3 được nhúng chìm hoàn toàn trong nước. Cho trọng lượng riêng của nước là d = 10.000 N/m3. Tính lực đẩy Archimedes tác dụng lên khối sắt.",
            "steps": [
              "Bước 1: Do vật chìm hoàn toàn nên thể tích phần chất lỏng bị chiếm chỗ chính bằng thể tích vật: V = 0,002 m3.",
              "Bước 2: Áp dụng công thức lực đẩy Archimedes: F_A = d * V.",
              "Bước 3: Thay số: F_A = 10.000 * 0,002 = 20 N."
            ],
            "answer": "Lực đẩy Archimedes là 20 Newton."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy thể tích của toàn bộ vật nhân với d khi vật chỉ chìm một phần trong nước.",
            "why": "Lực đẩy Archimedes chỉ tính trên THỂ TÍCH PHẦN VẬT CHÌM TRONG CHẤT LỎNG (phần chiếm chỗ), không tính phần nổi trên không khí."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Tác dụng làm quay của lực và Đòn bẩy",
        "description": "Mômen lực, tác dụng làm quay của lực quanh một trục cố định, các loại đòn bẩy và ứng dụng trong đời sống.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Mômen lực và tác dụng làm quay", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Đòn bẩy và ứng dụng của đòn bẩy trong thực tiễn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Mômen lực (Moment of force)",
            "definition": "Là đại lượng đặc trưng cho tác dụng làm quay của lực quanh một trục hoặc điểm tựa cố định, phụ thuộc vào độ lớn của lực và khoảng cách từ trục quay đến giá của lực (cánh tay đòn).",
            "example": "Dùng cờ-lê có cán dài để vặn ốc chặt: Cán càng dài (cánh tay đòn lớn) thì vặn ốc càng nhẹ nhàng.",
            "essence": "Lực tác dụng càng xa trục quay thì hiệu quả làm quay càng lớn."
          }
        ],
        "rules": [
          {
            "statement": "Điều kiện cân bằng của đòn bẩy",
            "meaning": "Đòn bẩy ở trạng thái cân bằng khi tích của lực tác dụng F1 với cánh tay đòn d1 bằng tích của tải trọng F2 với cánh tay đòn d2: F1 * d1 = F2 * d2.",
            "example": "Hai bạn chơi bập bênh: Bạn nhẹ cân hơn phải ngồi xa điểm tựa hơn bạn nặng cân để bập bênh thăng bằng.",
            "essence": "Được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Người ta dùng một chiếc đòn bẩy có điểm tựa O để bẩy một tảng đá có trọng lượng 1.200 N. Khoảng cách từ điểm tựa đến tảng đá là d2 = 0,2m. Khoảng cách từ điểm tựa đến điểm tác dụng lực là d1 = 1,2m. Tính lực F1 tối thiểu cần tác dụng.",
            "steps": [
              "Bước 1: Áp dụng điều kiện cân bằng đòn bẩy: F1 * d1 = F2 * d2.",
              "Bước 2: Rút ra công thức: F1 = (F2 * d2) / d1.",
              "Bước 3: Thay số: F1 = (1.200 * 0,2) / 1,2 = 240 / 1,2 = 200 N."
            ],
            "answer": "Lực tối thiểu cần tác dụng là 200 Newton (giảm được lực 6 lần)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đo cánh tay đòn theo đường xiên thay vì khoảng cách vuông góc từ trục quay đến đường tác dụng của lực.",
            "why": "Cánh tay đòn d bắt buộc phải là đoạn thẳng VUÔNG GÓC kẻ từ trục quay đến đường thẳng chứa vectơ lực."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Điện và Nhiệt",
        "description": "Nhiệt năng, các hình thức truyền nhiệt (dẫn nhiệt, đối lưu, bức xạ nhiệt), dòng điện, mạch điện và tác dụng của dòng điện.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Nhiệt năng và các hình thức truyền nhiệt", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Mạch điện cơ bản và các tác dụng của dòng điện", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bức xạ nhiệt",
            "definition": "Là hình thức truyền nhiệt bằng các tia nhiệt đi thẳng, có thể xảy ra ngay cả trong môi trường chân không.",
            "example": "Năng lượng nhiệt từ Mặt Trời truyền qua không gian vũ trụ đến sưởi ấm Trái Đất hoàn toàn bằng bức xạ nhiệt.",
            "essence": "Mọi vật thể có nhiệt độ trên 0 độ tuyệt đối đều liên tục phát ra bức xạ nhiệt ra môi trường xung quanh."
          }
        ],
        "rules": [
          {
            "statement": "Chiều quy ước của dòng điện trong mạch",
            "meaning": "Chiều dòng điện là chiều từ cực dương qua dây dẫn và các thiết bị điện tới cực âm của nguồn điện.",
            "example": "Trong mạch điện kín, electron tự do chuyển động từ cực âm sang cực dương, tức là ngược chiều quy ước của dòng điện.",
            "essence": "Quy ước chiều dòng điện được thiết lập trước khi các nhà khoa học phát hiện ra hạt electron."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao các xoong nồi nấu thức ăn thường làm bằng kim loại (nhôm, inox), còn quai xoong lại bọc bằng nhựa hoặc gỗ?",
            "steps": [
              "Bước 1: Đáy và thân xoong cần dẫn nhiệt nhanh để truyền nhiệt từ bếp vào làm chín thức ăn nên làm bằng kim loại dẫn nhiệt tốt.",
              "Bước 2: Quai xoong là nơi người dùng cầm nắm di chuyển nên cần cách nhiệt để tránh bị bỏng.",
              "Bước 3: Nhựa và gỗ là các chất dẫn nhiệt kém nên giữ cho tay cầm luôn mát an toàn."
            ],
            "answer": "Kim loại dẫn nhiệt tốt để nấu chín thức ăn; nhựa/gỗ cách nhiệt tốt bảo vệ tay người nấu."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng dòng điện chuyển động từ cực âm sang cực dương.",
            "why": "Dòng electron chuyển động từ âm sang dương, nhưng CHIỀU QUY ƯỚC CỦA DÒNG ĐIỆN là từ cực DƯƠNG sang cực ÂM."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Sinh học Cơ thể người và Sức khỏe",
        "description": "Cấu tạo và chức năng của các hệ cơ quan trong cơ thể người (hệ tuần hoàn, hệ hô hấp, hệ tiêu hóa, hệ thần kinh) và vệ sinh phòng bệnh học đường.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Hệ tuần hoàn và bảo vệ sức khỏe tim mạch", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hệ tiêu hóa, hô hấp và lối sống lành mạnh", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Kháng thể và Miễn dịch (Antibodies & Immunity)",
            "definition": "Miễn dịch là khả năng của cơ thể nhận biết và tiêu diệt các tác nhân gây bệnh (vi khuẩn, virus); Kháng thể là các protein do tế bào lympho B tiết ra để vô hiệu hóa kháng nguyên lạ.",
            "example": "Tiêm vắc-xin sởi giúp cơ thể tự tạo ra kháng thể đặc hiệu, giúp bảo vệ cơ thể không bị mắc bệnh sởi trong tương lai.",
            "essence": "Hệ miễn dịch là lá chắn phòng thủ sinh học kỳ diệu bảo vệ cơ thể sống trước sự tấn công của thế giới vi sinh vật."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc truyền máu an toàn (Hệ nhóm máu ABO)",
            "meaning": "Không được để kháng nguyên trên hồng cầu của người cho bị ngưng kết bởi kháng thể tương ứng trong huyết tương của người nhận: Kháng nguyên A ngưng kết với Kháng thể alpha; Kháng nguyên B ngưng kết với Kháng thể beta.",
            "example": "Người có nhóm máu O là người cho phổ thông (hồng cầu không có kháng nguyên A, B); Người có nhóm máu AB là người nhận phổ thông.",
            "essence": "Hiện tượng ngưng kết hồng cầu gây tắc mạch máu và nguy hiểm đến tính mạng người bệnh."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày con đường di chuyển của một phân tử thức ăn giàu tinh bột (như bánh mì) qua hệ tiêu hóa của con người.",
            "steps": [
              "Bước 1: Khoang miệng: Nhai nghiền cơ học và enzyme amylase trong nước bọt biến đổi một phần tinh bột chín thành đường maltose.",
              "Bước 2: Dạ dày: Thức ăn được co bóp nhuyễn trong môi trường acid nhưng tinh bột không bị biến đổi hóa học tại đây.",
              "Bước 3: Ruột non: Enzyme của tuyến tụy và ruột phân giải hoàn toàn tinh bột thành đường đơn glucose và hấp thụ qua lông ruột vào máu."
            ],
            "answer": "Ruột non là cơ quan tiêu hóa hóa học và hấp thụ chất dinh dưỡng quan trọng nhất của cơ thể."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng dạ dày là nơi hấp thụ hầu hết các chất dinh dưỡng của thức ăn.",
            "why": "Dạ dày chủ yếu nhào trộn cơ học và tiêu hóa một phần protein; RUỘT NON mới là nơi diễn ra sự hấp thụ 90% chất dinh dưỡng của cơ thể."
          }
        ]
      }
    ]
  },

  "ngu-van": {
    "id": "ngu-van",
    "name": "Ngữ Văn",
    "icon": "📖",
    "chapters": [
      {
        "id": "ch01",
        "title": "Bài 1: Câu chuyện của lịch sử (Truyện lịch sử)",
        "description": "Đặc trưng truyện lịch sử, bối cảnh thời đại, nhân vật lịch sử, nghệ thuật tái hiện khí thế hào hùng của dân tộc.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu văn bản 'Lá cờ thêu sáu chữ vàng' (Nguyễn Huy Tưởng)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành tiếng Việt: Biệt ngữ xã hội và từ ngữ địa phương", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Truyện lịch sử",
            "definition": "Là tác phẩm truyện lấy đề tài từ các sự kiện và nhân vật lịch sử có thật, kết hợp giữa sự thật lịch sử và sự tưởng tượng, hư cấu nghệ thuật của nhà văn.",
            "example": "'Lá cờ thêu sáu chữ vàng' tái hiện hình tượng người anh hùng thiếu niên Trần Quốc Toản trong cuộc kháng chiến chống quân Nguyên.",
            "essence": "Truyện lịch sử làm sống dậy quá khứ oanh liệt, bồi đắp lòng tự hào dân tộc và lòng yêu nước sâu sắc."
          }
        ],
        "rules": [
          {
            "statement": "Mối quan hệ giữa sự thật lịch sử và hư cấu nghệ thuật",
            "meaning": "Nhà văn phải tôn trọng bản chất của sự thật lịch sử lớn, nhưng được quyền hư cấu chi tiết tâm lý, đối thoại và hoàn cảnh cụ thể để nhân vật trở nên sống động, gần gũi.",
            "example": "Chi tiết Trần Quốc Toản vì uất ức không được dự bàn việc quân mà vô tình bóp nát quả cam là hư cấu nghệ thuật tuyệt vời làm nổi bật lòng yêu nước cháy bỏng.",
            "essence": "Hư cấu phục vụ cho việc khắc họa chiều sâu nhân cách của nhân vật lịch sử."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích ý nghĩa chi tiết Trần Quốc Toản vô tình bóp nát quả cam trong văn bản 'Lá cờ thêu sáu chữ vàng'.",
            "steps": [
              "Bước 1: Hoàn cảnh: Đứng trên bờ nhìn vua và các vương hầu bàn kế đánh giặc, Quốc Toản uất ức vì tuổi còn nhỏ không được tham gia.",
              "Bước 2: Hành động vô thức: Tay nắm chặt quả cam vua ban, nỗi uất nghẹn và khát khao đánh giặc dồn lên đôi bàn tay bóp nát quả cam lúc nào không hay.",
              "Bước 3: Ý nghĩa: Chi tiết thể hiện tâm hồn trong sáng, lòng căm thù giặc tột độ và ý chí quyết tâm đền nợ nước của người thiếu niên anh hùng."
            ],
            "answer": "Chi tiết đắt giá biểu tượng cho hào khí quật cường của tuổi trẻ thời Trần."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Coi truyện lịch sử hoàn toàn là tài liệu lịch sử chính xác tuyệt đối từng câu chữ.",
            "why": "Truyện lịch sử là tác phẩm văn học nghệ thuật có chứa yếu tố hư cấu sáng tạo của nhà văn, khác với sách sử ký chính thống."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Bài 2: Vẻ đẹp cổ điển (Thơ Đường luật)",
        "description": "Thể thơ Thất ngôn bát cú Đường luật, niêm, luật, vần, đối, nghệ thuật tả cảnh ngụ tình và vẻ đẹp tâm hồn thi nhân xưa.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu bài thơ 'Qua Đèo Ngang' (Bà Huyện Thanh Quan)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Quy luật niêm, luật, đối trong thơ Thất ngôn bát cú", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thơ Thất ngôn bát cú Đường luật",
            "definition": "Thể thơ cổ điển xuất xứ từ thời Đường (Trung Quốc), mỗi bài gồm 8 câu, mỗi câu 7 chữ, tuân theo quy tắc nghiêm ngặt về niêm, luật bằng trắc, vần và phép đối ở hai cặp câu thực và luận.",
            "example": "Bố cục chuẩn mực 4 phần: Đề (câu 1, 2) -> Thực (câu 3, 4) -> Luận (câu 5, 6) -> Kết (câu 7, 8).",
            "essence": "Vẻ đẹp trang nhã, hàm súc, 'ý tại ngôn ngoại' (ý ở ngoài lời)."
          }
        ],
        "rules": [
          {
            "statement": "Nghệ thuật đối trong hai câu Thực và hai câu Luận",
            "meaning": "Câu 3 đối với câu 4; câu 5 đối với câu 6 về cả thanh điệu (bằng đối trắc), từ loại (danh đối danh, động đối động) và ý nghĩa hình ảnh.",
            "example": "'Nhớ nước đau lòng con quốc quốc / Thương nhà mỏi miệng cái gia gia' (đối thanh, đối từ và chơi chữ đồng âm).",
            "essence": "Phép đối tạo nên sự đăng đối, cân xứng và nhạc điệu trầm bổng tuyệt mỹ."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Chỉ ra nghệ thuật tả cảnh ngụ tình và tâm trạng của tác giả trong hai câu thơ cuối bài 'Qua Đèo Ngang': 'Dừng chân đứng lại trời, non, nước / Một mảnh tình riêng, ta với ta'.",
            "steps": [
              "Bước 1: Không gian: Mênh mông bao la rợn ngợp với ba tầng 'trời, non, nước'.",
              "Bước 2: Con người: Nhỏ bé, cô đơn tột cùng với 'một mảnh tình riêng' sâu kín.",
              "Bước 3: Nghệ thuật đối lập: Giữa vũ trụ vô tận và con người cô độc, cụm từ 'ta với ta' diễn tả sự đối diện với chính tâm hồn cô đơn hoài cổ của nữ sĩ."
            ],
            "answer": "Nỗi buồn sâu lắng, tình yêu nước non và nỗi cô đơn da diết của thi nhân trước hoàng hôn Đèo Ngang."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm cụm từ 'ta với ta' trong bài 'Qua Đèo Ngang' với 'ta với ta' trong bài 'Bạn đến chơi nhà' của Nguyễn Khuyến.",
            "why": "Trong 'Qua Đèo Ngang', 'ta với ta' là một mình đối diện với chính mình cô đơn; còn trong 'Bạn đến chơi nhà', 'ta với ta' là hai người bạn tri âm thấu hiểu gắn kết."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Bài 3: Lời sông núi (Văn bản nghị luận trung đại)",
        "description": "Nghị luận cổ đại, áng văn chính luận mẫu mực, hào khí non sông và tư tưởng nhân nghĩa, độc lập dân tộc.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu văn bản 'Hịch tướng sĩ' (Trần Quốc Tuấn)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Nghệ thuật lập luận và biểu cảm trong văn chính luận", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thể Hịch (Trung đại)",
            "definition": "Là thể văn thư hành chính cổ do vua chúa, tướng lĩnh ban bố trước ba quân nhằm khích lệ tinh thần chiến đấu, vạch trần tội ác kẻ thù và kêu gọi lòng yêu nước chống ngoại xâm.",
            "example": "'Hịch tướng sĩ' của Tiết chế Hưng Đạo Vương Trần Quốc Tuấn viết trước cuộc kháng chiến chống quân Nguyên lần thứ hai (1285).",
            "essence": "Ngôn ngữ đanh thép, hùng hồn, giàu nhạc điệu bi tráng và sức thuyết phục lay động lòng người."
          }
        ],
        "rules": [
          {
            "statement": "Nghệ thuật kết hợp giữa Lí trí và Tình cảm trong văn chính luận",
            "meaning": "Lập luận sắc bén bằng lí lẽ lịch sử kết hợp với cảm xúc chân thành, đau xót và căm thù giặc của người chủ soái tạo nên sức thuyết phục mãnh liệt.",
            "example": "'Ta thường tới bữa quên ăn, nửa đêm vỗ gối; ruột đau như cắt, nước mắt đầm đìa; chỉ căm tức chưa xả thịt lột da, nuốt gan uống máu quân thù...'",
            "essence": "Tình cảm chân thành của người tướng soái làm bừng cháy lòng trung quân ái quốc của ba quân tướng sĩ."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trần Quốc Tuấn đã phê phán những thái độ sai trái nào của tướng sĩ trong 'Hịch tướng sĩ'?",
            "steps": [
              "Bước 1: Thái độ bàng quan, thờ ơ: Thấy nước nhà chịu nhục trước sứ giặc mà không biết lo, thấy chủ nhục mà không biết thẹn.",
              "Bước 2: Ham thú vui tầm thường: Ham chọi gà, mê cờ bạc, chăm lo vườn ruộng, đắm đuối tiếng hát câu ca.",
              "Bước 3: Hậu quả: Khi giặc tràn đến, cựa gà không đâm thủng áo giáp giặc, bạc vàng không chuộc được tính mạng, làm mất nước tan nhà."
            ],
            "answer": "Lời phê phán nghiêm khắc nhưng đầy ân tình thức tỉnh trách nhiệm của người cầm vũ khí bảo vệ non sông."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng 'Hịch tướng sĩ' chỉ mang tính đe dọa, trừng phạt quân sĩ.",
            "why": "Bản hịch tràn đầy tình thương yêu ruột thịt của chủ tướng đối với tướng sĩ; lời răn đe chỉ nhằm mục đích thức tỉnh lương tri và danh dự quân nhân."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Bài 4: Tiếng cười trào phúng (Truyện cười và Thơ trào phúng)",
        "description": "Nghệ thuật tạo tiếng cười, tiếng cười tự trào và châm biếm, phê phán thói hư tật xấu trong xã hội phong kiến xưa.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu thơ trào phúng của Tú Xương và Nguyễn Khuyến", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành tiếng Việt: Nghĩa tường minh và hàm ý", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Văn học trào phúng",
            "definition": "Là loại văn học dùng tiếng cười châm biếm, mỉa mai, hài hước để phê phán, đả kích những hiện tượng tiêu cực, thói hư tật xấu và sự giả tạo trong đời sống xã hội.",
            "example": "Tú Xương chế giễu cảnh trường thi nhốn nháo thời thực dân nửa phong kiến trong bài thơ 'Vịnh khoa thi Hương'.",
            "essence": "Đằng sau tiếng cười trào phúng sắc sảo là giọt nước mắt xót xa cho tình cảnh non sông đất nước."
          }
        ],
        "rules": [
          {
            "statement": "Nghĩa tường minh và Hàm ý",
            "meaning": "Nghĩa tường minh là phần thông báo được diễn đạt trực tiếp bằng từ ngữ trong câu; Hàm ý là phần thông báo tuy không nói ra trực tiếp nhưng có thể suy ra từ ngữ cảnh.",
            "example": "'Bác có bật đèn không?' có hàm ý nhắc nhở trời đã tối hoặc phòng quá tối, hãy bật đèn lên.",
            "essence": "Hàm ý làm cho lời nói trở nên lịch sự, tế nhị hoặc châm biếm sâu cay."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích nghệ thuật đối lập và hàm ý châm biếm trong hai câu thơ của Tú Xương: 'Lôi thôi sĩ tử vai đeo lọ / Ậm ọe quan trường miệng thét loa'.",
            "steps": [
              "Bước 1: Từ láy tạo hình: 'Lôi thôi' diễn tả sự luộm thuộm, nhếch nhác của người đi thi; 'ậm ọe' gợi âm thanh ú ớ, ra oai giả tạo của quan trường.",
              "Bước 2: Đảo ngữ: Đưa từ láy lên đầu câu nhấn mạnh cảnh tượng hỗn độn, bi hài của chốn trường thi vốn tôn nghiêm.",
              "Bước 3: Hàm ý châm biếm: Vạch trần sự suy đồi của nền Nho học thời mạt vận khi chữ nghĩa thánh hiền bị đem ra làm trò hề."
            ],
            "answer": "Bức tranh bi hài kịch vạch trần sự tha hóa của kỳ thi cử thời thực dân nửa phong kiến."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa nói bóng gió vô nghĩa với hàm ý nghệ thuật.",
            "why": "Hàm ý phải có căn cứ suy luận logic dựa trên ngữ cảnh giao tiếp cụ thể; người nghe phải có khả năng giải mã được ý đồ của người nói."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Bài 5: Chân dung cuộc sống (Truyện ngắn hiện đại)",
        "description": "Nghệ thuật xây dựng tình huống truyện, phân tích diễn biến tâm lý nhân vật và thông điệp nhân đạo sâu sắc trong tác phẩm văn xuôi hiện đại.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu văn bản truyện ngắn 'Chiếc lá cuối cùng' (O. Henry)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Viết bài văn phân tích một nhân vật văn học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Kiệt tác nghệ thuật (Masterpiece) trong văn học",
            "definition": "Là tác phẩm nghệ thuật đỉnh cao không chỉ đạt đến sự hoàn mỹ về kỹ thuật mà còn chứa đựng tình yêu thương bao la và đức hi sinh quên mình vì sự sống con người.",
            "example": "Bức tranh chiếc lá thường xuân trên tường của cụ bơ-men được vẽ trong đêm mưa tuyết dữ dội cứu sống cô gái trẻ Johnsy.",
            "essence": "Nghệ thuật chân chính là nghệ thuật vị nhân sinh, cứu rỗi tâm hồn và thắp sáng hy vọng sống."
          }
        ],
        "rules": [
          {
            "statement": "Nghệ thuật đảo ngược tình huống hai lần (Twist ending)",
            "meaning": "Đặc trưng truyện ngắn O. Henry với kết thúc bất ngờ: Johnsy từ tuyệt vọng cận kề cái chết trở nên yêu đời khỏe mạnh; ngược lại cụ Bơ-men đang khỏe mạnh lại qua đời vì viêm phổi sau đêm vẽ kiệt tác.",
            "example": "Sự hoán đổi số phận tạo nên dư ba rung động mãnh liệt trong lòng độc giả.",
            "essence": "Sự hi sinh thầm lặng của cụ họa sĩ già làm bừng sáng giá trị nhân đạo cao cả."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao chiếc lá thường xuân do cụ Bơ-men vẽ lại được coi là một kiệt tác nghệ thuật?",
            "steps": [
              "Bước 1: Vẽ giống như thật: Chiếc lá giống thật đến mức cả hai nữ họa sĩ trẻ nhìn ở cự li gần cũng không hề nhận ra đó là tranh vẽ.",
              "Bước 2: Hoàn cảnh sáng tác: Cụ Bơ-men vẽ trong một đêm mưa tuyết lạnh giá cùng cực, đánh đổi bằng cả tính mạng của mình.",
              "Bước 3: Hiệu quả cứu rỗi: Chiếc lá đã đánh thức niềm tin, nghị lực và cứu sống cô gái trẻ Johnsy thoát khỏi lưỡi hái tử thần."
            ],
            "answer": "Chiếc lá là kiệt tác vì nó được vẽ bằng tình yêu thương vô bờ và mang lại sự hồi sinh cho một con người."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Khi viết bài phân tích nhân vật chỉ tóm tắt lại cốt truyện từ đầu đến cuối.",
            "why": "Phân tích nhân vật phải chia theo các luận điểm (phẩm chất, tính cách, hành động, diễn biến tâm lý) kèm dẫn chứng và nghệ thuật khắc họa, tránh biến thành bài kể chuyện."
          }
        ]
      }
    ]
  },

  "lich-su-dia-li": {
    "id": "lich-su-dia-li",
    "name": "Lịch sử & Địa lí",
    "icon": "🌍",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Cách mạng tư sản và Chủ nghĩa đế quốc (TK XVI - đầu XX)",
        "description": "Cách mạng tư sản Anh, Chiến tranh giành độc lập của 13 thuộc địa Anh ở Bắc Mỹ, Cách mạng tư sản Pháp và sự ra đời của chủ nghĩa đế quốc.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Các cuộc cách mạng tư sản tiêu biểu thế kỉ XVII - XVIII", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Cách mạng công nghiệp và sự hình thành chủ nghĩa đế quốc", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Cách mạng tư sản",
            "definition": "Là cuộc cách mạng do giai cấp tư sản (hoặc quý tộc mới) lãnh đạo nhằm lật đổ chế độ phong kiến chuyên chế, xóa bỏ các rào cản kinh tế, mở đường cho chủ nghĩa tư bản phát triển.",
            "example": "Cách mạng tư sản Pháp (1789) lật đổ chế độ quân chủ chuyên chế Louis XVI, ban bố Tuyên ngôn Nhân quyền và Dân quyền.",
            "essence": "Xác lập quyền lực chính trị của giai cấp tư sản và thúc đẩy nền kinh tế thị trường tự do."
          }
        ],
        "rules": [
          {
            "statement": "Đặc trưng của Chủ nghĩa tư bản chuyển sang giai đoạn Chủ nghĩa đế quốc (cuối TK XIX)",
            "meaning": "Sự xuất hiện của các tổ chức độc quyền chi phối nền kinh tế, tư bản tài chính xuất khẩu tư bản và cuộc cạnh tranh xâu xé thuộc địa trên quy mô toàn cầu.",
            "example": "Các tập đoàn độc quyền dầu mỏ, thép ở Mỹ và các đế quốc Anh, Pháp phân chia thị trường thuộc địa ở châu Á, châu Phi.",
            "essence": "Mâu thuẫn tranh giành thuộc địa giữa các đế quốc là nguyên nhân sâu xa dẫn đến Chiến tranh thế giới thứ nhất."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Khẩu hiệu nổi tiếng 'Tự do - Bình đẳng - Bác ái' xuất phát từ cuộc cách mạng nào? Ý nghĩa lịch sử của nó là gì?",
            "steps": [
              "Bước 1: Nguồn gốc: Xuất phát từ cuộc Đại cách mạng tư sản Pháp năm 1789.",
              "Bước 2: Nội dung tiến bộ: Khẳng định con người sinh ra có quyền tự do và bình đẳng, tấn công trực diện vào trật tự đẳng cấp phong kiến bất công.",
              "Bước 3: Tầm ảnh hưởng: Trở thành ngọn cờ cổ vũ phong trào đấu tranh giải phóng con người trên toàn thế giới suốt nhiều thế kỉ."
            ],
            "answer": "Xuất phát từ Cách mạng tư sản Pháp 1789, biểu tượng cho khát vọng dân chủ và quyền con người phổ quát."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng Cách mạng tư sản Pháp đã mang lại quyền lợi trọn vẹn bình đẳng tuyệt đối cho giai cấp công nhân và nông dân nghèo.",
            "why": "Cách mạng tư sản chỉ thay thế sự bóc lột phong kiến bằng sự bóc lột tư bản; quyền lợi kinh tế cốt lõi rơi vào tay giai cấp tư sản giàu có."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Việt Nam từ thế kỉ XVI đến đầu thế kỉ XVIII",
        "description": "Chiến tranh Nam - Bắc triều, chiến tranh Trịnh - Nguyễn, sự chia cắt Đàng Trong - Đàng Ngoài và công cuộc khẩn hoang xác lập chủ quyền phương Nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Xung đột Nam - Bắc triều và Trịnh - Nguyễn phân tranh", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Công cuộc khẩn hoang và xác lập chủ quyền Hoàng Sa, Trường Sa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Đội Hoàng Sa và Đội Bắc Hải thời các chúa Nguyễn",
            "definition": "Là các tổ chức dân binh do chính quyền chúa Nguyễn lập ra từ thế kỉ XVII để thực thi nhiệm vụ đo đạc hải trình, thu lượm hải vật, cắm mốc và khẳng định chủ quyền quốc gia trên hai quần đảo Hoàng Sa và Trường Sa.",
            "example": "Hàng năm vào tháng 3 âm lịch, các đội binh phu Hoàng Sa dong thuyền buồm ra khơi làm nhiệm vụ suốt 6 tháng ròng.",
            "essence": "Là bằng chứng lịch sử và pháp lý vững chắc khẳng định chủ quyền biển đảo thiêng liêng liên tục, hòa bình của Việt Nam."
          }
        ],
        "rules": [
          {
            "statement": "Hậu quả của cuộc Trịnh - Nguyễn phân tranh (1627 - 1672)",
            "meaning": "Đất nước bị chia cắt làm hai miền lấy sông Gianh (Quảng Bình) làm ranh giới; nhân dân chịu nhiều đau khổ vì chiến tranh huynh đệ tương tàn.",
            "example": "Đàng Ngoài do vua Lê - chúa Trịnh cai quản; Đàng Trong do các chúa Nguyễn cai quản.",
            "essence": "Sự chia cắt kéo dài hơn một thế kỉ kìm hãm sự phát triển thống nhất của đất nước."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Công cuộc khẩn hoang vùng đất Nam Bộ của các chúa Nguyễn thế kỉ XVII - XVIII có ý nghĩa lịch sử như thế nào?",
            "steps": [
              "Bước 1: Mở rộng lãnh thổ: Mở rộng không gian sinh tồn của đất nước về phương Nam, biến vùng đất hoang vu thành đồng bằng trù phú.",
              "Bước 2: Kinh tế - xã hội: Tiếp thu các nguồn lực mới, phát triển nông nghiệp lúa nước và thương nghiệp sầm uất tại Gia Định, Sài Gòn.",
              "Bước 3: Khẳng định chủ quyền: Xác lập và bảo vệ vững chắc chủ quyền biển đảo tại quần đảo Hoàng Sa, Trường Sa và vùng biển Tây Nam."
            ],
            "answer": "Mở rộng bờ cõi non sông, định hình không gian địa lí thống nhất của nước Việt Nam ngày nay."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng sông Bến Hải là ranh giới chia cắt Đàng Trong và Đàng Ngoài thời phong kiến.",
            "why": "Sông Bến Hải là giới tuyến quân sự tạm thời sau Hiệp định Genève 1954; còn thời Trịnh - Nguyễn thế kỉ XVII ranh giới là SÔNG GIANH (Quảng Bình)."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Vị trí địa lí và Địa hình Việt Nam",
        "description": "Vị trí địa lí, phạm vi lãnh thổ vùng đất, vùng trời, vùng biển; đặc điểm chung của địa hình đồi núi chiếm 3/4 diện tích và hướng nghiêng tây bắc - đông nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vị trí địa lí và phạm vi lãnh thổ Việt Nam", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Đặc điểm chung của địa hình và các khu vực địa hình", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tính chất nhiệt đới ẩm gió mùa của thiên nhiên Việt Nam",
            "definition": "Toàn bộ lãnh thổ nằm trọn trong vùng nội chí tuyến Bắc bán cầu, tiếp giáp Biển Đông rộng lớn và nằm trong khu vực gió mùa châu Á, tạo nên khí hậu nóng ẩm, mưa nhiều và thảm thực vật quanh năm xanh tốt.",
            "example": "Lượng mưa trung bình năm lớn (1500 - 2000 mm), số giờ nắng cao (1400 - 3000 giờ/năm).",
            "essence": "Vị trí địa lí quy định tính chất tự nhiên cơ bản nhất của thiên nhiên Việt Nam."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm cơ bản của địa hình Việt Nam",
            "meaning": "Địa hình đồi núi chiếm 3/4 diện tích lãnh thổ nhưng chủ yếu là đồi núi thấp (dưới 1000m chiếm 85%); Hướng nghiêng chung là Tây Bắc - Đông Nam; Có hai hướng núi chính là hướng Tây Bắc - Đông Nam và hướng vòng cung.",
            "example": "Dãy Hoàng Liên Sơn chạy theo hướng Tây Bắc - Đông Nam; Vùng núi Đông Bắc có 4 cánh cung núi mở rộng về phía bắc.",
            "essence": "Địa hình chi phối sự phân hóa sâu sắc của khí hậu, thủy văn và thổ nhưỡng giữa các vùng miền."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao nước ta không bị khô hạn như các nước cùng vĩ độ ở Tây Á và Bắc Phi (như sa mạc Sahara)?",
            "steps": [
              "Bước 1: Tây Á và Bắc Phi nằm sâu trong lục địa hoặc bờ biển có dòng biển lạnh ngự trị nên khô hạn cực độ.",
              "Bước 2: Việt Nam giáp Biển Đông rộng lớn (hơn 3,4 triệu km2) là nguồn dự trữ nhiệt ẩm khổng lồ.",
              "Bước 3: Khối khí gió mùa mùa hạ từ biển thổi vào mang theo lượng hơi nước lớn gây mưa dồi dào, biến nước ta thành một xứ sở xanh tươi trù phú."
            ],
            "answer": "Nhờ tác động điều hòa nhiệt ẩm của Biển Đông và hoàn lưu gió mùa ẩm ướt."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng địa hình Việt Nam chủ yếu là núi cao hiểm trở.",
            "why": "Địa hình đồi núi chiếm 3/4 diện tích nhưng ĐỒI NÚI THẤP dưới 1000m chiếm tới 85%; núi cao trên 2000m chỉ chiếm khoảng 1% diện tích."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Khí hậu và Thủy văn Việt Nam",
        "description": "Đặc điểm khí hậu nhiệt đới gió mùa phân hóa đa dạng (Bắc - Nam, Đông - Tây, theo độ cao) và mạng lưới sông ngòi dày đặc, nhiều nước, giàu phù sa.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khí hậu nhiệt đới gió mùa và sự phân hóa khí hậu", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Mạng lưới sông ngòi và chế độ nước sông theo mùa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Gió mùa Đông Bắc",
            "definition": "Khối khí lạnh xuất phát từ cao áp Siberia tràn xuống miền Bắc nước ta từ tháng 11 đến tháng 4 năm sau, làm cho miền Bắc có một mùa đông thực sự với nền nhiệt hạ thấp.",
            "example": "Nửa đầu mùa đông lạnh khô; nửa sau mùa đông (tháng 2-3) đi qua biển gây mưa phùn ẩm ướt khó chịu.",
            "essence": "Gió mùa Đông Bắc làm cho miền Bắc nước ta có mùa đông lạnh nhất so với các vùng đất cùng vĩ độ trên thế giới."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm chung của sông ngòi Việt Nam",
            "meaning": "Mạng lưới sông ngòi dày đặc (có tới 2.360 con sông dài trên 10km); Sông nhiều nước, giàu phù sa (hơn 200 triệu tấn/năm); Chế độ nước theo mùa rõ rệt (mùa lũ tương ứng mùa mưa, mùa cạn tương ứng mùa khô).",
            "example": "Sông Hồng và sông Mê Kông là hai hệ thống sông lớn nhất bồi đắp hai vựa lúa trù phú của đất nước.",
            "essence": "Sông ngòi là tấm gương phản chiếu trung thành của chế độ khí hậu nhiệt đới gió mùa mưa nhiều."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao sông ngòi miền Trung nước ta thường ngắn, dốc và lũ lên rất nhanh đột ngột?",
            "steps": [
              "Bước 1: Địa hình: Lãnh thổ hẹp ngang, dải núi Trường Sơn chạy sát biển, sườn dốc nghiêng nhanh về phía đông.",
              "Bước 2: Mưa bão: Lượng mưa mùa thu đông tập trung rất lớn, kết hợp với các cơn bão đổ bộ dồn dập.",
              "Bước 3: Lưu vực: Lưu vực nhỏ hẹp, nước mưa đổ dồn từ trên đỉnh núi xuống đồng bằng trong thời gian cực ngắn gây lũ quét ngập lụt cục bộ."
            ],
            "answer": "Do lãnh thổ hẹp ngang, địa hình dốc sát biển kết hợp mưa bão dồn dập."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng miền Nam cũng có mùa đông lạnh như miền Bắc.",
            "why": "Dãy Bạch Mã (vĩ tuyến 16 độ Bắc) ngăn chặn gió mùa Đông Bắc suy yếu, do đó từ Đà Nẵng trở vào Nam khí hậu mang tính chất cận xích đạo nóng quanh năm, không có mùa đông lạnh."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Thổ nhưỡng và Sinh vật Việt Nam",
        "description": "Các nhóm đất chính (đất feralit đồi núi, đất phù sa đồng bằng), sự đa dạng sinh học phong phú và các biện pháp bảo tồn thiên nhiên bền vững.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Các nhóm đất chính ở nước ta và giá trị sử dụng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sự đa dạng sinh học và vấn đề bảo tồn nguồn gen", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Đất Feralit (Ferralsols)",
            "definition": "Là loại đất hình thành ở vùng đồi núi nhiệt đới ẩm, quá trình phong hóa diễn ra mạnh mẽ làm rửa trôi các chất kiềm, tích tụ nhiều hợp chất oxide sắt và oxide nhôm tạo nên màu đỏ vàng đặc trưng.",
            "example": "Đất feralit trên đá bazan ở Tây Nguyên rất màu mỡ, thích hợp trồng cây công nghiệp lâu năm như cà phê, cao su, hồ tiêu.",
            "essence": "Chiếm hơn 65% diện tích tự nhiên, là tài nguyên quý giá phát triển kinh tế lâm - nông nghiệp đồi rừng."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc sử dụng và cải tạo đất đồi núi dốc",
            "meaning": "Phải kết hợp giữa nông nghiệp và lâm nghiệp (nông lâm kết hợp), trồng cây theo đường đồng mức, làm ruộng bậc thang để chống xói mòn, rửa trôi lớp đất màu.",
            "example": "Ruộng bậc thang Mù Cang Chải vừa là cảnh quan tuyệt mỹ vừa là sáng tạo chống xói mòn đất dốc của đồng bào vùng cao.",
            "essence": "Mất lớp thảm thực vật che phủ sẽ biến đất đồi dốc thành đất trống đồi trọc cằn cỗi."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 3 nguyên nhân chính làm suy giảm tính đa dạng sinh học ở nước ta và biện pháp khắc phục.",
            "steps": [
              "Bước 1: Nguyên nhân: Chặt phá rừng bừa bãi làm mất môi trường sống; Săn bắt, buôn bán động vật hoang dã trái phép; Ô nhiễm môi trường đất, nước.",
              "Bước 2: Hậu quả: Nhiều loài sinh vật quý hiếm đứng trước nguy cơ tuyệt chủng, mất cân bằng sinh thái.",
              "Bước 3: Biện pháp: Xây dựng và quản lý nghiêm ngặt các Vườn quốc gia, Khu bảo tồn thiên nhiên; Trồng rừng phòng hộ và xử phạt nghiêm minh các hành vi săn trộm."
            ],
            "answer": "Bảo vệ rừng đầu nguồn, lập khu bảo tồn và thực thi nghiêm pháp luật bảo vệ động vật hoang dã."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng đất phù sa đồng bằng chỉ phân bố ở Đồng bằng sông Hồng và Đồng bằng sông Cửu Long.",
            "why": "Ngoài hai đồng bằng châu thổ lớn, dải đồng bằng ven biển miền Trung cũng có đất phù sa (mặc dù nghèo dinh dưỡng và nhiều cát hơn)."
          }
        ]
      }
    ]
  },

  "tieng-anh": {
    "id": "tieng-anh",
    "name": "Tiếng Anh",
    "icon": "🇬🇧",
    "chapters": [
      {
        "id": "ch01",
        "title": "Unit 1: Leisure Time",
        "description": "Vocabulary about teen hobbies and pastimes, verbs of liking/disliking followed by Gerunds and To-infinitives.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Leisure activities vocabulary & Pronunciation /ʊ/ and /uː/", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Grammar: Verbs of liking + Gerunds vs. To-infinitives", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Verbs of liking + To-infinitive / Gerund",
            "definition": "Verbs like like, love, hate, prefer can be followed by either a gerund (V-ing) or a to-infinitive (to V) with little difference in meaning.",
            "example": "I like making origami. / I like to make origami in my free time.",
            "essence": "V-ing emphasizes the enjoyment of the activity; To-infinitive emphasizes habit, choice, or duty."
          }
        ],
        "rules": [
          {
            "statement": "Verbs ONLY followed by Gerunds (V-ing)",
            "meaning": "Certain verbs such as enjoy, fancy, adore, dislike, detest, mind can ONLY be followed by a gerund (V-ing), NEVER a to-infinitive.",
            "example": "She fancies doing DIY projects. (NOT: She fancies to do...)",
            "essence": "Memorizing the distinct verb categories prevents common grammatical errors."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Choose the correct form: 'My friends detest (surf) __________ the net when camping outdoors.'",
            "steps": [
              "Step 1: Identify the main verb: 'detest' (meaning intensely dislike).",
              "Step 2: 'Detest' belongs to the category of verbs followed strictly by a Gerund.",
              "Step 3: Change 'surf' to 'surfing'."
            ],
            "answer": "My friends detest surfing the net when camping outdoors."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'I enjoy to hang out with friends.'",
            "why": "'Enjoy' is always followed by a gerund: 'I enjoy hanging out with friends.'"
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Unit 2: Life in the Countryside",
        "description": "Rural activities and scenic vocabulary, comparative forms of adverbs of manner (more quickly, harder, better).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Rural lifestyle and farming vocabulary", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Comparative forms of Adverbs of manner", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Comparative Adverbs of Manner",
            "definition": "Used to compare how two people or things perform an action. For adverbs ending in -ly, add 'more' (more quietly); for irregular adverbs, change the form (fast -> faster, well -> better, badly -> worse, hard -> harder).",
            "example": "He drives more carefully than his brother. / Farmers work harder during harvest season.",
            "essence": "Adverbs modify verbs of action, whereas adjectives modify nouns."
          }
        ],
        "rules": [
          {
            "statement": "Irregular comparative adverbs",
            "meaning": "Fast -> faster; Early -> earlier; Late -> later; Well -> better; Badly -> worse; Far -> farther/further.",
            "example": "She ran faster than anyone else in the school competition.",
            "essence": "Do not add 'more' to adverbs that already have special irregular comparative endings."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Complete the sentence with the comparative form of the adverb in brackets: 'In the countryside, life moves (slowly) __________ than in big cities.'",
            "steps": [
              "Step 1: 'Slowly' is a two-syllable adverb ending in -ly.",
              "Step 2: Add 'more' before the adverb: 'more slowly'.",
              "Step 3: Complete sentence: 'In the countryside, life moves more slowly than in big cities.'"
            ],
            "answer": "more slowly"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'more fast' or 'fastly'.",
            "why": "'Fast' is both an adjective and an adverb; there is no word 'fastly'. The comparative form is 'faster'."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Unit 3: Teenagers and Peer Pressure",
        "description": "Teen clubs, school forums, social media, peer pressure, and complex sentences with adverbial clauses of result, concession, and reason.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Teen stress, school clubs and online forums", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Clauses of concession (Although / Even though) & Reason", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Clauses of concession (Although / Even though / Though)",
            "definition": "Introduces a contrasting fact that makes the statement in the main clause surprising: Although / Even though + S + V, S + V.",
            "example": "Although he was under a lot of study pressure, he managed to stay positive.",
            "essence": "Shows unexpected contrast between two interconnected ideas."
          }
        ],
        "rules": [
          {
            "statement": "Never use 'but' in the same sentence with 'although'",
            "meaning": "In Vietnamese we say 'Mặc dù... nhưng...', but in English, you must NEVER use both 'although' and 'but' together.",
            "example": "CORRECT: Although she prepared well, she felt nervous. (INCORRECT: Although she prepared well, but she felt nervous.)",
            "essence": "Subordinating conjunctions and coordinating conjunctions cannot join the same pair of clauses simultaneously."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Combine the sentences using 'Although': 'He practiced sports hard. He did not win the gold medal.'",
            "steps": [
              "Step 1: Place 'Although' at the beginning of the clause containing the effort.",
              "Step 2: 'Although he practiced sports hard, he did not win the gold medal.'",
              "Step 3: Ensure there is a comma separating the dependent clause and the main clause."
            ],
            "answer": "Although he practiced sports hard, he did not win the gold medal."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'Although + but' in the same sentence.",
            "why": "This is a direct word-by-word translation error from Vietnamese ('Mặc dù... nhưng...'). In English, use ONLY 'although' OR 'but'."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Unit 4: Ethnic Groups of Viet Nam",
        "description": "Cultural diversity, communal houses, stilt houses, traditional festivals, and yes/no questions vs. Wh-questions with articles (a, an, the, zero article).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Customs and costumes of Vietnamese ethnic groups", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Articles: Definite article 'The' vs. Indefinite / Zero article", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "The Definite Article 'The' with Ethnic Groups",
            "definition": "Use 'The' before the name of an ethnic group or nationality to refer to the entire people: The Kinh, the Thai, the H'mong, the Tay.",
            "example": "The Tay people have their own written language and rich folklore.",
            "essence": "'The' pluralizes and unifies the collective identity of the community."
          }
        ],
        "rules": [
          {
            "statement": "Zero article before plural countable nouns in general statements",
            "meaning": "Do not use 'the' when talking about things or people in general.",
            "example": "Terraced fields are common in mountainous areas. (General statement -> No article)",
            "essence": "Using 'the' specifies a particular set of fields already known to the speaker."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Fill in the blank with 'a', 'an', 'the' or zero article: '__________ communal house is __________ heart of the village in the Central Highlands.'",
            "steps": [
              "Step 1: First blank refers to a typical communal house in general: 'A communal house' or specific 'The communal house'.",
              "Step 2: Second blank refers to a unique metaphorical centre: 'the heart of...'",
              "Step 3: 'The communal house is the heart of the village in the Central Highlands.'"
            ],
            "answer": "The / the"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Omitting 'the' when referring to ethnic groups: 'Kinh people' instead of 'The Kinh people'.",
            "why": "In formal English, the definite article 'the' is mandatory when designating an entire ethnic group."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Unit 5: Our Customs and Traditions",
        "description": "Family traditions, social etiquette, generational customs, and modal verbs of obligation: Should / Shouldn't vs. Have to / Must.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Dining etiquette and table manners around the world", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Modal verbs: Have to (external obligation) vs. Must (internal)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "'Must' vs. 'Have to'",
            "definition": "'Must' expresses internal obligation from the speaker's own feelings or moral sense; 'Have to' expresses external obligation from rules, laws, or circumstances.",
            "example": "I must call my grandmother today. (My personal wish) / You have to wear a uniform at school. (School rule)",
            "essence": "In the past tense, 'had to' must be used because 'must' has no past form."
          }
        ],
        "rules": [
          {
            "statement": "'Mustn't' (Prohibition) vs. 'Don't have to' (Lack of necessity)",
            "meaning": "'Mustn't' means you are NOT allowed to do it (forbidden); 'Don't have to' means it is NOT necessary (you can do it if you want).",
            "example": "You mustn't speak loudly in the library. / Tomorrow is Sunday, so I don't have to wake up early.",
            "essence": "Crucial distinction between prohibition and freedom of choice."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Choose 'mustn't' or 'don't have to': 'You __________ touch the temple statues; it is strictly forbidden.'",
            "steps": [
              "Step 1: 'strictly forbidden' signals a strict legal/religious prohibition.",
              "Step 2: 'Mustn't' is the modal verb of strict prohibition.",
              "Step 3: Complete sentence: 'You mustn't touch the temple statues; it is strictly forbidden.'"
            ],
            "answer": "mustn't"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'mustn't' when you want to say something is unnecessary.",
            "why": "If something is not needed, use 'don't have to' or 'needn't'. 'Mustn't' means DO NOT DO IT UNDER ANY CIRCUMSTANCES."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Unit 6: Science and Technology",
        "description": "Inventions, digital gadgets, artificial intelligence, online learning, and reported speech (indirect statements).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Modern technological devices and AI applications", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Reported Speech: Statements and Tense shifting", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Reported Speech (Indirect Speech)",
            "definition": "Used to communicate what someone else said without quoting their exact words. Typically requires shifting tenses back (backshift), changing pronouns, and updating time/place markers.",
            "example": "Direct: 'I am reading a tech blog,' Minh said. -> Reported: Minh said that he was reading a tech blog.",
            "essence": "Allows the reporting speaker to integrate another person's statement smoothly into the current narrative context."
          }
        ],
        "rules": [
          {
            "statement": "Tense shift rule in Reported Speech",
            "meaning": "When the reporting verb is in the past (said, told), shift the verb in the quote one tense back: Present Simple -> Past Simple; Present Continuous -> Past Continuous; Will -> Would; Can -> Could.",
            "example": "'We will test the robot tomorrow' -> They said that they would test the robot the following day.",
            "essence": "Reflects the temporal distance between the moment of original utterance and the moment of reporting."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Change into reported speech: 'Lan said: \"My father works as a software engineer at a tech company.\"'",
            "steps": [
              "Step 1: Change pronoun: 'My father' becomes 'Her father'.",
              "Step 2: Shift tense: Present Simple 'works' becomes Past Simple 'worked'.",
              "Step 3: Combine with reporting clause: 'Lan said that her father worked as a software engineer at a tech company.'"
            ],
            "answer": "Lan said that her father worked as a software engineer at a tech company."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Forgetting to change time words: keeping 'tomorrow' instead of 'the next day / the following day'.",
            "why": "Time markers are anchored to the original moment of speaking; when reported later, they must be adjusted relative to the present."
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
        "title": "Chủ đề 1: Lịch sử Máy tính và Mạng Internet",
        "description": "Lịch sử phát triển các thế hệ máy tính, kết nối mạng máy tính toàn cầu, điện toán đám mây và lưu trữ trực tuyến.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Các thế hệ máy tính điện tử và xu hướng tương lai", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Mạng Internet và dịch vụ lưu trữ đám mây", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Điện toán đám mây (Cloud Computing)",
            "definition": "Là mô hình cung cấp các tài nguyên điện toán (phần mềm, lưu trữ, máy chủ) qua Internet theo nhu cầu, cho phép người dùng truy cập dữ liệu mọi lúc mọi nơi từ mọi thiết bị.",
            "example": "Google Drive, Microsoft OneDrive, Dropbox giúp học sinh lưu trữ bài tập trên mạng mà không lo mất ổ cứng hỏng.",
            "essence": "Chuyển dịch từ việc sở hữu phần cứng cục bộ sang việc thuê và chia sẻ tài nguyên tính toán trên mạng toàn cầu."
          }
        ],
        "rules": [
          {
            "statement": "Lợi ích của lưu trữ dữ liệu trên đám mây",
            "meaning": "Tự động sao lưu dữ liệu, khả năng đồng bộ hóa tức thì giữa điện thoại và máy tính, và khả năng chia sẻ tệp để làm việc nhóm cùng lúc theo thời gian thực.",
            "example": "Nhiều học sinh cùng mở một tệp Google Docs để viết chung bài thuyết trình môn Lịch sử.",
            "essence": "Phá vỡ giới hạn không gian và thúc đẩy làm việc nhóm hiệu quả cao."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 2 rủi ro tiềm ẩn khi lưu trữ dữ liệu nhạy cảm trên đám mây và biện pháp phòng ngừa.",
            "steps": [
              "Bước 1: Rủi ro 1: Nguy cơ bị lộ mật khẩu tài khoản dẫn đến kẻ xấu truy cập dữ liệu cá nhân. Biện pháp: Bật xác thực 2 lớp (2FA).",
              "Bước 2: Rủi ro 2: Mất kết nối Internet thì không thể truy cập tài liệu khẩn cấp. Biện pháp: Cài đặt chế độ lưu offline các tệp quan trọng.",
              "Bước 3: Đánh giá: Quản lý mật khẩu chặt chẽ và luôn có phương án dự phòng cục bộ."
            ],
            "answer": "Bật xác thực 2 bước (2FA) và lưu trữ dự phòng ngoại tuyến (offline)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chia sẻ quyền chỉnh sửa (Editor) công khai cho bất kỳ ai có đường liên kết đối với các tệp dữ liệu quan trọng.",
            "why": "Bất kỳ ai vô tình hoặc cố ý đều có thể xóa hoặc sửa hỏng nội dung dữ liệu của bạn mà không thể kiểm soát."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Đạo đức số và Bản quyền phần mềm",
        "description": "Bản quyền số, sở hữu trí tuệ, phần mềm mã nguồn mở, phòng chống mã độc và virus máy tính.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Bản quyền phần mềm và sở hữu trí tuệ trên Internet", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phòng chống mã độc, virus và an toàn hệ thống", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Phần mềm mã nguồn mở (Open Source Software)",
            "definition": "Là phần mềm mà mã nguồn công khai cho phép mọi người tự do sử dụng, nghiên cứu, sửa đổi và chia sẻ cho cộng đồng phi thương mại.",
            "example": "Hệ điều hành Linux, bộ ứng dụng văn phòng LibreOffice, trình duyệt web Mozilla Firefox.",
            "essence": "Tôn vinh tinh thần chia sẻ tri thức và hợp tác sáng tạo của cộng đồng lập trình viên thế giới."
          }
        ],
        "rules": [
          {
            "statement": "Luật Sở hữu trí tuệ đối với tác phẩm số",
            "meaning": "Mọi hình ảnh, bài viết, âm nhạc, video và phần mềm trên mạng đều thuộc quyền tác giả; sao chép hoặc sử dụng cho mục đích thương mại bắt buộc phải xin phép và trích dẫn nguồn rõ ràng.",
            "example": "Khi lấy ảnh trên mạng đưa vào bài thuyết trình phải ghi rõ: 'Nguồn ảnh: Tác giả A / Trang web B'.",
            "essence": "Tôn trọng bản quyền là thể hiện tư cách công dân số văn minh và thượng tôn pháp luật."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao việc cài đặt và sử dụng phần mềm bẻ khóa (cracked/lậu) lại gây nguy hiểm nghiêm trọng cho máy tính?",
            "steps": [
              "Bước 1: Vi phạm pháp luật về bản quyền phần mềm và quyền sở hữu trí tuệ của tác giả.",
              "Bước 2: Các tệp bẻ khóa thường bị kẻ xấu nhúng mã độc gián điệp (Trojan, Keylogger, Ransomware).",
              "Bước 3: Hậu quả: Máy tính bị mã hóa đòi tiền chuộc, mất tài khoản ngân hàng và thông tin cá nhân bị đánh cắp."
            ],
            "answer": "Tiềm ẩn nguy cơ lây nhiễm mã độc gián điệp và vi phạm đạo đức số."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng cái gì tìm thấy trên mạng Internet thì đều được phép tải về sử dụng miễn phí tùy tiện.",
            "why": "Tìm thấy công khai không đồng nghĩa với việc được phép sử dụng tự do; tác giả vẫn giữ toàn bộ quyền sở hữu trí tuệ của tác phẩm."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Lập trình Thuật toán cơ bản",
        "description": "Làm quen với ngôn ngữ lập trình trực quan hoặc Python, biến số, kiểu dữ liệu, cấu trúc rẽ nhánh (if - else) và cấu trúc lặp (for, while).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái niệm biến, kiểu dữ liệu và biểu thức điều kiện", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Cấu trúc rẽ nhánh if - else và vòng lặp trong lập trình", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Biến số (Variable)",
            "definition": "Là một vùng nhớ được đặt tên trong bộ nhớ máy tính dùng để lưu trữ giá trị và giá trị này có thể thay đổi được trong quá trình thực hiện chương trình.",
            "example": "Trong Python: diem_so = 8.5; sau đó tăng thêm điểm thưởng: diem_so = diem_so + 1.",
            "essence": "Biến là viên gạch cơ bản nhất để chương trình ghi nhớ và thao tác dữ liệu linh hoạt."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc hoạt động của cấu trúc rẽ nhánh if - else",
            "meaning": "Nếu điều kiện đúng (True) thì thực hiện khối lệnh 1; ngược lại nếu điều kiện sai (False) thì thực hiện khối lệnh 2.",
            "example": "if diem >= 8: print('Xếp loại Giỏi') else: print('Cần cố gắng thêm').",
            "essence": "Giúp chương trình có khả năng tự động đưa ra quyết định thông minh dựa trên dữ liệu đầu vào."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Viết đoạn mã giải thuật tính tổng các số tự nhiên chẵn từ 1 đến 10.",
            "steps": [
              "Bước 1: Khởi tạo biến tổng tong = 0.",
              "Bước 2: Sử dụng vòng lặp duyệt qua các số chẵn: for i in range(2, 11, 2): tong = tong + i.",
              "Bước 3: In kết quả ra màn hình: print('Tổng chẵn là:', tong) => Kết quả là 2 + 4 + 6 + 8 + 10 = 30."
            ],
            "answer": "Tổng các số chẵn từ 1 đến 10 là 30."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lập trình vòng lặp vô tận (Infinite Loop) do quên câu lệnh tăng biến đếm.",
            "why": "Nếu điều kiện lặp luôn đúng và không bao giờ thay đổi, chương trình sẽ chạy mãi mãi làm treo máy tính."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Xử lý và Trình bày thông tin số",
        "description": "Tạo bài trình chiếu đa phương tiện chuyên nghiệp, sử dụng hiệu ứng chuyển trang hợp lý và tạo biểu đồ minh họa số liệu sống động.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Thiết kế trang chiếu đa phương tiện (Hình ảnh, video, âm thanh)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sử dụng hiệu ứng chuyển động và liên kết siêu văn bản", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Liên kết siêu văn bản (Hyperlink)",
            "definition": "Là một đối tượng (từ ngữ, hình ảnh hoặc nút bấm) khi nhấp chuột vào sẽ đưa người dùng chuyển ngay tới một trang chiếu khác, một tệp tin hoặc một trang web trên Internet.",
            "example": "Nút bấm 'Về trang chủ' trên slide cuối giúp người thuyết trình nhảy ngay về trang mục lục.",
            "essence": "Biến bài thuyết trình từ cấu trúc tuần tự tuyến tính thành mạng thông tin đa chiều tương tác sống động."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc 6x6 trong thiết kế slide thuyết trình",
            "meaning": "Mỗi trang chiếu không nên có quá 6 dòng chữ, và mỗi dòng chữ không nên có quá 6 từ; ưu tiên hình ảnh trực quan thay vì chép cả đoạn văn dài.",
            "example": "Dùng từ khóa ngắn gọn và biểu đồ thay vì sao chép nguyên văn sách giáo khoa lên slide.",
            "essence": "Slide là công cụ hỗ trợ người nghe nắm bắt ý chính, không phải là kịch bản để người thuyết trình đọc thuộc lòng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 3 tiêu chí đánh giá một bài thuyết trình điện tử chất lượng cao.",
            "steps": [
              "Bước 1: Nội dung: Cô đọng, súc tích, bám sát chủ đề, thông tin có nguồn gốc rõ ràng.",
              "Bước 2: Hình thức thẩm mỹ: Màu sắc hài hòa (độ tương phản cao giữa chữ và nền), font chữ dễ đọc, cỡ chữ từ 24pt trở lên.",
              "Bước 3: Hiệu ứng: Chừng mực, mượt mà, phục vụ nội dung, không lạm dụng hiệu ứng âm thanh giật gân làm phân tán người nghe."
            ],
            "answer": "Nội dung cô đọng, thẩm mỹ hài hòa và hiệu ứng chuyển động tinh tế."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lạm dụng quá nhiều hiệu ứng bay lượn lấp lánh và âm thanh chói tai cho từng chữ cái.",
            "why": "Gây hoa mắt chóng mặt cho người xem và làm lu mờ nội dung cốt lõi của bài báo cáo."
          }
        ]
      }
    ]
  },

  "giao-duc-cong-dan": {
    "id": "giao-duc-cong-dan",
    "name": "Giáo dục Công dân",
    "icon": "🏛️",
    "chapters": [
      {
        "id": "ch01",
        "title": "Bài 1: Tự hào truyền thống dân tộc Việt Nam",
        "description": "Giá trị truyền thống yêu nước, bất khuất, đoàn kết, nhân nghĩa, cần cù và trách nhiệm của thế hệ trẻ trong thời kỳ hội nhập quốc tế.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khám phá những truyền thống vẻ vang của dân tộc", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Trách nhiệm giữ gìn và phát huy bản sắc văn hóa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bản sắc văn hóa dân tộc",
            "definition": "Là những nét đặc trưng văn hóa độc đáo, bền vững được hun đúc qua hàng nghìn năm lịch sử, phản ánh tâm hồn, cốt cách và trí tuệ của con người Việt Nam.",
            "example": "Tà áo dài duyên dáng, truyền thuyết con Rồng cháu Tiên, ngày Giỗ Tổ Hùng Vương, tinh thần tương thân tương ái 'Lá lành đùm lá rách'.",
            "essence": "Bản sắc văn hóa là căn cước công dân của một dân tộc trên trường quốc tế: 'Hòa nhập nhưng không hòa tan'."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc tiếp thu tinh hoa văn hóa nhân loại",
            "meaning": "Chủ động học hỏi các giá trị khoa học, công nghệ và văn minh hiện đại của thế giới nhưng trên nền tảng chọn lọc, giữ vững thuần phong mỹ tục dân tộc.",
            "example": "Học giỏi tiếng Anh và ứng dụng công nghệ số để quảng bá văn hóa ẩm thực, âm nhạc dân tộc Việt Nam ra thế giới.",
            "essence": "Tự tin bước ra thế giới với bản lĩnh và niềm tự hào nguồn cội văn hóa ngàn năm."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một số bạn trẻ có thái độ sính ngoại quá mức, coi thường các lễ hội dân gian truyền thống. Em suy nghĩ như thế nào về hiện tượng này?",
            "steps": [
              "Bước 1: Nhận định: Đây là biểu hiện lệch lạc về nhận thức, thiếu hiểu biết về cội nguồn và đánh mất bản sắc cá nhân.",
              "Bước 2: Phân tích hậu quả: Làm mai một các giá trị di sản văn hóa phi vật thể quý báu của tổ tiên.",
              "Bước 3: Giải pháp: Cần đổi mới cách tổ chức lễ hội truyền thống hấp dẫn hơn, tăng cường giáo dục trải nghiệm di sản văn hóa cho học sinh."
            ],
            "answer": "Cần phê phán lối sống sính ngoại tiêu cực và tích cực tìm hiểu để yêu quý di sản văn hóa dân tộc."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Bảo thủ, từ chối mọi yếu tố văn hóa mới của nhân loại vì cho rằng sẽ làm mất truyền thống.",
            "why": "Truyền thống không phải là bất biến đóng kín; truyền thống cần tiếp thu tinh hoa mới để làm giàu thêm bản sắc văn hóa dân tộc."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Bài 2: Tôn trọng sự đa dạng của các dân tộc",
        "description": "Ý nghĩa của việc tôn trọng văn hóa, phong tục, ngôn ngữ của các dân tộc anh em trên đất nước Việt Nam và các dân tộc trên thế giới.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sự phong phú, đa dạng của các nền văn hóa", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tôn trọng và ứng xử văn minh trước sự khác biệt văn hóa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bình đẳng giữa các dân tộc",
            "definition": "Mọi dân tộc dù số lượng người đông hay ít đều có quyền bình đẳng về chính trị, kinh tế, văn hóa, giáo dục và được Nhà nước tôn trọng, bảo vệ.",
            "example": "Con em đồng bào các dân tộc thiểu số được Nhà nước hỗ trợ học bổng, bảo tồn chữ viết và tiếng nói mẹ đẻ.",
            "essence": "54 dân tộc anh em là một khối đại đoàn kết thống nhất không thể tách rời của đại gia đình Việt Nam."
          }
        ],
        "rules": [
          {
            "statement": "Hành vi nghiêm cấm đối với vấn đề dân tộc",
            "meaning": "Nghiêm cấm mọi hành vi kỳ thị, chia rẽ, miệt thị vùng miền hoặc xúc phạm phong tục tập quán, tín ngưỡng của các dân tộc khác.",
            "example": "Không trêu chọc, nhại giọng nói địa phương hay bêu xấu trang phục của các bạn học sinh dân tộc thiểu số.",
            "essence": "Tôn trọng sự khác biệt là thước đo nhân cách của con người có văn hóa trong xã hội hiện đại."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Khi đi du lịch đến vùng cao Tây Bắc và tham quan bản làng của người dân tộc H'Mông, em cần lưu ý những nét văn minh ứng xử nào?",
            "steps": [
              "Bước 1: Xin phép trước khi chụp ảnh người già hoặc trẻ nhỏ trong bản làng.",
              "Bước 2: Tìm hiểu và tuân thủ các kiêng kị văn hóa (không chỉ tay vào bàn thờ tổ tiên, không ngồi ở gian giữa linh thiêng).",
              "Bước 3: Tôn trọng môi trường cảnh quan, không vứt rác bừa bãi và ủng hộ các sản phẩm thủ công thổ cẩm truyền thống của bà con."
            ],
            "answer": "Ứng xử lịch thiệp, tôn trọng phong tục địa phương và bảo vệ môi trường du lịch."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đánh giá phong tục tập quán của dân tộc khác bằng chuẩn mực cá nhân của mình rồi chê bai là kỳ quặc.",
            "why": "Mỗi nền văn hóa có lịch sử hình thành và giá trị nhân văn riêng; không có nền văn hóa nào cao hơn hay thấp hơn nền văn hóa nào."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Bài 3: Lao động cần cù, sáng tạo",
        "description": "Giá trị của lao động, biểu hiện của sự cần cù và tinh thần sáng tạo, phê phán thói lười biếng, ỷ lại và học vẹt thụ động.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Ý nghĩa của lao động cần cù và tinh thần sáng tạo", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Rèn luyện tính cần cù, sáng tạo trong học tập và đời sống", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Lao động sáng tạo",
            "definition": "Là luôn suy nghĩ, cải tiến, tìm tòi phương pháp mới, cách làm mới để nâng cao năng suất, chất lượng và hiệu quả công việc mà tốn ít sức lực nhất.",
            "example": "Học sinh tự sáng tạo ra sơ đồ tư duy (Mindmap) nhiều màu sắc để ghi nhớ nhanh các bài học môn Sinh học.",
            "essence": "Cần cù là nền tảng kiên trì; sáng tạo là đôi cánh đưa năng suất lao động bứt phá đỉnh cao."
          }
        ],
        "rules": [
          {
            "statement": "Mối quan hệ giữa Cần cù và Sáng tạo",
            "meaning": "Cần cù và sáng tạo là hai mặt không thể tách rời: Có cần cù tích lũy kiến thức mới nảy sinh ý tưởng sáng tạo; có sáng tạo mới giải phóng con người khỏi sự vất vả cơ bắp.",
            "example": "Bác học Thomas Edison từng nói: 'Thiên tài là 1% cảm hứng và 99% mồ hôi nước mắt'.",
            "essence": "Không có sự sáng tạo nào tự nhiên rơi xuống đầu người lười biếng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Học sinh lớp 8 có thể rèn luyện tính sáng tạo trong học tập như thế nào mỗi ngày?",
            "steps": [
              "Bước 1: Không thỏa mãn với một cách giải duy nhất: Luôn tìm tòi thêm 2-3 cách giải khác ngắn gọn, thông minh hơn cho một bài toán.",
              "Bước 2: Ứng dụng công nghệ: Sử dụng các phần mềm mô phỏng 3D, ứng dụng flashcard để học từ vựng tiếng Anh chủ động.",
              "Bước 3: Liên hệ thực tế: Đặt câu hỏi 'Kiến thức bài này giúp giải quyết vấn đề gì trong cuộc sống xung quanh mình?'."
            ],
            "answer": "Chủ động tìm kiếm giải pháp mới, ứng dụng công nghệ và liên hệ kiến thức với thực tiễn."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng sáng tạo là năng khiếu bẩm sinh chỉ dành cho các thiên tài, người bình thường không làm được.",
            "why": "Sáng tạo là một kỹ năng có thể rèn luyện được thông qua thói quen quan sát tinh tế, tò mò khoa học và không ngại thất bại."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Bài 4: Bảo vệ Môi trường và Tài nguyên thiên nhiên",
        "description": "Tầm quan trọng của môi trường và tài nguyên, quy định pháp luật về bảo vệ môi trường, phân loại rác thải tại nguồn và lối sống xanh.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Thực trạng môi trường, tài nguyên và quy định của pháp luật", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hành động thiết thực bảo vệ môi trường và ứng phó biến đổi khí hậu", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Kinh tế tuần hoàn (Circular Economy)",
            "definition": "Là mô hình kinh tế trong đó các chất thải được thu hồi, tái chế và tái sử dụng liên tục để làm nguyên liệu đầu vào cho sản phẩm mới, giảm thiểu tối đa rác thải xả ra tự nhiên.",
            "example": "Tái chế chai nhựa PET đã qua sử dụng thành sợi dệt may áo thể thao hoặc túi xách thời trang bền đẹp.",
            "essence": "Biến rác thải của chu trình này thành nguồn tài nguyên quý giá của chu trình tiếp theo."
          }
        ],
        "rules": [
          {
            "statement": "Trách nhiệm pháp lý về bảo vệ môi trường của công dân",
            "meaning": "Mọi công dân có nghĩa vụ giữ gìn vệ sinh nơi công cộng, phân loại rác thải tại nguồn, tố cáo các hành vi xả thải độc hại và bồi thường thiệt hại nếu gây ô nhiễm môi trường.",
            "example": "Nghiêm cấm xả nước thải chưa qua xử lý ra sông suối; cấm đốt rác thải sinh hoạt bừa bãi gây khói độc.",
            "essence": "Bảo vệ môi trường là bảo vệ chính mạng sống và tương lai của con cháu chúng ta."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Hướng dẫn các bước phân loại rác thải sinh hoạt 3 nhóm tại gia đình và trường học chuẩn quy định mới.",
            "steps": [
              "Bước 1: Rác hữu cơ dễ phân hủy (thức ăn thừa, vỏ rau củ quả, lá cây): Dùng làm phân bón hữu cơ ủ gốc cây.",
              "Bước 2: Rác tái chế (giấy vụn, vỏ lon kim loại, chai nhựa sạch, bìa carton): Thu gom bán ve chai hoặc chuyển nhà máy tái chế.",
              "Bước 3: Rác còn lại / Rác nguy hại (túi nilon bẩn, pin cũ, bóng đèn vỡ): Đựng túi riêng đưa cho đơn vị thu gom xử lý chuyên biệt."
            ],
            "answer": "Phân chia đúng 3 nhóm giúp giảm 70% lượng rác chôn lấp và tiết kiệm tài nguyên quốc gia."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Vứt pin cũ đã qua sử dụng chung với rác thải sinh hoạt thông thường.",
            "why": "Một viên pin cũ rò rỉ ra môi trường có thể làm ô nhiễm 500 lít nước ngầm hoặc 1m3 đất suốt 50 năm do chứa kim loại nặng cực độc (thủy ngân, chì, cadimi)."
          }
        ]
      }
    ]
  },

  "cong-nghe": {
    "id": "cong-nghe",
    "name": "Công nghệ",
    "icon": "⚙️",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Bản vẽ Kỹ thuật cơ khí",
        "description": "Tiêu chuẩn trình bày bản vẽ kỹ thuật, hình chiếu vuông góc của các khối đa diện, khối tròn xoay và đọc bản vẽ chi tiết đơn giản.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tiêu chuẩn bản vẽ và hình chiếu các khối hình học", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Đọc bản vẽ chi tiết và bản vẽ lắp đơn giản", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bản vẽ chi tiết",
            "definition": "Là tài liệu kỹ thuật thể hiện đầy đủ hình dạng, kích thước, yêu cầu kỹ thuật và vật liệu của một chi tiết máy đơn lẻ dùng để chế tạo và kiểm tra.",
            "example": "Bản vẽ chế tạo bu lông, đai ốc, trục truyền động máy tiện.",
            "essence": "Bản vẽ chi tiết là bản thiết kế hướng dẫn trực tiếp cho người thợ gia công trên máy công cụ."
          }
        ],
        "rules": [
          {
            "statement": "Trình tự 4 bước đọc bản vẽ chi tiết chuẩn kỹ thuật",
            "meaning": "Bước 1: Đọc khung tên (tên chi tiết, vật liệu, tỉ lệ) -> Bước 2: Đọc hình biểu diễn (tên các hình chiếu, hình cắt) -> Bước 3: Đọc kích thước (kích thước chung và chi tiết) -> Bước 4: Đọc yêu cầu kỹ thuật và tổng hợp.",
            "example": "Tuân thủ đúng trình tự giúp không bỏ sót thông tin kích thước dung sai quan trọng của chi tiết máy.",
            "essence": "Đọc bản vẽ có phương pháp đảm bảo độ chính xác tuyệt đối trong sản xuất công nghiệp."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu ý nghĩa của con số ghi tỉ lệ 1:2 và 2:1 trên khung tên bản vẽ kỹ thuật.",
            "steps": [
              "Bước 1: Tỉ lệ 1:2 là tỉ lệ thu nhỏ: Kích thước hình vẽ trên giấy bằng một nửa kích thước thực tế của chi tiết ngoài đời.",
              "Bước 2: Tỉ lệ 2:1 là tỉ lệ phóng to: Kích thước hình vẽ trên giấy gấp đôi kích thước thực tế (thường dùng cho chi tiết đồng hồ, vi mạch nhỏ).",
              "Bước 3: Lưu ý: Dù vẽ theo tỉ lệ nào thì con số kích thước ghi trên bản vẽ LUÔN LÀ KÍCH THƯỚC THỰC của vật thể."
            ],
            "answer": "1:2 là thu nhỏ, 2:1 là phóng to; số đo kích thước ghi trên bản vẽ luôn là giá trị thực."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy thước đo trực tiếp trên giấy rồi coi đó là kích thước thực của chi tiết khi vẽ theo tỉ lệ phóng to/thu nhỏ.",
            "why": "Phải căn cứ vào con số kích thước được ghi bằng số trên đường gióng kích thước, không được đo trực tiếp bằng thước dây trên hình vẽ."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Cơ khí và Gia công cơ khí bằng tay",
        "description": "Vật liệu cơ khí (kim loại, phi kim), các dụng cụ cầm tay (dụng cụ đo, cưa, đục, dũa) và quy tắc an toàn lao động trong xưởng cơ khí.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vật liệu cơ khí và dụng cụ gia công cầm tay", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Kỹ thuật cưa, đục, dũa và an toàn lao động cơ khí", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thước cặp (Vernier Caliper)",
            "definition": "Là dụng cụ đo cơ khí chính xác dùng để đo kích thước ngoài (độ dày, đường kính ngoài), kích thước trong (đường kính lỗ) và độ sâu của các lỗ, rãnh với độ chính xác đến 0,1mm hoặc 0,02mm.",
            "example": "Đo đường kính ngoài của một thanh cốt thép hoặc đường kính trong của ống nước sắt.",
            "essence": "Dụng cụ đo không thể thiếu đảm bảo độ chính xác lắp ghép của các chi tiết máy."
          }
        ],
        "rules": [
          {
            "statement": "Tư thế đứng và thao tác dũa kim loại chuẩn xác",
            "meaning": "Đứng chân trước chân sau vững chắc tạo góc 75 độ; khi đẩy dũa về phía trước ấn lực đều hai tay để cắt phoi; khi kéo dũa về không ấn lực để tránh mòn răng dũa.",
            "example": "Mặt dũa phải luôn giữ song song với mặt phẳng gia công để phôi sắt phẳng lì không bị lượn sóng.",
            "essence": "Phối hợp nhịp nhàng giữa lực tay và trọng tâm cơ thể tạo nên độ phẳng tinh xảo của bề mặt kim loại."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày 3 quy tắc an toàn tính mạng bắt buộc khi làm việc trong xưởng thực hành cơ khí.",
            "steps": [
              "Bước 1: Trang phục bảo hộ: Mặc quần áo bảo hộ gọn gàng, đi giày mũi sắt chống đinh, đeo kính bảo hộ bảo vệ mắt khỏi mạt sắt bắn.",
              "Bước 2: Sử dụng dụng cụ: Kiểm tra cán búa, cán dũa phải chắc chắn không lỏng lẻo; kẹp chặt phôi trên ê-tô trước khi cưa, đục.",
              "Bước 3: Vệ sinh an toàn: Không dùng tay gạt mạt sắt (phải dùng chổi quét); không đùa nghịch, xô đẩy trong khu vực máy móc đang hoạt động."
            ],
            "answer": "Mặc đồ bảo hộ, kẹp chặt phôi bằng ê-tô và dùng chổi quét mạt sắt bảo vệ an toàn."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Dùng tay không quẹt mạt sắt dính trên bề mặt kim loại vừa gia công.",
            "why": "Mạt sắt rất sắc nhọn và có nhiệt độ cao dễ găm sâu vào da tay gây nhiễm trùng, đứt tay nghiêm trọng."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Kỹ thuật Điện và An toàn điện gia dụng",
        "description": "Nguyên nhân gây tai nạn điện, các biện pháp an toàn khi sử dụng điện, sơ cứu người bị điện giật và các thiết bị đóng cắt, lấy điện trong gia đình.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: An toàn điện và các biện pháp phòng tránh tai nạn điện", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các thiết bị bảo vệ và đóng cắt trong mạng điện gia đình", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Aptomat (Cầu dao tự động - MCB/ELCB)",
            "definition": "Là thiết bị điện đóng cắt tự động dùng để ngắt mạch điện ngay lập tức khi xảy ra sự cố quá tải, ngắn mạch (chập điện) hoặc rò rỉ điện, bảo vệ an toàn cho thiết bị và con người.",
            "example": "Khi dây điện trong nhà bị chập tóe lửa, Aptomat lập tức tự động 'nhảy' ngắt nguồn điện trong vòng vài phần nghìn giây.",
            "essence": "Lá chắn an toàn tối thượng phòng chống cháy nổ và điện giật trong ngôi nhà hiện đại."
          }
        ],
        "rules": [
          {
            "statement": "Quy trình sơ cứu khẩn cấp người bị điện giật",
            "meaning": "Bước 1: Lập tức ngắt cầu dao/công tắc điện gần nhất hoặc dùng vật cách điện khô (gậy gỗ, thanh nhựa) gạt dây điện ra khỏi người nạn nhân -> Bước 2: Đưa nạn nhân ra nơi thoáng khí -> Bước 3: Nếu ngừng thở phải hô hấp nhân tạo, ép tim ngoài lồng ngực và gọi cấp cứu 115.",
            "example": "Tuyệt đối không dùng tay không chạm trực tiếp vào người nạn nhân khi nguồn điện chưa được ngắt.",
            "essence": "Hành động nhanh chóng và cách điện an toàn quyết định mạng sống của người bị nạn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao các thiết bị điện có vỏ kim loại (tủ lạnh, máy giặt, bình nóng lạnh) bắt buộc phải có dây nối đất an toàn (dây tiếp địa)?",
            "steps": [
              "Bước 1: Khi thiết bị sử dụng lâu ngày bị ẩm ướt hoặc chuột cắn dây làm rò điện ra vỏ kim loại.",
              "Bước 2: Nếu không có dây tiếp địa, người chạm vào vỏ kim loại sẽ bị điện giật truyền qua cơ thể xuống đất.",
              "Bước 3: Khi có dây tiếp địa, điện trở của dây đồng tiếp địa rất nhỏ (dưới 4 Ohm) nên dòng điện rò sẽ lập tức truyền an toàn xuống đất làm nhảy Aptomat bảo vệ người dùng."
            ],
            "answer": "Dây tiếp địa triệt tiêu dòng điện rò rỉ ra vỏ kim loại, bảo vệ an toàn tuyệt đối cho người dùng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lao vào dùng tay không kéo người bị điện giật ra.",
            "why": "Dòng điện sẽ lập tức truyền qua người nạn nhân sang người cứu hộ khiến cả hai cùng bị điện giật nguy kịch. Phải luôn ngắt điện hoặc dùng vật cách điện khô."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Mạch điện điều khiển và Công nghệ thông minh",
        "description": "Cấu trúc mạch điện điều khiển, các cảm biến thông dụng (cảm biến ánh sáng, cảm biến nhiệt độ, cảm biến chuyển động) và lắp ráp mạch điện thông minh đơn giản.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cấu trúc mạch điện điều khiển và các linh kiện cảm biến", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành lắp ráp mạch điện điều khiển tự động đơn giản", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Cảm biến quang (LDR - Quang điện trở)",
            "definition": "Là linh kiện điện tử có giá trị điện trở thay đổi theo cường độ ánh sáng chiếu vào: Khi trời sáng điện trở giảm mạnh, khi trời tối điện trở tăng rất cao.",
            "example": "Đèn đường thông minh tự động bật sáng khi trời tối và tự động tắt khi trời sáng nhờ cảm biến quang LDR.",
            "essence": "Chuyển hóa tín hiệu quang học của môi trường thành tín hiệu điện để mạch vi xử lý điều khiển cơ cấu chấp hành."
          }
        ],
        "rules": [
          {
            "statement": "Cấu trúc 3 khối của một mạch điện điều khiển tự động",
            "meaning": "Khối cảm biến (thu nhận tín hiệu môi trường) -> Khối xử lý tín hiệu (so sánh và khuếch đại dòng điện) -> Khối chấp hành (rơ-le, bóng đèn, còi báo, động cơ).",
            "example": "Cảm biến hồng ngoại phát hiện người đến -> Mạch kích mở transistor -> Rơ-le bật sáng bóng đèn cầu thang.",
            "essence": "Nguyên lý tự động hóa khép kín: Cảm nhận -> Quyết định -> Hành động."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Mô tả nguyên lý hoạt động của mạch đèn báo cháy tự động sử dụng cảm biến nhiệt độ.",
            "steps": [
              "Bước 1: Khi nhiệt độ phòng tăng cao đột ngột (do có đám cháy), cảm biến nhiệt độ (Thermistor) giảm điện trở nhanh chóng.",
              "Bước 2: Điện áp đưa vào chân điều khiển của transistor tăng lên vượt ngưỡng mở mạch.",
              "Bước 3: Transistor dẫn dòng kích hoạt rơ-le đóng tiếp điểm cấp điện cho còi hú và đèn chớp báo động người dân sơ tán."
            ],
            "answer": "Nhiệt độ cao làm giảm điện trở cảm biến -> Kích mở transistor -> Còi báo động hú cảnh báo cháy."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cắm ngược cực tính dương (+) và âm (-) của linh kiện bán dẫn như diode hoặc LED.",
            "why": "Diode và LED chỉ cho dòng điện đi qua theo một chiều duy nhất (từ Anode sang Cathode); cắm ngược cực đèn sẽ không sáng hoặc có thể bị đánh thủng cháy hỏng."
          }
        ]
      }
    ]
  }
}

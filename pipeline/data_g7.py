# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa 8 môn học Lớp 7 SGK Kết nối tri thức với cuộc sống 2026-2027:
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

GRADE_07_SUBJECTS = {
  "toan": {
    "id": "toan",
    "name": "Toán học",
    "icon": "📐",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Số hữu tỉ",
        "description": "Tập hợp các số hữu tỉ, các phép tính cộng, trừ, nhân, chia, lũy thừa với số mũ tự nhiên của số hữu tỉ và quy tắc dấu ngoặc.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tập hợp các số hữu tỉ và biểu diễn trên trục số", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các phép tính với số hữu tỉ và lũy thừa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Số hữu tỉ",
            "definition": "Là số viết được dưới dạng phân số a/b với a, b thuộc tập hợp số nguyên Z và b khác 0. Kí hiệu tập hợp các số hữu tỉ là Q.",
            "example": "-0,5 = -1/2; 2 1/3 = 7/3; 0 = 0/1; -5 = -5/1 đều là các số hữu tỉ.",
            "essence": "Mọi số nguyên, phân số và số thập phân hữu hạn hoặc vô hạn tuần hoàn đều là các số hữu tỉ."
          },
          {
            "term": "Số đối của số hữu tỉ",
            "definition": "Hai số hữu tỉ có điểm biểu diễn trên trục số nằm về hai phía so với điểm gốc 0 và cách đều điểm 0 gọi là hai số đối nhau. Số đối của x là -x.",
            "example": "Số đối của 3/4 là -3/4; số đối của -2,5 là 2,5; số đối của 0 là chính nó (0).",
            "essence": "Tổng của hai số hữu tỉ đối nhau luôn luôn bằng 0: x + (-x) = 0."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc dấu ngoặc và chuyển vế đối với số hữu tỉ",
            "meaning": "Khi bỏ dấu ngoặc có dấu '-' đằng trước, ta phải đổi dấu tất cả các số hạng trong ngoặc. Khi chuyển một số hạng từ vế này sang vế kia của một đẳng thức, ta phải đổi dấu số hạng đó.",
            "example": "a - (b - c) = a - b + c. Nếu x - 1/3 = 5/6 thì x = 5/6 + 1/3.",
            "essence": "Dấu '-' trước ngoặc đảo ngược toàn bộ chiều biến thiên của các số hạng bên trong."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tính giá trị biểu thức: A = 3/4 + (-1/2) * (8/3 - 2/3).",
            "steps": [
              "Bước 1: Thực hiện phép tính trong ngoặc: 8/3 - 2/3 = 6/3 = 2.",
              "Bước 2: Thực hiện phép nhân trước: (-1/2) * 2 = -1.",
              "Bước 3: Thực hiện phép cộng: A = 3/4 + (-1) = 3/4 - 4/4 = -1/4."
            ],
            "answer": "A = -1/4"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên đổi dấu các số hạng bên trong khi bỏ dấu ngoặc có dấu trừ đằng trước.",
            "why": "Viết a - (b - c) thành a - b - c là sai; dấu trừ phía trước áp dụng cho cả biểu thức nên -(-c) biến thành +c."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Số thực và Căn bậc hai số học",
        "description": "Số vô tỉ, căn bậc hai số học của một số không âm, tập hợp số thực R và giá trị tuyệt đối của một số thực.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Số vô tỉ và căn bậc hai số học", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tập hợp số thực và giá trị tuyệt đối", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Căn bậc hai số học",
            "definition": "Căn bậc hai số học của số a không âm là số x không âm sao cho x bình phương bằng a. Kí hiệu là căn bậc hai của a.",
            "example": "Căn bậc hai số học của 25 là 5 (vì 5 >= 0 và 5^2 = 25); căn bậc hai của 0 là 0.",
            "essence": "Căn bậc hai số học luôn là một giá trị không âm: căn(a) >= 0 với mọi a >= 0."
          },
          {
            "term": "Số vô tỉ",
            "definition": "Là số viết được dưới dạng số thập phân vô hạn không tuần hoàn. Tập hợp các số vô tỉ kí hiệu là I.",
            "example": "Số pi = 3,14159265...; căn(2) = 1,41421356... đều là các số vô tỉ.",
            "essence": "Số vô tỉ lấp đầy những 'khoảng trống' trên trục số mà các số hữu tỉ không thể biểu diễn được."
          }
        ],
        "rules": [
          {
            "statement": "Định nghĩa giá trị tuyệt đối của số thực",
            "meaning": "|x| = x nếu x >= 0 và |x| = -x nếu x < 0. Giá trị tuyệt đối của mọi số thực luôn không âm.",
            "example": "|-3,5| = 3,5; |pi| = pi; |0| = 0.",
            "essence": "Giá trị tuyệt đối biểu thị khoảng cách hình học từ điểm biểu diễn số x đến điểm gốc 0 trên trục số."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tìm x biết: |x - 1,5| = 2,5.",
            "steps": [
              "Bước 1: Chia hai trường hợp do tính chất giá trị tuyệt đối: x - 1,5 = 2,5 hoặc x - 1,5 = -2,5.",
              "Bước 2: Trường hợp 1: x = 2,5 + 1,5 = 4.",
              "Bước 3: Trường hợp 2: x = -2,5 + 1,5 = -1."
            ],
            "answer": "x thuộc {4; -1}"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Viết căn(a^2) = a mà không xét điều kiện dấu của a.",
            "why": "Đúng ra căn(a^2) = |a|. Nếu a âm, ví dụ a = -3 thì căn((-3)^2) = căn(9) = 3 = |-3|, không thể bằng -3."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Góc và Đường thẳng song song",
        "description": "Các góc ở vị trí đặc biệt (kề bù, so le trong, đồng vị), tia phân giác của một góc và dấu hiệu nhận biết hai đường thẳng song song.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Các góc ở vị trí đặc biệt và tia phân giác", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hai đường thẳng song song và tiên đề Euclid", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hai góc đối đỉnh",
            "definition": "Là hai góc mà mỗi cạnh của góc này là tia đối của một cạnh của góc kia. Hai góc đối đỉnh thì bằng nhau.",
            "example": "Hai đường thẳng xx' và yy' cắt nhau tại O tạo ra cặp góc xOy và x'Oy' đối đỉnh và bằng nhau.",
            "essence": "Phép đối đỉnh bảo toàn độ lớn góc qua tâm đối xứng là giao điểm của hai đường thẳng."
          }
        ],
        "rules": [
          {
            "statement": "Dấu hiệu nhận biết hai đường thẳng song song",
            "meaning": "Nếu một đường thẳng cắt hai đường thẳng phân biệt và tạo thành một cặp góc so le trong bằng nhau (hoặc đồng vị bằng nhau) thì hai đường thẳng đó song song.",
            "example": "Đường thẳng c cắt a và b, góc A1 so le trong với góc B1 và A1 = B1 = 60 độ => a // b.",
            "essence": "Góc so le trong bằng nhau đảm bảo độ nghiêng của hai đường thẳng so với cát tuyến là hoàn toàn như nhau."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho hai đường thẳng song song a và b. Một cát tuyến c cắt a tại A và b tại B. Biết góc A1 = 70 độ. Tính số đo góc trong cùng phía B2.",
            "steps": [
              "Bước 1: Do a // b, hai góc trong cùng phía có tổng số đo bằng 180 độ.",
              "Bước 2: Ta có: A1 + B2 = 180 độ.",
              "Bước 3: Suy ra: B2 = 180 độ - 70 độ = 110 độ."
            ],
            "answer": "Góc B2 = 110 độ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa cặp góc so le trong bằng nhau và cặp góc trong cùng phía bù nhau.",
            "why": "Góc so le trong thì bằng nhau (A1 = B1), còn hai góc trong cùng phía thì bù nhau có tổng bằng 180 độ (A1 + B2 = 180 độ)."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Tam giác bằng nhau",
        "description": "Tổng ba góc trong một tam giác, các trường hợp bằng nhau của hai tam giác: c-c-c, c-g-c, g-c-g và tam giác cân.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tổng ba góc và trường hợp bằng nhau c-c-c, c-g-c", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Trường hợp bằng nhau g-c-g và tính chất tam giác cân", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tam giác cân",
            "definition": "Là tam giác có hai cạnh bằng nhau. Hai góc ở đáy của tam giác cân thì bằng nhau.",
            "example": "Tam giác ABC có AB = AC là tam giác cân tại A; khi đó góc B = góc C.",
            "essence": "Tam giác cân sở hữu tính chất đối xứng trục qua đường phân giác của góc ở đỉnh."
          }
        ],
        "rules": [
          {
            "statement": "Định lí tổng ba góc trong một tam giác",
            "meaning": "Tổng số đo ba góc trong một tam giác luôn bằng 180 độ.",
            "example": "Tam giác ABC có góc A = 80 độ, góc B = 60 độ thì góc C = 180 - (80 + 60) = 40 độ.",
            "essence": "Định lí này xuất phát từ tiên đề Euclid về đường thẳng song song qua đỉnh tam giác."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho tam giác ABC cân tại A có góc A = 50 độ. Tính số đo góc B và góc C ở đáy.",
            "steps": [
              "Bước 1: Do tam giác ABC cân tại A nên góc B = góc C.",
              "Bước 2: Tổng ba góc: góc A + góc B + góc C = 180 độ => 2 * góc B = 180 độ - góc A.",
              "Bước 3: Thay số: 2 * góc B = 180 - 50 = 130 độ => góc B = góc C = 65 độ."
            ],
            "answer": "Góc B = góc C = 65 độ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Áp dụng trường hợp c-g-c khi góc không xen giữa hai cạnh bằng nhau.",
            "why": "Để hai tam giác bằng nhau theo c-g-c, góc bằng nhau bắt buộc phải là góc xen giữa hai cặp cạnh tương ứng bằng nhau."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Thu thập và Biểu diễn dữ liệu",
        "description": "Thu thập, phân loại dữ liệu, biểu diễn dữ liệu trên bảng, biểu đồ đoạn thẳng và biểu đồ hình quạt tròn.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Thu thập và phân loại dữ liệu thống kê", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Biểu đồ đoạn thẳng và biểu đồ hình quạt tròn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Biểu đồ hình quạt tròn",
            "definition": "Là biểu đồ dùng hình tròn được chia thành các hình quạt để biểu diễn tỉ lệ phần trăm của từng loại số liệu so với toàn thể.",
            "example": "Biểu diễn cơ cấu học lực lớp 7A: Giỏi 40%, Khá 35%, Đạt 25% trên một hình tròn 360 độ.",
            "essence": "Hình quạt tròn giúp người xem so sánh trực quan quy mô thành phần trong tổng thể 100%."
          }
        ],
        "rules": [
          {
            "statement": "Mối quan hệ giữa phần trăm và số đo góc ở tâm hình quạt tròn",
            "meaning": "1% tương ứng với góc ở tâm 3,6 độ (360 độ / 100). Muốn vẽ hình quạt biểu diễn p%, góc ở tâm là p * 3,6 độ.",
            "example": "Dữ liệu 25% tương ứng với góc ở tâm bằng 25 * 3,6 = 90 độ (một phần tư hình tròn).",
            "essence": "Quy đổi tỉ lệ phần trăm thành góc hình học đảm bảo độ chính xác của biểu đồ thống kê."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một nhóm học sinh có 40 bạn gồm: 16 bạn thích bóng đá, 12 bạn thích cầu lông, 8 bạn thích bơi lội, 4 bạn thích cờ vua. Tính tỉ lệ phần trăm bạn thích bóng đá.",
            "steps": [
              "Bước 1: Xác định tổng số học sinh là 40 bạn.",
              "Bước 2: Lấy số bạn thích bóng đá chia cho tổng số: 16 / 40 = 0,4.",
              "Bước 3: Nhân với 100%: 0,4 * 100% = 40%."
            ],
            "answer": "Tỉ lệ thích bóng đá là 40%."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Tổng các phần trăm trong biểu đồ hình quạt tròn không bằng 100%.",
            "why": "Toàn bộ hình tròn tượng trưng cho 100% dữ liệu khảo sát; tổng các thành phần phải luôn luôn bằng 100%."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Biểu thức đại số và Đa thức một biến",
        "description": "Biểu thức đại số, đa thức một biến, cộng trừ đa thức một biến và nghiệm của đa thức một biến.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái niệm biểu thức đại số và đa thức một biến", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phép cộng, trừ đa thức và nghiệm của đa thức", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Nghiệm của đa thức một biến",
            "definition": "Nếu tại x = a, đa thức P(x) có giá trị bằng 0 (P(a) = 0) thì ta nói a là một nghiệm của đa thức P(x).",
            "example": "Đa thức P(x) = 2x - 6 có nghiệm x = 3 vì P(3) = 2*3 - 6 = 0.",
            "essence": "Nghiệm là giá trị của biến số làm cho biểu thức triệt tiêu hoàn toàn."
          }
        ],
        "rules": [
          {
            "statement": "Bậc của đa thức một biến",
            "meaning": "Bậc của đa thức một biến (khác đa thức không, đã thu gọn) là số mũ lớn nhất của biến trong đa thức đó.",
            "example": "Đa thức P(x) = 5x^4 - 2x^2 + 7 có bậc là 4; hệ số cao nhất là 5, hệ số tự do là 7.",
            "essence": "Bậc của đa thức quyết định số lượng nghiệm tối đa của đa thức đó."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho P(x) = 3x^2 - 5x + 2. Kiểm tra xem x = 1 có phải là nghiệm của P(x) không?",
            "steps": [
              "Bước 1: Thay x = 1 vào biểu thức P(x).",
              "Bước 2: Tính toán: P(1) = 3*(1)^2 - 5*(1) + 2 = 3 - 5 + 2 = 0.",
              "Bước 3: Do P(1) = 0, kết luận x = 1 là một nghiệm của đa thức P(x)."
            ],
            "answer": "x = 1 là nghiệm của P(x)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Xác định bậc của đa thức khi đa thức chưa được thu gọn các hạng tử đồng dạng.",
            "why": "Nếu đa thức là P(x) = x^3 - x^3 + 2x + 1 thì x^3 đã triệt tiêu, bậc thực tế của đa thức chỉ là 1 chứ không phải 3."
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
        "title": "Chương 1: Nguyên tử và Bảng tuần hoàn",
        "description": "Mô hình nguyên tử Rutherford - Bohr, cấu tạo hạt proton, neutron, electron và nguyên tắc sắp xếp các nguyên tố trong bảng tuần hoàn hóa học.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cấu tạo nguyên tử và khối lượng nguyên tử", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Bảng tuần hoàn các nguyên tố hóa học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hạt nhân nguyên tử",
            "definition": "Nằm ở tâm nguyên tử, mang điện tích dương, gồm các hạt proton (mang điện tích +1) và hạt neutron (không mang điện).",
            "example": "Hạt nhân nguyên tử Carbon có 6 proton và 6 neutron, tạo nên điện tích hạt nhân là +6.",
            "essence": "Hầu như toàn bộ khối lượng của nguyên tử tập trung ở hạt nhân vì khối lượng electron vô cùng nhỏ bé."
          },
          {
            "term": "Bảng tuần hoàn các nguyên tố hóa học",
            "definition": "Gồm các nguyên tố sắp xếp theo chiều tăng dần của điện tích hạt nhân, chia thành ô nguyên tố, chu kì (hàng ngang) và nhóm (cột dọc).",
            "example": "Chu kì 2 gồm các nguyên tố có 2 lớp electron (Lithium đến Neon); Nhóm IA gồm các kim loại kiềm có 1 electron lớp ngoài cùng.",
            "essence": "Các nguyên tố trong cùng một nhóm có cấu hình electron lớp ngoài cùng tương tự nhau nên có tính chất hóa học tương tự nhau."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tử trung hòa về điện",
            "meaning": "Trong một nguyên tử bất kỳ, số hạt proton mang điện tích dương luôn luôn bằng số hạt electron mang điện tích âm: Số p = Số e.",
            "example": "Nguyên tử Sodium (Na) có 11 proton thì bắt buộc phải có đúng 11 electron chuyển động xung quanh.",
            "essence": "Sự cân bằng điện tích đảm bảo tính bền vững của vật chất trong tự nhiên."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một nguyên tử X có tổng số hạt là 40, trong đó số hạt mang điện nhiều hơn số hạt không mang điện là 12. Tìm số proton và electron của X.",
            "steps": [
              "Bước 1: Gọi số p = số e = Z và số neutron là N. Ta có tổng số hạt: 2Z + N = 40.",
              "Bước 2: Số hạt mang điện (2Z) nhiều hơn không mang điện (N) là 12: 2Z - N = 12.",
              "Bước 3: Cộng hai phương trình: 4Z = 52 => Z = 13 (Số p = số e = 13, đó là nguyên tố Nhôm - Al)."
            ],
            "answer": "Số p = 13, số e = 13, số n = 14."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng electron chuyển động trên các quỹ đạo tròn cố định như hành tinh quay quanh mặt trời.",
            "why": "Theo mô hình hiện đại, electron chuyển động rất nhanh xung quanh hạt nhân trong khu vực không gian gọi là đám mây electron."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Phân tử và Liên kết hóa học",
        "description": "Đơn chất và hợp chất, liên kết ion, liên kết cộng hóa trị và cách tính hóa trị, lập công thức hóa học.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phân tử, đơn chất và hợp chất", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Liên kết ion và liên kết cộng hóa trị", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Liên kết cộng hóa trị",
            "definition": "Là liên kết được hình thành giữa hai nguyên tử bằng một hoặc nhiều đôi electron dùng chung.",
            "example": "Phân tử nước (H2O): Nguyên tử Oxygen dùng chung 2 đôi electron với 2 nguyên tử Hydrogen.",
            "essence": "Các phi kim có xu hướng góp chung electron để đạt cấu hình 8 electron bền vững như khí hiếm."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc hóa trị trong hợp chất hai nguyên tố",
            "meaning": "Trong công thức AxBy, tích của chỉ số và hóa trị của nguyên tố này bằng tích của chỉ số và hóa trị của nguyên tố kia: x * a = y * b.",
            "example": "Trong Al2O3, Al hóa trị III và O hóa trị II: 2 * III = 3 * II = 6.",
            "essence": "Quy tắc hóa trị phản ánh sự cân bằng về số electron trao đổi hoặc dùng chung giữa các nguyên tử."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Lập công thức hóa học của hợp chất tạo bởi nguyên tố Carbon (IV) và Oxygen (II).",
            "steps": [
              "Bước 1: Đặt công thức tổng quát là CxOy.",
              "Bước 2: Áp dụng quy tắc hóa trị: x * IV = y * II => x/y = II/IV = 1/2.",
              "Bước 3: Chọn x = 1, y = 2. Công thức hóa học là CO2."
            ],
            "answer": "Công thức hóa học là CO2 (Khí carbon dioxide)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa đơn chất và hợp chất.",
            "why": "Đơn chất tạo nên từ 1 nguyên tố (O2, Fe, N2), còn hợp chất tạo nên từ 2 nguyên tố hóa học trở lên (H2O, NaCl, CO2)."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Tốc độ và Đồ thị quãng đường - thời gian",
        "description": "Khái niệm tốc độ chuyển động, công thức tính tốc độ v = s/t, đơn vị đo tốc độ và cách đọc đồ thị quãng đường - thời gian.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tốc độ chuyển động và thiết bị đo tốc độ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Đồ thị quãng đường - thời gian", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tốc độ chuyển động",
            "definition": "Là đại lượng đặc trưng cho sự nhanh hay chậm của chuyển động, được tính bằng quãng đường đi được trong một đơn vị thời gian: v = s / t.",
            "example": "Một xe máy đi được quãng đường 90 km trong 2 giờ thì tốc độ là v = 90 / 2 = 45 km/h.",
            "essence": "Tốc độ cho biết mức độ thay đổi vị trí của vật trong không gian theo thời gian."
          }
        ],
        "rules": [
          {
            "statement": "Đổi đơn vị tốc độ chuẩn giữa m/s và km/h",
            "meaning": "1 m/s = 3,6 km/h. Muốn đổi từ m/s sang km/h ta nhân với 3,6; ngược lại từ km/h sang m/s ta chia cho 3,6.",
            "example": "Vận động viên chạy 10 m/s tương đương với tốc độ 10 * 3,6 = 36 km/h.",
            "essence": "Xuất phát từ 1 km = 1000m và 1 giờ = 3600 giây."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một ô tô chạy từ Hà Nội đến Hải Phòng trên quãng đường dài 108 km hết 1 giờ 30 phút. Tính tốc độ của ô tô theo đơn vị km/h và m/s.",
            "steps": [
              "Bước 1: Đổi thời gian: 1 giờ 30 phút = 1,5 giờ.",
              "Bước 2: Tính tốc độ: v = s / t = 108 / 1,5 = 72 km/h.",
              "Bước 3: Đổi sang m/s: v = 72 / 3,6 = 20 m/s."
            ],
            "answer": "Tốc độ ô tô là 72 km/h (hay 20 m/s)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy trực tiếp 108 chia cho 1,3 khi đổi 1 giờ 30 phút.",
            "why": "30 phút là nửa giờ (0,5 giờ), không phải 0,3 giờ. 1 giờ 30 phút bắt buộc phải đổi thành 1,5 giờ."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Âm thanh và Ánh sáng",
        "description": "Nguồn âm, sự truyền sóng âm, độ cao và độ to của âm, sự phản xạ ánh sáng và định luật phản xạ ánh sáng.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sóng âm, độ cao và độ to của âm", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Ánh sáng, tia sáng và định luật phản xạ ánh sáng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tần số dao động của âm",
            "definition": "Là số dao động mà nguồn âm thực hiện được trong một giây. Đơn vị tần số là héc (Hz). Tần số càng lớn, âm phát ra càng cao (bổng).",
            "example": "Giọng nữ cao hát nốt Sol có tần số khoảng 784 Hz, tiếng trống trầm có tần số khoảng 60 Hz.",
            "essence": "Độ cao của âm chỉ phụ thuộc vào tần số dao động; độ to của âm phụ thuộc vào biên độ dao động."
          }
        ],
        "rules": [
          {
            "statement": "Định luật phản xạ ánh sáng",
            "meaning": "Tia sáng phản xạ nằm trong mặt phẳng tới và ở phía bên kia pháp tuyến so với tia tới. Góc phản xạ luôn bằng góc tới: i' = i.",
            "example": "Chiếu tia sáng tới gương phẳng với góc tới 40 độ thì góc phản xạ cũng bằng 40 độ.",
            "essence": "Bảo toàn tính đối xứng quang học khi ánh sáng gặp bề mặt nhẵn bóng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Chiếu một tia sáng tới gương phẳng hợp với mặt gương một góc 30 độ. Tính góc phản xạ.",
            "steps": [
              "Bước 1: Pháp tuyến vuông góc với mặt gương nên góc hợp bởi pháp tuyến và mặt gương là 90 độ.",
              "Bước 2: Tính góc tới i: i = 90 độ - 30 độ = 60 độ.",
              "Bước 3: Áp dụng định luật phản xạ ánh sáng: Góc phản xạ i' = i = 60 độ."
            ],
            "answer": "Góc phản xạ là 60 độ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm góc hợp bởi tia tới và mặt gương chính là góc tới.",
            "why": "Góc tới là góc hợp bởi tia tới và đường PHÁP TUYẾN (đường vuông góc với gương), không phải góc hợp với mặt gương."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Từ trường và Nam châm",
        "description": "Nam châm vĩnh cửu, từ trường, đường sức từ, từ trường Trái Đất và ứng dụng chế tạo nam châm điện.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Nam châm, từ trường và đường sức từ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Nam châm điện và ứng dụng trong đời sống", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Từ trường",
            "definition": "Là không gian xung quanh nam châm hoặc dây dẫn có dòng điện chạy qua, có khả năng tác dụng lực từ lên kim nam châm đặt trong nó.",
            "example": "Kim la bàn luôn định hướng theo trục Bắc - Nam là do chịu tác dụng của từ trường Trái Đất.",
            "essence": "Từ trường là một dạng vật chất đặc biệt không nhìn thấy bằng mắt thường nhưng cảm nhận được qua lực tác dụng."
          }
        ],
        "rules": [
          {
            "statement": "Quy ước chiều đường sức từ của nam châm",
            "meaning": "Bên ngoài nam châm, đường sức từ là những đường cong khép kín đi ra từ cực Bắc (N) và đi vào cực Nam (S) của nam châm: 'Vào Nam - Ra Bắc'.",
            "example": "Đường sức từ của thanh nam châm thẳng tỏa ra từ đầu cực Bắc màu đỏ và uốn cong hội tụ vào đầu cực Nam màu xanh.",
            "essence": "Chiều đường sức từ tại mỗi điểm là chiều chỉ của kim nam châm thử đặt tại điểm đó."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 2 cách làm tăng lực từ của một nam châm điện đơn giản cuốn quanh lõi sắt non.",
            "steps": [
              "Bước 1: Tăng cường độ dòng điện chạy qua các vòng dây (tăng số pin hoặc điện áp nguồn).",
              "Bước 2: Tăng số vòng dây cuốn quanh lõi sắt non.",
              "Bước 3: Sử dụng lõi sắt non có từ tính tốt thay vì lõi thép."
            ],
            "answer": "Tăng cường độ dòng điện và tăng số vòng dây cuộn."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng nam châm hút được tất cả các kim loại như đồng, nhôm, vàng.",
            "why": "Nam châm chỉ tương tác hút các vật liệu từ như sắt, thép, niken, coban. Đồng, nhôm, vàng là kim loại phi từ tính."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Trao đổi chất và Năng lượng ở sinh vật",
        "description": "Quang hợp ở thực vật, hô hấp tế bào, vai trò của nước và chất dinh dưỡng đối với cơ thể sinh vật.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Quang hợp ở thực vật và vai trò đối với sinh quyển", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hô hấp tế bào và các yếu tố ảnh hưởng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quang hợp",
            "definition": "Là quá trình lục lạp ở lá cây hấp thụ năng lượng ánh sáng mặt trời để tổng hợp chất hữu cơ (glucose) từ nước và khí carbon dioxide, đồng thời giải phóng khí oxygen.",
            "example": "Cây xanh ban ngày dưới ánh nắng hấp thụ CO2 và thải ra O2, tạo ra tinh bột nuôi sống toàn cây.",
            "essence": "Quang hợp là nhà máy năng lượng sinh học duy nhất chuyển hóa quang năng thành hóa năng dự trữ cho toàn bộ sự sống trên Trái Đất."
          },
          {
            "term": "Hô hấp tế bào",
            "definition": "Là quá trình phân giải các phân tử chất hữu cơ (chủ yếu là glucose) với sự tham gia của oxygen tạo thành CO2, nước và giải phóng năng lượng dưới dạng ATP cung cấp cho các hoạt động sống.",
            "example": "Khi vận động mạnh, nhịp thở và nhịp tim tăng lên để cung cấp đủ O2 cho hô hấp tế bào sản sinh năng lượng cơ bắp.",
            "essence": "Hô hấp tế bào và quang hợp là hai quá trình ngược chiều nhưng gắn kết mật thiết trong chu trình vật chất và năng lượng sinh quyển."
          }
        ],
        "rules": [
          {
            "statement": "Phương trình tổng quát của quang hợp và hô hấp",
            "meaning": "Quang hợp: Nước + Carbon dioxide + Ánh sáng -> Glucose + Oxygen. Hô hấp tế bào: Glucose + Oxygen -> Carbon dioxide + Nước + Năng lượng (ATP + Nhiệt).",
            "example": "Cây xanh vừa quang hợp ban ngày vừa hô hấp liên tục suốt ngày đêm.",
            "essence": "Sự cân bằng giữa tổng hợp và phân giải duy trì sự sống bền vững của sinh vật."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao không nên để nhiều chậu cây xanh trong phòng ngủ đóng kín cửa vào ban đêm?",
            "steps": [
              "Bước 1: Ban đêm không có ánh sáng mặt trời, cây xanh ngừng quang hợp nhưng vẫn tiếp tục hô hấp tế bào.",
              "Bước 2: Quá trình hô hấp của cây tiêu thụ khí oxygen (O2) và thải ra khí carbon dioxide (CO2).",
              "Bước 3: Trong phòng kín, lượng O2 bị giảm nhanh chóng và nồng độ CO2 tăng cao, có thể gây ngạt thở nguy hiểm cho con người."
            ],
            "answer": "Để tránh hiện tượng thiếu dưỡng khí O2 và ngộ độc CO2 khi ngủ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng cây xanh chỉ hô hấp vào ban đêm, còn ban ngày chỉ quang hợp.",
            "why": "Cây xanh hô hấp tế bào liên tục 24/24 giờ để duy trì sự sống. Ban ngày cường độ quang hợp mạnh hơn hô hấp nên cây thải O2 ròng ra môi trường."
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
        "title": "Bài 1: Bầu trời tuổi thơ",
        "description": "Thể loại truyện ngắn hiện đại, nghệ thuật miêu tả tâm lý trẻ thơ, không gian thiên nhiên trong trẻo và vẻ đẹp của tình cảm gia đình, bè bạn.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu văn bản 'Bầy chim chìa vôi' (Nguyễn Quang Thiều)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành tiếng Việt: Mở rộng trạng ngữ và ngôi kể", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Ngôi kể thứ ba",
            "definition": "Người kể chuyện giấu mình, không xưng 'tôi', gọi các nhân vật bằng tên gọi của họ. Người kể có khả năng quan sát bao quát toàn bộ sự việc và diễn biến tâm lý của mọi nhân vật.",
            "example": "Trong 'Bầy chim chìa vôi', người kể đứng ngoài quan sát cuộc trò chuyện lúc nửa đêm của hai anh em Mên và Mon về bãi cát ngập nước.",
            "essence": "Ngôi kể thứ ba tạo ra tính khách quan, đa chiều cho câu chuyện kể."
          }
        ],
        "rules": [
          {
            "statement": "Tác dụng của thành phần trạng ngữ mở rộng",
            "meaning": "Mở rộng trạng ngữ bằng cụm từ giúp bổ sung thông tin chi tiết, cụ thể hơn về thời gian, không gian, nguyên nhân hoặc phương tiện diễn ra hành động.",
            "example": "'Vào một đêm mưa to gió lớn đầu mùa hạ, hai đứa trẻ không ngủ được vì lo cho bầy chim non.'",
            "essence": "Làm cho câu văn giàu hình ảnh và bối cảnh sinh động hơn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích ý nghĩa chi tiết bầy chim chìa vôi non cất cánh bay lên giữa dòng nước lũ ở cuối văn bản 'Bầy chim chìa vôi'.",
            "steps": [
              "Bước 1: Hoàn cảnh: Nước sông dâng cao sắp nhấn chìm dải cát, bầy chim non đối mặt hiểm nguy sinh tử.",
              "Bước 2: Hình ảnh: Những cánh chim non ướt át nhưng vút bay lên không trung đón ánh bình minh rực rỡ.",
              "Bước 3: Ý nghĩa: Biểu tượng cho sức sống kỳ diệu của thiên nhiên và niềm hạnh phúc vỡ òa, tấm lòng nhân hậu của hai đứa trẻ."
            ],
            "answer": "Chi tiết tôn vinh tình yêu thiên nhiên, lòng trắc ẩn và sự kỳ diệu của sự sống."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa ngôi kể thứ nhất xưng 'tôi' và ngôi kể thứ ba giấu mình.",
            "why": "Khi nhân vật xưng 'tôi' kể chuyện của chính mình thì đó là ngôi kể thứ nhất; còn khi người kể gọi tên 'Mên', 'Mon' thì là ngôi kể thứ ba."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Bài 2: Khúc nhạc tâm hồn",
        "description": "Thơ bốn chữ, năm chữ; vần chân, vần lưng; nhịp thơ và nghệ thuật biểu đạt cảm xúc lắng đọng về thiên nhiên, con người.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu bài thơ 'Đồng dao mùa xuân' (Nguyễn Khoa Điềm)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thơ bốn chữ, năm chữ và biện pháp tu từ điệp ngữ", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thơ bốn chữ, năm chữ",
            "definition": "Là thể thơ có nguồn gốc từ đồng dao, ca dao dân tộc, mỗi dòng gồm 4 hoặc 5 tiếng, ngắt nhịp linh hoạt (2/2 hoặc 3/2, 2/3), giàu nhạc điệu và dễ nhớ.",
            "example": "'Có một người lính / Đi vào rừng sâu / Chưa một lần yêu / Cà phê chưa uống...' (Đồng dao mùa xuân).",
            "essence": "Nhịp điệu cô đọng, tự nhiên như lời ru hoặc bài đồng dao ngân vang muôn đời."
          }
        ],
        "rules": [
          {
            "statement": "Hiệu quả nghệ thuật của biện pháp điệp ngữ",
            "meaning": "Lặp lại từ ngữ hoặc cụm từ nhằm nhấn mạnh cảm xúc, khắc sâu hình tượng nghệ thuật hoặc tạo nhịp điệu dồn dập, tha thiết cho lời thơ.",
            "example": "'Anh không về nữa / Anh vẫn một mình...' nhấn mạnh sự hi sinh thầm lặng và bất tử của người lính trẻ.",
            "essence": "Điệp từ điệp ngữ là đòn bẩy xúc cảm mãnh liệt trong thơ ca trữ tình."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Hình ảnh người lính trong 'Đồng dao mùa xuân' của Nguyễn Khoa Điềm được khắc họa với những vẻ đẹp nào?",
            "steps": [
              "Bước 1: Nét hồn nhiên, trẻ trung: Chưa từng yêu, còn thích thả diều, nụ cười hiền hậu.",
              "Bước 2: Tinh thần quả cảm: Sẵn sàng hiến dâng tuổi thanh xuân vì độc lập tự do của Tổ quốc.",
              "Bước 3: Sự bất tử: Người lính hòa vào cỏ cây Trường Sơn, sống mãi cùng mùa xuân của đất nước."
            ],
            "answer": "Bức tượng đài người lính bình dị, kiên cường và vĩnh hằng cùng non sông."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Xác định sai thể thơ do đếm không kĩ số chữ trong từng dòng.",
            "why": "Cần kiểm tra toàn bộ các câu trong bài thơ; thể thơ 4 chữ thì đa số dòng có 4 tiếng, thể 5 chữ thì đa số dòng có 5 tiếng."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Bài 3: Cội nguồn yêu thương",
        "description": "Tình mẫu tử, tình phụ tử thiêng liêng, giá trị của mái ấm gia đình và nghệ thuật viết văn bản nghị luận xã hội về lối sống.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu văn bản 'Vừa nhắm mắt vừa mở cửa sổ' (Nguyễn Ngọc Thuần)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Viết bài văn nghị luận về một vấn đề đời sống", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Văn bản nghị luận về vấn đề đời sống",
            "definition": "Là kiểu văn bản bàn luận về một hiện tượng, phẩm chất hoặc lối sống trong xã hội, sử dụng lí lẽ chặt chẽ và bằng chứng xác thực để thuyết phục người đọc.",
            "example": "Bàn về lòng biết ơn cha mẹ, sự đồng cảm với người có hoàn cảnh khó khăn.",
            "essence": "Mục đích của nghị luận là định hướng nhận thức đúng đắn và khơi dậy hành động nhân văn."
          }
        ],
        "rules": [
          {
            "statement": "Mối quan hệ giữa Luận điểm, Lí lẽ và Dẫn chứng",
            "meaning": "Luận điểm là tư tưởng cốt lõi; Lí lẽ là lời giải thích logic làm sáng tỏ luận điểm; Dẫn chứng là ví dụ thực tế chứng minh lí lẽ là đúng đắn.",
            "example": "Luận điểm: Tình bạn cần sự chân thành -> Lí lẽ: Sự dối trá sẽ phá vỡ niềm tin -> Dẫn chứng: Tình bạn Lưu Bình - Dương Lễ.",
            "essence": "Thiếu lí lẽ bài viết sẽ rời rạc, thiếu dẫn chứng bài viết sẽ sáo rỗng thiếu sức thuyết phục."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Bài học sâu sắc nhất em rút ra từ văn bản 'Vừa nhắm mắt vừa mở cửa sổ' của Nguyễn Ngọc Thuần là gì?",
            "steps": [
              "Bước 1: Cảm nhận thế giới bằng mọi giác quan: Lắng nghe tiếng bước chân, ngửi mùi hương hoa để thấu hiểu vạn vật.",
              "Bước 2: Trân trọng những món quà: Món quà lớn nhất chính là tấm lòng và tình yêu thương của người trao tặng.",
              "Bước 3: Tình yêu thương gia đình: Sự dạy dỗ kiên nhẫn, ấm áp của người cha giúp tâm hồn đứa trẻ nở hoa."
            ],
            "answer": "Yêu thương thế giới bằng cả trái tim và trân trọng từng phút giây bên gia đình."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy dẫn chứng mơ hồ, bịa đặt số liệu hoặc dẫn chứng không liên quan đến luận điểm.",
            "why": "Dẫn chứng phải tiêu biểu, chân thực, được xã hội thừa nhận thì mới tạo nên sức nặng cho lập luận."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Bài 4: Giai điệu đất nước",
        "description": "Thể loại tùy bút, tản văn; chất trữ tình của văn xuôi; lòng tự hào về cảnh sắc quê hương và bản sắc văn hóa ẩm thực Việt Nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu tản văn 'Mùa xuân nho nhỏ' và tùy bút 'Cốm Làng Vòng'", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành tiếng Việt: Từ Hán Việt và nghĩa của từ", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tùy bút và Tản văn",
            "definition": "Là thể loại văn xuôi phi hư cấu giàu chất trữ tình, ghi chép lại những quan sát tinh tế, rung động nội tâm và suy ngẫm của tác giả trước cảnh vật, đời sống.",
            "example": "Thạch Lam viết về hạt cốm Vòng: Một thức quà thanh nhã mang hương vị đồng quê mộc mạc của lúa nếp non.",
            "essence": "Tùy bút bộc lộ trực tiếp cái 'tôi' tài hoa, uyên bác và giàu cảm xúc của nhà văn."
          }
        ],
        "rules": [
          {
            "statement": "Sắc thái ý nghĩa của từ Hán Việt",
            "meaning": "Từ Hán Việt mang sắc thái trang trọng, tao nhã, cổ kính hoặc trừu tượng hơn so với từ thuần Việt đồng nghĩa.",
            "example": "Dùng 'phụ nữ' thay cho 'đàn bà', dùng 'hi sinh' thay cho 'chết', dùng 'giang sơn' thay cho 'sông núi'.",
            "essence": "Sử dụng đúng từ Hán Việt nâng cao tính biểu cảm và sự tôn nghiêm của văn bản."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao Thạch Lam gọi cốm là 'thức quà riêng biệt của đất nước, là thức dâng của những cánh đồng lúa bát ngát'?",
            "steps": [
              "Bước 1: Nguồn gốc nguyên liệu: Cốm chắt lọc từ những hạt lúa nếp non thơm ngát mùi sữa mẹ thiên nhiên.",
              "Bước 2: Nghệ thuật chế biến: Đòi hỏi sự công phu, khéo léo và bí quyết gia truyền của những cô gái làng Vòng.",
              "Bước 3: Giá trị văn hóa: Cốm không chỉ để ăn no mà để thưởng thức hương vị thanh khiết, gắn liền với phong tục sêu tết trang trọng."
            ],
            "answer": "Cốm là biểu tượng tinh hoa kết tinh văn hóa ẩm thực và linh hồn đồng quê Việt Nam."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lạm dụng từ Hán Việt trong giao tiếp hàng ngày gây cảm giác kiểu cách, xa lạ.",
            "why": "Cần sử dụng từ ngữ phù hợp với ngữ cảnh; văn phong đời thường nên ưu tiên từ thuần Việt trong sáng."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Bài 5: Bài học cuộc sống (Truyện ngụ ngôn)",
        "description": "Đặc trưng truyện ngụ ngôn, nhân vật ngụ ngôn, nghệ thuật ẩn dụ và những bài học triết lý nhân sinh sâu sắc.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đọc hiểu truyện ngụ ngôn 'Ếch ngồi đáy giếng', 'Đẽo cày giữa đường'", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành tiếng Việt: Thành ngữ và ngữ cảnh sử dụng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Truyện ngụ ngôn",
            "definition": "Là truyện kể bằng văn xuôi hoặc văn vần, mượn chuyện về loài vật, đồ vật hoặc con người để kín đáo gửi gắm những bài học đạo đức, kinh nghiệm sống sâu sắc.",
            "example": "Truyện 'Ếch ngồi đáy giếng' mượn tiếng kêu ồm ộp của con ếch để phê phán thói kiêu ngạo, tầm nhìn hạn hẹp.",
            "essence": "Truyện ngụ ngôn mang tính giáo huấn nhẹ nhàng nhưng thấm thía thông qua tiếng cười châm biếm."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm của thành ngữ tiếng Việt",
            "meaning": "Thành ngữ là cụm từ cố định có cấu trúc chặt chẽ và nghĩa bóng mang tính biểu trưng cao, không thể hiểu đơn thuần qua nghĩa đen của từng từ.",
            "example": "'Ếch ngồi đáy giếng' chỉ người có tầm nhìn hạn hẹp nhưng lại tự cao tự đại; 'Đẽo cày giữa đường' chỉ người không có chủ kiến.",
            "essence": "Thành ngữ đúc kết trí tuệ dân gian ngàn đời qua hình ảnh so sánh độc đáo."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Từ truyện ngụ ngôn 'Đẽo cày giữa đường', em rút ra bài học gì về việc lắng nghe ý kiến của người khác?",
            "steps": [
              "Bước 1: Tóm tắt sai lầm: Người thợ mộc ai bảo gì cũng nghe theo, cuối cùng gỗ hỏng hết và không chiếc cày nào dùng được.",
              "Bước 2: Phân tích nguyên nhân: Do thiếu lập trường vững vàng, không hiểu rõ nhu cầu và không biết chọn lọc lời khuyên.",
              "Bước 3: Bài học: Phải có chính kiến của bản thân, lắng nghe có chọn lọc và phân tích thấu đáo trước khi thay đổi quyết định."
            ],
            "answer": "Cần giữ vững chủ kiến, tiếp thu lời khuyên một cách thông minh và có căn cứ khoa học."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đồng nhất thành ngữ với tục ngữ.",
            "why": "Thành ngữ là cụm từ cố định chưa thành câu trọn vẹn (ví dụ: 'nước đổ đầu vịt'); còn tục ngữ là một câu hoàn chỉnh đúc kết kinh nghiệm (ví dụ: 'Gần mực thì đen, gần đèn thì rạng')."
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
        "title": "Chương 1: Tây Âu từ thế kỉ V đến nửa đầu thế kỉ XVI",
        "description": "Sự hình thành chế độ phong kiến Tây Âu, các cuộc phát kiến địa lí lớn và phong trào Văn hóa Phục hưng rực rỡ.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sự hình thành lãnh địa phong kiến và thành thị trung đại", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các cuộc phát kiến địa lí và phong trào Văn hóa Phục hưng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Lãnh địa phong kiến",
            "definition": "Là vùng đất rộng lớn của quý tộc phong kiến bị biến thành khu vực khép kín về kinh tế và tự trị về chính trị, có lâu đài, hào nước và nông nô phục dịch.",
            "example": "Lãnh chúa sống xa hoa trong lâu đài kiên cố, bóc lột địa tô nặng nề đối với người nông nô cày cấy trên đồng ruộng.",
            "essence": "Lãnh địa là tế bào kinh tế tự cung tự cấp đặc trưng cho thời kỳ phong kiến phân quyền Tây Âu."
          },
          {
            "term": "Văn hóa Phục hưng",
            "definition": "Phong trào văn hóa tiến bộ của giai cấp tư sản thế kỉ XIV - XVII nhằm khôi phục tinh hoa văn hóa Hy Lạp - La Mã cổ đại và đề cao giá trị con người (Chủ nghĩa nhân văn).",
            "example": "Danh họa Leonardo da Vinci với bức tranh Mona Lisa, kịch tác gia Shakespeare với các vở kịch Hamlet, Romeo và Juliet.",
            "essence": "Giải phóng tư tưởng con người khỏi sự kìm kẹp của giáo hội thời Trung cổ, mở đường cho khoa học hiện đại."
          }
        ],
        "rules": [
          {
            "statement": "Ý nghĩa lịch sử của các cuộc phát kiến địa lí (thế kỉ XV - XVI)",
            "meaning": "Mở ra những con đường hàng hải mới kết nối các châu lục, thúc đẩy giao lưu thương mại toàn cầu và tích lũy tư bản ban đầu cho châu Âu.",
            "example": "Colombo tìm ra châu Mỹ (1492), Magellan thực hiện chuyến thám hiểm vòng quanh Trái Đất (1519 - 1522).",
            "essence": "Mở rộng tầm hiểu biết của nhân loại về thế giới địa cầu nhưng cũng mở đầu thời kỳ thực dân xâm lược."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao nói 'Thành thị trung đại Tây Âu là những bông hoa rực rỡ nhất của thời Trung cổ'?",
            "steps": [
              "Bước 1: Kinh tế: Phá vỡ nền kinh tế tự nhiên khép kín của lãnh địa, hình thành thị trường tự do buôn bán hàng hóa.",
              "Bước 2: Xã hội: Tạo ra tầng lớp thị dân mới tự do, độc lập khỏi quyền lực của lãnh chúa phong kiến.",
              "Bước 3: Văn hóa: Thành thị là nơi lập nên các trường đại học đầu tiên (Bologna, Paris), nuôi dưỡng tri thức và văn hóa tự do."
            ],
            "answer": "Thành thị là cái nôi sản sinh ra nền kinh tế hàng hóa và chuẩn bị tiền đề cho xã hội tư bản chủ nghĩa."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng người nông nô hoàn toàn là nô lệ không có tài sản.",
            "why": "Nông nô khác nô lệ: Nông nô có gia đình riêng, có túp lều và nông cụ riêng, nhưng bị gắn chặt vào ruộng đất của lãnh chúa và phải nộp địa tô."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Đại Việt thời Tiền Lê, Lý, Trần (Thế kỉ X - XIV)",
        "description": "Công cuộc xây dựng nhà nước quân chủ độc lập, các cuộc kháng chiến chống Tống, Mông - Nguyên oanh liệt và thành tựu văn hóa Thăng Long.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Nước Đại Việt thời Lý và phòng tuyến sông Như Nguyệt", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Nước Đại Việt thời Trần và ba lần đánh thắng quân Mông - Nguyên", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hào khí Đông A",
            "definition": "Là tinh thần đoàn kết toàn dân, ý chí tự lực tự cường và lòng yêu nước quật cường của quân dân nhà Trần trong thế kỉ XIII (chữ 'Đông' ghép với chữ 'A' tạo thành chữ 'Trần').",
            "example": "Hội nghị Diên Hồng: Các bô lão đồng thanh hô 'Đánh!'; tướng sĩ khắc hai chữ 'Sát Thát' lên cánh tay thề diệt giặc.",
            "essence": "Sức mạnh bách chiến bách thắng bắt nguồn từ việc 'Vua tôi đồng lòng, anh em hòa mục, cả nước góp sức'."
          }
        ],
        "rules": [
          {
            "statement": "Nghệ thuật quân sự 'Tiên phát chế nhân' của Lý Thường Kiệt",
            "meaning": "Chủ động tiến công trước để phá vỡ thế chuẩn bị xâm lược của địch, sau đó lui về lập phòng tuyến hiểm yếu chặn đứng bước tiến quân thù.",
            "example": "Tập kích đồn Ung Châu phá hủy kho lương địch (1075), sau đó lui về lập phòng tuyến vững chắc trên sông Như Nguyệt (1077).",
            "essence": "Lấy thế chủ động của người làm chủ địa hình đánh bại ưu thế quân đông của đối phương."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích kế sách 'Vườn không nhà trống' của nhà Trần trong cuộc kháng chiến chống quân xâm lược Mông - Nguyên.",
            "steps": [
              "Bước 1: Chủ động rút lui: Rút khỏi kinh thành Thăng Long, không đối đầu trực diện khi giặc đang hung hãn.",
              "Bước 2: Triệt phá hậu cần: Nhân dân cất giấu toàn bộ lương thực, biến Thăng Long thành thành phố hoang tàn khiến giặc lâm vào cảnh đói khát.",
              "Bước 3: Phản công chiến lược: Khi giặc suy yếu và hoang mang, quân dân nhà Trần mở các trận quyết chiến (Đông Bộ Đầu, Hàm Tử, Chương Dương, Bạch Đằng)."
            ],
            "answer": "Kế sách phát huy cao độ chiến tranh nhân dân, biến sở trường kỵ binh của giặc thành sở đoản bại trận."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa trận Bạch Đằng năm 938 (Ngô Quyền diệt quân Nam Hán) và trận Bạch Đằng năm 1288 (Trần Quốc Tuấn diệt quân Nguyên).",
            "why": "Cả hai đều dùng bãi cọc ngầm trên sông Bạch Đằng nhưng diễn ra ở hai triều đại lịch sử cách nhau 350 năm."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Khám phá Châu Âu",
        "description": "Vị trí địa lí, đặc điểm địa hình, khí hậu, các đới thiên nhiên và đặc điểm dân cư, đô thị hóa tại châu Âu.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vị trí địa lí và đặc điểm tự nhiên châu Âu", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Đặc điểm dân cư, xã hội và đô thị hóa châu Âu", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Khí hậu ôn đới hải dương",
            "definition": "Kiểu khí hậu phổ biến ở Tây Âu ven Đại Tây Dương, chịu ảnh hưởng mạnh của dòng biển nóng Bắc Đại Tây Dương và gió Tây ôn đới: Mùa hạ mát mẻ, mùa đông không quá lạnh, mưa quanh năm.",
            "example": "Khí hậu nước Anh và miền bắc nước Pháp luôn có sương mù ẩm ướt và lượng mưa phân bố đều các tháng.",
            "essence": "Hải lưu nóng và gió biển làm điều hòa nền nhiệt lục địa, giảm bớt sự khắc nghiệt mùa đông."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm cơ cấu dân số châu Âu (Dân số già)",
            "meaning": "Tỉ lệ gia tăng tự nhiên rất thấp hoặc âm; nhóm tuổi dưới 15 tuổi giảm mạnh trong khi nhóm tuổi trên 65 tuổi tăng nhanh.",
            "example": "Nhiều quốc gia như Đức, Ý phải ban hành chính sách khuyến khích sinh con và thu hút người lao động nhập cư chất lượng cao.",
            "essence": "Dân số già tạo ra thách thức lớn về thiếu hụt lao động và gia tăng gánh nặng quỹ phúc lợi hưu trí."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao càng đi sâu về phía đông lục địa châu Âu, khí hậu càng mang tính chất lục địa sâu sắc?",
            "steps": [
              "Bước 1: Khoảng cách tới biển: Càng đi về phía đông, khoảng cách từ đất liền đến Đại Tây Dương càng xa.",
              "Bước 2: Hơi ẩm giảm dần: Gió Tây ôn đới mang hơi ẩm từ biển vào bị cản lại và giảm dần lượng mưa trên đường đi.",
              "Bước 3: Biên độ nhiệt tăng: Mùa hạ trở nên nóng hơn và mùa đông rất lạnh giá, có tuyết rơi dày (như vùng đồng bằng Đông Âu, Nga)."
            ],
            "answer": "Do giảm ảnh hưởng điều hòa của biển và tăng cường tính chất lục địa khô lạnh."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng châu Âu có diện tích rộng lớn hơn châu Á hay châu Phi.",
            "why": "Châu Âu là lục địa có diện tích tương đối nhỏ (khoảng 10 triệu km2), chỉ lớn hơn châu Đại Dương, nhỏ hơn rất nhiều so với châu Á (44 triệu km2)."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Thiên nhiên và Con người Châu Á",
        "description": "Địa hình đồ sộ, các đới khí hậu gió mùa, mạng lưới sông ngòi và đặc điểm dân cư đông đúc nhất hành tinh.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Địa hình, khoáng sản và khí hậu gió mùa châu Á", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sông ngòi và đặc điểm dân cư, xã hội châu Á", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Gió mùa châu Á",
            "definition": "Là loại gió đổi hướng theo mùa rõ rệt: Mùa hạ gió thổi từ biển vào mang theo khối khí ẩm gây mưa lớn; Mùa đông gió thổi từ lục địa ra mang khối khí lạnh và khô.",
            "example": "Khu vực Nam Á và Đông Nam Á (trong đó có Việt Nam) chịu ảnh hưởng sâu sắc của gió mùa mùa hạ gây mưa rào nhiệt đới.",
            "essence": "Sự chênh lệch nhiệt độ và áp suất giữa lục địa châu Á khổng lồ và các đại dương bao quanh là nguyên nhân sinh ra gió mùa."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm phân bố mạng lưới sông ngòi châu Á",
            "meaning": "Mạng lưới sông ngòi phát triển nhưng phân bố không đều: Khu vực gió mùa mưa nhiều có sông ngòi dày đặc và nhiều nước (Hoàng Hà, Trường Giang, Mê Kông); Khu vực nội địa khô hạn sông ngòi kém phát triển.",
            "example": "Sông Mê Kông bắt nguồn từ cao nguyên Tây Tạng, chảy qua 6 nước đổ ra Biển Đông với lượng phù sa bồi đắp đồng bằng trù phú.",
            "essence": "Chế độ nước sông phản ánh trung thành chế độ mưa của từng đới khí hậu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu những thuận lợi và khó khăn của đặc điểm dân số châu Á đối với phát triển kinh tế.",
            "steps": [
              "Bước 1: Thuận lợi: Dân số đông (chiếm gần 60% dân số thế giới) tạo ra nguồn lao động dồi dào, giá rẻ và thị trường tiêu thụ rộng lớn.",
              "Bước 2: Khó khăn: Gây sức ép nặng nề lên giải quyết việc làm, y tế, giáo dục, nhà ở và ô nhiễm môi trường sống.",
              "Bước 3: Đánh giá: Cần nâng cao chất lượng nguồn nhân lực và đào tạo nghề thay vì chỉ dựa vào lao động thô sơ."
            ],
            "answer": "Vừa là động lực phát triển vừa là thách thức lớn về an sinh xã hội."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng toàn bộ châu Á đều có khí hậu nóng ẩm quanh năm.",
            "why": "Châu Á trải dài qua nhiều đới khí hậu: Từ cực lạnh giá (Bắc Á Siberia), khô hạn sa mạc (Tây Á, Trung Á) đến nhiệt đới gió mùa (Đông Nam Á)."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Khám phá Châu Phi",
        "description": "Vị trí địa lí châu lục nóng nhất thế giới, hoang mạc Sahara khổng lồ, vấn đề bùng nổ dân số và nạn đói, xung đột sắc tộc.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Thiên nhiên châu Phi và hoang mạc hóa", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Vấn đề dân số, xung đột sắc tộc và di sản văn hóa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hoang mạc hóa",
            "definition": "Là quá trình suy thoái đất đai ở các vùng khô hạn do tác động của biến đổi khí hậu và hoạt động khai thác quá mức của con người (chặt phá rừng, chăn thả gia súc bừa bãi).",
            "example": "Vùng Sahel nằm ở rìa phía nam hoang mạc Sahara đang bị cát sa mạc lấn dần mỗi năm hàng chục km.",
            "essence": "Đất đai màu mỡ biến thành cồn cát khô cằn làm mất đi sinh kế của hàng triệu người dân."
          }
        ],
        "rules": [
          {
            "statement": "Vì sao châu Phi là châu lục nóng và khô hạn nhất thế giới?",
            "meaning": "Do phần lớn lãnh thổ nằm giữa hai đường chí tuyến (khối khí nhiệt đới ngự trị), bờ biển ít khúc khuỷu, dạng hình khối khổng lồ và có dòng biển lạnh ven bờ ngăn cản hơi ẩm vào đất liền.",
            "example": "Dòng biển lạnh Canarian ở phía tây bắc và dòng biển lạnh Benguela ở phía tây nam làm cho bờ biển châu Phi khô hạn cực độ.",
            "essence": "Hình khối lục địa vững chắc và hải lưu lạnh làm triệt tiêu khả năng bốc hơi tạo mưa."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Đề xuất 2 giải pháp cấp bách nhằm đẩy lùi nạn đói và hạn chế hoang mạc hóa ở châu Phi.",
            "steps": [
              "Bước 1: Dự án 'Bức tường xanh vĩ đại': Trồng dải rừng phòng hộ dài hàng nghìn km ngăn cát sa mạc lấn xuống phía nam.",
              "Bước 2: Áp dụng công nghệ tưới tiết kiệm: Sử dụng hệ thống tưới nhỏ giọt và phát triển giống cây trồng chịu hạn năng suất cao.",
              "Bước 3: Ổn định chính trị: Chấm dứt xung đột vũ trang để tập trung nguồn lực phát triển kinh tế nông nghiệp."
            ],
            "answer": "Trồng rừng ngăn sa mạc kết hợp nông nghiệp tiết kiệm nước và hòa bình khu vực."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng châu Phi hoàn toàn không có sông lớn.",
            "why": "Châu Phi có con sông Nin (Nile) dài nhất thế giới (6.650 km) và sông Công-gô (Congo) có lưu lượng nước khổng lồ thứ hai thế giới."
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
        "title": "Unit 1: Hobbies",
        "description": "Vocabulary about leisure activities, present simple tense, verbs of liking and disliking followed by gerunds (V-ing).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Vocabulary & Pronunciation /ə/ and /ɜː/", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Grammar: Present Simple & Verbs of liking + V-ing", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Verbs of liking + V-ing",
            "definition": "Verbs expressing preferences such as like, love, enjoy, fancy, adore, hate, dislike are followed by a gerund (verb + -ing).",
            "example": "I enjoy collecting stamps. / She hates playing computer games all day.",
            "essence": "The gerund acts as a noun representing the activity itself."
          }
        ],
        "rules": [
          {
            "statement": "Present Simple Tense for habitual actions",
            "meaning": "Use Present Simple to describe habits, routines, or general truths. Add -s/-es for third-person singular subjects (He/She/It).",
            "example": "He goes swimming twice a week. / The sun rises in the east.",
            "essence": "Adverbs of frequency (always, usually, often, sometimes, never) normally precede the main verb."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Complete the sentence with the correct form of the verb: 'My brother (not like) __________ (read) __________ comics.'",
            "steps": [
              "Step 1: The subject 'My brother' is third-person singular, so the negative auxiliary is 'does not' (doesn't).",
              "Step 2: The verb 'like' remains in base form: doesn't like.",
              "Step 3: After 'like', the verb 'read' takes the -ing form: reading."
            ],
            "answer": "My brother doesn't like reading comics."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'She like' instead of 'She likes' with third-person singular subjects.",
            "why": "In Present Simple, always remember to add -s or -es to the verb when the subject is He, She, It, or a singular noun."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Unit 2: Healthy Living",
        "description": "Health problems, healthy habits, imperative sentences with 'more' and 'less', and simple sentences with compound coordinators.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Health problems and advice with More / Less", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Simple sentences and conjunctions (and, but, or, so)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Imperatives with 'More' and 'Less'",
            "definition": "Used to give direct health advice or instructions. Use 'More' for good habits and 'Less' for bad habits.",
            "example": "Eat more vegetables and fresh fruits. / Spend less time on electronic screens.",
            "essence": "Short, powerful imperative structures help reinforce healthy lifestyle choices."
          }
        ],
        "rules": [
          {
            "statement": "Coordinating conjunctions (FANBOYS: and, but, or, so)",
            "meaning": "'And' joins similar ideas; 'But' shows contrast; 'Or' gives an alternative; 'So' expresses a result.",
            "example": "I had a sunburn, so I put on some aloe vera cream. / He likes sports, but he is lazy.",
            "essence": "A comma usually precedes the coordinating conjunction when linking two independent clauses."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Combine two sentences using a suitable conjunction: 'She feels tired. She stayed up late last night.'",
            "steps": [
              "Step 1: Identify the relationship: Staying up late is the reason, feeling tired is the result.",
              "Step 2: Use 'so' for result or 'because' for reason: 'She stayed up late last night, so she feels tired.'",
              "Step 3: Add a comma before 'so'."
            ],
            "answer": "She stayed up late last night, so she feels tired."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'less' with countable plural nouns instead of 'fewer'.",
            "why": "Use 'less' for uncountable nouns (less sugar, less fast food) and 'fewer' for countable nouns (fewer candies)."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Unit 3: Community Service",
        "description": "Volunteer activities, community helpers, past simple tense, and distinguishing between past simple and present perfect.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Community activities and volunteering vocabulary", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Past Simple Tense with regular and irregular verbs", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Past Simple Tense",
            "definition": "Describes actions that started and finished at a specific, definite time in the past.",
            "example": "Last summer, our youth club planted 200 trees in the community park.",
            "essence": "Common time markers: yesterday, last week, 2 days ago, in 2020."
          }
        ],
        "rules": [
          {
            "statement": "Pronunciation of regular -ed verb endings",
            "meaning": "Pronounced /t/ after voiceless sounds (/p, k, f, s, ʃ, tʃ/); /ɪd/ after /t, d/; and /d/ after voiced sounds.",
            "example": "Helped /t/, donated /ɪd/, cleaned /d/.",
            "essence": "The physical ease of voice chord vibration determines how -ed is pronounced."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Put the verb in brackets into the correct past tense: 'We (donate) __________ warm clothes to street children last winter.'",
            "steps": [
              "Step 1: Time marker 'last winter' signals the Past Simple tense.",
              "Step 2: 'Donate' is a regular verb ending in -e, so add -d: donated.",
              "Step 3: Check pronunciation: /dəʊˈneɪtɪd/."
            ],
            "answer": "We donated warm clothes to street children last winter."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using the base form or past participle when asking questions with 'Did'.",
            "why": "In questions and negatives, the auxiliary 'did' takes the past marker, so the main verb must return to its bare infinitive: 'Did you donate...?' not 'Did you donated...?'"
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Unit 4: Music and Arts",
        "description": "Musical instruments, famous artists, comparisons with 'as... as', 'the same as', and 'different from'.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Types of arts and musical performances", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Comparisons: (not) as... as, the same as, different from", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Comparison of equality with 'as... as'",
            "definition": "Used to show that two people, things, or actions are equal or unequal: S + be + (not) as + adj + as + O.",
            "example": "Classical music is as interesting as pop music. / Pop art is not as traditional as folk art.",
            "essence": "Adjectives placed between 'as' and 'as' remain in their base positive degree."
          }
        ],
        "rules": [
          {
            "statement": "Usage of 'the same as' and 'different from'",
            "meaning": "'The same as' indicates identity or similarity; 'different from' indicates contrast or divergence.",
            "example": "Her taste in music is the same as mine. / Water puppetry is completely different from Western puppet shows.",
            "essence": "'Same' always requires the definite article 'the'."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rewrite the sentence without changing its meaning: 'Rock music is louder than classical music.' -> 'Classical music is not as...'",
            "steps": [
              "Step 1: Identify the comparison: Rock is louder than classical, meaning classical is less loud than rock.",
              "Step 2: Use negative equality: 'is not as loud as'.",
              "Step 3: Form the sentence: 'Classical music is not as loud as rock music.'"
            ],
            "answer": "Classical music is not as loud as rock music."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'different with' or 'different than' instead of 'different from'.",
            "why": "In standard British English curriculum, the correct preposition after 'different' is always 'from'."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Unit 5: Food and Drink",
        "description": "Traditional Vietnamese dishes, recipes, countable and uncountable nouns, quantifiers (some, any, much, many, a lot of).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Food ingredients and cooking methods", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Quantifiers: Some, Any, How much, How many", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Countable vs. Uncountable Nouns",
            "definition": "Countable nouns can be counted with numbers and have plural forms (apples, eggs); Uncountable nouns cannot be counted directly and take singular verbs (rice, water, flour).",
            "example": "Three eggs (countable) vs. some milk (uncountable).",
            "essence": "Uncountable nouns require units of measurement: a bottle of milk, a bowl of rice."
          }
        ],
        "rules": [
          {
            "statement": "Rules for 'Some' and 'Any'",
            "meaning": "'Some' is used in affirmative sentences and polite offers/requests; 'Any' is used in negative sentences and general questions.",
            "example": "There is some sugar in the jar. / Would you like some tea? / Is there any milk left? / No, there isn't any.",
            "essence": "'Some' expects a positive answer or offers assistance; 'Any' opens open-ended possibilities."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Fill in the blank with 'How much' or 'How many': '__________ bottles of water do you drink each day?'",
            "steps": [
              "Step 1: Identify the noun following the question: 'bottles of water'.",
              "Step 2: 'Bottles' is a plural countable noun.",
              "Step 3: Use 'How many' for countable nouns."
            ],
            "answer": "How many bottles of water do you drink each day?"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Asking 'How many water' because water is an uncountable liquid.",
            "why": "Water cannot be counted directly; ask 'How much water' or 'How many bottles of water'."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Unit 6: Traffic and Future Transport",
        "description": "Road safety rules, road signs, traffic problems in big cities, distances with 'It is... from... to...', and modal verb 'should / shouldn't'.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Traffic signs and road safety vocabulary", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: It is (about)... to indicate distance & Should / Shouldn't", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Distance structure with 'It'",
            "definition": "Structure used to describe distance between two geographical locations: It is (about) + distance + from A to B.",
            "example": "It is about 2 kilometers from my house to school.",
            "essence": "The pronoun 'It' acts as an impersonal subject representing geographical length."
          }
        ],
        "rules": [
          {
            "statement": "Modal verbs 'Should' and 'Shouldn't' for obligation and advice",
            "meaning": "Used to give advice, recommendations, or explain rules. Followed directly by a bare infinitive (without 'to').",
            "example": "You should fasten your seatbelt when driving. / You shouldn't ride a bicycle on the pavement.",
            "essence": "Expresses moral obligation or sound judgment rather than strict legal compulsion (must)."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Make a sentence using the cues: 'It / about / 100 km / Ha Noi / Hai Phong.'",
            "steps": [
              "Step 1: Apply the distance formula: It + is + (about) + [distance] + from [Place A] + to [Place B].",
              "Step 2: Insert the components: 'It is about 100 km from Ha Noi to Hai Phong.'",
              "Step 3: Check subject-verb agreement and punctuation."
            ],
            "answer": "It is about 100 km from Ha Noi to Hai Phong."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Adding 'to' after modal verbs: 'You should to wear a helmet.'",
            "why": "Modal verbs (should, must, can) are followed directly by the bare infinitive verb without 'to': 'You should wear a helmet.'"
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
        "title": "Chủ đề 1: Máy tính và Cộng đồng",
        "description": "Các thiết bị vào - ra của máy tính, hệ điều hành và phần mềm ứng dụng, quản lý tệp và thư mục an toàn.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Thiết bị vào - ra và tương tác với máy tính", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hệ điều hành và quản lý tệp tin khoa học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thiết bị vào - ra (Input/Output Devices)",
            "definition": "Thiết bị vào (bàn phím, chuột, máy quét) dùng để đưa dữ liệu vào máy tính; Thiết bị ra (màn hình, máy in, loa) dùng để xuất thông tin ra ngoài cho người dùng.",
            "example": "Microphone là thiết bị vào âm thanh, tai nghe headphone là thiết bị ra âm thanh.",
            "essence": "Là cầu nối giao tiếp hai chiều giữa con người và thế giới kỹ thuật số của máy tính."
          }
        ],
        "rules": [
          {
            "statement": "Vai trò của Hệ điều hành (Operating System)",
            "meaning": "Hệ điều hành là phần mềm hệ thống quản lý toàn bộ phần cứng, điều khiển tài nguyên máy tính và tạo môi trường để các phần mềm ứng dụng hoạt động.",
            "example": "Windows, macOS, Linux, Android, iOS đều là các hệ điều hành phổ biến.",
            "essence": "Không có hệ điều hành, máy tính chỉ là một khối kim loại và mạch điện vô tri."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 3 quy tắc đặt tên tệp và tổ chức thư mục khoa học để dễ tìm kiếm dữ liệu.",
            "steps": [
              "Bước 1: Đặt tên tệp ngắn gọn, phản ánh đúng nội dung và có mốc thời gian (ví dụ: BaiTapToan_Lop7_20261012.docx).",
              "Bước 2: Tổ chức thư mục theo cấu trúc hình cây phân cấp rõ ràng (Thư mục Cha -> Thư mục Con).",
              "Bước 3: Không dùng các ký tự đặc biệt bị cấm trong tên tệp (/ \\ : * ? \" < > |)."
            ],
            "answer": "Giúp tiết kiệm thời gian tìm kiếm và tránh bị thất lạc dữ liệu quan trọng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lưu tất cả các tệp tài liệu bừa bãi ra màn hình chính (Desktop).",
            "why": "Làm chậm tốc độ khởi động máy tính, màn hình rối mắt và dễ bị mất dữ liệu khi máy tính bị lỗi hệ điều hành."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Tổ chức lưu trữ và Tìm kiếm thông tin",
        "description": "Mạng xã hội và giao tiếp trên Internet, văn hóa ứng xử trên mạng, tìm kiếm thông tin bằng từ khóa chính xác.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Mạng xã hội và giao tiếp an toàn trên không gian mạng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Kĩ năng tìm kiếm thông tin trên Internet với từ khóa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Dấu chân kỹ thuật số (Digital Footprint)",
            "definition": "Là dấu vết dữ liệu mà một người để lại khi hoạt động trên Internet (bài đăng, bình luận, lịch sử duyệt web, ảnh chia sẻ).",
            "example": "Những bình luận hay bức ảnh đăng tải trên mạng xã hội có thể tồn tại vĩnh viễn và ảnh hưởng đến uy tín cá nhân trong tương lai.",
            "essence": "Không có gì trên không gian mạng là hoàn toàn biến mất sau khi đã được tải lên."
          }
        ],
        "rules": [
          {
            "statement": "Kỹ thuật sử dụng từ khóa tìm kiếm chính xác",
            "meaning": "Sử dụng dấu ngoặc kép \"...\" để tìm kiếm chính xác cụm từ; sử dụng dấu trừ (-) để loại bỏ kết quả không mong muốn.",
            "example": "\"Lịch sử Việt Nam thế kỉ X\" sẽ tìm chính xác bài viết có nguyên văn cụm từ đó.",
            "essence": "Từ khóa chính xác giúp lọc bớt hàng triệu kết quả rác trên công cụ tìm kiếm Google."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 3 nguyên tắc bảo mật thông tin cá nhân khi tham gia mạng xã hội.",
            "steps": [
              "Bước 1: Không chia sẻ công khai số điện thoại, địa chỉ nhà riêng, vị trí check-in trực tiếp.",
              "Bước 2: Đặt mật khẩu mạnh (gồm chữ hoa, chữ thường, số, ký tự đặc biệt) và bật xác thực 2 lớp.",
              "Bước 3: Cảnh giác trước các đường link lạ hoặc tin nhắn mượn tiền từ tài khoản bạn bè bị hack."
            ],
            "answer": "Bảo vệ bản thân khỏi nguy cơ bị đánh cắp danh tính và lừa đảo qua mạng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chia sẻ thông tin chưa được kiểm chứng từ các trang tin giả (fake news).",
            "why": "Vi phạm Luật An ninh mạng và có thể gây hoang mang dư luận xã hội."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Bảng tính điện tử (Spreadsheet)",
        "description": "Làm quen với phần mềm bảng tính Excel, địa chỉ ô, nhập dữ liệu, sử dụng các hàm tính toán cơ bản: SUM, AVERAGE, MAX, MIN, COUNT.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Làm quen với giao diện và nhập dữ liệu bảng tính", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sử dụng công thức và các hàm thống kê cơ bản", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Địa chỉ ô tính (Cell Address)",
            "definition": "Được xác định bởi tên cột kết hợp với tên hàng mà ô đó nằm tại vị trí giao nhau.",
            "example": "Ô C5 là ô nằm ở giao điểm của cột C và hàng 5.",
            "essence": "Địa chỉ ô cho phép thiết lập các công thức tự động cập nhật khi dữ liệu thay đổi."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc bắt đầu công thức trong bảng tính",
            "meaning": "Mọi công thức hoặc hàm tính toán trong bảng tính đều bắt buộc phải bắt đầu bằng dấu bằng '='.",
            "example": "=SUM(A1:A10) hoặc =B2 * C2.",
            "essence": "Dấu '=' báo hiệu cho phần mềm biết đây là một phép toán cần xử lý chứ không phải văn bản thuần túy."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Viết công thức tính điểm trung bình môn của học sinh có điểm Toán ở ô C3, Văn ở ô D3, Anh ở ô E3.",
            "steps": [
              "Bước 1: Sử dụng hàm AVERAGE tính trung bình cộng.",
              "Bước 2: Xác định vùng dữ liệu từ C3 đến E3 (kí hiệu là C3:E3).",
              "Bước 3: Viết công thức hoàn chỉnh: =AVERAGE(C3:E3)."
            ],
            "answer": "=AVERAGE(C3:E3) hoặc =(C3+D3+E3)/3"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên dấu '=' ở đầu công thức, khiến phần mềm chỉ hiển thị dòng chữ SUM(A1:A5) mà không tính ra kết quả.",
            "why": "Nếu thiếu dấu bằng, ô tính sẽ coi đó là chuỗi ký tự văn bản thông thường."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Thuật toán tìm kiếm và Sắp xếp",
        "description": "Thuật toán tìm kiếm tuần tự (Sequential Search), thuật toán tìm kiếm nhị phân (Binary Search), thuật toán sắp xếp nổi bọt (Bubble Sort).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Thuật toán tìm kiếm tuần tự và tìm kiếm nhị phân", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thuật toán sắp xếp nổi bọt và sắp xếp chọn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thuật toán tìm kiếm nhị phân",
            "definition": "Là thuật toán tìm kiếm trên danh sách ĐÃ ĐƯỢC SẮP XẾP bằng cách liên tục so sánh giá trị cần tìm với phần tử ở giữa, loại bỏ một nửa danh sách không chứa phần tử sau mỗi bước.",
            "example": "Tìm từ trong cuốn từ điển dày: Mở trang chính giữa, so sánh chữ cái đầu để quyết định tìm tiếp ở nửa trước hay nửa sau.",
            "essence": "Tốc độ tìm kiếm cực nhanh, giảm một nửa không gian tìm kiếm sau mỗi lần lặp."
          }
        ],
        "rules": [
          {
            "statement": "Điều kiện tiên quyết áp dụng tìm kiếm nhị phân",
            "meaning": "Thuật toán tìm kiếm nhị phân CHỈ ÁP DỤNG ĐƯỢC khi dãy dữ liệu đầu vào đã được sắp xếp theo thứ tự tăng dần hoặc giảm dần.",
            "example": "Nếu dãy số lộn xộn (7, 2, 9, 1), bắt buộc phải dùng tìm kiếm tuần tự hoặc sắp xếp lại trước.",
            "essence": "Quy luật thứ tự là chìa khóa để biết chắc chắn phần tử cần tìm nằm ở nửa bên trái hay nửa bên phải."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho dãy số tăng dần: [2, 5, 8, 12, 16, 23, 38]. Mô tả các bước tìm số 16 bằng thuật toán tìm kiếm nhị phân.",
            "steps": [
              "Bước 1: Phần tử ở giữa dãy là 12 (vị trí 4). So sánh: 16 > 12 nên bỏ nửa trái [2, 5, 8, 12], xét nửa phải [16, 23, 38].",
              "Bước 2: Phần tử ở giữa nửa phải là 23. So sánh: 16 < 23 nên bỏ nửa phải [23, 38], xét phần tử bên trái là 16.",
              "Bước 3: So sánh: 16 = 16. Tìm thấy phần tử tại vị trí 5 sau 2 lần so sánh."
            ],
            "answer": "Tìm thấy số 16 tại vị trí thứ 5 sau 2 bước lặp."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Áp dụng tìm kiếm nhị phân cho một danh sách chưa được sắp xếp thứ tự.",
            "why": "Khi danh sách chưa có thứ tự, việc bỏ qua một nửa danh sách sẽ dẫn đến nguy cơ bỏ sót phần tử cần tìm."
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
        "title": "Bài 1: Tự hào về truyền thống quê hương",
        "description": "Nhận thức về truyền thống yêu nước, hiếu học, đoàn kết, cần cù của quê hương và trách nhiệm phát huy giá trị tốt đẹp đó.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khám phá các truyền thống tốt đẹp của quê hương", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Trách nhiệm của học sinh trong giữ gìn truyền thống", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Truyền thống quê hương",
            "definition": "Là những giá trị văn hóa, tinh thần, đạo đức, nghề thủ công tốt đẹp được hình thành và trao truyền qua nhiều thế hệ tại một địa phương.",
            "example": "Làng gốm Bát Tràng (Hà Nội), lễ hội đua thuyền (Đà Nẵng), truyền thống hiếu học đất học Nam Đàn (Nghệ An).",
            "essence": "Truyền thống là cội nguồn tạo nên bản sắc và niềm tự hào của mỗi người con sinh ra trên mảnh đất quê hương."
          }
        ],
        "rules": [
          {
            "statement": "Hành động thiết thực phát huy truyền thống quê hương",
            "meaning": "Không dừng lại ở lời nói tự hào mà phải biến thành hành động cụ thể: Nỗ lực học tập tốt, tôn trọng di tích lịch sử và quảng bá văn hóa địa phương đến bạn bè muôn phương.",
            "example": "Tham gia đội tình nguyện chăm sóc nghĩa trang liệt sĩ, giới thiệu đặc sản quê hương trên mạng xã hội văn minh.",
            "essence": "Truyền thống chỉ sống mãi khi được thế hệ trẻ tiếp nối bằng sự sáng tạo và cống hiến thực chất."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một người bạn chê bai trang phục truyền thống của dân tộc mình là lạc hậu. Em sẽ ứng xử như thế nào?",
            "steps": [
              "Bước 1: Giữ thái độ bình tĩnh, tự tin, không cáu gắt hay đối đầu bạo lực.",
              "Bước 2: Giải thích cho bạn hiểu ý nghĩa hoa văn, chất liệu và bề dày lịch sử ngàn năm kết tinh trong bộ trang phục.",
              "Bước 3: Mời bạn cùng trải nghiệm mặc thử trang phục truyền thống trong ngày hội văn hóa trường học."
            ],
            "answer": "Bảo vệ giá trị văn hóa bằng sự tự tin, hiểu biết và thái độ hòa nhã, thuyết phục."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Mặc cảm, tự ti về nguồn gốc xuất thân nông thôn hoặc phong tục tập quán mộc mạc của quê mình.",
            "why": "Mọi vùng quê đều có vẻ đẹp và giá trị riêng biệt; người có lòng tự trọng luôn biết trân quý nguồn cội của mình."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Bài 2: Quan tâm, cảm thông và chia sẻ",
        "description": "Ý nghĩa của sự quan tâm, thấu cảm và sẻ chia đối với những người xung quanh, rèn luyện lối sống yêu thương, nhân ái.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Giá trị của sự quan tâm, cảm thông và chia sẻ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Rèn luyện kỹ năng lắng nghe và giúp đỡ người yếu thế", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Sự cảm thông (Empathy)",
            "definition": "Là khả năng hiểu và cảm nhận được nỗi buồn, niềm vui và hoàn cảnh khó khăn của người khác từ góc nhìn của chính họ.",
            "example": "Khi thấy bạn trong lớp buồn vì điểm kém, không trêu chọc mà ngồi cạnh an ủi và đề nghị kèm bạn học nhóm.",
            "essence": "Cảm thông là nhịp cầu xóa nhòa sự vô cảm và gắn kết con người lại gần nhau hơn."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc chia sẻ tế nhị, bảo vệ lòng tự trọng",
            "meaning": "Khi giúp đỡ người khác, phải xuất phát từ sự chân thành, kín đáo và tôn trọng phẩm giá của họ; tuyệt đối không ban ơn hay làm tổn thương người nhận.",
            "example": "Quyên góp quần áo ấm sạch sẽ, gấp gọn gàng trao tận tay thay vì vứt bỏ đồ cũ rách rưới.",
            "essence": "Cách cho quý hơn của đem cho."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trong lớp có một bạn khuyết tật vận động gặp khó khăn khi leo cầu thang. Em và các bạn nên làm gì?",
            "steps": [
              "Bước 1: Chủ động hỏi bạn xem bạn có cần hỗ trợ không trước khi hành động.",
              "Bước 2: Luân phiên giúp bạn xách cặp sách và hỗ trợ dìu bạn đi lại an toàn.",
              "Bước 3: Đề xuất với thầy cô chuyển phòng học xuống tầng 1 để tạo thuận lợi cho bạn hòa nhập."
            ],
            "answer": "Hành động yêu thương thiết thực giúp bạn cảm nhận được sự ấm áp của tập thể lớp."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Giúp đỡ người khác nhằm mục đích khoe khoang trên mạng xã hội để lấy lời khen ngợi.",
            "why": "Lòng tốt đích thực không cần phô trương; sự vị kỷ làm mất đi vẻ đẹp thuần khiết của lòng nhân ái."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Bài 3: Học tập tự giác, tích cực và Giữ chữ tín",
        "description": "Rèn luyện tính tự giác, tinh thần chủ động trong học tập, ý nghĩa của việc giữ lời hứa và xây dựng niềm tin xã hội.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phương pháp học tập tự giác và tích cực", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Giữ chữ tín — Nền tảng của danh dự cá nhân", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Giữ chữ tín",
            "definition": "Là coi trọng lòng tin của mọi người đối với mình, biết giữ lời hứa và tin tưởng lẫn nhau trong công việc và cuộc sống.",
            "example": "Đã hẹn bạn 8 giờ sáng cùng làm bài tập nhóm thì đúng 8 giờ có mặt, không trễ hẹn vì lý do cá nhân.",
            "essence": "Chữ tín là danh dự, là tài sản vô giá khẳng định nhân cách của một con người."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc 'Một lần bất tín, vạn lần bất tin'",
            "meaning": "Một lần không giữ lời hứa sẽ đánh mất niềm tin của người khác, và rất khó để lấy lại được niềm tin đó dù có giải thích bằng ngàn lời.",
            "example": "Hứa nộp bài tập đúng hạn nhưng nhiều lần viện cớ quên sẽ khiến thầy cô và bạn bè không còn tin tưởng giao phó nhiệm vụ quan trọng.",
            "essence": "Xây dựng chữ tín mất cả đời, nhưng phá hủy nó chỉ trong một khoảnh khắc bội ước."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nếu vì sự cố bất khả kháng (như hỏng xe giữa đường) khiến em không thể đến đúng giờ hẹn với nhóm, em cần xử lý thế nào?",
            "steps": [
              "Bước 1: Gọi điện thoại báo ngay cho bạn bè trong nhóm biết tình hình, thành thật giải thích lý do.",
              "Bước 2: Ước lượng thời gian khắc phục và xin lỗi vì làm gián đoạn kế hoạch chung của nhóm.",
              "Bước 3: Chủ động nhận phần việc bù đắp sau buổi học để thể hiện trách nhiệm."
            ],
            "answer": "Xử lý trung thực, trách nhiệm giúp giữ gìn chữ tín và sự thông cảm của bạn bè."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Hứa bừa, hứa suông để người khác vừa lòng mà không hề có ý định thực hiện lời hứa.",
            "why": "Thói quen hứa suông bào mòn nhân cách và biến bản thân thành người dối trá, không đáng tin cậy."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Bài 4: Quản lý tiền và Ứng phó căng thẳng",
        "description": "Kỹ năng lập kế hoạch chi tiêu hợp lý, phân biệt nhu cầu và mong muốn, kỹ thuật giải tỏa căng thẳng tâm lý tuổi dậy thì.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Quản lý tiền thông minh và thói quen tiết kiệm", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Nhận diện và ứng phó với áp lực tâm lý học đường", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Nhu cầu (Needs) và Mong muốn (Wants)",
            "definition": "Nhu cầu là những thứ thiết yếu để sinh tồn và học tập (sách vở, ăn uống, quần áo giản dị); Mong muốn là những thứ sở thích nếu không có vẫn sống tốt (đồ chơi đắt tiền, điện thoại xịn, trà sữa mỗi ngày).",
            "example": "Mua bữa sáng no bụng là Nhu cầu; mua chiếc áo hàng hiệu đắt đỏ là Mong muốn.",
            "essence": "Biết phân biệt Nhu cầu và Mong muốn là bước đầu tiên để không rơi vào bẫy chi tiêu phung phí."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc chi tiêu 'Nhu cầu trước - Mong muốn sau'",
            "meaning": "Chỉ chi tiền cho các món đồ mong muốn sau khi đã đảm bảo toàn bộ các nhu cầu thiết yếu và trích một phần vào quỹ tiết kiệm dự phòng.",
            "example": "Dành tiền tiêu vặt mua đủ dụng cụ học tập trước, phần còn dư mới cân nhắc mua truyện tranh.",
            "essence": "Kỷ luật tài chính tạo ra sự an tâm và độc lập tự chủ trong cuộc sống."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Học sinh lớp 7 cảm thấy vô cùng căng thẳng (stress) trước kỳ thi học kỳ. Nêu 3 bước tự giải tỏa áp lực hiệu quả.",
            "steps": [
              "Bước 1: Lập thời gian biểu ôn tập rõ ràng từng môn, chia nhỏ mục tiêu mỗi ngày 1 chương để không bị ngợp.",
              "Bước 2: Vận động thể thao nhẹ nhàng 30 phút (đi bộ, đạp xe, nghe nhạc thư giãn) và ngủ đủ 8 tiếng/ngày.",
              "Bước 3: Chia sẻ lo lắng với cha mẹ, thầy cô hoặc bạn bè thân thiết để nhận được lời động viên tích cực."
            ],
            "answer": "Giải tỏa áp lực bằng kế hoạch học tập khoa học và chế độ sinh hoạt cân bằng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Giấu kín cảm xúc tiêu cực, thu mình trong phòng hoặc lạm dụng chơi game thâu đêm để trốn tránh áp lực.",
            "why": "Trốn tránh không giải quyết được vấn đề mà còn làm suy kiệt sức khỏe tinh thần và thể chất."
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
        "title": "Chương 1: Trồng trọt đại cương",
        "description": "Vai trò của trồng trọt, các nhóm cây trồng phổ biến, phương pháp nhân giống vô tính (giâm cành, ghép cành, chiết cành).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Giới thiệu về trồng trọt và các nhóm cây trồng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các phương pháp nhân giống vô tính cây trồng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Giâm cành",
            "definition": "Là phương pháp nhân giống vô tính bằng cách cắt một đoạn cành bánh tẻ từ cây mẹ cắm vào giá thể ẩm để cành ra rễ và phát triển thành cây mới.",
            "example": "Nhân giống hoa hồng, rau ngót, cây khoai lang bằng phương pháp giâm cành.",
            "essence": "Giữ nguyên vẹn các đặc tính di truyền quý giá của cây mẹ và cho thu hoạch nhanh hơn gieo hạt."
          }
        ],
        "rules": [
          {
            "statement": "Tiêu chuẩn chọn cành giâm đạt tỉ lệ sống cao",
            "meaning": "Chọn cành bánh tẻ (không quá non, không quá già), khỏe mạnh, sạch sâu bệnh, cắt vát góc 45 độ để tăng diện tích tiếp xúc hút nước.",
            "example": "Cắt cành hoa hồng vào sáng sớm, nhúng gốc vào dung dịch kích thích ra rễ trước khi cắm vào đất cát ẩm.",
            "essence": "Cành bánh tẻ có sức sống tế bào mạnh mẽ nhất để phân chia tạo mô sẹo và rễ mới."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày 4 bước thực hiện phương pháp chiết cành cây ăn quả (như bưởi, cam).",
            "steps": [
              "Bước 1: Chọn cành chiết: Cành bánh tẻ ở tầng tán giữa, đường kính 1-1,5 cm, nhiều ánh sáng.",
              "Bước 2: Khoanh vỏ: Dùng dao sắc khoanh 2 vòng cách nhau 3-5 cm, bóc sạch lớp vỏ và cạo sạch lớp tượng tầng nhầy.",
              "Bước 3: Bó bầu đất: Dùng đất mùn ẩm trộn rơm rác bọc quanh vết khoanh, bọc kín bên ngoài bằng màng nilon trong suốt buộc chặt 2 đầu.",
              "Bước 4: Cắt cành trồng: Sau 1-2 tháng rễ mọc trắng quanh bầu đất thì cắt cành đem trồng vào bầu ươm."
            ],
            "answer": "Chiết cành giúp cây nhanh ra quả và giữ nguyên phẩm chất ngọt thơm của cây mẹ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Không cạo sạch lớp tượng tầng (lớp nhầy) trên thân gỗ sau khi bóc vỏ cành chiết.",
            "why": "Nếu để sót tượng tầng, vỏ cây sẽ tự liền sẹo nối lại mà không kích thích rễ mới mọc ra ở mép trên vết cắt."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Kỹ thuật Trồng và Chăm sóc cây trồng",
        "description": "Kỹ thuật làm đất, bón phân, tưới nước, phòng trừ sâu bệnh hại theo hướng an toàn sinh học và thu hoạch nông sản.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Làm đất, bón phân và gieo trồng cây nông nghiệp", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phòng trừ sâu bệnh hại bằng biện pháp sinh học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Biện pháp sinh học trong bảo vệ thực vật",
            "definition": "Là việc sử dụng các loài thiên địch (bọ rùa, ong ký sinh, nấm đối kháng Trichoderma) hoặc chế phẩm vi sinh để tiêu diệt sâu bệnh mà không dùng hóa chất độc hại.",
            "example": "Nuôi thả bọ rùa để ăn rệp sáp hại cây có múi; phun thuốc trừ sâu sinh học thảo mộc từ tỏi ớt gừng.",
            "essence": "Bảo vệ cân bằng sinh thái, tạo ra nông sản sạch và an toàn cho sức khỏe người tiêu dùng."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc bón lót và bón thúc",
            "meaning": "Bón lót (bằng phân hữu cơ ủ hoai mục) được thực hiện trước khi gieo trồng để cải tạo đất; Bón thúc (bằng phân hóa học dễ tan) thực hiện trong các giai đoạn sinh trưởng mạnh.",
            "example": "Trộn phân chuồng hoai mục vào luống đất trước khi trồng cà chua; khi cây ra hoa bón thúc phân NPK.",
            "essence": "Cung cấp dinh dưỡng đúng nhịp điệu phát triển sinh lý của cây trồng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vì sao cần thu hoạch rau quả đúng thời điểm và tránh thu hoạch vào lúc trời nắng gắt?",
            "steps": [
              "Bước 1: Đúng thời điểm: Đảm bảo hàm lượng dinh dưỡng và vitamin đạt mức cao nhất, không quá non (ít chất) hoặc quá già (nhiều xơ cứng).",
              "Bước 2: Tránh nắng gắt: Trời nắng làm nông sản bốc hơi nước nhanh, lá rau bị héo úa, giảm phẩm cấp và khó bảo quản.",
              "Bước 3: Thời điểm tốt nhất: Thu hoạch vào sáng sớm mát mẻ hoặc chiều muộn khi cây đã tích lũy đủ chất đồng hóa."
            ],
            "answer": "Giữ trọn độ tươi ngon, chất lượng dinh dưỡng và giá trị kinh tế của nông sản."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Bón phân hữu cơ tươi (chưa qua ủ hoai mục) trực tiếp vào gốc cây trồng.",
            "why": "Phân tươi lên men sinh nhiệt làm cháy rễ cây và mang theo nhiều mầm bệnh nấm, vi khuẩn có hại vào đất."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Chăn nuôi Gia súc và Gia cầm",
        "description": "Vai trò của chăn nuôi, các giống vật nuôi phổ biến, chuồng nuôi hợp vệ sinh, thức ăn chăn nuôi và phòng dịch bệnh gia súc, gia cầm.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Giống vật nuôi và kỹ thuật nuôi dưỡng chăm sóc", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Vệ sinh phòng bệnh trong chăn nuôi an toàn sinh học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chăn nuôi an toàn sinh học",
            "definition": "Là các biện pháp kỹ thuật nhằm ngăn chặn sự xâm nhập và lây lan của mầm bệnh từ bên ngoài vào khu vực chăn nuôi và ngược lại.",
            "example": "Trại gà có hố vôi sát trùng ở cổng, rào lưới chống chim hoang dã, tiêm phòng vắc-xin định kỳ đầy đủ.",
            "essence": "Chủ động phòng bệnh từ gốc để hạn chế tối đa việc sử dụng kháng sinh."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc xây dựng chuồng nuôi gia súc, gia cầm",
            "meaning": "Chuồng nuôi phải thoáng mát về mùa hè, ấm áp về mùa đông; hướng chuồng tốt nhất là hướng Nam hoặc Đông Nam để đón gió mát và ánh nắng buổi sáng.",
            "example": "Chuồng lợn có nền dốc nhẹ 2-3% về phía rãnh thoát nước thải dẫn vào hầm biogas xử lý chất thải.",
            "essence": "Môi trường sống sạch sẽ quyết định 70% sức đề kháng và tốc độ tăng trọng của vật nuôi."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày lợi ích kép của việc xây dựng hầm khí sinh học (Biogas) trong xử lý chất thải chăn nuôi.",
            "steps": [
              "Bước 1: Lợi ích môi trường: Phân giải toàn bộ chất thải hữu cơ, tiêu diệt vi khuẩn gây bệnh, giảm thiểu mùi hôi và không ô nhiễm nguồn nước ngầm.",
              "Bước 2: Lợi ích kinh tế năng lượng: Tạo ra khí gas sinh học (CH4) phục vụ đun nấu, thắp sáng miễn phí thay thế củi và điện.",
              "Bước 3: Lợi ích nông nghiệp: Nước thải sau hầm biogas là nguồn phân bón hữu cơ sinh học tuyệt vời cho cây trồng."
            ],
            "answer": "Mô hình kinh tế tuần hoàn bền vững, vừa bảo vệ môi trường vừa tiết kiệm chi phí sinh hoạt."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lạm dụng thuốc kháng sinh trộn vào thức ăn hàng ngày nhằm mục đích kích thích tăng trọng.",
            "why": "Gây ra hiện tượng kháng kháng sinh nguy hiểm, để lại tồn dư kháng sinh trong thịt gây hại cho sức khỏe người tiêu dùng."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Nuôi thủy sản bền vững",
        "description": "Môi trường nuôi thủy sản, kỹ thuật nuôi cá nước ngọt, bảo vệ nguồn lợi thủy sản và ứng dụng công nghệ cao trong nuôi trồng thủy sản.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Quản lý môi trường ao nuôi thủy sản nước ngọt", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Chăm sóc, phòng bệnh và thu hoạch cá an toàn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hàm lượng oxy hòa tan (DO) trong nước ao",
            "definition": "Là lượng khí oxy hòa tan trong nước cần thiết cho sự hô hấp của cá và các sinh vật thủy sinh. Tiêu chuẩn tốt cho cá nước ngọt là từ 4-6 mg/lít.",
            "example": "Vào sáng sớm hoặc ngày trời âm u, cá nổi đầu lên mặt nước đớp khí là dấu hiệu thiếu oxy trầm trọng.",
            "essence": "Oxy hòa tan là yếu tố sống còn quyết định sự tồn tại và khả năng tiêu hóa thức ăn của đàn cá."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc cho cá ăn '4 định'",
            "meaning": "Định lượng (vừa đủ không thừa), Định chất (thức ăn tươi ngon đủ đạm), Định vị trí (ăn đúng điểm cố định), và Định thời gian (ăn đúng giờ vào buổi sáng mát).",
            "example": "Không cho cá ăn quá nhiều vào buổi trưa nắng gắt hoặc ban đêm khi hàm lượng oxy trong ao đang xuống thấp.",
            "essence": "Thức ăn thừa phân hủy dưới đáy ao là thủ phạm số một làm ô nhiễm nước và bùng phát dịch bệnh."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Khi thấy ao cá có hiện tượng nổi đầu đớp khí vào sáng sớm, người nuôi cần làm gì ngay lập tức?",
            "steps": [
              "Bước 1: Bật máy quạt nước hoặc máy sục khí oxy khẩn cấp để tạo dòng chảy và bổ sung oxy hòa tan.",
              "Bước 2: Cấp thêm nước mới sạch vào ao để làm mát và giảm nồng độ khí độc.",
              "Bước 3: Ngừng cho cá ăn bữa sáng cho đến khi cá bơi lặn trở lại bình thường dưới đáy ao."
            ],
            "answer": "Bật quạt nước sục khí, cấp nước mới và tạm dừng cho ăn."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đánh bắt thủy sản bằng chất độc, xung điện hoặc mắt lưới quá nhỏ.",
            "why": "Vi phạm nghiêm trọng Luật Thủy sản, tiêu diệt cả cá con và sinh vật đáy, làm hủy hoại vĩnh viễn nguồn lợi thủy sản tự nhiên."
          }
        ]
      }
    ]
  }
}

# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa 8 môn học Lớp 9 SGK Kết nối tri thức với cuộc sống 2026-2027:
- Toán học (6 chương trọng tâm ôn thi vào 10)
- Khoa học tự nhiên (6 chương: Hóa hữu cơ, Kim loại, Quang học, Điện từ, Di truyền học)
- Ngữ văn (5 bài trọng tâm văn học và kỹ năng viết nghị luận)
- Lịch sử & Địa lí (5 chương: Lịch sử hiện đại và Địa lí kinh tế các vùng)
- Tiếng Anh (6 units Global Success chuẩn cấu trúc ôn thi tuyển sinh 10)
- Tin học (4 chủ đề)
- Giáo dục công dân (4 bài)
- Công nghệ (4 chương định hướng nghề nghiệp và kĩ thuật điện)
"""

true = True
false = False
null = None

GRADE_09_SUBJECTS = {
  "toan": {
    "id": "toan",
    "name": "Toán học",
    "icon": "📐",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Phương trình và Hệ hai phương trình bậc nhất hai ẩn",
        "description": "Phương trình bậc nhất hai ẩn, hệ hai phương trình bậc nhất hai ẩn, phương pháp thế, phương pháp cộng đại số, giải bài toán bằng cách lập hệ phương trình.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái niệm phương trình và hệ hai phương trình bậc nhất hai ẩn", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phương pháp thế và phương pháp cộng đại số", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Giải bài toán bằng cách lập hệ phương trình", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hệ hai phương trình bậc nhất hai ẩn",
            "definition": "Là hệ phương trình có dạng { ax + by = c; a'x + b'y = c' }, trong đó a, b không đồng thời bằng 0 và a', b' không đồng thời bằng 0.",
            "example": "Hệ { 2x + y = 5; x - y = 1 } có nghiệm duy nhất là cặp số (x; y) = (2; 1).",
            "essence": "Mỗi phương trình bậc nhất hai ẩn biểu diễn một đường thẳng trên mặt phẳng tọa độ; nghiệm của hệ tương ứng với tọa độ giao điểm của hai đường thẳng."
          },
          {
            "term": "Nghiệm của hệ phương trình",
            "definition": "Cặp số (x0; y0) đồng thời thỏa mãn cả hai phương trình của hệ được gọi là nghiệm của hệ phương trình.",
            "example": "Với cặp (2; 1): 2*(2) + 1 = 5 (đúng) và 2 - 1 = 1 (đúng), do đó (2; 1) là nghiệm của hệ.",
            "essence": "Hệ có thể có nghiệm duy nhất (hai đường cắt nhau), vô nghiệm (hai đường song song), hoặc vô số nghiệm (hai đường trùng nhau)."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc giải hệ bằng phương pháp cộng đại số",
            "meaning": "Nhân hai vế của mỗi phương trình với hệ số thích hợp để hệ số của cùng một ẩn bằng nhau hoặc đối nhau, rồi cộng hoặc trừ từng vế hai phương trình để triệt tiêu ẩn đó.",
            "example": "Với { 2x + 3y = 7; 2x - y = 3 }, lấy phương trình (1) trừ (2) ta được: 4y = 4 => y = 1, thế vào tìm x = 2.",
            "essence": "Mục tiêu tối thượng là khử đi một ẩn để quy về phương trình bậc nhất một ẩn dễ giải."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Giải bài toán bằng cách lập hệ phương trình: Hai tổ sản xuất cùng làm thì sau 12 giờ hoàn thành công việc. Nếu tổ 1 làm 4 giờ rồi tổ 2 làm tiếp 10 giờ thì được 7/12 công việc. Hỏi mỗi tổ làm một mình mất bao lâu?",
            "steps": [
              "Bước 1: Gọi thời gian tổ 1 làm một mình xong việc là x (giờ), tổ 2 là y (giờ) với điều kiện x, y > 12.",
              "Bước 2: Trong 1 giờ, tổ 1 làm được 1/x công việc, tổ 2 làm được 1/y công việc. Hai tổ cùng làm 12 giờ xong nên: 1/x + 1/y = 1/12.",
              "Bước 3: Tổ 1 làm 4 giờ và tổ 2 làm 10 giờ được: 4/x + 10/y = 7/12.",
              "Bước 4: Đặt u = 1/x, v = 1/y, ta có hệ: { u + v = 1/12; 4u + 10v = 7/12 }. Giải hệ tìm được u = 1/20, v = 1/30.",
              "Bước 5: Suy ra x = 20 (thỏa mãn) và y = 30 (thỏa mãn)."
            ],
            "answer": "Tổ 1 làm một mình hết 20 giờ, tổ 2 làm một mình hết 30 giờ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên đặt điều kiện cho ẩn số (x, y > 12) hoặc quên đổi đơn vị thời gian trước khi lập phương trình.",
            "why": "Bài toán năng suất yêu cầu ẩn số phải dương và công suất một giờ là nghịch đảo của thời gian hoàn thành."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Phương trình bậc hai một ẩn và Hệ thức Viète",
        "description": "Phương trình bậc hai một ẩn, biệt thức Delta và Delta', định lí Viète và ứng dụng tìm hai số biết tổng và tích, phân loại nghiệm.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Công thức nghiệm và công thức nghiệm thu gọn của phương trình bậc hai", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Định lí Viète và các ứng dụng giải toán", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Biệt thức Delta (Δ)",
            "definition": "Với phương trình ax^2 + bx + c = 0 (a ≠ 0), biệt thức Delta được tính bởi công thức: Δ = b^2 - 4ac.",
            "example": "Phương trình x^2 - 5x + 6 = 0 có a = 1, b = -5, c = 6 => Δ = (-5)^2 - 4*1*6 = 25 - 24 = 1 > 0.",
            "essence": "Dấu của Δ quyết định số nghiệm thực: Δ > 0 phương trình có 2 nghiệm phân biệt; Δ = 0 có nghiệm kép; Δ < 0 vô nghiệm."
          },
          {
            "term": "Hệ thức Viète",
            "definition": "Nếu phương trình ax^2 + bx + c = 0 (a ≠ 0) có hai nghiệm x1, x2 thì: x1 + x2 = -b/a và x1 * x2 = c/a.",
            "example": "Phương trình x^2 - 7x + 12 = 0 có S = x1 + x2 = 7 và P = x1 * x2 = 12 => Hai nghiệm là x1 = 3, x2 = 4.",
            "essence": "Định lí Viète cho phép tính tổng và tích nghiệm mà không cần giải phương trình, đồng thời lập phương trình khi biết hai nghiệm."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc tìm hai số biết tổng S và tích P",
            "meaning": "Nếu hai số có tổng bằng S và tích bằng P thì hai số đó là nghiệm của phương trình: X^2 - SX + P = 0. Điều kiện để có hai số là S^2 - 4P ≥ 0.",
            "example": "Tìm hai số có tổng S = 9 và tích P = 20: Phương trình X^2 - 9X + 20 = 0 có hai nghiệm X = 4 và X = 5.",
            "essence": "Chuyển bài toán tìm hai số về giải phương trình bậc hai một ẩn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho phương trình x^2 - 2(m - 1)x + m^2 - 3 = 0. Tìm m để phương trình có hai nghiệm x1, x2 thỏa mãn: x1^2 + x2^2 = 10.",
            "steps": [
              "Bước 1: Tính Δ' = (m - 1)^2 - (m^2 - 3) = m^2 - 2m + 1 - m^2 + 3 = 4 - 2m. Để có hai nghiệm: Δ' ≥ 0 <=> 4 - 2m ≥ 0 <=> m ≤ 2.",
              "Bước 2: Theo Viète: x1 + x2 = 2(m - 1) và x1 * x2 = m^2 - 3.",
              "Bước 3: Biến đổi biểu thức: x1^2 + x2^2 = (x1 + x2)^2 - 2x1*x2 = 4(m - 1)^2 - 2(m^2 - 3) = 4(m^2 - 2m + 1) - 2m^2 + 6 = 2m^2 - 8m + 10.",
              "Bước 4: Cho 2m^2 - 8m + 10 = 10 <=> 2m^2 - 8m = 0 <=> 2m(m - 4) = 0 <=> m = 0 hoặc m = 4.",
              "Bước 5: Đối chiếu điều kiện m ≤ 2, ta nhận m = 0 và loại m = 4."
            ],
            "answer": "Giá trị cần tìm là m = 0."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên đối chiếu điều kiện tồn tại hai nghiệm (Δ ≥ 0 hoặc Δ' ≥ 0) sau khi tìm ra giá trị tham số m.",
            "why": "Nếu Δ < 0 thì phương trình không có nghiệm thực, các hệ thức Viète trở nên vô nghĩa trên tập số thực."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Căn bậc hai và Căn bậc ba",
        "description": "Căn bậc hai số học, hằng đẳng thức căn(A^2) = |A|, liên hệ giữa phép nhân/chia và phép khai phương, biến đổi đơn giản và rút gọn biểu thức chứa căn.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Căn bậc hai số học và hằng đẳng thức căn(A^2) = |A|", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các phép biến đổi đơn giản biểu thức chứa căn thức bậc hai", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Căn bậc hai số học",
            "definition": "Với số dương a, số căn(a) được gọi là căn bậc hai số học của a. Số 0 có căn bậc hai số học là 0.",
            "example": "Căn bậc hai số học của 25 là 5 (vì 5 ≥ 0 và 5^2 = 25). Chú ý: số 25 có hai căn bậc hai là 5 và -5.",
            "essence": "Kí hiệu căn(a) luôn chỉ giá trị không âm (căn bậc hai số học)."
          },
          {
            "term": "Hằng đẳng thức căn(A^2) = |A|",
            "definition": "Với mọi biểu thức A, ta có căn(A^2) = |A| = A (nếu A ≥ 0) hoặc -A (nếu A < 0).",
            "example": "căn((1 - căn(3))^2) = |1 - căn(3)| = căn(3) - 1 (vì 1 < căn(3)).",
            "essence": "Tuyệt đối không được bỏ dấu căn mà quên lấy dấu giá trị tuyệt đối khi chưa biết dấu của A."
          }
        ],
        "rules": [
          {
            "statement": "Trục căn thức ở mẫu",
            "meaning": "Nhân cả tử và mẫu với biểu thức liên hợp để làm mất căn thức ở mẫu số: 1 / (căn(a) - căn(b)) = (căn(a) + căn(b)) / (a - b) với a, b ≥ 0, a ≠ b.",
            "example": "1 / (căn(3) - 1) = (căn(3) + 1) / ((căn(3) - 1)(căn(3) + 1)) = (căn(3) + 1) / 2.",
            "essence": "Ứng dụng hằng đẳng thức hiệu hai bình phương (A - B)(A + B) = A^2 - B^2 để khử dấu căn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rút gọn biểu thức P = [ (căn(x)/(căn(x) - 2)) - (4/(x - 2căn(x))) ] : (1/(căn(x) - 2)) với x > 0, x ≠ 4.",
            "steps": [
              "Bước 1: Nhận xét mẫu số: x - 2căn(x) = căn(x)*(căn(x) - 2). Mẫu thức chung là căn(x)*(căn(x) - 2).",
              "Bước 2: Quy đồng trong ngoặc: [ căn(x)*căn(x) - 4 ] / [ căn(x)*(căn(x) - 2) ] = (x - 4) / [ căn(x)*(căn(x) - 2) ].",
              "Bước 3: Phân tích tử số x - 4 = (căn(x) - 2)*(căn(x) + 2). Biểu thức trong ngoặc thành: (căn(x) + 2) / căn(x).",
              "Bước 4: Thực hiện phép chia: [ (căn(x) + 2) / căn(x) ] * (căn(x) - 2) = (x - 4) / căn(x)."
            ],
            "answer": "P = (x - 4) / căn(x)"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Viết căn((2 - căn(5))^2) = 2 - căn(5).",
            "why": "Vì 2 < căn(5) nên 2 - căn(5) < 0, trong khi căn bậc hai luôn là số không âm. Kết quả đúng phải là |2 - căn(5)| = căn(5) - 2."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Hệ thức lượng trong tam giác vuông",
        "description": "Hệ thức về cạnh và đường cao trong tam giác vuông, tỉ số lượng giác của góc nhọn (sin, cos, tan, cot), hệ thức về cạnh và góc, giải tam giác vuông.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Một số hệ thức về cạnh và đường cao trong tam giác vuông", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tỉ số lượng giác của góc nhọn và ứng dụng thực tế", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hệ thức đường cao và hình chiếu",
            "definition": "Trong tam giác vuông ABC vuông tại A, đường cao AH: h^2 = b'*c' (AH^2 = BH*CH) và a*h = b*c (BC*AH = AB*AC).",
            "example": "Nếu BH = 4 cm, CH = 9 cm thì AH^2 = 4*9 = 36 => AH = 6 cm.",
            "essence": "Mối liên hệ giữa các cạnh góc vuông, cạnh huyền và hình chiếu giúp tính toán nhanh khoảng cách mà không cần dựng hình phức tạp."
          },
          {
            "term": "Tỉ số lượng giác góc nhọn",
            "definition": "sin = đối/huyền, cos = kề/huyền, tan = đối/kề, cot = kề/đối. Góc phụ nhau: sin(α) = cos(90° - α), tan(α) = cot(90° - α).",
            "example": "Tam giác vuông có góc 30°: sin 30° = 1/2, cos 30° = căn(3)/2, tan 30° = 1/căn(3).",
            "essence": "Tỉ số lượng giác chỉ phụ thuộc vào độ lớn của góc mà không phụ thuộc vào kích thước của tam giác vuông."
          }
        ],
        "rules": [
          {
            "statement": "Hệ thức cơ bản giữa sin và cos",
            "meaning": "Với mọi góc nhọn α, luôn có: sin^2(α) + cos^2(α) = 1 và tan(α) = sin(α) / cos(α).",
            "example": "Nếu biết sin α = 0,6 thì cos^2 α = 1 - 0,6^2 = 0,64 => cos α = 0,8 và tan α = 0,6/0,8 = 0,75.",
            "essence": "Hệ quả trực tiếp từ định lí Pythagore trên tam giác vuông chuẩn hóa có cạnh huyền bằng 1."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một cột cờ cao h đổ bóng trên mặt đất dài 12 m. Góc tạo bởi tia nắng mặt trời và mặt đất là 35°. Tính chiều cao của cột cờ (làm tròn đến chữ số thập phân thứ nhất).",
            "steps": [
              "Bước 1: Gọi AB là chiều cao cột cờ, BC là chiều dài bóng = 12 m, góc BCA = 35°.",
              "Bước 2: Trong tam giác vuông ABC tại B: tan(C) = AB / BC => AB = BC * tan(C).",
              "Bước 3: Thay số: AB = 12 * tan(35°) ≈ 12 * 0,7002 = 8,402 m."
            ],
            "answer": "Chiều cao cột cờ khoảng 8,4 mét."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa sin (đối/huyền) và cos (kề/huyền) khi lập tỉ số trong bài toán ứng dụng thực tế.",
            "why": "Cần vẽ phác tam giác vuông và xác định rõ góc quan sát cùng cạnh đối, cạnh kề tương ứng."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Đường tròn và Góc với đường tròn",
        "description": "Đường kính và dây cung, tiếp tuyến của đường tròn, góc ở tâm, góc nội tiếp, góc tạo bởi tia tiếp tuyến và dây cung, tứ giác nội tiếp đường tròn.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đường kính, dây cung và dấu hiệu nhận biết tiếp tuyến", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Góc nội tiếp và định lí tứ giác nội tiếp đường tròn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Góc nội tiếp đường tròn",
            "definition": "Là góc có đỉnh nằm trên đường tròn và hai cạnh chứa hai dây cung của đường tròn đó. Số đo góc nội tiếp bằng nửa số đo cung bị chắn.",
            "example": "Góc nội tiếp chắn nửa đường tròn luôn là góc vuông (90°).",
            "essence": "Trong một đường tròn, các góc nội tiếp cùng chắn một cung hoặc chắn hai cung bằng nhau thì bằng nhau."
          },
          {
            "term": "Tứ giác nội tiếp",
            "definition": "Là tứ giác có bốn đỉnh cùng nằm trên một đường tròn. Dấu hiệu: Tứ giác có tổng hai góc đối diện bằng 180°, hoặc hai đỉnh kề cùng nhìn một cạnh dưới hai góc bằng nhau.",
            "example": "Tứ giác ABCD có góc A + góc C = 180° thì ABCD nội tiếp được trong một đường tròn.",
            "essence": "Tứ giác nội tiếp là chìa khóa vàng để chứng minh các góc bằng nhau, các điểm thẳng hàng và đường thẳng vuông góc trong hình học phẳng."
          }
        ],
        "rules": [
          {
            "statement": "Định lí hai tiếp tuyến cắt nhau",
            "meaning": "Nếu hai tiếp tuyến của một đường tròn cắt nhau tại một điểm thì điểm đó cách đều hai tiếp điểm; tia nối điểm đó với tâm là tia phân giác của góc tạo bởi hai tiếp tuyến.",
            "example": "Từ điểm M ngoài (O) kẻ tiếp tuyến MA, MB: MA = MB, tia MO là phân giác góc AMB và OM là trung trực đoạn AB.",
            "essence": "Tính chất đối xứng gương hoàn hảo của hình tròn quanh trục nối từ tâm tới điểm ngoài."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho tam giác ABC nhọn nội tiếp đường tròn (O), các đường cao AD, BE cắt nhau tại H. Chứng minh tứ giác CDHE nội tiếp.",
            "steps": [
              "Bước 1: Xét tứ giác CDHE có AD là đường cao => AD vuông góc BC => góc HDC = 90°.",
              "Bước 2: Có BE là đường cao => BE vuông góc AC => góc HEC = 90°.",
              "Bước 3: Xét tổng hai góc đối diện: góc HDC + góc HEC = 90° + 90° = 180°.",
              "Bước 4: Suy ra tứ giác CDHE nội tiếp đường tròn đường kính CH."
            ],
            "answer": "Tứ giác CDHE nội tiếp đường tròn (đường kính HC)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn dấu hiệu 'hai góc đối bằng nhau' thay vì 'tổng hai góc đối bằng 180°'.",
            "why": "Hai góc đối bằng nhau là dấu hiệu của hình bình hành, trong khi tứ giác nội tiếp yêu cầu tổng hai góc đối bù nhau (180°)."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Hình trụ, Hình nón, Hình cầu",
        "description": "Hình dạng, diện tích xung quanh, diện tích toàn phần và thể tích của hình trụ, hình nón, hình cầu; các bài toán ứng dụng hình không gian thực tế.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Hình trụ và Hình nón: Diện tích và thể tích", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hình cầu: Diện tích mặt cầu và thể tích hình cầu", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hình trụ (Cylinder)",
            "definition": "Được sinh ra khi quay hình chữ nhật một vòng quanh một cạnh cố định. Sxq = 2*pi*r*h; V = pi*r^2*h.",
            "example": "Lon nước ngọt hình trụ có bán kính đáy r = 3 cm, chiều cao h = 10 cm có V = pi * 3^2 * 10 = 90pi ≈ 282,7 cm^3.",
            "essence": "Thể tích hình trụ bằng diện tích đáy nhân với chiều cao, diện tích xung quanh bằng chu vi đáy nhân đường sinh."
          },
          {
            "term": "Hình nón (Cone) và Hình cầu (Sphere)",
            "definition": "Hình nón: V = (1/3)*pi*r^2*h, Sxq = pi*r*l (l^2 = r^2 + h^2). Hình cầu: S = 4*pi*R^2, V = (4/3)*pi*R^3.",
            "example": "Quả bóng đá có bán kính R = 11 cm có thể tích V = (4/3)*pi*11^3 ≈ 5575 cm^3.",
            "essence": "Thể tích hình nón bằng 1/3 thể tích hình trụ có cùng bán kính đáy và chiều cao."
          }
        ],
        "rules": [
          {
            "statement": "Mối liên hệ giữa đường sinh, bán kính và chiều cao hình nón",
            "meaning": "Trong hình nón, đường sinh l, bán kính đáy r và chiều cao h tạo thành tam giác vuông: l^2 = r^2 + h^2.",
            "example": "Một chiếc nón lá có r = 20 cm, h = 15 cm thì đường sinh l = căn(20^2 + 15^2) = 25 cm.",
            "essence": "Áp dụng trực tiếp định lý Pythagore trong thiết diện qua trục của hình nón."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một hộp sữa đặc hình trụ có đường kính đáy 7,4 cm và chiều cao 8 cm. Tính diện tích giấy làm nhãn dán quanh thân hộp sữa (diện tích xung quanh, lấy pi = 3,14, bỏ qua mép dán).",
            "steps": [
              "Bước 1: Bán kính đáy hộp sữa là r = 7,4 / 2 = 3,7 cm.",
              "Bước 2: Chiều cao hộp sữa là h = 8 cm.",
              "Bước 3: Diện tích xung quanh: Sxq = 2 * pi * r * h = 2 * 3,14 * 3,7 * 8 = 185,888 cm^2."
            ],
            "answer": "Diện tích nhãn dán khoảng 185,9 cm^2."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên chia đôi đường kính để lấy bán kính đáy r khi tính toán thể tích hoặc diện tích xung quanh.",
            "why": "Công thức sử dụng bán kính r; nếu đề bài cho đường kính d thì phải luôn tính r = d / 2 trước."
          }
        ]
      }
    ]
  },
  "khoa-hoc-tu-nhien": {
    "id": "khoa-hoc-tu-nhien",
    "name": "Khoa học tự nhiên",
    "icon": "🔬",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Kim loại và Dãy hoạt động hóa học",
        "description": "Tính chất vật lí và hóa học của kim loại, dãy hoạt động hóa học của kim loại, sự ăn mòn kim loại và các biện pháp bảo vệ.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tính chất của kim loại và dãy hoạt động hóa học", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sự ăn mòn kim loại và bảo vệ kim loại", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Dãy hoạt động hóa học của kim loại",
            "definition": "K, Na, Ca, Mg, Al, Zn, Fe, Pb, (H), Cu, Ag, Au. Xếp theo chiều giảm dần tính hoạt động hóa học.",
            "example": "Fe tác dụng được với dung dịch CuSO4 vì Fe đứng trước Cu trong dãy: Fe + CuSO4 -> FeSO4 + Cu.",
            "essence": "Kim loại đứng trước đẩy kim loại đứng sau ra khỏi dung dịch muối; kim loại đứng trước H đẩy được H2 ra khỏi axit."
          },
          {
            "term": "Sự ăn mòn kim loại",
            "definition": "Là sự phá hủy kim loại hoặc hợp kim do tác dụng hóa học hoặc điện hóa học của môi trường xung quanh.",
            "example": "Đinh sắt để ngoài không khí ẩm bị gỉ tạo thành gỉ sắt Fe2O3.nH2O.",
            "essence": "Bảo vệ kim loại bằng cách sơn phủ bề mặt, bôi dầu mỡ, mạ kim loại trơ hoặc dùng phương pháp bảo vệ điện hóa."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc phản ứng kim loại với dung dịch muối",
            "meaning": "Kim loại đứng trước (từ Mg trở đi) đẩy được kim loại đứng sau ra khỏi dung dịch muối của chúng.",
            "example": "Mg + 2AgNO3 -> Mg(NO3)2 + 2Ag (Mg đứng trước Ag nên đẩy Ag ra tạo kim loại bạc sáng).",
            "essence": "Các kim loại kiềm tan (K, Na, Ca) sẽ tác dụng với nước trước nên không dùng để đẩy kim loại trong dung dịch muối."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Ngâm một lá sắt có khối lượng 10 g vào 200 ml dung dịch CuSO4 1M. Sau một thời gian lấy lá sắt ra rửa nhẹ làm khô cân nặng 10,8 g. Tính khối lượng Cu sinh ra bám trên lá sắt.",
            "steps": [
              "Bước 1: Phương trình: Fe + CuSO4 -> FeSO4 + Cu. Cứ 1 mol Fe (56 g) tan ra sẽ có 1 mol Cu (64 g) bám vào, khối lượng tăng 64 - 56 = 8 g.",
              "Bước 2: Khối lượng thanh sắt tăng thực tế: delta m = 10,8 - 10 = 0,8 g.",
              "Bước 3: Số mol Cu bám vào: n = delta m / 8 = 0,8 / 8 = 0,1 mol.",
              "Bước 4: Khối lượng Cu bám vào lá sắt: m_Cu = 0,1 * 64 = 6,4 g."
            ],
            "answer": "Khối lượng Cu bám vào là 6,4 gam."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho kim loại Na vào dung dịch CuSO4 và cho rằng Na đẩy Cu ra tạo thành kim loại Cu.",
            "why": "Na phản ứng mãnh liệt với nước trong dung dịch trước tạo NaOH và H2, sau đó NaOH phản ứng với CuSO4 tạo kết tủa xanh Cu(OH)2."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Hợp chất hữu cơ và Hydrocarbon",
        "description": "Khái niệm hợp chất hữu cơ, methane (alkane), ethylene (alkene), acetylene (alkyne), nhiên liệu dầu mỏ và khí thiên nhiên.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Methane và Ethylene: Cấu tạo và tính chất hóa học", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Nhiên liệu và biến đổi khí hậu", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hydrocarbon",
            "definition": "Là những hợp chất hữu cơ mà phân tử chỉ gồm hai nguyên tố carbon (C) và hydrogen (H).",
            "example": "CH4 (methane), C2H4 (ethylene), C2H2 (acetylene) đều là các hydrocarbon tiêu biểu.",
            "essence": "Hydrocarbon là nguồn năng lượng hóa thạch chủ đạo và là nguyên liệu cơ bản cho ngành công nghiệp hóa dầu."
          },
          {
            "term": "Phản ứng cộng của Ethylene",
            "definition": "Do có liên kết đôi C=C kém bền, ethylene dễ dàng tham gia phản ứng cộng làm mất màu dung dịch nước brom.",
            "example": "CH2=CH2 + Br2 -> CH2Br-CH2Br (1,2-dibromoethane).",
            "essence": "Phản ứng làm mất màu nước brom là thuốc thử đặc trưng để phân biệt hydrocarbon không no (ethylene) với hydrocarbon no (methane)."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm phản ứng cháy của Hydrocarbon",
            "meaning": "Khi đốt cháy hoàn toàn trong oxi, mọi hydrocarbon đều sinh ra khí CO2 và hơi nước, đồng thời tỏa nhiều nhiệt: CxHy + (x + y/4) O2 -> x CO2 + (y/2) H2O.",
            "example": "CH4 + 2O2 -> CO2 + 2H2O + nhiệt lượng lớn (khí đun nấu gia đình).",
            "essence": "Hiệu ứng nhà kính gia tăng chủ yếu do lượng phát thải khí CO2 từ việc đốt nhiên liệu hóa thạch."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Dẫn 4,48 lít hỗn hợp khí gồm CH4 và C2H4 (đktc) qua bình đựng dung dịch brom dư, thấy có 16 g brom tham gia phản ứng. Tính phần trăm thể tích của mỗi khí trong hỗn hợp ban đầu.",
            "steps": [
              "Bước 1: Tổng số mol hỗn hợp: n = 4,48 / 22,4 = 0,2 mol.",
              "Bước 2: Chỉ có C2H4 phản ứng với Br2: C2H4 + Br2 -> C2H4Br2. Số mol Br2 = 16 / 160 = 0,1 mol.",
              "Bước 3: Do đó số mol C2H4 = n_Br2 = 0,1 mol. Suy ra n_CH4 = 0,2 - 0,1 = 0,1 mol.",
              "Bước 4: Vì số mol bằng nhau nên %V(C2H4) = %V(CH4) = (0,1 / 0,2) * 100% = 50%."
            ],
            "answer": "%V(C2H4) = 50% và %V(CH4) = 50%."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng khí CH4 có thể làm mất màu dung dịch brom ở điều kiện thường.",
            "why": "CH4 chỉ chứa liên kết đơn C-H rất bền vững nên chỉ tham gia phản ứng thế với clo khi có ánh sáng, không làm mất màu nước brom."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Rượu Ethylic, Acid Acetic và Chất béo",
        "description": "Rượu ethylic (C2H5OH), acid acetic (CH3COOH), độ rượu, phản ứng ester hóa, chất béo và polymer trong đời sống.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Rượu ethylic và độ rượu", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Acid acetic và phản ứng ester hóa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Độ rượu",
            "definition": "Là số mililít rượu ethylic nguyên chất có trong 100 mililít hỗn hợp rượu với nước.",
            "example": "Rượu 40° nghĩa là trong 100 ml dung dịch rượu có chứa 40 ml rượu ethylic nguyên chất và 60 ml nước.",
            "essence": "Độ rượu phản ánh nồng độ cồn thể tích theo tiêu chuẩn đo lường quốc tế (% vol)."
          },
          {
            "term": "Phản ứng ester hóa",
            "definition": "Là phản ứng thuận nghịch giữa acid carboxylic và alcohol có mặt acid H2SO4 đặc làm xúc tác và đun nóng: CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O.",
            "example": "Sản phẩm ethyl acetate (CH3COOC2H5) là ester có mùi thơm hoa quả đặc trưng, ít tan trong nước và nổi lên trên.",
            "essence": "Phản ứng ester hóa có tính thuận nghịch; H2SO4 đặc đóng vai trò vừa là chất xúc tác vừa hút nước để chuyển dịch cân bằng."
          }
        ],
        "rules": [
          {
            "statement": "Tính acid của acid acetic",
            "meaning": "Acid acetic làm quỳ tím hóa đỏ, tác dụng với kim loại trước H, oxit bazo, bazo và muối carbonate giải phóng khí CO2.",
            "example": "2CH3COOH + CaCO3 -> (CH3COO)2Ca + CO2 + H2O (giấm ăn dùng để tẩy sạch cặn vôi ấm đun nước).",
            "essence": "Tuy là acid hữu cơ yếu nhưng acid acetic vẫn mang đầy đủ tính chất chung của một acid vô cơ."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cho 60 g acid acetic tác dụng với 46 g rượu ethylic đun nóng có H2SO4 đặc xúc tác. Biết hiệu suất phản ứng đạt 60%. Tính khối lượng ethyl acetate thu được.",
            "steps": [
              "Bước 1: Số mol CH3COOH = 60 / 60 = 1 mol. Số mol C2H5OH = 46 / 46 = 1 mol.",
              "Bước 2: Phương trình: CH3COOH + C2H5OH <=> CH3COOC2H5 + H2O. Tỉ lệ phản ứng 1:1, về lý thuyết thu được 1 mol ester.",
              "Bước 3: Do hiệu suất H = 60% nên số mol ester thực tế = 1 * 60% = 0,6 mol.",
              "Bước 4: Khối lượng ester (M = 88 g/mol): m = 0,6 * 88 = 52,8 g."
            ],
            "answer": "Khối lượng ethyl acetate thu được là 52,8 gam."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên nhân với hiệu suất phản ứng (H = 60%) khi tính khối lượng sản phẩm ester.",
            "why": "Phản ứng ester hóa là phản ứng hai chiều thuận nghịch nên không bao giờ đạt hiệu suất 100% trong điều kiện thông thường."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Hiện tượng khúc xạ ánh sáng và Thấu kính",
        "description": "Hiện tượng khúc xạ ánh sáng, phản xạ toàn phần, thấu kính hội tụ, thấu kính phân kì, ảnh của vật qua thấu kính, tật cận thị và viễn thị.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Hiện tượng khúc xạ ánh sáng và thấu kính hội tụ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thấu kính phân kì và các tật của mắt", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Khúc xạ ánh sáng",
            "definition": "Hiện tượng tia sáng bị gãy khúc khi truyền xiên góc từ môi trường trong suốt này sang môi trường trong suốt khác.",
            "example": "Nhúng một chiếc đũa vào cốc nước, ta nhìn thấy chiếc đũa như bị gãy tại mặt phân cách giữa nước và không khí.",
            "essence": "Hiện tượng gãy khúc xảy ra do tốc độ truyền ánh sáng thay đổi khác nhau giữa hai môi trường chiết quang."
          },
          {
            "term": "Thấu kính hội tụ",
            "definition": "Thấu kính có phần rìa mỏng hơn phần giữa. Chùm sáng song song tới thấu kính hội tụ cho chùm tia ló hội tụ tại tiêu điểm của thấu kính.",
            "example": "Vật đặt ngoài khoảng tiêu cự (d > f) cho ảnh thật ngược chiều với vật; vật trong tiêu cự (d < f) cho ảnh ảo lớn hơn vật (kính lúp).",
            "essence": "Mắt cận thị phải đeo thấu kính phân kì để nhìn rõ vật ở xa; mắt lão thị/viễn thị đeo kính hội tụ để nhìn gần."
          }
        ],
        "rules": [
          {
            "statement": "Đường truyền của ba tia sáng đặc biệt qua thấu kính hội tụ",
            "meaning": "1) Tia tới qua quang tâm O truyền thẳng. 2) Tia tới song song trục chính cho tia ló đi qua tiêu điểm F'. 3) Tia tới qua tiêu điểm F cho tia ló song song trục chính.",
            "example": "Dùng hai trong ba tia sáng đặc biệt này để xác định vị trí ảnh của một điểm sáng.",
            "essence": "Quy tắc dựng hình quang học chuẩn xác dựa trên tính chất đối xứng quang học."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Đặt vật sáng AB cao 2 cm vuông góc với trục chính của thấu kính hội tụ có tiêu cự f = 10 cm. Vật cách thấu kính d = 15 cm. Tính khoảng cách từ ảnh đến thấu kính d' và chiều cao của ảnh A'B'.",
            "steps": [
              "Bước 1: Áp dụng công thức thấu kính hội tụ cho ảnh thật: 1/f = 1/d + 1/d'.",
              "Bước 2: Thay số: 1/10 = 1/15 + 1/d' => 1/d' = 1/10 - 1/15 = 1/30 => d' = 30 cm.",
              "Bước 3: Chiều cao ảnh: A'B' / AB = d' / d => A'B' = 2 * (30 / 15) = 4 cm."
            ],
            "answer": "Ảnh thật cách thấu kính 30 cm và cao 4 cm (ảnh thật ngược chiều, phóng đại gấp 2 lần vật)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa ảnh thật (hứng được trên màn) và ảnh ảo (nhìn thấy bằng mắt nhưng không hứng được trên màn).",
            "why": "Thấu kính phân kì luôn luôn cho ảnh ảo nhỏ hơn vật; thấu kính hội tụ cho ảnh ảo lớn hơn vật khi vật đặt trong khoảng tiêu cự."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Cảm ứng điện từ và Dòng điện xoay chiều",
        "description": "Hiện tượng cảm ứng điện từ, điều kiện xuất hiện dòng điện cảm ứng, dòng điện xoay chiều (AC), máy biến thế và truyền tải điện năng đi xa.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Hiện tượng cảm ứng điện từ và dòng điện xoay chiều", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Máy biến áp và hao phí khi truyền tải điện năng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Dòng điện cảm ứng",
            "definition": "Dòng điện xuất hiện trong cuộn dây dẫn kín khi số đường sức từ xuyên qua tiết diện S của cuộn dây biến thiên (tăng hoặc giảm).",
            "example": "Đưa thanh nam châm lại gần hoặc rút ra xa cuộn dây kín làm kim điện kế lệch khỏi vạch số 0.",
            "essence": "Bản chất là sự chuyển hóa từ cơ năng thành điện năng trong máy phát điện xoay chiều."
          },
          {
            "term": "Máy biến thế (Máy biến áp)",
            "definition": "Thiết bị dùng để biến đổi hiệu điện thế xoay chiều mà không làm thay đổi tần số: U1 / U2 = N1 / N2.",
            "example": "Nếu số vòng dây cuộn thứ cấp N2 gấp 10 lần cuộn sơ cấp N1 thì hiệu điện thế U2 tăng 10 lần (máy tăng thế).",
            "essence": "Muốn giảm hao phí do tỏa nhiệt trên đường dây truyền tải thì giải pháp hiệu quả nhất là tăng hiệu điện thế U ở đầu nguồn."
          }
        ],
        "rules": [
          {
            "statement": "Công thức công suất hao phí do tỏa nhiệt trên đường dây",
            "meaning": "P_hp = R * P^2 / U^2. Công suất hao phí tỉ lệ nghịch với bình phương hiệu điện thế giữa hai đầu dây tải.",
            "example": "Khi tăng hiệu điện thế U lên 10 lần thì hao phí nhiệt P_hp giảm đi 10^2 = 100 lần.",
            "essence": "Đó là lí do người ta phải dùng đường dây siêu cao áp 500 kV để truyền tải điện năng Bắc - Nam."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cần truyền tải một công suất điện P = 100 kW trên đường dây tải điện có điện trở R = 10 ôm. Tính công suất hao phí trên đường dây khi truyền tải ở hiệu điện thế U1 = 10 000 V và khi tăng lên U2 = 20 000 V.",
            "steps": [
              "Bước 1: Đổi đơn vị: P = 100 kW = 100 000 W.",
              "Bước 2: Hao phí ở U1 = 10 000 V: P_hp1 = 10 * (100 000)^2 / (10 000)^2 = 10 * 10^10 / 10^8 = 1 000 W = 1 kW.",
              "Bước 3: Hao phí ở U2 = 20 000 V: P_hp2 = 10 * (100 000)^2 / (20 000)^2 = 10 * 10^10 / (4 * 10^8) = 250 W = 0,25 kW.",
              "Bước 4: So sánh: Khi U tăng 2 lần thì P_hp giảm 4 lần (từ 1 kW xuống 0,25 kW)."
            ],
            "answer": "Hao phí lần lượt là 1000 W và 250 W."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng máy biến thế có thể làm việc được với dòng điện một chiều không đổi (DC từ pin/ắc quy).",
            "why": "Dòng điện không đổi tạo ra từ trường không đổi nên không có sự biến thiên từ thông, do đó không sinh ra dòng điện cảm ứng ở cuộn thứ cấp."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Di truyền học Mendel, ADN và Đột biến",
        "description": "Các quy luật di truyền của Mendel, cấu trúc và chức năng của ADN và ARN, nhiễm sắc thể, đột biến gene, đột biến cấu trúc và số lượng NST.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Di truyền học Mendel và cấu trúc của ADN", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Đột biến gene và đột biến nhiễm sắc thể", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quy luật phân li của Mendel",
            "definition": "Trong quá trình phát sinh giao tử, mỗi nhân tố di truyền (allele) trong cặp phân li về một giao tử và giữ nguyên bản chất như ở cơ thể thuần chủng P.",
            "example": "Lai đậu Hà Lan hạt vàng (AA) với hạt xanh (aa) thu được F1 toàn hạt vàng (Aa); cho F1 tự thụ phấn được F2 tỉ lệ 3 hạt vàng : 1 hạt xanh.",
            "essence": "Tính trạng trội lấn át tính trạng lặn ở trạng thái dị hợp tử (Aa)."
          },
          {
            "term": "Nguyên tắc bổ sung trong phân tử ADN",
            "definition": "Các nucleotide trên hai mạch đơn liên kết với nhau bằng liên kết hydrogen theo nguyên tắc: A liên kết với T bằng 2 liên kết, G liên kết với C bằng 3 liên kết.",
            "example": "Nếu một mạch có trình tự - A - T - G - C - thì mạch bổ sung tương ứng là - T - A - C - G -.",
            "essence": "Nguyên tắc bổ sung đảm bảo sự nhân đôi ADN chính xác tuyệt đối từ tế bào mẹ sang tế bào con."
          }
        ],
        "rules": [
          {
            "statement": "Hệ quả của nguyên tắc bổ sung trong phân tử ADN",
            "meaning": "Trong phân tử ADN mạch kép: A = T và G = C. Suy ra tổng số nucleotide N = 2A + 2G = 2T + 2C và chiều dài L = (N / 2) * 3,4 Å.",
            "example": "Một đoạn ADN có 3000 nucleotide thì chiều dài của đoạn ADN đó là L = (3000 / 2) * 3,4 = 5100 Å.",
            "essence": "Mỗi chu kì xoắn của ADN gồm 10 cặp nucleotide, dài 34 Å và có đường kính 20 Å."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một phân tử ADN mạch kép có 2400 nucleotide, trong đó số nucleotide loại Adenine (A) chiếm 20% tổng số nucleotide. Tính số nucleotide mỗi loại và số liên kết hydrogen của phân tử ADN này.",
            "steps": [
              "Bước 1: Tính số nucleotide loại A: A = T = 2400 * 20% = 480 nucleotide.",
              "Bước 2: Tính số nucleotide loại G: Tổng %A + %G = 50% => %G = 30%. Do đó G = C = 2400 * 30% = 720 nucleotide.",
              "Bước 3: Tính số liên kết hydrogen: H = 2A + 3G = 2 * 480 + 3 * 720 = 960 + 2160 = 3120 liên kết."
            ],
            "answer": "A = T = 480; G = C = 720; Số liên kết hydrogen H = 3120."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa đột biến gene (biến đổi trong cấu trúc của gene tại 1 hoặc vài cặp nu) với đột biến nhiễm sắc thể (biến đổi số lượng/cấu trúc NST).",
            "why": "Đột biến gene ở cấp độ phân tử, còn đột biến nhiễm sắc thể ở cấp độ tế bào có thể quan sát được dưới kính hiển vi."
          }
        ]
      }
    ]
  },
  "ngu-van": {
    "id": "ngu-van",
    "name": "Ngữ văn",
    "icon": "📖",
    "chapters": [
      {
        "id": "ch01",
        "title": "Bài 1: Vẻ đẹp của thơ hiện đại và tình cảm gia đình, quê hương",
        "description": "Bếp lửa (Bằng Việt), Mùa xuân nho nhỏ (Thanh Hải), Ánh trăng (Nguyễn Duy), vẻ đẹp tình bà cháu và trách nhiệm công dân với đất nước.",
        "lessons": [
          { "id": "l01", "title": "Văn bản: Bếp lửa (Bằng Việt) và Mùa xuân nho nhỏ (Thanh Hải)", "hasRealContent": true },
          { "id": "l02", "title": "Tiếng Việt & Viết: Phân tích hình tượng thơ và cảm xúc trữ tình", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hình tượng 'Bếp lửa' trong thơ Bằng Việt",
            "definition": "Bếp lửa vừa là hình ảnh thực gắn liền với bàn tay tảo tần của người bà trong những năm tháng kháng chiến gian khổ, vừa là biểu tượng thiêng liêng cho tình yêu thương, sự che chở và cội nguồn nuôi dưỡng tâm hồn người cháu.",
            "example": "'Lận đận đời bà biết mấy nắng mưa / Mấy chục năm rồi, đến tận bây giờ / Bà vẫn giữ thói quen dậy sớm / Nhóm bếp lửa ấp iu nồng đượm...'",
            "essence": "Bếp lửa gắn với bà, nhóm lên niềm tin bất diệt, tình bà cháu nâng tầm thành tình yêu quê hương, đất nước."
          },
          {
            "term": "Ước nguyện dâng hiến trong 'Mùa xuân nho nhỏ'",
            "definition": "Khát vọng chân thành, khiêm nhường được hòa nhập vào bản trường ca chung của đất nước: làm một cành hoa, một con chim hót, một nốt trầm xao xuyến để dâng hiến cho mùa xuân lớn của cuộc đời.",
            "example": "'Một mùa xuân nho nhỏ / Lặng lẽ dâng cho đời / Dù là tuổi hai mươi / Dù là khi tóc bạc...'",
            "essence": "Lẽ sống cao đẹp của nhà thơ Thanh Hải viết trên giường bệnh trước lúc qua đời: cống hiến âm thầm, bền bỉ và không vụ lợi."
          }
        ],
        "rules": [
          {
            "statement": "Kỹ năng phân tích một đoạn thơ trữ tình",
            "meaning": "Khai thác từ ngữ, hình ảnh, nhịp điệu, các biện pháp tu từ (ẩn dụ, điệp từ, hoán dụ) để bộc lộ chiều sâu cảm xúc và tư tưởng mà tác giả gửi gắm.",
            "example": "Phân tích từ 'ấp iu' trong Bếp lửa: gợi bàn tay khéo léo, kiên nhẫn nhóm lửa và tấm lòng ấp ủ tình thương của người bà.",
            "essence": "Không diễn xuôi bài thơ mà phải bám vào thi pháp và giọng điệu nghệ thuật."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cảm nhận về triết lí sống nhân nghĩa trong bài thơ 'Ánh trăng' của Nguyễn Duy qua khổ thơ cuối: 'Ngửa mặt lên nhìn mặt / có cái gì rưng rưng / như là đồng là bể / như là sông là rừng... Trăng cứ tròn vành vạnh / kể chi người vô tình / ánh trăng im phăng phắc / đủ cho ta giật mình'.",
            "steps": [
              "Bước 1: Giới thiệu tác giả Nguyễn Duy, hoàn cảnh sáng tác năm 1978 tại TP.HCM và chủ đề gợi nhắc đạo lí ân nghĩa thủy chung.",
              "Bước 2: Phân tích tư thế 'ngửa mặt lên nhìn mặt' - sự đối diện thẳng thắn giữa con người và vầng trăng quá khứ; cảm xúc 'rưng rưng' nghẹn ngào vì nhớ lại năm tháng rừng suối gian nan.",
              "Bước 3: Phân tích sự đối lập: 'Trăng tròn vành vạnh' tượng trưng cho quá khứ vẹn nguyên thủy chung; con người 'vô tình' đã từng quên lãng trong ánh điện cửa gương.",
              "Bước 4: Hình tượng 'ánh trăng im phăng phắc' như một lời nhắc nhở không lời nhưng đầy nghiêm khắc; cái 'giật mình' thức tỉnh lương tâm để trở về với lối sống uống nước nhớ nguồn."
            ],
            "answer": "Khổ thơ cuối bài 'Ánh trăng' là lời tự vấn lương tâm sâu sắc, nhắc nhở con người không được bội bạc với quá khứ gian lao và nghĩa tình."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chỉ kể lại nội dung câu chuyện trong bài thơ 'Ánh trăng' mà không phân tích giá trị biểu tượng của vầng trăng và sự thức tỉnh lương tâm.",
            "why": "Thơ trữ tình cần được tiếp cận từ ngôn từ, hình ảnh biểu tượng và chiều sâu cảm xúc triết lí."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Bài 2: Truyện ngắn hiện đại và hình tượng con người Việt Nam",
        "description": "Làng (Kim Lân), Lặng lẽ Sa Pa (Nguyễn Thành Long), Chiếc lược ngà (Nguyễn Quang Sáng), tình yêu nước và vẻ đẹp tâm hồn con người lao động, chiến đấu.",
        "lessons": [
          { "id": "l01", "title": "Văn bản: Làng (Kim Lân) và Lặng lẽ Sa Pa (Nguyễn Thành Long)", "hasRealContent": true },
          { "id": "l02", "title": "Văn bản: Chiếc lược ngà (Nguyễn Quang Sáng)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tâm lí ông Hai khi nghe tin làng Chợ Dầu theo giặc (truyện 'Làng')",
            "definition": "Đỉnh cao diễn biến nội tâm: từ bàng hoàng, đau đớn, tủi hổ đến sự dằn vặt gay gắt giữa tình yêu làng quê với tình yêu kháng chiến, để rồi quyết định dứt khoát: 'Làng thì yêu thật, nhưng làng theo Tây thì phải thù'.",
            "example": "Kim Lân miêu tả ông Hai 'cổ nghẹn đắng lại, da mặt tê rân rân', về nhà nằm vật ra giường, không dám bước ra đường vì sợ tiếng làng theo giặc.",
            "essence": "Kim Lân phản ánh bước chuyển biến lớn trong nhận thức của người nông dân Việt Nam sau Cách mạng tháng Tám: tình yêu làng hòa quyện và thống nhất với lòng yêu nước."
          },
          {
            "term": "Vẻ đẹp của anh thanh niên trong 'Lặng lẽ Sa Pa'",
            "definition": "Chàng thanh niên 26 tuổi làm công tác khí tượng kiêm vật lí địa cầu trên đỉnh Yên Sơn cao 2600m: say mê công việc, có tinh thần trách nhiệm cao, suy nghĩ sâu sắc về ý nghĩa cuộc sống, khiêm tốn và cởi mở, hiếu khách.",
            "example": "'Khi ta làm việc, ta với công việc là đôi, sao gọi là một mình được? Huống chi việc của cháu gắn liền với việc của bao anh em đồng chí dưới mặt đất...'",
            "essence": "Hình mẫu tiêu biểu cho thế hệ trẻ cống hiến thầm lặng cho công cuộc xây dựng đất nước trong những năm tháng kháng chiến chống Mỹ."
          }
        ],
        "rules": [
          {
            "statement": "Nghệ thuật xây dựng tình huống truyện",
            "meaning": "Tình huống truyện là lát cắt của đời sống, nơi tính cách nhân vật bộc lộ sâu sắc và tư tưởng của nhà văn được phát sáng rực rỡ nhất.",
            "example": "Tình huống nghe tin làng Chợ Dầu theo giặc đẩy xung đột nội tâm ông Hai lên đến đỉnh điểm thử thách lòng trung thành với Cụ Hồ.",
            "essence": "Phân tích truyện ngắn phải luôn bắt đầu từ việc nắm bắt tình huống truyện độc đáo."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích tình cha con sâu sắc giữa ông Sáu và bé Thu trong truyện ngắn 'Chiếc lược ngà' của Nguyễn Quang Sáng.",
            "steps": [
              "Bước 1: Nêu hoàn cảnh éo le: chiến tranh chia cắt suốt 8 năm, khi ông Sáu về phép thì vết sẹo trên mặt khiến bé Thu sợ hãi không chịu nhận cha.",
              "Bước 2: Phân tích sự bướng bỉnh nhưng ngây thơ của bé Thu: phản ứng cự tuyệt chứng tỏ tình yêu thương tuyệt đối dành cho người cha trong bức ảnh chụp chung với má.",
              "Bước 3: Phút giây nhận cha trước lúc chia tay: sự thức tỉnh sau khi được bà ngoại giải thích về vết sẹo chiến tranh, tiếng gọi 'Ba... a... a... ba!' xé lòng và cái ôm siết chặt không muốn buông.",
              "Bước 4: Tình thương của người cha nơi chiến khu: dồn hết nỗi nhớ thương vào việc tỉ mẩn mài từng chiếc răng lược ngà cho con, đến hơi thở cuối cùng trước khi hi sinh vẫn gửi lại chiếc lược cho người đồng đội chuyển về cho con gái."
            ],
            "answer": "'Chiếc lược ngà' là khúc ca bi tráng về tình phụ tử thiêng liêng bất diệt trước sự tàn khốc của chiến tranh."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đánh giá thái độ ban đầu của bé Thu là vô lễ, hư đốn mà không hiểu nguyên nhân tâm lí sâu xa của đứa trẻ 8 tuổi.",
            "why": "Phản ứng của bé Thu xuất phát từ lòng tôn thờ người cha duy nhất trong tấm ảnh; khi hiểu ra sự thật thì tình yêu ấy bùng cháy mãnh liệt hơn bao giờ hết."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Bài 3: Văn học trung đại Việt Nam và Kiệt tác Truyện Kiều",
        "description": "Chuyện người con gái Nam Xương (Nguyễn Dữ), Truyện Kiều (Nguyễn Du): Chị em Thúy Kiều, Kiều ở lầu Ngưng Bích, nghệ thuật ước lệ và miêu tả nội tâm.",
        "lessons": [
          { "id": "l01", "title": "Văn bản: Chuyện người con gái Nam Xương (Nguyễn Dữ)", "hasRealContent": true },
          { "id": "l02", "title": "Văn bản: Kiệt tác Truyện Kiều và đoạn trích Kiều ở lầu Ngưng Bích (Nguyễn Du)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Nỗi oan khuất của Vũ Nương",
            "definition": "Vũ Nương là người phụ nữ đảm đang, hiếu nghĩa, tiết hạnh vẹn toàn nhưng phải chịu bi kịch oan khuất đến mức phải gieo mình xuống sông Hoàng Giang vì thói ghen tuông gia trưởng mù quáng của Trương Sinh và sự éo le của chiến tranh phong kiến.",
            "example": "Chiếc bóng trên vách tường vốn là biểu hiện của tình yêu thương và sự bù đắp người cha cho đứa con thơ, nhưng lại vô tình trở thành nguyên cớ của tấn bi kịch tan vỡ gia đình.",
            "essence": "Tố cáo chế độ phong kiến bất công trọng nam khinh nữ và ngợi ca phẩm giá ngời sáng của người phụ nữ Việt Nam."
          },
          {
            "term": "Bút pháp tả cảnh ngụ tình trong 'Kiều ở lầu Ngưng Bích'",
            "definition": "Nghệ thuật mượn cảnh vật thiên nhiên bên ngoài để thể hiện tâm trạng cô đơn, xót xa, hoang mang và dự cảm về số phận giông bão của Thúy Kiều.",
            "example": "'Buồn trông cửa bể chiều hôm / Thuyền ai thấp thoáng cánh buồm xa xa? / Buồn trông ngọn nước mới sa / Hoa trôi man mác biết là về đâu? / Buồn trông nội cỏ rầu rầu / Chân mây mặt đất một màu xanh xanh / Buồn trông gió cuốn mặt duềnh / Ầm ầm tiếng sóng kêu quanh ghế ngồi.'",
            "essence": "Điệp ngữ 'Buồn trông' đứng đầu 4 cặp câu lục bát tạo nên điệp khúc triền miên của nỗi sầu thương vô tận, từ xa đến gần, từ tĩnh đến động dữ dội."
          }
        ],
        "rules": [
          {
            "statement": "Nghệ thuật ước lệ tượng trưng trong văn học trung đại",
            "meaning": "Sử dụng những hình ảnh quy ước từ thiên nhiên tươi đẹp (trăng, hoa, tuyết, ngọc, liễu, thu thủy, xuân sơn) để miêu tả vẻ đẹp thanh cao của con người.",
            "example": "'Làn thu thủy nét xuân sơn / Hoa ghen thua thắm liễu hờn kém xanh' (vẻ đẹp sắc sảo, đằm thắm của Thúy Kiều khiến tạo hóa phải hờn ghen).",
            "essence": "Vẻ đẹp của Thúy Kiều vượt qua chuẩn mực tự nhiên, dự báo một số mệnh truân chuyên 'tài mệnh tương đố'."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích diễn biến tâm trạng Thúy Kiều qua nỗi nhớ người yêu Kim Trọng và cha mẹ trong đoạn trích 'Kiều ở lầu Ngưng Bích'.",
            "steps": [
              "Bước 1: Nêu hoàn cảnh Kiều bị giam lỏng ở lầu Ngưng Bích giữa bốn bề non xa trăng gần cô quạnh.",
              "Bước 2: Phân tích nỗi nhớ Kim Trọng trước: nhớ lời thề nguyền dưới trăng, xót xa tưởng tượng chàng Kim đang uổng công mong đợi; tự thấy mình phụ bạc lời thề ước ('Tưởng người dưới nguyệt chén đồng...').",
              "Bước 3: Phân tích nỗi nhớ cha mẹ sau: thương cha mẹ sớm hôm tựa cửa ngóng trông; xót xa cảnh cha mẹ già yếu mà không thể tự tay quạt nồng ấp lạnh phụng dưỡng ('Xót người tựa cửa hôm mai...').",
              "Bước 4: Nhận xét: Việc nhớ Kim Trọng trước rồi nhớ cha mẹ sau là hoàn toàn phù hợp với tâm lí và đạo lí, bởi Kiều đã hi sinh chữ hiếu để bán mình chuộc cha, nên món nợ tình với Kim Trọng vẫn luôn là nỗi day dứt không yên."
            ],
            "answer": "Thúy Kiều hiện lên là một người con hiếu thảo tột cùng và một người tình thủy chung son sắt vị tha."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng Kiều bất hiếu vì nhớ người yêu trước khi nhớ đến cha mẹ.",
            "why": "Kiều đã bán mình chuộc cha và em, tức là đã hoàn thành bổn phận chữ hiếu cao nhất; món nợ thề nguyền dang dở với Kim Trọng khiến Kiều cảm thấy có lỗi và dằn vặt nhất."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Bài 4: Văn bản nghị luận và các vấn đề tư tưởng, đời sống",
        "description": "Bàn về đọc sách (Chu Quang Tiềm), Tiếng nói của văn nghệ (Nguyễn Đình Thi), Chuẩn bị hành trang vào thế kỉ mới, nghệ thuật lập luận chặt chẽ.",
        "lessons": [
          { "id": "l01", "title": "Văn bản: Bàn về đọc sách (Chu Quang Tiềm) và Tiếng nói của văn nghệ (Nguyễn Đình Thi)", "hasRealContent": true },
          { "id": "l02", "title": "Kỹ năng: Lập luận trong văn nghị luận xã hội", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Ý nghĩa của việc đọc sách theo Chu Quang Tiềm",
            "definition": "Đọc sách là con đường quan trọng của học vấn, là sự chuẩn bị để tiếp thu di sản tinh thần của nhân loại qua các thời đại, giúp con người tích lũy tri thức và nâng cao tầm vóc tâm hồn.",
            "example": "Sách là cột mốc trên con đường tiến hóa học thuật của nhân loại; không đọc sách thì học vấn bị thụt lùi và giam mình trong thế giới hạn hẹp.",
            "essence": "Đọc sách không cốt lấy nhiều mà phải chọn cho tinh, đọc cho kĩ, kết hợp giữa đọc sâu và đọc rộng."
          },
          {
            "term": "Sức mạnh kì diệu của văn nghệ theo Nguyễn Đình Thi",
            "definition": "Văn nghệ không chỉ phản ánh thực tại khách quan mà còn gửi gắm tư tưởng, tình cảm của người nghệ sĩ vào cuộc sống; văn nghệ thanh lọc tâm hồn, kết nối con người với thế giới xung quanh.",
            "example": "Một bài thơ, một bản đàn hay đánh thức những xúc cảm ngủ quên, giúp con người tìm thấy niềm an ủi, nghị lực sống và khát khao vươn tới cái đẹp.",
            "essence": "Văn nghệ tác động trực tiếp vào trái tim và cảm xúc, từ đó lay chuyển nhận thức và hành động của con người."
          }
        ],
        "rules": [
          {
            "statement": "Cấu trúc một bài văn nghị luận xã hội chuẩn",
            "meaning": "Gồm 4 phần: 1) Giải thích khái niệm/vấn đề. 2) Bàn luận, phân tích các khía cạnh đúng/sai và dẫn chứng thực tế. 3) Phản đề, mở rộng góc nhìn. 4) Bài học nhận thức và hành động của bản thân.",
            "example": "Bàn về lòng biết ơn: Giải thích là gì -> Tại sao cần biết ơn -> Dẫn chứng tấm gương tri ân -> Phê phán kẻ vô ơn bạc bẽo -> Hành động cụ thể hàng ngày.",
            "essence": "Lập luận sắc bén, dẫn chứng xác thực, cảm xúc chân thành và lời văn truyền cảm."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Viết đoạn văn nghị luận (khoảng 200 chữ) bàn về ý kiến của Chu Quang Tiềm: 'Đọc sách không cốt lấy nhiều, quan trọng nhất là phải chọn cho tinh, đọc cho kĩ'.",
            "steps": [
              "Bước 1: Mở đoạn nêu trích dẫn ý kiến của Chu Quang Tiềm về phương pháp đọc sách khoa học.",
              "Bước 2: Giải thích: 'Không cốt lấy nhiều' nghĩa là tránh lối đọc tham lam số lượng, đọc lướt cưỡi ngựa xem hoa; 'chọn cho tinh' là lựa chọn những cuốn sách thực sự có giá trị, phù hợp chuyên môn; 'đọc cho kĩ' là đọc sâu, suy ngẫm, nghiền ngẫm để thấu hiểu bản chất.",
              "Bước 3: Bàn luận: Sách ngày nay xuất bản tràn lan, nếu không chọn tinh sẽ mất thời gian vô bổ; đọc kĩ một cuốn sách kinh điển quý giá gấp ngàn lần liếc qua trăm cuốn sách hời hợt.",
              "Bước 4: Liên hệ bản thân: Cần lập kế hoạch đọc sách chủ động, ghi chép tóm tắt và vận dụng bài học từ sách vào đời sống thực tế."
            ],
            "answer": "Đoạn văn hoàn chỉnh khẳng định phương pháp đọc sách chất lượng hơn số lượng là chìa khóa mở cánh cửa tri thức đích thực."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy dẫn chứng chung chung mơ hồ không có tên tuổi cụ thể trong bài văn nghị luận xã hội.",
            "why": "Dẫn chứng cần tiêu biểu, xác thực và thuyết phục (ví dụ: Chủ tịch Hồ Chí Minh, thầy giáo Nguyễn Ngọc Ký, Bill Gates...)."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Bài 5: Tiếng Việt và Kỹ năng làm bài thi tuyển sinh vào lớp 10",
        "description": "Các phép liên kết câu và liên kết đoạn văn, thành phần biệt lập (tình thái, cảm thán, gọi - đáp, phụ chú), khởi ngữ, phương châm hội thoại và kỹ năng viết nghị luận văn học.",
        "lessons": [
          { "id": "l01", "title": "Tiếng Việt: Các thành phần biệt lập và phép liên kết câu", "hasRealContent": true },
          { "id": "l02", "title": "Kỹ năng: Chiến lược làm bài thi Ngữ văn vào lớp 10 đạt điểm 8+", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thành phần biệt lập",
            "definition": "Là các thành phần không tham gia vào việc diễn đạt nghĩa sự việc của câu. Bao gồm: thành phần tình thái, cảm thán, gọi - đáp, và phụ chú.",
            "example": "'Chắc chắn, ngày mai chúng ta sẽ chiến thắng' ('chắc chắn' là thành phần tình thái thể hiện độ tin cậy cao).",
            "essence": "Thành phần biệt lập giúp câu văn biểu cảm phong phú, làm rõ thái độ người nói mà không làm thay đổi cấu trúc chủ vị cốt lõi."
          },
          {
            "term": "Các phép liên kết câu và đoạn văn",
            "definition": "Bao gồm: phép lặp từ ngữ, phép đồng nghĩa - trái nghĩa và liên tưởng, phép thay thế (dùng đại từ), phép nối (dùng quan hệ từ hoặc từ ngữ chuyển tiếp).",
            "example": "'Trường học của chúng ta là trường học của chế độ dân chủ nhân dân. Trường học ấy nhằm đào tạo những công dân có ích...' (phép lặp 'trường học', phép thế 'trường học ấy').",
            "essence": "Đảm bảo sự mạch lạc về chủ đề và liên kết chặt chẽ về hình thức giữa các câu trong văn bản."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc nhận diện thành phần phụ chú",
            "meaning": "Thành phần phụ chú dùng để bổ sung một số chi tiết cho nội dung chính của câu; thường được đặt giữa hai dấu gạch ngang, hai dấu phẩy, hai dấu ngoặc đơn hoặc sau dấu hai chấm.",
            "example": "Bác Ba - người bạn thân thiết của ba tôi - đã trao lại chiếc lược ngà cho tôi ('người bạn thân thiết của ba tôi' là thành phần phụ chú).",
            "essence": "Lược bỏ thành phần phụ chú thì nghĩa sự việc cơ bản của câu vẫn hoàn chỉnh."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xác định thành phần biệt lập trong câu sau và cho biết đó là thành phần gì: 'Than ôi! Thời oanh liệt nay còn đâu?' và 'Chao ôi, bắt gặp một con người như anh ta là một cơ hội hãn hữu cho sáng tác...'.",
            "steps": [
              "Bước 1: Trong câu thứ nhất: 'Than ôi!' đứng đầu câu bộc lộ nỗi tiếc nuối xót xa của con hổ trong vườn bách thú => Thành phần cảm thán.",
              "Bước 2: Trong câu thứ hai: 'Chao ôi' bộc lộ sự xúc động ngỡ ngàng của người họa sĩ già khi gặp anh thanh niên => Thành phần cảm thán."
            ],
            "answer": "Cả hai từ 'Than ôi!' và 'Chao ôi' đều là thành phần cảm thán dùng để bộc lộ cảm xúc trực tiếp."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa thành phần tình thái (thể hiện cách nhìn của người nói: có lẽ, dường như, chắc chắn) với trạng ngữ chỉ cách thức.",
            "why": "Trạng ngữ trả lời cho câu hỏi 'làm như thế nào?', còn thành phần tình thái chỉ mức độ tin cậy hoặc thái độ chủ quan của người nói."
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
        "title": "Chương 1: Lịch sử thế giới hiện đại từ năm 1918 đến nay",
        "description": "Chiến tranh thế giới thứ hai (1939 - 1945), trật tự hai cực Ianta, Liên Hợp Quốc, phong trào giải phóng dân tộc Á - Phi - Mỹ Latinh, xu thế toàn cầu hóa.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Chiến tranh thế giới thứ hai và Trật tự thế giới hai cực Ianta", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phong trào giải phóng dân tộc và xu thế toàn cầu hóa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Trật tự thế giới hai cực Ianta",
            "definition": "Trật tự thế giới mới được thiết lập sau Hội nghị Ianta (2/1945) với sự phân chia phạm vi ảnh hưởng giữa hai siêu cường Liên Xô và Mỹ, chi phối nền chính trị quốc tế suốt thời kì Chiến tranh Lạnh.",
            "example": "Châu Âu bị chia đôi: Đông Âu thuộc phạm vi ảnh hưởng của Liên Xô, Tây Âu thuộc phạm vi của Mỹ.",
            "essence": "Mối quan hệ vừa đối đầu căng thẳng vừa kiềm chế giữa hai phe tư bản chủ nghĩa và xã hội chủ nghĩa."
          },
          {
            "term": "Xu thế Toàn cầu hóa",
            "definition": "Là quá trình gia tăng mạnh mẽ những mối liên hệ, sự tác động qua lại, phụ thuộc lẫn nhau giữa các quốc gia, dân tộc trên phạm vi toàn cầu về kinh tế, văn hóa, công nghệ.",
            "example": "Sự hình thành các tổ chức thương mại thế giới WTO, liên minh khu vực ASEAN, EU và chuỗi cung ứng sản xuất toàn cầu.",
            "essence": "Vừa là cơ hội to lớn để hội nhập kinh tế, vừa là thách thức gay gắt về giữ gìn bản sắc và chủ quyền quốc gia."
          }
        ],
        "rules": [
          {
            "statement": "Mục đích thành lập Liên Hợp Quốc (UN)",
            "meaning": "Duy trì hòa bình và an ninh thế giới, phát triển các mối quan hệ hữu nghị giữa các dân tộc trên cơ sở tôn trọng độc lập chủ quyền, bình đẳng và thúc đẩy hợp tác quốc tế.",
            "example": "Hiến chương Liên Hợp Quốc có hiệu lực ngày 24/10/1945; Việt Nam chính thức gia nhập Liên Hợp Quốc năm 1977.",
            "essence": "Tổ chức quốc tế lớn nhất hành tinh đóng vai trò diễn đàn đa phương giải quyết các xung đột toàn cầu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích nguyên nhân thắng lợi của cuộc chiến tranh chống chủ nghĩa phát xít trong Chiến tranh thế giới thứ hai (1939 - 1945).",
            "steps": [
              "Bước 1: Nêu tính chất chính nghĩa của cuộc chiến đấu chống phát xít do Liên Xô, các nước Đồng minh và nhân dân các nước bị chiếm đóng tiến hành.",
              "Bước 2: Vai trò trụ cột của Liên Xô: đánh bại các đạo quân tinh nhuệ nhất của phát xít Đức ở Stalingrad, giải phóng Đông Âu và tiến đánh tận sào huyệt Berlin, tiêu diệt đạo quân Quan Đông của Nhật.",
              "Bước 3: Sự phối hợp chiến đấu quả cảm của quân đội các nước Đồng minh Anh, Mỹ và các lực lượng kháng chiến trên toàn cầu.",
              "Bước 4: Sự sụp đổ của chủ nghĩa phát xít là quy luật tất yếu của tội ác chống lại loài người."
            ],
            "answer": "Thắng lợi thuộc về nhân loại tiến bộ nhờ tính chất chính nghĩa và vai trò quyết định của Liên Xô cùng khối Đồng minh."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đánh giá thấp vai trò quyết định của Liên Xô trong việc tiêu diệt chủ nghĩa phát xít ở mặt trận châu Âu.",
            "why": "Chiến trường Xô - Đức là mặt trận chính, nơi tiêu hao và tiêu diệt hơn 75% lực lượng quân đội phát xít Đức."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Lịch sử Việt Nam từ 1918 đến 1945 và CMT8",
        "description": "Phong trào dân tộc dân chủ (1919 - 1930), Nguyễn Ái Quốc tìm đường cứu nước, Đảng Cộng sản Việt Nam ra đời (1930), Cách mạng tháng Tám 1945 và sự khai sinh nước VNDCCH.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phong trào cách mạng và sự ra đời của Đảng Cộng sản Việt Nam", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Cách mạng tháng Tám năm 1945 và Bản Tuyên ngôn Độc lập", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Ý nghĩa sự ra đời của Đảng Cộng sản Việt Nam (3/2/1930)",
            "definition": "Là kết quả của sự kết hợp giữa chủ nghĩa Mác - Lênin với phong trào công nhân và phong trào yêu nước Việt Nam; chấm dứt thời kì khủng hoảng sâu sắc về đường lối và giai cấp lãnh đạo cách mạng kéo dài suốt nửa thế kỉ.",
            "example": "Đảng ra đời mở ra kỉ nguyên độc lập dân tộc gắn liền với chủ nghĩa xã hội dưới sự dẫn dắt của Chủ tịch Hồ Chí Minh.",
            "essence": "Bước ngoặt vĩ đại nhất trong lịch sử cách mạng Việt Nam thế kỉ XX."
          },
          {
            "term": "Cách mạng tháng Tám năm 1945",
            "definition": "Cuộc tổng khởi nghĩa giành chính quyền thần tốc trong vòng 15 ngày (từ 14/8 đến 28/8/1945), đập tan ách thống trị của phát xít Nhật và thực dân Pháp, lật đổ ngai vàng phong kiến ngàn năm.",
            "example": "Ngày 2/9/1945 tại Quảng trường Ba Đình, Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập khai sinh nước Việt Nam Dân chủ Cộng hòa.",
            "essence": "Mở ra kỉ nguyên mới cho dân tộc: kỉ nguyên độc lập, tự do và nhân dân lao động làm chủ đất nước."
          }
        ],
        "rules": [
          {
            "statement": "Thời cơ ngàn năm có một của Cách mạng tháng Tám",
            "meaning": "Xuất hiện khi phát xít Nhật đầu hàng Đồng minh (15/8/1945), chính phủ bù nhìn Trần Trọng Kim tê liệt hoang mang, trong khi quân Đồng minh chưa kịp vào giải giáp quân Nhật.",
            "example": "Lời kêu gọi khẩn thiết của Bác Hồ: 'Dù phải đốt cháy cả dãy Trường Sơn cũng phải kiên quyết giành cho được độc lập!'.",
            "essence": "Nghệ thuật chớp thời cơ và kết hợp nhuần nhuyễn lực lượng chính trị với lực lượng vũ trang."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao nói Cách mạng tháng Tám năm 1945 là một cuộc cách mạng dân tộc dân chủ nhân dân điển hình?",
            "steps": [
              "Bước 1: Tính chất dân tộc: Giải quyết mâu thuẫn chủ yếu giữa toàn thể dân tộc Việt Nam với thực dân, phát xít xâm lược; giành lại độc lập chủ quyền hoàn toàn.",
              "Bước 2: Tính chất dân chủ: Lật đổ chế độ quân chủ chuyên chế ngàn năm, đem lại các quyền tự do dân chủ cơ bản cho các tầng lớp nhân dân lao động.",
              "Bước 3: Tính nhân dân sâu sắc: Động viên được sức mạnh của khối đại đoàn kết toàn dân tộc dưới ngọn cờ của Mặt trận Việt Minh."
            ],
            "answer": "CMT8 mang tính dân tộc giải phóng sâu sắc, tính dân chủ tiến bộ và tính nhân dân rộng rãi."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng Cách mạng tháng Tám thành công là do 'khoảng trống quyền lực' ngẫu nhiên chứ không phải nhờ sự chuẩn bị chu đáo.",
            "why": "Đảng và Bác Hồ đã chuẩn bị chu đáo suốt 15 năm qua 3 cao trào cách mạng 1930-1931, 1936-1939 và 1939-1945 mới có thể chớp thời cơ thần tốc."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Địa lí Dân cư và các ngành Kinh tế Việt Nam",
        "description": "Đặc điểm dân số, lao động và việc làm, đô thị hóa, sự chuyển dịch cơ cấu kinh tế theo ngành, nông nghiệp, công nghiệp và dịch vụ.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Dân số, nguồn lao động và sự chuyển dịch cơ cấu kinh tế", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các ngành kinh tế trọng điểm: Nông nghiệp, Công nghiệp và Dịch vụ", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chuyển dịch cơ cấu kinh tế theo ngành",
            "definition": "Xu hướng giảm tỉ trọng khu vực I (Nông - lâm - thủy sản), tăng tỉ trọng khu vực II (Công nghiệp - xây dựng) và nâng cao chất lượng khu vực III (Dịch vụ).",
            "example": "Nước ta đang đẩy mạnh công nghiệp hóa, hiện đại hóa và chuyển đổi số nền kinh tế.",
            "essence": "Phản ánh trình độ phát triển của lực lượng sản xuất và sự hội nhập kinh tế quốc tế sâu rộng."
          },
          {
            "term": "Nguồn lao động Việt Nam",
            "definition": "Nước ta có nguồn lao động dồi dào, cần cù, sáng tạo, có kinh nghiệm sản xuất phong phú và khả năng tiếp thu nhanh khoa học công nghệ, đang trong thời kì 'dân số vàng'.",
            "example": "Lực lượng lao động trên 50 triệu người; hạn chế là tỉ lệ lao động qua đào tạo có bằng cấp chứng chỉ còn cần nâng cao.",
            "essence": "Lao động chất lượng cao là động lực then chốt để phát triển kinh tế tri thức."
          }
        ],
        "rules": [
          {
            "statement": "Quy luật phân bố ngành công nghiệp chế biến lương thực thực phẩm",
            "meaning": "Ngành này phân bố gần nguồn nguyên liệu phong phú (Đồng bằng sông Cửu Long, Đồng bằng sông Hồng) và gần thị trường tiêu thụ lớn (các đô thị, cảng biển).",
            "example": "Các nhà máy chế biến gạo, thủy hải sản đông lạnh tập trung dày đặc ở Cần Thơ, An Giang, Cà Mau.",
            "essence": "Giảm thiểu chi phí vận chuyển nguyên liệu tươi sống cồng kềnh và đáp ứng kịp thời nhu cầu xuất khẩu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Dựa vào bảng số liệu cơ cấu GDP phân theo ngành của nước ta: Nông nghiệp: 12%, Công nghiệp - xây dựng: 38%, Dịch vụ: 41%, Thuế sản phẩm: 9%. Nhận xét xu hướng chuyển dịch cơ cấu ngành kinh tế.",
            "steps": [
              "Bước 1: Nêu tỉ trọng: Khu vực Dịch vụ chiếm tỉ trọng cao nhất (41%), tiếp đến là Công nghiệp - xây dựng (38%), Nông - lâm - thủy sản chiếm tỉ trọng thấp nhất (12%).",
              "Bước 2: Đánh giá: Cơ cấu kinh tế có sự chuyển biến tích cực theo hướng công nghiệp hóa, hiện đại hóa.",
              "Bước 3: Kết luận: Phù hợp với xu thế phát triển kinh tế chung của các nước đang phát triển trên thế giới."
            ],
            "answer": "Cơ cấu kinh tế nước ta đang chuyển dịch mạnh mẽ theo hướng hiện đại, giảm dần tỉ trọng nông nghiệp và tăng mạnh công nghiệp, dịch vụ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa cơ cấu kinh tế theo ngành (I, II, III) với cơ cấu kinh tế theo thành phần kinh tế (nhà nước, ngoài nhà nước, có vốn FDI).",
            "why": "Hai tiêu chí phân chia phản ánh hai khía cạnh quản lí và tính chất khác nhau của nền kinh tế."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Sự phân hóa lãnh thổ và các vùng kinh tế Bắc Bộ - Miền Trung",
        "description": "Vùng Trung du và miền núi Bắc Bộ, Đồng bằng sông Hồng, Bắc Trung Bộ và Duyên hải Nam Trung Bộ, Tây Nguyên: Tiềm năng và thế mạnh kinh tế.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vùng Trung du miền núi Bắc Bộ và Đồng bằng sông Hồng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Vùng Duyên hải miền Trung và Tây Nguyên", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thế mạnh của Trung du và miền núi Bắc Bộ",
            "definition": "Giàu tài nguyên khoáng sản (than đá Quảng Ninh, apatit Lào Cai), tiềm năng thủy điện lớn nhất nước (sông Đà: Thủy điện Hòa Bình, Sơn La), cây công nghiệp cận nhiệt và ôn đới (chè, hồi, quế).",
            "example": "Nhà máy thủy điện Sơn La có công suất lớn nhất Đông Nam Á (2400 MW).",
            "essence": "Địa hình hiểm trở và chia cắt là khó khăn lớn nhất đối với giao thông vận tải và sinh hoạt mùa mưa bão."
          },
          {
            "term": "Thế mạnh cây công nghiệp lâu năm ở Tây Nguyên",
            "definition": "Đất đỏ bazan màu mỡ, tầng phong hóa dày, phân bố tập trung trên các cao nguyên lượn sóng rộng lớn rất thuận lợi cho việc hình thành các vùng chuyên canh cà phê, cao su, hồ tiêu quy mô lớn.",
            "example": "Tây Nguyên là vùng trồng cà phê lớn nhất cả nước (nổi tiếng với cà phê Buôn Ma Thuột).",
            "essence": "Mùa khô kéo dài vừa tạo điều kiện phơi sấy nông sản nhưng cũng gây thiếu nước tưới nghiêm trọng."
          }
        ],
        "rules": [
          {
            "statement": "Ý nghĩa việc phát triển lâm nghiệp ở Tây Nguyên và Bắc Trung Bộ",
            "meaning": "Rừng đầu nguồn có vai trò xung yếu trong việc giữ nguồn nước ngầm, chống xói mòn rửa trôi đất, điều tiết lũ lụt cho các vùng đồng bằng duyên hải hạ lưu.",
            "example": "Bảo vệ rừng Vườn quốc gia Yok Đôn, Chư Mom Ray, Phong Nha - Kẻ Bàng.",
            "essence": "Phát triển kinh tế phải luôn gắn liền với bảo tồn sinh thái và an ninh nguồn nước bền vững."
          }
        ],
        "workedExamples": [
          {
            "prompt": "So sánh thế mạnh tự nhiên để phát triển nông nghiệp giữa Đồng bằng sông Hồng và Đồng bằng sông Cửu Long.",
            "steps": [
              "Bước 1: Giống nhau: Cả hai đều là những đồng bằng châu thổ phù sa màu mỡ rộng lớn nhất nước, nguồn nước tưới dồi dào, khí hậu nhiệt đới gió mùa.",
              "Bước 2: Khác nhau: ĐBSH có mùa đông lạnh cho phép trồng rau quả vụ đông cận nhiệt; đất có đê ngăn lũ chia cắt thành nhiều ô trũng. ĐBSCL có diện tích lớn gấp 3 lần, khí hậu cận xích đạo nóng quanh năm, có mạng lưới sông ngòi kênh rạch chằng chịt, không có đê bao ngăn lũ triệt để nên đất được bồi đắp phù sa hàng năm nhưng bị nhiễm phèn, nhiễm mặn vào mùa khô."
            ],
            "answer": "ĐBSH thế mạnh thâm canh cây vụ đông; ĐBSCL thế mạnh sản xuất lúa hàng hóa và thủy hải sản quy mô lớn nhất nước."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng Đồng bằng sông Hồng có diện tích tự nhiên lớn hơn Đồng bằng sông Cửu Long.",
            "why": "ĐBSCL rộng khoảng 40.000 km2, lớn hơn gấp gần 3 lần so với ĐBSH (khoảng 15.000 km2)."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Vùng Đông Nam Bộ và Kinh tế Biển đảo Việt Nam",
        "description": "Đông Nam Bộ - Vùng kinh tế năng động nhất cả nước, kinh tế biển đảo, các đảo và quần đảo Hoàng Sa, Trường Sa, an ninh chủ quyền quốc gia.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vùng Đông Nam Bộ: Đầu tàu kinh tế và đô thị hóa", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phát triển tổng hợp kinh tế biển và bảo vệ chủ quyền biển đảo", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Vị thế đầu tàu kinh tế của Đông Nam Bộ",
            "definition": "Đông Nam Bộ dẫn đầu cả nước về GDP, giá trị sản xuất công nghiệp, kim ngạch xuất khẩu và thu hút đầu tư trực tiếp nước ngoài (FDI); hạt nhân là Thành phố Hồ Chí Minh.",
            "example": "Các ngành mũi nhọn: khai thác dầu khí thềm lục địa, điện tử viễn thông, hóa chất, dịch vụ cảng biển logistics nước sâu Cái Mép - Thị Vải.",
            "essence": "Năng động, sáng tạo, cơ sở hạ tầng giao thông kết nối đồng bộ và nguồn lao động trình độ cao."
          },
          {
            "term": "Bốn ngành kinh tế biển tổng hợp",
            "definition": "1) Khai thác, nuôi trồng và chế biến hải sản. 2) Khai thác và chế biến khoáng sản biển (dầu khí, muối). 3) Du lịch biển - đảo. 4) Giao thông vận tải biển.",
            "example": "Vùng biển Việt Nam có hơn 3000 hòn đảo lớn nhỏ, hai quần đảo Hoàng Sa và Trường Sa giữ vị trí chiến lược trọng yếu.",
            "essence": "Phát triển kinh tế biển phải gắn liền với củng cố quốc phòng an ninh và bảo vệ môi trường sinh thái biển."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc khai thác hải sản xa bờ bền vững",
            "meaning": "Chuyển dịch từ đánh bắt ven bờ sang đánh bắt xa bờ vừa giúp bảo vệ nguồn lợi thủy sản ven bờ khỏi cạn kiệt, vừa khẳng định chủ quyền biển đảo hợp pháp của Tổ quốc.",
            "example": "Trang bị tàu vỏ thép công suất lớn, hệ thống định vị vệ tinh GPS cho ngư dân vươn khơi bám biển.",
            "essence": "Mỗi con tàu đánh cá của ngư dân là một cột mốc chủ quyền sống trên biển Đông."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao việc phát triển tổng hợp kinh tế biển có ý nghĩa chiến lược đối với sự nghiệp xây dựng và bảo vệ Tổ quốc Việt Nam?",
            "steps": [
              "Bước 1: Về kinh tế: Biển nước ta giàu tài nguyên dầu khí, hải sản, thuận lợi phát triển du lịch và thương mại hàng hải quốc tế, đóng góp lớn vào GDP.",
              "Bước 2: Về xã hội: Giải quyết việc làm cho hàng triệu lao động ven biển, nâng cao đời sống nhân dân.",
              "Bước 3: Về an ninh quốc phòng: Khẳng định chủ quyền biển đảo thiêng liêng, kiểm soát tuyến hàng hải quốc tế huyết mạch và bảo vệ biên cương Tổ quốc từ hướng biển."
            ],
            "answer": "Kinh tế biển tạo động lực tăng trưởng kinh tế đồng thời là bức tường thành vững chắc bảo vệ chủ quyền quốc gia."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng kinh tế biển chỉ đơn thuần là việc đánh bắt cá tôm trên biển.",
            "why": "Kinh tế biển gồm 4 ngành tổng hợp đan xen gắn kết: thủy sản, khoáng sản dầu khí, du lịch biển và giao thông vận tải biển."
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
        "title": "Unit 1: Local Community & Traditional Crafts",
        "description": "Vocabulary for craft villages and community helpers, complex sentences with adverb clauses of purpose/result/reason, phrasal verbs.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Vocabulary & Phrasal Verbs in Village Life", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Grammar: Complex Sentences & Review", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Phrasal Verbs (Cụm động từ)",
            "definition": "A verb combined with an adverb or a preposition that creates a meaning different from the original verb.",
            "example": "pass down (truyền lại), look around (ngắm nghía xung quanh), set up (khởi nghiệp/thành lập), live on (sống dựa vào).",
            "essence": "Mastering phrasal verbs makes English speaking and writing sound natural and authentic."
          },
          {
            "term": "Complex Sentences with Adverb Clauses",
            "definition": "Sentences containing an independent clause and at least one dependent clause introduced by subordinator: because/since (reason), so that (purpose), although (concession).",
            "example": "Although the pottery was handmade, it was sold at an affordable price.",
            "essence": "Used to link ideas logically in essays and descriptive paragraphs."
          }
        ],
        "rules": [
          {
            "statement": "Adverb clauses of purpose with 'so that' / 'in order that'",
            "meaning": "Subject + Verb + so that + Subject + can/could/will/would + Verb (bare infinitive).",
            "example": "We woke up early so that we could catch the first bus to Bat Trang ceramic village.",
            "essence": "Expresses the specific goal or aim of the action in the main clause."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rewrite the sentence using the phrasal verb in brackets: 'My grandparents started this workshop twenty years ago.' (SET UP)",
            "steps": [
              "Bước 1: Nhận diện động từ 'started' ở thì quá khứ đơn (Past Simple).",
              "Bước 2: Cụm động từ tương đương là 'set up' (quá khứ của set vẫn là set).",
              "Bước 3: Viết lại câu: 'My grandparents set up this workshop twenty years ago.'"
            ],
            "answer": "My grandparents set up this workshop twenty years ago."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'although' and 'but' together in the same sentence: 'Although he was tired, but he finished the craft.'",
            "why": "In English, never use 'although' and 'but' in the same sentence. Remove 'but': 'Although he was tired, he finished the craft.'"
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Unit 2: City Life & Modern Challenges",
        "description": "City adjectives, double comparatives (the more... the more...), comparison of adjectives and adverbs, urban problems.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: City Vocabulary & Comparisons", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Grammar: Double Comparatives (The more..., the more...)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Double Comparative (So sánh kép lũy tiến)",
            "definition": "The + comparative (+ S + V), the + comparative (+ S + V). Used to show that two things change together.",
            "example": "The bigger the city is, the higher the cost of living becomes.",
            "essence": "Expresses proportional cause-and-effect relationship between two changing factors."
          },
          {
            "term": "Urban Amenities & Drawbacks",
            "definition": "Amenities: metro line, entertainment center, healthcare. Drawbacks: traffic congestion, high cost of living, air pollution.",
            "example": "Hanoi is expanding its elevated metro network to ease traffic jams during rush hours.",
            "essence": "Key vocabulary for writing Grade 10 entrance exam essays on modern urban challenges."
          }
        ],
        "rules": [
          {
            "statement": "Structure of Double Comparative",
            "meaning": "The + more / -er + S + V, the + more / -er + S + V.",
            "example": "The more you practice listening, the better your English becomes.",
            "essence": "Both clauses must start with 'The' followed by a comparative adjective or adverb."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Combine two sentences using a double comparative: 'You travel widely. You learn a lot of things.'",
            "steps": [
              "Bước 1: Chuyển 'travel widely' thành so sánh hơn: 'The more widely you travel'.",
              "Bước 2: Chuyển 'learn a lot of things' thành: 'the more you learn'.",
              "Bước 3: Kết hợp hai mệnh đề với dấu phẩy: 'The more widely you travel, the more you learn.'"
            ],
            "answer": "The more widely you travel, the more you learn."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Forgetting 'The' in the second clause: 'The older he gets, more wise he is.'",
            "why": "Both clauses must begin with 'The': 'The older he gets, the wiser he becomes.'"
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Unit 3: Healthy Living & Teen Stress",
        "description": "Mental and physical health, stress management, question words before to-infinitive (what to do, where to go), modal verbs.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Coping with Stress & Pressure", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Question words before To-Infinitive", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Question Word + To-Infinitive",
            "definition": "A concise reported clause where question words (who, what, where, when, how) are followed by 'to + verb'.",
            "example": "I don't know what to do to overcome exam anxiety.",
            "essence": "Replaces longer clauses like 'what I should do' or 'where I ought to go'."
          },
          {
            "term": "Work-Life Balance for Teenagers",
            "definition": "Balancing academic demands with physical workouts, sufficient sleep (8 hours), and emotional well-being.",
            "example": "Teens should take regular breaks and talk to school counselors when feeling overwhelmed.",
            "essence": "Healthy minds reside in healthy bodies."
          }
        ],
        "rules": [
          {
            "statement": "Reported speech transformation with question word + to-V",
            "meaning": "S + asked/wondered + Wh-word + to-infinitive when the subject of both clauses is the same.",
            "example": "'Where should I register for the course?' -> She wondered where to register for the course.",
            "essence": "Cannot be used with the question word 'why'."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rewrite the sentence: 'He told me how I could solve this difficult math problem.' using question word + to-V.",
            "steps": [
              "Bước 1: Xác định mệnh đề danh ngữ: 'how I could solve this difficult math problem'.",
              "Bước 2: Thay 'I could solve' bằng 'to solve'.",
              "Bước 3: Viết lại: 'He told me how to solve this difficult math problem.'"
            ],
            "answer": "He told me how to solve this difficult math problem."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'why' with to-infinitive: 'I wonder why to do that.'",
            "why": "'Why' cannot be followed by to-infinitive in English. You must say: 'I wonder why I should do that.'"
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Unit 4: Remembering the Past & Heritage",
        "description": "Past life in Vietnam, preservation of cultural traditions, 'used to' + bare V, wishes for the present (wish + Past Simple).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Traditional Customs & Used To", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Wishes for the Present (Wish + Past Simple)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "'Used to' + Infinitive",
            "definition": "Used to describe past habits, routines or states that were true in the past but no longer exist today.",
            "example": "Children used to play folk games like tug-of-war instead of playing smartphone video games.",
            "essence": "Contrasts past reality with present modern lifestyle."
          },
          {
            "term": "Present Wish (Wish + Past Simple)",
            "definition": "Subject + wish(es) + Subject + Past Simple (were for all persons of to-be). Expresses regret about a current situation.",
            "example": "I wish I had more free time to visit historical monuments.",
            "essence": "The action is unreal in the present, so the verb is backshifted one tense into the past."
          }
        ],
        "rules": [
          {
            "statement": "Subjunctive 'were' in wish clauses",
            "meaning": "In formal English, use 'were' instead of 'was' for all subjects (I, he, she, it) after 'wish'.",
            "example": "She wishes she were a member of the heritage preservation club.",
            "essence": "Standard grammatical rule tested in high school entrance exams."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Write a sentence with 'wish': 'I don't know how to play the traditional musical instrument (Dan Bau).'",
            "steps": [
              "Bước 1: Xác định sự thật ở hiện tại: 'I don't know' (phủ định thì Hiện tại đơn).",
              "Bước 2: Chuyển sang câu ước: lùi một thì thành Khẳng định thì Quá khứ đơn: 'knew'.",
              "Bước 3: Viết câu: 'I wish I knew how to play the traditional musical instrument (Dan Bau).'"
            ],
            "answer": "I wish I knew how to play the traditional musical instrument (Dan Bau)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Confusing 'used to + V' (thói quen quá khứ) with 'be used to + V-ing' (quen với việc gì ở hiện tại).",
            "why": "'used to go' = đã từng đi trong quá khứ; 'is used to getting up early' = đã quen với việc dậy sớm."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Unit 5: Wonders of Viet Nam & Natural Beauty",
        "description": "Vocabulary for landscapes and UNESCO world wonders, Impersonal passive (It is said that...), suggestions with suggest + V-ing / clause.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Natural & Man-made Wonders", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Impersonal Passive & Suggestions", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Impersonal Passive (Bị động khách quan)",
            "definition": "Used with reporting verbs (say, believe, think, report, claim): It is + past participle + that + clause.",
            "example": "It is believed that Ha Long Bay was formed over millions of years by geological movements.",
            "essence": "Expresses general public opinions without specifying who holds the belief."
          },
          {
            "term": "Suggestions with 'Suggest'",
            "definition": "Suggest + V-ing OR Suggest that + Subject + (should) + bare infinitive.",
            "example": "The tour guide suggested that we visit Trang An eco-tourism complex early in the morning.",
            "essence": "The subjunctive bare infinitive is used regardless of the subject (he, she, they)."
          }
        ],
        "rules": [
          {
            "statement": "Two forms of Impersonal Passive transformation",
            "meaning": "People say that S + V -> 1) It is said that S + V. 2) S + is/are said + to-V (hoặc to have P2 nếu xảy ra trước).",
            "example": "People believe that Son Doong Cave is the largest cave in the world -> Son Doong Cave is believed to be the largest cave in the world.",
            "essence": "Frequently tested transformation pattern in Grade 10 English exams."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rewrite using impersonal passive: 'People report that thousands of foreign tourists visit Hoi An Ancient Town every week.'",
            "steps": [
              "Bước 1: Sử dụng cấu trúc: It is reported that...",
              "Bước 2: Giữ nguyên mệnh đề sau that: 'thousands of foreign tourists visit Hoi An Ancient Town every week.'",
              "Bước 3: Viết câu hoàn chỉnh: 'It is reported that thousands of foreign tourists visit Hoi An Ancient Town every week.'"
            ],
            "answer": "It is reported that thousands of foreign tourists visit Hoi An Ancient Town every week."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'suggest someone to do something': 'She suggested me to go there.'",
            "why": "'Suggest' never takes an object + to-infinitive. Correct: 'She suggested that I should go there' or 'She suggested going there.'"
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Unit 6: Viet Nam: Then and Now",
        "description": "Historical milestones, Past Perfect Tense (had + P2), comparison of past infrastructure and modern smart cities.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Life in the Subsidised Period vs Digital Age", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Past Perfect Tense & Timeline Analysis", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Past Perfect Tense (Quá khứ hoàn thành)",
            "definition": "Had + Past Participle (V3/-ed). Used to describe an action that happened before another past action or before a specific past point in time.",
            "example": "By the time the high-speed railway was opened in 2021, citizens had waited for several years.",
            "essence": "Establishes clear chronological order between two past events: action 1 (Past Perfect), action 2 (Past Simple)."
          },
          {
            "term": "Subsidised Period (Thời kì bao cấp)",
            "definition": "The historical era in Vietnam (1976-1986) before Doi Moi, characterized by food stamps, bicycles, and rationing coupons.",
            "example": "Before the Doi Moi reforms in 1986, people had bought goods using ration stamps.",
            "essence": "Cultural background knowledge frequently integrated into reading comprehension texts."
          }
        ],
        "rules": [
          {
            "statement": "Time conjunctions with Past Perfect: Before, After, By the time",
            "meaning": "Before / By the time + Past Simple, Past Perfect. After + Past Perfect, Past Simple.",
            "example": "After they had completed the survey, they submitted the report to the municipal authorities.",
            "essence": "Action happening first takes 'had + P2'; action happening later takes Past Simple."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Combine the two sentences using 'before': 'The fire brigade arrived. The historic wooden house burned down.'",
            "steps": [
              "Bước 1: Xác định hành động xảy ra trước: ngôi nhà bị cháy rụi (hành động 1). Cứu hỏa đến sau (hành động 2).",
              "Bước 2: Hành động 1 chia ở Past Perfect: 'had burned down'.",
              "Bước 3: Hành động 2 chia ở Past Simple: 'arrived'.",
              "Bước 4: Nối câu: 'The historic wooden house had burned down before the fire brigade arrived.'"
            ],
            "answer": "The historic wooden house had burned down before the fire brigade arrived."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Confusing which action happened first, leading to inverted tenses in the sentence.",
            "why": "Always sketch a mental timeline: the event that occurred earlier in the past must take 'had + P2'."
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
        "title": "Chủ đề 1: Máy tính và Cộng đồng: Tác động của Công nghệ số",
        "description": "Khai thác thông tin trên Internet, độ tin cậy của thông tin số, tác động của mạng xã hội, phòng tránh nghiện Internet và bảo vệ sức khỏe.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khai thác thông tin trên Internet và kiểm tra độ tin cậy", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sử dụng mạng xã hội văn minh và bảo vệ dữ liệu cá nhân", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tiêu chí đánh giá độ tin cậy của thông tin số",
            "definition": "1) Tác giả/Tổ chức xuất bản uy tín (.gov, .edu, các báo chí chính thống). 2) Tính cập nhật thời gian. 3) Mục đích thông tin khách quan. 4) Có nguồn dẫn chứng rõ ràng.",
            "example": "Thông tin dịch bệnh cần tra cứu trên cổng thông tin Bộ Y tế thay vì các bài đăng trôi nổi trên mạng xã hội.",
            "essence": "Tư duy phản biện số giúp bảo vệ bản thân trước tin giả (fake news) và lừa đảo trực tuyến."
          },
          {
            "term": "Dấu chân kỹ thuật số (Digital Footprint)",
            "definition": "Mọi dấu vết dữ liệu mà một người để lại khi sử dụng Internet: lịch sử duyệt web, các bài đăng, bình luận, vị trí GPS và ảnh tải lên.",
            "example": "Một bức ảnh hay bình luận tiêu cực đăng lên mạng xã hội có thể tồn tại vĩnh viễn và ảnh hưởng đến cơ hội xin học bổng hay việc làm sau này.",
            "essence": "Mỗi cá nhân phải có ý thức chịu trách nhiệm về phát ngôn và hành vi của mình trên không gian mạng."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc bảo mật tài khoản trực tuyến hai lớp (2FA)",
            "meaning": "Bật xác thực hai yếu tố cho email và tài khoản mạng xã hội để ngăn chặn kẻ xấu chiếm đoạt quyền điều khiển dù biết mật khẩu.",
            "example": "Đăng nhập cần nhập mật khẩu kèm mã OTP gửi về điện thoại hoặc ứng dụng Authenticator.",
            "essence": "Nguyên tắc phòng thủ theo chiều sâu bảo vệ tài sản số cá nhân."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nhận được một tin nhắn thông báo trúng thưởng xe máy SH kèm đường link yêu cầu đăng nhập mật khẩu Facebook để nhận thưởng. Em sẽ xử lí như thế nào?",
            "steps": [
              "Bước 1: Nhận diện dấu hiệu lừa đảo: tin nhắn trúng thưởng bất ngờ từ người lạ, đường link giả mạo (phishing) nhằm đánh cắp tài khoản.",
              "Bước 2: Tuyệt đối không bấm vào đường link lạ và không cung cấp bất kì thông tin cá nhân hay mật khẩu nào.",
              "Bước 3: Chặn tin nhắn, báo cáo tài khoản lừa đảo cho ban quản trị mạng xã hội và cảnh báo cho bạn bè, người thân."
            ],
            "answer": "Không bấm vào liên kết, không cung cấp thông tin, chặn và báo cáo hành vi lừa đảo."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Sử dụng chung một mật khẩu đơn giản (như 123456, ngày sinh) cho tất cả các tài khoản mạng xã hội và email.",
            "why": "Khi một tài khoản bị lộ, kẻ tấn công sẽ dễ dàng chiếm đoạt toàn bộ các tài khoản còn lại."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Tổ chức lưu trữ và Chia sẻ tài nguyên trên Điện toán đám mây",
        "description": "Dịch vụ lưu trữ đám mây (Google Drive, OneDrive), chia sẻ tài liệu số, làm việc nhóm trực tuyến và bảo mật thư điện tử nâng cao.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Lưu trữ và đồng bộ dữ liệu trên đám mây", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hợp tác làm việc nhóm trực tuyến hiệu quả", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Điện toán đám mây (Cloud Computing)",
            "definition": "Mô hình cung cấp tài nguyên điện toán (máy chủ, dung lượng lưu trữ, phần mềm) qua Internet theo yêu cầu của người dùng mà không cần cài đặt phần cứng cồng kềnh tại chỗ.",
            "example": "Lưu file trên Google Drive giúp truy cập tài liệu từ mọi thiết bị điện thoại, máy tính bảng hay laptop ở bất kì đâu có Internet.",
            "essence": "Đồng bộ hóa tức thời, sao lưu tự động và khả năng phục hồi dữ liệu vượt trội."
          },
          {
            "term": "Phân quyền chia sẻ tài liệu trực tuyến",
            "definition": "Các mức quyền hạn khi chia sẻ tệp tin: 1) Người xem (Viewer). 2) Người nhận xét (Commenter). 3) Người chỉnh sửa (Editor).",
            "example": "Khi nộp bài tập nhóm cho giáo viên, nên phân quyền 'Người nhận xét' hoặc 'Người xem' để tránh vô tình bị sửa đổi nội dung.",
            "essence": "Quản trị quyền truy cập chặt chẽ bảo vệ tính toàn vẹn của dữ liệu."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc sao lưu dữ liệu 3-2-1",
            "meaning": "Lưu giữ ít nhất 3 bản sao dữ liệu, trên 2 loại phương tiện lưu trữ khác nhau, và ít nhất 1 bản sao được lưu trữ ở nơi khác (trên đám mây).",
            "example": "File khóa luận lưu trên máy tính cá nhân, 1 bản trên USB và 1 bản trên Google Drive.",
            "essence": "Chiến lược an toàn tuyệt đối chống lại nguy cơ hỏng ổ cứng hay nhiễm mã độc tống tiền (ransomware)."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày các bước tạo thư mục chung trên Google Drive để 4 bạn trong tổ cùng soạn thảo bài báo cáo thuyết trình môn Khoa học tự nhiên.",
            "steps": [
              "Bước 1: Đăng nhập Google Drive, bấm 'Mới' -> chọn 'Thư mục mới', đặt tên 'Bao cao KHTN 9 To 1'.",
              "Bước 2: Nhấp chuột phải vào thư mục, chọn 'Chia sẻ' (Share).",
              "Bước 3: Nhập địa chỉ email của 3 bạn trong tổ, thiết lập quyền 'Người chỉnh sửa' (Editor) và bấm Gửi.",
              "Bước 4: Tạo tệp Google Trang trình bày (Slides) bên trong thư mục để cả nhóm cùng thiết kế đồng thời."
            ],
            "answer": "Thư mục dùng chung được thiết lập với quyền chỉnh sửa giúp cả nhóm làm việc cộng tác thời gian thực."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chia sẻ tệp với quyền 'Bất kì ai có đường liên kết đều có thể chỉnh sửa' mà không giới hạn quyền truy cập.",
            "why": "Bất kì ai nhận được link đều có thể xóa hoặc sửa hỏng tài liệu của nhóm."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Đạo đức, Pháp luật và Văn hóa trong Môi trường số",
        "description": "Bản quyền phần mềm, sở hữu trí tuệ số, phòng chống mã độc (virus, trojan, ransomware), quy định của Luật An ninh mạng Việt Nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tôn trọng bản quyền tác giả và sở hữu trí tuệ số", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phòng chống mã độc và tuân thủ Luật An ninh mạng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bản quyền phần mềm và Giấy phép mã nguồn mở",
            "definition": "Phần mềm thương mại yêu cầu mua bản quyền để sử dụng hợp pháp. Phần mềm mã nguồn mở (như Linux, LibreOffice) cho phép người dùng tự do sử dụng, chỉnh sửa và phân phối theo giấy phép GPL/MIT.",
            "example": "Sử dụng phần mềm 'bẻ khóa' (crack) là hành vi vi phạm bản quyền và tiềm ẩn nguy cơ nhiễm virus độc hại rất cao.",
            "essence": "Tôn trọng công sức sáng tạo của lập trình viên và xây dựng hệ sinh thái công nghệ lành mạnh."
          },
          {
            "term": "Luật An ninh mạng Việt Nam",
            "definition": "Quy định về bảo đảm an ninh mạng; quyền và trách nhiệm của cơ quan, tổ chức, cá nhân tham gia không gian mạng; nghiêm cấm các hành vi phát tán thông tin sai sự thật, xúc phạm danh dự người khác hoặc tấn công mạng.",
            "example": "Tung tin thất thiệt về vỡ đập hay thiên tai trên Facebook bị xử phạt hành chính từ 10 đến 20 triệu đồng theo pháp luật.",
            "essence": "Không gian mạng là không gian thực ảo song hành; mọi hành vi đều chịu sự điều chỉnh của pháp luật."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc trích dẫn học thuật số chuẩn mực",
            "meaning": "Khi sử dụng hình ảnh, đoạn văn hoặc video của người khác trong bài thuyết trình, bắt buộc phải ghi rõ tên tác giả và đường dẫn nguồn gốc.",
            "example": "Ghi chú dưới chân ảnh: 'Nguồn ảnh: Báo Nhân Dân, phóng viên Nguyễn Văn A (2026)'.",
            "essence": "Tránh lỗi đạo văn (plagiarism) và tôn trọng quyền tác giả."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân biệt virus máy tính và phần mềm gián điệp (Spyware).",
            "steps": [
              "Bước 1: Virus máy tính: Là đoạn mã độc có khả năng tự nhân bản lây nhiễm từ file này sang file khác, phá hủy dữ liệu hoặc làm tê liệt hệ điều hành.",
              "Bước 2: Phần mềm gián điệp (Spyware): Chạy ngầm trong máy tính để bí mật theo dõi thao tác bàn phím, đánh cắp mật khẩu, tài khoản ngân hàng và gửi về máy chủ của tin tặc.",
              "Bước 3: Biện pháp phòng chống chung: Cài đặt phần mềm diệt virus chính hãng (Windows Defender, Kaspersky), không tải file từ nguồn không rõ ràng."
            ],
            "answer": "Virus tập trung phá hoại hệ thống, trong khi Spyware tập trung đánh cắp dữ liệu riêng tư nhạy cảm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng tải phim, nhạc, sách lậu từ các trang web chia sẻ miễn phí là vô hại.",
            "why": "Các tệp crack thường bị chèn mã độc ngầm để biến máy tính của nạn nhân thành mạng máy tính ma (botnet)."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Phân tích Dữ liệu với Bảng tính và Giải quyết Vấn đề",
        "description": "Các hàm thống kê nâng cao (SUMIF, COUNTIF, VLOOKUP/XLOOKUP), biểu đồ phân tích trực quan dữ liệu, tư duy thuật toán chia để trị trong tin học.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sử dụng các hàm tính toán có điều kiện trong bảng tính điện tử", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tạo biểu đồ trực quan hóa dữ liệu và tư duy thuật toán", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hàm tính toán có điều kiện COUNTIF và SUMIF",
            "definition": "COUNTIF(range, criteria): Đếm số ô thỏa mãn tiêu chuẩn. SUMIF(range, criteria, sum_range): Tính tổng các ô thỏa mãn tiêu chuẩn.",
            "example": "=COUNTIF(C2:C40, '>=8.0') đếm số học sinh đạt điểm giỏi từ 8.0 trở lên trong danh sách lớp.",
            "essence": "Tự động hóa trích xuất thông tin định lượng từ tập dữ liệu lớn mà không cần đếm thủ công."
          },
          {
            "term": "Trực quan hóa dữ liệu (Data Visualization)",
            "definition": "Chuyển đổi số liệu dạng bảng thành biểu đồ trực quan: biểu đồ cột (so sánh số lượng), biểu đồ tròn (thể hiện cơ cấu %), biểu đồ đường (thể hiện xu hướng biến thiên theo thời gian).",
            "example": "Dùng biểu đồ đường để theo dõi diễn biến nhiệt độ trung bình các tháng trong năm tại Hà Nội.",
            "essence": "Một hình ảnh trực quan truyền tải thông điệp nhanh gấp hàng chục lần một bảng tính dày đặc số liệu."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc chọn loại biểu đồ phù hợp trong Excel",
            "meaning": "Cơ cấu thành phần -> Biểu đồ hình tròn (Pie chart); So sánh các đối tượng -> Biểu đồ cột (Column chart); Xu hướng tăng giảm qua các năm -> Biểu đồ đường (Line chart).",
            "example": "Biểu diễn cơ cấu 3 khu vực kinh tế dùng biểu đồ tròn tỉ lệ %.",
            "essence": "Chọn sai loại biểu đồ làm sai lệch nhận thức của người xem về bản chất dữ liệu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Viết công thức Excel để tính tổng tiền bán hàng của nhân viên có tên 'Nguyễn Nam' trong bảng tính có cột Tên (B2:B20) và cột Thành tiền (D2:D20).",
            "steps": [
              "Bước 1: Xác định hàm cần dùng: tính tổng theo điều kiện là hàm SUMIF.",
              "Bước 2: Vùng điều kiện là cột Tên nhân viên: B2:B20.",
              "Bước 3: Tiêu chuẩn điều kiện là: 'Nguyễn Nam'.",
              "Bước 4: Vùng tính tổng là cột Thành tiền: D2:D20.",
              "Bước 5: Lắp ghép công thức: =SUMIF(B2:B20, 'Nguyễn Nam', D2:D20)."
            ],
            "answer": "Công thức là: =SUMIF(B2:B20, \"Nguyễn Nam\", D2:D20)"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên đặt dấu ngoặc kép quanh tiêu chuẩn điều kiện dạng chuỗi hoặc biểu thức so sánh: =COUNTIF(A1:A10, >=5).",
            "why": "Excel sẽ báo lỗi cú pháp; phải viết là =COUNTIF(A1:A10, \">=5\")."
          }
        ]
      }
    ]
  },
  "giao-duc-cong-dan": {
    "id": "giao-duc-cong-dan",
    "name": "Giáo dục công dân",
    "icon": "🏛️",
    "chapters": [
      {
        "id": "ch01",
        "title": "Bài 1: Chí công vô tư và Tự chủ trong cuộc sống",
        "description": "Khái niệm chí công vô tư, tính tự chủ, làm chủ bản thân trước cám dỗ, rèn luyện phẩm chất đạo đức của người công dân có trách nhiệm.",
        "lessons": [
          { "id": "l01", "title": "Tiết 1: Phẩm chất chí công vô tư và ý nghĩa xã hội", "hasRealContent": true },
          { "id": "l02", "title": "Tiết 2: Tính tự chủ và kỹ năng kiểm soát cảm xúc bản thân", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chí công vô tư",
            "definition": "Là phẩm chất đạo đức của con người, thể hiện ở sự công bằng, không thiên vị, giải quyết công việc theo lẽ phải, xuất phát từ lợi ích chung và đặt lợi ích của tập thể lên trên lợi ích cá nhân.",
            "example": "Chủ tịch Hồ Chí Minh là tấm gương sáng ngời trọn đời hi sinh cho độc lập dân tộc mà không màng danh lợi cá nhân.",
            "essence": "Làm cho xã hội công bằng, dân chủ, tạo được lòng tin yêu và kính trọng của mọi người xung quanh."
          },
          {
            "term": "Tính tự chủ",
            "definition": "Là khả năng làm chủ bản thân: làm chủ suy nghĩ, tình cảm và hành vi của mình trong mọi hoàn cảnh, luôn có thái độ bình tĩnh, tự tin và biết điều chỉnh hành vi phù hợp.",
            "example": "Trước lời rủ rê trốn học đi chơi game của bạn bè, em kiên quyết từ chối để ở lại trường ôn bài.",
            "essence": "Người có tính tự chủ biết vượt qua khó khăn, không bị cám dỗ bởi các tệ nạn xã hội."
          }
        ],
        "rules": [
          {
            "statement": "Phương pháp rèn luyện tính tự chủ",
            "meaning": "Tập suy nghĩ kĩ trước khi nói và hành động; xem xét hậu quả của hành vi; sau mỗi việc làm cần rút kinh nghiệm; khi nóng giận cần hít thở sâu và giữ im lặng.",
            "example": "Không vội vàng tranh cãi khi người khác hiểu lầm mà bình tĩnh giải thích bằng lý lẽ mềm mỏng.",
            "essence": "'Thắng vạn quân chưa phải là chiến công oanh liệt nhất, chiến thắng chính bản thân mình mới là chiến công vẻ vang nhất'."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trong cuộc bình bầu thi đua cuối năm của lớp, bạn thân của lớp trưởng vi phạm nhiều lỗi nhưng lớp trưởng vẫn đề nghị xếp bạn loại Tốt để giữ thành tích. Em nhận xét gì về việc làm của bạn lớp trưởng?",
            "steps": [
              "Bước 1: Nhận xét: Việc làm của bạn lớp trưởng là sai, không thể hiện phẩm chất chí công vô tư.",
              "Bước 2: Phân tích: Bạn lớp trưởng đã để tình cảm cá nhân xen vào việc chung, bao che khuyết điểm khiến việc đánh giá thiếu công bằng và không giúp bạn tiến bộ.",
              "Bước 3: Lời khuyên: Cần thẳng thắn chỉ ra khuyết điểm trên tinh thần xây dựng để bạn sửa chữa, đồng thời đảm bảo tính minh bạch, công bằng của tập thể."
            ],
            "answer": "Lớp trưởng thiếu tính chí công vô tư; cần đánh giá công tâm vì sự tiến bộ chung của tập thể lớp."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đồng nhất chí công vô tư với sự thờ ơ, lạnh lùng, không quan tâm đến quyền lợi chính đáng của cá nhân.",
            "why": "Chí công vô tư bảo vệ lẽ phải và lợi ích chính đáng của mọi người, không chà đạp quyền lợi hợp pháp của bất kì ai."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Bài 2: Bảo vệ hòa bình và Tình hữu nghị giữa các dân tộc",
        "description": "Khái niệm hòa bình, hậu quả tàn khốc của chiến tranh, chính sách đối ngoại rộng mở của Việt Nam, xây dựng tình bạn hữu nghị quốc tế.",
        "lessons": [
          { "id": "l01", "title": "Tiết 1: Ý nghĩa của hòa bình và trách nhiệm bảo vệ hòa bình", "hasRealContent": true },
          { "id": "l02", "title": "Tiết 2: Tình hữu nghị và hợp tác cùng phát triển giữa các dân tộc", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bảo vệ hòa bình",
            "definition": "Là gìn giữ cuộc sống bình yên, không để xảy ra chiến tranh hay xung đột vũ trang; giải quyết mọi tranh chấp, bất đồng giữa các quốc gia, dân tộc bằng biện pháp đàm phán hòa bình trên cơ sở luật pháp quốc tế.",
            "example": "Thủ đô Hà Nội vinh dự được UNESCO trao tặng danh hiệu 'Thành phố vì hòa bình' năm 1999.",
            "essence": "Hòa bình là khát vọng thiêng liêng của toàn nhân loại, đem lại cuộc sống ấm no, hạnh phúc cho mọi trẻ em."
          },
          {
            "term": "Chính sách đối ngoại của Việt Nam",
            "definition": "'Việt Nam là bạn, là đối tác tin cậy và là thành viên tích cực, có trách nhiệm trong cộng đồng quốc tế'.",
            "example": "Việt Nam cử lực lượng gìn giữ hòa bình tham gia các phái bộ của Liên Hợp Quốc tại Nam Sudan và Cộng hòa Trung Phi.",
            "essence": "Đa phương hóa, đa dạng hóa các mối quan hệ quốc tế trên nguyên tắc tôn trọng độc lập chủ quyền và cùng có lợi."
          }
        ],
        "rules": [
          {
            "statement": "Hành vi thể hiện tinh thần yêu chuộng hòa bình của học sinh",
            "meaning": "Tôn trọng bạn bè khác sắc tộc, vùng miền; không gây gổ bạo lực học đường; biết lắng nghe hòa giải mâu thuẫn; giao lưu văn hóa quốc tế cởi mở.",
            "example": "Tham gia vẽ tranh, viết thư UPU quốc tế về chủ đề hòa bình và chống biến đổi khí hậu.",
            "essence": "Hòa bình thế giới bắt đầu từ sự hòa thuận trong lớp học và gia đình mỗi ngày."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao loài người tiến bộ hiện nay cần phải kiên quyết ngăn chặn chiến tranh và bảo vệ hòa bình?",
            "steps": [
              "Bước 1: Chiến tranh hiện đại với vũ khí hủy diệt hàng loạt (hạt nhân, sinh học) có thể hủy diệt toàn bộ nền văn minh nhân loại và môi trường Trái Đất.",
              "Bước 2: Chiến tranh cướp đi sinh mạng của hàng triệu người vô tội, tàn phá nhà cửa bệnh viện trường học, gây đói nghèo li tán.",
              "Bước 3: Chỉ trong môi trường hòa bình, các quốc gia mới có thể hợp tác giải quyết các thách thức toàn cầu như dịch bệnh, biến đổi khí hậu."
            ],
            "answer": "Bảo vệ hòa bình là điều kiện tiên quyết để nhân loại sinh tồn và phát triển thịnh vượng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng bảo vệ hòa bình là trách nhiệm của riêng các nguyên thủ quốc gia, học sinh nhỏ tuổi không làm được gì.",
            "why": "Mỗi hành vi ứng xử văn minh, chống bạo lực học đường của học sinh đều đóng góp trực tiếp vào việc nuôi dưỡng môi trường sống hòa bình."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Bài 3: Kế thừa và Phát huy Truyền thống tốt đẹp của Dân tộc",
        "description": "Các truyền thống quý báu của dân tộc Việt Nam (yêu nước, đoàn kết, nhân nghĩa, hiếu học), phê phán thái độ tự ti hoặc sùng ngoại mù quáng.",
        "lessons": [
          { "id": "l01", "title": "Tiết 1: Các truyền thống đạo đức và văn hóa tốt đẹp của dân tộc", "hasRealContent": true },
          { "id": "l02", "title": "Tiết 2: Trách nhiệm của thế hệ trẻ trong việc giữ gìn và phát huy truyền thống", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Truyền thống tốt đẹp của dân tộc",
            "definition": "Là những giá trị tinh thần (tư tưởng, đạo đức, tập quán, lối sống) được hình thành trong lịch sử dựng nước và giữ nước, được truyền từ thế hệ này sang thế hệ khác.",
            "example": "Truyền thống yêu nước nồng nàn, đoàn kết một lòng, 'Tương thân tương ái', 'Uống nước nhớ nguồn', hiếu thảo với cha mẹ, tôn sư trọng đạo.",
            "essence": "Là nguồn sức mạnh vô tận giúp dân tộc Việt Nam vượt qua mọi giông bão ngoại xâm và thiên tai để trường tồn."
          },
          {
            "term": "Thái độ đúng đắn đối với truyền thống",
            "definition": "Tự hào, trân trọng, bảo vệ và phát huy những nét đẹp truyền thống; đồng thời kiên quyết bài trừ những hủ tục lạc hậu, mê tín dị đoan không còn phù hợp với đời sống hiện đại.",
            "example": "Học sinh mặc trang phục áo dài truyền thống trong các ngày lễ trang trọng, học hát dân ca quan họ, chèo.",
            "essence": "'Hòa nhập nhưng không hòa tan' trong dòng chảy toàn cầu hóa văn hóa."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc tiếp thu tinh hoa văn hóa nhân loại",
            "meaning": "Tiếp thu có chọn lọc những thành tựu văn minh tiến bộ của thế giới trên nền tảng giữ vững cốt cách và bản sắc văn hóa dân tộc Việt Nam.",
            "example": "Học tập công nghệ tiên tiến của phương Tây nhưng vẫn giữ trọn đạo hiếu và tình làng nghĩa xóm của người Á Đông.",
            "essence": "Bản sắc văn hóa dân tộc là tấm căn cước công dân đưa đất nước tự tin bước ra thế giới."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một bạn học sinh cho rằng: 'Trong thời đại công nghệ số 4.0, các phong tục cổ truyền như gói bánh chưng ngày Tết hay đi chúc Tết ông bà là rườm rà, lạc hậu'. Em sẽ trao đổi với bạn như thế nào?",
            "steps": [
              "Bước 1: Khẳng định ý kiến của bạn là phiến diện và chưa hiểu đúng giá trị của phong tục cổ truyền.",
              "Bước 2: Phân tích ý nghĩa: Tục gói bánh chưng và chúc Tết là dịp để con cháu sum vầy, tri ân tổ tiên, gắn kết tình cảm gia đình sau một năm bận rộn.",
              "Bước 3: Kết luận: Đó là những giá trị nhân văn cao đẹp cần được gìn giữ và trân trọng trong mọi thời đại công nghệ."
            ],
            "answer": "Phong tục ngày Tết là nét đẹp văn hóa tâm linh gắn kết gia đình thiêng liêng, không thể xem là lạc hậu."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa nét đẹp truyền thống văn hóa với các phong tục tập quán hủ lậu, mê tín dị đoan (đốt nhiều vàng mã, bói toán).",
            "why": "Cần phân định rạch ròi: giữ gìn tinh hoa đạo đức tốt đẹp và loại bỏ những hủ tục tốn kém, lạc hậu."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Bài 4: Quyền và Nghĩa vụ của Công dân trong Gia đình, Lao động và Kinh doanh",
        "description": "Quyền và nghĩa vụ hôn nhân gia đình, quyền tự do kinh doanh và nghĩa vụ nộp thuế, quyền và nghĩa vụ lao động của công dân theo Hiến pháp.",
        "lessons": [
          { "id": "l01", "title": "Tiết 1: Quyền và nghĩa vụ của công dân trong hôn nhân và gia đình", "hasRealContent": true },
          { "id": "l02", "title": "Tiết 2: Quyền tự do kinh doanh, nghĩa vụ đóng thuế và nghĩa vụ lao động", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quyền và nghĩa vụ trong gia đình",
            "definition": "Cha mẹ có nghĩa vụ nuôi dạy con thành công dân tốt; con cái có bổn phận yêu quý, kính trọng, chăm sóc và phụng dưỡng cha mẹ khi già yếu.",
            "example": "Nghiêm cấm các hành vi bạo lực gia đình, phân biệt đối xử giữa các con hoặc ngược đãi cha mẹ già.",
            "essence": "Gia đình là tế bào của xã hội, là cái nôi nuôi dưỡng nhân cách của mỗi con người."
          },
          {
            "term": "Quyền tự do kinh doanh và Nghĩa vụ nộp thuế",
            "definition": "Công dân có quyền tự do lựa chọn ngành nghề, quy mô kinh doanh theo quy định của pháp luật, đồng thời có nghĩa vụ kê khai trung thực và nộp thuế đầy đủ vào ngân sách nhà nước.",
            "example": "Cửa hàng kinh doanh phải niêm yết giá công khai, bán hàng đảm bảo vệ sinh an toàn thực phẩm và xuất hóa đơn điện tử.",
            "essence": "Thuế là nguồn thu chủ yếu của ngân sách nhà nước để chi trả cho giáo dục, y tế, quốc phòng và xây dựng đường sá."
          }
        ],
        "rules": [
          {
            "statement": "Độ tuổi tham gia lao động theo Bộ luật Lao động",
            "meaning": "Người lao động là người từ đủ 15 tuổi trở lên, có khả năng lao động và làm việc theo hợp đồng lao động.",
            "example": "Nghiêm cấm người sử dụng lao động cưỡng bức, bóc lột hoặc sử dụng lao động chưa thành niên làm công việc nặng nhọc, nguy hiểm.",
            "essence": "Bảo vệ quyền lợi chính đáng và sự phát triển toàn diện của thanh thiếu niên."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Anh Nam mở một quán ăn nhưng trốn thuế, không đăng kí giấy phép an toàn vệ sinh thực phẩm và xả nước thải bẩn chưa qua xử lí ra mương thoát nước chung. Anh Nam đã vi phạm những quy định pháp luật nào?",
            "steps": [
              "Bước 1: Vi phạm nghĩa vụ nộp thuế của công dân (hành vi trốn thuế).",
              "Bước 2: Vi phạm quy định về điều kiện an toàn vệ sinh thực phẩm trong kinh doanh dịch vụ ăn uống.",
              "Bước 3: Vi phạm Luật Bảo vệ môi trường (xả thải trực tiếp gây ô nhiễm môi trường công cộng)."
            ],
            "answer": "Anh Nam vi phạm pháp luật về thuế, vệ sinh an toàn thực phẩm và bảo vệ môi trường; sẽ bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng công dân có quyền kinh doanh bất kì mặt hàng nào mà không cần tuân theo danh mục ngành nghề của pháp luật.",
            "why": "Pháp luật nghiêm cấm kinh doanh các mặt hàng độc hại, ma túy, vũ khí quân dụng, pháo nổ hoặc động vật hoang dã nguy cấp."
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
        "title": "Chương 1: Định hướng Nghề nghiệp trong Kĩ thuật và Công nghệ",
        "description": "Thế giới nghề nghiệp trong thời đại 4.0, các ngành nghề kĩ thuật then chốt (cơ khí, điện - điện tử, CNTT), tự đánh giá sở thích và năng lực nghề nghiệp.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tổng quan về nghề nghiệp kĩ thuật và công nghệ hiện đại", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tự đánh giá năng lực và lập kế hoạch nghề nghiệp tương lai", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thị trường lao động thời đại CMCN 4.0",
            "definition": "Đặc trưng bởi sự kết hợp giữa các công nghệ số, vật lí và sinh học; gia tăng nhu cầu về các vị trí việc làm liên quan đến tự động hóa, trí tuệ nhân tạo (AI), robot và IoT.",
            "example": "Kĩ sư phần mềm, kĩ sư cơ điện tử, chuyên gia phân tích dữ liệu, kĩ thuật viên năng lượng tái tạo.",
            "essence": "Đòi hỏi người lao động phải có tư duy logic, kỹ năng số, ngoại ngữ và tinh thần tự học nâng cao trình độ suốt đời."
          },
          {
            "term": "Nguyên tắc chọn nghề theo mô hình Tam giác hướng nghiệp",
            "definition": "Sự giao thoa giữa 3 yếu tố: 1) Sở thích, đam mê của bản thân. 2) Năng lực, thế mạnh thực tế. 3) Nhu cầu việc làm của xã hội.",
            "example": "Chọn ngành nghề mình yêu thích và có thế mạnh, đồng thời xã hội đang có nhu cầu tuyển dụng cao.",
            "essence": "Tránh chạy theo ngành nghề theo phong trào nhất thời mà thiếu năng lực chuyên môn phù hợp."
          }
        ],
        "rules": [
          {
            "statement": "Các bước lập kế hoạch nghề nghiệp cho học sinh lớp 9",
            "meaning": "Bước 1: Tìm hiểu bản thân -> Bước 2: Khám phá thế giới nghề nghiệp -> Bước 3: Lựa chọn hướng đi sau THCS (vào THPT chuyên/thường, trường nghề, trung cấp) -> Bước 4: Lập kế hoạch học tập cụ thể.",
            "example": "Học sinh có thiên hướng kĩ thuật thực hành có thể định hướng vào các trường nghề chất lượng cao để sớm có việc làm.",
            "essence": "Chủ động phân luồng học sinh sau tốt nghiệp THCS phù hợp với hoàn cảnh và năng lực."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Bạn Minh học rất giỏi môn Toán và Tin học, thích mày mò lập trình và lắp ráp vi mạch điều khiển xe robot tự hành. Em hãy tư vấn ngành học tương lai phù hợp cho Minh.",
            "steps": [
              "Bước 1: Đánh giá thế mạnh: Tư duy logic toán học tốt, đam mê công nghệ phần cứng và phần mềm.",
              "Bước 2: Gợi ý các ngành nghề: Ngành Kĩ thuật Cơ điện tử (Mechatronics), Kĩ thuật Robot và Trí tuệ nhân tạo, Kĩ thuật Máy tính.",
              "Bước 3: Lời khuyên học tập: Tiếp tục ôn thi tốt vào lớp 10 khối tự nhiên, tham gia các câu lạc bộ STEM robot và nâng cao trình độ tiếng Anh kĩ thuật."
            ],
            "answer": "Tư vấn ngành Kĩ thuật Cơ điện tử hoặc Kĩ thuật Máy tính / Robot."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chọn nghề chỉ dựa vào ý kiến ép buộc của cha mẹ hoặc đi theo bạn bè mà không xét đến năng lực thực tế của bản thân.",
            "why": "Dễ dẫn đến tình trạng chán nản, bỏ học hoặc khó tìm được việc làm phù hợp sau khi ra trường."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Thiết kế và Lắp đặt Mạch điện Gia đình",
        "description": "Vật liệu và thiết bị điện dân dụng, sơ đồ nguyên lí và sơ đồ lắp đặt mạch điện chiếu sáng, aptomat, công tắc, cầu chì, chuông điện.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sơ đồ nguyên lí và sơ đồ lắp đặt mạch điện dân dụng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành lắp đặt mạch điện một công tắc điều khiển một đèn và mạch hai công tắc ba cực", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Sơ đồ nguyên lí và Sơ đồ lắp đặt",
            "definition": "Sơ đồ nguyên lí: Nêu lên mối liên hệ về điện giữa các phần tử mà không phụ thuộc vị trí đặt thực tế. Sơ đồ lắp đặt: Biểu thị rõ vị trí lắp đặt cụ thể của các thiết bị và đường đi của dây dẫn trong phòng.",
            "example": "Khi thi công đấu dây thực tế trong gia đình, người thợ điện bắt buộc phải dựa vào sơ đồ lắp đặt.",
            "essence": "Từ sơ đồ nguyên lí tiến hành thiết kế sơ đồ lắp đặt trước khi thi công đường dây."
          },
          {
            "term": "Mạch điện cầu thang (Hai công tắc 3 cực điều khiển 1 đèn)",
            "definition": "Mạch điện sử dụng hai công tắc ba cực đặt ở tầng 1 và tầng 2 để có thể bật/tắt cùng một bóng đèn cầu thang từ cả hai vị trí khác nhau.",
            "example": "Bật đèn ở tầng 1 để đi lên tầng 2, sau đó tắt đèn bằng công tắc ở tầng 2 mà không cần quay lại tầng 1.",
            "essence": "Đem lại sự tiện nghi và tiết kiệm điện năng cho các công trình nhà nhiều tầng."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc lắp đặt cầu chì và công tắc an toàn",
            "meaning": "Cầu chì và công tắc bắt buộc phải được lắp trên dây pha (dây nóng L), tuyệt đối không lắp trên dây trung tính (dây nguội N).",
            "example": "Khi ngắt công tắc để thay bóng đèn, điện áp pha không còn truyền đến đui đèn, tránh nguy cơ bị điện giật.",
            "essence": "Quy chuẩn an toàn điện dân dụng sống còn cho thợ điện và người sử dụng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Vẽ quy trình các bước thực hành lắp đặt mạch điện bảng điện gia đình gồm 1 cầu chì, 1 công tắc điều khiển 1 bóng đèn sợi đốt.",
            "steps": [
              "Bước 1: Vạch dấu vị trí các thiết bị trên bảng điện và vị trí bóng đèn trên bảng thực hành.",
              "Bước 2: Khoan lỗ bảng điện để luồn dây và bắt vít cố định thiết bị.",
              "Bước 3: Nối dây mạch điện: Nối dây nguồn pha (L) qua cầu chì -> vào công tắc -> vào một cực của bóng đèn; Cực còn lại của bóng đèn nối về dây trung tính (N).",
              "Bước 4: Bắt vít cố định các thiết bị vào bảng điện và lắp bóng đèn vào đui.",
              "Bước 5: Kiểm tra thông mạch bằng đồng hồ vạn năng trước khi đóng nguồn điện thử nghiệm."
            ],
            "answer": "Quy trình 5 bước đảm bảo an toàn tuyệt đối và đúng tiêu chuẩn kĩ thuật điện."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lắp công tắc vào dây nguội (dây trung tính N) thay vì dây nóng (dây pha L).",
            "why": "Khi tắt công tắc đèn vẫn tắt nhưng đui đèn vẫn mang điện thế 220V nguy hiểm; chạm vào đui đèn sẽ bị giật điện ngay lập tức."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: An toàn Điện và Tiết kiệm Năng lượng",
        "description": "Các nguyên nhân gây tai nạn điện, biện pháp an toàn điện (nối đất, aptomat chống giật ELCB), sử dụng thiết bị Inverter tiết kiệm điện.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: An toàn điện và xử lí sự cố điện giật", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tiết kiệm năng lượng điện và bảo vệ môi trường", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Aptomat chống giật (ELCB/RCCB)",
            "definition": "Thiết bị bảo vệ tự động ngắt nguồn điện trong thời gian phần nghìn giây khi phát hiện dòng điện rò rỉ ra vỏ kim loại của thiết bị hoặc qua cơ thể người xuống đất vượt quá 30 mA.",
            "example": "Lắp ELCB riêng cho bình nóng lạnh và máy giặt để ngăn ngừa sự cố rò điện gây nguy hiểm tính mạng trong phòng tắm ẩm ướt.",
            "essence": "Cứu mạng sống con người trước các rủi ro hở điện mà cầu chì thông thường không thể ngắt được."
          },
          {
            "term": "Công nghệ Inverter (Biến tần tiết kiệm điện)",
            "definition": "Công nghệ điều khiển tần số dòng điện để thay đổi tốc độ quay của máy nén linh hoạt theo nhiệt độ phòng thay vì liên tục bật/tắt toàn bộ động cơ.",
            "example": "Điều hòa nhiệt độ Inverter giúp tiết kiệm từ 30% đến 50% điện năng tiêu thụ so với điều hòa truyền thống.",
            "essence": "Vận hành êm ái, kéo dài tuổi thọ thiết bị và giảm thiểu chi phí tiền điện hàng tháng."
          }
        ],
        "rules": [
          {
            "statement": "Các bước sơ cứu người bị điện giật",
            "meaning": "Bước 1: Nhanh chóng ngắt cầu dao hoặc aptomat tổng. Bước 2: Dùng vật cách điện khô (gậy gỗ, thanh nhựa) gạt dây điện ra khỏi người nạn nhân (tuyệt đối không chạm tay trực tiếp). Bước 3: Đưa nạn nhân ra nơi thoáng khí và thực hiện hà hơi thổi ngạt, ép tim ngoài lồng ngực nếu ngừng thở.",
            "example": "Bình tĩnh xử lí và gọi cấp cứu y tế 115 ngay lập tức.",
            "essence": "Thời gian vàng sơ cứu trong vòng 3 phút đầu quyết định sự sống còn của nạn nhân."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Gia đình em sử dụng 4 bóng đèn LED 15W thắp sáng 6 giờ mỗi ngày. Tính lượng điện năng tiêu thụ trong 1 tháng (30 ngày) và số tiền tiết kiệm được so với việc dùng bóng đèn sợi đốt 60W (giá điện trung bình 2.500 đồng/kWh).",
            "steps": [
              "Bước 1: Điện năng đèn LED trong 30 ngày: A_LED = 4 * 15 * 6 * 30 = 10.800 Wh = 10,8 kWh.",
              "Bước 2: Điện năng đèn sợi đốt trong 30 ngày: A_soidot = 4 * 60 * 6 * 30 = 43.200 Wh = 43,2 kWh.",
              "Bước 3: Lượng điện năng tiết kiệm được: delta A = 43,2 - 10,8 = 32,4 kWh.",
              "Bước 4: Số tiền tiết kiệm được trong tháng: 32,4 * 2.500 = 81.000 đồng."
            ],
            "answer": "Tiết kiệm được 32,4 kWh điện và giảm được 81.000 đồng tiền điện mỗi tháng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lao vào dùng tay không kéo người bị điện giật ra khỏi nguồn điện.",
            "why": "Dòng điện sẽ truyền ngay lập tức qua cơ thể nạn nhân sang người cứu hộ khiến cả hai cùng bị điện giật."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Nhà thông minh (Smart Home) và Nông nghiệp Công nghệ cao",
        "description": "Hệ thống nhà thông minh Smart Home, cảm biến tự động, điều khiển qua smartphone, ứng dụng công nghệ IoT và tưới tự động trong nông nghiệp hiện đại.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái niệm và các hệ thống chức năng trong ngôi nhà thông minh", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Ứng dụng công nghệ cao và tự động hóa trong nông nghiệp", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hệ thống Smart Home (Ngôi nhà thông minh)",
            "definition": "Ngôi nhà được trang bị hệ thống điều khiển tự động hoặc bán tự động cho các thiết bị điện (chiếu sáng, rèm cửa, điều hòa, an ninh) kết nối qua mạng Internet.",
            "example": "Hệ thống đèn hành lang tự động bật sáng khi cảm biến hồng ngoại phát hiện có người bước vào và tự tắt sau 30 giây.",
            "essence": "Tối ưu hóa sự tiện nghi, an toàn và tiết kiệm năng lượng tối đa cho gia chủ."
          },
          {
            "term": "Hệ thống tưới nhỏ giọt tự động (Drip Irrigation)",
            "definition": "Hệ thống cung cấp nước và phân bón trực tiếp đến từng gốc rễ cây trồng với liều lượng chính xác thông qua mạng lưới ống dẫn và đầu tưới nhỏ giọt kiểm soát bằng van điện từ.",
            "example": "Hệ thống nhà màng trồng dưa lưới công nghệ cao tại Đà Lạt điều khiển tưới dựa trên dữ liệu cảm biến độ ẩm đất.",
            "essence": "Tiết kiệm từ 50% đến 70% lượng nước tưới so với phương pháp tưới rãnh truyền thống và tăng năng suất cây trồng."
          }
        ],
        "rules": [
          {
            "statement": "Cơ chế hoạt động của hệ thống an ninh nhà thông minh",
            "meaning": "Cảm biến cửa mở/cảm biến chuyển động -> Bộ điều khiển trung tâm (Gateway) -> Kích hoạt còi hú báo động -> Gửi thông báo khẩn cấp tức thời về điện thoại của chủ nhà.",
            "example": "Camera AI nhận diện khuôn mặt người lạ và cảnh báo đột nhập trái phép.",
            "essence": "Bảo vệ tài sản và sự an toàn của các thành viên trong gia đình 24/7."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Thiết kế một mô hình tự động hóa đơn giản: Khi độ ẩm đất trong chậu cây cảnh xuống dưới 40%, máy bơm mini sẽ tự động bật để tưới nước, và khi độ ẩm đạt 70% thì máy bơm sẽ tự ngắt.",
            "steps": [
              "Bước 1: Các thiết bị cần dùng: Cảm biến độ ẩm đất, vi điều khiển (như Arduino hoặc ESP32), module rơ-le (Relay), máy bơm nước mini 12V.",
              "Bước 2: Nguyên lí hoạt động: Cảm biến đo độ ẩm đất gửi tín hiệu liên tục về vi điều khiển.",
              "Bước 3: Thuật toán điều khiển: Nếu độ ẩm < 40%, gửi tín hiệu đóng rơ-le để cấp điện cho máy bơm hoạt động. Nếu độ ẩm >= 70%, gửi tín hiệu ngắt rơ-le để dừng bơm.",
              "Bước 4: Ứng dụng: Giúp cây trồng luôn đủ ẩm dù chủ nhà đi công tác vắng nhà nhiều ngày."
            ],
            "answer": "Mô hình IoT nông nghiệp thông minh khép kín kiểm soát độ ẩm đất hoàn toàn tự động."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng nhà thông minh bắt buộc phải đập phá xây lại toàn bộ ngôi nhà cũ.",
            "why": "Hiện nay các thiết bị thông minh sử dụng sóng không dây (Zigbee, Wi-Fi) có thể lắp đặt thay thế trực tiếp vào các đế âm tường cũ mà không cần can thiệp kết cấu nhà."
          }
        ]
      }
    ]
  }
}

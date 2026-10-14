# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa 8 môn học Lớp 5 SGK Kết nối tri thức với cuộc sống 2026-2027:
- Toán học (6 chương: Phân số & Số thập phân, Các phép tính số thập phân, Hình học phẳng, Hình học không gian, Số đo thời gian & Toán chuyển động đều, Ôn tập cuối cấp)
- Tiếng Việt (5 chủ điểm: Đọc hiểu, Từ đồng nghĩa - trái nghĩa - nhiều nghĩa, Đại từ & Quan hệ từ, Câu ghép & Liên kết câu, Tập làm văn miêu tả)
- Tiếng Anh (6 units Global Success chuẩn đầu ra Tiểu học)
- Khoa học (5 chủ đề: Chất và sự biến đổi, Năng lượng, Thực vật và động vật, Con người và sức khỏe, Môi trường)
- Lịch sử & Địa lí (5 chủ đề: Đất nước và con người Việt Nam, Lịch sử dựng nước và giữ nước, Địa lí các châu lục và thế giới)
- Tin học (4 chủ đề: Khám phá máy tính, An toàn không gian số, Soạn thảo & Bảng tính, Lập trình trực quan Scratch)
- Đạo đức (4 chủ đề: Biết ơn thầy cô & gia đình, Tôn trọng sự khác biệt, Vượt khó trong học tập, Yêu chuộng hòa bình)
- Công nghệ (4 chương: Đồ dùng điện gia đình, An toàn điện, Sáng chế công nghệ đơn giản, Lắp ghép mô hình kĩ thuật)
"""

true = True
false = False
null = None

GRADE_05_SUBJECTS = {
  "toan": {
    "id": "toan",
    "name": "Toán học",
    "icon": "🔢",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Phân số và Số thập phân",
        "description": "Ôn tập phân số, phân số thập phân, khái niệm số thập phân, hàng của số thập phân, so sánh và sắp xếp thứ tự các số thập phân.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Ôn tập phân số và phân số thập phân", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Khái niệm số thập phân và hàng của số thập phân", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: So sánh và viết các số thập phân theo thứ tự", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Số thập phân",
            "definition": "Mỗi số thập phân gồm hai phần: phần nguyên và phần thập phân, chúng được phân cách nhau bởi dấu phẩy. Những chữ số ở bên trái dấu phẩy thuộc về phần nguyên, những chữ số ở bên phải dấu phẩy thuộc về phần thập phân.",
            "example": "Trong số 35,48: phần nguyên là 35 (gồm 3 chục và 5 đơn vị), phần thập phân là 48 (gồm 4 phần mười và 8 phần trăm).",
            "essence": "Số thập phân là một cách viết gọn gàng của phân số thập phân giúp việc đo lường và tính toán trong đời sống tiện lợi hơn rất nhiều."
          },
          {
            "term": "Phân số thập phân",
            "definition": "Là các phân số có mẫu số là 10; 100; 1000; ...",
            "example": "3/10 = 0,3; 15/100 = 0,15; 275/1000 = 0,275.",
            "essence": "Mọi phân số có mẫu số chia hết cho 2 hoặc 5 đều có thể quy đồng về phân số thập phân."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc so sánh hai số thập phân",
            "meaning": "So sánh phần nguyên trước: số nào có phần nguyên lớn hơn thì số đó lớn hơn. Nếu phần nguyên bằng nhau, so sánh lần lượt các hàng ở phần thập phân từ trái sang phải: hàng phần mười, hàng phần trăm, hàng phần nghìn,...",
            "example": "So sánh 8,5 và 8,49: phần nguyên đều là 8; so sánh hàng phần mười có 5 > 4 nên 8,5 > 8,49.",
            "essence": "Tuyệt đối không đếm số lượng chữ số ở phần thập phân để kết luận số nào lớn hơn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Viết số thích hợp vào chỗ chấm: 3 m 45 cm = ... m và so sánh 4,75 với 4,705.",
            "steps": [
              "Bước 1: Đổi 45 cm = 45/100 m = 0,45 m.",
              "Bước 2: Vậy 3 m 45 cm = 3 + 0,45 = 3,45 m.",
              "Bước 3: So sánh 4,75 và 4,705: phần nguyên đều là 4; hàng phần mười đều là 7; hàng phần trăm có 5 > 0, do đó 4,75 > 4,705."
            ],
            "answer": "3 m 45 cm = 3,45 m và 4,75 > 4,705"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng 8,49 lớn hơn 8,5 vì số 49 trông 'dài hơn' và 'nhiều hơn' số 5.",
            "why": "Ở phần thập phân, 8,5 chính là 8,50; so sánh 50 phần trăm với 49 phần trăm thì rõ ràng 8,50 lớn hơn 8,49."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Các phép tính với Số thập phân",
        "description": "Phép cộng, phép trừ số thập phân; phép nhân số thập phân với số tự nhiên và với số thập phân; phép chia số thập phân; nhân nhẩm và chia nhẩm với 10, 100, 0,1, 0,01.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phép cộng và phép trừ số thập phân", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phép nhân số thập phân và nhân nhẩm với 10, 100, 0,1, 0,01", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Phép chia số thập phân và chia cho 0,1, 0,01", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Đặt tính cộng và trừ số thập phân",
            "definition": "Viết số hạng này dưới số hạng kia sao cho các chữ số ở cùng một hàng đặt thẳng cột với nhau (đặc biệt các dấu phẩy phải thẳng cột một hàng dọc). Cộng/trừ như đối với số tự nhiên rồi viết dấu phẩy ở kết quả thẳng cột với các dấu phẩy phía trên.",
            "example": "45,8 + 6,25 = 52,05 (đặt dấu phẩy của 45,8 và 6,25 thẳng hàng dọc).",
            "essence": "Thẳng cột dấu phẩy là quy tắc vàng sống còn để không bị cộng nhầm hàng chục với hàng phần mười."
          },
          {
            "term": "Vị trí dấu phẩy trong phép nhân số thập phân",
            "definition": "Đếm xem trong phần thập phân của cả hai thừa số có tất cả bao nhiêu chữ số rồi dùng dấu phẩy tách ở tích ra bấy nhiêu chữ số kể từ phải sang trái.",
            "example": "1,25 * 0,4: thừa số 1,25 có 2 chữ số thập phân, thừa số 0,4 có 1 chữ số thập phân => tổng cộng có 3 chữ số thập phân. 125 * 4 = 500 => Tích là 0,500 = 0,5.",
            "essence": "Số chữ số thập phân của tích bằng tổng số chữ số thập phân của các thừa số."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc nhân nhẩm và chia nhẩm đặc biệt",
            "meaning": "Nhân với 10; 100; 1000 chuyển dấu phẩy sang phải 1, 2, 3 chữ số. Nhân với 0,1; 0,01 chuyển dấu phẩy sang trái 1, 2 chữ số (tương đương chia cho 10, 100).",
            "example": "4,35 * 10 = 43,5; 4,35 * 0,1 = 0,435; 18,6 : 0,1 = 186.",
            "essence": "Nhân với 0,1 tương đương chia cho 10; chia cho 0,1 tương đương nhân với 10."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tính giá trị biểu thức bằng cách thuận tiện nhất: A = 3,45 * 8,7 + 3,45 * 1,3.",
            "steps": [
              "Bước 1: Nhận thấy cả hai tích đều có thừa số chung là 3,45.",
              "Bước 2: Áp dụng tính chất phân phối của phép nhân đối với phép cộng: A = 3,45 * (8,7 + 1,3).",
              "Bước 3: Tính trong ngoặc: 8,7 + 1,3 = 10,0 = 10.",
              "Bước 4: Thực hiện phép nhân nhẩm: 3,45 * 10 = 34,5."
            ],
            "answer": "A = 34,5"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Khi đặt tính 25,4 - 3,18 viết thành 25,4 - 3,18 rồi hạ 8 xuống thành đuôi 8 thay vì lấy 0 trừ 8 bằng 2 nhớ 1.",
            "why": "Phải hiểu 25,4 chính là 25,40. Khi trừ phải lấy 10 trừ 8 được 2, nhớ 1 vào 1 thành 2; 4 trừ 2 được 2."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Tỉ số phần trăm và Ứng dụng",
        "description": "Khái niệm tỉ số phần trăm, tìm tỉ số phần trăm của hai số, tìm giá trị phần trăm của một số, giải toán thực tế về lãi suất và giảm giá.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái niệm tỉ số phần trăm và cách tính", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Giải toán về tỉ số phần trăm (3 dạng toán cơ bản)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tỉ số phần trăm (%)",
            "definition": "Là tỉ số giữa hai số được viết dưới dạng phân số có mẫu số là 100 và dùng kí hiệu % thay cho /100.",
            "example": "3/5 = 60/100 = 60%; 0,25 = 25%.",
            "essence": "Tỉ số phần trăm cho biết một bộ phận chiếm bao nhiêu phần nếu toàn thể được chia đều thành 100 phần bằng nhau."
          },
          {
            "term": "Ba dạng toán cơ bản về tỉ số phần trăm",
            "definition": "Dạng 1: Tìm tỉ số phần trăm của a và b (lấy a chia b rồi nhân 100%). Dạng 2: Tìm a% của số B (lấy B nhân a rồi chia 100). Dạng 3: Tìm một số khi biết a% của nó là B (lấy B chia a rồi nhân 100).",
            "example": "Tìm 20% của 80 kg: 80 * 20 : 100 = 16 kg.",
            "essence": "Phân biệt rõ bài toán 'tìm phần trăm của một số' hay 'tìm số khi biết phần trăm'."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc tìm tỉ số phần trăm của hai số a và b",
            "meaning": "Bước 1: Tìm thương của a và b. Bước 2: Nhân thương đó với 100 và viết thêm kí hiệu % vào bên phải kết quả.",
            "example": "Lớp 5A có 40 học sinh, trong đó có 24 học sinh nữ. Tỉ số phần trăm học sinh nữ là: 24 : 40 = 0,6 = 60%.",
            "essence": "Lấy thương số thập phân nhân nhẩm 100 rồi đính kèm kí hiệu %."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một chiếc cặp học sinh có giá niêm yết là 250.000 đồng. Nhân dịp năm học mới, cửa hàng giảm giá 15%. Hỏi người mua phải trả bao nhiêu tiền?",
            "steps": [
              "Bước 1: Tính số tiền được giảm giá: 250.000 * 15 : 100 = 37.500 (đồng).",
              "Bước 2: Tính số tiền thực tế phải trả: 250.000 - 37.500 = 212.500 (đồng).",
              "Bước 3 (Cách 2): Giá sau giảm chiếm: 100% - 15% = 85%. Tiền phải trả: 250.000 * 85 : 100 = 212.500 (đồng)."
            ],
            "answer": "Người mua phải trả 212.500 đồng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên không chia cho 100 khi tính '15% của 250.000', mà lấy luôn 250.000 * 15 ra con số khổng lồ.",
            "why": "Kí hiệu % có nghĩa là chia cho 100 (15% = 15/100 = 0,15)."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Hình học phẳng: Tam giác, Hình thang, Hình tròn",
        "description": "Diện tích hình tam giác, diện tích hình thang, chu vi và diện tích hình tròn, giải bài toán thực tế về đo đạc đất đai.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Diện tích hình tam giác và diện tích hình thang", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Chu vi và diện tích hình tròn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Diện tích hình tam giác",
            "definition": "Diện tích hình tam giác bằng độ dài đáy nhân với chiều cao (cùng đơn vị đo) rồi chia cho 2: S = (a * h) / 2.",
            "example": "Tam giác có đáy a = 8 cm, chiều cao h = 5 cm có diện tích S = (8 * 5) / 2 = 20 cm^2.",
            "essence": "Tam giác bằng một nửa hình chữ nhật hoặc hình bình hành có cùng đáy và chiều cao tương ứng."
          },
          {
            "term": "Chu vi và diện tích hình tròn",
            "definition": "Chu vi C = d * 3,14 = r * 2 * 3,14. Diện tích S = r * r * 3,14 (r là bán kính, d là đường kính).",
            "example": "Hình tròn có bán kính r = 3 cm thì chu vi C = 3 * 2 * 3,14 = 18,84 cm; diện tích S = 3 * 3 * 3,14 = 28,26 cm^2.",
            "essence": "Số 3,14 là giá trị xấp xỉ của số Pi (π), thể hiện tỉ số giữa chu vi và đường kính của mọi hình tròn."
          }
        ],
        "rules": [
          {
            "statement": "Công thức tính diện tích hình thang",
            "meaning": "Diện tích hình thang bằng tổng độ dài hai đáy nhân với chiều cao (cùng đơn vị đo) rồi chia cho 2: S = ((a + b) * h) / 2.",
            "example": "'Muốn tính diện tích hình thang / Đáy lớn đáy bé ta mang cộng vào / Cộng vào nhân với chiều cao / Chia đôi lấy nửa thế nào cũng ra'.",
            "essence": "Ghép hai hình thang bằng nhau sẽ tạo thành một hình bình hành có đáy bằng (đáy lớn + đáy bé)."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một thửa ruộng hình thang có đáy lớn 120 m, đáy bé bằng 2/3 đáy lớn, chiều cao bằng 40 m. Tính diện tích thửa ruộng đó ra mét vuông và héc-ta (ha).",
            "steps": [
              "Bước 1: Tính đáy bé thửa ruộng: 120 * 2/3 = 80 (m).",
              "Bước 2: Tính diện tích hình thang: S = (120 + 80) * 40 / 2 = 200 * 20 = 4.000 (m^2).",
              "Bước 3: Đổi đơn vị sang héc-ta: 1 ha = 10.000 m^2 => 4.000 m^2 = 0,4 ha."
            ],
            "answer": "Diện tích thửa ruộng là 4.000 m^2 (bằng 0,4 ha)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Khi tính diện tích hình tròn lại lấy 'r * 2 * 3,14' thay vì 'r * r * 3,14'.",
            "why": "r * 2 * 3,14 là công thức tính CHU VI, còn DIỆN TÍCH bắt buộc phải là bán kính nhân với bán kính (r * r * 3,14)."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chương 5: Hình học không gian: Hình hộp chữ nhật và Hình lập phương",
        "description": "Đặc điểm hình hộp chữ nhật và hình lập phương, diện tích xung quanh, diện tích toàn phần, thể tích, các đơn vị đo thể tích (cm3, dm3, m3, lít).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Diện tích xung quanh và diện tích toàn phần của hình hộp chữ nhật & hình lập phương", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thể tích và các đơn vị đo thể tích (xăng-ti-mét khối, đề-xi-mét khối, mét khối)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thể tích hình hộp chữ nhật và hình lập phương",
            "definition": "Hình hộp chữ nhật: V = a * b * c (dài nhân rộng nhân cao). Hình lập phương: V = a * a * a (cạnh nhân cạnh nhân cạnh).",
            "example": "Bể cá dài 80 cm, rộng 50 cm, cao 40 cm có thể tích V = 80 * 50 * 40 = 160.000 cm^3 = 160 dm^3 = 160 lít.",
            "essence": "Thể tích đo lượng không gian mà vật thể chiếm chỗ; 1 dm^3 chứa đúng 1 lít nước."
          },
          {
            "term": "Mối liên hệ giữa các đơn vị đo thể tích",
            "definition": "Mỗi đơn vị đo thể tích gấp 1000 lần đơn vị bé hơn liền sau: 1 m^3 = 1000 dm^3 = 1.000.000 cm^3. Đặc biệt: 1 dm^3 = 1 lít.",
            "example": "0,5 m^3 = 500 dm^3 = 500 lít nước.",
            "essence": "Khác với đơn vị diện tích (gấp 100 lần), đơn vị thể tích trong hệ thập phân gấp kém nhau 1000 lần (3 chữ số 0)."
          }
        ],
        "rules": [
          {
            "statement": "Công thức diện tích xung quanh hình hộp chữ nhật",
            "meaning": "Diện tích xung quanh bằng chu vi đáy nhân với chiều cao (cùng một đơn vị đo): Sxq = (a + b) * 2 * c.",
            "example": "Thùng cát tông dài 6 dm, rộng 4 dm, cao 5 dm có Sxq = (6 + 4) * 2 * 5 = 100 dm^2.",
            "essence": "Mở bốn mặt bên của hình hộp chữ nhật ra ta được một hình chữ nhật lớn có chiều dài là chu vi đáy."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một bể nước dạng hình hộp chữ nhật có kích thước bên trong lòng bể: chiều dài 2 m, chiều rộng 1,5 m, chiều cao 1,2 m. Hiện bể đang chứa 60% thể tích nước. Hỏi trong bể có bao nhiêu lít nước?",
            "steps": [
              "Bước 1: Tính thể tích toàn phần của bể: V = 2 * 1,5 * 1,2 = 3,6 (m^3).",
              "Bước 2: Đổi sang đơn vị lít (dm^3): 3,6 m^3 = 3.600 dm^3 = 3.600 lít.",
              "Bước 3: Lượng nước thực tế đang có trong bể: 3.600 * 60 : 100 = 2.160 (lít)."
            ],
            "answer": "Trong bể có 2.160 lít nước."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đổi 1 m^3 = 100 dm^3 thay vì 1000 dm^3.",
            "why": "Vì 1 m = 10 dm nên 1 m^3 = 10 * 10 * 10 = 1000 dm^3."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chương 6: Số đo thời gian và Toán chuyển động đều",
        "description": "Các phép tính với số đo thời gian, vận tốc, quãng đường, thời gian (s = v * t), bài toán hai chuyển động ngược chiều và cùng chiều.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cộng, trừ, nhân, chia số đo thời gian", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Vận tốc, quãng đường, thời gian và bài toán chuyển động đều", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Vận tốc trong chuyển động đều",
            "definition": "Vận tốc là quãng đường đi được trong một đơn vị thời gian: v = s : t (đơn vị thông dụng: km/giờ hoặc m/giây).",
            "example": "Một ô tô đi được quãng đường 120 km trong 2 giờ thì vận tốc của ô tô là v = 120 : 2 = 60 km/giờ.",
            "essence": "Vận tốc cho biết mức độ chuyển động nhanh hay chậm của một vật thể."
          },
          {
            "term": "Chuyển động ngược chiều gặp nhau",
            "definition": "Hai chuyển động khởi hành cùng lúc và đi ngược chiều về phía nhau để gặp nhau: Thời gian gặp nhau = Quãng đường ban đầu chia cho Tổng hai vận tốc: t = s : (v1 + v2).",
            "example": "Hai xe cách nhau 180 km, xe 1 đi 50 km/h, xe 2 đi 40 km/h: thời gian gặp nhau t = 180 : (50 + 40) = 2 giờ.",
            "essence": "Mỗi giờ hai xe cùng tiến gần nhau một khoảng bằng tổng hai vận tốc."
          }
        ],
        "rules": [
          {
            "statement": "Mối quan hệ giữa s, v và t",
            "meaning": "s = v * t (quãng đường = vận tốc * thời gian); v = s : t (vận tốc = quãng đường : thời gian); t = s : v (thời gian = quãng đường : vận tốc).",
            "example": "Một người đi xe đạp với vận tốc 12 km/h trong 2,5 giờ thì đi được: s = 12 * 2,5 = 30 km.",
            "essence": "Phải luôn thống nhất đơn vị đo: nếu vận tốc là km/h thì thời gian phải là GIỜ và quãng đường là KM."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Quãng đường AB dài 150 km. Một ô tô đi từ A đến B với vận tốc 60 km/giờ, cùng lúc đó một xe máy đi từ B về A với vận tốc 40 km/giờ. Hỏi sau bao lâu hai xe gặp nhau và điểm gặp cách A bao nhiêu km?",
            "steps": [
              "Bước 1: Tính tổng vận tốc của hai xe: 60 + 40 = 100 (km/giờ).",
              "Bước 2: Thời gian để hai xe gặp nhau: 150 : 100 = 1,5 (giờ) = 1 giờ 30 phút.",
              "Bước 3: Điểm gặp nhau cách A chính là quãng đường ô tô đã đi: 60 * 1,5 = 90 (km)."
            ],
            "answer": "Hai xe gặp nhau sau 1,5 giờ tại điểm cách A 90 km."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy thời gian 1 giờ 30 phút viết thành 1,3 giờ để nhân với vận tốc.",
            "why": "1 giờ 30 phút = 1 và 30/60 giờ = 1,5 giờ chứ không phải 1,3 giờ."
          }
        ]
      }
    ]
  },
  "tieng-viet": {
    "id": "tieng-viet",
    "name": "Tiếng Việt",
    "icon": "📖",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ điểm 1: Khám phá thế giới kì diệu của từ ngữ",
        "description": "Từ đồng nghĩa, từ trái nghĩa, từ đồng âm, từ nhiều nghĩa, phân biệt nghĩa gốc và nghĩa chuyển của từ.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Từ đồng nghĩa và từ trái nghĩa trong tiếng Việt", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Từ đồng âm và từ nhiều nghĩa (nghĩa gốc & nghĩa chuyển)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Từ nhiều nghĩa",
            "definition": "Là từ có một nghĩa gốc và một hay một số nghĩa chuyển. Các nghĩa của từ nhiều nghĩa luôn có mối liên hệ mật thiết với nhau về mặt ngữ nghĩa.",
            "example": "Từ 'mắt': 'đôi mắt bé tròn xoe' (nghĩa gốc - cơ quan thị giác); 'quả na mở mắt', 'mắt mía', 'mắt lưới' (nghĩa chuyển - hình dáng giống con mắt).",
            "essence": "Nghĩa chuyển được phát triển từ nghĩa gốc thông qua hiện tượng ẩn dụ hoặc hoán dụ."
          },
          {
            "term": "Phân biệt từ nhiều nghĩa và từ đồng âm",
            "definition": "Từ đồng âm là những từ giống nhau về âm đọc nhưng nghĩa hoàn toàn khác nhau, không có mối liên hệ nào. Từ nhiều nghĩa có các nghĩa cùng xuất phát từ một nghĩa gốc chung.",
            "example": "'Con ruồi đậu trên mâm xôi đậu': từ 'đậu' thứ nhất (hành động hạ cánh) và từ 'đậu' thứ hai (loại hạt đỗ) là hai từ đồng âm khác hẳn nhau.",
            "essence": "Mấu chốt là tìm xem giữa các nét nghĩa có 'sợi dây liên kết' nào về hình dạng, tính chất hay chức năng hay không."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc sử dụng từ đồng nghĩa phù hợp ngữ cảnh",
            "meaning": "Các từ đồng nghĩa có thể mang sắc thái biểu cảm khác nhau (thân mật, trang trọng hoặc tiêu cực) nên cần chọn từ chính xác với hoàn cảnh nói và viết.",
            "example": "Hi sinh (trang trọng, cao cả), chết (trung tính), toi mạng (coi thường, phê phán).",
            "essence": "Dùng đúng từ giúp câu văn vừa giàu hình ảnh vừa thể hiện thái độ chuẩn mực."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xác định từ 'chân' trong các câu sau được dùng theo nghĩa gốc hay nghĩa chuyển: a) 'Bé bị đau chân'. b) 'Dưới chân núi có con suối nhỏ'. c) 'Anh ấy có chân trong ban chỉ huy'.",
            "steps": [
              "Bước 1: 'Bé bị đau chân': chân ở đây là bộ phận dưới cùng của cơ thể người để đi đứng => Nghĩa gốc.",
              "Bước 2: 'Dưới chân núi': bộ phận dưới cùng của ngọn núi, nơi tiếp giáp với mặt đất => Nghĩa chuyển (tương đồng vị trí dưới cùng).",
              "Bước 3: 'Có chân trong ban chỉ huy': tư cách thành viên, vị trí trong một tổ chức => Nghĩa chuyển."
            ],
            "answer": "a) Nghĩa gốc; b) Nghĩa chuyển; c) Nghĩa chuyển."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa từ đồng âm và từ nhiều nghĩa (ví dụ coi 'cánh buồm' và 'cánh đồng' là từ đồng âm).",
            "why": "'Cánh buồm' và 'cánh đồng' là từ nhiều nghĩa vì đều gợi hình ảnh bề mặt rộng trải dài."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ điểm 2: Đại từ, Quan hệ từ và Nghệ thuật liên kết câu",
        "description": "Đại từ xưng hô, đại từ thay thế, quan hệ từ và cặp quan hệ từ chỉ nguyên nhân - kết quả, điều kiện - kết quả, tương phản, tăng tiến.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đại từ và cách dùng đại từ xưng hô lịch sự", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Quan hệ từ và các cặp quan hệ từ biểu thị ý nghĩa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quan hệ từ",
            "definition": "Là từ dùng để nối các từ ngữ hoặc các câu với nhau nhằm thể hiện mối quan hệ ngữ pháp giữa chúng (và, với, hay, hoặc, nhưng, mà, thì, của, ở, tại,...).",
            "example": "Trời mưa TO nhưng em VẪN đến trường đúng giờ (thể hiện sự tương phản).",
            "essence": "Quan hệ từ làm cho câu văn mạch lạc, chặt chẽ và thể hiện chính xác tư duy logic của người viết."
          },
          {
            "term": "Các cặp quan hệ từ thông dụng",
            "definition": "Vì... nên... (nguyên nhân - kết quả); Nếu... thì... / Hễ... thì... (điều kiện/giả thiết - kết quả); Tuy... nhưng... / Mặc dù... nhưng... (tương phản, nhượng bộ); Không những... mà còn... (tăng tiến).",
            "example": "Không những Lan học giỏi mà bạn ấy còn hát rất hay.",
            "essence": "Cặp quan hệ từ đóng vai trò như đòn bẩy kết nối hai vế của câu ghép."
          }
        ],
        "rules": [
          {
            "statement": "Tránh lỗi lặp từ bằng phép thay thế đại từ",
            "meaning": "Trong một đoạn văn, để tránh lặp lại cùng một danh từ nhiều lần, ta có thể dùng đại từ (nó, họ, chúng, hắn, người) hoặc từ đồng nghĩa để thay thế.",
            "example": "'Bác Hồ là vị cha già kính yêu của dân tộc. Người đã cống hiến trọn đời mình cho sự nghiệp giải phóng đất nước.'",
            "essence": "Giúp đoạn văn vừa liên kết chặt chẽ vừa tránh cảm giác nhàm chán, vụng về."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Điền cặp quan hệ từ thích hợp vào chỗ trống: '... trời mưa to ... đường sá trơn trượt' và '... bạn Dũng gặp nhiều khó khăn ... bạn ấy vẫn vươn lên học giỏi'.",
            "steps": [
              "Bước 1: Câu 1 có quan hệ nguyên nhân - kết quả: dùng cặp 'Vì... nên...' hoặc 'Do... nên...'.",
              "Bước 2: Câu 2 có quan hệ tương phản, nhượng bộ: dùng cặp 'Tuy... nhưng...' hoặc 'Mặc dù... nhưng...'."
            ],
            "answer": "1) 'Vì trời mưa to nên đường sá trơn trượt.' 2) 'Tuy bạn Dũng gặp nhiều khó khăn nhưng bạn ấy vẫn vươn lên học giỏi.'"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Dùng sai cặp quan hệ từ khập khiễng, cọc cạch: 'Tuy trời mưa nên em vẫn đi học'.",
            "why": "Phải đi theo cặp chuẩn: 'Tuy... nhưng...' chứ không thể ghép 'Tuy' với 'nên'."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ điểm 3: Câu ghép và Cách nối các vế câu ghép",
        "description": "Khái niệm câu ghép, cấu tạo ngữ pháp của câu ghép, cách nối các vế câu ghép bằng từ nối hoặc bằng dấu câu (dấu phẩy, dấu chấm phẩy, dấu hai chấm).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cấu tạo của câu ghép trong tiếng Việt", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Cách nối các vế câu ghép (dùng từ nối hoặc dấu câu)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Câu ghép",
            "definition": "Là câu do nhiều vế câu ghép lại. Mỗi vế câu ghép thường có cấu tạo giống như một câu đơn (có đủ cụm chủ ngữ - vị ngữ) và thể hiện một ý có quan hệ chặt chẽ với ý của những vế câu khác.",
            "example": "'Gió thổi mạnh (Vế 1: C1 - V1) và mây đen ùn ùn kéo đến (Vế 2: C2 - V2)'.",
            "essence": "Câu ghép diễn đạt những ý phức hợp mà câu đơn không thể hiện trọn vẹn được."
          },
          {
            "term": "Hai cách nối các vế câu ghép",
            "definition": "Cách 1: Nối trực tiếp bằng các dấu câu (dấu phẩy, dấu chấm phẩy, dấu hai chấm). Cách 2: Nối bằng từ có tác dụng nối (quan hệ từ hoặc cặp từ hô ứng: càng... càng..., vừa... vừa...).",
            "example": "Nối bằng dấu câu: 'Mặt trời mọc, chim hót ríu rít.' Nối bằng từ: 'Trời càng mưa to, nước sông càng dâng cao.'",
            "essence": "Tùy thuộc vào nhịp điệu và cảm xúc muốn truyền tải để lựa chọn cách nối vế phù hợp."
          }
        ],
        "rules": [
          {
            "statement": "Phân biệt câu ghép với câu đơn có nhiều chủ ngữ hoặc vị ngữ",
            "meaning": "Câu đơn có thể có nhiều C hoặc nhiều V cùng làm một nòng cốt. Câu ghép bắt buộc phải có từ hai cụm C - V riêng biệt không bao hàm nhau.",
            "example": "'Lan và Mai cùng đi học' là câu đơn có 2 chủ ngữ. 'Lan đi học còn Mai ở nhà' là câu ghép gồm 2 vế C-V.",
            "essence": "Vạch ranh giới các cụm Chủ ngữ - Vị ngữ để nhận diện cấu trúc câu chuẩn xác."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xác định chủ ngữ và vị ngữ của từng vế trong câu ghép sau: 'Mùa xuân đã về, muôn hoa đua nhau khoe sắc thắm.'",
            "steps": [
              "Bước 1: Vế 1: 'Mùa xuân đã về'. Chủ ngữ 1 là 'Mùa xuân'; Vị ngữ 1 là 'đã về'.",
              "Bước 2: Vế 2: 'muôn hoa đua nhau khoe sắc thắm'. Chủ ngữ 2 là 'muôn hoa'; Vị ngữ 2 là 'đua nhau khoe sắc thắm'.",
              "Bước 3: Hai vế được nối trực tiếp với nhau bằng dấu phẩy."
            ],
            "answer": "Vế 1: C1 (Mùa xuân) - V1 (đã về); Vế 2: C2 (muôn hoa) - V2 (đua nhau khoe sắc thắm)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm câu đơn có trạng ngữ mở đầu là câu ghép: 'Sáng nay, em đi học sớm'.",
            "why": "'Sáng nay' chỉ là trạng ngữ chỉ thời gian, câu chỉ có 1 cụm C-V duy nhất là 'em đi học sớm' nên vẫn là câu đơn."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ điểm 4: Tập làm văn: Nghệ thuật Miêu tả Cảnh và Người",
        "description": "Cấu tạo bài văn tả cảnh và tả người, quan sát và chọn lọc chi tiết tiêu biểu, sử dụng biện pháp so sánh và nhân hóa trong miêu tả.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Cấu tạo và phương pháp làm bài văn tả cảnh", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Cấu tạo và phương pháp làm bài văn tả người", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bố cục 3 phần của bài văn miêu tả",
            "definition": "1) Mở bài: Giới thiệu bao quát đối tượng miêu tả (cảnh hoặc người). 2) Thân bài: Tả từng phần của cảnh hoặc sự thay đổi theo thời gian; Tả ngoại hình kết hợp tính tình và hoạt động của người. 3) Kết bài: Nêu cảm nghĩ, tình cảm gắn bó với đối tượng.",
            "example": "Tả người mẹ: Mở bài giới thiệu người thân yêu nhất; Thân bài tả dáng người, ánh mắt, bàn tay tảo tần và công việc nấu cơm chăm sóc con; Kết bài lòng biết ơn sâu sắc.",
            "essence": "Miêu tả không phải là liệt kê khô khan mà là vẽ bức tranh sinh động bằng từ ngữ và cảm xúc chân thành."
          },
          {
            "term": "Biện pháp So sánh và Nhân hóa trong miêu tả",
            "definition": "So sánh đối chiếu nét tương đồng (như, tựa như); Nhân hóa gắn hành động, cảm xúc con người cho sự vật vô tri.",
            "example": "'Mặt trời như một quả cầu lửa khổng lồ' (so sánh); 'Những hàng cây ven đường đang thì thầm trò chuyện trong gió' (nhân hóa).",
            "essence": "Làm cho bức tranh phong cảnh và con người trở nên có hồn, chạm tới trái tim người đọc."
          }
        ],
        "rules": [
          {
            "statement": "Trình tự miêu tả cảnh vật hợp lí",
            "meaning": "Có thể tả theo trình tự không gian (từ xa đến gần, từ bao quát đến chi tiết, từ dưới lên trên) hoặc theo trình tự thời gian (từ sáng đến trưa đến tối, hoặc qua các mùa trong năm).",
            "example": "Tả cơn mưa rào: Lúc sắp mưa -> Lúc mưa bắt đầu trút xuống -> Cảnh vật sau khi cơn mưa tạnh.",
            "essence": "Mạch miêu tả phải tự nhiên, mạch lạc, không nhảy cóc lộn xộn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Lập dàn ý vắn tắt cho bài văn tả cảnh một buổi sáng bình minh trên quê hương em.",
            "steps": [
              "Bước 1: Mở bài: Giới thiệu thời gian và địa điểm ngắm bình minh (sáng sớm trên cánh đồng làng).",
              "Bước 2: Thân bài - Bầu trời: nền trời trong xanh, những tia nắng sớm xuyên qua sương mờ; Cây cỏ: giọt sương mai long lanh đọng trên ngọn cỏ; Âm thanh & con người: tiếng gà gáy râm ran, bác nông dân dắt trâu ra đồng, học sinh ríu rít đến trường.",
              "Bước 3: Kết bài: Cảm xúc tự hào, thêm yêu tha thiết vẻ đẹp bình dị, trù phú của quê hương."
            ],
            "answer": "Dàn ý 3 phần chuẩn hóa từ bao quát đến cụ thể và bộc lộ tình cảm sâu sắc."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Tả người nhưng biến thành bản kê khai lí lịch khô khan: tên gì, mấy tuổi, làm nghề gì mà không tả cử chỉ, ánh mắt, nụ cười.",
            "why": "Bài văn tả người cần làm nổi bật nét thần thái riêng biệt thông qua chi tiết ngoại hình và hành động cụ thể."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chủ điểm 5: Ôn tập Đọc hiểu và Kỹ năng viết Chuyển cấp Lớp 6",
        "description": "Kỹ năng trả lời câu hỏi đọc hiểu văn bản, phát hiện biện pháp tu từ, viết đoạn văn thể hiện tình cảm, cảm xúc hoặc ý kiến cá nhân.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Kỹ năng đọc hiểu văn bản truyện và thơ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Kỹ năng viết đoạn văn cảm nghĩ và chuẩn bị thi vào lớp 6", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chủ đề và Thông điệp của văn bản",
            "definition": "Chủ đề là vấn đề đời sống được tác giả đề cập trong tác phẩm. Thông điệp là bài học, lời khuyên hoặc tư tưởng nhân văn sâu sắc mà tác giả muốn gửi gắm tới độc giả.",
            "example": "Bài thơ 'Hạt gạo làng ta' ca ngợi công sức giọt mồ hôi của người nông dân và gửi thông điệp trân quý từng hạt cơm hạt gạo.",
            "essence": "Đọc hiểu sâu sắc là nhìn thấu bài học cuộc sống đằng sau từng con chữ."
          },
          {
            "term": "Đoạn văn nêu cảm nghĩ",
            "definition": "Gồm 3 phần: Câu mở đoạn (giới thiệu sự việc/nhân vật và ấn tượng chung), các câu thân đoạn (nêu các chi tiết khiến mình rung động và lí giải vì sao), câu kết đoạn (khẳng định lại tình cảm hoặc rút ra bài học cho bản thân).",
            "example": "Đoạn văn bày tỏ lòng biết ơn thầy cô giáo nhân ngày 20/11.",
            "essence": "Viết chân thật từ cảm xúc của chính mình, tránh sáo rỗng sao chép văn mẫu."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc trả lời câu hỏi đọc hiểu trọn câu",
            "meaning": "Khi trả lời câu hỏi đọc hiểu, phải trả lời thành câu hoàn chỉnh có đủ Chủ ngữ và Vị ngữ, dẫn chứng trực tiếp từ ngữ liệu trong bài đọc.",
            "example": "Không trả lời cộc lốc 'Màu xanh', mà phải viết: 'Chi tiết thể hiện màu sắc của dòng sông là màu xanh biếc.'",
            "essence": "Tác phong diễn đạt gãy gọn, chuẩn mực trong các bài thi khảo sát năng lực."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Đọc hai câu thơ sau và nêu tác dụng của biện pháp so sánh: 'Trẻ em như búp trên cành / Biết ăn ngủ, biết học hành là ngoan' (Hồ Chí Minh).",
            "steps": [
              "Bước 1: Xác định hình ảnh so sánh: 'Trẻ em' được so sánh với 'búp trên cành'.",
              "Bước 2: Phân tích nét tương đồng: Búp non trên cành tươi non, giàu sức sống, dễ bị tổn thương và cần được chăm sóc; trẻ em cũng thơ ngây, trong trắng, là mầm non tương lai của đất nước.",
              "Bước 3: Nêu tác dụng: Bộc lộ tình yêu thương bao la và sự quan tâm sâu sắc của Bác Hồ đối với thế hệ thiếu nhi."
            ],
            "answer": "Biện pháp so sánh làm nổi bật vẻ đẹp ngây thơ, sức sống non tơ của trẻ em và khẳng định trách nhiệm chăm sóc, bảo bọc của toàn xã hội."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chỉ gọi tên biện pháp so sánh mà không phân tích hình ảnh và tác dụng biểu cảm của nó.",
            "why": "Điểm tối đa của câu hỏi tu từ nằm ở phần phân tích giá trị thẩm mĩ và cảm xúc."
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
        "title": "Unit 1: All About Us & School Life",
        "description": "Vocabulary for personal information and school subjects, present simple for daily routines, adverbs of frequency (always, usually, sometimes, never).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Daily Routines & School Subjects", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Adverbs of Frequency & Pronunciation", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Adverbs of Frequency (Trạng từ chỉ tần suất)",
            "definition": "Words that describe how often an action happens: always (100%), usually (80%), often (60%), sometimes (40%), rarely (10%), never (0%).",
            "example": "I always brush my teeth before going to bed. He never arrives late for school.",
            "essence": "Placed before normal verbs and after the verb 'to be'."
          },
          {
            "term": "Present Simple Tense for Routines",
            "definition": "Subject + Verb(s/es) for singular third-person (He/She/It). Used for facts, habits, and daily timetables.",
            "example": "She walks to school every morning. They play football after class.",
            "essence": "Mastering the 's/es' verb ending is the cornerstone of elementary grammar."
          }
        ],
        "rules": [
          {
            "statement": "Position of Adverbs of Frequency in a sentence",
            "meaning": "S + Adverb + Verb (e.g., I often read books) OR S + to be + Adverb (e.g., She is always cheerful).",
            "example": "He usually does his homework at 7 p.m.",
            "essence": "Do not place adverbs of frequency between a verb and its direct object."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Put the words in the correct order: 'school / goes / Nam / to / always / on / foot.'",
            "steps": [
              "Bước 1: Xác định chủ ngữ: 'Nam'.",
              "Bước 2: Trạng từ chỉ tần suất 'always' đứng trước động từ thường 'goes'.",
              "Bước 3: Cụm chỉ nơi chốn và phương tiện: 'to school on foot'.",
              "Bước 4: Ghép câu hoàn chỉnh: 'Nam always goes to school on foot.'"
            ],
            "answer": "Nam always goes to school on foot."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'She go to school' instead of 'She goes to school'.",
            "why": "With third-person singular subjects (He, She, It), the verb must take -s or -es."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Unit 2: Our Free-Time Activities & Hobbies",
        "description": "Vocabulary for indoor and outdoor hobbies, like / love / enjoy + V-ing, asking questions with 'What do you do in your free time?'.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Leisure Activities & Sports", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Gerunds after Verbs of Liking (Like/Enjoy + V-ing)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Gerund after Verbs of Preference",
            "definition": "Verbs like like, love, enjoy, prefer, hate are followed by a verb ending in -ing (Gerund).",
            "example": "I like drawing cartoons. My brother enjoys playing computer games.",
            "essence": "Turning an action into an activity noun."
          },
          {
            "term": "Question pattern for free-time activities",
            "definition": "'What do you do in your free time?' -> 'I often + verb...'; 'What does he/she do in his/her free time?' -> 'He/She usually + verb(s/es)...'",
            "example": "What do you do in your free time? - I read comic books and ride my bike.",
            "essence": "Standard question in speaking interviews and entrance exams."
          }
        ],
        "rules": [
          {
            "statement": "Spelling rules for adding -ing",
            "meaning": "Drop final 'e' before adding -ing (make -> making). Double final consonant if preceded by a single vowel (swim -> swimming).",
            "example": "ride -> riding; skate -> skating; run -> running.",
            "essence": "Pay close attention to double consonants to avoid spelling deductions."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Write a sentence using the given words: 'Linda / enjoy / read / folk tales / evening.'",
            "steps": [
              "Bước 1: Chủ ngữ 'Linda' là ngôi thứ ba số ít => 'enjoys'.",
              "Bước 2: Sau enjoy động từ 'read' thêm -ing => 'reading'.",
              "Bước 3: Cụm từ thời gian: 'in the evening'.",
              "Bước 4: Câu hoàn chỉnh: 'Linda enjoys reading folk tales in the evening.'"
            ],
            "answer": "Linda enjoys reading folk tales in the evening."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'I like play chess' instead of 'I like playing chess'.",
            "why": "After 'like', the verb must be in V-ing form: 'playing'."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Unit 3: Future Jobs & Dream Careers",
        "description": "Vocabulary for occupations (pilot, architect, writer, doctor), 'What would you like to be in the future?' and 'Because I'd like to...'.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Jobs & Workplaces", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Expressing Future Wishes (Would like to be / do)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "'Would like to be' Structure",
            "definition": "Used to express polite wishes and future dreams: S + would like to be + a/an + job. Why? Because I'd like to + verb...",
            "example": "'What would you like to be in the future?' - 'I'd like to be an astronaut because I want to explore space.'",
            "essence": "Polite conditional form used instead of simple 'want'."
          },
          {
            "term": "Indefinite Articles A vs An with Jobs",
            "definition": "Use 'an' before vowel sounds (a, e, i, o, u): an architect, an engineer, an artist. Use 'a' before consonant sounds: a doctor, a pilot, a teacher.",
            "example": "He wants to be an architect. She wants to be a nurse.",
            "essence": "Based on pronunciation sound rather than written spelling."
          }
        ],
        "rules": [
          {
            "statement": "Answering reasons with 'Because I would like to...'",
            "meaning": "Always link the dream job to its meaningful activity: doctor -> look after patients; teacher -> teach children; writer -> write stories.",
            "example": "Why would you like to be a pilot? - Because I'd like to fly planes.",
            "essence": "Demonstrates logical coherence in English speaking."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Answer the question: 'Why would you like to be an English teacher?'",
            "steps": [
              "Bước 1: Bắt đầu câu trả lời bằng 'Because I'd like to...'.",
              "Bước 2: Nêu hành động tương ứng với nghề giáo viên: 'teach English to young children' hoặc 'help students learn foreign languages'.",
              "Bước 3: Viết câu hoàn chỉnh: 'Because I'd like to teach English to children in my hometown.'"
            ],
            "answer": "Because I'd like to teach English to children in my hometown."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'I would like to be architect' (omitting 'an').",
            "why": "Singular countable job nouns must always have 'a' or 'an' before them: 'an architect'."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Unit 4: Stories, Legends & Moral Lessons",
        "description": "Vocabulary for fairy tales (The Fox and the Crow, Mai An Tiem, Tam Cam), past simple regular and irregular verbs (was/were, went, saw, had).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Characters and Plots in Fairy Tales", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Past Simple Tense in Storytelling", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Past Simple Tense (Quá khứ đơn)",
            "definition": "Used to describe completed actions in the past. Regular verbs add -ed (played, lived); irregular verbs change form (go -> went, see -> saw, have -> had).",
            "example": "Yesterday, Mai read the story of Mai An Tiem. He was very brave and hardworking.",
            "essence": "Key tense for narrating stories, folktales, and personal memories."
          },
          {
            "term": "Character Traits Adjectives",
            "definition": "Describing personality in stories: clever (thông minh), greedy (tham lam), kind (tốt bụng), hard-working (chăm chỉ), gentle (dịu dàng).",
            "example": "What is Mai An Tiem like? - He is hard-working and clever.",
            "essence": "Essential vocabulary for reading comprehension questions."
          }
        ],
        "rules": [
          {
            "statement": "Structure of question 'What is he/she like?'",
            "meaning": "Asks about personality and character traits, NOT physical looks. (Contrast with 'What does he look like?' for appearance).",
            "example": "'What is the fox like?' - 'It is clever and greedy.'",
            "essence": "Avoid confusing personality with appearance."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Change the verbs into past tense to complete the sentence: 'Last Sunday, Phong (visit) ... his grandparents and (eat) ... delicious watermelons.'",
            "steps": [
              "Bước 1: Động từ 'visit' là động từ có quy tắc => thêm -ed thành 'visited'.",
              "Bước 2: Động từ 'eat' là động từ bất quy tắc => chuyển thành 'ate'.",
              "Bước 3: Viết lại: 'Last Sunday, Phong visited his grandparents and ate delicious watermelons.'"
            ],
            "answer": "visited / ate"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Adding -ed to irregular verbs like 'eated' or 'goed'.",
            "why": "Irregular verbs have special past forms: eat -> ate; go -> went; see -> saw; buy -> bought."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Unit 5: Famous Places of Interest & Travel",
        "description": "Vocabulary for famous landmarks (Ha Long Bay, Hoi An Ancient Town, Trang An, Ben Thanh Market), comparative adjectives (-er, more).",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Landmarks and Natural Wonders of Viet Nam", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Comparative Adjectives (Short & Long Adjectives)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Comparative with Short Adjectives",
            "definition": "Short adjectives (one syllable): Adjective + -er + than. Used to compare two people, places, or things.",
            "example": "Da Nang is cleaner than this crowded street. Fansipan is higher than Ba Den mountain.",
            "essence": "Changes spelling if ending in -y: noisy -> noisier; big -> bigger."
          },
          {
            "term": "Comparative with Long Adjectives",
            "definition": "Long adjectives (two or more syllables): More + Adjective + than.",
            "example": "Ha Long Bay is more beautiful than I expected. Hoi An is more historic than this new town.",
            "essence": "The adjective itself remains in base form."
          }
        ],
        "rules": [
          {
            "statement": "Irregular Comparatives: Good and Bad",
            "meaning": "Good -> better (tốt hơn); Bad -> worse (tồi hơn, kém hơn). Far -> farther / further.",
            "example": "Life in the countryside is better for health than life in the noisy city.",
            "essence": "Do not write 'gooder' or 'more good'."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Complete the sentence with comparative form: 'Phu Quoc Island is (peaceful) ... than Ho Chi Minh City.'",
            "steps": [
              "Bước 1: 'Peaceful' là tính từ dài có 2 âm tiết.",
              "Bước 2: Cấu trúc so sánh hơn của tính từ dài: more + adj + than.",
              "Bước 3: Điền vào: 'more peaceful'."
            ],
            "answer": "Phu Quoc Island is more peaceful than Ho Chi Minh City."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using both 'more' and '-er' together: 'more bigger' or 'more cleaner'.",
            "why": "Use either '-er' (short adj) or 'more' (long adj), never combine both: 'bigger', 'cleaner'."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Unit 6: Weather Forecasts, Seasons & Directions",
        "description": "Vocabulary for seasons (spring, summer, autumn, winter) and weather (sunny, rainy, foggy, snowy), 'What will the weather be like tomorrow?' with 'It will be...'.",
        "lessons": [
          { "id": "l01", "title": "Lesson 1: Four Seasons & Weather Conditions", "hasRealContent": true },
          { "id": "l02", "title": "Lesson 2: Future Simple with 'Will' for Weather Predictions", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Future Predictions with 'Will'",
            "definition": "Subject + will + Verb (bare infinitive). Used to predict future events, especially weather forecasts.",
            "example": "'What will the weather be like tomorrow?' - 'It will be cold and stormy.'",
            "essence": "Simple future modal verb expressing expectations about tomorrow."
          },
          {
            "term": "Transforming Nouns into Weather Adjectives",
            "definition": "Add -y to weather nouns: sun -> sunny; rain -> rainy; wind -> windy; cloud -> cloudy; fog -> foggy.",
            "example": "There is a lot of rain today -> Today is a rainy day.",
            "essence": "Notice the double consonant: sun -> sunny; fog -> foggy."
          }
        ],
        "rules": [
          {
            "statement": "Answering 'What is your favourite season?'",
            "meaning": "S + like / love + season + because it is + weather adjective.",
            "example": "I like autumn because it is cool and windy.",
            "essence": "Always give a sensory reason explaining your weather preference."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Reorder the words to make a sentence: 'will / in / like / What / Hanoi / be / the / tomorrow / weather / ?'",
            "steps": [
              "Bước 1: Từ để hỏi: 'What'.",
              "Bước 2: Trợ động từ tương lai: 'will'.",
              "Bước 3: Cụm chủ ngữ: 'the weather in Hanoi'.",
              "Bước 4: Động từ và từ nối: 'be like tomorrow?'.",
              "Bước 5: Ghép lại: 'What will the weather be like in Hanoi tomorrow?'"
            ],
            "answer": "What will the weather be like in Hanoi tomorrow?"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Writing 'It will is cold' instead of 'It will be cold'.",
            "why": "After 'will', the verb must be in base form (bare infinitive): 'be'."
          }
        ]
      }
    ]
  },
  "khoa-hoc": {
    "id": "khoa-hoc",
    "name": "Khoa học",
    "icon": "🔬",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Chất và sự biến đổi hóa học",
        "description": "Đặc điểm của chất rắn, lỏng, khí; sự biến đổi lí học và sự biến đổi hóa học; hỗn hợp và dung dịch; an toàn khi dùng hóa chất.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Ba thể của chất và hỗn hợp, dung dịch", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sự biến đổi lí học và sự biến đổi hóa học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Sự biến đổi hóa học",
            "definition": "Là sự biến đổi từ chất này thành chất khác có tính chất hoàn toàn mới, thường đi kèm với các dấu hiệu: tỏa nhiệt, phát sáng, đổi màu, có mùi hoặc sinh ra chất khí, chất kết tủa.",
            "example": "Đốt cháy que diêm tạo thành than đen và khói; đinh sắt để ngoài không khí ẩm bị gỉ sét.",
            "essence": "Khác với biến đổi lí học (chỉ thay đổi hình dạng, thể), biến đổi hóa học làm thay đổi hoàn toàn bản chất chất ban đầu."
          },
          {
            "term": "Hỗn hợp và Dung dịch",
            "definition": "Hỗn hợp gồm hai hay nhiều chất trộn lẫn nhưng không hòa tan vào nhau (nước và dầu ăn, cát và nước). Dung dịch là hỗn hợp đồng nhất giữa chất tan và dung môi (nước đường, nước muối).",
            "example": "Hòa tan đường vào nước ấm khuấy đều ta được dung dịch nước đường trong suốt đồng nhất.",
            "essence": "Trong dung dịch, chất tan phân tán đều tới từng phân tử trong dung môi."
          }
        ],
        "rules": [
          {
            "statement": "Dấu hiệu nhận biết biến đổi hóa học",
            "meaning": "Nếu có chất mới xuất hiện (đổi màu, sinh khí, tạo kết tủa, cháy thành tro) thì đó là biến đổi hóa học. Nếu chất chỉ nóng chảy, đông đặc hoặc xé nhỏ thì chỉ là biến đổi lí học.",
            "example": "Nước đá tan thành nước lỏng là biến đổi lí học; đường đun nóng cháy thành than đen là biến đổi hóa học.",
            "essence": "Cốt lõi là có sinh ra chất mới hay không."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Hiện tượng nào sau đây là sự biến đổi hóa học? A. Thủy tinh bị vỡ vụn. B. Xi măng trộn với cát và nước đông cứng lại. C. Nước trong nồi sôi bốc hơi. D. Xé tờ giấy thành nhiều mảnh nhỏ.",
            "steps": [
              "Bước 1: Phân tích A, C, D: Thủy tinh vỡ, nước bốc hơi, giấy xé nhỏ chỉ thay đổi hình dạng hoặc thể, không sinh ra chất mới => Biến đổi lí học.",
              "Bước 2: Phân tích B: Xi măng phản ứng với nước và cát tạo thành khối bê tông kết tinh chất mới rắn chắc => Biến đổi hóa học."
            ],
            "answer": "Đáp án B là sự biến đổi hóa học."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng nước sôi bốc hơi là biến đổi hóa học vì thấy có khói bốc lên.",
            "why": "Khói hơi nước đó thực chất vẫn là nước ($H_2O$) ở thể khí, không tạo ra chất mới nào."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Năng lượng và Sử dụng năng lượng tiết kiệm",
        "description": "Năng lượng mặt trời, năng lượng gió, năng lượng nước chảy; điện năng và cách sử dụng điện an toàn, tiết kiệm năng lượng hóa thạch.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Năng lượng mặt trời, gió và nước chảy", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sử dụng năng lượng điện an toàn và tiết kiệm", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Năng lượng tái tạo (Năng lượng sạch)",
            "definition": "Là nguồn năng lượng tự nhiên vô tận, có thể tự phục hồi và không phát thải khí nhà kính gây ô nhiễm môi trường: năng lượng mặt trời, năng lượng gió, năng lượng sóng biển và thủy điện.",
            "example": "Pin năng lượng mặt trời lắp trên mái nhà cung cấp điện chiếu sáng cho gia đình.",
            "essence": "Thay thế dần năng lượng hóa thạch (than đá, dầu mỏ) để chống biến đổi khí hậu."
          },
          {
            "term": "Tiết kiệm điện năng trong gia đình",
            "definition": "Tắt các thiết bị điện khi không sử dụng, tận dụng tối đa ánh sáng tự nhiên, sử dụng bóng đèn LED và các thiết bị tiết kiệm năng lượng Inverter.",
            "example": "Tắt điều hòa và quạt khi rời khỏi phòng học; rút phích cắm sạc điện thoại khi đã đầy pin.",
            "essence": "Tiết kiệm điện vừa giảm chi phí cho gia đình vừa góp phần bảo vệ tài nguyên quốc gia."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc an toàn khi sử dụng điện",
            "meaning": "Không chạm tay ướt vào công tắc hoặc phích cắm điện; không chọc vật kim loại vào ổ cắm; không chơi thả diều gần đường dây điện cao thế.",
            "example": "Khi tay ướt, nước là chất dẫn điện tốt sẽ gây nguy cơ bị điện giật chết người.",
            "essence": "Nước và cơ thể người đều dẫn điện rất mạnh."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Kể tên 3 hành động cụ thể học sinh lớp 5 có thể làm ngay để tiết kiệm năng lượng điện tại trường học và ở nhà.",
            "steps": [
              "Bước 1: Tắt đèn và quạt điện trong lớp học trước khi ra sân tập thể dục hoặc khi ra về.",
              "Bước 2: Mở cửa sổ đón ánh sáng mặt trời và gió mát tự nhiên thay vì bật đèn và điều hòa liên tục.",
              "Bước 3: Nhắc nhở người thân tắt tivi khi không có người xem và đóng kín cửa tủ lạnh ngay sau khi lấy đồ."
            ],
            "answer": "3 hành động thiết thực: tắt thiết bị khi không dùng, tận dụng gió/nắng tự nhiên, tuyên truyền người thân."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng để điều hòa ở 16 độ C sẽ làm mát phòng nhanh hơn mà không tốn thêm điện.",
            "why": "Để nhiệt độ quá thấp làm máy nén hoạt động quá tải, tiêu tốn gấp đôi lượng điện và dễ gây sốc nhiệt cho cơ thể."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Thực vật và Động vật: Sự sinh sản và Phát triển",
        "description": "Sự sinh sản của thực vật có hoa (hoa đực, hoa cái, nhị, nhụy, thụ phấn, thụ tinh); sự sinh sản của động vật (đẻ trứng, đẻ con, chu trình sống của ếch và bướm).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sự sinh sản và phát triển của thực vật có hoa", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sự sinh sản của động vật và vòng đời sinh học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Sự thụ phấn và thụ tinh ở thực vật có hoa",
            "definition": "Thụ phấn là hiện tượng hạt phấn từ đầu nhị rơi vào đầu nhụy. Thụ tinh là hiện tượng tế bào sinh dục đực trong hạt phấn kết hợp với tế bào sinh dục cái trong noãn tạo thành hợp tử, hợp tử phát triển thành phôi.",
            "example": "Hoa thụ phấn nhờ côn trùng (ong, bướm) thường có màu sắc sặc sỡ và hương thơm ngào ngạt; hoa thụ phấn nhờ gió thường có hạt phấn nhỏ, nhẹ.",
            "essence": "Sau khi thụ tinh, noãn phát triển thành hạt chứa phôi, bầu nhụy phát triển thành quả."
          },
          {
            "term": "Vòng đời biến thái hoàn toàn của bướm",
            "definition": "Trứng -> Sâu bướm (ấu trùng) -> Nhộng -> Bướm trưởng thành.",
            "example": "Giai đoạn sâu bướm ăn lá cây phá hoại mùa màng nặng nề nhất; khi thành bướm lại giúp cây thụ phấn.",
            "essence": "Mỗi giai đoạn trong vòng đời có hình thái và vai trò sinh thái hoàn toàn khác nhau."
          }
        ],
        "rules": [
          {
            "statement": "Phân biệt hoa đơn tính và hoa lưỡng tính",
            "meaning": "Hoa có cả nhị và nhụy trên cùng một bông là hoa lưỡng tính (hoa bưởi, hoa dâm bụt). Hoa chỉ có nhị (hoa đực) hoặc chỉ có nhụy (hoa cái) là hoa đơn tính (hoa mướp, hoa bí, hoa ngô).",
            "example": "Cây mướp có hoa đực rụng đi sau khi thụ phấn, hoa cái có bầu nhụy sẽ lớn lên thành quả mướp.",
            "essence": "Chỉ những hoa cái hoặc hoa lưỡng tính đã thụ phấn mới có khả năng kết quả."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày các giai đoạn trong vòng đời phát triển của con ếch.",
            "steps": [
              "Bước 1: Ếch trưởng thành đẻ trứng thành chùm nổi dưới nước.",
              "Bước 2: Trứng nở thành nòng nọc (bơi bằng đuôi, thở bằng mang dưới nước giống như cá).",
              "Bước 3: Nòng nọc mọc hai chân sau, rồi mọc hai chân trước, đuôi ngắn dần.",
              "Bước 4: Đuôi tiêu biến hoàn toàn, phổi hình thành, biến đổi thành ếch con nhảy lên cạn sinh sống."
            ],
            "answer": "Vòng đời của ếch gồm 4 giai đoạn: Trứng -> Nòng nọc -> Nòng nọc có chân -> Ếch trưởng thành."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng hoa đực cũng có thể nở ra quả mướp nếu được bón nhiều phân.",
            "why": "Hoa đực chỉ có nhị sinh hạt phấn, không có noãn và bầu nhụy nên không thể phát triển thành quả."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Con người và Sức khỏe: Tuổi dậy thì và Phòng tránh bệnh",
        "description": "Đặc điểm cơ thể ở tuổi dậy thì, vệ sinh cá nhân, chăm sóc sức khỏe tinh thần, phòng tránh các bệnh truyền nhiễm (sốt xuất huyết, cúm) và phòng tránh bị xâm hại.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sự thay đổi thể chất và tâm lí ở tuổi dậy thì", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phòng tránh tai nạn thương tích và quy tắc tự bảo vệ bản thân", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tuổi dậy thì",
            "definition": "Là giai đoạn chuyển tiếp từ trẻ con thành người lớn (bé gái khoảng 10-15 tuổi, bé trai khoảng 13-17 tuổi). Cơ thể phát triển nhảy vọt về chiều cao, cân nặng, xuất hiện các đặc điểm sinh dục phụ và có nhiều biến đổi về cảm xúc.",
            "example": "Bé gái ngực phát triển, bắt đầu có kinh nguyệt; bé trai vỡ giọng (giọng trầm hơn), mọc ria mép, xuất hiện mụn trứng cá.",
            "essence": "Là sự phát triển sinh lí hoàn toàn bình thường và kì diệu của con người."
          },
          {
            "term": "Quy tắc 5 ngón tay phòng chống xâm hại",
            "definition": "1) Ngón cái: Ôm hôn người thân ruột thịt (bố mẹ, ông bà). 2) Ngón trỏ: Nắm tay bạn bè, thầy cô. 3) Ngón giữa: Bắt tay người quen. 4) Ngón áp út: Vẫy tay người mới gặp. 5) Ngón út: Xua tay, hét to và bỏ chạy nếu người lạ có hành vi đụng chạm vào vùng nhạy cảm đồ bơi.",
            "example": "Vùng đồ bơi là vùng riêng tư bất khả xâm phạm của mỗi người.",
            "essence": "Trang bị kĩ năng tự bảo vệ thân thể và dũng cảm nói 'KHÔNG'."
          }
        ],
        "rules": [
          {
            "statement": "Biện pháp phòng bệnh sốt xuất huyết hiệu quả nhất",
            "meaning": "Diệt lăng quăng/bọ gậy bằng cách đậy kín nắp lu bể chứa nước, thả cá nhỏ ăn bọ gậy, dọn sạch chai lọ đọng nước quanh nhà và ngủ màn kể cả ban ngày.",
            "example": "Muỗi vằn là vật trung gian truyền virus sốt xuất huyết, thường đốt người vào sáng sớm và chiều tối.",
            "essence": "'Không có lăng quăng, bọ gậy - Không có sốt xuất huyết'."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Khi một người lạ rủ em vào chỗ vắng cho bánh kẹo hoặc đồ chơi đắt tiền, em cần làm gì?",
            "steps": [
              "Bước 1: Kiên quyết từ chối quà tặng và giữ khoảng cách an toàn (trên 2 mét).",
              "Bước 2: Nhanh chóng di chuyển về phía nơi đông người (bảo vệ, thầy cô, người dân gần đó).",
              "Bước 3: Nếu người lạ cố tình lôi kéo, hét thật to: 'Cứu tôi với, tôi không quen người này!' để nhờ trợ giúp.",
              "Bước 4: Kể lại ngay toàn bộ sự việc cho cha mẹ hoặc thầy cô giáo."
            ],
            "answer": "Từ chối quà, giữ khoảng cách, hét to tìm sự trợ giúp từ người xung quanh và báo ngay cho người lớn."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Giấu giếm cha mẹ khi cơ thể có những biến đổi ở tuổi dậy thì vì cảm thấy xấu hổ.",
            "why": "Cần cởi mở chia sẻ với cha mẹ hoặc cô giáo y tế để được hướng dẫn vệ sinh cơ thể đúng cách và khoa học."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chủ đề 5: Môi trường và Bảo vệ Tài nguyên thiên nhiên",
        "description": "Các thành phần của môi trường, tài nguyên thiên nhiên, tác động tiêu cực của con người (ô nhiễm rác thải nhựa, phá rừng) và các biện pháp phát triển bền vững.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Môi trường và tài nguyên thiên nhiên quanh em", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hành động bảo vệ môi trường và giảm thiểu rác thải nhựa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Ô nhiễm trắng (Rác thải nhựa)",
            "definition": "Là tình trạng môi trường bị ô nhiễm nghiêm trọng do lượng lớn túi ni-lông và đồ nhựa dùng một lần thải ra không thể phân hủy tự nhiên (mất từ 400 đến 1000 năm mới phân rã thành vi nhựa).",
            "example": "Chai nhựa vứt ra sông ngòi trôi ra biển khiến sinh vật biển nuốt phải dẫn đến tắc nghẽn đường ruột và tử vong.",
            "essence": "Mỗi chiếc túi ni-lông dùng trong 5 phút nhưng gây hại cho Trái Đất suốt hàng thế kỉ."
          },
          {
            "term": "Mô hình 3R bảo vệ môi trường",
            "definition": "1) Reduce (Giảm thiểu tiêu dùng lãng phí). 2) Reuse (Tái sử dụng túi xách, chai lọ). 3) Recycle (Tái chế phế liệu thành sản phẩm mới có ích).",
            "example": "Dùng bình nước cá nhân đi học thay vì ngày nào cũng mua chai nước ngọt nhựa dùng một lần.",
            "essence": "Lối sống xanh bắt đầu từ những thói quen tiêu dùng thông minh hàng ngày."
          }
        ],
        "rules": [
          {
            "statement": "Ý nghĩa sống còn của việc trồng cây gây rừng",
            "meaning": "Rừng là lá phổi xanh hấp thụ khí $CO_2$ và thải ra khí $O_2$, rễ cây giữ đất chống sạt lở xói mòn, tán lá cản dòng chảy giảm thiểu lũ quét mùa mưa bão.",
            "example": "Trồng rừng ngập mặn chắn sóng ven biển ở Cần Giờ, Cà Mau.",
            "essence": "Bảo vệ rừng chính là bảo vệ mái nhà chung của loài người."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân biệt rác thải hữu cơ và rác thải tái chế trong gia đình.",
            "steps": [
              "Bước 1: Rác hữu cơ: Vỏ trái cây, rau thừa, cơm nguội, lá cây dễ phân hủy tự nhiên => Ủ làm phân bón hữu cơ cho cây.",
              "Bước 2: Rác tái chế: Vỏ lon bia nhôm, giấy báo cũ, bìa các-tông, vỏ chai nhựa sạch => Thu gom bán cho nhà máy tái chế.",
              "Bước 3: Phân loại rác tại nguồn giúp giảm 70% lượng rác phải chôn lấp."
            ],
            "answer": "Rác hữu cơ dễ phân hủy dùng làm phân bón; rác tái chế có thể làm nguyên liệu sản xuất sản phẩm mới."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Bỏ chung pin cũ hỏng vào thùng rác sinh hoạt gia đình rồi đốt.",
            "why": "Pin chứa kim loại nặng cực độc (chì, thủy ngân); đốt pin phát tán khí độc vào không khí, vứt ra đất làm nhiễm độc nguồn nước ngầm."
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
        "title": "Chủ đề 1: Đất nước và Con người Việt Nam",
        "description": "Vị trí địa lí, hình dạng lãnh thổ Việt Nam, các vùng địa hình, khí hậu nhiệt đới gió mùa, sông ngòi và biển đảo quê hương.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vị trí địa lí và lãnh thổ Việt Nam", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Địa hình, khí hậu và mạng lưới sông ngòi nước ta", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Vị trí địa lí nước ta",
            "definition": "Nước ta nằm trên bán đảo Đông Dương, thuộc khu vực Đông Nam Á; phần đất liền có hình chữ S cong lượn, phía đông giáp Biển Đông rộng lớn với hơn 3.260 km bờ biển.",
            "example": "Việt Nam tiếp giáp với Trung Quốc ở phía bắc, Lào và Cam-pu-chia ở phía tây; vùng biển có hàng ngàn đảo lớn nhỏ, nổi bật là hai quần đảo Hoàng Sa và Trường Sa.",
            "essence": "Là cầu nối giao thương hàng hải quốc tế chiến lược giữa các châu lục."
          },
          {
            "term": "Khí hậu nhiệt đới gió mùa",
            "definition": "Nhiệt độ trung bình năm cao trên 20°C, lượng mưa và độ ẩm lớn, có hai mùa gió chính: gió mùa mùa đông (lạnh và khô ở miền Bắc) và gió mùa mùa hạ (nóng ẩm, mưa nhiều).",
            "example": "Miền Bắc có 4 mùa rõ rệt (xuân, hạ, thu, đông); miền Nam có 2 mùa (mùa mưa và mùa khô).",
            "essence": "Thuận lợi để cây cối tốt tươi quanh năm, thâm canh lúa nước và cây ăn trái nhiệt đới."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm mạng lưới sông ngòi Việt Nam",
            "meaning": "Nước ta có mạng lưới sông ngòi dày đặc (hơn 2.360 con sông), lượng nước thay đổi theo mùa: mùa lũ trùng mùa mưa, mùa cạn trùng mùa khô. Sông bồi đắp phù sa màu mỡ tạo nên Đồng bằng sông Hồng và Đồng bằng sông Cửu Long.",
            "example": "Sông Hồng và sông Mê Kông (sông Cửu Long) là hai con sông lớn nhất bồi đắp hai vựa lúa của cả nước.",
            "essence": "Phù sa sông là món quà quý giá thiên nhiên ban tặng cho nền văn minh lúa nước ngàn đời."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao bờ biển dài 3.260 km và vùng biển rộng lớn là một lợi thế kinh tế to lớn của nước ta?",
            "steps": [
              "Bước 1: Nguồn lợi thủy hải sản: ngư trường rộng lớn cho phép đánh bắt tôm, cá, mực và nuôi trồng thủy sản ven bờ.",
              "Bước 2: Giao thông vận tải biển: thuận lợi xây dựng các cảng nước sâu (Hải Phòng, Đà Nẵng, Cái Mép) để xuất nhập khẩu hàng hóa với thế giới.",
              "Bước 3: Du lịch biển: nhiều bãi biển đẹp nổi tiếng thế giới (Nha Trang, Phú Quốc, Đà Nẵng, Vịnh Hạ Long).",
              "Bước 4: Khoáng sản biển: khai thác dầu khí ở thềm lục địa phía nam và nghề làm muối ven biển."
            ],
            "answer": "Biển nước ta tạo điều kiện phát triển tổng hợp 4 ngành: thủy sản, cảng biển hàng hải, du lịch và khoáng sản dầu khí."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng toàn bộ đất nước Việt Nam đều có mùa đông lạnh buốt có tuyết rơi.",
            "why": "Chỉ có miền Bắc và vùng núi cao (Sa Pa, Mẫu Sơn) mới có rét buốt mùa đông; từ đèo Hải Vân trở vào Nam thời tiết nắng ấm quanh năm."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Lịch sử dựng nước và giữ nước thời Cổ - Trung đại",
        "description": "Nhà nước Văn Lang - Âu Lạc, Khởi nghĩa Hai Bà Trưng, Chiến thắng Bạch Đằng năm 938, Triều đại nhà Lý - Trần và Ba lần kháng chiến chống quân Nguyên Mông.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Buổi đầu dựng nước: Nhà nước Văn Lang, Âu Lạc và Chiến thắng Bạch Đằng năm 938", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Nước Đại Việt thời Lý - Trần và Ba lần đánh tan quân Nguyên Mông", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chiến thắng Bạch Đằng năm 938 của Ngô Quyền",
            "definition": "Ngô Quyền dùng kế cắm cọc gỗ vạt nhọn bịt sắt dưới lòng sông Bạch Đằng, lợi dụng thủy triều lên nhử địch vào bãi cọc rồi phản công khi thủy triều rút, tiêu diệt hoàn toàn quân Nam Hán, chém chết tướng giặc Lưu Hoằng Tháo.",
            "example": "Chiến thắng chấm dứt hơn 1000 năm Bắc thuộc, mở ra thời kì độc lập tự chủ lâu dài cho dân tộc ta.",
            "essence": "Nghệ thuật quân sự tài tình kết hợp địa hình sông nước hiểm trở với lòng dũng cảm của nhân dân."
          },
          {
            "term": "Hào khí Đông A thời nhà Trần",
            "definition": "Ý chí đại đoàn kết toàn dân tộc 'Vua tôi đồng lòng, anh em hòa mục, cả nước góp sức' dưới sự lãnh đạo của Trần Hưng Đạo, ba lần đánh bại đội quân xâm lược Nguyên Mông hung hãn nhất thế giới thế kỉ XIII.",
            "example": "Hội nghị Diên Hồng vang dội tiếng hô 'ĐÁNH!' của các bô lão; Trần Quốc Toản bóp nát quả cam vì hận không được dự bàn việc nước.",
            "essence": "'Khoan thư sức dân để làm kế sâu rễ bền gốc, đó là thượng sách giữ nước'."
          }
        ],
        "rules": [
          {
            "statement": "Ý nghĩa lịch sử của việc dời đô về Thăng Long năm 1010",
            "meaning": "Vua Lý Thái Tổ ban Chiếu dời đô chuyển kinh đô từ Hoa Lư chật hẹp về thành Đại La (Thăng Long - Hà Nội ngày nay), nơi trung tâm bờ cõi, đất rộng mà bằng phẳng, dân cư trù phú ấm no.",
            "example": "Mở ra thời kì thịnh vượng rực rỡ của kinh đô Thăng Long nghìn năm văn hiến.",
            "essence": "Tầm nhìn chiến lược vượt thời đại của vị vua sáng lập triều Lý."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao quân dân nhà Trần có thể ba lần liên tiếp đánh thắng đạo quân Nguyên Mông hùng mạnh bậc nhất thế giới thời bấy giờ?",
            "steps": [
              "Bước 1: Tinh thần đoàn kết toàn dân: từ vua tôi, tướng sĩ đến nhân dân trăm họ đều một lòng yêu nước nồng nàn (Hội nghị Diên Hồng, Hội nghị Bình Than).",
              "Bước 2: Tài thao lược xuất chúng của các tướng lĩnh: tiêu biểu là Hưng Đạo Đại Vương Trần Quốc Tuấn với chiến lược 'Vườn không nhà trống' triệt đường tiếp tế của giặc.",
              "Bước 3: Tinh thần quyết chiến quyết thắng: binh sĩ khắc vào tay hai chữ 'Sát Thát' thề chết bảo vệ giang sơn."
            ],
            "answer": "Thắng lợi nhờ sức mạnh đại đoàn kết toàn dân, chiến thuật vườn không nhà trống và tài chỉ huy thiên tài của Trần Hưng Đạo."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa chiến thắng Bạch Đằng của Ngô Quyền (năm 938 chống quân Nam Hán) với chiến thắng Bạch Đằng của Trần Hưng Đạo (năm 1288 chống quân Nguyên Mông).",
            "why": "Hai trận đánh diễn ra trên cùng một dòng sông Bạch Đằng nhưng cách nhau tới 350 năm trong hai thời kì lịch sử khác nhau."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Lịch sử Việt Nam thời Cận - Hiện đại: Bác Hồ và Các cuộc Kháng chiến",
        "description": "Nguyễn Ái Quốc ra đi tìm đường cứu nước năm 1911, Đảng Cộng sản Việt Nam ra đời, Cách mạng tháng Tám năm 1945, Chiến thắng Điện Biên Phủ năm 1954, Đại thắng mùa Xuân 1975.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Bác Hồ tìm đường cứu nước và Cách mạng tháng Tám năm 1945", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Chiến thắng lịch sử Điện Biên Phủ 1954 và Đại thắng mùa Xuân 1975", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Ngày Quốc khánh 2 tháng 9 năm 1945",
            "definition": "Tại Quảng trường Ba Đình lịch sử ở Hà Nội, Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập khai sinh ra nước Việt Nam Dân chủ Cộng hòa (nay là nước Cộng hòa xã hội chủ nghĩa Việt Nam).",
            "example": "'Nước Việt Nam có quyền hưởng tự do và độc lập, và sự thật đã thành một nước tự do độc lập...'.",
            "essence": "Mở ra trang sử chói lọi: nhân dân lao động từ thân phận nô lệ trở thành người làm chủ đất nước."
          },
          {
            "term": "Chiến dịch Điện Biên Phủ 'Lừng lẫy năm châu, chấn động địa cầu'",
            "definition": "Kéo dài 56 ngày đêm 'khoét núi, ngủ hầm, mưa dầm, cơm vắt' (từ 13/3 đến 7/5/1954), đập tan tập đoàn cứ điểm quân sự mạnh nhất của thực dân Pháp ở Đông Dương, bắt sống tướng Đờ Ca-xtơ-ri.",
            "example": "Chiến thắng buộc Pháp phải kí Hiệp định Giơ-ne-vơ lập lại hòa bình ở miền Bắc Việt Nam.",
            "essence": "Biểu tượng sáng ngời cho tinh thần quật cường và sự hi sinh anh dũng của quân đội ta."
          }
        ],
        "rules": [
          {
            "statement": "Ý nghĩa lịch sử của Đại thắng mùa Xuân ngày 30/4/1975",
            "meaning": "Chiến dịch Hồ Chí Minh toàn thắng, giải phóng hoàn toàn miền Nam, thống nhất đất nước, non sông thu về một mối, mở ra kỉ nguyên độc lập tự do và đi lên chủ nghĩa xã hội.",
            "example": "11 giờ 30 phút ngày 30/4/1975, lá cờ cách mạng tung bay trên nóc Dinh Độc Lập.",
            "essence": "Thắng lợi vĩ đại nhất trong lịch sử chống giặc ngoại xâm của dân tộc thế kỉ XX."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Kể tên 3 tấm gương anh hùng tiêu biểu trong chiến dịch Điện Biên Phủ năm 1954 và hành động anh dũng của họ.",
            "steps": [
              "Bước 1: Anh hùng Phan Đình Giót: lấy thân mình lấp lỗ châu mai của hỏa lực địch để đồng đội xông lên.",
              "Bước 2: Anh hùng Bế Văn Đàn: lấy thân mình làm giá súng cho đồng đội bắn tỉa tiêu diệt địch.",
              "Bước 3: Anh hùng Tô Vĩnh Diện: dũng cảm lấy thân mình chèn khẩu pháo nặng hàng tấn không để lao xuống vực sâu."
            ],
            "answer": "Ba anh hùng: Phan Đình Giót (lấp lỗ châu mai), Bế Văn Đàn (làm giá súng), Tô Vĩnh Diện (chèn pháo)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn năm Bác Hồ ra đi tìm đường cứu nước tại Bến Nhà Rồng là năm 1945 thay vì 1911.",
            "why": "Bác ra đi tìm đường cứu nước ngày 5/6/1911 trên con tàu Đô đốc Latouche-Tréville; năm 1945 là năm đọc Tuyên ngôn Độc lập."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Địa lí các Châu lục: Châu Á và Châu Âu",
        "description": "Vị trí, địa hình, khí hậu, dân cư và kinh tế của Châu Á (núi Everest, các nước láng giềng Trung Quốc, Lào, Campuchia) và Châu Âu.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Châu Á — Châu lục lớn nhất và đông dân nhất thế giới", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Châu Âu — Khí hậu ôn đới và nền kinh tế phát triển", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Châu Á — Lục địa khổng lồ",
            "definition": "Là châu lục có diện tích lớn nhất và số dân đông nhất thế giới. Có dãy núi Hi-ma-lay-a cao nhất hành tinh với đỉnh Everest cao 8.848 m (nóc nhà của thế giới).",
            "example": "Châu Á là cái nôi của nhiều nền văn minh cổ đại rực rỡ và các tôn giáo lớn (Ấn Độ giáo, Phật giáo, Hồi giáo).",
            "essence": "Địa hình đa dạng, giàu tài nguyên thiên nhiên và có nền kinh tế phát triển năng động."
          },
          {
            "term": "Đặc điểm Châu Âu",
            "definition": "Nằm ở phía tây lục địa Á - Âu, chủ yếu thuộc đới khí hậu ôn đới mát mẻ; có nền công nghiệp cơ khí, hóa chất phát triển từ rất sớm và nông nghiệp đạt năng suất cao nhờ khoa học kĩ thuật.",
            "example": "Liên minh châu Âu (EU) là một trong những trung tâm kinh tế, tài chính và khoa học hàng đầu toàn cầu.",
            "essence": "Dân cư Châu Âu chủ yếu là người da trắng, phần lớn sinh sống ở các đô thị hiện đại."
          }
        ],
        "rules": [
          {
            "statement": "Mối quan hệ hữu nghị láng giềng giữa Việt Nam - Lào - Cam-pu-chia",
            "meaning": "Ba nước Đông Dương cùng tựa lưng vào dãy Trường Sơn hùng vĩ, cùng chung dòng sông Mê Kông xanh mát, có truyền thống đoàn kết kề vai sát cánh chống kẻ thù chung và hợp tác cùng phát triển kinh tế.",
            "example": "Mối tình thủy chung sắt son 'Việt - Lào hai nước chúng ta / Tình sâu hơn nước Hồng Hà, Cửu Long'.",
            "essence": "Gìn giữ hòa bình và tình láng giềng hữu nghị là tài sản vô giá của ba dân tộc."
          }
        ],
        "workedExamples": [
          {
            "prompt": "So sánh sự khác nhau cơ bản về màu da dân cư giữa Châu Á và Châu Âu.",
            "steps": [
              "Bước 1: Dân cư Châu Á phần lớn thuộc chủng tộc Môn-gô-lô-ít, có nước da vàng, tóc đen thẳng.",
              "Bước 2: Dân cư Châu Âu thuộc chủng tộc Ơ-rô-pê-ô-ít, có nước da trắng, tóc vàng hoặc nâu xoăn lượn sóng, mắt xanh hoặc nâu.",
              "Bước 3: Mọi màu da chủng tộc trên Trái Đất đều bình đẳng và có quyền sống hạnh phúc như nhau."
            ],
            "answer": "Châu Á chủ yếu là người da vàng; Châu Âu chủ yếu là người da trắng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng dãy Hi-ma-lay-a và đỉnh Everest nằm ở Châu Âu.",
            "why": "Dãy Hi-ma-lay-a nằm ở Châu Á (giữa Nepal và Tây Tạng - Trung Quốc); Châu Âu có dãy An-pơ (Alps)."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chủ đề 5: Châu Phi, Châu Mỹ, Châu Đại Dương và Các Đại dương trên Trái Đất",
        "description": "Châu Phi (hoang mạc Sahara), Châu Mỹ (rừng rậm Amazon), Châu Đại Dương (nước Úc), Châu Nam Cực băng giá và 4 đại dương lớn trên Trái Đất.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Châu Phi nóng bức và Châu Mỹ trù phú", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Châu Đại Dương, Châu Nam Cực và 4 Đại dương lớn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Châu Phi — Châu lục nóng nhất thế giới",
            "definition": "Đại bộ phận diện tích nằm giữa hai đường chí tuyến nên khí hậu quanh năm nóng bức và khô hạn bậc nhất hành tinh; có hoang mạc Xa-ha-ra (Sahara) lớn nhất thế giới và dòng sông Nin huyền thoại.",
            "example": "Động vật đặc trưng gồm sư tử, voi, hươu cao cổ, ngựa vằn sinh sống trên các đồng cỏ xavan bao la.",
            "essence": "Dân cư chủ yếu là người da đen, đời sống còn nhiều khó khăn do hạn hán và dịch bệnh kéo dài."
          },
          {
            "term": "Rừng rậm A-ma-dôn (Amazon) ở Châu Mỹ",
            "definition": "Là khu rừng nhiệt đới mưa ẩm rộng lớn nhất hành tinh nằm ở Nam Mỹ, được ví như 'lá phổi xanh' khổng lồ điều hòa khí hậu toàn cầu và là kho dự trữ sinh học đa dạng nhất Trái Đất.",
            "example": "Sông Amazon có lượng nước ngọt đổ ra đại dương lớn nhất thế giới.",
            "essence": "Bảo vệ rừng Amazon là trách nhiệm sống còn của toàn thể nhân loại trước thảm họa biến đổi khí hậu."
          }
        ],
        "rules": [
          {
            "statement": "Bốn đại dương lớn theo thứ tự diện tích",
            "meaning": "Thái Bình Dương (lớn nhất và sâu nhất) -> Đại Tây Dương -> Ấn Độ Dương -> Bắc Băng Dương (nhỏ nhất và lạnh nhất quanh năm đóng băng).",
            "example": "Nước biển và đại dương bao phủ hơn 70% bề mặt Trái Đất, biến hành tinh của chúng ta thành một 'Hành tinh Xanh'.",
            "essence": "Đại dương là nguồn tài nguyên hải sản, năng lượng và điều hòa nhiệt độ toàn cầu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao Châu Nam Cực được gọi là 'châu lục lạnh nhất và hoang vắng nhất thế giới'?",
            "steps": [
              "Bước 1: Vị trí: nằm trọn vẹn ở vùng cực Nam Trái Đất, quanh năm nhận được rất ít bức xạ nhiệt mặt trời.",
              "Bước 2: Khí hậu: băng tuyết phủ dày đặc quanh năm hàng ngàn mét, nhiệt độ mùa đông có thể xuống tới -80°C.",
              "Bước 3: Dân cư: không có người định cư sinh sống lâu dài, chỉ có chim cánh cụt và các nhà khoa học đến nghiên cứu trong các trạm thí nghiệm tạm thời."
            ],
            "answer": "Băng tuyết vĩnh cửu bao phủ quanh năm, nhiệt độ cực thấp và không có người dân cư trú thường xuyên."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng chim cánh cụt sống ở Bắc Cực.",
            "why": "Chim cánh cụt sinh sống chủ yếu ở vùng Nam Bán Cầu (Châu Nam Cực); ở Bắc Cực là loài gấu trắng Bắc Cực."
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
        "title": "Chủ đề 1: Máy tính và Em: Khám phá Thế giới số",
        "description": "Các thành phần cơ bản của máy tính, thiết bị vào - ra (bàn phím, chuột, màn hình, máy in), thư mục và tệp, cách tổ chức lưu trữ thông tin khoa học.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phần cứng, phần mềm và các thiết bị vào - ra", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tổ chức cây thư mục và lưu trữ tệp tin khoa học", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thiết bị Vào và Thiết bị Ra",
            "definition": "Thiết bị vào (Input): tiếp nhận thông tin từ người dùng đưa vào máy tính (bàn phím, chuột, micro, máy quét). Thiết bị ra (Output): xuất thông tin từ máy tính ra cho con người hiểu (màn hình, loa, máy in, máy chiếu).",
            "example": "Gõ phím chữ 'A' (thiết bị vào) -> màn hình hiển thị chữ 'A' (thiết bị ra).",
            "essence": "Luồng thông tin: Vào -> Bộ xử lí CPU -> Ra."
          },
          {
            "term": "Cây thư mục (Folder Tree)",
            "definition": "Cách sắp xếp các tệp dữ liệu vào từng thư mục mẹ và thư mục con phân cấp theo môn học hoặc theo năm để dễ tìm kiếm và quản lí.",
            "example": "Thư mục 'HOC TAP LOP 5' chứa các thư mục con: 'Toan', 'Tieng Viet', 'Tin hoc', 'Ve'.",
            "essence": "Sắp xếp gọn gàng ngăn nắp giúp tiết kiệm thời gian tìm kiếm tài liệu."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc đặt tên tệp và thư mục an toàn",
            "meaning": "Nên đặt tên ngắn gọn, rõ nghĩa, không dấu tiếng Việt có khoảng trắng kì lạ, tránh dùng các kí tự đặc biệt cấm: / \\ : * ? \" < > |.",
            "example": "Dat ten dung: Bai_tap_Toan_Lop5.docx thay vi Bai???***.docx.",
            "essence": "Giúp hệ điều hành không bị lỗi đường dẫn khi sao chép hoặc gửi qua email."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Em hãy phân loại các thiết bị sau vào hai nhóm Thiết bị Vào và Thiết bị Ra: Bàn phím, Tai nghe, Máy in, Chuột, Máy chiếu, Micro.",
            "steps": [
              "Bước 1: Thiết bị Vào: Bàn phím (nhập văn bản), Chuột (điều khiển con trỏ), Micro (thu âm thanh).",
              "Bước 2: Thiết bị Ra: Tai nghe (phát âm thanh), Máy in (in trang giấy), Máy chiếu (chiếu hình ảnh lên màn lớn)."
            ],
            "answer": "Vào: Bàn phím, Chuột, Micro. Ra: Tai nghe, Máy in, Máy chiếu."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn màn hình máy tính thông thường là thiết bị vào.",
            "why": "Màn hình thông thường chỉ hiển thị hình ảnh ra (thiết bị ra). Trừ trường hợp màn hình cảm ứng điện thoại/iPad vừa là thiết bị vào vừa là thiết bị ra."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: An toàn trên Mạng Internet và Ứng xử Văn minh số",
        "description": "Bảo vệ thông tin cá nhân, mật khẩu mạnh, nhận diện thư rác và liên kết độc hại, văn hóa tôn trọng bạn bè trên không gian mạng.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Bảo vệ thông tin cá nhân và mật khẩu an toàn", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phòng tránh lừa đảo mạng và ứng xử văn minh khi trực tuyến", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thông tin cá nhân nhạy cảm",
            "definition": "Là những thông tin tuyệt đối không được tùy tiện công khai cho người lạ trên mạng: Họ tên đầy đủ, ngày tháng năm sinh, địa chỉ nhà riêng, số điện thoại của bố mẹ, tên trường lớp, ảnh chụp thẻ học sinh.",
            "example": "Kẻ xấu có thể lợi dụng địa chỉ trường lớp để dàn cảnh bắt cóc hoặc lừa đảo người thân.",
            "essence": "Bảo vệ danh tính số là bảo vệ sự an toàn tính mạng ngoài đời thực."
          },
          {
            "term": "Mật khẩu mạnh (Strong Password)",
            "definition": "Mật khẩu có độ dài tối thiểu từ 8 kí tự trở lên, kết hợp chữ hoa, chữ thường, chữ số và kí hiệu đặc biệt (@, #, $). Không dùng ngày sinh hoặc số điện thoại làm mật khẩu.",
            "example": "Mat khau manh: BongBong@2026; Mat khau yeu: 123456 hoặc nam2014.",
            "essence": "Mật khẩu giống như chìa khóa cửa ngôi nhà số của em; mật khẩu yếu sẽ bị kẻ trộm bẻ khóa dễ dàng."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc ứng xử khi gặp nội dung xấu hoặc bị bắt nạt trên mạng",
            "meaning": "1) Không trả lời, không tranh cãi. 2) Chụp ảnh màn hình làm bằng chứng. 3) Chặn người gửi. 4) Kể ngay với cha mẹ hoặc thầy cô giáo tin cậy.",
            "example": "Không chia sẻ (share) hoặc bình luận vào các video bạo lực, tin tức giả mạo giật gân.",
            "essence": "Văn minh mạng là giữ cho đôi mắt và lời nói luôn trong sạch."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Khi đang chơi game online, một tài khoản lạ nhắn tin: 'Anh là bạn của bố em, cho anh số điện thoại của mẹ em để anh tặng quà sinh nhật nhé'. Em sẽ làm gì?",
            "steps": [
              "Bước 1: Nhận diện rủi ro: Người lạ xin số điện thoại người thân qua mạng có dấu hiệu lừa đảo.",
              "Bước 2: Tuyệt đối không cung cấp số điện thoại hoặc bất kì thông tin nào.",
              "Bước 3: Không tiếp tục nói chuyện, gọi ngay cho bố mẹ để hỏi và xác minh."
            ],
            "answer": "Không cung cấp số điện thoại, giữ khoảng cách và báo ngay cho bố mẹ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chia sẻ mật khẩu tài khoản học trực tuyến cho bạn thân vì tin tưởng nhau.",
            "why": "Mật khẩu là bí mật cá nhân duy nhất; bạn bè có thể vô tình làm lộ mật khẩu hoặc sử dụng vào mục đích xấu gây rắc rối."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Soạn thảo Văn bản và Thiết kế Bài trình chiếu",
        "description": "Định dạng văn bản tiếng Việt chuẩn Unicode, chèn ảnh và bảng biểu trong Word, tạo trang trình chiếu thuyết trình sinh động trong PowerPoint.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Kỹ năng định dạng văn bản và chèn bảng biểu trong Word", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thiết kế bài trình chiếu PowerPoint kèm hiệu ứng chuyển động", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Kiểu gõ tiếng Việt Telex và Bảng mã Unicode",
            "definition": "Quy tắc gõ dấu thanh: s (sắc), f (huyền), r (hỏi), x (ngã), j (nặng). Gõ chữ mũ: aa (â), oo (ô), ee (ê), aw (ă), ow (ơ), uw (ư), dd (đ). Bảng mã chuẩn quốc tế là Unicode dựng sẵn.",
            "example": "Gõ 'Toan hoc': T - o - a - n - f -> Toàn; h - o - c - j -> học.",
            "essence": "Gõ đúng quy tắc giúp văn bản không bị lỗi phông chữ trên mọi máy tính."
          },
          {
            "term": "Bố cục một trang trình chiếu (Slide) đẹp",
            "definition": "Quy tắc 6x6: Không quá 6 dòng chữ trên một slide, mỗi dòng không quá 6 từ. Kết hợp hình ảnh minh họa sắc nét, phông chữ to rõ ràng, màu nền tương phản với màu chữ.",
            "example": "Nền slide màu sáng (trắng, xanh nhạt) thì chữ màu tối (đen, xanh đậm); tránh lạm dụng quá nhiều hiệu ứng bay lượn rối mắt.",
            "essence": "Bài trình chiếu là công cụ hỗ trợ trực quan, giúp người nghe tập trung vào lời thuyết trình của em."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc gõ dấu câu trong soạn thảo văn bản",
            "meaning": "Dấu phẩy, dấu chấm, dấu hai chấm, dấu chấm phẩy phải gõ sát ngay sau từ phía trước, rồi mới gõ một dấu cách (Space) trước khi viết từ tiếp theo.",
            "example": "Gõ đúng: 'Hà Nội, Thủ đô của Việt Nam.' Gõ sai: 'Hà Nội ,Thủ đô của Việt Nam .'",
            "essence": "Tránh lỗi chính tả soạn thảo sơ đẳng nhất của người dùng máy tính."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày các bước chèn một hình ảnh từ máy tính vào trang văn bản Microsoft Word.",
            "steps": [
              "Bước 1: Đặt con trỏ chuột tại vị trí muốn chèn ảnh trong bài văn.",
              "Bước 2: Trên thanh công cụ, chọn thẻ 'Insert' (Chèn) -> bấm chọn 'Pictures' (Hình ảnh) -> chọn 'This Device'.",
              "Bước 3: Chọn thư mục lưu ảnh, nhấp chuột vào ảnh cần chèn rồi bấm nút 'Insert'.",
              "Bước 4: Nhấp vào ảnh, kéo 4 góc để thu nhỏ hoặc phóng to kích thước phù hợp."
            ],
            "answer": "Thực hiện theo quy trình 4 bước: Đặt trỏ chuột -> Insert -> Pictures -> Chọn ảnh và căn chỉnh kích thước."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chèn ảnh quá to che lấp toàn bộ chữ mà không biết dùng tính năng 'Wrap Text' để căn chỉnh văn bản bao quanh ảnh.",
            "why": "Chọn Wrap Text -> 'Square' hoặc 'Tight' để dòng chữ tự động uốn lượn gọn gàng quanh bức ảnh."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Giải quyết Vấn đề và Lập trình trực quan Scratch",
        "description": "Thuật toán tuần tự, rẽ nhánh và lặp; làm quen với môi trường lập trình kéo thả Scratch; lập trình nhân vật di chuyển, tính toán và vẽ hình.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái niệm thuật toán và các cấu trúc điều khiển cơ bản", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Lập trình kéo thả khối lệnh điều khiển nhân vật trong Scratch", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thuật toán (Algorithm)",
            "definition": "Là một dãy các bước hữu hạn, rõ ràng, được thực hiện theo một trình tự xác định để giải quyết một bài toán hoặc nhiệm vụ cụ thể.",
            "example": "Thuật toán pha nước chanh: Bước 1: Rót nước vào cốc -> Bước 2: Bỏ đường khuấy tan -> Bước 3: Vắt chanh bỏ hạt -> Bước 4: Thả đá và thưởng thức.",
            "essence": "Máy tính chỉ là cỗ máy thực thi chính xác từng bước thuật toán do con người lập trình ra."
          },
          {
            "term": "Ba cấu trúc điều khiển trong lập trình",
            "definition": "1) Tuần tự: Làm từng việc lần lượt từ trên xuống dưới. 2) Rẽ nhánh (Nếu... thì... / If... then...): Chỉ làm khi điều kiện đúng. 3) Lặp (Repeat / Forever): Lặp lại một hành động nhiều lần.",
            "example": "Lặp 4 lần [Đi thẳng 100 bước, quay phải 90 độ] => Nhân vật Scratch sẽ vẽ được một hình vuông hoàn hảo.",
            "essence": "Mọi chương trình phần mềm tinh vi trên thế giới đều được xây dựng từ 3 khối cấu trúc cơ bản này."
          }
        ],
        "rules": [
          {
            "statement": "Khối lệnh lặp vẽ hình đa giác đều trong Scratch",
            "meaning": "Để vẽ hình đa giác đều n cạnh, ta cho nhân vật lặp lại n lần: [Di chuyển a bước, xoay phải (360 : n) độ].",
            "example": "Vẽ hình tam giác đều: lặp 3 lần [di chuyển 100 bước, xoay phải 360:3 = 120 độ].",
            "essence": "Tổng các góc quay ngoài của mọi đa giác lồi luôn bằng đúng 360 độ."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Viết thuật toán bằng lời để nhân vật Chú mèo Scratch vẽ một hình ngôi sao 5 cánh.",
            "steps": [
              "Bước 1: Đặt bút vẽ xuống mặt sân khấu và chọn màu bút.",
              "Bước 2: Thiết lập vòng lặp 5 lần (tương ứng 5 cánh sao).",
              "Bước 3: Trong mỗi vòng lặp: Di chuyển thẳng 150 bước -> Xoay phải 144 độ (vì góc quay ngoài của ngôi sao 5 cánh là 720 : 5 = 144 độ).",
              "Bước 4: Nhấc bút lên sau khi vẽ xong."
            ],
            "answer": "Thuật toán lặp 5 lần [Di chuyển 150 bước, Xoay phải 144 độ]."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên không đặt góc quay đúng (ví dụ vẽ hình vuông lại xoay 60 độ thay vì 90 độ).",
            "why": "Hình vuông có 4 góc vuông 90 độ; lấy 360 độ chia cho 4 cạnh bằng đúng 90 độ."
          }
        ]
      }
    ]
  },
  "dao-duc": {
    "id": "dao-duc",
    "name": "Đạo đức",
    "icon": "🧡",
    "chapters": [
      {
        "id": "ch01",
        "title": "Bài 1: Biết ơn Thầy Cô và Tự hào Truyền thống Trường lớp",
        "description": "Ý nghĩa công ơn dạy dỗ của thầy cô giáo, truyền thống tôn sư trọng đạo, việc làm cụ thể thể hiện lòng biết ơn thầy cô và giữ gìn danh dự trường lớp.",
        "lessons": [
          { "id": "l01", "title": "Tiết 1: Ý nghĩa ngày Nhà giáo Việt Nam 20/11 và công ơn thầy cô", "hasRealContent": true },
          { "id": "l02", "title": "Tiết 2: Hành động thiết thực tri ân thầy cô và xây dựng trường học hạnh phúc", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Truyền thống Tôn sư trọng đạo",
            "definition": "Là nét đẹp đạo đức ngàn đời của dân tộc Việt Nam, thể hiện sự kính trọng, biết ơn và vâng lời thầy cô giáo - những người đã tận tụy dạy dỗ, truyền thụ tri thức và uốn nắn nhân cách cho học sinh.",
            "example": "'Không thầy đố mày làm nên'; 'Muốn sang thì bắc cầu kiều / Muốn con hay chữ thì yêu lấy thầy'.",
            "essence": "Thầy cô chắp cánh ước mơ cho bao thế hệ học trò bay cao, bay xa."
          },
          {
            "term": "Hành vi tri ân đích thực",
            "definition": "Không nằm ở những món quà đắt tiền mà thể hiện qua thái độ chăm chú nghe giảng, làm bài tập đầy đủ, chào hỏi lễ phép, nỗ lực đạt hoa điểm mười và sống trung thực, nhân ái.",
            "example": "Chăm sóc bồn hoa lớp học sạch đẹp, tự giác giúp đỡ bạn bè cùng tiến bộ.",
            "essence": "Sự trưởng thành và nên người của học sinh chính là món quà vô giá nhất dâng tặng thầy cô."
          }
        ],
        "rules": [
          {
            "statement": "Lời chào và thái độ ứng xử với thầy cô",
            "meaning": "Khi gặp thầy cô giáo ở trường cũng như ngoài đường phố, học sinh cần dừng lại, đứng nghiêm túc, khoanh tay và cất lời chào lễ phép rõ ràng: 'Em chào thầy/cô ạ!'.",
            "example": "Không chạy vụt qua mặt thầy cô hoặc cúi mặt giả vờ không nhìn thấy.",
            "essence": "'Tiên học lễ, hậu học văn' — Lễ phép là nấc thang đầu tiên của người có học thức."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trong giờ học môn Toán, bạn Hùng ngồi làm việc riêng và bị cô giáo nhắc nhở. Hùng cảm thấy bực bội và tỏ thái độ vùng vằng. Em có nhận xét gì về việc làm của bạn Hùng và sẽ khuyên bạn như thế nào?",
            "steps": [
              "Bước 1: Nhận xét: Việc làm của bạn Hùng là sai, thể hiện sự thiếu tôn trọng cô giáo và vi phạm nội quy lớp học.",
              "Bước 2: Phân tích: Cô giáo nhắc nhở vì muốn bạn chú ý nghe giảng để không bị hổng kiến thức; thái độ vùng vằng là vô lễ.",
              "Bước 3: Lời khuyên: Bạn Hùng nên đứng lên xin lỗi cô giáo, cất đồ chơi vào cặp và tập trung theo dõi bài giảng để hiểu bài."
            ],
            "answer": "Hùng sai vì vô lễ; cần nhận lỗi chân thành và tập trung học tập nghiêm túc."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng chỉ cần chào hỏi các thầy cô đang trực tiếp dạy lớp mình, còn thầy cô dạy lớp khác thì không cần chào.",
            "why": "Tất cả các thầy cô giáo trong trường đều là những người thầy đáng kính cần được tôn trọng như nhau."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Bài 2: Tôn trọng Sự khác biệt và Lòng Nhân ái",
        "description": "Tôn trọng bạn bè khác biệt về ngoại hình, hoàn cảnh gia đình, dân tộc hoặc sở thích; không trêu chọc miệt thị; lan tỏa tinh thần tương thân tương ái.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tôn trọng sở thích và hoàn cảnh riêng của người khác", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tinh thần tương thân tương ái và chia sẻ khó khăn", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tôn trọng sự khác biệt",
            "definition": "Là biết chấp nhận, thấu hiểu và tôn trọng những điểm khác nhau giữa mình và người khác về ngoại hình, tính cách, tiếng nói địa phương, phong tục tập quán hoặc sở thích cá nhân; không chê bai, kì thị hay cô lập bạn bè.",
            "example": "Một bạn học sinh người dân tộc thiểu số chuyển vào lớp, cả lớp niềm nở chào đón, giúp bạn làm quen với môi trường mới thay vì cười cợt giọng nói của bạn.",
            "essence": "Mỗi người là một bông hoa độc nhất vô nhị trong vườn hoa muôn sắc màu của cuộc sống."
          },
          {
            "term": "Lòng Nhân ái và Sự sẻ chia",
            "definition": "Tình yêu thương con người, biết đau nỗi đau của người khác, sẵn lòng giúp đỡ những mảnh đời bất hạnh, người già neo đơn, trẻ em khuyết tật mà không tính toán thiệt hơn.",
            "example": "Quyên góp sách vở, quần áo ấm ủng hộ các bạn học sinh vùng lũ lụt miền Trung.",
            "essence": "'Lá lành đùm lá rách' — Cho đi yêu thương là nhận lại niềm an vui trong tâm hồn."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc chống miệt thị ngoại hình (Body Shaming) trong học đường",
            "meaning": "Tuyệt đối không lấy ngoại hình của bạn bè (béo, gầy, cao, thấp, da đen, tật nguyền) ra làm trò đùa cợt hoặc đặt biệt danh xúc phạm.",
            "example": "Lời nói vô tình có thể gây tổn thương tâm lí sâu sắc và khiến bạn rơi vào trầm cảm tự ti.",
            "essence": "'Lời nói chẳng mất tiền mua / Lựa lời mà nói cho vừa lòng nhau'."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Lớp em có một bạn bị khuyết tật ở chân phải chống nạng đi lại rất khó khăn. Vào giờ ra chơi, một nhóm bạn chạy nhảy xô đẩy suýt làm bạn ngã rồi cười đùa. Em sẽ ứng xử như thế nào?",
            "steps": [
              "Bước 1: Nhanh chóng chạy lại đỡ bạn khuyết tật đứng vững và hỏi thăm xem bạn có bị đau ở đâu không.",
              "Bước 2: Nhắc nhở nghiêm túc nhóm bạn xô đẩy: 'Các bạn đùa giỡn như vậy rất nguy hiểm, lỡ bạn ngã gãy chân thì sao!'.",
              "Bước 3: Rủ bạn cùng ngồi chơi cờ vua hoặc đọc sách truyện tại chỗ để bạn cảm thấy vui vẻ, hòa đồng cùng lớp."
            ],
            "answer": "Đỡ bạn, nhắc nhở nhóm đùa giỡn và cùng chơi trò chơi phù hợp với bạn."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đứng ngoài cười theo khi thấy bạn bè trêu chọc một người yếu thế vì nghĩ 'mình không trêu thì không có tội'.",
            "why": "Hành vi hùa theo hoặc thờ ơ trước cái xấu cũng là đồng lõa với hành vi bạo lực tinh thần học đường."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Bài 3: Vượt khó vươn lên và Tinh thần Trách nhiệm",
        "description": "Ý chí vượt qua hoàn cảnh khó khăn, thói quen tự lập trong sinh hoạt và học tập, tinh thần dám làm dám chịu trách nhiệm trước sai lầm.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Ý chí vượt khó vươn lên trong học tập", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tinh thần tự giác và dũng cảm nhận lỗi", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tinh thần vượt khó",
            "definition": "Là nghị lực kiên trì, không nản lòng chùn bước trước những thử thách, khó khăn trong học tập và cuộc sống; luôn chủ động tìm cách khắc phục để vươn tới mục tiêu cao đẹp.",
            "example": "Thầy giáo Nguyễn Ngọc Ký bị liệt cả hai tay từ nhỏ đã kiên trì tập viết bằng đôi bàn chân để trở thành nhà giáo ưu tú.",
            "essence": "'Lửa thử vàng, gian nan thử sức' — Khó khăn là trường học tôi luyện bản lĩnh con người."
          },
          {
            "term": "Lòng dũng cảm nhận lỗi và sửa lỗi",
            "definition": "Khi làm sai hoặc làm hỏng việc gì, dám đứng ra thừa nhận khuyết điểm của bản thân, không đổ lỗi cho hoàn cảnh hay cho người khác, và quyết tâm sửa đổi sai lầm đó.",
            "example": "Vô tình đá bóng làm vỡ cửa kính nhà hàng xóm, em chạy lại lễ phép nhận lỗi và xin lỗi bác chủ nhà.",
            "essence": "Người biết nhận lỗi là người có lòng tự trọng và dũng cảm nhất."
          }
        ],
        "rules": [
          {
            "statement": "Phương châm tự lập của học sinh cuối cấp tiểu học",
            "meaning": "Tự giác chuẩn bị sách vở đồ dùng học tập theo thời khóa biểu từ tối hôm trước; tự gấp chăn màn và giặt tất dép của mình; không đợi cha mẹ nhắc nhở.",
            "example": "Tự lập hôm nay là nền móng vững chắc để tự tin bước vào môi trường THCS năng động.",
            "essence": "Làm chủ bản thân bắt đầu từ những việc nhỏ hàng ngày."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Gặp một bài toán chuyển động đều rất khó trong đề kiểm tra thử, Nam định giở sách giải ra chép cho nhanh để kịp giờ nộp. Nếu là bạn của Nam, em sẽ khuyên bạn điều gì?",
            "steps": [
              "Bước 1: Khuyên bạn không nên chép sách giải vì đó là hành vi gian lận, không trung thực.",
              "Bước 2: Giải thích cho Nam hiểu: chép lời giải thì được điểm cao ảo nhưng sẽ không hiểu bản chất, khi thi thật vào lớp 6 sẽ không làm được bài.",
              "Bước 3: Gợi ý cùng bạn vẽ sơ đồ đoạn thẳng tóm tắt bài toán để tìm ra hướng giải quyết độc lập."
            ],
            "answer": "Khuyên bạn trung thực tự làm bài; khó khăn cần suy nghĩ hoặc nhờ thầy cô hướng dẫn chứ không chép đối phó."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đổ lỗi cho đồng hồ báo thức hỏng khi bản thân ngủ dậy muộn đi học muộn.",
            "why": "Đó là hành vi trốn tránh trách nhiệm; cần dũng cảm thừa nhận mình thức khuya xem điện thoại để khắc phục."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Bài 4: Yêu chuộng Hòa bình và Giữ gìn Môi trường sống",
        "description": "Giá trị của cuộc sống hòa bình, bài trừ bạo lực học đường, trách nhiệm của thiếu nhi trong việc xây dựng tình hữu nghị quốc tế và bảo vệ hành tinh xanh.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Em yêu hòa bình và tình hữu nghị quốc tế", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Chung tay vì một hành tinh xanh - sạch - đẹp", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hòa bình là gì?",
            "definition": "Hòa bình là cuộc sống yên vui, ấm no, không có chiến tranh bom đạn; con người được tự do học tập, làm việc và yêu thương nhau trong sự tôn trọng lẫn nhau giữa các dân tộc.",
            "example": "Hình ảnh chim bồ câu trắng ngậm cành ô liu là biểu tượng thiêng liêng cho khát vọng hòa bình trên toàn thế giới.",
            "essence": "Hòa bình là điều kiện tiên quyết để trẻ em được cắp sách tới trường và mỉm cười hạnh phúc mỗi ngày."
          },
          {
            "term": "Phòng chống Bạo lực học đường",
            "definition": "Nói không với các hành vi đánh nhau, chửi thề, đe dọa, cô lập hoặc xúc phạm danh dự của bạn bè trong trường lớp cũng như trên mạng xã hội.",
            "example": "Khi có xích mích hiểu lầm, bình tĩnh ngồi lại nói chuyện nhẹ nhàng hoặc nhờ thầy cô chủ nhiệm làm trọng tài phân xử.",
            "essence": "'Một điều nhịn là chín điều lành' — Dùng sự bao dung hóa giải hận thù."
          }
        ],
        "rules": [
          {
            "statement": "Hành động thể hiện tinh thần yêu chuộng hòa bình của học sinh",
            "meaning": "Sống chan hòa với bạn bè; tôn trọng sự khác biệt sắc tộc; tích cực tham gia các phong trào vẽ tranh, viết thư quốc tế UPU vì hòa bình thế giới.",
            "example": "Xây dựng tình bạn trong sáng, đoàn kết giúp đỡ nhau cùng tiến bộ trong học tập.",
            "essence": "Hòa bình thế giới bắt đầu từ sự hòa thuận trong mỗi lớp học."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao chiến tranh lại là thảm họa tàn khốc nhất đối với trẻ em?",
            "steps": [
              "Bước 1: Chiến tranh bom đạn tước đoạt sinh mạng của biết bao trẻ em ngây thơ vô tội.",
              "Bước 2: Chiến tranh phá hủy trường học, bệnh viện, nhà cửa khiến trẻ em bị mồ côi cha mẹ, đói khát và thất học.",
              "Bước 3: Nỗi đau và nỗi ám ảnh tinh thần sau chiến tranh để lại vết thương sâu sắc suốt cả cuộc đời.",
              "Bước 4: Do đó, mọi người phải kiên quyết lên án chiến tranh và bảo vệ nền hòa bình bền vững."
            ],
            "answer": "Chiến tranh cướp đi sinh mạng, người thân, trường học và tương lai tươi sáng của trẻ thơ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng việc bảo vệ hòa bình là việc to lớn của các nguyên thủ quốc gia, học sinh nhỏ tuổi không liên quan.",
            "why": "Chống bạo lực học đường, nhường nhịn bạn bè và giữ gìn tình đoàn kết lớp học chính là hành động gìn giữ hòa bình cụ thể nhất."
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
        "title": "Chương 1: Công nghệ và Đời sống: Đồ dùng điện gia đình",
        "description": "Các thiết bị điện thông dụng trong nhà (quạt điện, đèn học, nồi cơm điện, tủ lạnh), nguyên lí hoạt động cơ bản và thói quen sử dụng an toàn, tiết kiệm.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Các đồ dùng điện thông dụng trong gia đình", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Cách sử dụng đồ dùng điện an toàn và hiệu quả", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Đồ dùng điện loại nhiệt và loại cơ",
            "definition": "Đồ dùng loại nhiệt: biến đổi điện năng thành nhiệt năng (nồi cơm điện, bàn là, ấm đun nước). Đồ dùng loại cơ: biến đổi điện năng thành cơ năng làm quay động cơ (quạt điện, máy xay sinh tố, máy hút bụi).",
            "example": "Nồi cơm điện dùng mâm nhiệt nóng đỏ để nấu chín gạo; quạt điện dùng động cơ điện quay cánh quạt tạo luồng gió mát.",
            "essence": "Mỗi thiết bị được thiết kế để biến đổi điện năng thành dạng năng lượng phục vụ nhu cầu đời sống."
          },
          {
            "term": "Nhãn năng lượng tiết kiệm điện",
            "definition": "Nhãn dán hình ngôi sao trên thiết bị điện (từ 1 đến 5 sao). Càng nhiều sao thì thiết bị đó càng tiết kiệm điện năng tiêu thụ.",
            "example": "Khi mua tủ lạnh hoặc điều hòa, nên chọn loại có dán nhãn 5 sao có công nghệ Inverter.",
            "essence": "Tiêu chuẩn quốc gia giúp người tiêu dùng lựa chọn sản phẩm thân thiện môi trường."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc an toàn khi sử dụng ấm đun nước siêu tốc",
            "meaning": "Không đổ nước quá vạch MAX (tránh nước sôi trào ra ngoài gây chập điện) và không để nước dưới vạch MIN (tránh cháy mâm nhiệt); chỉ cắm điện khi đã đậy kín nắp.",
            "example": "Khi rót nước phải rút phích cắm hoặc nhấc thân ấm ra khỏi đế tiếp điện.",
            "essence": "Đồ dùng điện sinh nhiệt cao luôn tiềm ẩn nguy cơ cháy nổ nếu dùng sai hướng dẫn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Gia đình em sử dụng một chiếc đèn bàn học LED công suất 10W để học bài 4 giờ mỗi ngày. Tính số tiền điện phải trả cho chiếc đèn trong một tháng (30 ngày), biết giá điện trung bình là 2.000 đồng/kWh.",
            "steps": [
              "Bước 1: Tính điện năng tiêu thụ trong 30 ngày: A = 10W * 4 giờ * 30 ngày = 1.200 Wh.",
              "Bước 2: Đổi sang đơn vị ki-lô-oát giờ (số điện kWh): 1.200 Wh = 1,2 kWh.",
              "Bước 3: Tính số tiền điện: 1,2 * 2.000 = 2.400 (đồng)."
            ],
            "answer": "Chiếc đèn bàn LED chỉ tốn 2.400 đồng tiền điện mỗi tháng, rất tiết kiệm điện."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy bàn là điện đang cắm nóng đặt nằm ngang trên quần áo rồi bỏ đi làm việc khác.",
            "why": "Nhiệt lượng tích tụ sẽ làm cháy quần áo và gây hỏa hoạn thiêu rụi ngôi nhà trong chốc lát."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Sáng chế Công nghệ và Thiết kế Kĩ thuật đơn giản",
        "description": "Quy trình thiết kế kĩ thuật, các bước sáng chế đồ chơi công nghệ, sử dụng vật liệu tái chế (bìa các-tông, chai nhựa, que kem) để chế tạo sản phẩm hữu ích.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Quy trình thiết kế kĩ thuật 5 bước", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành làm đồ chơi hoặc dụng cụ học tập từ vật liệu tái chế", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quy trình thiết kế kĩ thuật 5 bước",
            "definition": "1) Xác định vấn đề/nhu cầu -> 2) Tìm hiểu và đề xuất ý tưởng giải pháp -> 3) Thiết kế bản vẽ phác thảo -> 4) Chế tạo mô hình thử nghiệm -> 5) Đánh giá và cải tiến hoàn thiện.",
            "example": "Thiết kế chiếc giá đỡ điện thoại bằng que kem: Vẽ phác thảo -> Dán keo que kem -> Thử đặt điện thoại xem có vững không -> Sơn màu trang trí.",
            "essence": "Tư duy kĩ sư: biến ý tưởng trong đầu thành sản phẩm thực tế hữu ích."
          },
          {
            "term": "Vật liệu STEM tái chế",
            "definition": "Sử dụng lại các phế liệu sạch trong gia đình (hộp sữa, nắp chai, que kem, ống hút giấy, dây thun) để làm mô hình kĩ thuật thay vì vứt bỏ ra môi trường.",
            "example": "Làm chiếc thuyền buồm chạy bằng dây thun từ chai nước rỗng và que kem.",
            "essence": "Sáng tạo công nghệ gắn liền với tinh thần bảo vệ môi trường xanh."
          }
        ],
        "rules": [
          {
            "statement": "An toàn khi sử dụng dụng cụ cắt dán (kéo, dao rọc giấy, súng bắn keo)",
            "meaning": "Không đùa nghịch mũi kéo hướng vào bạn bè; khi dùng súng bắn keo nến tuyệt đối không chạm tay vào đầu kim loại nóng để tránh bị bỏng rát; luôn có người lớn hỗ trợ khi dùng dao nhọn.",
            "example": "Đặt kéo nằm ngang gọn gàng trên bàn khi không sử dụng.",
            "essence": "An toàn lao động là nguyên tắc bất di bất dịch trong mọi hoạt động chế tạo."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Em hãy nêu các bước làm một chiếc hộp đựng bút nhiều ngăn để bàn học từ vỏ hộp sữa giấy bỏ đi.",
            "steps": [
              "Bước 1: Rửa sạch và phơi khô 4 vỏ hộp sữa tươi bằng giấy.",
              "Bước 2: Cắt bỏ phần nắp trên của các hộp với chiều cao so le nhau (ngăn cao để thước kẻ, ngăn thấp để tẩy và gọt bút chì).",
              "Bước 3: Dùng keo sữa hoặc băng dính hai mặt dán 4 hộp sữa dính chặt lại với nhau.",
              "Bước 4: Bọc giấy màu hoa văn bên ngoài và dán sticker trang trí theo sở thích."
            ],
            "answer": "Chiếc hộp bút 4 ngăn tái chế vừa đẹp mắt vừa giúp bàn học ngăn nắp."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Bắt tay vào cắt dán ngay mà không đo đạc và vẽ phác thảo kích thước trước.",
            "why": "Dẫn đến tình trạng các ngăn bị lệch lạc, xiêu vẹo, không đựng vừa bút viết."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Lắp ghép Mô hình Kĩ thuật và Cơ cấu Truyền động",
        "description": "Các chi tiết trong bộ lắp ghép kĩ thuật, cơ cấu truyền động bánh răng, truyền động đai (dây curoa), lắp ráp mô hình xe chạy pin hoặc cần cẩu đơn giản.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Các cơ cấu truyền động cơ học (Bánh răng và Đai truyền)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành lắp ghép mô hình xe đua hoặc cần cẩu", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Truyền động bánh răng",
            "definition": "Là cơ cấu truyền chuyển động quay và lực từ trục này sang trục khác nhờ sự ăn khớp giữa các răng của hai bánh răng.",
            "example": "Đồng hồ cơ học hoạt động nhờ hệ thống bánh răng ăn khớp tỉ mỉ; bánh răng lớn quay chậm nhưng lực khỏe, bánh răng nhỏ quay nhanh hơn.",
            "essence": "Đảm bảo tỉ số truyền chính xác tuyệt đối mà không bị trượt."
          },
          {
            "term": "Truyền động đai (Dây curoa / Dây xích)",
            "definition": "Truyền chuyển động quay giữa hai trục ở khoảng cách xa nhau thông qua dây đai hoặc xích ma sát.",
            "example": "Hệ thống xích líp của xe đạp: đĩa xích lớn ở bàn đạp truyền chuyển động qua dây xích đến líp nhỏ ở bánh sau giúp xe chạy nhanh về phía trước.",
            "essence": "Vận hành êm ái, giảm chấn động và truyền lực được ở cự li xa."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc siết ốc vít trong lắp ghép mô hình kĩ thuật",
            "meaning": "Phải lắp vòng đệm trước khi vặn đai ốc (ê-cu); dùng cờ-lê giữ chặt đai ốc và dùng tuốc-nơ-vít vặn theo chiều kim đồng hồ để siết chặt; vặn ngược chiều kim đồng hồ khi tháo ra.",
            "example": "Vặn theo chiều kim đồng hồ: VÀO (chặt); ngược chiều kim đồng hồ: RA (lỏng).",
            "essence": "Vặn đúng chiều giúp mối ghép cơ học chắc chắn và không làm nhờn ren ốc."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao khi đạp xe đạp lên dốc cao, người ta thường chuyển sang líp sau lớn hơn (ở xe đạp thể thao nhiều tầng số)?",
            "steps": [
              "Bước 1: Líp sau lớn hơn giúp tăng tỉ số truyền lực (được lợi về lực).",
              "Bước 2: Tuy chân phải đạp nhiều vòng hơn (thiệt về đường đi) nhưng lực đạp sẽ nhẹ hơn rất nhiều.",
              "Bước 3: Quy tắc vàng của cơ học: 'Được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi'."
            ],
            "answer": "Chuyển sang líp lớn để đạp nhẹ hơn, giúp xe dễ dàng vượt qua dốc cao."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lắp bánh răng quá sát nhau làm kẹt cứng không thể quay được mô tơ.",
            "why": "Phải để một khoảng hở khe ăn khớp vừa phải (khoảng 0,5 mm) để bánh răng quay êm và không bị ma sát hãm."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Trải nghiệm Nghề nghiệp và Nông nghiệp Công nghệ cao",
        "description": "Các ngành nghề kĩ thuật trong xã hội (thợ điện, thợ cơ khí, kĩ sư nông nghiệp), mô hình trồng rau thủy canh, hệ thống nhà kính thông minh.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khám phá các ngành nghề kĩ thuật và công nghệ quanh em", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Mô hình trồng cây thủy canh và nông nghiệp thông minh", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Trồng cây thủy canh (Hydroponics)",
            "definition": "Là phương pháp trồng cây hiện đại không dùng đất, rễ cây được ngâm trực tiếp vào dung dịch dinh dưỡng hòa tan trong nước có sục khí ô-xy.",
            "example": "Trồng rau xà lách thủy canh trong nhà màng cho rau sạch tuyệt đối, không có sâu bệnh và không tồn dư thuốc bảo vệ thực vật.",
            "essence": "Tiết kiệm 80% nước tưới và kiểm soát chính xác từng khoáng chất nuôi cây."
          },
          {
            "term": "Nông nghiệp công nghệ cao",
            "definition": "Ứng dụng các công nghệ tiên tiến: cảm biến nhiệt độ - độ ẩm, hệ thống tưới phun sương tự động, camera theo dõi sâu bệnh và máy bay không người lái (drone) bón phân.",
            "example": "Nhà kính trồng dưa lưới công nghệ cao tại Đà Lạt năng suất gấp 5 lần trồng ngoài trời tự nhiên.",
            "essence": "Giải phóng sức lao động nặng nhọc của nông dân và đem lại nông sản an toàn cho người tiêu dùng."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm của người làm nghề kĩ thuật, công nghệ",
            "meaning": "Cần có tính cẩn thận, kiên nhẫn, tư duy sáng tạo, yêu thích máy móc, tuân thủ nghiêm ngặt quy tắc an toàn lao động và tinh thần hợp tác nhóm.",
            "example": "Bác thợ điện luôn đeo găng tay cách điện và kiểm tra bút thử điện trước khi sửa chữa đường dây.",
            "essence": "Cẩn trọng và chính xác là phẩm chất số một của người làm kĩ thuật."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 2 ưu điểm nổi bật của mô hình trồng rau trong nhà màng thông minh so với phương pháp trồng rau truyền thống ngoài trời.",
            "steps": [
              "Bước 1: Ngăn chặn sâu bọ, côn trùng xâm nhập tự nhiên, giúp cây rau không bị phá hoại mà không cần phun thuốc trừ sâu độc hại.",
              "Bước 2: Che chắn mưa to gió lớn và kiểm soát nhiệt độ, độ ẩm tối ưu giúp rau phát triển nhanh quanh năm bất kể thời tiết."
            ],
            "answer": "Ưu điểm: Không dùng thuốc sâu độc hại và trồng được rau sạch quanh năm không phụ thuộc thời tiết."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng trồng cây thủy canh chỉ cần dùng nước giếng thông thường mà không cần pha dung dịch dinh dưỡng.",
            "why": "Nước tinh khiết thiếu các khoáng chất đa - vi lượng (đạm, lân, kali, canxi); cây sẽ bị còi cọc và vàng lá chết dần."
          }
        ]
      }
    ]
  }
}

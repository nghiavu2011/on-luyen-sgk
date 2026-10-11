# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa các môn Năng khiếu, Ứng dụng & Thể chất Lớp 12 SGK Kết nối tri thức 2026-2027:
- Công nghệ 12 (Lâm nghiệp & Thủy sản, 4 chương bám sát OCR SGK 12 Kết nối tri thức)
- Mĩ thuật 12 (Điêu khắc, Đồ họa tranh in & Thiết kế sân khấu điện ảnh, 3 chương bám sát OCR SGK 12 Kết nối tri thức)
- Giáo dục Thể chất 12 (Yếu tố tự nhiên & Dinh dưỡng, Bóng đá - Bóng rổ nâng cao, Cầu lông - Bóng chuyền nâng cao, 3 chương bám sát OCR SGK 12 Kết nối tri thức)
"""

true = True
false = False
null = None

APPLIED_SUBJECTS = {
  "cong-nghe": {
    "id": "cong-nghe",
    "name": "Công nghệ 12 - Lâm nghiệp & Thủy sản",
    "icon": "🌲",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Giới thiệu chung về lâm nghiệp",
        "description": "Tìm hiểu vai trò và triển vọng phát triển của ngành lâm nghiệp, đặc trưng của sản xuất lâm nghiệp, các hoạt động lâm nghiệp cơ bản cùng nguyên nhân và giải pháp hạn chế suy thoái tài nguyên rừng.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vai trò và triển vọng của lâm nghiệp", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Các hoạt động lâm nghiệp cơ bản và suy thoái tài nguyên rừng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Sản xuất lâm nghiệp",
            "definition": "Là ngành sản xuất vật chất đặc thù có đối tượng lao động là rừng và đất lâm nghiệp, chu kì kinh doanh dài, mang tính liên ngành sinh thái - kinh tế - xã hội cao và gắn liền mật thiết với điều kiện tự nhiên.",
            "example": "Trồng và kinh doanh rừng keo lấy gỗ nguyên liệu giấy cần chu kì từ 5 đến 7 năm, còn trồng rừng gỗ lớn bản địa như lim xanh, sến, táu đòi hỏi chu kì từ 25 đến 40 năm.",
            "essence": "Lâm nghiệp không chỉ tạo ra lâm sản có giá trị kinh tế mà còn đảm nhận vai trò sống còn trong việc bảo vệ môi trường sinh thái và giảm nhẹ thiên tai."
          },
          {
            "term": "Suy thoái tài nguyên rừng",
            "definition": "Là hiện tượng diện tích rừng bị thu hẹp hoặc chất lượng rừng, độ che phủ, tính đa dạng sinh học và trữ lượng carbon của hệ sinh thái rừng bị suy giảm nghiêm trọng do tác động tiêu cực của con người và biến đổi khí hậu.",
            "example": "Chuyển đổi trái phép rừng tự nhiên sang đất canh tác cây công nghiệp ngắn ngày hoặc khai thác gỗ bừa bãi làm mất đi các tầng tán rừng nguyên sinh.",
            "essence": "Suy thoái rừng làm suy giảm chức năng phòng hộ đầu nguồn, gia tăng nguy cơ lũ ống, lũ quét, xói mòn sạt lở đất và làm mất nơi cư trú của động thực vật hoang dã."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc phát triển lâm nghiệp bền vững",
            "meaning": "Hoạt động lâm nghiệp phải kết hợp hài hòa ba mục tiêu cốt lõi: Bảo tồn sinh thái tự nhiên, nâng cao giá trị kinh tế lâm sản và bảo đảm an sinh xã hội cho cộng đồng dân cư sống phụ thuộc vào rừng.",
            "example": "Áp dụng chứng chỉ quản lý rừng bền vững FSC nhằm đảm bảo gỗ khai thác có nguồn gốc hợp pháp, duy trì độ che phủ và chia sẻ lợi ích công bằng với người dân địa phương.",
            "essence": "Bảo vệ diện tích rừng hiện có đi đôi với nâng cao chất lượng rừng và đẩy mạnh tái tạo tài nguyên rừng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích tác động sinh thái và kinh tế khi độ che phủ rừng ở vùng đầu nguồn bị suy giảm dưới 30%. Đề xuất 3 hành động khắc phục.",
            "steps": [
              "Bước 1: Phân tích tác động sinh thái: Giảm khả năng giữ nước ngầm, gia tăng tốc độ dòng chảy mặt khi mưa lớn dẫn đến xói mòn đất, lũ quét và khô hạn vào mùa cạn.",
              "Bước 2: Phân tích tác động kinh tế: Gây hư hại công trình thủy điện, thủy lợi, vùi lấp đồng ruộng hạ du và làm cạn kiệt nguồn thu lâm sản phi gỗ của cư dân vùng cao.",
              "Bước 3: Đề xuất giải pháp: (1) Khoanh nuôi xúc tiến tái sinh tự nhiên kết hợp trồng bổ sung cây bản địa gỗ lớn; (2) Thực hiện giao đất giao rừng gắn liền với chính sách chi trả dịch vụ môi trường rừng (PES); (3) Tăng cường tuần tra, áp dụng viễn thám và thiết bị bay không người lái để giám sát mất rừng."
            ],
            "answer": "Suy giảm độ che phủ rừng đầu nguồn phá vỡ cân bằng thủy văn sinh thái; giải pháp then chốt là phục hồi rừng phòng hộ bằng cây bản địa kết hợp chính sách chi trả dịch vụ môi trường rừng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng trồng rừng độc canh cây ngoại lai ngắn ngày (như keo, bạch đàn) có giá trị sinh thái phòng hộ tương đương rừng tự nhiên.",
            "why": "Rừng cây ngoại lai độc canh có cấu trúc tầng tán đơn giản, thảm mục mỏng, khả năng giữ nước và bảo vệ đa dạng sinh học kém hơn rất nhiều so với rừng tự nhiên đa tầng tán."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Trồng và chăm sóc rừng",
        "description": "Quy luật sinh trưởng và phát triển của cây rừng qua từng giai đoạn, kỹ thuật gieo ươm cây con giống, các bước làm đất, thời vụ trồng và quy trình chăm sóc rừng trồng đạt tiêu chuẩn kỹ thuật.",
        "lessons": [
          { "id": "l01", "title": "Bài 3: Vai trò, nhiệm vụ của trồng và chăm sóc rừng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 4: Quy luật sinh trưởng và phát triển của cây rừng", "hasRealContent": true },
          { "id": "l03", "title": "Bài 5: Kỹ thuật trồng và chăm sóc rừng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quy luật sinh trưởng và phát triển của cây rừng",
            "definition": "Là chuỗi biến đổi sinh học tuần tự của cây rừng từ giai đoạn non (hạt nảy mầm hình thành cây mạ), giai đoạn sào gần khép tán, giai đoạn trung niên sinh trưởng mạnh về sinh khối đến giai đoạn thành thục và già cỗi.",
            "example": "Giai đoạn cây con cần che bóng nhẹ và độ ẩm cao, nhưng khi bước sang giai đoạn sào và thành thục cần tỉa cành tự nhiên và nhu cầu ánh sáng hoàn toàn để tăng trưởng đường kính thân cây.",
            "essence": "Hiểu rõ từng giai đoạn giúp chủ rừng xác định chính xác thời điểm tỉa thưa, bón thúc và khai thác gỗ tối ưu sinh khối."
          },
          {
            "term": "Kỹ thuật trồng rừng bằng cây con có bầu",
            "definition": "Phương pháp đưa cây giống đã được ươm dưỡng ổn định trong bầu đất dinh dưỡng ra trồng tại hố đào đúng quy cách kích thước trên đất lâm nghiệp đã xử lý thực bì.",
            "example": "Đào hố kích thước 30x30x30 cm, rạch bỏ vỏ bầu nilon khéo léo không làm vỡ bầu đất, đặt cây thẳng đứng giữa hố, lấp đất màu mịn rồi dẫm chặt gốc và vun đất hình mui rùa.",
            "essence": "Cây con có bầu giữ nguyên bộ rễ non hoàn chỉnh, đảm bảo tỷ lệ sống trên 90% sau khi trồng ngoài thực địa."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc mùa vụ và mật độ trồng rừng",
            "meaning": "Thời vụ trồng rừng phải đón đầu mùa mưa ẩm thuận lợi, mật độ trồng phải phù hợp với đặc tính sinh thái của loài cây và mục tiêu kinh doanh gỗ (gỗ lớn hay gỗ nhỏ).",
            "example": "Ở miền Bắc trồng vụ xuân (tháng 2 - 4) hoặc vụ thu (tháng 7 - 9); trồng keo lấy gỗ lớn bố trí mật độ thưa từ 1.100 - 1.660 cây/ha để cây phát triển đường kính thân tối đa.",
            "essence": "Đúng thời vụ đảm bảo đủ ẩm tự nhiên; đúng mật độ hạn chế cạnh tranh ánh sáng dinh dưỡng bất lợi giữa các cá thể cây."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xây dựng quy trình 4 bước kỹ thuật trồng cây con có bầu trên vùng đồi dốc thoái hóa nhằm đảm bảo tỷ lệ sống cao nhất.",
            "steps": [
              "Bước 1: Chuẩn bị hiện trường: Xử lý thực bì cục bộ theo băng hoặc theo hố trước 15 - 30 ngày để tránh xói mòn rửa trôi đất sườn dốc.",
              "Bước 2: Cuốc hố và bón lót: Đào hố 40x40x40 cm, gom lớp đất mặt màu mỡ để riêng, bón lót phân vi sinh hữu cơ trộn đều dưới đáy hố.",
              "Bước 3: Trồng cây: Rạch vỏ bầu cẩn thận không làm nứt vỡ bầu, đặt cây ngay ngắn thẳng đứng, lấp đất tầng mặt nén chặt gốc, đắp đất cao hơn cổ rễ 2 - 3 cm tránh đọng úng nước.",
              "Bước 4: Chăm sóc ban đầu: Dọn cỏ dại xung quanh đường kính 1m, xới xáo phá váng và kiểm tra dặm cây chết sau 15 - 20 ngày."
            ],
            "answer": "Quy trình chuẩn gồm: Xử lý thực bì -> Đào hố bón lót -> Rạch bầu trồng cây nén chặt -> Chăm sóc phá váng dặm cây kịp thời."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Quên rạch bỏ túi nilon bọc bầu đất hoặc giẫm trực tiếp lên cổ rễ non khi trồng cây con có bầu.",
            "why": "Không xé túi bầu khiến rễ cây bị nghẹt không phát triển ra đất ngoài được; giẫm đè rễ gây dập gãy mô dẫn đến thối rễ chết cây."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Bảo vệ và khai thác tài nguyên rừng bền vững",
        "description": "Phương thức quản lý, bảo vệ diện tích rừng nguyên vẹn, phòng trừ dịch bệnh sâu hại cây rừng, kỹ thuật phòng cháy chữa cháy rừng (PCCCR) và nguyên tắc khai thác lâm sản chính quy không làm kiệt quệ tài nguyên.",
        "lessons": [
          { "id": "l01", "title": "Bài 6: Ý nghĩa, nhiệm vụ, thực trạng của việc bảo vệ và khai thác rừng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 7: Biện pháp bảo vệ và khai thác tài nguyên rừng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Phòng cháy và chữa cháy rừng (PCCCR)",
            "definition": "Hệ thống các biện pháp kỹ thuật lâm sinh, tổ chức lực lượng và công nghệ nhằm ngăn chặn nguy cơ bùng phát lửa rừng và dập tắt kịp thời khi có đám cháy xảy ra.",
            "example": "Thiết kế đường băng cản lửa trắng (dọn sạch vật liệu cháy) và đường băng xanh (trồng cây chịu lửa như mỡ, sim mu mua), lắp đặt tháp canh lửa kết hợp cảm biến cảnh báo nhiệt độ ẩm độ.",
            "essence": "Phương châm phòng cháy là chính kết hợp bốn tại chỗ: chỉ huy tại chỗ, lực lượng tại chỗ, phương tiện tại chỗ và hậu cần tại chỗ."
          },
          {
            "term": "Khai thác chọn (Selective Logging)",
            "definition": "Phương thức khai thác chỉ chặt hạ những cây gỗ đã đến tuổi thành thục công nợ, cây già cỗi, cây sâu bệnh trong lâm phần, giữ lại cây non và tầng cây tái sinh để rừng tiếp tục duy trì liên tục chức năng sinh thái.",
            "example": "Chặt không quá 20 - 30% trữ lượng gỗ của lô rừng tự nhiên trong một luân kỳ khai thác, tuyệt đối bảo vệ cây con tái sinh dưới tán.",
            "essence": "Khai thác chọn giúp bảo tồn cấu trúc đa tầng, đa loài và độ che phủ liên tục của rừng tự nhiên."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc khai thác tài nguyên rừng bền vững",
            "meaning": "Lượng gỗ chặt hạ hàng năm trong một lâm phần không được vượt quá lượng tăng trưởng tự nhiên của lâm phần đó, đồng thời phải thực hiện các biện pháp tái sinh phục hồi ngay sau khai thác.",
            "example": "Nếu một khu rừng sản xuất tăng trưởng 8 m3 gỗ/ha/năm thì lượng khai thác bình quân không được vượt quá mức 6 - 7 m3/ha/năm để bảo tồn sinh khối nền tảng.",
            "essence": "Khai thác có kiểm soát đi đôi với tái sinh liên tục để duy trì nguồn vốn tài nguyên vĩnh viễn cho tương lai."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày các bước thiết kế đường băng cản lửa xanh phòng chống cháy rừng trong khu vực rừng trồng giáp ranh khu dân cư.",
            "steps": [
              "Bước 1: Khảo sát địa hình và hướng gió thịnh hành vào mùa khô kiệt để xác định tuyến bố trí đường băng thẳng góc hoặc xiên chéo 45 độ với hướng gió chính.",
              "Bước 2: Xác định bề rộng đường băng cản lửa (thường từ 10 - 20 m tuỳ theo cấp dự báo cháy của loài cây trồng chính).",
              "Bước 3: Dọn sạch thực bì dễ bắt lửa (cỏ tranh, lá khô rụng) trên dải băng cản lửa.",
              "Bước 4: Trồng các loài cây bản địa có khả năng chịu lửa tốt, lá dày mọng nước khó bắt cháy như vối thuốc, mỡ, muồng đen với mật độ dày để ngăn tán lửa lan truyền."
            ],
            "answer": "Đường băng cản lửa xanh được thiết kế vuông góc hướng gió, dọn sạch vật liệu cháy và trồng dải cây xanh lá mọng nước chịu lửa dày tán."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa phương thức khai thác trắng (Clear-cutting) và khai thác chọn (Selective Logging) trên đất rừng dốc.",
            "why": "Khai thác trắng chặt hạ toàn bộ cây trên diện tích lớn khiến đất sườn đồi trơ trọi, gây sạt lở lũ quét thảm khốc; trên sườn dốc chỉ được phép áp dụng khai thác chọn hoặc khai thác dần dải hẹp."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Đại cương và kỹ thuật nuôi thuỷ sản",
        "description": "Vai trò và triển vọng phát triển ngành thủy sản trong kỷ nguyên mới, các chỉ tiêu chất lượng môi trường nước nuôi, kỹ thuật nuôi thương phẩm các loài thủy sản kinh tế và biện pháp phòng trị dịch bệnh thủy sản an toàn sinh học.",
        "lessons": [
          { "id": "l01", "title": "Bài 8: Vai trò và triển vọng của thuỷ sản", "hasRealContent": true },
          { "id": "l02", "title": "Bài 10: Giới thiệu về môi trường nuôi thuỷ sản", "hasRealContent": true },
          { "id": "l03", "title": "Bài 19: Công nghệ nuôi một số loài thuỷ sản kinh tế", "hasRealContent": true },
          { "id": "l04", "title": "Bài 24: Một số bệnh thuỷ sản phổ biến và biện pháp phòng trị", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chỉ tiêu môi trường nước nuôi thủy sản",
            "definition": "Tập hợp các thông số lý - hóa - sinh của khối nước quyết định sự sinh tồn và tăng trưởng của động vật thủy sản như nhiệt độ, độ mặn, oxy hòa tan (DO), pH, hàm lượng khí độc (NH3, NO2, H2S).",
            "example": "Cá tra và tôm nước lợ sinh trưởng tối ưu ở ngưỡng oxy hòa tan DO > 4.0 mg/L và pH dao động ổn định trong khoảng 7.5 - 8.5.",
            "essence": "Môi trường nước là môi trường sống trực tiếp; chất lượng nước quyết định tới 80% tỷ lệ sống và chỉ số chuyển hóa thức ăn FCR của thủy sản."
          },
          {
            "term": "Quy trình nuôi thủy sản theo tiêu chuẩn VietGAP",
            "definition": "Bộ tiêu chuẩn thực hành sản xuất nông nghiệp tốt tại Việt Nam trong nuôi trồng thủy sản, kiểm soát nghiêm ngặt từ con giống sạch bệnh, thức ăn rõ nguồn gốc, an toàn sinh học đến truy xuất nguồn gốc sản phẩm xuất khẩu.",
            "example": "Ghi chép nhật ký ao nuôi điện tử hàng ngày, sử dụng chế phẩm vi sinh Probiotic thay thế hoàn toàn kháng sinh cấm để kiểm soát tảo và phân hủy mùn bã đáy ao.",
            "essence": "VietGAP đảm bảo tạo ra nguồn thủy sản sạch, an toàn vệ sinh thực phẩm, không dư lượng hóa chất độc hại và bảo vệ hệ sinh thái thủy vực."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc phòng bệnh tổng hợp trong nuôi thủy sản",
            "meaning": "Lấy phòng bệnh làm biện pháp chủ động tiên quyết: Giữ môi trường sạch, sử dụng giống kiểm dịch âm tính, bồi dưỡng dinh dưỡng tăng cường miễn dịch và tuyệt đối cách ly khi có mầm bệnh phát sinh.",
            "example": "Trước khi thả giống tôm, vét bùn đáy ao phơi nắng 7 - 10 ngày, khử trùng nguồn nước bằng iodine hoặc thuốc tím, định kỳ trộn vitamin C và beta-glucan vào thức ăn.",
            "essence": "Trị bệnh thủy sản trong môi trường nước chi phí rất tốn kém và hiệu quả thấp; phòng bệnh chủ động bảo toàn toàn bộ năng suất ao nuôi."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phát hiện ao nuôi tôm thẻ chân trắng có hiện tượng tôm nổi đầu tấp mé vào sáng sớm, đo oxy hòa tan thấy DO = 2.0 mg/L và nồng độ khí độc NH3 tăng cao. Hãy xử lý cấp cứu khẩn cấp.",
            "steps": [
              "Bước 1: Bật ngay toàn bộ hệ thống quạt nước và dàn sục khí oxy đáy công suất tối đa để khẩn cấp bù đắp lượng oxy thiếu hụt.",
              "Bước 2: Cắt giảm ngay 50 - 100% khẩu phần thức ăn bữa sáng để hạn chế tôm tiêu hao oxy tiêu hóa và tránh thức ăn dư thừa sinh thêm khí độc.",
              "Bước 3: Tạt oxy viên (Sodium percarbonate) tại các góc chết và mé ao nơi tôm tập trung dồn cục bộ.",
              "Bước 4: Cấp thêm nước sạch đã qua xử lý vào ao, đánh vi sinh phân hủy khí độc (chủng Nitrosomonas và Nitrobacter) kết hợp Zeolite hấp phụ khí độc đáy ao."
            ],
            "answer": "Quy trình cấp cứu: Tăng cường sục khí tối đa -> Giảm hoặc ngừng cho ăn -> Đánh oxy viên cấp cứu -> Cấp nước sạch và tạt chế phẩm vi sinh phân giải khí độc."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lạm dụng thuốc kháng sinh đổ tràn lan xuống ao nuôi khi thủy sản bỏ ăn hoặc có hiện tượng bất thường.",
            "why": "Kháng sinh tiêu diệt luôn hệ vi sinh vật có lợi của nguồn nước ao, làm bùng phát khí độc đáy ao, gây ra hiện tượng kháng kháng sinh nguy hiểm và tồn dư hóa chất khiến sản phẩm bị cấm xuất khẩu."
          }
        ]
      }
    ]
  },

  "mi-thuat": {
    "id": "mi-thuat",
    "name": "Mĩ thuật 12 - Điêu khắc, Đồ họa tranh in & Thiết kế sân khấu",
    "icon": "🎨",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Nghệ thuật điêu khắc và sắp đặt",
        "description": "Nghiên cứu khái quát về nghệ thuật điêu khắc hiện đại kết hợp nghệ thuật sắp đặt (Installation Art), cách khai thác ngôn ngữ hình khối, không gian ba chiều và vật liệu sẵn có (Found Objects) để biểu đạt thông điệp thẩm mĩ.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái quát về sắp đặt sản phẩm điêu khắc", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Sắp đặt sản phẩm điêu khắc bằng vật liệu sẵn có", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Nghệ thuật sắp đặt (Installation Art)",
            "definition": "Là hình thức nghệ thuật thị giác đương đại trong đó các tác phẩm điêu khắc hoặc vật thể được bố trí trong một không gian ba chiều cụ thể nhằm biến đổi nhận thức của người xem về không gian và môi trường tương tác đó.",
            "example": "Sắp đặt hàng trăm khối tượng người bằng đất nung kích thước nhỏ trong một căn phòng tràn ngập ánh sáng vàng và âm thanh gió rít để gợi cảm thức về sự cô đơn giữa xã hội hiện đại.",
            "essence": "Không gian trưng bày không đơn thuần là nơi chứa tác phẩm mà trở thành một phần cấu thành hữu cơ không thể tách rời của chính tác phẩm nghệ thuật."
          },
          {
            "term": "Vật liệu sẵn có (Found Objects)",
            "definition": "Những vật dụng đời thường, phế liệu công nghiệp, rác thải tái chế hoặc vật thể tự nhiên được nghệ sĩ lựa chọn, tái cấu trúc và gán cho một ý niệm thẩm mĩ mới mẻ trong tác phẩm sắp đặt.",
            "example": "Tái sử dụng các sợi dây đồng vụn, bánh răng đồng hồ hỏng và ống nhựa để tạo hình một cây cổ thụ cơ khí mô phỏng sự xung đột giữa công nghệ và tự nhiên.",
            "essence": "Biến đổi chức năng thực dụng nguyên bản của vật thể thành ngôn ngữ biểu tượng giàu sức gợi mở triết lý nhân sinh."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc tương tác không gian và thị giác trong nghệ thuật sắp đặt",
            "meaning": "Tác phẩm sắp đặt điêu khắc phải tạo ra một tuyến đường trải nghiệm thị giác và vận động cơ thể liền mạch cho người xem, kết hợp hài hòa tỷ lệ hình khối, ánh sáng bóng đổ và vật liệu.",
            "example": "Khi sắp đặt cụm tượng chủ đề 'Đô thị', bố trí các khối thẳng đứng vươn cao ở trung tâm, khoảng cách giữa các khối đủ rộng để người xem có thể đi len lỏi vào bên trong tác phẩm.",
            "essence": "Người xem không chỉ đứng quan sát từ xa mà chủ động bước vào bên trong, trở thành một phần của không gian nghệ thuật tương tác."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Thiết kế phác thảo ý tưởng một tác phẩm sắp đặt điêu khắc chủ đề 'Dấu ấn môi trường' sử dụng vật liệu phế liệu tái chế trong phòng triển lãm trường học.",
            "steps": [
              "Bước 1: Xác định thông điệp ý tưởng: Cảnh báo sự xâm lấn của rác thải nhựa vi mô đối với đại dương và nguồn sống sinh thái.",
              "Bước 2: Tuyển chọn và xử lý vật liệu sẵn có: Vỏ chai nhựa trong suốt, lưới đánh cá rách đã được làm sạch khử khuẩn, khung sắt phế liệu làm cốt đỡ chịu lực.",
              "Bước 3: Tạo hình điêu khắc: Uốn khung sắt tạo hình bộ xương một con cá voi khổng lồ dài 2m, bên trong bụng cá lèn chặt các chai lọ nhựa nhiều màu sắc.",
              "Bước 4: Sắp đặt không gian và ánh sáng: Treo bộ xương cá lơ lửng giữa phòng bằng dây cước trong suốt, chiếu đèn hắt ánh sáng xanh lam tạo ảo giác bơi dưới đáy biển sâu cùng âm thanh sóng vỗ nhẹ."
            ],
            "answer": "Tác phẩm kết hợp khung xương điêu khắc cá voi từ lưới sắt và rác nhựa bên trong lòng, sắp đặt lơ lửng cùng ánh sáng xanh gợi mở ý thức bảo vệ đại dương sâu sắc."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa việc 'sắp đặt nghệ thuật' với việc 'bày biện, xếp dọn đồ đạc ngẫu nhiên'.",
            "why": "Nghệ thuật sắp đặt đòi hỏi ý niệm thẩm mĩ rõ ràng, sự tính toán tỉ mỉ về tỉ lệ không gian, nhịp điệu ánh sáng và cảm xúc tương tác của người xem, không phải là gom đồ chất đống."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Đồ họa tranh in",
        "description": "Các kỹ thuật đồ họa tranh in truyền thống và hiện đại: In nổi (gỗ, cao su), in lõm (khắc kim loại), in phẳng (độc bản monotype) và quy trình sáng tạo bản in độc bản giàu giá trị hội họa.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Kỹ thuật in nổi và in lõm — Khái quát tranh in độc bản", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành sáng tạo tác phẩm tranh in độc bản và nhiều bản", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tranh in độc bản (Monotype)",
            "definition": "Là thể loại tranh in trung gian độc đáo giữa đồ họa và hội họa, trong đó họa sĩ tạo hình trực tiếp bằng màu mực trên bề mặt không thấm nước (kính, mica, tấm kim loại) rồi ép sang giấy để tạo ra một bản in duy nhất không thể sao chép y hệt lần thứ hai.",
            "example": "Vẽ tranh phong cảnh hoàng hôn bằng sơn dầu trên tấm mica bóng, dùng khăn mềm và que tre gạt sáng, sau đó đặt giấy can ẩm lên ép lăn bằng con lăn tay để truyền mực sang giấy.",
            "essence": "Mỗi bản in là độc bản mang những hiệu ứng loang màu, xước hạt ngẫu nhiên kỳ thú mà kỹ thuật vẽ bút lông trực tiếp không thể tạo ra được."
          },
          {
            "term": "Nguyên lý kỹ thuật in nổi và in lõm",
            "definition": "In nổi là kỹ thuật mực bám vào các phần gờ nổi nhô cao trên bề mặt chế bản (phần lõm đã bị đục khoét bỏ); ngược lại in lõm là kỹ thuật mực được chà lèn sâu vào các rãnh chìm được khắc axit hoặc kim nhọn tạo nên.",
            "example": "Tranh khắc gỗ dân gian Đông Hồ là ví dụ điển hình của in nổi; trong khi tranh khắc kim loại kẽm Etching là đỉnh cao của kỹ thuật in lõm tinh xảo.",
            "essence": "Sự đối lập vị trí giữ mực (nổi hay lõm) quyết định tính chất đường nét, độ sắc bén và mật độ phân bố sắc độ trên trang giấy in."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc đảo ngược hình ảnh và lực ép trong đồ họa in ấn",
            "meaning": "Mọi hình vẽ, chữ viết khắc trên chế bản khi in ra giấy sẽ bị lật ngược gương theo trục dọc; do đó khi tạo bản in cần vẽ phác ngược lại hình mong muốn, đồng thời lực ép của máy lăn phải đồng đều khắp mặt giấy.",
            "example": "Khi khắc bản tranh in có chữ khẩu hiệu, người khắc phải vẽ và đục chữ theo chiều lộn ngược từ phải qua trái để khi in ra giấy chữ hiển thị xuôi chiều đọc bình thường.",
            "essence": "Tư duy đảo ngược thị giác là phẩm chất tiên quyết của người nghệ sĩ đồ họa tạo hình."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày 4 bước thực hiện một bức tranh in độc bản chân dung trên tấm mi-ca bằng màu acrylic kết hợp kỹ thuật gạt sáng.",
            "steps": [
              "Bước 1: Chuẩn bị mặt in: Làm sạch và lau khô bề mặt tấm mi-ca kích thước A4, đặt bản vẽ nét phác thảo chân dung lót dưới tấm mi-ca để làm cữ định vị.",
              "Bước 2: Phủ màu nền: Dùng con lăn phủ đều một lớp màu acrylic nền mỏng lên mặt trên của tấm mi-ca.",
              "Bước 3: Khắc họa và gạt sáng (Tạo hình âm bản): Dùng tăm bông, bay vẽ hoặc giẻ mềm lau bớt lớp màu ướt ở các vị trí bắt sáng trên khuôn mặt (sống mũi, trán, gò má), dùng bút lông thêm các nét chi tiết đậm cho mắt, tóc.",
              "Bước 4: In ép chuyển giao: Đặt nhẹ nhàng tờ giấy vẽ chuyên dụng lên mặt mi-ca, dùng con lăn tay hoặc mu bàn tay chà miết đều lực từ giữa ra ngoài mép rồi từ từ bóc tách tờ giấy."
            ],
            "answer": "Quy trình in độc bản gồm: Chuẩn bị mặt mi-ca -> Phủ màu nền -> Gạt sáng tạo hình chi tiết -> Đặt giấy ép miết đều lực và bóc bản in."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Để lớp sơn màu trên tấm mi-ca bị khô hoàn toàn trước khi đặt giấy lên ép in.",
            "why": "Khi màu acrylic đã khô đóng màng polymer, mực màu không còn khả năng bám dính truyền dịch chuyển sang thớ giấy, khiến bản in bị trắng hoặc loang lổ loang lấm."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Thiết kế mĩ thuật sân khấu và điện ảnh",
        "description": "Nghiên cứu nguyên lý không gian phối cảnh sân khấu, nghệ thuật tạo hình trang phục biểu diễn và phục trang điện ảnh, thiết kế đạo cụ và ứng dụng công nghệ nghệ thuật nghe nhìn hiện đại.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khái quát về thiết kế trang phục và không gian nghệ thuật biểu diễn", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành thiết kế bối cảnh sân khấu và phục trang điện ảnh từ vật liệu sẵn có", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thiết kế phục trang nghệ thuật (Costume Design)",
            "definition": "Là công việc sáng tạo trang phục cho diễn viên trong sân khấu hoặc điện ảnh nhằm khắc họa tính cách, nghề nghiệp, địa vị xã hội, tâm lý và bối cảnh lịch sử thời đại của nhân vật kịch bản.",
            "example": "Thiết kế bộ trang phục áo quan triều đình thời Trần với chất liệu gấm thô, hoa văn rồng uốn khúc mộc mạc khác biệt hoàn toàn với trang phục cung đình thời Nguyễn rực rỡ vàng kim.",
            "essence": "Khác với thời trang thương mại phục vụ đời sống, phục trang nghệ thuật phục vụ tuyệt đối cho việc xây dựng tính cách kịch và thế giới quan của bộ phim."
          },
          {
            "term": "Không gian phối cảnh sân khấu (Stage Scenography)",
            "definition": "Nghệ thuật tổ chức không gian ba chiều của sàn diễn bao gồm phông màn, cánh gà, bục bệ đạo cụ và ánh sáng nhằm kiến tạo môi trường sống và hoạt động chân thực của nhân vật trong vở diễn.",
            "example": "Sử dụng các bục nghiêng nhiều tầng bậc kết hợp hiệu ứng đèn chiếu ngược để tạo nên cảm giác hiểm trở của trận địa biên cương trong một vở kịch lịch sử.",
            "essence": "Không gian sân khấu mở ra một thế giới ước lệ nơi thời gian và khoảng cách địa lý được cô đọng bằng ngôn ngữ mĩ thuật biểu trưng."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc đồng bộ phong cách mĩ thuật sân khấu và điện ảnh",
            "meaning": "Mọi yếu tố mĩ thuật từ thiết kế bối cảnh, phục trang nhân vật, đạo cụ cầm tay đến ánh sáng màu sắc phải thống nhất tuyệt đối theo ý đồ dàn dựng của đạo diễn và thông điệp tư tưởng của kịch bản.",
            "example": "Trong một vở kịch hiện thực tâm lý u ám, phục trang của nhân vật không được dùng tông màu dạ quang rực rỡ đối chọi với phông nền xám xịt trừ khi có chủ ý tương phản biểu tượng.",
            "essence": "Mĩ thuật sân khấu điện ảnh là nghệ thuật tổng hợp, vẻ đẹp của từng chi tiết phải tôn vinh tổng thể câu chuyện kịch."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Lập bảng phác thảo thiết kế tạo hình trang phục cho nhân vật 'Chị Dậu' trong trích đoạn kịch 'Tắt đèn' của Ngô Tất Tố biểu diễn tại trường học.",
            "steps": [
              "Bước 1: Phân tích bối cảnh và tính cách nhân vật: Người phụ nữ nông dân nghèo khổ cùng quẫn trước cách mạng, tần tảo, chịu thương chịu khó nhưng kiên cường bảo vệ gia đình.",
              "Bước 2: Lựa chọn phom dáng trang phục: Áo tứ thân may bằng vải thô nhuộm màu nâu sồng bạc phếch, vạt áo buộc túm gọn gàng trước bụng biểu thị sự nhanh nhẹn tần tảo; quần thô đen cạp túm.",
              "Bước 3: Chi tiết điểm nhấn (Aging - Đánh cũ phục trang): Dùng giấy ráp mài mòn các mép tay áo và gấu quần, tạo vài miếng vá chắp khác màu ở vai áo để lột tả cảnh nghèo túng; vấn khăn nhung đen cũ trên đầu.",
              "Bước 4: Đạo cụ bổ trợ: Đôi guốc mộc cũ hoặc đi chân đất lấm lem bùn đất, quang gánh tre mộc mạc."
            ],
            "answer": "Bản thiết kế gồm áo tứ thân nâu bạc có miếng vá, quần đen vải thô, khăn vấn đầu cũ và chi tiết chân đất lấm lem thể hiện trọn vẹn số phận người nông dân bần cùng chịu áp bức."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Thiết kế trang phục sân khấu giống hệt quần áo thời trang dạ hội lộng lẫy mà không quan tâm đến tính cách và hoàn cảnh nghèo đói của nhân vật trong kịch bản.",
            "why": "Phục trang nghệ thuật phải phục vụ tính cách kịch; trang phục quá mới, bóng bẩy xa rời thực tế sẽ phá hủy hoàn toàn niềm tin thị giác của khán giả vào số phận nhân vật."
          }
        ]
      }
    ]
  },

  "giao-duc-the-chat": {
    "id": "giao-duc-the-chat",
    "name": "Giáo dục thể chất 12 - Thể thao tự chọn & Rèn luyện thể lực",
    "icon": "⚽",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Sử dụng yếu tố tự nhiên và dinh dưỡng rèn luyện thể chất",
        "description": "Nghiên cứu phương pháp sử dụng có khoa học các yếu tố tự nhiên (không khí, ánh nắng mặt trời, nước, địa hình tự nhiên) và chế độ dinh dưỡng thể thao để phục hồi thể lực và nâng cao sức đề kháng cơ thể.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sử dụng các yếu tố tự nhiên để rèn luyện sức khoẻ và phát triển thể lực", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Dinh dưỡng thể thao và các biện pháp phục hồi sau vận động", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Rèn luyện bằng yếu tố tự nhiên",
            "definition": "Là việc tận dụng có kế hoạch các tác nhân vật lý của tự nhiên như không khí trong lành (tắm không khí, hít thở sâu), ánh nắng mặt trời (tắm nắng hấp thụ vitamin D) và nước (tắm nước mát, bơi lội) nhằm rèn luyện cơ chế điều nhiệt và nâng cao khả năng thích ứng của cơ thể.",
            "example": "Tập bài hít thở sâu ngoài trời thoáng khí vào sáng sớm (nhịp 1 hít sâu bằng mũi 4 - 5 giây, nhịp 2 thở hết bằng miệng 5 - 6 giây) giúp tăng dung tích sống của phổi và giảm căng thẳng thần kinh.",
            "essence": "Tận dụng nguồn năng lượng tự nhiên miễn phí để tôi luyện sức chịu đựng của cơ thể trước sự biến đổi thất thường của thời tiết."
          },
          {
            "term": "Bù nước và dinh dưỡng phục hồi sau vận động",
            "definition": "Quy trình bổ sung kịp thời lượng nước, chất điện giải (Na+, K+) và năng lượng (Carbohydrate hấp thu nhanh, Protein phục hồi cơ) bị tiêu hao trong quá trình luyện tập thể thao cường độ cao.",
            "example": "Sau buổi tập bóng đá kéo dài 60 phút, uống từng ngụm nhỏ nước điện giải oresol hoặc nước dừa tươi, sau đó trong vòng 30 - 45 phút ăn nhẹ một quả chuối chín cùng sữa chua để tái tạo glycogen cơ bắp.",
            "essence": "Cửa sổ phục hồi 30 phút sau vận động là thời điểm vàng để cơ bắp hấp thu dưỡng chất sửa chữa các vi tổn thương mô cơ."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc an toàn khi tắm nắng và rèn luyện ngoài trời",
            "meaning": "Chỉ tắm nắng rèn luyện vào sáng sớm khi cường độ tia tử ngoại UV ở mức an toàn (trước 8 giờ sáng mùa hè); tuyệt đối không tập luyện dưới ánh nắng gay gắt giữa trưa để tránh say nắng, sốc nhiệt và tổn thương da.",
            "example": "Thời gian tắm nắng ban đầu từ 5 - 10 phút, sau tăng dần lên 20 - 30 phút; đội mũ rộng vành che đầu và uống đủ nước trước khi ra nắng.",
            "essence": "Đúng thời điểm mang lại sức khỏe dồi dào; sai thời điểm biến ánh nắng thành tác nhân gây hại nghiêm trọng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xây dựng kế hoạch phục hồi thể lực 3 bước cho học sinh lớp 12 sau khi hoàn thành bài kiểm tra chạy cự ly 1.500m.",
            "steps": [
              "Bước 1: Hồi tĩnh tích cực (Cool-down): Không ngồi sụp xuống đất ngay mà đi bộ thả lỏng nhẹ nhàng từ 3 - 5 phút, kết hợp lắc nhẹ cơ bắp đùi bắp chân và hít thở sâu điều hòa nhịp tim hạ dần.",
              "Bước 2: Căng cơ tĩnh (Static Stretching): Thực hiện các động tác giãn cơ bắp chân, cơ đùi trước và cơ đùi sau mỗi tư thế giữ yên 15 - 20 giây để giảm co thắt và giải phóng axit lactic tồn đọng.",
              "Bước 3: Bù nước và năng lượng: Uống 200 - 300 ml nước bù khoáng điện giải từng ngụm nhỏ ở nhiệt độ mát (15 - 20 độ C), ăn nhẹ một mẩu bánh mì kèm chuối sau khi nhịp thở trở về bình thường."
            ],
            "answer": "Kế hoạch phục hồi gồm: Đi bộ hồi tĩnh -> Căng cơ giải tỏa axit lactic -> Bổ sung nước điện giải và carbohydrate hấp thu nhanh."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Ngồi thụp xuống đất hoặc uống ừng ực một chai nước đá lạnh buốt ngay khi vừa cán đích chạy cự ly dài.",
            "why": "Ngồi sụp xuống đột ngột làm máu ứ đọng ở chi dưới gây thiếu máu não tạm thời dẫn đến hoa mắt choáng váng; uống nước đá lạnh gây co thắt mạch dạ dày và viêm họng cấp."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Kỹ thuật bóng đá và bóng rổ nâng cao",
        "description": "Các kỹ thuật phối hợp nhóm nâng cao, chiến thuật tấn công và phòng thủ phản công nhanh, nguyên lý bọc lót trong bóng đá và luật thi đấu bóng rổ 3x3 chính thức của FIBA.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Kỹ thuật phối hợp nhóm và phòng thủ bọc lót trong bóng đá", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Chiến thuật tấn công nhanh và luật thi đấu bóng rổ 3x3 nâng cao", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Phòng thủ bọc lót (Covering / Mutual Support)",
            "definition": "Chiến thuật phối hợp phòng ngự trong bóng đá, trong đó một cầu thủ áp sát tranh chấp trực diện cản trở đối phương dẫn bóng, cầu thủ thứ hai đứng chéo góc giữ cự ly hợp lý phía sau sẵn sàng can thiệp nếu đồng đội bị vượt qua.",
            "example": "Khi trung vệ dâng lên kèm sát tiền đạo đối phương, hậu vệ cánh lập tức bó vào trong tạo thành cự ly bọc lót 3 - 5m bịt kín khoảng trống khe hở sau lưng.",
            "essence": "Nguyên lý phòng ngự chiều sâu: Không bao giờ để cầu thủ kèm người rơi vào thế đơn độc một chọi một không có sự hỗ trợ."
          },
          {
            "term": "Chiến thuật tấn công nhanh (Fast Break) trong bóng rổ 3x3",
            "definition": "Chiến thuật chuyển đổi trạng thái cực nhanh từ phòng thủ sang tấn công ngay khi đoạt được bóng bật bảng (rebound) hoặc cướp bóng, đưa bóng ra ngoài vạch 2 điểm và dứt điểm ghi điểm trước khi đối phương kịp ổn định đội hình.",
            "example": "Sau khi đồng đội bắt bóng bật bảng phòng thủ, lập tức chuyền nhanh ra ngoài vạch bán nguyệt 6.75m cho đồng đội đang di chuyển trống trải ném rổ ghi 2 điểm hoặc đột phá lên rổ.",
            "essence": "Thời gian tấn công trong bóng rổ 3x3 chỉ có 12 giây; tốc độ chuyển đổi và tính quyết đoán là chìa khóa chiến thắng."
          }
        ],
        "rules": [
          {
            "statement": "Luật thời gian 12 giây tấn công trong bóng rổ 3x3 FIBA",
            "meaning": "Đội kiểm soát bóng phải thực hiện một cú ném bóng chạm vào vành rổ trong vòng 12 giây; nếu hết 12 giây mà bóng chưa rời tay ném hoặc chưa chạm vành thì bị tính lỗi và mất quyền kiểm soát bóng cho đối phương.",
            "example": "Đồng hồ hiển thị còn 3 giây, cầu thủ cầm bóng bắt buộc phải thực hiện ngay cú ném rổ hoặc chuyền cho đồng đội dứt điểm gấp thay vì tiếp tục nhồi bóng câu giờ.",
            "essence": "Luật buộc trận đấu diễn ra với tốc độ rất cao, liên tục và hấp dẫn kịch tính đến giây cuối cùng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích tình huống phối hợp 2 đánh 1 (bật tường một - hai, Give and Go) để vượt qua một hậu vệ đối phương trong bóng đá.",
            "steps": [
              "Bước 1: Cầu thủ A dẫn bóng trực diện thu hút hậu vệ đối phương lao vào tranh chấp, quan sát thấy đồng đội B đang đứng ở cự ly 5 - 7m chếch một bên.",
              "Bước 2: Cầu thủ A chuyền sệt một chạm chuẩn xác cho B, đồng thời lập tức bứt tốc độ cao chạy vòng ra sau lưng hậu vệ vượt qua khoảng trống.",
              "Bước 3: Cầu thủ B nhận bóng không giữ bóng mà thực hiện ngay đường chuyền một chạm chuẩn xác vừa tầm vào đà di chuyển của A.",
              "Bước 4: Cầu thủ A nhận bóng đối mặt với thủ môn đối phương và tung cú dứt điểm vào góc xa."
            ],
            "answer": "Chiến thuật bật tường 1-2 loại bỏ hoàn toàn hậu vệ nhờ yếu tố chuyền một chạm nhanh kết hợp bứt tốc độ vào khoảng trống sau lưng đối thủ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Trong bóng rổ 3x3, sau khi cướp được bóng từ đối thủ trong khu vực cấm địa lại ném rổ ngay mà không chuyền hoặc dẫn bóng ra ngoài vạch 2 điểm.",
            "why": "Theo luật bóng rổ 3x3, khi đổi quyền kiểm soát bóng bên trong vạch, đội phòng thủ trở thành tấn công bắt buộc phải dẫn bóng hoặc chuyền bóng ra ngoài vạch 6.75m mới được phép ném rổ hợp lệ; ném ngay sẽ không được tính điểm."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Kỹ thuật cầu lông và bóng chuyền nâng cao",
        "description": "Các kỹ thuật đập cầu hiểm hóc, kỹ thuật phòng thủ cứu cầu sân sau trong cầu lông và chiến thuật phối hợp thi đấu đôi ăn ý, phối hợp đệm bóng chuyền bước một và đập bóng tấn công trên lưới.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Kỹ thuật đập cầu thuận tay và phòng thủ sân sau trong cầu lông", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Chiến thuật phối hợp đánh đôi trong cầu lông và phối hợp tấn công bóng chuyền", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Kỹ thuật đập cầu thuận tay (Forehand Smash)",
            "definition": "Đòn tấn công chủ lực có tốc độ bay nhanh nhất trong cầu lông, vận động viên nhảy lên cao đón cầu ở điểm cao nhất phía trước trán, gập mạnh cổ tay kết hợp xoay lườn đánh cầu cắm nhanh xuống phần sân đối phương.",
            "example": "Khi đối thủ hất cầu bổng non giữa sân, bước lùi đón cầu, bật nhảy co chân trên không và dồn toàn lực vung vợt đập quả cầu cắm sát vạch biên dọc sân đối diện.",
            "essence": "Điểm tiếp xúc cầu cao nhất mang lại góc đập cắm hiểm hóc và quỹ đạo bóng không thể cản phá."
          },
          {
            "term": "Chiến thuật phối hợp đôi trước - sau và song song trong cầu lông",
            "definition": "Quy tắc di chuyển vị trí trong đánh đôi: Khi đội mình tấn công đập cầu thì chuyển sang thế Trước - Sau (một người canh lưới chớp thời cơ, một người ở sân sau đập cầu liên tục); khi bị đối phương tấn công thì chuyển sang thế Song song ngang sân để bao quát hai góc phòng ngự.",
            "example": "Khi cầu thủ sân sau tung cú đập cầu, đồng đội lập tức di chuyển lên áp sát lưới để đón bắt quả cầu ve lưới non của đối thủ.",
            "essence": "Linh hoạt hoán đổi đội hình công - thủ nhịp nhàng triệt tiêu điểm mù và không gian trống trên sân."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc tiếp xúc cầu trên lưới trong luật thi đấu cầu lông BWF",
            "meaning": "Vợt của người chơi không được chạm lưới hoặc xâm phạm qua phần sân đối phương khi cầu chưa bay qua mặt lưới; cầu phải bay qua phía trên lưới vào sân đối phương mới được phép thực hiện cú đánh.",
            "example": "Khi đối thủ bỏ nhỏ sát mép lưới, người đập chặn lưới vung vợt chạm vào dây cáp lưới trên sẽ bị trọng tài thổi phạt lỗi chạm lưới (Fault) mất điểm.",
            "essence": "Đảm bảo tính công bằng và an toàn tuyệt đối tránh va chạm thân thể giữa các vận động viên qua lưới ngăn cách."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày 4 giai đoạn cơ bản của kỹ thuật đập cầu thuận tay (Smash) uy lực trong cầu lông.",
            "steps": [
              "Bước 1: Chuẩn bị và di chuyển: Phán đoán điểm rơi cầu bổng của đối phương, nhanh chóng di chuyển lùi chân thuận về sau, vai hướng về phía lưới, trọng tâm dồn lên chân sau.",
              "Bước 2: Giương vợt đón cầu: Nâng hai tay giữ thăng bằng, tay cầm vợt đưa ra sau gáy, mở rộng ngực, mắt tập trung cao độ vào quả cầu đang rơi trước trán.",
              "Bước 3: Vung vợt tiếp xúc cầu: Bật nhảy hoặc đạp mạnh chân sau xoay lườn ra trước, vung vợt theo quỹ đạo từ sau ra trước lên cao, tiếp xúc cầu ở điểm cao nhất hơi chếch phía trước mặt với mặt vợt nghiêng chúc xuống, gập nhanh cổ tay tạo lực bộc phát.",
              "Bước 4: Kết thúc và hồi vị: Vợt theo quán tính chéo xuống hông bên chân nghịch, chân sau bước lên tiếp đất giữ thăng bằng và ngay lập tức trở về tư thế sẵn sàng đón đường trả cầu tiếp theo."
            ],
            "answer": "Quy trình đập cầu: Di chuyển chọn vị trí -> Giương vợt mở lườn -> Bật nhảy đập cầu tại điểm cao nhất gập cổ tay -> Vung vợt theo quán tính và hồi vị về trung tâm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đập cầu khi điểm tiếp xúc cầu ở quá sâu phía sau đầu lưng hoặc chỉ dùng lực bắp tay mà không sử dụng lực gập cổ tay và xoay lườn.",
            "why": "Cầu rơi sau đầu làm đường cầu bay bổng ra ngoài sân hoặc rúc lưới; không dùng lực cổ tay và xoay lườn khiến cú đập bị yếu, thiếu tốc độ và nhanh mỏi cơ khớp vai."
          }
        ]
      }
    ]
  }
}

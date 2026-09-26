# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa 5 môn Năng khiếu, Ứng dụng & Hướng nghiệp Lớp 10 SGK Kết nối tri thức 2026-2027:
- Công nghệ 10 (4 chương trọng tâm: Đại cương công nghệ, Vẽ kỹ thuật, Thiết kế kỹ thuật, Công nghệ trồng trọt)
- Hoạt động trải nghiệm, Hướng nghiệp 10 (4 chủ đề mạch nội dung: Bản thân, Xã hội, Môi trường, Hướng nghiệp)
- Âm nhạc 10 (4 chủ đề: Giai điệu quê hương, Kĩ thuật thanh nhạc, Thưởng thức âm nhạc, Giai điệu bốn phương)
- Mĩ thuật 10 (4 chủ đề: Nghệ thuật hội họa, Điêu khắc tạo hình, Nghệ thuật kiến trúc, Thiết kế đồ họa)
- Giáo dục Thể chất 10 (5 chủ đề: Thể lực & dinh dưỡng, Điền kinh, Bóng đá, Cầu lông/Bóng rổ, Phòng chống chấn thương)
"""

true = True
false = False
null = None

APPLIED_SUBJECTS = {
  "cong-nghe": {
    "id": "cong-nghe",
    "name": "Công nghệ",
    "icon": "⚙️",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chương 1: Đại cương về công nghệ",
        "description": "Bản chất của kỹ thuật và công nghệ, hệ thống kỹ thuật, các công nghệ phổ biến, đánh giá công nghệ và tác động của Cách mạng công nghiệp 4.0.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Công nghệ và đời sống — Hệ thống kỹ thuật", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Một số công nghệ mới và Cách mạng công nghiệp 4.0", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hệ thống kỹ thuật",
            "definition": "Là một hệ thống bao gồm các phần tử đầu vào, phần tử xử lý và phần tử đầu ra liên kết chặt chẽ nhằm thực hiện một nhiệm vụ công nghệ xác định.",
            "example": "Hệ thống máy điều hòa không khí: Đầu vào là điện năng và nhiệt độ cài đặt, phần xử lý là mạch điều khiển và máy nén, đầu ra là luồng khí lạnh ổn định.",
            "essence": "Mọi cỗ máy hay dây chuyền phức tạp đều tuân thủ nguyên lý chu trình hệ thống: Nhận dữ liệu/năng lượng -> Biến đổi -> Cung cấp giá trị đầu ra."
          },
          {
            "term": "Công nghệ mới trong Cách mạng công nghiệp 4.0",
            "definition": "Tập hợp các công nghệ mang tính đột phá dựa trên nền tảng kỹ thuật số và kết nối vạn vật như: Trí tuệ nhân tạo (AI), Internet vạn vật (IoT), In 3D (Additive Manufacturing), và Tự động hóa thông minh.",
            "example": "Nhà máy thông minh sử dụng cánh tay robot kết nối cảm biến IoT để tự động lắp ráp linh kiện và kiểm tra lỗi bằng thị giác máy tính AI.",
            "essence": "Bản chất của CMCN 4.0 là xóa nhòa ranh giới giữa thế giới vật lý, kỹ thuật số và sinh học thông qua kết nối dữ liệu liên tục theo thời gian thực."
          }
        ],
        "rules": [
          {
            "statement": "Tiêu chí toàn diện đánh giá công nghệ",
            "meaning": "Đánh giá công nghệ phải kết hợp hài hòa 4 yếu tố then chốt: Hiệu quả kỹ thuật, Hiệu quả kinh tế, Tính an toàn cho con người và Tính bền vững với môi trường.",
            "example": "Khi lựa chọn công nghệ phát điện, không chỉ xem xét giá thành kilowatt-giờ rẻ mà phải đánh giá mức phát thải carbon và rủi ro môi trường sống xung quanh.",
            "essence": "Công nghệ tiến bộ đích thực là công nghệ phục vụ hạnh phúc con người và không đánh đổi tương lai sinh thái của Trái đất."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích cấu trúc hệ thống kỹ thuật của hệ thống tưới nước tự động trong nông nghiệp công nghệ cao.",
            "steps": [
              "Bước 1: Xác định phần tử đầu vào: Cảm biến độ ẩm đất đo đạc tín hiệu, nguồn nước và nguồn điện năng cấp cho máy bơm.",
              "Bước 2: Xác định phần tử xử lý: Vi điều khiển trung tâm (Arduino/PLC) so sánh độ ẩm thực tế với ngưỡng cài đặt chuẩn.",
              "Bước 3: Xác định phần tử đầu ra: Rơ-le kích hoạt van điện từ mở nước tưới nhỏ giọt khi đất khô và tự động ngắt khi đủ ẩm."
            ],
            "answer": "Hệ thống khép kín gồm Cảm biến -> Bộ vi xử lý -> Cơ cấu chấp hành bơm tưới, đảm bảo tiết kiệm nước tối ưu."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đồng nhất khái niệm 'Khoa học' và 'Công nghệ'.",
            "why": "Khoa học là tìm tòi khám phá các quy luật khách quan của tự nhiên (trả lời câu hỏi TẠI SAO?), còn Công nghệ là ứng dụng tri thức khoa học để tạo ra sản phẩm phục vụ con người (trả lời câu hỏi LÀM THẾ NÀO?)."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chương 2: Vẽ kỹ thuật và Biểu diễn vật thể",
        "description": "Bản vẽ kỹ thuật, tiêu chuẩn trình bày bản vẽ, các phương pháp chiếu: hình chiếu vuông góc, hình cắt, mặt cắt, hình chiếu trục đo và hình chiếu phối cảnh.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phương pháp hình chiếu vuông góc và hình cắt", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Hình chiếu trục đo và bản vẽ cơ khí", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hình chiếu vuông góc",
            "definition": "Là hình biểu diễn nhận được từ phép chiếu vuông góc các điểm của vật thể lên mặt phẳng hình chiếu (hình chiếu đứng, hình chiếu bằng, hình chiếu cạnh).",
            "example": "Khi nhìn thẳng từ trước vào khối lập phương có khoét rãnh, hình chiếu đứng cho biết chiều dài và chiều cao cùng vị trí rãnh khoét.",
            "essence": "Biến không gian 3 chiều của vật thể thực thành các mặt phẳng 2 chiều chính xác tuyệt đối để chế tạo chuẩn xác."
          },
          {
            "term": "Hình cắt và Mặt cắt",
            "definition": "Hình cắt là hình biểu diễn phần vật thể còn lại sau khi tưởng tượng dùng mặt phẳng cắt cắt bỏ phần vật thể ở giữa người quan sát và mặt phẳng cắt.",
            "example": "Cắt đôi một ống lót kim loại để quan sát rõ bậc ren trong và lỗ trụ rỗng mà các đường nét đứt thông thường khó diễn tả rõ ràng.",
            "essence": "Hình cắt giúp người thợ nhìn thấu cấu trúc rỗng bên trong chi tiết mà không bị nhầm lẫn giữa các đường bao khuất."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc bố trí các hình chiếu vuông góc trên bản vẽ kỹ thuật",
            "meaning": "Hình chiếu bằng đặt ngay phía dưới hình chiếu đứng; Hình chiếu cạnh đặt ngay bên phải hình chiếu đứng theo phương chiếu góc thứ nhất.",
            "example": "Kích thước chiều rộng của vật thể phải gióng thẳng hàng chính xác tuyệt đối giữa hình chiếu bằng và hình chiếu cạnh thông qua đường gióng 45 độ.",
            "essence": "Sự thống nhất vị trí gióng hình đảm bảo ngôn ngữ kỹ thuật được hiểu đồng nhất trên toàn cầu mà không cần chú thích chữ."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu các bước lập bản vẽ hình chiếu vuông góc của một giá chữ L có lỗ trụ đứng.",
            "steps": [
              "Bước 1: Chọn hướng chiếu chính (từ trước) phản ánh rõ nhất hình dạng giá chữ L làm hình chiếu đứng.",
              "Bước 2: Gióng từ trên xuống để vẽ hình chiếu bằng, thể hiện chiều rộng và vị trí tâm lỗ tròn bằng nét gạch chấm mảnh.",
              "Bước 3: Gióng sang phải để vẽ hình chiếu cạnh, dùng nét đứt mảnh biểu diễn đường biên của lỗ rỗng bị khuất."
            ],
            "answer": "Bản vẽ hoàn chỉnh gồm 3 hình chiếu gióng thẳng hàng, có đầy đủ đường kích thước và khung tên tiêu chuẩn TCVN."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Dùng sai nét vẽ: Vẽ đường bao khuất bằng nét liền đậm thay vì nét đứt mảnh.",
            "why": "Nét liền đậm chỉ dành cho đường bao thấy. Mọi cạnh khuất bên trong bắt buộc phải vẽ bằng nét đứt mảnh (độ dày khoảng 1/2 nét đậm)."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chương 3: Thiết kế kỹ thuật và Sáng chế",
        "description": "Bản chất của thiết kế kỹ thuật, quy trình thiết kế kỹ thuật 5 bước, phương pháp tư duy sáng tạo trong sáng chế và thực hiện dự án thiết kế đơn giản.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Quy trình thiết kế kỹ thuật và giải quyết vấn đề", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Tư duy sáng tạo và thực hành dự án thiết kế", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quy trình thiết kế kỹ thuật",
            "definition": "Là chuỗi các hoạt động có hệ thống từ xác định vấn đề, đề xuất giải pháp, thiết kế chi tiết, chế tạo thử nghiệm cho đến đánh giá và hoàn thiện sản phẩm.",
            "example": "Thiết kế giá đỡ điện thoại thông minh: Khảo sát góc nhìn người dùng -> Phác thảo bản vẽ -> Cắt laser mô hình gỗ thử nghiệm -> Điều chỉnh độ nghiêng vững chắc.",
            "essence": "Thiết kế kỹ thuật là cầu nối biến ý tưởng sáng tạo trên giấy thành sản phẩm hữu hình phục vụ đời sống một cách tối ưu."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc thử nghiệm lặp (Iteration Principle)",
            "meaning": "Nếu sản phẩm thử nghiệm chưa đạt các tiêu chí đặt ra ban đầu, bắt buộc phải quay lại bước đề xuất giải pháp hoặc chỉnh sửa thiết kế chi tiết.",
            "example": "Một robot dò đường bị lật khi rẽ gấp đòi hỏi hạ thấp trọng tâm và viết lại thuật toán phanh trước khi sản xuất hàng loạt.",
            "essence": "Thất bại trong thử nghiệm là nguồn dữ liệu quý giá nhất để tối ưu hóa thiết kế kỹ thuật."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xác định 5 bước cơ bản của quy trình thiết kế giá để sách treo tường tiết kiệm không gian.",
            "steps": [
              "Bước 1: Xác định yêu cầu: Giá sách chịu lực 15kg, gắn tường không rung lắc, tận dụng góc chết của phòng học.",
              "Bước 2: Tìm kiếm giải pháp: Khảo sát mẫu giá nan gỗ, khung sắt tam giác chịu lực.",
              "Bước 3: Thiết kế chi tiết: Vẽ bản vẽ 2D/3D kích thước 800x250x300mm, tính toán độ võng.",
              "Bước 4: Chế tạo mẫu thử: Lắp ghép gỗ ép và bắt vít nở vào tường thử tải.",
              "Bước 5: Thử nghiệm & Đánh giá: Đặt 20 cuốn sách kiểm tra độ cong vênh và hoàn thiện lớp sơn chống ẩm."
            ],
            "answer": "Hoàn thành sản phẩm đạt chuẩn an toàn, thẩm mỹ và công năng sử dụng theo đúng 5 bước thiết kế kỹ thuật."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Bắt tay vào gia công chế tạo ngay mà không qua bước phác thảo bản vẽ và tính toán độ bền.",
            "why": "Thiếu bản vẽ kỹ thuật sẽ dẫn đến sai lệch kích thước, hao phí vật liệu và kết cấu không đảm bảo an toàn chịu lực."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chương 4: Công nghệ trồng trọt và Nông nghiệp công nghệ cao",
        "description": "Vai trò của trồng trọt, thành phần và tính chất của đất trồng, phân bón và dinh dưỡng cây trồng, kỹ thuật bảo vệ thực vật và mô hình nông nghiệp thông minh.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Đất trồng và dinh dưỡng khoáng cho cây trồng", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Ứng dụng công nghệ cao trong trồng trọt và bảo vệ mùa màng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Độ phì nhiêu của đất",
            "definition": "Là khả năng của đất cung cấp đồng thời và liên tục nước, chất dinh dưỡng, không khí cho cây trồng sinh trưởng và phát triển đạt năng suất cao.",
            "example": "Đất phù sa bồi tụ ven sông có cấu trúc hạt tơi xốp, giữ ẩm tốt và giàu mùn dinh dưỡng tự nhiên.",
            "essence": "Đất không chỉ là giá thể nâng đỡ rễ cây mà là một hệ sinh thái sống phức hợp gồm khoáng chất, chất hữu cơ và vi sinh vật có ích."
          },
          {
            "term": "Nông nghiệp công nghệ cao",
            "definition": "Là nền nông nghiệp ứng dụng các thành tựu khoa học công nghệ tiên tiến (nhà màng thông minh, tưới tự động hồi lưu, thủy canh, cảm biến khí hậu) nhằm tăng năng suất và bảo vệ môi trường.",
            "example": "Trồng dâu tây trong nhà kính điều khiển bằng máy tính tại Đà Lạt: Năng suất gấp 3 lần trồng truyền thống ngoài trời và hoàn toàn sạch sâu bệnh.",
            "essence": "Kiểm soát chủ động toàn bộ các yếu tố môi trường (ánh sáng, nhiệt độ, dinh dưỡng) để giải phóng nông nghiệp khỏi sự phụ thuộc vào thời tiết."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc bón phân '4 đúng'",
            "meaning": "Bón phân đạt hiệu quả cao nhất khi thực hiện nghiêm ngặt: Đúng loại, Đúng liều lượng, Đúng thời điểm và Đúng phương pháp.",
            "example": "Giai đoạn cây con cần bón thúc đạm (N) để phát triển thân lá, khi ra hoa tạo quả chuyển sang bón tăng lân (P) và kali (K).",
            "essence": "Thừa phân bón không chỉ gây lãng phí kinh tế mà còn gây cháy rễ cây và ô nhiễm nguồn nước ngầm."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích ưu điểm của phương pháp trồng rau thủy canh hồi lưu so với phương pháp trồng truyền thống trên đất.",
            "steps": [
              "Bước 1: So sánh hiệu quả sử dụng đất: Thủy canh có thể bố trí theo giàn tầng đứng, tiết kiệm 70% diện tích canh tác.",
              "Bước 2: So sánh lượng nước tiêu thụ: Nước và dinh dưỡng tuần hoàn khép kín, giảm thất thoát do bốc hơi và ngấm sâu.",
              "Bước 3: So sánh chất lượng an toàn: Không tiếp xúc mầm bệnh trong đất, kiểm soát chính xác dư lượng nitrat trong rau."
            ],
            "answer": "Thủy canh hồi lưu cho năng suất cao gấp 2-3 lần, thời gian thu hoạch rút ngắn 10-15 ngày và tạo ra nông sản sạch chuẩn VietGAP."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lạm dụng thuốc bảo vệ thực vật hóa học phun định kỳ thay vì áp dụng quản lý dịch hại tổng hợp (IPM).",
            "why": "Lạm dụng thuốc hóa học tiêu diệt thiên địch có ích, dẫn đến sâu hại kháng thuốc và để lại dư lượng độc hại cho người tiêu dùng."
          }
        ]
      }
    ]
  },

  "hdtn-huong-nghiep": {
    "id": "hdtn-huong-nghiep",
    "name": "HĐTN & Hướng nghiệp",
    "icon": "🎯",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Khám phá và Phát triển bản thân",
        "description": "Xây dựng hình ảnh bản thân tự tin, nhận diện cá tính, năng khiếu, quản lý cảm xúc, thích ứng với môi trường THPT và quản lý tài chính cá nhân.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Thích ứng với môi trường THPT và phát huy truyền thống nhà trường", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Làm chủ cảm xúc và quản lý tài chính cá nhân thông minh", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tự nhận thức bản thân (Self-awareness)",
            "definition": "Là khả năng hiểu rõ tính cách, điểm mạnh, điểm hạn chế, hệ giá trị, cảm xúc và động lực cá nhân trong mọi hoàn cảnh sống.",
            "example": "Biết mình có tư duy logic tốt nhưng dễ căng thẳng khi nói trước đám đông để chủ động rèn luyện kỹ năng thuyết trình mỗi tuần.",
            "essence": "Hiểu rõ chính mình là xuất phát điểm của mọi sự trưởng thành và thành công vững chắc."
          },
          {
            "term": "Nguyên tắc quản lý tài chính 50/30/20",
            "definition": "Quy tắc phân bổ thu nhập/tiền tiêu vặt: 50% cho nhu cầu thiết yếu, 30% cho mong muốn cá nhân và 20% cho tiết kiệm, quỹ dự phòng.",
            "example": "Học sinh có khoản tiền tiêu vặt 500.000đ/tháng: Dành 250k mua dụng cụ học tập, 150k giao lưu bạn bè và 100k bỏ ống heo tiết kiệm.",
            "essence": "Tự chủ tài chính giúp học sinh hình thành thói quen kỷ luật và làm chủ cuộc sống độc lập trong tương lai."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc làm chủ cảm xúc tiêu cực (Dừng lại — Hít sâu — Quan sát — Lựa chọn)",
            "meaning": "Khi gặp xung đột hoặc tức giận, không phản ứng bộc phát ngay mà dừng lại 10 giây để não bộ lấy lại trạng thái cân bằng lý trí.",
            "example": "Khi bị bạn bè hiểu lầm, hít thở sâu 3 nhịp để bình tĩnh lắng nghe trước khi giải thích một cách lịch sự, chân thành.",
            "essence": "Cảm xúc là phản xạ tự nhiên, nhưng cách chúng ta hành xử trước cảm xúc là sự lựa chọn bản lĩnh của người trưởng thành."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xây dựng kế hoạch thích ứng với môi trường học tập mới tại trường THPT trong tháng đầu tiên.",
            "steps": [
              "Bước 1: Tìm hiểu văn hóa, nội quy nhà trường, sơ đồ phòng chức năng và các câu lạc bộ học thuật.",
              "Bước 2: Chủ động làm quen với bạn bè cùng bàn, lập nhóm học tập chung 3-4 bạn cùng sở thích.",
              "Bước 3: Thiết lập thời gian biểu tự học buổi tối, chuẩn bị bài trước khi đến lớp để không bị ngợp trước khối lượng kiến thức."
            ],
            "answer": "Hình thành tâm lý tự tin, chủ động kết nối và bắt nhịp xuất sắc với phương pháp học tập THPT."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Thu mình khép kín, mặc cảm so sánh bản thân với các bạn giỏi hơn trong lớp.",
            "why": "Mỗi người có một lộ trình phát triển và thế mạnh riêng biệt; thước đo duy nhất có giá trị là sự tiến bộ của bản thân so với ngày hôm qua."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Trách nhiệm với gia đình và Xây dựng cộng đồng",
        "description": "Ứng xử văn minh trong gia đình, lắng nghe và thấu cảm giữa các thế hệ, tham gia hoạt động xã hội thiện nguyện và xây dựng cộng đồng gắn kết.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Gắn kết yêu thương và giải quyết bất đồng trong gia đình", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Trách nhiệm công dân và tham gia dự án thiện nguyện cộng đồng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thấu cảm liên thế hệ",
            "definition": "Là khả năng đặt mình vào vị trí của ông bà, cha mẹ để thấu hiểu sự khác biệt về lối sống, quan điểm và áp lực cuộc sống của thế hệ đi trước.",
            "example": "Thay vì cáu gắt khi cha mẹ nhắc nhở chuyện dùng điện thoại, học sinh hiểu rằng sự lo lắng đó xuất phát từ mong muốn bảo vệ sức khỏe cho mình.",
            "essence": "Tình yêu thương trong gia đình cần được nuôi dưỡng bằng sự tôn trọng và đối thoại kiên nhẫn thay vì im lặng đối đầu."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc giao tiếp 'Tôi' (I-message) trong hòa giải mâu thuẫn",
            "meaning": "Khi chia sẻ sự bất đồng, hãy bắt đầu bằng cảm nhận của bản thân ('Con cảm thấy...') thay vì công kích hoặc đổ lỗi ('Bố mẹ luôn luôn...').",
            "example": "Nói 'Con cảm thấy hơi áp lực khi bố mẹ so sánh con với anh chị' thay vì nói 'Bố mẹ lúc nào cũng bất công với con'.",
            "essence": "Giao tiếp xây dựng giúp đối phương mở lòng lắng nghe mà không dựng lên hàng rào phòng thủ tiêu cực."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Lập kế hoạch tổ chức một hoạt động gây quỹ thiện nguyện ủng hộ học sinh có hoàn cảnh khó khăn tại vùng cao.",
            "steps": [
              "Bước 1: Xác định mục tiêu và đối tượng thụ hưởng: Tặng 50 suất học bổng và sách giáo khoa cho điểm trường miền núi.",
              "Bước 2: Lựa chọn hình thức gây quỹ: Tổ chức thu gom phế liệu tái chế trong trường và bán sản phẩm thủ công handmade.",
              "Bước 3: Phân công nhiệm vụ cụ thể: Nhóm truyền thông, nhóm thu gom, nhóm tài chính minh bạch thu chi trên bảng tin.",
              "Bước 4: Tổ chức trao quà và gửi thư cảm ơn các nhà hảo tâm cùng báo cáo tài chính công khai."
            ],
            "answer": "Dự án lan tỏa tinh thần tương thân tương ái, rèn luyện kỹ năng làm việc nhóm và trách nhiệm công dân cho học sinh."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Tham gia thiện nguyện mang tính hình thức chụp ảnh đăng mạng xã hội mà không thực tâm hướng tới người nhận.",
            "why": "Giá trị cốt lõi của hoạt động cộng đồng là sự chân thành, tôn trọng phẩm giá và lòng tự trọng của những người yếu thế."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Bảo tồn cảnh quan và Bảo vệ môi trường sống",
        "description": "Thực trạng cảnh quan thiên nhiên và di tích văn hóa địa phương, hành vi tiêu dùng xanh, giảm thiểu rác thải nhựa và lối sống bền vững.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Bảo tồn danh lam thắng cảnh và di tích lịch sử địa phương", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thực hành lối sống xanh và bảo vệ hệ sinh thái", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Dấu chân sinh thái (Ecological Footprint)",
            "definition": "Thước đo mức độ tiêu dùng tài nguyên thiên nhiên và lượng chất thải mà một cá nhân hoặc cộng đồng tạo ra so với khả năng tự tái tạo của Trái đất.",
            "example": "Sử dụng xe đạp đi học, tắt điện khi rời phòng và mang bình nước cá nhân giúp giảm đáng kể lượng phát thải carbon mỗi ngày.",
            "essence": "Mỗi hành động tiêu dùng nhỏ của ngày hôm nay đều để lại hệ quả trực tiếp đối với ngôi nhà chung Trái đất."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc 5R trong quản lý chất thải và tiêu dùng xanh",
            "meaning": "Thực hiện theo thứ tự ưu tiên: Refuse (Từ chối) -> Reduce (Tiết giảm) -> Reuse (Tái sử dụng) -> Repurpose (Chuyển đổi công năng) -> Recycle (Tái chế).",
            "example": "Từ chối dùng túi nilon một lần khi đi siêu thị bằng cách mang theo túi vải sử dụng nhiều lần.",
            "essence": "Tái chế là giải pháp cuối cùng; giải pháp bền vững nhất là không phát sinh rác thải ngay từ nguồn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xây dựng chiến dịch 'Trường học không rác thải nhựa một lần' trong khuôn viên trường THPT.",
            "steps": [
              "Bước 1: Khảo sát thực trạng: Thống kê số lượng chai nhựa và cốc trà sữa vứt bỏ mỗi ngày tại căng tin trường.",
              "Bước 2: Truyền thông thay đổi nhận thức: Phát động cuộc thi làm video ngắn về tác hại của hạt vi nhựa đối với sức khỏe.",
              "Bước 3: Đưa ra giải pháp hành động: Lắp đặt trạm lấy nước uống miễn phí; căng tin giảm giá 2.000đ cho học sinh tự mang bình cá nhân."
            ],
            "answer": "Giảm thiểu 80% rác thải nhựa dùng một lần trong trường sau 2 tháng triển khai bền bỉ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng bảo vệ môi trường là việc của chính quyền và các nhà khoa học, cá nhân học sinh không tạo ra khác biệt.",
            "why": "Hiệu ứng cánh bướm: Hàng triệu học sinh cùng từ chối một chiếc ống hút nhựa sẽ tạo nên thay đổi to lớn cho hệ sinh thái đại dương."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Tìm hiểu nghề nghiệp và Định hướng tương lai",
        "description": "Thế giới nghề nghiệp trong kỷ nguyên 4.0, mô hình tính cách RIASEC, xu hướng phát triển thị trường lao động và lập kế hoạch rèn luyện nghề nghiệp.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Khám phá thế giới nghề nghiệp và thị trường lao động 4.0", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Định vị bản thân qua mô hình RIASEC và lập kế hoạch nghề nghiệp", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Mô hình tính cách nghề nghiệp RIASEC (John Holland)",
            "definition": "Phân loại tính cách và môi trường làm việc thành 6 nhóm: Thực tế (R), Nghiên cứu (I), Nghệ thuật (A), Xã hội (S), Quản lý (E) và Nghiệp vụ (C).",
            "example": "Người thuộc nhóm Nghiên cứu (I) phù hợp với công việc phân tích dữ liệu, nhà khoa học; người thuộc nhóm Nghệ thuật (A) phù hợp thiết kế sáng tạo.",
            "essence": "Sự phù hợp giữa đặc điểm tính cách cá nhân và bản chất công việc là chìa khóa tạo nên niềm say mê và thành công bền vững."
          },
          {
            "term": "Kỹ năng mềm thế kỷ 21 (4C Skills)",
            "definition": "Bộ 4 kỹ năng cốt lõi giúp người lao động không bị thay thế bởi AI: Tư duy phản biện (Critical Thinking), Giao tiếp (Communication), Hợp tác (Collaboration) và Sáng tạo (Creativity).",
            "example": "Trong dự án lập trình AI, kỹ sư không chỉ viết code mà phải hợp tác với bác sĩ y khoa để hiểu đúng nghiệp vụ chẩn đoán bệnh.",
            "essence": "Máy móc vượt trội ở tính toán lặp lại; con người vượt trội ở sự đồng cảm, sáng tạo và tư duy đạo đức."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc chọn nghề theo mô hình Cây nghề nghiệp",
            "meaning": "Chọn nghề phải bắt đầu từ gốc rễ: Sở thích, Khả năng cá nhân và Giá trị sống, sau đó mới xét đến các cành lá bên ngoài: Nhu cầu xã hội và Thu nhập.",
            "example": "Nếu chỉ chọn nghề vì 'hot' nhất thời mà bản thân không có năng khiếu hay đam mê thì rất dễ bỏ dở giữa chừng khi gặp khó khăn.",
            "essence": "Rễ có vững thì cây mới đơm hoa kết trái ngọt ngào qua năm tháng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Lập kế hoạch hành động 3 năm THPT của học sinh định hướng theo đuổi ngành Khoa học dữ liệu (Data Science).",
            "steps": [
              "Lớp 10: Tập trung xây dựng nền tảng Toán học giải tích, rèn luyện tư duy logic và tham gia CLB Tin học học ngôn ngữ Python căn bản.",
              "Lớp 11: Nâng cao năng lực Tiếng Anh học thuật (IELTS 6.5+), thực hiện một dự án khảo sát và phân tích số liệu nhỏ trong trường.",
              "Lớp 12: Đăng ký tổ hợp xét tuyển A00/A01, chuẩn bị hồ sơ ứng tuyển vào các trường đại học công nghệ uy tín."
            ],
            "answer": "Kế hoạch chi tiết, có mục tiêu đo lường được và định hướng rõ ràng qua từng năm học."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Phó mặc hoàn toàn quyết định chọn ngành chọn nghề cho phụ huynh hoặc chạy theo trào lưu đám đông.",
            "why": "Người trực tiếp học tập và làm việc suốt 40 năm cuộc đời là chính bạn; hãy lắng nghe lời khuyên nhưng người chịu trách nhiệm cuối cùng phải là chính bạn."
          }
        ]
      }
    ]
  },

  "am-nhac": {
    "id": "am-nhac",
    "name": "Âm nhạc",
    "icon": "🎵",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Giai điệu quê hương và Di sản âm nhạc dân tộc",
        "description": "Lí thuyết âm nhạc cơ bản, giọng điệu, thang âm ngũ cung, đặc trưng các làn điệu dân ca ba miền (Bắc Bộ, Trung Bộ, Nam Bộ) và di sản âm nhạc truyền thống.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Giọng điệu và thang âm ngũ cung trong âm nhạc truyền thống", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Vẻ đẹp các làn điệu dân ca và nhạc cổ truyền Việt Nam", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thang âm ngũ cung (Pentatonic scale)",
            "definition": "Là hệ thống âm gồm 5 bậc âm tự nhiên trong một quãng tám (Hò, Xự, Xang, Xê, Cống), không có các nửa cung, tạo nên màu sắc giai điệu mộc mạc, đậm hồn dân tộc.",
            "example": "Giai điệu bài dân ca Quan họ Bắc Ninh 'Người ơi người ở đừng về' hay dân ca Nam Bộ 'Lý ngựa ô' đều được xây dựng trên thang âm ngũ cung.",
            "essence": "Thang âm ngũ cung phản ánh tâm hồn bình dị, đằm thắm và triết lý hòa hợp với thiên nhiên của người Việt Nam."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc xác định giọng trưởng và giọng thứ song song",
            "meaning": "Hai giọng song song có cùng hóa biểu (số dấu thăng/giáng) nhưng chủ âm cách nhau một quãng 3 thứ (bậc I giọng thứ thấp hơn bậc I giọng trưởng 1,5 cung).",
            "example": "Giọng Đô trưởng (C major) không có dấu hóa nào ở đầu khuông nhạc, giọng song song tương ứng là La thứ (A minor).",
            "essence": "Mối quan hệ song song biểu thị sự tương phản cảm xúc: Giọng trưởng mang màu sắc tươi sáng, giọng thứ mang sắc thái trầm lắng trữ tình."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích đặc trưng âm nhạc của nghệ thuật Hát Xoan Phú Thọ — Di sản văn hóa phi vật thể của nhân loại.",
            "steps": [
              "Bước 1: Nguồn gốc và môi trường diễn xướng: Hát Xoan gắn với lễ hội đầu xuân tại các cửa đình đền vùng đất Tổ Phú Thọ.",
              "Bước 2: Cấu trúc biểu diễn gồm 3 chặng: Hát nghi lễ (chúc tụng), Hát quả cách (kể chuyện cày cấy, lịch sử), và Hát hội (giao duyên nam nữ).",
              "Bước 3: Nghệ thuật âm nhạc: Sử dụng nhịp phách trống cái, trống con rộn rã, các bài hát có lối hát đối đáp xen kẽ động tác múa phụ họa duyên dáng."
            ],
            "answer": "Hát Xoan là biểu tượng gắn kết cộng đồng và lưu giữ nguồn cội văn hóa ngàn năm của dân tộc."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa giọng C trưởng (Đô trưởng) và giọng A thứ (La thứ) vì chúng có cùng hóa biểu trắng.",
            "why": "Dù cùng hóa biểu nhưng bài hát giọng C trưởng kết thúc ở nốt Đô (C) mang cảm giác sáng sủa, còn bài hát giọng A thứ kết thúc ở nốt La (A) mang cảm giác sâu lắng."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Kĩ thuật thanh nhạc và Hát tập thể",
        "description": "Tư thế hát chuẩn mực, kĩ thuật làm chủ hơi thở cơ hoành, khẩu hình phát âm rõ chữ tiếng Việt và kĩ thuật hát bè hợp xướng hòa quyện.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Làm chủ hơi thở cơ hoành và mở khẩu hình phát âm", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Kĩ thuật hát bè và biểu cảm trong ca khúc hợp xướng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thở bụng (Hơi thở cơ hoành)",
            "definition": "Là kĩ thuật hít sâu để không khí tràn vào đáy phổi làm cơ hoành hạ thấp, bụng và khoang sườn nở ra, giúp trữ lượng hơi dồi dào và kiểm soát luồng hơi ổn định khi hát.",
            "example": "Khi lấy hơi hát câu dài, vai và ngực giữ nguyên thả lỏng, chỉ có vùng bụng nở ra nhẹ nhàng như ngửi hương một bông hoa thơm.",
            "essence": "Hơi thở là chiếc lò xo đẩy âm thanh bay bổng; hơi thở yếu sẽ khiến giọng hát bị phô, căng cổ và mất kiểm soát cao độ."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc hòa âm trong hát bè hợp xướng (Blend & Balance)",
            "meaning": "Mỗi thành viên phải lắng nghe bè của bạn, tiết chế âm lượng cá nhân để các bè chính và bè phụ hòa quyện thành một khối âm vang thống nhất.",
            "example": "Bè 2 hát bè trầm hơn một quãng 3 không được hát quá to lấn át bè chính lĩnh xướng giai điệu.",
            "essence": "Hợp xướng là nghệ thuật của sự khiêm nhường và lắng nghe; cái tôi cá nhân tan biến để tạo nên vẻ đẹp hòa hợp vĩ đại."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày 3 bước luyện thanh mở khẩu hình chữ 'A' để âm thanh vang tròn và không bị bẹt giọng.",
            "steps": [
              "Bước 1: Hạ hàm dưới nhẹ nhàng tự nhiên như trạng thái ngáp ngủ, lưỡi thả lỏng đặt sát đáy hàm.",
              "Bước 2: Nâng hàm ếch mềm phía sau lên cao để tạo vòm họng tròn rộng như quả trứng.",
              "Bước 3: Đẩy luồng hơi từ cơ hoành đưa âm thanh hướng lên xoang trán (điểm tựa âm thanh phía trước) tạo độ vang tự nhiên."
            ],
            "answer": "Giúp âm thanh phát ra tròn vành, sáng rõ và không bị nghẹt cổ họng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lấy hơi bằng ngực làm nhô vai lên cao khi chuẩn bị hát nốt cao.",
            "why": "Thở ngực làm dung tích khí bị hạn chế, cơ cổ bị gồng cứng khiến giọng hát bị nghẹn và dễ gây tổn thương dây thanh quản."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Thưởng thức âm nhạc và Nhạc cụ phương Tây",
        "description": "Lịch sử âm nhạc cổ điển phương Tây qua các thời kỳ (Baroque, Cổ điển Vienna, Lãng mạn), các nhà soạn nhạc vĩ đại và kĩ thuật đệm đàn guitar cơ bản.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Các bậc thầy âm nhạc cổ điển thế giới (Bach, Mozart, Beethoven)", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Làm quen với đàn guitar và kĩ thuật gảy hợp âm đệm hát", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bản giao hưởng (Symphony)",
            "definition": "Là tác phẩm khí nhạc quy mô lớn viết cho dàn nhạc giao hưởng đầy đủ, thường gồm 4 chương với cấu trúc hình thức xô-nát (sonata-allegro) chặt chẽ và tương phản sâu sắc.",
            "example": "Giao hưởng số 5 'Định mệnh' của Beethoven với mô-típ 4 nốt nhạc mở đầu đầy uy lực gõ cửa định mệnh.",
            "essence": "Giao hưởng là đỉnh cao trí tuệ của nghệ thuật âm thanh, nơi diễn tả toàn bộ các cung bậc triết học, xung đột và khát vọng của loài người."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc bấm hợp âm trên cần đàn guitar",
            "meaning": "Ngón tay bấm vuông góc với mặt phím đàn, đầu ngón tay đặt sát gờ kim loại (phím đàn) nhưng không đè lên phím để dây không bị tịt tiếng.",
            "example": "Khi bấm hợp âm Đô trưởng (C), ngón trỏ bấm dây 2 ngăn 1, ngón giữa bấm dây 4 ngăn 2, ngón áp út bấm dây 5 ngăn 3 đều vuông góc.",
            "essence": "Bấm sát phím giúp tốn ít lực tay nhất mà âm thanh phát ra vẫn tròn tiếng và trong trẻo."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích ý nghĩa thông điệp nhân văn trong Chương 4 Giao hưởng số 9 'Khải hoàn ca' của L.V. Beethoven.",
            "steps": [
              "Bước 1: Bối cảnh sáng tác: Beethoven viết tác phẩm khi đã bị điếc hoàn toàn, vượt qua bi kịch cá nhân để hướng về ánh sáng.",
              "Bước 2: Đột phá nghệ thuật: Lần đầu tiên trong lịch sử giao hưởng, Beethoven đưa giọng hát của dàn hợp xướng vào chương cuối dựa trên lời thơ Schiller.",
              "Bước 3: Thông điệp cốt lõi: 'Tất cả con người đều trở thành anh em', ca ngợi tình yêu tự do, hòa bình và sự đoàn kết toàn nhân loại."
            ],
            "answer": "Bản giao hưởng số 9 là di sản bất hủ khẳng định sức mạnh tinh thần bất diệt của con người chiến thắng số phận."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Bấm ngón tay nằm nghiêng đè lên các dây bên cạnh khi chơi đàn guitar.",
            "why": "Khi ngón tay bị nghiêng sẽ chạm vào dây đàn lân cận khiến dây đó bị tịt nốt và làm hỏng toàn bộ hợp âm hòa thanh."
          }
        ]
      }
    ]
  },

  "mi-thuat": {
    "id": "mi-thuat",
    "name": "Mĩ thuật",
    "icon": "🎨",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Khái quát về Nghệ thuật Hội họa",
        "description": "Ngôn ngữ thị giác của hội họa: Điểm, đường nét, mảng hình, khối, ánh sáng, màu sắc và thực hành vẽ tranh bằng chất liệu chì, than.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Ngôn ngữ hội họa và các yếu tố tạo hình thị giác", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Kĩ thuật vẽ tranh tĩnh vật chất liệu chì và than", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Luật xa gần (Linear Perspective)",
            "definition": "Là phương pháp khoa học biểu diễn không gian 3 chiều lên mặt phẳng 2 chiều dựa trên nguyên lý: Vật ở gần thì to, rõ nét; vật ở xa thì nhỏ, mờ nhạt và quy tụ về đường chân trời.",
            "example": "Hàng cây ven đường thẳng tắp: Cây gần nhất nhìn cao lớn vượt khung hình, các cây xa dần thu nhỏ lại và gặp nhau tại điểm tụ trên đường chân trời.",
            "essence": "Luật xa gần là cuộc cách mạng thời Phục hưng giúp hội họa tái hiện hiện thực với chiều sâu không gian sống động như mắt người cảm nhận."
          },
          {
            "term": "Tương phản sắc độ (Chiaroscuro)",
            "definition": "Kĩ thuật sử dụng độ tương phản mạnh mẽ giữa vùng sáng và vùng tối để tạo cảm giác về khối nổi ba chiều và bầu không khí kịch tính trong tranh.",
            "example": "Các bức họa của danh họa Rembrandt hay Caravaggio với luồng ánh sáng bí ẩn rọi vào khuôn mặt nhân vật giữa nền tối thẳm.",
            "essence": "Ánh sáng định hình hình khối; bóng tối tôn vinh ánh sáng và dẫn dắt cảm xúc người xem."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc bố cục 'Một phần ba' (Rule of Thirds)",
            "meaning": "Chia khung tranh thành lưới 3x3 bằng 2 đường dọc và 2 đường ngang; điểm nhấn chính của bức tranh nên đặt tại một trong 4 giao điểm của các đường này.",
            "example": "Khi vẽ phong cảnh biển, đường chân trời đặt ở đường ngang 1/3 phía dưới và cánh buồm đỏ thắm đặt tại điểm giao nhau 1/3 bên phải.",
            "essence": "Tránh đặt chủ thể chính ngay chính giữa tâm tranh vì sẽ gây cảm giác tĩnh lặng khô cứng, thiếu sự chuyển động thị giác."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Các bước cơ bản để dựng hình và đánh bóng một khối cầu thạch cao bằng bút chì 2B-6B.",
            "steps": [
              "Bước 1: Dựng hình: Vẽ khung hình vuông, vạch trục đối xứng và phác nét thẳng để tìm chu vi tròn của khối cầu.",
              "Bước 2: Xác định nguồn sáng: Đánh dấu vùng sáng trực tiếp, vùng bóng bản thân (vùng tối nhất), vùng phản quang và bóng đổ trên mặt bàn.",
              "Bước 3: Lên đậm nhạt: Dùng nét chì đan chéo nhẹ nhàng theo độ cong của khối, chuyển sắc độ êm dịu từ sáng -> trung gian -> tối -> bóng đổ."
            ],
            "answer": "Khối cầu hiện lên tròn trịa, có chiều sâu không gian và tách bạch rõ ràng khỏi mặt phẳng đỡ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đánh bóng đều đều một sắc độ xám mờ nhạt, thiếu sự tương phản giữa điểm sáng nhất (Highlight) và điểm tối nhất (Core shadow).",
            "why": "Thiếu tương phản sắc độ sẽ làm bức tranh bị 'bạc', hình khối phẳng lì và không tạo được cảm giác không gian ba chiều."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Nghệ thuật Điêu khắc và Kiến trúc",
        "description": "Không gian ba chiều trong điêu khắc (tượng tròn, phù điêu), ngôn ngữ tạo hình kiến trúc, các phong cách kiến trúc tiêu biểu và di sản kiến trúc Việt Nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Ngôn ngữ hình khối trong nghệ thuật điêu khắc tượng tròn và phù điêu", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Vẻ đẹp công trình kiến trúc truyền thống và hiện đại", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Điêu khắc tượng tròn (Freestanding Sculpture)",
            "definition": "Tác phẩm điêu khắc ba chiều hoàn chỉnh trong không gian thực, cho phép người xem quan sát thưởng ngoạn vẻ đẹp từ mọi góc độ xung quanh 360 độ.",
            "example": "Tượng Phật Bà Quan Âm nghìn mắt nghìn tay chùa Bút Tháp hay tượng David của Michelangelo.",
            "essence": "Điêu khắc là nghệ thuật của sự chiếm lĩnh không gian vật lý bằng các khối đặc và rỗng tương tác với ánh sáng thực."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc tỉ lệ vàng trong tạo hình kiến trúc và điêu khắc",
            "meaning": "Tỉ lệ xích xấp xỉ 1:1,618 (Phi) mang lại cảm giác hài hòa, cân đối và thẩm mỹ tự nhiên cao nhất cho công trình thị giác.",
            "example": "Tỉ lệ mặt tiền đền Parthenon (Hy Lạp cổ đại) hay chùa Một Cột (Hà Nội) đều tuân theo tỉ lệ vàng cân xứng.",
            "essence": "Tỉ lệ vàng phản ánh sự hài hòa toán học vốn ẩn chứa trong cấu trúc của vũ trụ và giới tự nhiên."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích giá trị tạo hình của kiến trúc Đình làng Việt Nam truyền thống.",
            "steps": [
              "Bước 1: Cấu trúc mái đình: Hệ thống mái cong hình mũi thuyền thanh thoát, lợp ngói mũi hài rêu phong hòa quyện với cảnh quan làng quê.",
              "Bước 2: Kết cấu vì kèo gỗ: Khung gỗ lim chịu lực vững chãi liên kết bằng mộng, không dùng đinh kim loại.",
              "Bước 3: Điêu khắc trang trí: Các bức chạm lộng trên vì kèo mô tả cảnh sinh hoạt dân gian (đấu vật, đi săn, chèo thuyền) tràn đầy sức sống hồn nhiên."
            ],
            "answer": "Đình làng là đỉnh cao kiến trúc gỗ dân gian, vừa là trung tâm tín ngưỡng vừa là không gian sinh hoạt văn hóa cộng đồng gắn kết."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa phù điêu (chạm nổi trên một mặt phẳng nền) với tượng tròn (không có mặt phẳng nền, đứng độc lập trong không gian).",
            "why": "Phù điêu chỉ quan sát được từ phía trước giống như tranh đắp nổi, trong khi tượng tròn bắt buộc phải hoàn thiện trọn vẹn cả mặt trước, mặt bên và mặt sau."
          }
        ]
      }
    ]
  },

  "giao-duc-the-chat": {
    "id": "giao-duc-the-chat",
    "name": "Giáo dục Thể chất",
    "icon": "⚽",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Rèn luyện Thể lực và Dinh dưỡng Thể thao",
        "description": "Các tố chất thể lực cơ bản (sức nhanh, sức mạnh, sức bền, sự khéo léo, độ dẻo), chế độ dinh dưỡng vận động và lập kế hoạch rèn luyện thể chất cá nhân.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Phát triển các tố chất thể lực và nguyên tắc tập luyện khoa học", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Dinh dưỡng hợp lý và hồi phục năng lượng trong thể thao", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quy luật siêu bù trừ (Supercompensation)",
            "definition": "Là hiện tượng sau khi tập luyện mệt mỏi, cơ thể được nghỉ ngơi và dinh dưỡng đầy đủ sẽ phục hồi vượt mức năng lực ban đầu, giúp thể lực tiến bộ lên nấc thang mới.",
            "example": "Sau buổi tập chạy sức bền, cơ bắp được bổ sung protein và ngủ đủ giấc sẽ tái tạo sợi cơ dày hơn, giúp buổi sau chạy bền bỉ hơn.",
            "essence": "Tập luyện phá vỡ giới hạn; nghỉ ngơi và dinh dưỡng mới là lúc cơ thể xây dựng lại sức mạnh vượt trội."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc tăng dần lượng vận động (Overload Principle)",
            "meaning": "Để nâng cao thể lực, lượng vận động (cường độ và thời gian) phải tăng lên từng bước một cách khoa học, tránh tăng đột ngột gây kiệt sức.",
            "example": "Tuần đầu chạy cự li 1.500m với tốc độ vừa phải, tuần thứ hai tăng lên 1.800m hoặc giữ 1.500m nhưng rút ngắn thời gian hoàn thành.",
            "essence": "Cơ thể con người có khả năng thích nghi phi thường nhưng cần thời gian tích lũy kiên trì từng ngày."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Xây dựng kế hoạch rèn luyện sức bền tim mạch cho học sinh lớp 10 chuẩn bị cho kỳ kiểm tra chạy 1.500m.",
            "steps": [
              "Bước 1: Tần suất: Tập luyện 3 buổi/tuần (thứ 2 - thứ 4 - thứ 6), xen kẽ ngày nghỉ ngơi hồi phục.",
              "Bước 2: Cấu trúc buổi tập: Khởi động kĩ 10 phút -> Chạy biến tốc 20 phút (chạy nhanh 1 phút, đi bộ thả lỏng 1 phút) -> Thả lỏng giãn cơ 10 phút.",
              "Bước 3: Dinh dưỡng & Nước: Uống 200ml nước trước khi chạy 15 phút, bổ sung chuối và sữa sau khi tập để bù đắp glycogen."
            ],
            "answer": "Giúp nâng cao dung tích sống của phổi, cải thiện nhịp tim và đạt loại Giỏi trong kỳ kiểm tra thể lực quốc gia."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Bỏ qua bước khởi động và thả lỏng trước và sau buổi tập luyện thể thao.",
            "why": "Không khởi động làm cơ bắp bị cứng dễ gây rách cơ, chuột rút; không thả lỏng làm acid lactic ứ đọng gây đau nhức kéo dài nhiều ngày."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Kĩ thuật Thể thao và Phòng chống chấn thương",
        "description": "Kĩ thuật các môn thể thao phổ biến (Bóng đá, Cầu lông, Bóng rổ), chiến thuật thi đấu phối hợp đồng đội và nguyên tắc sơ cứu chấn thương thể thao R.I.C.E.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Kĩ thuật cơ bản trong Bóng đá và Cầu lông", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Nguyên tắc sơ cứu chấn thương thể thao theo giao thức R.I.C.E", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Giao thức R.I.C.E trong xử lý chấn thương phần mềm",
            "definition": "Quy trình sơ cứu 4 bước chuẩn quốc tế khi bị bong gân, căng cơ: R (Rest — Nghỉ ngơi), I (Ice — Chườm lạnh), C (Compression — Băng ép), E (Elevation — Kê cao chi chấn thương).",
            "example": "Khi bị lật sơ mi cổ chân lúc chơi bóng rổ: Lập tức dừng thi đấu -> Chườm túi đá lạnh 15-20 phút -> Dùng băng thun quấn nhẹ -> Kê chân cao hơn tim.",
            "essence": "Xử lý chuẩn trong 24 giờ đầu giúp co mạch máu, giảm sưng đau tức thì và rút ngắn một nửa thời gian phục hồi dây chằng."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc cấm tuyệt đối khi sơ cứu bong gân cấp tính (HARM)",
            "meaning": "Trong 48 giờ đầu tuyệt đối KHÔNG: H (Heat — Xoa dầu nóng/chườm nóng), A (Alcohol — Uống rượu bia), R (Running — Chạy nhảy vận động), M (Massage — Xoa bóp mạnh).",
            "example": "Tuyệt đối không bóp cồn mật gấu hoặc dầu gió vào khớp vừa bị trật vì sẽ làm giãn mạch máu gây xuất huyết và sưng phù nặng nề hơn.",
            "essence": "Hành vi xoa bóp dầu nóng theo thói quen dân gian khi khớp đang sưng tấy là sai lầm nguy hiểm làm tổn thương thêm dây chằng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày kĩ thuật đá bóng bằng lòng bàn chân (chuyền bóng ngắn chính xác) trong môn bóng đá.",
            "steps": [
              "Bước 1: Chạy đà: Góc chạy đà 45 độ so với hướng bóng, bước đà cuối dài và hạ thấp trọng tâm.",
              "Bước 2: Đặt chân trụ: Chân trụ đặt song song và cách bóng 10-15cm, mũi chân hướng thẳng về mục tiêu.",
              "Bước 3: Vung chân đá: Gập gối, xoay má trong bàn chân vuông góc với hướng chạy, tiếp xúc bóng đúng tâm điểm sau quả bóng."
            ],
            "answer": "Đường bóng đi sệt, chính xác và có độ đầm thuận lợi nhất cho đồng đội khống chế bước một."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chân trụ đặt quá xa hoặc quá gần bóng, mũi chân trụ lệch hướng mục tiêu chuyền.",
            "why": "Chân trụ là điểm tựa cân bằng; đặt sai vị trí chân trụ sẽ làm lệch trọng tâm cơ thể và khiến cú đá bị bay bổng ra ngoài hoặc thiếu lực."
          }
        ]
      }
    ]
  }
}

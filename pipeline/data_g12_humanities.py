# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa 5 môn Xã hội & Nhân văn Lớp 12 SGK Kết nối tri thức 2026-2027:
- Ngữ Văn (9 bài bám sát 100% OCR 12-sgk-ngu-van-12-tap-mot & tap-hai)
- Tiếng Anh (10 units Global Success bám sát chương trình THPT 2018)
- Lịch sử (6 chủ đề: Thế giới sau Chiến tranh lạnh, ASEAN, CMT8 & Giải phóng DT, Đổi mới 1986, Đối ngoại VN, Hồ Chí Minh)
- Địa lí (6 phần bám sát 100% OCR 12-sgk-dia-li-12: Tự nhiên VN, Dân cư VN, Các ngành kinh tế, Dịch vụ, Các vùng KT-XH, Biển đảo)
- Giáo dục kinh tế & pháp luật (6 chủ đề: Tăng trưởng KT, Hội nhập KT, An sinh xã hội, Tài chính cá nhân, Quyền tự do kinh doanh & lao động, Sở hữu tài sản & môi trường)
"""

true = True
false = False
null = None

HUMANITIES_SUBJECTS = {
  "ngu-van": {
    "id": "ngu-van",
    "name": "Ngữ Văn",
    "icon": "📖",
    "chapters": [
      {
        "id": "ch01",
        "title": "Bài 1: Khả năng lớn lao của tiểu thuyết",
        "description": "Đọc hiểu tiểu thuyết hiện đại và đương đại; nghệ thuật trần thuật, xây dựng nhân vật; biện pháp tu từ nói mỉa, nghịch ngữ; viết bài văn nghị luận so sánh, đánh giá hai tác phẩm truyện.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Xuân Tóc Đỏ cứu quốc (Trích Số đỏ – Vũ Trọng Phụng)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Mùa lá rụng trong vườn (Trích – Ma Văn Kháng)", "hasRealContent": true },
          { "id": "l03", "title": "Thực hành tiếng Việt: Biện pháp tu từ nói mỉa, nghịch ngữ", "hasRealContent": true },
          { "id": "l04", "title": "Viết: Bài văn nghị luận so sánh, đánh giá hai tác phẩm truyện", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tiểu thuyết hiện đại",
            "definition": "Là thể loại tự sự cỡ lớn có khả năng dung chứa bức tranh đời sống sâu rộng, tái hiện số phận con người trong tính đa diện, phức tạp và khai thác chiều sâu tâm lý nội tâm nhân vật.",
            "example": "Tác phẩm 'Số đỏ' của Vũ Trọng Phụng phơi bày bức tranh xã hội thành thị tư sản nhố nhăng, đồi bại dưới chiêu bài 'Âu hóa' và 'văn minh'.",
            "essence": "Tiểu thuyết phá vỡ cái nhìn đơn tuyến, đưa con người từ biểu tượng đạo đức lý tưởng hóa về với thực tại đời thường nhiều chiều kích."
          },
          {
            "term": "Biện pháp tu từ nói mỉa và nghịch ngữ",
            "definition": "Nói mỉa là cách dùng từ ngữ mang nghĩa tích cực bề ngoài để phê phán, châm biếm mỉa mai thực chất tiêu cực bên trong. Nghịch ngữ (oxymoron) là sự kết hợp bất ngờ giữa hai khái niệm trái ngược nhau tạo nên hiệu quả trào phúng sâu sắc.",
            "example": "'Xuân Tóc Đỏ cứu quốc' – một kẻ hạ lưu vô học, lưu manh đầu đường xó chợ bỗng được tôn xưng là 'vĩ nhân', 'anh hùng cứu quốc'.",
            "essence": "Tạo ra khoảng cách trào phúng giữa ngôn từ biểu hiện và bản chất thực tế, kích thích người đọc bật cười châm biếm."
          }
        ],
        "rules": [
          {
            "statement": "Quy trình nghị luận so sánh hai tác phẩm truyện",
            "meaning": "Cần xác định điểm tương đồng và khác biệt về đề tài, chủ đề, hình tượng nhân vật và nghệ thuật trần thuật; từ đó lý giải nguyên nhân gắn liền với phong cách nhà văn và bối cảnh thời đại.",
            "example": "So sánh nhân vật Xuân Tóc Đỏ (Số đỏ) và nhân vật anh Pha (Bước đường cùng) để thấy bức tranh xã hội đa góc nhìn của văn học hiện thực 1930-1945.",
            "essence": "So sánh không phải là liệt kê cơ học mà là đặt hai đối tượng trong thế đối sánh để làm nổi bật nét độc đáo của từng tác giả."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích nghệ thuật trào phúng đỉnh cao của Vũ Trọng Phụng qua màn kịch 'Xuân Tóc Đỏ cứu quốc' trong đoạn trích SGK.",
            "steps": [
              "Bước 1: Giới thiệu tình huống trào phúng: Một trận đấu quần vợt giao hữu thể thao biến thành sự kiện chính trị tầm cỡ quốc tế định đoạt vận mệnh hai nước.",
              "Bước 2: Phân tích nghệ thuật xây dựng nhân vật: Xuân Tóc Đỏ từ chỗ bị đe dọa vì chơi quá giỏi chuyển sang 'nhường' phần thắng để cứu vãn hòa bình một cách trơ trẽn.",
              "Bước 3: Phân tích phản ứng đám đông: Đám đông dân chúng mù quáng, hoan hô cuồng nhiệt kẻ cơ hội; giọng điệu người kể chuyện lạnh lùng, giễu nhại chua cay.",
              "Bước 4: Đánh giá giá trị hiện thực: Tố cáo bản chất xã hội thực dân nửa phong kiến đảo điên thật - giả, sang - hèn."
            ],
            "answer": "Nghệ thuật trào phúng thể hiện qua tình huống phi lý, ngôn ngữ giễu nhại và màn kịch biến kẻ lưu manh thành vị cứu tinh dân tộc, lột trần bản chất nhố nhăng của xã hội tư sản."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa so sánh văn học với việc tóm tắt lần lượt hai tác phẩm một cách độc lập.",
            "why": "Bài văn so sánh phải liên tục đối chiếu theo từng tiêu chí cụ thể (nội dung, nhân vật, nghệ thuật) chứ không viết thành hai bài phân tích rời rạc."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Bài 2: Những thế giới thơ",
        "description": "Đọc hiểu thế giới hình tượng thơ trữ tình trung đại và hiện đại; thi luật và nhạc điệu; tác dụng của biện pháp tu từ trong thơ; viết bài văn nghị luận so sánh hai tác phẩm thơ.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Cảm hoài (Nỗi lòng – Đặng Dung)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Tây Tiến (Quang Dũng)", "hasRealContent": true },
          { "id": "l03", "title": "Đọc: Đàn ghi ta của Lor-ca (Thanh Thảo)", "hasRealContent": true },
          { "id": "l04", "title": "Thực hành tiếng Việt: Tác dụng của biện pháp tu từ trong thơ", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Thế giới hình tượng thơ",
            "definition": "Là bức tranh hiện thực và tâm trạng được khúc xạ qua lăng kính cảm xúc chủ quan của thi nhân, tổ chức bằng ngôn ngữ giàu nhạc tính, hình ảnh tượng trưng và liên tưởng bất ngờ.",
            "example": "Bức tranh thiên nhiên Tây Bắc vừa hùng vĩ dữ dội ('Dốc lên khúc khuỷu dốc thăm thẳm') vừa thơ mộng trữ tình ('Nhà ai Châu Mộc khói lam chiều').",
            "essence": "Thơ không miêu tả sự vật đơn thuần mà khơi gợi sự đồng điệu tâm hồn thông qua thế giới cảm xúc thẩm mỹ."
          },
          {
            "term": "Chất bi tráng trong thơ kháng chiến",
            "definition": "Là sự hòa quyện giữa hiện thực gian khổ, hy sinh mất mát đau thương (bi) với khí phách anh hùng hào hoa, tinh thần lạc quan và lý tưởng cống hiến cao cả (tráng).",
            "example": "'Tây Tiến đoàn binh không mọc tóc / Quân xanh màu lá dữ oai hùm / Mắt trừng gửi mộng qua biên giới / Đêm mơ Hà Nội dáng kiều thơm'.",
            "essence": "Vẻ đẹp bi tráng nâng tầm hiện thực khốc liệt thành tượng đài bất tử về người lính vệ quốc."
          }
        ],
        "rules": [
          {
            "statement": "Đặc trưng ngôn ngữ thơ ca",
            "meaning": "Ngôn ngữ thơ có tính hàm súc, giàu hình ảnh, nhịp điệu và nhạc tính; sử dụng nhiều biện pháp tu từ (ẩn dụ, hoán dụ, điệp từ, tượng trưng) để tạo nên nhiều tầng nghĩa liên tưởng.",
            "example": "Hình ảnh 'tiếng đàn bọt nước', 'áo choàng đỏ gắt' trong thơ Thanh Thảo biểu tượng cho nghệ thuật cách tân và bi kịch của Lor-ca.",
            "essence": "Ý tại ngôn ngoại: lời thơ ít mà gợi ý nghĩa mênh mông vô tận."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Cảm nhận vẻ đẹp hào hoa và bi tráng của hình tượng người lính Tây Tiến trong bài thơ của Quang Dũng.",
            "steps": [
              "Bước 1: Nêu bối cảnh xuất thân: Đa số là thanh niên, học sinh trí thức Hà Nội mang tâm hồn lãng mạn, trẻ trung ra chiến trường.",
              "Bước 2: Phân tích hiện thực gian khổ: Bệnh tật rụng tóc, sốt rét xanh xao da thịt nhưng khí phách oai vệ như hùm thiêng chốn rừng sâu.",
              "Bước 3: Phân tích thế giới tâm hồn hào hoa: Dù bom đạn biên cương vẫn hướng về 'dáng kiều thơm' thanh lịch đất kinh kỳ.",
              "Bước 4: Khắc họa sự hy sinh cao cả: 'Chiếu manh rách rưới / Áo bào thay chiếu anh về đất / Sông Mã gầm lên khúc độc hành' – sự hy sinh được thi vị hóa trang trọng."
            ],
            "answer": "Người lính Tây Tiến mang vẻ đẹp bi tráng độc đáo: Vừa gánh chịu gian khổ hy sinh tột cùng, vừa ngời sáng tâm hồn hào hoa lãng mạn và khí phách dâng hiến cho non sông."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chỉ nhấn mạnh khía cạnh gian khổ, bệnh tật làm cho bài thơ có cảm giác bi lụy, tiêu cực.",
            "why": "Quang Dũng nhìn gian khổ bằng cảm quan lãng mạn hào hùng, biến cái bi thương thành bi tráng bất tử."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Bài 3: Lập luận trong văn bản nghị luận",
        "description": "Đọc hiểu văn bản nghị luận xã hội và văn hóa; nghệ thuật lập luận chặt chẽ, luận điểm sắc bén và dẫn chứng thuyết phục; nhận diện và sửa lỗi logic, lỗi câu mơ hồ trong tiếng Việt.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Nhìn về vốn văn hoá dân tộc (Trích – Trần Đình Hượu)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Năng lực sáng tạo (Trích – Phan Đình Diệu)", "hasRealContent": true },
          { "id": "l03", "title": "Đọc: Mấy ý nghĩ về thơ (Trích – Nguyễn Đình Thi)", "hasRealContent": true },
          { "id": "l04", "title": "Thực hành tiếng Việt: Lỗi logic, lỗi câu mơ hồ và cách sửa", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Vốn văn hóa dân tộc",
            "definition": "Là hệ thống những giá trị vật chất và tinh thần được cộng đồng người Việt sáng tạo, tích lũy và kiểm nghiệm qua trường kỳ lịch sử dựng nước và giữ nước, phản ánh cốt cách tâm hồn dân tộc.",
            "example": "Trần Đình Hượu chỉ ra văn hóa truyền thống Việt Nam coi trọng sự hài hòa, thiết thực, chuộng sự yên ổn bình dị hơn là những công trình vĩ đại, kỳ vĩ tột bậc.",
            "essence": "Nhìn nhận bản sắc văn hóa dân tộc một cách khách quan, khoa học: thấy rõ điểm mạnh để phát huy và hạn chế để hội nhập đổi mới."
          },
          {
            "term": "Lỗi logic và lỗi câu mơ hồ trong tiếng Việt",
            "definition": "Lỗi logic xảy ra khi các phán đoán trong câu mâu thuẫn nhau hoặc quan hệ nhân quả không tương thích. Lỗi câu mơ hồ xảy ra do cách dùng từ, ngắt ngữ đoạn hoặc sắp xếp trật tự từ ngữ dẫn đến nhiều cách hiểu trái ngược nhau.",
            "example": "'Nó nhìn tôi bằng đôi mắt vừa nghiêm khắc vừa buồn cười' (lỗi mâu thuẫn logic) -> Sửa: 'vừa nghiêm khắc vừa pha chút hóm hỉnh'.",
            "essence": "Tư duy sáng rõ là tiền đề cho ngôn ngữ chuẩn xác; lập luận thuyết phục đòi hỏi sự chặt chẽ tuyệt đối về mặt logic hình thức."
          }
        ],
        "rules": [
          {
            "statement": "Quy tắc xây dựng hệ thống luận điểm trong văn nghị luận",
            "meaning": "Mỗi luận điểm phải trả lời một khía cạnh của vấn đề trọng tâm, diễn đạt ngắn gọn mạch lạc, sắp xếp theo trình tự lập luận hợp lý (từ khái quát đến cụ thể, từ bản chất đến biểu hiện, từ nguyên nhân đến giải pháp).",
            "example": "Nghị luận về văn hóa: Luận điểm 1: Đặc trưng nổi bật -> Luận điểm 2: Nguyên nhân cội rễ -> Luận điểm 3: Bài học phát triển thời hiện đại.",
            "essence": "Hệ thống luận điểm là khung xương chịu lực của toàn bộ bài văn nghị luận."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Theo tác giả Trần Đình Hượu trong 'Nhìn về vốn văn hóa dân tộc', đặc trưng nổi bật trong quan niệm sống của người Việt Nam truyền thống là gì?",
            "steps": [
              "Bước 1: Tác giả chỉ ra người Việt chuộng sự thiết thực: không chuộng cái quá cao xa hay cái tuyệt đối lý tưởng.",
              "Bước 2: Coi trọng sự hài hòa, dung dị: 'Cái đẹp vừa xinh, vừa khéo', 'ấm no, bình yên' là ước vọng lớn nhất của đời sống.",
              "Bước 3: Tinh thần khoan dung, hòa đồng với thiên nhiên và cộng đồng xóm giềng.",
              "Bước 4: Nhận xét: Đó là vẻ đẹp của sự bình ổn, bền vững nhưng cũng thiếu vắng những khát vọng sáng tạo mang tính đột phá phi thường."
            ],
            "answer": "Đặc trưng nổi bật là tinh thần chuộng sự thiết thực, hài hòa, bình dị và chừng mực; sống yên vui và thích ứng khéo léo với hoàn cảnh tự nhiên và xã hội."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nêu dẫn chứng chung chung, sáo rỗng mà không phân tích làm sáng tỏ luận điểm.",
            "why": "Dẫn chứng chỉ có giá trị thuyết phục khi đi kèm với thao tác bình luận và kết nối chặt chẽ với luận điểm cần chứng minh."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Bài 4: Yếu tố kì ảo trong truyện kể",
        "description": "Đặc trưng của yếu tố kì ảo trong văn xuôi trung đại và hiện đại; chức năng thẩm mĩ và giải thiêng; nghệ thuật sử dụng điển cố; viết bài văn nghị luận về vay mượn, cải biến và sáng tạo.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Hải khẩu linh từ (Đền thiêng cửa bể – Đoàn Thị Điểm)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Muối của rừng (Trích – Nguyễn Huy Thiệp)", "hasRealContent": true },
          { "id": "l03", "title": "Thực hành tiếng Việt: Nghệ thuật sử dụng điển cố trong văn học", "hasRealContent": true },
          { "id": "l04", "title": "Viết: Nghị luận về việc vay mượn – cải biến – sáng tạo trong tác phẩm", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Yếu tố kì ảo trong văn học",
            "definition": "Là những chi tiết, hình ảnh, sự việc siêu nhiên hoang đường không có thực được nhà văn sáng tạo nhằm thể hiện ước mơ công lý, tạo không khí huyền thoại hoặc triết lý về nhân sinh.",
            "example": "Trong 'Muối của rừng', hình ảnh hoa tử huyền ba chục năm mới nở một lần báo hiệu điềm lành và sự thức tỉnh lương tri của ông Diểu.",
            "essence": "Kì ảo là phương tiện nghệ thuật biểu đạt sâu sắc hơn hiện thực đời sống và thế giới tâm linh con người."
          },
          {
            "term": "Điển cố trong văn học trung đại",
            "definition": "Là những câu chuyện, sự tích, sự kiện lịch sử hoặc câu thơ cổ được cô đúc lại thành cụm từ nhằm gợi lên một hàm ý sâu sắc mà không cần diễn giải dông dài.",
            "example": "Điển 'Bá Nha - Tử Kỳ' biểu tượng cho tình tri âm tri kỷ thấu hiểu lòng nhau.",
            "essence": "Thể hiện vốn học uyên bác của tác giả và tạo nên vẻ đẹp hàm súc, trang nhã cho tác phẩm văn chương."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc tiếp nhận và sáng tạo nghệ thuật (Vay mượn và cải biến)",
            "meaning": "Một tác phẩm có thể tiếp thu cốt truyện dân gian hoặc điển tích nước ngoài, nhưng giá trị đích thực chỉ xuất hiện khi nhà văn cải biến sáng tạo mang đậm hơi thở thời đại và phong cách cá nhân.",
            "example": "Nguyễn Du mượn cốt truyện 'Kim Vân Kiều truyện' của Thanh Tâm Tài Nhân nhưng đã sáng tạo nên kiệt tác thi ca 'Truyện Kiều' mang linh hồn dân tộc Việt.",
            "essence": "Kế thừa truyền thống để thăng hoa sáng tạo mới chứ không phải sao chép mô phỏng nguyên xi."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích ý nghĩa chi tiết ông Diểu buông súng và trần truồng đi về trong mưa xuân ở cuối truyện ngắn 'Muối của rừng' (Nguyễn Huy Thiệp).",
            "steps": [
              "Bước 1: Hành động buông súng: Từ bỏ vũ khí săn bắn tượng trưng cho việc từ bỏ bạo lực, dã tâm hủy diệt thiên nhiên.",
              "Bước 2: Hành động trần truồng: Rũ bỏ lớp áo văn minh nhân tạo đầy toan tính để trở về với trạng thái nguyên sơ, trong sạch của con người tự nhiên.",
              "Bước 3: Chi tiết hoa tử huyền nở trong mưa xuân: Biểu tượng cho sự tái sinh tâm hồn, sự phục thiện và mối hòa giải thiêng liêng giữa con người và mẹ thiên nhiên."
            ],
            "answer": "Chi tiết đánh dấu sự thức tỉnh lương tri và sự thanh lọc tâm hồn của ông Diểu, khẳng định triết lý con người chỉ tìm thấy an lạc thực sự khi biết yêu thương và sống hòa hợp với thiên nhiên."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Xem yếu tố kì ảo chỉ là chi tiết mê tín dị đoan hoang đường vô căn cứ.",
            "why": "Trong văn học, kì ảo là một thủ pháp nghệ thuật ẩn dụ chứa đựng những thông điệp nhân văn và triết lý nhân sinh sâu sắc."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Bài 5: Tiếng cười của hài kịch",
        "description": "Đặc trưng của thể loại hài kịch: xung đột kịch, nhân vật hài hước, ngôn ngữ kịch trào lộng; viết báo cáo nghiên cứu về một vấn đề tự nhiên hoặc xã hội.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Nhân vật quan trọng (Trích Quan thanh tra – Gogol)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Giấu của (Trích Quẫn – Lộng Chương)", "hasRealContent": true },
          { "id": "l03", "title": "Viết: Viết báo cáo nghiên cứu về một vấn đề tự nhiên, xã hội", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Xung đột kịch trong hài kịch",
            "definition": "Là mâu thuẫn không thể dung hòa giữa cái xấu xa, lố lăng, lạc hậu cố tình ngụy trang dưới vỏ bọc cao đạo, tiến bộ với chân lý đời sống và lương tri con người.",
            "example": "Trong 'Quan thanh tra' của Gogol, toàn bộ đám quan chức địa phương tha hóa, tham nhũng đều run sợ trước một chàng công chức quèn bị tưởng nhầm là thanh tra triều đình.",
            "essence": "Tiếng cười hài kịch là vũ khí sắc bén tước bỏ mặt nạ giả tạo của các thói hư tật xấu trong xã hội."
          },
          {
            "term": "Báo cáo nghiên cứu khoa học",
            "definition": "Là văn bản trình bày kết quả khảo sát, thực nghiệm hoặc nghiên cứu lý thuyết về một đề tài cụ thể, tuân thủ cấu trúc khoa học gồm: Đặt vấn đề, Phương pháp nghiên cứu, Kết quả và Bàn luận, Kết luận và Tài liệu tham khảo.",
            "example": "Báo cáo nghiên cứu về thực trạng sử dụng mạng xã hội và sức khỏe tâm thần của học sinh THPT.",
            "essence": "Rèn luyện tư duy nghiên cứu khách quan, phương pháp thu thập dữ liệu minh bạch và kỹ năng lập luận khoa học."
          }
        ],
        "rules": [
          {
            "statement": "Cấu trúc chuẩn của một báo cáo nghiên cứu",
            "meaning": "Báo cáo phải có đầy đủ phần mở đầu (lý do chọn đề tài), nội dung chính (phân tích số liệu có biểu đồ minh chứng) và kết luận đề xuất; phải trích dẫn nguồn tài liệu tham khảo chính xác.",
            "example": "Mọi số liệu khảo sát phần trăm cần chú thích rõ cỡ mẫu điều tra (ví dụ: N = 300 học sinh) và thời gian thực hiện.",
            "essence": "Tính trung thực và chuẩn mực khoa học là linh hồn của báo cáo nghiên cứu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích tình huống kịch trớ trêu trong đoạn trích 'Quan thanh tra' của Gogol.",
            "steps": [
              "Bước 1: Nhận diện mâu thuẫn: Đám quan chức thị trấn quen thói ăn hối lộ, lộng hành đang đứng trước nguy cơ bị phát giác bởi quan thanh tra vi hành bí mật.",
              "Bước 2: Tình huống nhầm lẫn: Khlestakov – một viên công chức quèn thua bạc cháy túi – tình cờ ghé qua quán trọ và bị đám quan chức tưởng nhầm là quan thanh tra đại thần.",
              "Bước 3: Sự phát triển xung đột: Khlestakov mặc sức vòi vĩnh, nhận hối lộ và tán tỉnh trong sự nịnh bợ, run sợ tột độ của tên Thị trưởng.",
              "Bước 4: Tiếng cười trào phúng: Vạch trần sự hèn hạ, dối trá và tha hóa đến cùng cực của bộ máy quan lại Sa hoàng."
            ],
            "answer": "Tình huống nhầm lẫn khôi hài tạo nên sự bộc lộ bản chất tự nhiên: Sự sợ hãi của tội lỗi tham nhũng đã biến đám quan lại thành những kẻ ngốc nghếch, nịnh bợ kệch cỡm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đạo văn hoặc sao chép nguyên văn tài liệu trên mạng vào báo cáo nghiên cứu mà không dẫn nguồn.",
            "why": "Vi phạm nghiêm trọng đạo đức học thuật và quyền sở hữu trí tuệ; mọi trích dẫn cần đặt trong ngoặc kép và ghi rõ tác giả, năm công bố."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Bài 6: Hồ Chí Minh - 'Văn hoá phải soi đường cho quốc dân đi'",
        "description": "Quan điểm sáng tác văn học của Hồ Chí Minh; phong cách nghệ thuật đa dạng kết hợp tính chiến đấu cách mạng và tinh hoa dân tộc; nghệ thuật lập luận trong Tuyên ngôn Độc lập; biện pháp tu từ khẳng định, phủ định.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Tuyên ngôn Độc lập (Hồ Chí Minh)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Phong cách Hồ Chí Minh và Di sản tư tưởng", "hasRealContent": true },
          { "id": "l03", "title": "Thực hành tiếng Việt: Biện pháp tu từ khẳng định, phủ định trong văn chính luận", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quan điểm sáng tác văn học của Hồ Chí Minh",
            "definition": "Văn hóa nghệ thuật là một mặt trận, người nghệ sĩ là chiến sĩ trên mặt trận ấy; văn chương phải có tính chiến đấu, phục vụ sự nghiệp đấu tranh giải phóng dân tộc và xây dựng cuộc sống mới của nhân dân.",
            "example": "'Nay ở trong thơ nên có thép / Nhà thơ cũng phải biết xung phong' (Cảm tưởng đọc Thiên gia thi).",
            "essence": "Gắn bó văn học với vận mệnh đất nước; viết cho ai? viết để làm gì? rồi mới quyết định viết như thế nào?"
          },
          {
            "term": "Văn chính luận Hồ Chí Minh",
            "definition": "Đặc trưng bởi hệ thống lập luận chặt chẽ, luận cứ xác thực không thể bác bỏ, lời văn đanh thép hùng hồn nhưng chan chứa tình cảm nhân văn sâu sắc.",
            "example": "Bản 'Tuyên ngôn Độc lập' (1945) là áng thiên cổ hùng văn đặt nền móng pháp lý và đạo lý khẳng định quyền độc lập, tự do thiêng liêng của dân tộc Việt Nam.",
            "essence": "Sức mạnh thuyết phục bắt nguồn từ chân lý thời đại và tình yêu thương vô bờ bến đối với giống nòi."
          }
        ],
        "rules": [
          {
            "statement": "Nghệ thuật mở đầu văn bản chính luận trong Tuyên ngôn Độc lập",
            "meaning": "Mở đầu bản Tuyên ngôn, Người trích dẫn Tuyên ngôn Độc lập 1776 của Mỹ và Tuyên ngôn Nhân quyền & Dân quyền 1791 của Pháp để tạo cơ sở pháp lý vững chắc có giá trị quốc tế không ai có thể phủ nhận.",
            "example": "'Nước Pháp và nước Mỹ đã tự hào về quyền tự do bình đẳng, thì quyền bình đẳng dân tộc của Việt Nam cũng là chân lý hiển nhiên'.",
            "essence": "Chiến thuật gậy ông đập lưng ông: Dùng chính lý tưởng tiến bộ của tổ tiên đối phương để bác bỏ luận điệu xâm lược của chúng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích giá trị pháp lý và nhân văn của câu kết bản 'Tuyên ngôn Độc lập' năm 1945.",
            "steps": [
              "Bước 1: Trích dẫn câu kết: 'Nước Việt Nam có quyền hưởng tự do và độc lập, và sự thật đã thành một nước tự do độc lập. Toàn thể dân tộc Việt Nam quyết đem tất cả tinh thần và lực lượng, tính mạng và của cải để giữ vững quyền tự do, độc lập ấy'.",
              "Bước 2: Phân tích cơ sở pháp lý: Khẳng định quyền lợi chính đáng và hiện thực đã hoàn thành (sự thật lịch sử).",
              "Bước 3: Phân tích ý chí sắt đá: Lời thề quyết tâm hy sinh tất cả ('tính mạng và của cải') để bảo vệ nền tự do vừa giành được.",
              "Bước 4: Đánh giá: Đó là lời tuyên bố đanh thép trước toàn thế giới về chủ quyền không thể xâm phạm của Tổ quốc."
            ],
            "answer": "Câu kết là sự tổng hòa giữa chân lý pháp lý sáng ngời và ý chí sắt đá quật cường của triệu triệu người Việt Nam sẵn sàng hy sinh để bảo vệ nền độc lập tự do."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chỉ tiếp cận Tuyên ngôn Độc lập như một văn kiện lịch sử thuần túy mà bỏ quên giá trị văn học chính luận mẫu mực của tác phẩm.",
            "why": "Đây là tác phẩm đỉnh cao của thể loại văn chính luận với nghệ thuật lập luận, kết cấu và ngôn từ bậc thầy."
          }
        ]
      },
      {
        "id": "ch07",
        "title": "Bài 7: Nhìn lại một chặng đường văn học",
        "description": "Khái quát tiến trình văn học Việt Nam từ 1945 đến hết thế kỉ XX; các khuynh hướng sử thi, cảm hứng lãng mạn và sự đổi mới mạnh mẽ sau 1986; đọc hiểu truyện ngắn Vợ nhặt và Chiếc thuyền ngoài xa.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Vợ nhặt (Kim Lân)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Chiếc thuyền ngoài xa (Nguyễn Minh Châu)", "hasRealContent": true },
          { "id": "l03", "title": "Khái quát văn học Việt Nam từ 1945 đến hết thế kỉ XX", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Văn học giai đoạn đổi mới (từ 1986)",
            "definition": "Chuyển từ khuynh hướng sử thi và cảm hứng lãng mạn ca ngợi tập thể sang cảm hứng thế sự, đời tư; khám phá con người trong chiều sâu bi kịch, góc khuất tâm lý và số phận cá nhân phức tạp.",
            "example": "'Chiếc thuyền ngoài xa' của Nguyễn Minh Châu đặt ra câu hỏi nhức nhối về mối quan hệ giữa nghệ thuật và cuộc đời, giữa cái đẹp bề ngoài và nỗi đau hiện thực bên trong.",
            "essence": "Văn học trở về với chức năng nhân bản đích thực: bảo vệ nhân phẩm và lắng nghe nỗi trăn trở của từng số phận con người."
          },
          {
            "term": "Tình huống truyện độc đáo",
            "definition": "Là sự kiện, hoàn cảnh éo le bất thường tạo nên bước ngoặt thúc đẩy tính cách nhân vật bộc lộ và tư tưởng chủ đề tác phẩm phát sáng.",
            "example": "Tình huống Tràng 'nhặt' được vợ giữa những ngày nạn đói khủng khiếp năm 1945 trong truyện ngắn của Kim Lân.",
            "essence": "Tình huống truyện là lát cắt vàng chứa đựng toàn bộ giọt máu sự sống của tác phẩm."
          }
        ],
        "rules": [
          {
            "statement": "Quy luật vận động của văn học Việt Nam hiện đại",
            "meaning": "Văn học 1945 - 1975 gắn liền với nhiệm vụ cứu nước mang tính sử thi hoành tráng; văn học sau 1986 hướng nội, đổi mới tư duy nghệ thuật, đề cao tinh thần dân chủ và trách nhiệm công dân.",
            "example": "Từ tượng đài người lính anh hùng trong 'Tây Tiến' đến số phận nhọc nhằn của người đàn bà hàng chài trong 'Chiếc thuyền ngoài xa'.",
            "essence": "Sự phát triển biện chứng từ nhận thức cộng đồng sử thi đến nhận thức cá nhân đa diện."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích nghịch lý giữa cái đẹp nghệ thuật và hiện thực cuộc sống qua phát hiện của người nghệ sĩ nhiếp ảnh Phùng trong 'Chiếc thuyền ngoài xa'.",
            "steps": [
              "Bước 1: Phát hiện thứ nhất - Cái đẹp tuyệt mỹ: Cảnh chiếc thuyền lưới vó ngoài xa trong sương sớm đẹp như 'bức tranh mực tàu của một danh họa thời cổ', khiến tâm hồn Phùng rung động thăng hoa.",
              "Bước 2: Phát hiện thứ hai - Hiện thực tàn nhẫn: Khi thuyền cập bến, bước ra là cảnh người chồng vũ phu đánh đập dã man người vợ hàng chài trong sự câm lặng nhẫn nhục.",
              "Bước 3: Nghịch lý triết lý: Đằng sau cái đẹp lung linh huyền ảo của nghệ thuật lại là nỗi đau đớn quẫn bách của kiếp mưu sinh đói nghèo.",
              "Bước 4: Bài học nghệ thuật: Người nghệ sĩ không được nhìn cuộc đời một cách dễ dãi, hời hợt từ xa mà phải dấn thân vào chiều sâu hiện thực đau xót của con người."
            ],
            "answer": "Nghịch lý cảnh tỉnh người nghệ sĩ: Nghệ thuật chân chính không được tách rời cuộc đời; cái đẹp phải đi liền với lòng trắc ẩn và sự thấu cảm nỗi đau nhân thế."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Lên án người đàn bà hàng chài là nhu nhược, hèn nhát khi kiên quyết xin chánh án Đẩu đừng bắt mình bỏ chồng.",
            "why": "Chị chấp nhận đòn roi vì tình mẫu tử thiêng liêng: đàn con cần một người đàn ông khỏe mạnh để chèo chống con thuyền vượt qua phong ba biển cả."
          }
        ]
      },
      {
        "id": "ch08",
        "title": "Bài 8: Dữ liệu trong văn bản thông tin",
        "description": "Cách tiếp cận và phân tích văn bản thông tin; tính xác thực và khách quan của dữ liệu; tôn trọng và bảo vệ quyền sở hữu trí tuệ; kỹ năng viết thư trao đổi công việc chuẩn mực.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Pa-ra-na (Trích Nhiệt đới buồn – Claude Lévi-Strauss)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Giáo dục khai phóng ở Việt Nam nhìn từ Đông Kinh Nghĩa Thục", "hasRealContent": true },
          { "id": "l03", "title": "Thực hành tiếng Việt: Tôn trọng và bảo vệ quyền sở hữu trí tuệ", "hasRealContent": true },
          { "id": "l04", "title": "Viết: Viết thư trao đổi về công việc hoặc một vấn đề đáng quan tâm", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Văn bản thông tin và Dữ liệu đa phương tiện",
            "definition": "Là văn bản nhằm mục đích cung cấp tri thức, số liệu, sự kiện khách quan cho người đọc; kết hợp linh hoạt văn bản ngôn ngữ với hình ảnh, bảng biểu, sơ đồ đồ họa (Infographic).",
            "example": "Bài viết phân tích mô hình giáo dục khai phóng của Đông Kinh Nghĩa Thục đầu thế kỉ XX kèm tư liệu lịch sử và hình ảnh nhân chứng.",
            "essence": "Cung cấp thông tin chính xác, minh bạch, kiểm chứng được giúp mở rộng hiểu biết xã hội."
          },
          {
            "term": "Quyền sở hữu trí tuệ trong thời đại số",
            "definition": "Là quyền của tổ chức, cá nhân đối với tài sản trí tuệ bao gồm quyền tác giả (tác phẩm văn học, âm nhạc, phần mềm) và quyền sở hữu công nghiệp (sáng chế, nhãn hiệu).",
            "example": "Trích dẫn nội dung từ một bài báo khoa học phải ghi rõ tên tác giả, tên công trình và năm xuất bản.",
            "essence": "Tôn trọng quyền tác giả là nền tảng thúc đẩy sáng tạo khoa học và văn hóa pháp lý văn minh."
          }
        ],
        "rules": [
          {
            "statement": "Quy chuẩn viết thư trao đổi công việc chuyên nghiệp",
            "meaning": "Thư phải có tiêu đề rõ ràng, lời chào trang trọng, trình bày mục đích ngắn gọn đi thẳng vào trọng tâm, nêu đề xuất cụ thể kèm thời hạn phản hồi và lời cảm ơn kết thư lịch sự.",
            "example": "Email gửi đối tác xin lịch hẹn phỏng vấn tuyển dụng hoặc đề xuất hợp tác dự án nghiên cứu học tập.",
            "essence": "Kỹ năng giao tiếp bằng văn bản thể hiện tính chuyên nghiệp và văn hóa ứng xử của công dân toàn cầu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày 3 nguyên tắc vàng khi trích dẫn tài liệu trong bài viết học thuật để tránh vi phạm quyền tác giả.",
            "steps": [
              "Bước 1: Trích dẫn trực tiếp: Phải đặt toàn bộ câu chữ trích dẫn trong dấu ngoặc kép và chỉ rõ nguồn xuất bản cụ thể.",
              "Bước 2: Trích dẫn gián tiếp (diễn giải lại - paraphrase): Dùng văn phong của mình nhưng vẫn phải dẫn nguồn tác giả gốc của ý tưởng.",
              "Bước 3: Lập danh mục tài liệu tham khảo đầy đủ ở cuối bài viết theo chuẩn quy định (như chuẩn APA hoặc IEEE)."
            ],
            "answer": "3 nguyên tắc: Đặt trong ngoặc kép khi trích trực tiếp, Ghi nhận tác giả khi diễn đạt lại, và Lập danh mục tài liệu tham khảo minh bạch."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Sao chép nguyên văn đoạn văn của người khác rồi chỉ thay đổi vài từ đồng nghĩa và coi đó là bài viết của mình.",
            "why": "Đây vẫn là hành vi đạo văn ý tưởng tinh vi nếu không dẫn nguồn gốc của tài liệu tham khảo."
          }
        ]
      },
      {
        "id": "ch09",
        "title": "Bài 9: Văn học và cuộc đời",
        "description": "Mối quan hệ mật thiết giữa văn học và đời sống; triết lý nhân sinh trong thi ca và kịch nghệ; đọc hiểu Vội vàng, Ông già và biển cả, Hồn Trương Ba da hàng thịt; giữ gìn và phát triển sự trong sáng của tiếng Việt.",
        "lessons": [
          { "id": "l01", "title": "Đọc: Vội vàng (Xuân Diệu)", "hasRealContent": true },
          { "id": "l02", "title": "Đọc: Trở về (Trích Ông già và biển cả – Hemingway)", "hasRealContent": true },
          { "id": "l03", "title": "Đọc: Hồn Trương Ba, da hàng thịt (Lưu Quang Vũ)", "hasRealContent": true },
          { "id": "l04", "title": "Thực hành tiếng Việt: Giữ gìn và phát triển tiếng Việt", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Xung đột kịch Hồn và Xác (Lưu Quang Vũ)",
            "definition": "Mâu thuẫn đau đớn giữa tâm hồn thanh cao, nhân hậu, trong sạch của Trương Ba với thân xác thô phàm, dung tục của anh hàng thịt mà hồn phải nương náu.",
            "example": "Màn đối thoại bi kịch giữa Hồn Trương Ba và Xác hàng thịt: Hồn khinh bỉ xác nhưng vẫn bị bản năng của xác thao túng, làm biến chất bản thân.",
            "essence": "Khát vọng được sống toàn vẹn, sống là chính mình: Con người không thể sống chắp vá, bên trong một đằng bên ngoài một nẻo."
          },
          {
            "term": "Nguyên lý Tảng băng trôi (The Iceberg Theory)",
            "definition": "Quan niệm nghệ thuật của Hemingway: Nhà văn chỉ viết 1 phần nổi trên mặt nước (câu chữ, hành động giản dị), 7 phần chìm dưới mặt nước để cho người đọc tự cảm nhận, suy ngẫm và đồng sáng tạo.",
            "example": "Cuộc chiến của ông lão Santiago với con cá kiếm khổng lồ biểu tượng cho vẻ đẹp kiên cường, bất khuất của con người trước tự nhiên khắc nghiệt.",
            "essence": "Văn chương cô đọng tối đa, mở ra khoảng không vô hạn cho chiều sâu tư tưởng."
          }
        ],
        "rules": [
          {
            "statement": "Quan niệm sống vội vàng, gắn bó tha thiết với cuộc đời của Xuân Diệu",
            "meaning": "Thời gian tuyến tính một đi không trở lại, tuổi trẻ ngắn ngủi; con người phải sống mãnh liệt, cuống quýt, tận hiến và tận hưởng từng giây phút tươi đẹp của cuộc đời nơi trần thế.",
            "example": "'Mau đi thôi! Mùa chưa ngả chiều hôm / Ta muốn ôm / Cả sự sống mới bắt đầu mơn mởn'.",
            "essence": "Tuyên ngôn nhân sinh đầy tích cực, nâng niu sự sống và tuổi thanh xuân của cái tôi Thơ mới."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích ý nghĩa triết lý nhân sinh qua quyết định cuối cùng của nhân vật Hồn Trương Ba: thà chết hẳn chứ không chấp nhận nhập vào xác cu Tị.",
            "steps": [
              "Bước 1: Bối cảnh lựa chọn: Đế Thích cho Trương Ba cơ hội nhập vào xác cu Tị vừa chết để tiếp tục tồn tại.",
              "Bước 2: Sự từ chối kiên quyết: Trương Ba hiểu rằng nhập vào cu Tị sẽ tiếp tục chuỗi ngày sống giả tạo, gượng ép và làm khổ người khác.",
              "Bước 3: Lựa chọn cái chết tự nhiên: Trương Ba xin cho cu Tị được sống lại bằng chính linh hồn của nó, còn mình thanh thản tan biến vào cây cỏ hoa vườn.",
              "Bước 4: Bài học triết lý: Cuộc sống chỉ có ý nghĩa khi con người được sống trung thực, hài hòa giữa thể xác và tâm hồn; chấp nhận quy luật sinh tử tự nhiên thay vì sống kéo dài một cách vô nghĩa."
            ],
            "answer": "Quyết định của Trương Ba thể hiện sự chiến thắng của nhân cách cao đẹp: Thà chết để giữ trọn vẹn sự thanh sạch của tâm hồn còn hơn sống chắp vá, tha hóa làm khổ người thân."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng quan niệm 'Vội vàng' của Xuân Diệu cổ vũ lối sống hưởng thụ ích kỷ, buông thả.",
            "why": "Xuân Diệu kêu gọi sống hết mình, cống hiến và trân trọng từng phút giây thanh xuân, đối lập hoàn toàn với chủ nghĩa hưởng lạc vô trách nhiệm."
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
        "title": "Unit 1: Life Stories We Admire",
        "description": "Vocabulary about biographies and historical figures; Past simple vs Past continuous with when/while; compound adjectives; reading and writing about admirable life stories.",
        "lessons": [
          { "id": "l01", "title": "Getting Started & Language Focus", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading & Speaking about Inspiring Lives", "hasRealContent": true },
          { "id": "l03", "title": "Skills: Listening & Writing a Biography", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Past Simple vs Past Continuous",
            "definition": "Past continuous describes an action in progress in the past when another shorter action (Past simple) interrupted it: When S + V(past simple), S + was/were V-ing; or While S + was/were V-ing, S + V(past simple).",
            "example": "While Uncle Ho was working abroad, he traveled to many countries to find a way to liberate Vietnam.",
            "essence": "Expressing background context and specific interrupting events in historical narrative."
          },
          {
            "term": "Compound Adjectives",
            "definition": "Adjectives formed by joining two or more words (often with a hyphen) such as well-known, warm-hearted, hard-working, open-minded.",
            "example": "General Vo Nguyen Giap was a world-famous military strategist admired by people globally.",
            "essence": "Enriching descriptions of character traits and personal achievements concisely."
          }
        ],
        "rules": [
          {
            "statement": "Usage of While and When with Past tenses",
            "meaning": "Use 'While' before continuous long actions (While + Past Continuous); use 'When' before sudden short actions (When + Past Simple) or concurrent events.",
            "example": "When I arrived home, my family was having dinner.",
            "essence": "Time relationships must match the aspectual nature of the events."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Combine two sentences using 'when' or 'while': 'Isaac Newton was sitting under an apple tree.' and 'An apple fell on his head.'",
            "steps": [
              "Step 1: Identify the continuous background action: sitting under an apple tree -> Past Continuous.",
              "Step 2: Identify the short interrupting action: an apple fell -> Past Simple.",
              "Step 3: Combine with 'while': While Isaac Newton was sitting under an apple tree, an apple fell on his head.",
              "Step 4: Alternative with 'when': Isaac Newton was sitting under an apple tree when an apple fell on his head."
            ],
            "answer": "While Isaac Newton was sitting under an apple tree, an apple fell on his head."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using Past Continuous for stative verbs: *While I was knowing the answer*.",
            "why": "Stative verbs (know, understand, believe, love) are not used in continuous aspect; use Past Simple instead: While I knew the answer."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Unit 2: A Multicultural World",
        "description": "Vocabulary related to cultural diversity and customs; articles (a, an, the, zero article); intercultural communication and cultural exchange.",
        "lessons": [
          { "id": "l01", "title": "Language: Articles & Cultural Vocabulary", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading & Discussion on Cultural Traditions", "hasRealContent": true },
          { "id": "l03", "title": "Writing: Describing a Cultural Festival", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Definite Article 'The' vs Indefinite 'A/An'",
            "definition": "Use 'a/an' for singular countable nouns mentioned for the first time or non-specific items. Use 'the' when both speaker and listener know what is being referred to, for unique objects (the sun, the earth), or previously mentioned nouns.",
            "example": "I attended a cultural festival yesterday. The festival was colorful and exciting.",
            "essence": "Establishing shared knowledge context between communicators."
          },
          {
            "term": "Zero Article (Ø)",
            "definition": "No article is used before plural countable nouns or uncountable nouns in general statements, proper names of people, most countries, sports, and languages.",
            "example": "Vietnam has rich cultural traditions. She speaks English fluently.",
            "essence": "Generalizing abstract concepts and specific proper identities."
          }
        ],
        "rules": [
          {
            "statement": "Geographical names requiring 'The'",
            "meaning": "Use 'the' with plural country names (the United States, the Philippines), mountain ranges (the Himalayas), oceans/seas/rivers (the Pacific Ocean, the Red River), and deserts (the Sahara). Do NOT use 'the' with single mountains (Mount Everest) or single lakes (Lake Geneva).",
            "example": "The Mekong River flows through several Southeast Asian countries.",
            "essence": "Plurality and collective geographical features trigger the definite article."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Fill in the blanks with 'a', 'an', 'the' or 'Ø' (zero article): '___ culture of Vietnam is influenced by ___ Confucianism and Buddhism.'",
            "steps": [
              "Step 1: 'culture of Vietnam' has a defining prepositional phrase 'of Vietnam', making it specific -> use 'The'.",
              "Step 2: 'Confucianism' is an abstract religious/philosophical system -> use zero article 'Ø'.",
              "Step 3: Combine: The culture of Vietnam is influenced by Confucianism and Buddhism."
            ],
            "answer": "The; Ø"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'the' before meals in daily life: *I had the breakfast at 7 AM*.",
            "why": "Names of meals do not take articles unless preceded by an adjective: have breakfast, but have a delicious breakfast."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Unit 3: Green Living",
        "description": "Vocabulary about sustainability, eco-friendly lifestyle, carbon footprint; Relative clauses with which referring to a whole sentence; writing an essay on environmental solutions.",
        "lessons": [
          { "id": "l01", "title": "Language: Relative clauses referring to a whole clause", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading about Zero-Waste Lifestyle", "hasRealContent": true },
          { "id": "l03", "title": "Writing: Problem and Solution Essay on Plastic Waste", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Relative pronoun 'which' referring to a whole clause",
            "definition": "Non-defining relative clause introduced by ', which' modifies and comments on the entire preceding sentence or situation rather than a single noun.",
            "example": "Many young people choose to ride bicycles to school, which helps reduce carbon emissions significantly.",
            "essence": "Creating coherent evaluative commentary and causal links between ideas."
          },
          {
            "term": "Carbon Footprint",
            "definition": "The total amount of greenhouse gases (including carbon dioxide and methane) that are generated by our actions and daily consumption choices.",
            "example": "Switching to plant-based diets and renewable energy reduces your personal carbon footprint.",
            "essence": "Quantitative indicator measuring individual and collective ecological impact."
          }
        ],
        "rules": [
          {
            "statement": "Punctuation rule for sentential relative 'which'",
            "meaning": "Always place a comma before 'which' when it refers to the whole preceding clause; 'that' can never replace 'which' in this structure.",
            "example": "He refused to use single-use plastic, which impressed everyone in the group.",
            "essence": "Clear boundary marking ensures reader interprets the referent as a full proposition."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Combine using a relative clause: 'More people are recycling household waste. This is beneficial for our planet.'",
            "steps": [
              "Step 1: Identify that 'This' refers to the whole fact 'More people are recycling household waste'.",
              "Step 2: Replace 'This' with ', which'.",
              "Step 3: Form: More people are recycling household waste, which is beneficial for our planet."
            ],
            "answer": "More people are recycling household waste, which is beneficial for our planet."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'that' after a comma to refer to a whole clause: *...household waste, that is beneficial...*",
            "why": "'That' is never used in non-defining relative clauses or to modify full clauses."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Unit 4: Urbanisation",
        "description": "Vocabulary related to smart cities, rural-urban migration, infrastructure; Double comparatives (The more... the more...); discussing urban challenges and future solutions.",
        "lessons": [
          { "id": "l01", "title": "Language: Double Comparatives", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading on Smart City Development", "hasRealContent": true },
          { "id": "l03", "title": "Writing: Advantages and Disadvantages of Megacities", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Double Comparatives (The + comparative, the + comparative)",
            "definition": "Structure expressing proportional relationship where a change in one factor directly causes a corresponding change in another factor.",
            "example": "The more modern a city becomes, the higher the cost of living gets. The more trees we plant, the cleaner the air will be.",
            "essence": "Expressing continuous parallel progression and cause-effect correlation dynamically."
          },
          {
            "term": "Smart City",
            "definition": "An urban area that uses Internet of Things (IoT) sensors, data analytics, and digital technology to manage assets, resources, and services efficiently.",
            "example": "Smart traffic lights automatically adjust timing based on real-time vehicle density to minimize gridlock.",
            "essence": "Technological integration transforming urban governance and sustainability."
          }
        ],
        "rules": [
          {
            "statement": "Word order in double comparative structures",
            "meaning": "Both clauses start with 'The' followed by comparative adjective/adverb/noun, then subject + verb: The + comparative + S + V, the + comparative + S + V.",
            "example": "The more carefully you plan, the better results you will achieve.",
            "essence": "Symmetrical structural balance between dependent and independent clauses."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rewrite using double comparative: 'As cities grow bigger, traffic congestion becomes worse.'",
            "steps": [
              "Step 1: Identify the two changing elements: cities grow bigger -> The bigger cities grow;",
              "Step 2: Traffic congestion becomes worse -> the worse traffic congestion becomes.",
              "Step 3: Combine with parallel symmetry: The bigger cities grow, the worse traffic congestion becomes."
            ],
            "answer": "The bigger cities grow, the worse traffic congestion becomes."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Omitting 'the' before one of the comparatives: *More you practice, the better you become*.",
            "why": "Both parts must strictly start with 'The': The more you practice, the better you become."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Unit 5: The World of Work",
        "description": "Vocabulary about careers, job skills, employment market; Reported speech: statements, questions and reporting verbs; writing a CV and job application letter.",
        "lessons": [
          { "id": "l01", "title": "Language: Reported Speech with Reporting Verbs", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading about Future Job Market Trends", "hasRealContent": true },
          { "id": "l03", "title": "Writing: A Letter of Application for a Part-time Job", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Reported Speech with specialized reporting verbs",
            "definition": "Instead of merely using 'said' or 'told', advanced reporting employs verbs like advise, invite, remind, promise, offer, apologize for, congratulate on.",
            "example": "The manager advised me to improve my digital skills before the interview.",
            "essence": "Accurately conveying speaker's illocutionary intent and pragmatic nuance."
          },
          {
            "term": "Soft Skills vs Hard Skills",
            "definition": "Hard skills are teachable, measurable technical abilities (coding, bookkeeping, operating machinery). Soft skills are interpersonal and emotional competencies (communication, teamwork, adaptability).",
            "example": "In the modern AI era, soft skills like critical thinking and empathy become decisive factors for career promotion.",
            "essence": "Complementary skill architecture required for sustainable employment."
          }
        ],
        "rules": [
          {
            "statement": "Tense backshift rule in reported speech",
            "meaning": "When the reporting verb is in the past (said, asked), verbs in direct speech shift back one tense (Present Simple -> Past Simple; Present Perfect -> Past Perfect; Will -> Would; Can -> Could). Time and place expressions also adapt.",
            "example": "'I am applying for this job today' -> She said that she was applying for that job that day.",
            "essence": "Re-anchoring speech acts to the speaker's past perspective."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Change into reported speech: 'Will you attend the career orientation workshop tomorrow?' Nam asked Lan.",
            "steps": [
              "Step 1: Identify yes/no question structure -> use 'if' or 'whether'.",
              "Step 2: Change pronoun: you -> she.",
              "Step 3: Backshift modal verb: will -> would.",
              "Step 4: Shift time word: tomorrow -> the next day / the following day.",
              "Step 5: Assemble: Nam asked Lan if she would attend the career orientation workshop the following day."
            ],
            "answer": "Nam asked Lan if she would attend the career orientation workshop the following day."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Maintaining question word order in reported questions: *Nam asked Lan if would she attend...*",
            "why": "Reported questions take affirmative declarative word order: Subject + Verb (if she would attend)."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Unit 6: Artificial Intelligence",
        "description": "Vocabulary about AI, machine intelligence, robotics; Passive voice with modal verbs; debating benefits and potential risks of generative AI.",
        "lessons": [
          { "id": "l01", "title": "Language: Passive Voice with Modals", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading about AI in Daily Life", "hasRealContent": true },
          { "id": "l03", "title": "Writing: Opinion Essay on whether AI will replace humans", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Passive voice with Modal verbs",
            "definition": "Form: Modal verb + be + Past Participle (V3/ed). Used when emphasizing the action or object receiving the action rather than the doer, expressing possibility, necessity, or permission.",
            "example": "Ethical regulations must be established to monitor artificial intelligence development.",
            "essence": "Focusing academic discourse on processes, systems, and institutional policies."
          },
          {
            "term": "Generative AI",
            "definition": "Artificial intelligence systems capable of creating new text, images, video, code, and music in response to human prompts.",
            "example": "Large language models can write essays and translate languages with remarkable fluency.",
            "essence": "Paradigm shift from analytical recognition to creative synthesis."
          }
        ],
        "rules": [
          {
            "statement": "Passive with perfect modals",
            "meaning": "For actions in the past with modals, form: Modal + have been + V3/ed (should have been done, could have been avoided).",
            "example": "The security vulnerability could have been detected much earlier by automated testing tools.",
            "essence": "Evaluating past hypothetical outcomes and responsibilities objectively."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rewrite into passive voice: 'Governments should update legal frameworks to regulate AI algorithms.'",
            "steps": [
              "Step 1: Identify object: 'legal frameworks'.",
              "Step 2: Modal passive structure: should + be + updated.",
              "Step 3: Combine with remaining elements: Legal frameworks should be updated by governments to regulate AI algorithms."
            ],
            "answer": "Legal frameworks should be updated by governments to regulate AI algorithms."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Forgetting 'be' in modal passive: *AI tools should used carefully*.",
            "why": "Modal passive strictly requires base form 'be': should BE used."
          }
        ]
      },
      {
        "id": "ch07",
        "title": "Unit 7: The World of Mass Media",
        "description": "Vocabulary about social media, journalism, fake news detection; Adverbial clauses of manner and comparison (as if, as though); critical media consumption.",
        "lessons": [
          { "id": "l01", "title": "Language: Adverbial clauses with as if / as though", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading on Digital Media Literacy", "hasRealContent": true },
          { "id": "l03", "title": "Writing: Article discussing the impact of social media", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Clauses with 'As if / As though'",
            "definition": "Used to describe how a situation seems. If expressing an untrue/hypothetical situation in the present, use Past Simple/were; if referring to an untrue situation in the past, use Past Perfect (had V3).",
            "example": "He speaks about digital privacy as if he were an expert (in reality he is not).",
            "essence": "Distinguishing between realistic appearance and counterfactual pretense."
          },
          {
            "term": "Media Literacy",
            "definition": "The ability to critically access, analyze, evaluate, and create media messages in various formats, discerning verified facts from biased propaganda or fabricated misinformation.",
            "example": "Checking author credentials and reverse image searching before sharing controversial news headlines.",
            "essence": "Cognitive defense mechanism against information manipulation in the digital age."
          }
        ],
        "rules": [
          {
            "statement": "Subjunctive mood after 'as if / as though'",
            "meaning": "When the comparison is contrary to present fact, 'were' is conventionally used for all persons (as if I were, as if he were).",
            "example": "She acted as though she knew nothing about the incident.",
            "essence": "Formal grammatical signaling of counterfactual reality."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Put the verb into correct form: 'The boy speaks English fluently as if he (live) in London for years (in fact he has never been abroad).'",
            "steps": [
              "Step 1: Check reality: he has never been abroad -> the situation is unreal/hypothetical in relation to the present.",
              "Step 2: Expressing an unreal completed past experience -> use Past Perfect: had lived.",
              "Step 3: Assemble sentence: The boy speaks English fluently as if he had lived in London for years."
            ],
            "answer": "had lived"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Confusing real comparisons with unreal comparisons: *It looks as if it rained* when clouds are actually dark.",
            "why": "If something is likely or true, use real tenses: It looks as if it is going to rain."
          }
        ]
      },
      {
        "id": "ch08",
        "title": "Unit 8: Wildlife Conservation",
        "description": "Vocabulary about biodiversity, endangered species, poaching, natural habitats; Complex sentences with adverbial clauses of condition and concession (although, even though, unless, provided that).",
        "lessons": [
          { "id": "l01", "title": "Language: Concession and Condition Clauses", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading about Endangered Wildlife Protection in VN", "hasRealContent": true },
          { "id": "l03", "title": "Writing: Proposal for a Wildlife Conservation Campaign", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Concession Clauses (Although, Even though, In spite of, Despite)",
            "definition": "Express contrast between two ideas. Although/Even though are conjunctions followed by a clause (S + V). Despite/In spite of are prepositions followed by a noun phrase or V-ing.",
            "example": "Although severe penalties exist, illegal wildlife trafficking remains a global problem.",
            "essence": "Highlighting paradoxical real-world tensions and unexpected contrasts."
          },
          {
            "term": "Biodiversity Conservation",
            "definition": "The practice of protecting, managing, and preserving animal and plant species and their natural ecosystems from extinction and habitat fragmentation.",
            "example": "Establishing national parks like Cuc Phuong and Phong Nha-Ke Bang protects endemic endangered species.",
            "essence": "Maintaining ecological balance crucial for planetary resilience."
          }
        ],
        "rules": [
          {
            "statement": "Transforming between 'Although' and 'Despite / In spite of'",
            "meaning": "Although + S + V + O ⇔ Despite / In spite of + Noun phrase / Gerund (V-ing) / the fact that + clause.",
            "example": "Although the weather was harsh -> Despite the harsh weather.",
            "essence": "Syntax flexibility between clausal subordination and phrasal nominalization."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Rewrite without changing meaning: 'Although park rangers worked tirelessly, they could not prevent all poaching activities.' (Use 'Despite')",
            "steps": [
              "Step 1: Convert clause 'park rangers worked tirelessly' to noun phrase: 'park rangers' tireless efforts' or gerund: 'working tirelessly'.",
              "Step 2: Combine with 'Despite': Despite park rangers' tireless efforts, they could not prevent all poaching activities.",
              "Step 3: Alternatively: Despite working tirelessly, park rangers could not prevent all poaching activities."
            ],
            "answer": "Despite park rangers' tireless efforts, they could not prevent all poaching activities."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'Although' and 'But' in the same sentence: *Although it rained, but they went on patrol*.",
            "why": "English requires only one conjunction per contrast link: Although it rained, they went on patrol."
          }
        ]
      },
      {
        "id": "ch09",
        "title": "Unit 9: Career Paths",
        "description": "Vocabulary about career choices, vocational qualifications, university pathways; Phrasal verbs related to work and education (take up, carry out, get on with, look forward to); discussing career orientation.",
        "lessons": [
          { "id": "l01", "title": "Language: Work-related Phrasal Verbs", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading on Vocational Training vs University Degrees", "hasRealContent": true },
          { "id": "l03", "title": "Writing: Essay on choosing a career path based on passion or market demand", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Phrasal Verbs (Three-part phrasal verbs)",
            "definition": "Combinations of Verb + Adverb + Preposition that act as a single semantic unit (e.g., look forward to, come up with, run out of, keep up with). They are inseparable and always take an object.",
            "example": "Young graduates must keep up with technological advancements in their profession.",
            "essence": "Idiomatic authenticity in natural spoken and written English discourse."
          },
          {
            "term": "Vocational Education and Training (VET)",
            "definition": "Education focused on practical skills and hands-on preparation for specific trades and technical careers, offering direct pathways into the workforce.",
            "example": "Many school-leavers choose vocational colleges for culinary arts or automotive mechanics instead of 4-year academic degrees.",
            "essence": "Practical workforce readiness aligned with immediate industrial needs."
          }
        ],
        "rules": [
          {
            "statement": "Object placement with separable phrasal verbs",
            "meaning": "With separable two-part phrasal verbs (take on, fill out), if the object is a pronoun (it, them), it MUST go between verb and particle: fill it out (NOT *fill out it*).",
            "example": "Here is the application form; please fill it out carefully.",
            "essence": "Rhythmic constraints of English phonology prioritizing weak pronoun stress internally."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Replace the underlined phrase with an appropriate phrasal verb: 'She decided to start learning graphic design to improve her job prospects.'",
            "steps": [
              "Step 1: 'start learning an activity/hobby' translates to phrasal verb 'take up'.",
              "Step 2: Replace: She decided to take up graphic design to improve her job prospects."
            ],
            "answer": "take up"
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Placing pronouns after inseparable or three-part phrasal verbs: *I look forward to meet you*.",
            "why": "'To' in 'look forward to' is a preposition, which must be followed by a noun or gerund: look forward to meeting you."
          }
        ]
      },
      {
        "id": "ch10",
        "title": "Unit 10: Lifelong Learning",
        "description": "Vocabulary about continuous education, self-improvement, online learning platforms; Mixed conditional sentences (Type 2 + Type 3); reflecting on personal learning strategies for adulthood.",
        "lessons": [
          { "id": "l01", "title": "Language: Mixed Conditionals", "hasRealContent": true },
          { "id": "l02", "title": "Skills: Reading on Lifelong Learning in the 21st Century", "hasRealContent": true },
          { "id": "l03", "title": "Writing: Personal Development Plan for Lifelong Learning", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Mixed Conditionals (Type 3 + Type 2 & Type 2 + Type 3)",
            "definition": "Conditionals where the time of the if-clause is different from the time of the main clause. Common mix: Past condition (Type 3: If + had V3) with Present result (Type 2: would + V-base).",
            "example": "If I had practiced English regularly during high school, I would be completely confident in international communication today.",
            "essence": "Connecting past decisions with enduring present reality and identity."
          },
          {
            "term": "Lifelong Learning",
            "definition": "The ongoing, voluntary, and self-motivated pursuit of knowledge for either personal or professional reasons throughout life.",
            "example": "Professionals enrolling in evening coding bootcamps to transition into data science.",
            "essence": "Essential survival mindset in an era of rapid technological disruption."
          }
        ],
        "rules": [
          {
            "statement": "Mixed Conditional Type 3 condition with Type 2 result",
            "meaning": "If + S + had (not) + V3/ed [past action], S + would/could (not) + V-base [present state/consequence].",
            "example": "If she had accepted that scholarship last year, she would be studying in Canada now.",
            "essence": "Counterfactual past causing counterfactual present."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Combine using a mixed conditional: 'He didn't learn computer programming in college. Now he is unable to apply for this software engineer position.'",
            "steps": [
              "Step 1: Past condition: He didn't learn -> If he had learned computer programming in college.",
              "Step 2: Present consequence: He cannot apply -> he would be able to apply for this software engineer position now.",
              "Step 3: Combine: If he had learned computer programming in college, he would be able to apply for this software engineer position now."
            ],
            "answer": "If he had learned computer programming in college, he would be able to apply for this software engineer position now."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Using 'would have V3' in both clauses: *If he would have studied, he would have...*",
            "why": "The if-clause never contains 'would'; use Past Perfect (had studied) in the if-clause."
          }
        ]
      }
    ]
  },
  "lich-su": {
    "id": "lich-su",
    "name": "Lịch sử",
    "icon": "🏛️",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Thế giới trong và sau Chiến tranh lạnh",
        "description": "Sự hình thành Trật tự hai cực Ianta, nguồn gốc và diễn biến Chiến tranh lạnh, sự sụp đổ của trật tự hai cực và xu thế phát triển của thế giới sau Chiến tranh lạnh (đa cực, hòa hoãn, toàn cầu hóa).",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Sự hình thành Trật tự thế giới hai cực Ianta", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Chiến tranh lạnh và xu thế đa cực", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Trật tự thế giới hai cực Ianta",
            "definition": "Là trật tự thế giới mới được thiết lập sau Chiến tranh thế giới thứ hai dựa trên những thỏa thuận của ba cường quốc Liên Xô, Mỹ, Anh tại Hội nghị Ianta (tháng 2/1945), phân chia phạm vi ảnh hưởng ở châu Âu và châu Á do hai siêu cường Mỹ và Liên Xô đứng đầu.",
            "example": "Liên Xô ảnh hưởng ở Đông Âu, Bắc Triều Tiên; Mỹ và phương Tây ảnh hưởng ở Tây Âu, Nam Triều Tiên.",
            "essence": "Sự đối đầu mang tính ý thức hệ và quân sự chi phối toàn bộ quan hệ quốc tế trong nửa sau thế kỉ XX."
          },
          {
            "term": "Chiến tranh lạnh (Cold War)",
            "definition": "Là tình trạng đối đầu căng thẳng toàn diện giữa hai phe tư bản chủ nghĩa do Mỹ cầm đầu và xã hội chủ nghĩa do Liên Xô đứng đầu (1947 - 1989) trên mọi lĩnh vực chính trị, kinh tế, quân sự, tư tưởng nhưng không nổ ra xung đột vũ trang trực tiếp giữa hai siêu cường.",
            "example": "Biểu hiện bằng chạy đua vũ trang hạt nhân, thành lập các khối quân sự NATO và Vác-sa-va, các cuộc chiến tranh cục bộ (Triều Tiên, Việt Nam).",
            "essence": "Cuộc chiến tranh cân não tiêu tốn khổng lồ của cải và tiềm lực của nhân loại."
          }
        ],
        "rules": [
          {
            "statement": "Xu thế phát triển của thế giới sau Chiến tranh lạnh",
            "meaning": "Sau khi Trật tự hai cực sụp đổ (1991), thế giới chuyển biến theo 4 xu thế lớn: (1) Hòa bình, hợp tác và phát triển là xu thế chủ đạo; (2) Trật tự thế giới đa cực nhiều trung tâm đang hình thành; (3) Các quốc gia điều chỉnh chiến lược lấy phát triển kinh tế làm trọng tâm; (4) Quá trình toàn cầu hóa diễn ra mạnh mẽ.",
            "example": "Sự trỗi dậy của các trung tâm kinh tế - chính trị như Liên minh châu Âu (EU), Trung Quốc, Nhật Bản, Ấn Độ, ASEAN.",
            "essence": "Hợp tác cùng phát triển thay thế tư duy đối đầu đối kháng một mất một còn."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân tích tác động của việc chấm dứt Chiến tranh lạnh đối với khu vực Đông Nam Á.",
            "steps": [
              "Bước 1: Chấm dứt tình trạng đối đầu giữa hai nhóm nước: Khối ASEAN và nhóm các nước Đông Dương.",
              "Bước 2: Mở đường giải quyết hòa bình vấn đề Campuchia bằng Hiệp định Paris năm 1991.",
              "Bước 3: Tạo điều kiện mở rộng ASEAN: Việt Nam gia nhập năm 1995, tiến tới hiện thực hóa ý tưởng một ASEAN quy tụ toàn bộ 10 quốc gia Đông Nam Á.",
              "Bước 4: Thúc đẩy hội nhập kinh tế khu vực: Chuyển trọng tâm từ liên minh an ninh chính trị sang xây dựng Cộng đồng kinh tế vững mạnh."
            ],
            "answer": "Chấm dứt Chiến tranh lạnh mở ra kỷ nguyên hòa bình, hòa giải dân tộc và hội nhập toàn diện, giúp ASEAN trở thành tổ chức hợp tác khu vực thành công hàng đầu."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng sau Chiến tranh lạnh thế giới đã hoàn toàn chấm dứt chiến tranh và xung đột vũ trang.",
            "why": "Nguy cơ chiến tranh thế giới bị đẩy lùi nhưng xung đột cục bộ, sắc tộc, tôn giáo, khủng bố và tranh chấp chủ quyền vẫn diễn biến phức tạp ở nhiều khu vực."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: ASEAN: Những chặng đường lịch sử",
        "description": "Quá trình thành lập và phát triển của Hiệp hội các quốc gia Đông Nam Á (ASEAN), các giai đoạn phát triển, xây dựng Cộng đồng ASEAN trên 3 trụ cột vững chắc, thời cơ và thách thức của Việt Nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 3: Quá trình hình thành và phát triển của ASEAN", "hasRealContent": true },
          { "id": "l02", "title": "Bài 4: Cộng đồng ASEAN: Thách thức và triển vọng", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hiệp hội các quốc gia Đông Nam Á (ASEAN)",
            "definition": "Được thành lập ngày 8/8/1967 tại Băng Cốc (Thái Lan) với 5 nước sáng lập (Indonesia, Malaysia, Philippines, Singapore, Thái Lan). Mục tiêu: thúc đẩy tăng trưởng kinh tế, tiến bộ xã hội và duy trì hòa bình, an ninh khu vực.",
            "example": "Hiến chương ASEAN có hiệu lực năm 2008 tạo tư cách pháp nhân và khuôn khổ thể chế chính thức cho toàn khối.",
            "essence": "Tổ chức liên kết khu vực tự cường trên tinh thần tự nguyện và thống nhất trong đa dạng."
          },
          {
            "term": "Cộng đồng ASEAN (thành lập ngày 31/12/2015)",
            "definition": "Là một thực thể liên kết chặt chẽ hoạt động dựa trên 3 trụ cột then chốt: (1) Cộng đồng Chính trị - An ninh (APSC); (2) Cộng đồng Kinh tế (AEC); (3) Cộng đồng Văn hóa - Xã hội (ASCC).",
            "example": "Cộng đồng Kinh tế AEC tạo nên một thị trường chung và cơ sở sản xuất thống nhất, tự do lưu chuyển hàng hóa, dịch vụ, vốn và lao động có tay nghề.",
            "essence": "Tầm nhìn chiến lược hướng tới một khu vực hòa bình, thịnh vượng và lấy người dân làm trung tâm."
          }
        ],
        "rules": [
          {
            "statement": "'Phương cách ASEAN' (The ASEAN Way)",
            "meaning": "Nguyên tắc hoạt động độc đáo của ASEAN dựa trên: Tôn trọng chủ quyền độc lập và toàn vẹn lãnh thổ; Không can thiệp vào công việc nội bộ của nhau; Giải quyết hòa bình các tranh chấp; và Ra quyết định dựa trên sự đồng thuận (consensus) và tham vấn.",
            "example": "Các nước thành viên luôn kiên trì đối thoại kín và dung hòa lợi ích để đạt đồng thuận chung mà không dùng biện pháp áp đặt cưỡng chế.",
            "essence": "Bảo đảm tính bền vững và sự đoàn kết giữa các quốc gia có thể chế chính trị và văn hóa rất đa dạng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Việc Việt Nam gia nhập ASEAN vào ngày 28/7/1995 có ý nghĩa chiến lược gì đối với công cuộc Đổi mới đất nước?",
            "steps": [
              "Bước 1: Phá vỡ hoàn toàn thế bao vây cô lập cấm vận về chính trị và ngoại giao.",
              "Bước 2: Mở ra thị trường thương mại và đầu tư rộng lớn trong khu vực, tạo đà cho nền kinh tế hội nhập quốc tế.",
              "Bước 3: Tạo lập môi trường hòa bình, ổn định lâu dài ở khu vực lân cận phục vụ công cuộc xây dựng đất nước.",
              "Bước 4: Nâng cao vị thế và uy tín quốc tế của Việt Nam trên trường quốc tế."
            ],
            "answer": "Là bước đột phá chiến lược mở đường cho Việt Nam hội nhập kinh tế quốc tế sâu rộng, củng cố môi trường hòa bình phát triển đất nước."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đồng nhất mô hình Cộng đồng ASEAN với Liên minh châu Âu (EU).",
            "why": "EU là mô hình siêu quốc gia (supranational) có đồng tiền chung và cơ quan lập pháp chung; ASEAN là tổ chức liên chính phủ (intergovernmental) tôn trọng quyền tối cao của từng nhà nước."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Cách mạng tháng Tám 1945 và Chiến tranh giải phóng dân tộc (1945 - 1975)",
        "description": "Thắng lợi Cách mạng tháng Tám năm 1945; cuộc kháng chiến chống thực dân Pháp (Chiến dịch Điện Biên Phủ 1954); cuộc kháng chiến chống Mỹ cứu nước (Đại thắng mùa Xuân 1975); nguyên nhân thắng lợi và bài học lịch sử.",
        "lessons": [
          { "id": "l01", "title": "Bài 5: Cách mạng tháng Tám năm 1945 và thành lập nước VNDCCH", "hasRealContent": true },
          { "id": "l02", "title": "Bài 6: Cuộc kháng chiến chống thực dân Pháp (1945 - 1954)", "hasRealContent": true },
          { "id": "l03", "title": "Bài 7: Cuộc kháng chiến chống Mỹ, cứu nước (1954 - 1975)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chiến dịch Điện Biên Phủ (1954)",
            "definition": "Trận quyết chiến chiến lược đỉnh cao trong cuộc kháng chiến chống Pháp. Quân đội Việt Nam đập tan tập đoàn cứ điểm quân sự mạnh nhất Đông Dương của Pháp, 'lừng lẫy năm châu, chấn động địa cầu', buộc Pháp phải ký Hiệp định Giơ-ne-vơ công nhận độc lập chủ quyền của ba nước Đông Dương.",
            "example": "Quyết định chuyển phương châm tác chiến từ 'Đánh nhanh thắng nhanh' sang 'Đánh chắc tiến chắc' của Đại tướng Võ Nguyên Giáp.",
            "essence": "Mẫu mực của nghệ thuật chiến tranh nhân dân, đập tan ý chí xâm lược của chủ nghĩa thực dân kiểu cũ."
          },
          {
            "term": "Đại thắng mùa Xuân 1975",
            "definition": "Đỉnh cao là Chiến dịch Hồ Chí Minh lịch sử giải phóng hoàn toàn miền Nam ngày 30/4/1975, kết thúc 21 năm kháng chiến chống Mỹ và 30 năm chiến tranh giải phóng dân tộc, thống nhất trọn vẹn non sông.",
            "example": "Xe tăng húc đổ cổng Dinh Độc Lập trưa ngày 30/4/1975 chấm dứt hoàn toàn chế độ ngụy quyền Sài Gòn.",
            "essence": "Mở ra kỷ nguyên độc lập, tự do và cả nước cùng đi lên chủ nghĩa xã hội."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên nhân thắng lợi cốt lõi của các cuộc chiến tranh giải phóng",
            "meaning": "Sự lãnh đạo đúng đắn, sáng suốt của Đảng Cộng sản Việt Nam đứng đầu là Chủ tịch Hồ Chí Minh; Sức mạnh khối đại đoàn kết toàn dân tộc; Nghệ thuật quân sự tài tình và sự ủng hộ giúp đỡ quý báu của bạn bè quốc tế.",
            "example": "Đường lối chiến tranh nhân dân toàn dân, toàn diện, trường kỳ và tự lực cánh sinh.",
            "essence": "Ý chí sắt đá 'Không có gì quý hơn độc lập tự do' kết tinh thành sức mạnh bách chiến bách thắng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao nói Cách mạng tháng Tám năm 1945 là một cuộc cách mạng 'chớp thời cơ' tài tình của Đảng ta?",
            "steps": [
              "Bước 1: Phân tích thời cơ xuất hiện: Ngày 15/8/1945, phát xít Nhật đầu hàng Đồng minh, quân đội Nhật ở Đông Dương tê liệt hoang mang; chính phủ bù nhìn Trần Trọng Kim rệu rã.",
              "Bước 2: Phân tích khoảng thời gian thời cơ tồn tại: Thời cơ chỉ kéo dài từ khi Nhật đầu hàng đến trước khi quân đội Đồng minh (Anh và Tưởng) kéo vào Đông Dương (cuối tháng 8/1945).",
              "Bước 3: Sự chuẩn bị chu đáo: Đảng đã chuẩn bị suốt 15 năm (1930 - 1945) về lực lượng chính trị và vũ trang.",
              "Bước 4: Hành động quyết đoán: Hội nghị toàn quốc của Đảng và Quốc dân Đại hội Tân Trào quyết định phát lệnh Tổng khởi nghĩa giành chính quyền trong cả nước chỉ trong 15 ngày."
            ],
            "answer": "Đảng đã chuẩn bị kỹ lưỡng lực lượng, nhạy bén nắm bắt 'cơ hội ngàn năm có một' khi quân Nhật đầu hàng và kịp thời lãnh đạo nhân dân tổng khởi nghĩa thành công trước khi Đồng minh đổ bộ."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng thắng lợi Cách mạng tháng Tám năm 1945 hoàn toàn là do sự may mắn ngẫu nhiên khi Nhật đầu hàng.",
            "why": "Nếu Đảng và nhân dân không chuẩn bị công phu suốt 15 năm thì thời cơ dù có đến cũng không thể chuyển hóa thành thắng lợi lịch sử."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Công cuộc Đổi mới ở Việt Nam từ năm 1986 đến nay",
        "description": "Bối cảnh lịch sử và nội dung đường lối Đổi mới toàn diện tại Đại hội VI (1986); các thành tựu phát triển kinh tế, chính trị, văn hóa, xã hội và quan hệ đối ngoại sau gần 40 năm Đổi mới.",
        "lessons": [
          { "id": "l01", "title": "Bài 8: Đường lối Đổi mới toàn diện đất nước từ năm 1986", "hasRealContent": true },
          { "id": "l02", "title": "Bài 9: Thành tựu của công cuộc Đổi mới", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Đường lối Đổi mới toàn diện (Đại hội VI - 1986)",
            "definition": "Quyết sách lịch sử của Đảng chuyển đổi nền kinh tế từ cơ chế tập trung quan liêu bao cấp sang nền kinh tế thị trường định hướng xã hội chủ nghĩa; thực hiện đa dạng hóa các hình thức sở hữu; đổi mới tư duy lý luận và mở rộng đối ngoại.",
            "example": "Xóa bỏ chế độ tem phiếu bao cấp, trao quyền tự chủ sản xuất kinh doanh cho nông dân (Khoán 10) và các thành phần kinh tế tư nhân.",
            "essence": "Nhìn thẳng vào sự thật, đánh giá đúng sự thật, nói rõ sự thật để tìm con đường phát triển phù hợp với quy luật khách quan."
          },
          {
            "term": "Kinh tế thị trường định hướng XHCN",
            "definition": "Là nền kinh tế vận hành theo các quy luật của thị trường, có sự quản lý của Nhà nước pháp quyền XHCN dưới sự lãnh đạo của Đảng nhằm mục tiêu: Dân giàu, nước mạnh, dân chủ, công bằng, văn minh.",
            "example": "Kinh tế nhà nước giữ vai trò chủ đạo, kinh tế tư nhân là một động lực quan trọng của nền kinh tế quốc dân.",
            "essence": "Kết hợp sức mạnh phân bổ nguồn lực hiệu quả của thị trường với bản chất ưu việt tiến bộ của chế độ XHCN."
          }
        ],
        "rules": [
          {
            "statement": "Bài học kinh nghiệm sau gần 40 năm Đổi mới",
            "meaning": "Kiên định mục tiêu độc lập dân tộc và chủ nghĩa xã hội trên nền tảng chủ nghĩa Mác - Lênin và tư tưởng Hồ Chí Minh; Luôn lấy dân làm gốc, nhân dân là trung tâm và là chủ thể của công cuộc Đổi mới; Chủ động thích ứng linh hoạt với bối cảnh quốc tế.",
            "example": "Đất nước chưa bao giờ có được cơ đồ, tiềm lực, vị thế và uy tín quốc tế như ngày nay.",
            "essence": "Đổi mới không phải là thay đổi mục tiêu XHCN mà là tìm ra con đường và bước đi đúng đắn nhất để hiện thực hóa mục tiêu đó."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày 3 thành tựu nổi bật nhất về kinh tế của Việt Nam sau gần 40 năm thực hiện công cuộc Đổi mới.",
            "steps": [
              "Bước 1: Thoát khỏi khủng hoảng kinh tế - xã hội trầm trọng: Từ một nước thiếu ăn phải nhập khẩu lương thực trở thành một trong những quốc gia xuất khẩu gạo và nông sản hàng đầu thế giới.",
              "Bước 2: Quy mô nền kinh tế và thu nhập đầu người tăng vọt: Từ nước nghèo kém phát triển vươn lên nhóm quốc gia có thu nhập trung bình, tốc độ tăng trưởng GDP duy trì mức cao trong khu vực.",
              "Bước 3: Hội nhập kinh tế quốc tế sâu rộng: Tham gia hàng loạt hiệp định thương mại tự do thế hệ mới (CPTPP, EVFTA, RCEP) với kim ngạch xuất nhập khẩu vượt mốc 700 tỷ USD."
            ],
            "answer": "Thành tựu toàn diện: Đảm bảo an ninh lương thực và xuất khẩu nông sản hàng đầu; Tăng trưởng kinh tế bền vững vươn lên mức thu nhập trung bình; Hội nhập kinh tế quốc tế sâu rộng."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng Đổi mới kinh tế đồng nghĩa với việc tư nhân hóa hoàn toàn và từ bỏ định hướng xã hội chủ nghĩa.",
            "why": "Việt Nam phát triển kinh tế thị trường có sự điều tiết của Nhà nước nhằm bảo đảm tiến bộ và công bằng xã hội trong từng bước phát triển."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chủ đề 5: Lịch sử đối ngoại của Việt Nam thời cận - hiện đại",
        "description": "Quá trình hình thành và phát triển của nền ngoại giao Việt Nam thời cận - hiện đại; đường lối đối ngoại độc lập, tự chủ, hòa bình, hữu nghị, hợp tác và phát triển; 'Ngoại giao cây tre' Việt Nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 10: Lịch sử đối ngoại của Việt Nam từ 1945 đến nay", "hasRealContent": true },
          { "id": "l02", "title": "Bài 11: Trường phái 'Ngoại giao cây tre' Việt Nam", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Trường phái 'Ngoại giao cây tre' Việt Nam",
            "definition": "Đường lối đối ngoại đặc sắc do Tổng Bí thư Nguyễn Phú Trọng khái quát: 'Gốc vững, thân chắc, cành uyển chuyển'. Gốc vững là lợi ích quốc gia - dân tộc; Thân chắc là bản lĩnh tự chủ, kiên định; Cành uyển chuyển là sách lược linh hoạt, khôn khéo.",
            "example": "Việt Nam thiết lập quan hệ Đối tác Chiến lược Toàn diện với cả 5 nước thường trực Hội đồng Bảo an Liên Hợp Quốc.",
            "essence": "Biết nhu biết cương, kiên định về nguyên tắc chiến lược nhưng mềm dẻo về sách lược đối ngoại."
          },
          {
            "term": "Chính sách quốc phòng 'Bốn không'",
            "definition": "Là nguyên tắc quốc phòng hòa bình, tự vệ của Việt Nam: Không tham gia liên minh quân sự; Không liên kết với nước này để chống nước kia; Không cho nước ngoài đặt căn cứ quân sự hoặc sử dụng lãnh thổ để chống nước khác; Không sử dụng vũ lực hoặc đe dọa sử dụng vũ lực trong quan hệ quốc tế.",
            "example": "Giải quyết mọi tranh chấp chủ quyền trên Biển Đông bằng biện pháp hòa bình trên cơ sở luật pháp quốc tế và UNCLOS 1982.",
            "essence": "Bảo vệ vững chắc độc lập chủ quyền từ sớm, từ xa mà không tạo ra nguy cơ xung đột vũ trang."
          }
        ],
        "rules": [
          {
            "statement": "Phương châm đối ngoại của Việt Nam hiện nay",
            "meaning": "Việt Nam là bạn, là đối tác tin cậy và là thành viên tích cực, có trách nhiệm trong cộng đồng quốc tế; đa phương hóa, đa dạng hóa các quan hệ quốc tế.",
            "example": "Đảm nhận thành công vai trò Ủy viên không thường trực Hội đồng Bảo an Liên Hợp Quốc và cử lực lượng gìn giữ hòa bình tham gia phái bộ LHQ.",
            "essence": "Hội nhập quốc tế chủ động, tích cực đóng góp vào hòa bình, hợp tác và tiến bộ của nhân loại."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Giải thích hàm ý của hình tượng 'Gốc vững, thân chắc, cành uyển chuyển' trong nghệ thuật ngoại giao Việt Nam.",
            "steps": [
              "Bước 1: Gốc vững: Là lợi ích quốc gia - dân tộc tối cao, là độc lập chủ quyền, là đường lối đối ngoại độc lập tự chủ được soi đường bởi tư tưởng Hồ Chí Minh.",
              "Bước 2: Thân chắc: Là nội lực đất nước vững vàng, là sức mạnh khối đại đoàn kết toàn dân tộc, là bản lĩnh kiên cường trước mọi sóng gió thời đại.",
              "Bước 3: Cành uyển chuyển: Là nghệ thuật ứng biến linh hoạt 'Dĩ bất biến, ứng vạn biến', mềm mại nhưng kiên định, thích ứng nhạy bén với mọi biến động phức tạp của địa chính trị thế giới."
            ],
            "answer": "Hình tượng cây tre phản ánh bản sắc ngoại giao Việt Nam: Kiên định nguyên tắc độc lập tự chủ và lợi ích dân tộc (gốc vững), dựa trên sức mạnh nội lực đất nước (thân chắc), vận dụng sách lược linh hoạt hòa hiếu (cành uyển chuyển)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Hiểu lầm sự mềm dẻo, linh hoạt trong ngoại giao là sự thỏa hiệp vô nguyên tắc.",
            "why": "Ngoại giao Việt Nam luôn lấy lợi ích quốc gia - dân tộc và chủ quyền toàn vẹn lãnh thổ làm nguyên tắc bất di bất dịch."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chủ đề 6: Hồ Chí Minh trong lịch sử Việt Nam",
        "description": "Hành trình tìm đường cứu nước của người thanh niên Nguyễn Tất Thành, sự kết hợp giữa chủ nghĩa yêu nước và chủ nghĩa Mác - Lênin, công lao vĩ đại sáng lập Đảng và khai sinh nước VNDCCH, di sản tư tưởng Hồ Chí Minh.",
        "lessons": [
          { "id": "l01", "title": "Bài 12: Cuộc đời và sự nghiệp cách mạng của Chủ tịch Hồ Chí Minh", "hasRealContent": true },
          { "id": "l02", "title": "Bài 13: Di sản tư tưởng Hồ Chí Minh và ý nghĩa thời đại", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tư tưởng Hồ Chí Minh",
            "definition": "Là hệ thống quan điểm toàn diện và sâu sắc về những vấn đề cơ bản của cách mạng Việt Nam, kết quả của sự vận dụng và phát triển sáng tạo chủ nghĩa Mác - Lênin vào điều kiện cụ thể của Việt Nam, kế thừa và phát triển các giá trị truyền thống tốt đẹp của dân tộc, tiếp thu tinh hoa văn hóa nhân loại.",
            "example": "Tư tưởng về độc lập dân tộc gắn liền với chủ nghĩa xã hội; tư tưởng về đại đoàn kết toàn dân tộc; tư tưởng về xây dựng Đảng trong sạch vững mạnh.",
            "essence": "Tài sản tinh thần vô giá của Đảng và dân tộc, mãi mãi soi đường cho sự nghiệp cách mạng của nhân dân ta."
          },
          {
            "term": "Hành trình tìm đường cứu nước (1911 - 1920)",
            "definition": "Năm 1911, người thanh niên Nguyễn Tất Thành rời bến cảng Nhà Rồng sang phương Tây tìm hiểu cội nguồn văn minh và cách thức đấu tranh. Tháng 7/1920, đọc Sơ thảo Luận cương của Lênin về vấn đề dân tộc và thuộc địa, Người tìm thấy con đường cứu nước duy nhất: Con đường cách mạng vô sản.",
            "example": "'Luận cương của Lênin làm cho tôi rất cảm động, phấn khởi, sáng tỏ, tin tưởng biết bao! Tôi vui mừng đến phát khóc lên' (Hồ Chí Minh).",
            "essence": "Bước ngoặt quyết định đưa phong trào giải phóng dân tộc Việt Nam hòa vào dòng chảy cách mạng vô sản thế giới."
          }
        ],
        "rules": [
          {
            "statement": "Chân lý bất hủ của Chủ tịch Hồ Chí Minh",
            "meaning": "'Không có gì quý hơn độc lập, tự do!' - Lời kêu gọi thiêng liêng vang vọng non sông, là cội nguồn sức mạnh cổ vũ toàn dân tộc đứng lên vượt qua mọi phong ba bão táp đánh thắng mọi kẻ thù xâm lược.",
            "example": "Kháng chiến chống Mỹ cứu nước diễn ra với tinh thần 'Dù có phải đốt cháy cả dãy Trường Sơn cũng phải kiên quyết giành cho được độc lập'.",
            "essence": "Giá trị nhân quyền và chủ quyền thiêng liêng cao nhất của mọi dân tộc trên thế giới."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Điểm khác biệt căn bản trong con đường cứu nước của Nguyễn Ái Quốc so với các bậc tiền bối Phan Bội Châu và Phan Châu Trinh là gì?",
            "steps": [
              "Bước 1: Phan Bội Châu chọn hướng Đông (sang Nhật) cầu viện nước ngoài đánh Pháp; Phan Châu Trinh chọn dựa vào Pháp để cải cách nâng cao dân trí.",
              "Bước 2: Nguyễn Ái Quốc quyết định sang phương Tây - tận sào huyệt của chủ nghĩa thực dân để tìm hiểu bản chất của 'Tự do, Bình đẳng, Bác ái'.",
              "Bước 3: Người nhận ra bản chất áp bức của chủ nghĩa tư bản và tìm thấy ở chủ nghĩa Mác - Lênin con đường cứu nước gắn liền độc lập dân tộc với giải phóng giai cấp vô sản.",
              "Bước 4: Con đường của Người dựa vào sức mạnh tự lực của chính khối liên minh công nông chứ không ảo tưởng vào sự giúp đỡ của ngoại bang."
            ],
            "answer": "Nguyễn Ái Quốc chọn sang phương Tây tìm hiểu thực chất kẻ thù, gắn cuộc đấu tranh dân tộc với cách mạng vô sản thế giới và dựa vào sức mạnh tự giải phóng của quần chúng nhân dân lao động."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng Nguyễn Ái Quốc tiếp nhận chủ nghĩa Mác - Lênin một cách giáo điều, rập khuôn theo mô hình của Liên Xô.",
            "why": "Hồ Chí Minh vận dụng cực kỳ sáng tạo: coi trọng chủ nghĩa yêu nước chân chính, gắn giải phóng dân tộc lên hàng đầu và thành lập Đảng mang bản sắc công - nông - trí thức Việt Nam."
          }
        ]
      }
    ]
  },
  "dia-li": {
    "id": "dia-li",
    "name": "Địa lí",
    "icon": "🌍",
    "chapters": [
      {
        "id": "ch01",
        "title": "Phần 1: Địa lí tự nhiên Việt Nam",
        "description": "Vị trí địa lí và phạm vi lãnh thổ, tính chất nhiệt đới ẩm gió mùa, sự phân hoá đa dạng của thiên nhiên theo Bắc - Nam, Đông - Tây và theo độ cao, sử dụng hợp lí tài nguyên thiên nhiên và bảo vệ môi trường bền vững.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Vị trí địa lí và phạm vi lãnh thổ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Thiên nhiên nhiệt đới ẩm gió mùa", "hasRealContent": true },
          { "id": "l03", "title": "Bài 3: Sự phân hoá đa dạng của thiên nhiên", "hasRealContent": true },
          { "id": "l04", "title": "Bài 5: Vấn đề sử dụng hợp lí tài nguyên thiên nhiên và bảo vệ môi trường", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Vị trí địa lí và Ý nghĩa đối với tự nhiên",
            "definition": "Việt Nam nằm ở rìa phía đông bán đảo Đông Dương, gần trung tâm khu vực Đông Nam Á; nằm hoàn toàn trong vùng nội chí tuyến bán cầu Bắc, tiếp giáp Biển Đông rộng lớn và nằm trên ngã tư đường di lưu sinh vật, luồng gió mùa châu Á.",
            "example": "Quy định thiên nhiên mang tính chất nhiệt đới ẩm gió mùa, thảm thực vật 4 mùa xanh tốt khác biệt hẳn với các vùng khô hạn cùng vĩ độ ở Tây Á và Bắc Phi.",
            "essence": "Tạo nên tính phong phú, đa dạng và tính nhạy cảm trước thiên tai của môi trường tự nhiên nước ta."
          },
          {
            "term": "Gió mùa châu Á tại Việt Nam",
            "definition": "Gồm gió mùa mùa đông (gió mùa Đông Bắc từ áp cao Siberia gây lạnh khô đầu đông, lạnh ẩm mưa phùn cuối đông ở miền Bắc) và gió mùa mùa hạ (gió mùa Tây Nam gây mưa lớn cho Nam Bộ, Tây Nguyên và hiệu ứng phơn khô nóng ở Bắc Trung Bộ).",
            "example": "Dãy Hoàng Liên Sơn và dãy Trường Sơn chắn gió tạo nên sự tương phản khí hậu sâu sắc giữa sườn đón gió và sườn khuất gió.",
            "essence": "Nhịp điệu gió mùa chi phối trực tiếp lịch biểu canh tác nông nghiệp và chế độ thủy văn sông ngòi."
          }
        ],
        "rules": [
          {
            "statement": "Quy luật phân hóa thiên nhiên theo độ cao địa hình",
            "meaning": "Càng lên cao nhiệt độ càng giảm (trung bình giảm 0.6 °C khi lên cao 100 m) và độ ẩm thay đổi, hình thành 3 đai cao sinh thái: Đai nhiệt đới gió mùa chân núi -> Đai cận nhiệt đới gió mùa trên núi -> Đai ôn đới gió mùa trên núi (từ 2600m trở lên ở Hoàng Liên Sơn).",
            "example": "Đỉnh Phan-xi-păng có khí hậu ôn đới quanh năm mát lạnh, có thảm thực vật đỗ quyên và thiết sam ôn đới.",
            "essence": "Địa hình núi non tái hiện lại các đới thiên nhiên theo chiều thẳng đứng."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Giải thích tại sao vùng đồng bằng ven biển Nam Trung Bộ và Tây Nguyên lại có mùa mưa lệch pha nhau rõ rệt?",
            "steps": [
              "Bước 1: Vào đầu mùa hạ: Gió mùa Tây Nam vượt vịnh Bengal thổi vào gây mưa lớn cho Tây Nguyên; khi vượt qua dãy Trường Sơn sang Duyên hải Nam Trung Bộ bị biến tính trở thành gió phơn khô nóng (không có mưa).",
              "Bước 2: Vào thu - đông: Gió mùa Đông Bắc và dải hội tụ nhiệt đới kết hợp bão đi qua Biển Đông đập trực diện vào sườn đón gió Trường Sơn Đông gây mưa lũ đặc biệt lớn cho vùng đồng bằng duyên hải, trong khi Tây Nguyên bước vào mùa khô.",
              "Bước 3: Kết luận: Bức chắn địa hình dãy Trường Sơn kết hợp hướng thổi của các luồng gió mùa là nguyên nhân gây ra hiện tượng mưa lệch pha độc đáo."
            ],
            "answer": "Do bức chắn địa hình Trường Sơn đón gió và khuất gió đối với các luồng gió mùa Tây Nam và gió Đông Bắc qua Biển Đông."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng toàn bộ lãnh thổ Việt Nam đều có mùa đông lạnh giá như nhau.",
            "why": "Gió mùa Đông Bắc bị suy yếu và chặn lại bởi dãy Bạch Mã (vĩ độ 16°B), do đó từ Đà Nẵng trở vào Nam khí hậu mang tính chất cận xích đạo nóng quanh năm, không có mùa đông lạnh."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Phần 2: Địa lí dân cư Việt Nam",
        "description": "Quy mô và cơ cấu dân số Việt Nam, gia tăng dân số, phân bố dân cư không đều, vấn đề lao động và việc làm, quá trình đô thị hoá và tác động đến phát triển kinh tế - xã hội.",
        "lessons": [
          { "id": "l01", "title": "Bài 7: Dân số Việt Nam", "hasRealContent": true },
          { "id": "l02", "title": "Bài 8: Lao động và việc làm", "hasRealContent": true },
          { "id": "l03", "title": "Bài 9: Đô thị hoá ở Việt Nam", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Cơ cấu dân số vàng và Già hóa dân số",
            "definition": "Dân số vàng xuất hiện khi tỉ lệ người trong độ tuổi lao động (15 - 64 tuổi) gấp đôi tỉ lệ người phụ thuộc (dưới 15 và trên 65 tuổi). Đồng thời, Việt Nam cũng là một trong những quốc gia có tốc độ già hóa dân số nhanh hàng đầu thế giới.",
            "example": "Cung cấp nguồn nhân lực dồi dào thu hút đầu tư FDI nhưng đặt ra thách thức lớn về an sinh xã hội, y tế chăm sóc người cao tuổi trong tương lai gần.",
            "essence": "Thời cơ nhân khẩu học quý báu cần được tận dụng tối đa để nâng cao chất lượng nguồn nhân lực và bứt phá năng suất lao động."
          },
          {
            "term": "Đô thị hóa tự giác và bền vững",
            "definition": "Là quá trình mở rộng không gian đô thị, nâng cao tỉ lệ thị dân gắn liền với chuyển dịch cơ cấu kinh tế công nghiệp - dịch vụ và phát triển hạ tầng kỹ thuật hiện đại, bảo vệ môi trường sinh thái.",
            "example": "Các đại đô thị như Hà Nội, TP. Hồ Chí Minh đang phát triển mạng lưới tàu điện đường sắt đô thị (Metro) để giảm ùn tắc giao thông.",
            "essence": "Đô thị là đầu tàu thúc đẩy chuyển giao công nghệ và tăng trưởng kinh tế vùng."
          }
        ],
        "rules": [
          {
            "statement": "Đặc điểm phân bố dân cư tại Việt Nam",
            "meaning": "Dân cư phân bố không đồng đều: Tập trung đông đúc ở đồng bằng và ven biển (Đồng bằng sông Hồng mật độ trên 1000 người/km²), thưa thớt ở miền núi và trung du (Tây Bắc, Tây Nguyên mật độ dưới 100 người/km²); chênh lệch lớn giữa thành thị (khoảng 38-40%) và nông thôn.",
            "example": "Gây mất cân đối giữa nơi thừa lao động thiếu tài nguyên với nơi giàu tài nguyên nhưng khan hiếm lao động.",
            "essence": "Phân bố dân cư chịu sự chi phối tổng hợp của điều kiện tự nhiên và lịch sử khai thác lãnh thổ."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao việc giải quyết việc làm đang là vấn đề kinh tế - xã hội gay gắt hàng đầu ở Việt Nam hiện nay?",
            "steps": [
              "Bước 1: Nguồn cung lao động lớn: Mỗi năm có hơn 1 triệu thanh niên bước vào độ tuổi lao động do hậu quả của mức tăng dân số giai đoạn trước.",
              "Bước 2: Chất lượng lao động chưa đáp ứng yêu cầu: Tỉ lệ lao động qua đào tạo có bằng cấp, chứng chỉ còn hạn chế, thiếu lao động tay nghề cao trong các ngành công nghệ mũi nhọn.",
              "Bước 3: Tình trạng thất nghiệp và thiếu việc làm: Khu vực thành thị tỉ lệ thất nghiệp còn cao, trong khi khu vực nông thôn tỉ lệ sử dụng thời gian lao động chưa triệt để.",
              "Bước 4: Tác động của chuyển đổi số và tự động hóa: Nhiều công việc giản đơn bị robot và AI thay thế đặt ra sức ép chuyển đổi nghề nghiệp khẩn cấp."
            ],
            "answer": "Do áp lực nguồn lao động bổ sung hàng năm rất lớn, chất lượng tay nghề chưa bắt kịp yêu cầu công nghệ và chuyển dịch cơ cấu việc làm chưa đủ nhanh để hấp thụ hết lao động."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đánh giá chất lượng nguồn lao động chỉ dựa trên số lượng lao động đông đảo.",
            "why": "Lợi thế số lượng (nhân công giá rẻ) đang mất dần ưu thế; giá trị cốt lõi hiện nay là năng suất lao động, trình độ khoa học công nghệ và kỹ năng mềm."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Phần 3: Địa lí các ngành kinh tế",
        "description": "Chuyển dịch cơ cấu kinh tế theo ngành, theo thành phần và theo lãnh thổ; phát triển nông nghiệp sinh thái, lâm nghiệp và thuỷ sản bền vững; chuyển dịch cơ cấu và phân bố các ngành công nghiệp trọng điểm.",
        "lessons": [
          { "id": "l01", "title": "Bài 11: Chuyển dịch cơ cấu kinh tế", "hasRealContent": true },
          { "id": "l02", "title": "Bài 12: Vấn đề phát triển ngành nông nghiệp", "hasRealContent": true },
          { "id": "l03", "title": "Bài 13: Vấn đề phát triển ngành lâm nghiệp và thuỷ sản", "hasRealContent": true },
          { "id": "l04", "title": "Bài 16: Chuyển dịch cơ cấu ngành công nghiệp", "hasRealContent": true },
          { "id": "l05", "title": "Bài 17: Một số ngành công nghiệp trọng điểm", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Chuyển dịch cơ cấu ngành kinh tế",
            "definition": "Xu hướng giảm tỉ trọng khu vực I (Nông - lâm - thủy sản), tăng tỉ trọng khu vực II (Công nghiệp - Xây dựng) và khu vực III (Dịch vụ); trong từng ngành tăng tỉ trọng sản phẩm chế biến sâu có giá trị gia tăng cao.",
            "example": "Nông nghiệp chuyển từ độc canh lúa nước sang nông nghiệp hữu cơ công nghệ cao kết hợp du lịch sinh thái.",
            "essence": "Phản ánh quá trình công nghiệp hóa, hiện đại hóa và hội nhập chuỗi giá trị toàn cầu."
          },
          {
            "term": "Công nghiệp điện tử - tin học",
            "definition": "Là ngành công nghiệp mũi nhọn công nghệ cao, đòi hỏi lao động có hàm lượng tri thức lớn, tiêu tốn ít năng lượng và nguyên liệu, tạo giá trị xuất khẩu khổng lồ.",
            "example": "Các tổ hợp sản xuất vi mạch, điện thoại thông minh của Samsung, Foxconn, Intel đặt tại Bắc Ninh, Thái Nguyên, TP. Hồ Chí Minh.",
            "essence": "Động lực then chốt đưa Việt Nam tham gia sâu vào mạng lưới sản xuất điện tử thế giới."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc phát triển nông nghiệp hàng hóa hiện đại",
            "meaning": "Chuyển mạnh từ tư duy sản xuất nông nghiệp thuần túy sang tư duy kinh tế nông nghiệp; gắn sản xuất với nhu cầu thị trường, hình thành các vùng chuyên canh tập trung quy mô lớn gắn với công nghiệp chế biến và chuỗi cung ứng logistics.",
            "example": "Vùng chuyên canh cà phê Tây Nguyên, chuyên canh lúa gạo và trái cây xuất khẩu Đồng bằng sông Cửu Long.",
            "essence": "Tối đa hóa giá trị trên một đơn vị diện tích và thích ứng linh hoạt với biến đổi khí hậu."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Trình bày những thế mạnh tự nhiên để phát triển ngành nuôi trồng thủy sản nước lợ và nước mặn ở nước ta.",
            "steps": [
              "Bước 1: Đường bờ biển dài 3260 km với nhiều vũng vịnh kín gió, đầm phá, bãi triều, rừng ngập mặn thuận lợi lập trại nuôi tôm sú, tôm thẻ chân trắng.",
              "Bước 2: Hệ thống các đảo và quần đảo ven bờ có nhiều vụng biển nước sâu, trong sạch lý tưởng để phát triển nuôi cá biển (cá chẽm, cá bớp, cá mú) và nuôi trai lấy ngọc.",
              "Bước 3: Khí hậu nhiệt đới nắng ấm quanh năm cho phép sinh vật biển sinh trưởng nhanh, chu kỳ nuôi ngắn.",
              "Bước 4: Nguồn thức ăn tự nhiên phong phú và nguồn giống thủy sản dồi dào."
            ],
            "answer": "Thế mạnh bao gồm bờ biển dài nhiều đầm phá rừng ngập mặn nuôi nước lợ, các đảo và vịnh kín gió nuôi nước mặn, khí hậu nhiệt đới nắng ấm cho phép nuôi trồng quanh năm."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa điều kiện phát triển đánh bắt thủy sản với điều kiện phát triển nuôi trồng thủy sản.",
            "why": "Đánh bắt cần ngư trường rộng lớn, trữ lượng cá nhiều; nuôi trồng cần diện tích mặt nước tĩnh (vịnh, đầm phá, bãi triều, ao hồ)."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Phần 4: Địa lí các ngành dịch vụ",
        "description": "Vai trò và nhân tố ảnh hưởng đến sự phát triển phân bố ngành dịch vụ; giao thông vận tải đa phương thức; bưu chính viễn thông số; thương mại nội địa và xuất nhập khẩu; tiềm năng và loại hình du lịch.",
        "lessons": [
          { "id": "l01", "title": "Bài 20: Vai trò và phân bố các ngành dịch vụ", "hasRealContent": true },
          { "id": "l02", "title": "Bài 21: Giao thông vận tải và bưu chính viễn thông", "hasRealContent": true },
          { "id": "l03", "title": "Bài 22: Thương mại và du lịch", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Giao thông vận tải đa phương thức và Logistics",
            "definition": "Là việc vận chuyển hàng hóa bằng ít nhất hai phương thức vận tải khác nhau (đường bộ, đường sắt, đường biển, hàng không) trên cơ sở một hợp đồng vận tải thống nhất kết hợp hệ thống kho bãi lưu trữ hàng thông minh.",
            "example": "Cảng biển nước sâu Cái Mép - Thị Vải kết nối đường cao tốc và sân bay quốc tế Long Thành hình thành trung tâm logistics trung chuyển quốc tế.",
            "essence": "Mạch máu giao thông lưu thông hàng hóa nhanh chóng, giảm chi phí logistics giúp tăng sức cạnh tranh quốc gia."
          },
          {
            "term": "Cán cân xuất nhập khẩu (Cán cân thương mại)",
            "definition": "Là hiệu số giữa giá trị xuất khẩu và giá trị nhập khẩu hàng hóa, dịch vụ của một quốc gia trong một thời kỳ nhất định. Xuất siêu khi giá trị xuất khẩu > nhập khẩu; nhập siêu khi xuất khẩu < nhập khẩu.",
            "example": "Những năm gần đây Việt Nam liên tục duy trì trạng thái xuất siêu hàng chục tỷ USD nhờ xuất khẩu hàng điện tử, dệt may, da giày và nông sản.",
            "essence": "Thước đo quan trọng phản ánh sức khỏe ngoại thương và nguồn dự trữ ngoại hối của nền kinh tế."
          }
        ],
        "rules": [
          {
            "statement": "Tuyến đường huyết mạch Bắc - Nam của giao thông Việt Nam",
            "meaning": "Tuyến giao thông trục dọc đóng vai trò liên kết kinh tế then chốt đất nước gồm: Quốc lộ 1A, Đường sắt Bắc - Nam (Thống Nhất), Đường Hồ Chí Minh và Tuyến đường bộ cao tốc Bắc - Nam phía Đông.",
            "example": "Đường bộ cao tốc Bắc - Nam giúp rút ngắn thời gian di chuyển từ Hà Nội vào TP. Hồ Chí Minh xuống dưới 20 giờ xe chạy.",
            "essence": "Khung xương hạ tầng kết nối các vùng kinh tế trọng điểm xuyên suốt chiều dài đất nước."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao ngành du lịch nước ta ngày càng phát triển nhanh và đóng vai trò là ngành kinh tế mũi nhọn?",
            "steps": [
              "Bước 1: Tài nguyên du lịch tự nhiên phong phú: Vịnh Hạ Long, Vườn quốc gia Phong Nha - Kẻ Bàng, hàng trăm bãi biển đẹp (Đà Nẵng, Nha Trang, Phú Quốc).",
              "Bước 2: Tài nguyên du lịch nhân văn đậm đà bản sắc: Hàng ngàn di tích lịch sử, phố cổ Hội An, di sản Cố đô Huế, văn hóa ẩm thực và lễ hội truyền thống đa dạng.",
              "Bước 3: Chính sách đổi mới: Nâng cấp hạ tầng hàng không, khách sạn cao cấp, chính sách thị thực (visa) thông thoáng và đẩy mạnh quảng bá hình ảnh đất nước hòa bình, mến khách.",
              "Bước 4: Nhu cầu du lịch trong và ngoài nước bùng nổ khi mức sống của người dân ngày càng được cải thiện."
            ],
            "answer": "Do sở hữu tài nguyên du lịch tự nhiên và nhân văn đặc sắc, hạ tầng giao thông và dịch vụ lưu trú được đầu tư hiện đại, cùng chính sách mở cửa visa thu hút du khách."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đồng nhất ngành ngoại thương với toàn bộ hoạt động của ngành thương mại.",
            "why": "Thương mại bao gồm cả nội thương (buôn bán, trao đổi hàng hóa trong nước) và ngoại thương (xuất nhập khẩu hàng hóa với nước ngoài)."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Phần 5: Địa lí các vùng kinh tế - xã hội",
        "description": "Khai thác thế mạnh và giải pháp phát triển bền vững tại 6 vùng kinh tế: Trung du miền núi Bắc Bộ, Đồng bằng sông Hồng, Bắc Trung Bộ, Duyên hải Nam Trung Bộ & Tây Nguyên, Đông Nam Bộ, Đồng bằng sông Cửu Long.",
        "lessons": [
          { "id": "l01", "title": "Bài 24: Khai thác thế mạnh ở Trung du và miền núi phía Bắc", "hasRealContent": true },
          { "id": "l02", "title": "Bài 25: Phát triển kinh tế - xã hội ở Đồng bằng sông Hồng", "hasRealContent": true },
          { "id": "l03", "title": "Bài 27: Phát triển kinh tế - xã hội ở Bắc Trung Bộ", "hasRealContent": true },
          { "id": "l04", "title": "Bài 28: Phát triển KT-XH ở Duyên hải Nam Trung Bộ và Tây Nguyên", "hasRealContent": true },
          { "id": "l05", "title": "Bài 30: Phát triển kinh tế - xã hội ở Đông Nam Bộ", "hasRealContent": true },
          { "id": "l06", "title": "Bài 31: Sử dụng hợp lí tự nhiên ở Đồng bằng sông Cửu Long", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Vùng Đông Nam Bộ - Đầu tàu kinh tế của cả nước",
            "definition": "Là vùng dẫn đầu cả nước về GDP, giá trị sản xuất công nghiệp, xuất khẩu và thu hút đầu tư nước ngoài (FDI). Cơ cấu kinh tế phát triển năng động nhất với các ngành công nghệ cao, dầu khí, hóa chất và dịch vụ tài chính.",
            "example": "TP. Hồ Chí Minh giữ vai trò hạt nhân trung tâm kinh tế, tài chính, đổi mới sáng tạo kết nối với các tỉnh công nghiệp Bình Dương, Đồng Nai, Bà Rịa - Vũng Tàu.",
            "essence": "Mô hình đi đầu trong công nghiệp hóa, hiện đại hóa và hội nhập kinh tế quốc tế."
          },
          {
            "term": "Thích ứng thuận thiên tại Đồng bằng sông Cửu Long (Nghị quyết 120)",
            "definition": "Chiến lược chuyển đổi cơ cấu kinh tế chủ động thích ứng với biến đổi khí hậu, nước biển dâng và xâm nhập mặn; chuyển đổi từ tư duy 'ngọt hóa bằng mọi giá' sang mô hình kinh tế 'nước ngọt - nước lợ - nước mặn'.",
            "example": "Mô hình xen canh tôm - lúa ở các huyện ven biển: mùa mưa ngọt trồng lúa hữu cơ, mùa khô mặn nuôi tôm sinh thái.",
            "essence": "Biến thách thức mặn thành cơ hội phát triển kinh tế tuần hoàn bền vững."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc phát triển kinh tế biển ở vùng Duyên hải miền Trung",
            "meaning": "Khai thác tổng hợp kinh tế biển kết hợp 4 ngành then chốt: Đánh bắt và nuôi trồng thủy sản; Khai thác khoáng sản biển; Giao thông vận tải biển gắn với hệ thống cảng nước sâu; và Du lịch biển đảo gắn với bảo đảm quốc phòng an ninh.",
            "example": "Chuỗi các cảng biển nước sâu Nghi Sơn, Vũng Áng, Chân Mây, Chu Lai, Dung Quất, Quy Nhơn, Cam Ranh.",
            "essence": "Khai thác tối đa lợi thế mặt tiền hướng biển của dải đất duyên hải miền Trung."
          }
        ],
        "workedExamples": [
          {
            "prompt": "So sánh thế mạnh chuyên môn hóa nông nghiệp giữa vùng Tây Nguyên và vùng Trung du miền núi Bắc Bộ.",
            "steps": [
              "Bước 1: Tây Nguyên: Địa hình cao nguyên xếp tầng đất đỏ bazan màu mỡ, khí hậu cận xích đạo nóng quanh năm -> Chuyên môn hóa cây công nghiệp lâu năm nhiệt đới (Cà phê vối, cao su, hồ tiêu, sầu riêng).",
              "Bước 2: Trung du miền núi Bắc Bộ: Địa hình đồi núi dốc, đất feralit đỏ vàng, có mùa đông lạnh buốt -> Chuyên môn hóa cây công nghiệp có nguồn gốc cận nhiệt và ôn đới (Chè búp, hồi, quế, thảo quả, cây ăn quả cận nhiệt đào, lê, mận).",
              "Bước 3: Nhận xét: Sự khác biệt về khí hậu và thổ nhưỡng quyết định sự khác biệt về cơ cấu sản phẩm nông nghiệp."
            ],
            "answer": "Tây Nguyên chuyên canh cây công nghiệp nhiệt đới ưa nóng (cà phê, cao su); Trung du miền núi Bắc Bộ chuyên canh cây cận nhiệt và ôn đới ưa lạnh (chè, cây dược liệu, cây ăn quả ôn đới)."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng Đồng bằng sông Hồng và Đồng bằng sông Cửu Long có điều kiện tự nhiên hoàn toàn giống nhau vì đều là đồng bằng châu thổ.",
            "why": "ĐB sông Hồng có hệ thống đê ngăn lũ dài, có mùa đông lạnh, đất trong đê không được bồi đắp phù sa hàng năm; ĐB sông Cửu Long không có đê, ngập lũ định kỳ mùa nước nổi, diện tích đất phèn mặn rất lớn."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Phần 6: Biển đảo và Địa lí địa phương",
        "description": "Vùng biển và các đảo, quần đảo Việt Nam (Hoàng Sa, Trường Sa); phát triển kinh tế biển gắn liền với bảo vệ chủ quyền, an ninh quốc phòng; địa lí tỉnh/thành phố trực thuộc Trung ương.",
        "lessons": [
          { "id": "l01", "title": "Bài 33: Phát triển kinh tế và đảm bảo an ninh quốc phòng ở Biển Đông", "hasRealContent": true },
          { "id": "l02", "title": "Bài 34: Bảo vệ chủ quyền biển, đảo của Việt Nam", "hasRealContent": true },
          { "id": "l03", "title": "Địa lí địa phương (Tỉnh / Thành phố)", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Các vùng biển thuộc chủ quyền và quyền tài phán của Việt Nam",
            "definition": "Theo Công ước LHQ về Luật Biển 1982 (UNCLOS) và Luật Biển Việt Nam 2012, vùng biển nước ta rộng trên 1 triệu km² bao gồm 5 vùng: Nội thủy, Lãnh hải (12 hải lý), Vùng tiếp giáp lãnh hải (12 hải lý tiếp theo), Vùng đặc quyền kinh tế (200 hải lý tính từ đường cơ sở) và Thềm lục địa.",
            "example": "Hai quần đảo Hoàng Sa (thuộc thành phố Đà Nẵng) và Trường Sa (thuộc tỉnh Khánh Hòa) là bộ phận lãnh thổ thiêng liêng không thể tách rời của Tổ quốc.",
            "essence": "Cơ sở pháp lý quốc tế vững chắc khẳng định chủ quyền, quyền chủ quyền và quyền tài phán quốc gia trên biển."
          },
          {
            "term": "Chiến lược biển Việt Nam đến năm 2030, tầm nhìn 2045",
            "definition": "Xây dựng Việt Nam trở thành quốc gia biển mạnh; đạt cơ bản các tiêu chí về phát triển bền vững kinh tế biển; chủ động thích ứng với biến đổi khí hậu; ngăn chặn xu thế ô nhiễm, suy thoái môi trường biển.",
            "example": "Phát triển điện gió ngoài khơi, du lịch biển đảo cao cấp và đội tàu biển vận tải viễn dương quốc tế.",
            "essence": "Đưa nước ta vươn ra biển lớn, làm giàu từ biển và bảo vệ vững chắc biển đảo quê hương."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc kết hợp phát triển kinh tế với củng cố an ninh quốc phòng trên biển",
            "meaning": "Mỗi hoạt động kinh tế biển (đánh bắt xa bờ, giàn khoan dầu khí, đảo du lịch) đồng thời là một phên dậu bảo vệ chủ quyền biên giới quốc gia; ngư dân bám biển là những chiến sĩ dân quân bảo vệ chủ quyền biển đảo Tổ quốc.",
            "example": "Đóng tàu cá vỏ thép công suất lớn hỗ trợ ngư dân vươn khơi bám các ngư trường truyền thống Hoàng Sa - Trường Sa.",
            "essence": "Thế trận lòng dân và quốc phòng toàn dân trên không gian sinh tồn biển đảo."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu ý nghĩa chiến lược của hai quần đảo Hoàng Sa và Trường Sa về mặt kinh tế và an ninh quốc phòng.",
            "steps": [
              "Bước 1: Về kinh tế: Nằm giữa các tuyến đường hàng hải quốc tế nhộn nhịp bậc nhất thế giới; vùng biển giàu tài nguyên thủy hải sản quý và tiềm năng băng cháy, dầu khí thềm lục địa.",
              "Bước 2: Về an ninh quốc phòng: Đóng vai trò là hệ thống tiền tiêu bảo vệ sườn phía đông của đất nước; kiểm soát các tuyến giao thương huyết mạch trên Biển Đông.",
              "Bước 3: Về chủ quyền pháp lý: Là căn cứ xác định vùng đặc quyền kinh tế và thềm lục địa rộng lớn của Việt Nam theo luật pháp quốc tế."
            ],
            "answer": "Hoàng Sa và Trường Sa vừa có giá trị kinh tế khổng lồ về ngư trường, khoáng sản và vận tải biển quốc tế, vừa là tiền tiêu phòng thủ chiến lược sống còn bảo vệ Tổ quốc từ hướng biển."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nhầm lẫn giữa phạm vi vùng Lãnh hải và Vùng đặc quyền kinh tế (EEZ).",
            "why": "Lãnh hải (12 hải lý) là lãnh thổ biển thuộc chủ quyền tuyệt đối như đất liền; Vùng đặc quyền kinh tế (200 hải lý) quốc gia có quyền chủ quyền về kinh tế nhưng tàu thuyền nước ngoài vẫn được tự do hàng hải theo UNCLOS."
          }
        ]
      }
    ]
  },
  "gdkt-pl": {
    "id": "gdkt-pl",
    "name": "GDKT & Pháp luật",
    "icon": "⚖️",
    "chapters": [
      {
        "id": "ch01",
        "title": "Chủ đề 1: Tăng trưởng và phát triển kinh tế",
        "description": "Các chỉ tiêu đo lường tăng trưởng kinh tế (GDP, GNI, GDP/người, tốc độ tăng trưởng), phát triển kinh tế bền vững, mối quan hệ giữa tăng trưởng kinh tế với tiến bộ, công bằng xã hội và bảo vệ môi trường.",
        "lessons": [
          { "id": "l01", "title": "Bài 1: Tăng trưởng và phát triển kinh tế", "hasRealContent": true },
          { "id": "l02", "title": "Bài 2: Phát triển kinh tế bền vững", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Tổng sản phẩm quốc nội (GDP) và Tổng thu nhập quốc gia (GNI)",
            "definition": "GDP là tổng giá trị bằng tiền của tất cả hàng hóa và dịch vụ cuối cùng được sản xuất ra trên phạm vi lãnh thổ của một quốc gia trong một thời kỳ nhất định (thường là 1 năm). GNI là tổng thu nhập do các công dân của quốc gia đó tạo ra (cả trong nước và ngoài nước).",
            "example": "GDP bình quân đầu người của Việt Nam năm 2024 đạt xấp xỉ 4.700 USD/người/năm.",
            "essence": "Thước đo quy mô và sức khỏe kinh tế vĩ mô của một quốc gia."
          },
          {
            "term": "Phát triển kinh tế bền vững",
            "definition": "Là sự phát triển kinh tế kết hợp hài hòa và chặt chẽ giữa 3 trụ cột: Tăng trưởng kinh tế bền vững, Tiến bộ và công bằng xã hội (giảm nghèo, bảo đảm an sinh) và Bảo vệ môi trường sinh thái cho các thế hệ tương lai.",
            "example": "Chuyển đổi sang kinh tế xanh, kinh tế tuần hoàn, cam kết phát thải ròng bằng 0 (Net Zero) vào năm 2050 tại COP26.",
            "essence": "Không đánh đổi môi trường và công bằng xã hội để lấy tăng trưởng kinh tế đơn thuần."
          }
        ],
        "rules": [
          {
            "statement": "Mối quan hệ giữa tăng trưởng kinh tế và phát triển kinh tế",
            "meaning": "Tăng trưởng kinh tế là điều kiện cần và là cơ sở vật chất cho phát triển kinh tế; nhưng phát triển kinh tế là khái niệm rộng hơn, bao hàm cả sự biến đổi tiến bộ về cơ cấu kinh tế, chất lượng cuộc sống (chỉ số HDI) và thể chế xã hội.",
            "example": "Một quốc gia có GDP tăng cao nhưng chênh lệch giàu nghèo quá lớn và môi trường bị hủy hoại thì chưa được coi là phát triển kinh tế thực sự.",
            "essence": "Tăng trưởng về lượng là tiền đề cho bước nhảy vọt tiến bộ về chất."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tại sao một quốc gia không thể theo đuổi mục tiêu tăng trưởng kinh tế bằng mọi giá mà phải hướng tới phát triển bền vững?",
            "steps": [
              "Bước 1: Tăng trưởng bằng mọi giá dẫn đến cạn kiệt tài nguyên thiên nhiên (khoáng sản, rừng, đất đai) không thể phục hồi.",
              "Bước 2: Gây ô nhiễm môi trường nghiêm trọng, biến đổi khí hậu và thiên tai đe dọa trực tiếp đời sống và sức khỏe con người.",
              "Bước 3: Gia tăng khoảng cách giàu nghèo, bất bình đẳng xã hội dẫn đến nguy cơ bất ổn chính trị.",
              "Bước 4: Phát triển bền vững bảo đảm cân bằng kinh tế - xã hội - môi trường, tạo dựng tương lai vững chắc cho các thế hệ mai sau."
            ],
            "answer": "Vì tăng trưởng bằng mọi giá sẽ hủy hoại môi trường sống, gia tăng bất công xã hội và làm triệt tiêu các điều kiện phát triển trong tương lai."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Đồng nhất khái niệm 'Tăng trưởng kinh tế' với 'Phát triển kinh tế'.",
            "why": "Tăng trưởng chỉ đo lường sự gia tăng thuần túy về quy mô sản lượng tiền tệ (GDP); Phát triển bao gồm cả nâng cao tuổi thọ, giáo dục, giảm nghèo và bảo vệ môi trường."
          }
        ]
      },
      {
        "id": "ch02",
        "title": "Chủ đề 2: Hội nhập kinh tế quốc tế",
        "description": "Bản chất và các hình thức hội nhập kinh tế quốc tế (song phương, khu vực, toàn cầu); các tổ chức kinh tế WTO, ASEAN, APEC và các hiệp định thương mại tự do thế hệ mới (CPTPP, EVFTA); thời cơ và thách thức đối với Việt Nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 3: Hội nhập kinh tế quốc tế", "hasRealContent": true },
          { "id": "l02", "title": "Bài 4: Các tổ chức kinh tế và hiệp định thương mại tự do", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Hội nhập kinh tế quốc tế",
            "definition": "Là quá trình một quốc gia gắn kết nền kinh tế của mình với nền kinh tế khu vực và thế giới thông qua các nỗ lực tự do hóa thương mại, mở cửa thị trường, tham gia các định chế tài chính và chuỗi cung ứng toàn cầu.",
            "example": "Việt Nam gia nhập Tổ chức Thương mại Thế giới (WTO) năm 2007, ký kết Hiệp định Đối tác Toàn diện và Tiến bộ xuyên Thái Bình Dương (CPTPP).",
            "essence": "Mở rộng không gian kinh tế, tận dụng vốn, công nghệ và thị trường quốc tế để phát triển đất nước."
          },
          {
            "term": "Hiệp định Thương mại Tự do thế hệ mới (FTA thế hệ mới)",
            "definition": "Là các thỏa thuận thương mại không chỉ xóa bỏ thuế quan đối với hàng hóa và dịch vụ mà còn bao gồm các cam kết sâu rộng về sở hữu trí tuệ, tiêu chuẩn lao động, bảo vệ môi trường, mua sắm chính phủ và thương mại điện tử.",
            "example": "Hiệp định Thương mại Tự do Việt Nam - Liên minh châu Âu (EVFTA).",
            "essence": "Tạo sân chơi minh bạch, tiêu chuẩn cao, thúc đẩy cải cách thể chế kinh tế trong nước."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc cơ bản trong hội nhập kinh tế quốc tế của Việt Nam",
            "meaning": "Chủ động, tích cực hội nhập kinh tế quốc tế trên nguyên tắc bảo đảm độc lập tự chủ dân tộc, bình đẳng, cùng có lợi, tuân thủ luật pháp quốc tế và các cam kết đã ký kết.",
            "example": "Hội nhập nhưng không hòa tan, giữ vững an ninh kinh tế và bản sắc văn hóa dân tộc.",
            "essence": "Kết hợp hài hòa sức mạnh dân tộc với sức mạnh thời đại."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Nêu 2 thời cơ lớn và 2 thách thức hàng đầu đối với các doanh nghiệp Việt Nam khi tham gia vào các Hiệp định thương mại tự do thế hệ mới như EVFTA, CPTPP?",
            "steps": [
              "Bước 1: Thời cơ 1: Thuế quan xuất khẩu giảm về 0% giúp hàng hóa Việt Nam (dệt may, da giày, nông thủy sản) cạnh tranh vượt trội tại thị trường EU và châu Mỹ.",
              "Bước 2: Thời cơ 2: Tiếp cận nguồn vốn đầu tư, công nghệ nguồn hiện đại và chuỗi cung ứng tiêu chuẩn cao từ các tập đoàn đa quốc gia.",
              "Bước 3: Thách thức 1: Cạnh tranh gay gắt ngay trên thị trường nội địa với các sản phẩm chất lượng cao của nước ngoài.",
              "Bước 4: Thách thức 2: Hàng rào kỹ thuật phi thuế quan khắt khe (tiêu chuẩn xuất xứ nguồn gốc, bảo vệ môi trường xanh, trách nhiệm xã hội và lao động)."
            ],
            "answer": "Thời cơ: Mở rộng thị trường xuất khẩu thuế 0% và tiếp thu công nghệ; Thách thức: Cạnh tranh thị trường khốc liệt và rào cản kỹ thuật xanh nghiêm ngặt."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng hội nhập kinh tế quốc tế chỉ mang lại toàn bộ lợi ích mà không có rủi ro.",
            "why": "Nền kinh tế mở dễ bị tổn thương trước các biến động khủng hoảng tài chính, lạm phát và đứt gãy chuỗi cung ứng toàn cầu nếu không có năng lực tự chủ cao."
          }
        ]
      },
      {
        "id": "ch03",
        "title": "Chủ đề 3: Bảo hiểm và An sinh xã hội",
        "description": "Bản chất, vai trò và các loại hình bảo hiểm (Bảo hiểm xã hội bắt buộc và tự nguyện, Bảo hiểm y tế, Bảo hiểm thất nghiệp); hệ thống chính sách an sinh xã hội tại Việt Nam.",
        "lessons": [
          { "id": "l01", "title": "Bài 5: Bảo hiểm", "hasRealContent": true },
          { "id": "l02", "title": "Bài 6: An sinh xã hội", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Bảo hiểm xã hội (BHXH)",
            "definition": "Là sự bảo đảm thay thế hoặc bù đắp một phần thu nhập của người lao động khi họ bị giảm hoặc mất thu nhập do ốm đau, thai sản, tai nạn lao động, bệnh nghề nghiệp, hết tuổi lao động hoặc chết, trên cơ sở đóng vào quỹ BHXH.",
            "example": "Người lao động tham gia BHXH bắt buộc được hưởng chế độ lương hưu hàng tháng khi đủ tuổi nghỉ hưu theo quy định.",
            "essence": "Cơ chế san sẻ rủi ro tài chính giữa cộng đồng người lao động và bảo đảm cuộc sống lâu dài."
          },
          {
            "term": "Hệ thống An sinh xã hội (Social Security)",
            "definition": "Là hệ thống các chính sách và chương trình của Nhà nước nhằm trợ giúp các cá nhân, hộ gia đình đối phó với rủi ro và khó khăn trong cuộc sống, bảo đảm mức sống tối thiểu thông qua 4 trụ cột: Phòng ngừa rủi ro, Giảm thiểu rủi ro, Khắc phục rủi ro và Dịch vụ xã hội cơ bản.",
            "example": "Chính sách miễn giảm học phí cho học sinh nghèo, cấp thẻ BHYT miễn phí cho người có hoàn cảnh khó khăn.",
            "essence": "Lưới an toàn bảo vệ nhân phẩm và quyền được sống no ấm của mọi công dân trong xã hội văn minh."
          }
        ],
        "rules": [
          {
            "statement": "Tính bắt buộc và trách nhiệm tham gia BHXH, BHYT của người sử dụng lao động",
            "meaning": "Người sử dụng lao động có nghĩa vụ bắt buộc phải trích nộp BHXH, BHYT, BHTN cho người lao động có hợp đồng lao động từ đủ 1 tháng trở lên theo đúng tỷ lệ luật định; hành vi trốn đóng là vi phạm pháp luật nghiêm trọng có thể bị truy cứu trách nhiệm hình sự.",
            "example": "Doanh nghiệp không được thỏa thuận trả tiền thay cho việc đóng BHXH để trốn tránh trách nhiệm pháp lý.",
            "essence": "Bảo vệ quyền lợi an sinh chính đáng và không thể chuyển nhượng của người lao động."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Phân biệt Bảo hiểm xã hội bắt buộc và Bảo hiểm thương mại về mục đích hoạt động và cơ quan quản lý.",
            "steps": [
              "Bước 1: Mục đích: BHXH là chính sách phi lợi nhuận của Nhà nước nhằm bảo đảm an sinh xã hội bền vững cho người dân; Bảo hiểm thương mại do các doanh nghiệp kinh doanh nhằm mục đích sinh lời tài chính.",
              "Bước 2: Cơ quan quản lý: BHXH do cơ quan Bảo hiểm xã hội Việt Nam (thuộc Chính phủ) trực tiếp quản lý và bảo hộ; Bảo hiểm thương mại do các công ty bảo hiểm (như Prudential, Manulife, Bảo Việt) vận hành chịu sự giám sát của Bộ Tài chính.",
              "Bước 3: Tính chất: BHXH có phần bắt buộc đối với người có hợp đồng lao động; Bảo hiểm thương mại hoàn toàn dựa trên sự tự nguyện thỏa thuận giữa khách hàng và công ty."
            ],
            "answer": "BHXH mang tính an sinh phi lợi nhuận do Nhà nước bảo trợ; Bảo hiểm thương mại mang tính tự nguyện kinh doanh tìm kiếm lợi nhuận."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng chỉ những người làm việc trong cơ quan nhà nước mới được tham gia và hưởng lương hưu BHXH.",
            "why": "Mọi người lao động tự do, nông dân, kinh doanh cá thể đều có quyền tham gia BHXH tự nguyện để được hưởng lương hưu và chế độ tử tuất khi về già."
          }
        ]
      },
      {
        "id": "ch04",
        "title": "Chủ đề 4: Quản lý thu, chi trong gia đình và Kế hoạch tài chính cá nhân",
        "description": "Các nguồn thu nhập và khoản chi tiêu trong gia đình; kỹ năng quản lý tài chính thông minh; các bước lập và thực hiện kế hoạch tài chính cá nhân ngắn hạn, trung hạn và dài hạn.",
        "lessons": [
          { "id": "l01", "title": "Bài 7: Quản lý thu, chi trong gia đình", "hasRealContent": true },
          { "id": "l02", "title": "Bài 8: Kế hoạch tài chính cá nhân", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Kế hoạch tài chính cá nhân",
            "definition": "Là bản kế hoạch phân bổ thu nhập hợp lý cho các mục tiêu chi tiêu thiết yếu, tiết kiệm, đầu tư và dự phòng rủi ro trong từng khoảng thời gian xác định nhằm đạt được sự an toàn và tự do tài chính.",
            "example": "Lập kế hoạch tiết kiệm mỗi tháng 20% tiền lương để xây dựng quỹ khẩn cấp tương đương 6 tháng sinh hoạt phí.",
            "essence": "Làm chủ tiền bạc thay vì để tiền bạc chi phối cuộc sống cá nhân."
          },
          {
            "term": "Quy tắc quản lý tài chính 50/30/20",
            "definition": "Phương pháp phân bổ thu nhập phổ biến: 50% cho Nhu cầu thiết yếu (ăn ở, điện nước, học tập); 30% cho Mong muốn cá nhân (giải trí, mua sắm sở thích); 20% cho Tiết kiệm và Đầu tư tương lai.",
            "example": "Với thu nhập 10 triệu đồng: 5 triệu cho sinh hoạt phí bắt buộc, 3 triệu cho giao lưu bạn bè, 2 triệu gửi tiết kiệm tích lũy.",
            "essence": "Tạo kỷ luật tài chính tự giác, cân bằng giữa hưởng thụ hiện tại và bảo đảm an toàn tương lai."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc quản lý chi tiêu: Phân biệt Nhu cầu (Needs) và Mong muốn (Wants)",
            "meaning": "Cần ưu tiên tuyệt đối chi trả cho các Nhu cầu sống còn trước khi chi tiền cho các Mong muốn sở thích; kiểm soát ham muốn mua sắm bốc đồng để tránh rơi vào bẫy nợ nần.",
            "example": "Mua thực phẩm sạch là Nhu cầu; mua điện thoại đời mới nhất khi máy cũ vẫn dùng tốt là Mong muốn.",
            "essence": "Tiêu dùng thông minh và có trách nhiệm là gốc rễ của sự thịnh vượng tài chính."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Một bạn học sinh lớp 12 được bố mẹ cho 2 triệu đồng tiền tiêu vặt mỗi tháng. Hãy tư vấn bạn ấy phân bổ ngân sách theo nguyên tắc quản lý tài chính hiệu quả.",
            "steps": [
              "Bước 1: 50% (1.000.000 đ) dành cho các nhu cầu học tập và sinh hoạt thiết yếu: Tiền gửi xe, sách vở tài liệu học tập, đồ dùng học tập.",
              "Bước 2: 30% (600.000 đ) dành cho sở thích cá nhân: Ăn uống giao lưu với bạn bè cuối tuần, giải trí lành mạnh.",
              "Bước 3: 20% (400.000 đ) dành cho quỹ tiết kiệm cá nhân: Bỏ ống heo hoặc gửi tài khoản tiết kiệm để mua sắm món đồ giá trị lớn hoặc dự phòng ốm đau."
            ],
            "answer": "Phân bổ hợp lý: 1.000.000 đ học tập thiết yếu; 600.000 đ giao lưu giải trí; 400.000 đ tiết kiệm tích lũy tương lai."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Chờ chi tiêu xong còn thừa tiền mới đem đi tiết kiệm.",
            "why": "Quy tắc vàng của triệu phú: Thu nhập - Tiết kiệm = Chi tiêu (trích ngay phần tiết kiệm khi vừa nhận tiền trước khi bắt đầu chi tiêu)."
          }
        ]
      },
      {
        "id": "ch05",
        "title": "Chủ đề 5: Quyền và nghĩa vụ của công dân trong kinh doanh và lao động",
        "description": "Quyền tự do kinh doanh theo pháp luật; nghĩa vụ nộp thuế của công dân; quyền và nghĩa vụ cơ bản của người lao động và người sử dụng lao động theo Bộ luật Lao động.",
        "lessons": [
          { "id": "l01", "title": "Bài 9: Quyền và nghĩa vụ của công dân trong kinh doanh", "hasRealContent": true },
          { "id": "l02", "title": "Bài 10: Quyền và nghĩa vụ của công dân trong lao động", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quyền tự do kinh doanh",
            "definition": "Là quyền hiến định của công dân được tự do lựa chọn hình thức tổ chức kinh doanh, ngành nghề, quy mô, địa bàn hoạt động mà pháp luật không cấm; tự chủ ký kết hợp đồng và tuyển dụng lao động.",
            "example": "Công dân đủ 18 tuổi có quyền đăng ký thành lập doanh nghiệp tư nhân hoặc công ty trách nhiệm hữu hạn.",
            "essence": "Giải phóng sức sản xuất và khơi dậy tinh thần khởi nghiệp sáng tạo của toàn dân."
          },
          {
            "term": "Nghĩa vụ nộp thuế",
            "definition": "Nộp thuế là nghĩa vụ hiến định của mọi công dân và doanh nghiệp nhằm đóng góp vào ngân sách nhà nước, phục vụ các công trình phúc lợi công cộng, quốc phòng, y tế, giáo dục và điều tiết thu nhập xã hội.",
            "example": "Kê khai và nộp thuế thu nhập cá nhân, thuế giá trị gia tăng, thuế thu nhập doanh nghiệp đúng hạn.",
            "essence": "Thuế là nguồn thu chủ yếu của quốc gia để xây dựng và bảo vệ đất nước."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc giao kết hợp đồng lao động",
            "meaning": "Hợp đồng lao động phải được giao kết dựa trên 2 nguyên tắc cốt lõi: Tự nguyện, bình đẳng, thiện chí, hợp tác và trung thực; Không trái pháp luật, thỏa ước lao động tập thể và đạo đức xã hội.",
            "example": "Doanh nghiệp không được giữ bản chính giấy tờ tùy thân (CCCD) hoặc văn bằng chứng chỉ của người lao động.",
            "essence": "Bảo vệ tự do thân thể và quyền lợi chính đáng của người lao động trong quan hệ lao động."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Anh A mở cửa hàng kinh doanh đồ điện tử nhưng không đăng ký kinh doanh và bán hàng trôi nổi không hóa đơn chứng từ. Hành vi của anh A vi phạm những quy định pháp luật nào?",
            "steps": [
              "Bước 1: Vi phạm nghĩa vụ đăng ký kinh doanh theo quy định của Luật Doanh nghiệp (hoạt động kinh doanh không có giấy phép).",
              "Bước 2: Vi phạm pháp luật thuế (hành vi trốn thuế do không lập hóa đơn, không kê khai doanh thu nộp thuế).",
              "Bước 3: Vi phạm quy định về bảo vệ quyền lợi người tiêu dùng và thương mại (kinh doanh hàng hóa không rõ nguồn gốc xuất xứ).",
              "Bước 4: Hậu quả pháp lý: Bị xử phạt vi phạm hành chính, truy thu tiền thuế và tịch thu tang vật vi phạm."
            ],
            "answer": "Anh A vi phạm nghĩa vụ đăng ký kinh doanh, vi phạm pháp luật về thuế và kinh doanh hàng hóa không rõ nguồn gốc xuất xứ; sẽ bị xử phạt hành chính và truy thu thuế."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Cho rằng 'Tự do kinh doanh' có nghĩa là được kinh doanh bất cứ thứ gì mình muốn mà không cần sự quản lý của Nhà nước.",
            "why": "Công dân chỉ được kinh doanh các ngành nghề mà pháp luật không cấm và phải tuân thủ điều kiện kinh doanh đối với các ngành nghề có điều kiện (y tế, giáo dục, an ninh)."
          }
        ]
      },
      {
        "id": "ch06",
        "title": "Chủ đề 6: Quyền và nghĩa vụ về sở hữu tài sản và môi trường",
        "description": "Quyền sở hữu tài sản và nghĩa vụ tôn trọng tài sản của người khác; các quy định cơ bản của Luật Doanh nghiệp; nghĩa vụ bảo vệ môi trường của công dân và doanh nghiệp trong hoạt động sản xuất kinh doanh.",
        "lessons": [
          { "id": "l01", "title": "Bài 11: Quyền và nghĩa vụ của công dân về sở hữu tài sản", "hasRealContent": true },
          { "id": "l02", "title": "Bài 12: Nghĩa vụ bảo vệ môi trường", "hasRealContent": true }
        ],
        "concepts": [
          {
            "term": "Quyền sở hữu tài sản (Bộ luật Dân sự)",
            "definition": "Bao gồm 3 quyền năng cơ bản của chủ sở hữu đối với tài sản của mình: Quyền chiếm hữu (nắm giữ, chi phối tài sản), Quyền sử dụng (khai thác công dụng, hưởng hoa lợi lợi tức) và Quyền định đoạt (chuyển giao quyền sở hữu, bán, tặng cho, hủy bỏ tài sản).",
            "example": "Chủ sở hữu ngôi nhà có quyền ở (sử dụng), cho thuê lấy tiền (hưởng hoa lợi), hoặc bán ngôi nhà đó cho người khác (định đoạt).",
            "essence": "Bảo hộ tài sản hợp pháp của công dân là nền tảng của nhà nước pháp quyền và trật tự kinh tế thị trường."
          },
          {
            "term": "Trách nhiệm xã hội và môi trường của doanh nghiệp (CSR)",
            "definition": "Cam kết của doanh nghiệp đóng góp vào sự phát triển kinh tế bền vững, tuân thủ nghiêm ngặt Luật Bảo vệ môi trường, xử lý chất thải đạt chuẩn, bảo vệ sức khỏe cộng đồng và tiết kiệm tài nguyên thiên nhiên.",
            "example": "Nhà máy dệt nhuộm đầu tư hệ thống xử lý nước thải tuần hoàn tự động trước khi xả ra sông suối tự nhiên.",
            "essence": "Lợi nhuận kinh doanh không thể xây dựng trên sự suy thoái môi trường sống của xã hội."
          }
        ],
        "rules": [
          {
            "statement": "Nguyên tắc 'Người gây ô nhiễm môi trường phải trả tiền'",
            "meaning": "Mọi tổ chức, cá nhân có hoạt động xả thải gây ô nhiễm môi trường phải nộp thuế bảo vệ môi trường, chi trả tiền xử lý chất thải và bồi thường thiệt hại toàn diện nếu gây sự cố ô nhiễm môi trường.",
            "example": "Doanh nghiệp xả thải trộm ra biển bị phạt hàng triệu USD bồi thường thiệt hại cho ngư dân và phục hồi hệ sinh thái biển.",
            "essence": "Nội hóa chi phí ngoại ứng tiêu cực buộc các chủ thể sản xuất phải đầu tư công nghệ sạch."
          }
        ],
        "workedExamples": [
          {
            "prompt": "Tập đoàn công nghiệp B lén lút chôn lấp chất thải nguy hại xuống đất vườn dân cư gây ô nhiễm nguồn nước ngầm. Phân tích trách nhiệm pháp lý mà doanh nghiệp B phải gánh chịu?",
            "steps": [
              "Bước 1: Trách nhiệm hành chính / hình sự: Bị phạt tiền ở khung cao nhất hoặc bị khởi tố vụ án hình sự về tội 'Gây ô nhiễm môi trường' (Điều 235 Bộ luật Hình sự).",
              "Bước 2: Trách nhiệm khắc phục hậu quả: Buộc phải bốc dỡ, vận chuyển và xử lý toàn bộ khối lượng chất thải nguy hại theo đúng quy chuẩn kỹ thuật; tiến hành cải tạo phục hồi môi trường đất và nước ngầm bị ô nhiễm.",
              "Bước 3: Trách nhiệm bồi thường dân sự: Bồi thường toàn bộ thiệt hại về sức khỏe, mùa màng, nguồn nước sinh hoạt cho các hộ dân bị ảnh hưởng."
            ],
            "answer": "Doanh nghiệp B phải chịu trách nhiệm hình sự/hành chính, buộc chi trả kinh phí khắc phục phục hồi môi trường và bồi thường toàn bộ thiệt hại vật chất, sức khỏe cho người dân xung quanh."
          }
        ],
        "commonMistakes": [
          {
            "mistake": "Nghĩ rằng quyền sở hữu tài sản là tuyệt đối và chủ sở hữu có quyền sử dụng tài sản gây tổn hại đến môi trường và người khác.",
            "why": "Việc thực hiện quyền sở hữu không được gây thiệt hại hoặc làm ảnh hưởng đến lợi ích quốc gia, lợi ích công cộng, quyền và lợi ích hợp pháp của người khác."
          }
        ]
      }
    ]
  }
}

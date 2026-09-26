# -*- coding: utf-8 -*-
"""
Builder script to generate pipeline/data_g10_humanities.py
Containing full authentic curriculum for:
- ngu-van (9 units)
- tieng-anh (10 units)
- lich-su (6 chapters)
- dia-li (10 chapters)
- gdkt-pl (9 units)
"""
import json
from pathlib import Path

HUMANITIES_DATA = {
    "ngu-van": {
        "id": "ngu-van",
        "name": "Ngữ Văn",
        "icon": "📖",
        "chapters": [
            {
                "id": "ch01",
                "title": "Bài 1: Sức sống của sử thi",
                "description": "Thể loại sử thi, không gian, thời gian sử thi, hình tượng người anh hùng trong sử thi Đăm Săn (Ê-đê), Ra-ma-ya-na (Ấn Độ) và Thần thoại Hy Lạp.",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Đăm Săn chiến thắng Mtao Mxây", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Rama buộc tội và Hê-ra-clét đi tìm táo vàng", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Sử thi anh hùng",
                        "definition": "Tác phẩm tự sự dân gian quy mô lớn, sử dụng ngôn từ có vần, nhịp, hình ảnh hào hùng để kể về những biến cố trọng đại của cộng đồng và người anh hùng đại diện cho sức mạnh, khát vọng của cộng đồng.",
                        "example": "Chàng Đăm Săn múa khiên như gió bão, đâm chém tiêu diệt tù trưởng Mtao Mxây để bảo vệ danh dự bộ tộc và mở mang buôn làng.",
                        "essence": "Người anh hùng sử thi không sống cho cá nhân mình mà là hiện thân tập trung cho danh dự, quyền lợi và sức mạnh đoàn kết của toàn bộ tộc."
                    }
                ],
                "rules": [
                    {
                        "statement": "Nghệ thuật phóng đại và so sánh trùng điệp trong sử thi",
                        "meaning": "Sử dụng các hình ảnh so sánh liên tiếp lấy từ thiên nhiên vũ trụ (mặt trời, giông bão, đại ngàn) để tôn vinh tầm vóc phi thường của nhân vật anh hùng.",
                        "example": "'Chàng múa trên cao, gió như bão. Chàng múa dưới thấp, gió như lốc. Tiếng khiên đập vào nhau như tiếng sấm sét rền vang.'",
                        "essence": "Mở rộng không gian nghệ thuật chạm tới tầm vóc vũ trụ, tạo nên giọng điệu sử thi trang trọng, thiêng liêng."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Phân tích ý nghĩa cảnh ăn mừng chiến thắng ở cuối đoạn trích 'Đăm Săn chiến thắng Mtao Mxây'.",
                        "steps": [
                            "Bước 1: Không gian ăn mừng: buôn làng rộn rã tiếng cồng chiêng, đông vui tấp nập, thịt trâu thịt bò ê hề, rượu cần chảy như suối.",
                            "Bước 2: Hình ảnh Đăm Săn: tóc dài chấm đất, ngực nở như vách đá, mắt sáng như chim prâu, nằm trên võng ngắm nhìn buôn làng thịnh vượng.",
                            "Bước 3: Ý nghĩa: Không chỉ là chiến thắng cá nhân mà là sự trưởng thành, giàu mạnh và thống nhất cộng đồng các thị tộc Ê-đê cổ đại."
                        ],
                        "answer": "Cảnh ăn mừng khẳng định khát vọng thái bình, thịnh vượng và tự hào cộng đồng người Tây Nguyên."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Đánh giá hành động giao tranh của Đăm Săn bằng thước đo đạo đức cá nhân hiện đại.",
                        "why": "Trong xã hội thị tộc cổ sơ, cuộc chiến tranh đoạt phụ nữ và của cải giữa các tù trưởng là quy luật sinh tồn và thống nhất buôn làng."
                    }
                ]
            },
            {
                "id": "ch02",
                "title": "Bài 2: Vẻ đẹp của thơ ca",
                "description": "Thơ trữ tình, nhân vật trữ tình, hình ảnh, vần điệu, nhạc tính, thi nhãn qua các kiệt tác thơ Đường (Thu hứng - Đỗ Phủ) và thơ lãng mạn hiện đại (Mùa xuân chín - Hàn Mặc Tử).",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Mùa xuân chín (Hàn Mặc Tử) và Cảm xúc mùa thu (Đỗ Phủ)", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Tự tình II (Hồ Xuân Hương) và Thực hành tiếng Việt", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Nhân vật trữ tình (Chủ thể trữ tình)",
                        "definition": "Là cái 'tôi' tác giả hoặc người gián tiếp bộc lộ cảm xúc, suy tư, rung động thẩm mỹ trong bài thơ.",
                        "example": "Trong 'Mùa xuân chín', nhân vật trữ tình lắng nghe bước đi của mùa xuân và bâng khuâng nuối tiếc vẻ đẹp xuân thì chóng tàn phai.",
                        "essence": "Thơ ca không phản ánh thế giới khách quan thuần túy mà soi chiếu thế giới qua lăng kính cảm xúc chủ quan sâu lắng."
                    }
                ],
                "rules": [
                    {
                        "statement": "Bút pháp thi trung hữu họa và thi trung hữu nhạc",
                        "meaning": "Trong thơ có tranh vẽ (hình ảnh gợi màu sắc, đường nét) và có âm nhạc (sự phối hợp thanh điệu bằng trắc, vần và ngắt nhịp).",
                        "example": "'Trong làn nắng ửng khói mơ tan / Đôi mái nhà tranh lấm tấm vàng' vừa tạo hình sắc nét vừa có vần êm ái.",
                        "essence": "Ngôn ngữ thơ là ngôn ngữ cô đọng, giàu hình ảnh và giàu nhạc tính nhất trong các thể loại văn học."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Cảm nhận từ 'chín' trong nhan đề 'Mùa xuân chín' của thi sĩ Hàn Mặc Tử.",
                        "steps": [
                            "Bước 1: Nghĩa thực: Trạng thái chín mọng của hoa trái, độ căng tràn tươi tắn nhất của cảnh sắc mùa xuân.",
                            "Bước 2: Nghĩa chuyển: Đỉnh cao rực rỡ nhất của tuổi trẻ, tình yêu và vẻ đẹp trần thế.",
                            "Bước 3: Chiều sâu triết lý: 'Chín' cũng dự báo sự tàn phai, chuyển giao sang mùa khác, tạo nên nỗi hoài niệm tiếc nuối kín đáo của cái tôi trữ tình."
                        ],
                        "answer": "Từ 'chín' gợi vẻ đẹp viên mãn tột cùng đồng thời hàm chứa nỗi bâng khuâng về sự mong manh của thời gian."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Phân tích thơ như kể lại câu chuyện văn xuôi, bỏ quên các yếu tố thi pháp (vần, nhịp, thanh điệu, từ ngữ thi nhãn).",
                        "why": "Linh hồn của thơ nằm ở nhạc tính và sức gợi mở của hình ảnh ngôn từ, không phải cốt truyện."
                    }
                ]
            },
            {
                "id": "ch03",
                "title": "Bài 3: Nghệ thuật thuyết phục trong văn nghị luận",
                "description": "Văn bản nghị luận xã hội và chính luận, luận đề, hệ thống luận điểm, luận cứ, dẫn chứng và nghệ thuật lập luận sắc bén.",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Hịch tướng sĩ (Trần Quốc Tuấn)", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Tuyên ngôn Độc lập (Hồ Chí Minh)", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Luận điểm và Luận cứ",
                        "definition": "Luận điểm là ý kiến thể hiện tư tưởng, quan điểm của người viết về luận đề. Luận cứ là các lí lẽ và dẫn chứng thực tế dùng để chứng minh cho luận điểm.",
                        "example": "Luận điểm: Tinh thần yêu nước nồng nàn của nhân dân ta. Luận cứ: Lịch sử các cuộc kháng chiến Bà Trưng, Lê Lợi, Quang Trung.",
                        "essence": "Lập luận là cây cầu logic kết nối dẫn chứng cụ thể với kết luận khái quát."
                    }
                ],
                "rules": [
                    {
                        "statement": "Sự kết hợp giữa Lí và Tình trong văn chính luận",
                        "meaning": "Lí lẽ sắc bén, chặt chẽ thuyết phục lí trí; cảm xúc chân thành, nồng nàn lay động con tim người đọc.",
                        "example": "Trần Quốc Tuấn trong Hịch tướng sĩ vừa vạch rõ tội ác quân giặc (Lí) vừa bày tỏ 'ruột đau như cắt, nước mắt đầm đìa' (Tình).",
                        "essence": "Sức mạnh tối cao của văn nghị luận là sự giao thoa hoàn hảo giữa ánh sáng trí tuệ và ngọn lửa cảm xúc."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Chỉ ra nghệ thuật lập luận chặt chẽ trong mở đầu bản 'Tuyên ngôn Độc lập' của Chủ tịch Hồ Chí Minh.",
                        "steps": [
                            "Bước 1: Trích dẫn Tuyên ngôn Độc lập 1776 của Mỹ và Tuyên ngôn Nhân quyền 1789 của Pháp về quyền bình đẳng, tự do, mưu cầu hạnh phúc.",
                            "Bước 2: Nghệ thuật 'gậy ông đập lưng ông': dùng chính chân lý của tổ tiên phương Tây để khẳng định quyền độc lập của dân tộc Việt Nam.",
                            "Bước 3: Mở rộng quyền con người thành quyền dân tộc: 'Suy rộng ra, câu ấy có ý nghĩa là: Tất cả các dân tộc trên thế giới đều sinh ra bình đẳng'."
                        ],
                        "answer": "Lập luận chuẩn xác, đặt cuộc đấu tranh độc lập của Việt Nam ngang hàng với các phong trào tiến bộ nhất của nhân loại."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Liệt kê dẫn chứng tràn lan mà không gắn kết phân tích lí lẽ để làm sáng tỏ luận điểm.",
                        "why": "Dẫn chứng chỉ có giá trị khi được người viết 'soi sáng' bằng lập luận sắc sảo phục vụ mục đích nghị luận."
                    }
                ]
            },
            {
                "id": "ch04",
                "title": "Bài 4: Sức sống của Chèo và Tuồng",
                "description": "Nghệ thuật sân khấu truyền thống dân tộc, tính ước lệ, nhân vật tích trò, tích tuồng và nhân vật hề chèo mang tính phê phán xã hội.",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Xúy Vân giả dại (Trích chèo Kim Nham)", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Huyện đường (Trích tuồng Nghêu, Sò, Ốc, Hến)", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Tính ước lệ trong sân khấu Chèo",
                        "definition": "Quy ước biểu diễn không tả thực: chiếc roi ngựa tượng trưng cho cưỡi ngựa, mái chèo tượng trưng cho đi thuyền, động tác múa cách điệu bộc lộ nội tâm.",
                        "example": "Xúy Vân vừa điên dại múa nón vừa hát những câu hát ẩn dụ về thân phận bèo bọt, khát vọng tự do yêu đương.",
                        "essence": "Ước lệ giải phóng không gian sân khấu nhỏ hẹp thành vũ đài tâm trạng vô hạn trong trí tưởng tượng khán giả."
                    }
                ],
                "rules": [
                    {
                        "statement": "Nhân vật Hề chèo",
                        "meaning": "Nhân vật tạo tiếng cười hài hước, châm biếm sâu cay những thói hư tật xấu của tầng lớp quan lại thống trị phong kiến.",
                        "example": "Hề mồi, hề gậy trong chèo cổ đại diện cho tiếng nói phê phán sắc sảo của người bình dân.",
                        "essence": "Tiếng cười chèo là vũ khí đấu tranh xã hội và giải tỏa áp bức tinh thần của nhân dân lao động."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Phân tích bi kịch nội tâm của nhân vật Xúy Vân qua đoạn hát xắp 'Gà rừng ăn lẫn với công...'.",
                        "steps": [
                            "Bước 1: Hình ảnh ẩn dụ đối lập: 'gà rừng' và 'công', thân phận nhỏ nhoi lạc lõng giữa gia đình chồng xa lạ.",
                            "Bước 2: Mâu thuẫn giằng xé: một bên là khát vọng tình yêu đôi lứa tự do, một bên là danh tiết đạo đức phong kiến ràng buộc.",
                            "Bước 3: Nỗi đau đớn cô đơn: giả dại để thoát nợ duyên nhưng lại rơi vào ngõ cụt tha hóa, cùng quẫn bi đát."
                        ],
                        "answer": "Tiếng hát Xúy Vân là lời tố cáo chế độ hôn nhân phong kiến tước đoạt hạnh phúc người phụ nữ."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Quy kết nhân vật Xúy Vân là kẻ lăng loàn, độc ác theo định kiến phong kiến xưa.",
                        "why": "Dưới góc nhìn nhân văn hiện đại, Xúy Vân là nạn nhân đáng thương của bi kịch hôn nhân sắp đặt không tình yêu."
                    }
                ]
            },
            {
                "id": "ch05",
                "title": "Bài 5: Tích lũy tri thức văn học",
                "description": "Tổng kết phương pháp đọc hiểu văn bản văn học theo thể loại (thơ, truyện, kịch bản sân khấu) và viết bài văn nghị luận phân tích tác phẩm văn học.",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Kĩ năng phân tích đặc trưng thể loại văn học", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Thực hành viết bài văn nghị luận văn học chuẩn GDPT 2018", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Đặc trưng thể loại văn học",
                        "definition": "Mỗi thể loại (tự sự, trữ tình, kịch, nghị luận) có hệ thống quy ước hình thức và phương thức tiếp cận hiện thực riêng biệt.",
                        "example": "Đọc truyện cần chú ý cốt truyện, nhân vật, điểm nhìn trần thuật; đọc thơ cần chú ý hình tượng, cảm xúc, thi pháp.",
                        "essence": "Nắm vững đặc trưng thể loại là chiếc chìa khóa vạn năng để giải mã bất kỳ văn bản mới nào ngoài SGK."
                    }
                ],
                "rules": [
                    {
                        "statement": "Cấu trúc bài văn nghị luận văn học 3 phần chuẩn mực",
                        "meaning": "Mở bài: Giới thiệu tác giả, tác phẩm, vấn đề nghị luận. Thân bài: Hệ thống luận điểm phân tích nội dung và nghệ thuật kèm dẫn chứng. Kết bài: Đánh giá vị trí tác phẩm và bài học cuộc sống.",
                        "example": "Thân bài luôn đi từ phân tích chi tiết nghệ thuật cụ thể đến khái quát giá trị tư tưởng nhân văn sâu sắc.",
                        "essence": "Mạch lập luận chặt chẽ, luận điểm rõ ràng, dẫn chứng xác đáng và cảm xúc thăng hoa."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Xây dựng dàn ý bài văn phân tích một đoạn trích thơ trữ tình tự chọn ngoài SGK.",
                        "steps": [
                            "Bước 1: Mở bài: Giới thiệu tác giả, hoàn cảnh sáng tác, trích dẫn đoạn thơ và nêu cảm nhận chung.",
                            "Bước 2: Luận điểm 1: Bức tranh không gian, thời gian và cảnh sắc thiên nhiên được gợi tả qua hình ảnh, từ ngữ đặc sắc.",
                            "Bước 3: Luận điểm 2: Tâm trạng, cảm xúc sâu kín của nhân vật trữ tình ẩn sau cảnh sắc thiên nhiên.",
                            "Bước 4: Luận điểm 3: Đánh giá nét độc đáo nghệ thuật (nhịp thơ, biện pháp tu từ, ngôn ngữ biểu cảm).",
                            "Bước 5: Kết bài: Khẳng định vẻ đẹp đoạn thơ và dấu ấn phong cách tác giả."
                        ],
                        "answer": "Dàn ý hoàn chỉnh theo cấu trúc 3 phần và các luận điểm tiếp cận đặc trưng thể loại thơ."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Diễn xuôi lại bài thơ thành văn xuôi thay vì phân tích nghệ thuật và tư tưởng.",
                        "why": "Nghị luận thơ đòi hỏi phải bóc tách lớp vỏ ngôn từ, các tín hiệu thẩm mỹ (từ ngữ, nhịp, vần, ẩn dụ) để tìm ra ý đồ của nhà thơ."
                    }
                ]
            },
            {
                "id": "ch06",
                "title": "Bài 6: Nguyễn Trãi - Người bạn của muôn đời",
                "description": "Tác giả Nguyễn Trãi, văn chính luận kiệt xuất 'Bình Ngô đại cáo', tư tưởng nhân nghĩa, tình yêu thiên nhiên đất nước trong thơ Nôm Quốc âm thi tập.",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Bình Ngô đại cáo (Nguyễn Trãi)", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Bảo kính cảnh giới - bài 43 và Thư lại dụ Vương Thông", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Tư tưởng Nhân nghĩa của Nguyễn Trãi",
                        "definition": "'Việc nhân nghĩa cốt ở yên dân / Quân điếu phạt trước lo trừ bạo'. Nhân nghĩa gắn liền với yêu nước thương dân, vì dân trừ bạo ngược ngoại xâm.",
                        "example": "Tha mạng cho mười vạn quân Minh bại trận, cấp ngựa thuyền cho về nước thể hiện lòng nhân đạo cao cả của dân tộc Đại Việt.",
                        "essence": "Nguyễn Trãi đã kế thừa nhân nghĩa Nho giáo nhưng nâng lên thành tư tưởng yêu nước, lấy dân làm gốc, vì độc lập chủ quyền dân tộc."
                    }
                ],
                "rules": [
                    {
                        "statement": "Thể Cáo trong văn học trung đại",
                        "meaning": "Thể văn nghị luận cổ có tính chất quốc gia đại sự, thường do vua chúa hoặc tướng lĩnh dùng để ban bố tuyên cáo về một sự kiện trọng đại trước toàn dân.",
                        "example": "Bình Ngô đại cáo được coi là bản 'Tuyên ngôn Độc lập thứ hai' của nước Đại Việt sau đại thắng kháng chiến chống quân Minh.",
                        "essence": "Lời văn biền ngẫu sóng đôi nhịp nhàng, lập luận đanh thép hào hùng đầy tự hào dân tộc."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Phân tích 5 yếu tố khẳng định chủ quyền độc lập dân tộc ở đoạn mở đầu 'Bình Ngô đại cáo'.",
                        "steps": [
                            "Bước 1: Nền văn hiến lâu đời: 'Như nước Đại Việt ta từ trước, vốn xưng nền văn hiến đã lâu'.",
                            "Bước 2: Cương vực lãnh thổ xác định: 'Núi sông bờ cõi đã chia'.",
                            "Bước 3: Phong tục tập quán riêng biệt: 'Phong tục Bắc Nam cũng khác'.",
                            "Bước 4: Lịch sử các triều đại độc lập song song: 'Từ Triệu, Đinh, Lí, Trần bao đời gây nền độc lập, Cùng Hán, Đường, Tống, Nguyên mỗi bên xưng đế một phương'.",
                            "Bước 5: Lịch sử hào hùng với các anh hùng hào kiệt đánh bại mọi kẻ thù xâm lược."
                        ],
                        "answer": "Quan niệm toàn diện, sâu sắc vượt bậc của Nguyễn Trãi về chủ quyền quốc gia độc lập."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Bỏ qua yếu tố 'văn hiến' khi phân tích quan niệm về độc lập dân tộc của Nguyễn Trãi.",
                        "why": "Văn hiến (truyền thống văn hóa, đạo lý lâu đời) là nền tảng cốt lõi khẳng định tầm vóc tự chủ của một dân tộc."
                    }
                ]
            },
            {
                "id": "ch07",
                "title": "Bài 7: Quyền năng của người kể chuyện",
                "description": "Nghệ thuật tự sự trong tiểu thuyết và truyện ngắn, người kể chuyện toàn tri và hạn tri, sự thay đổi điểm nhìn trần thuật qua các tác phẩm văn học hiện thực và lãng mạn.",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Người cầm quyền khôi phục uy quyền (V. Huy-gô)", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Dưới bóng hoàng lan (Thạch Lam)", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Người kể chuyện ngôi thứ ba (Toàn tri và Hạn tri)",
                        "definition": "Người kể chuyện ẩn mình không trực tiếp xuất hiện. Người kể toàn tri (biết hết mọi suy nghĩ, hành động, quá khứ tương lai của nhân vật). Người kể hạn tri (chỉ nhìn qua góc nhìn giới hạn của một nhân vật).",
                        "example": "Trong 'Dưới bóng hoàng lan', câu chuyện được kể theo điểm nhìn ấm áp, tinh tế dõi theo từng cảm xúc dịu dàng của nhân vật Thanh khi trở về quê.",
                        "essence": "Điểm nhìn trần thuật quyết định khoảng cách tâm lý và cảm xúc của độc giả đối với thế giới nhân vật."
                    }
                ],
                "rules": [
                    {
                        "statement": "Nghệ thuật tương phản đối lập trong lãng mạn chủ nghĩa",
                        "meaning": "Đặt hai hình tượng đối lập gay gắt cạnh nhau để làm nổi bật vẻ đẹp thánh thiện hoặc sự tàn bạo ghê tởm.",
                        "example": "Văn hào Victor Hugo đặt Giăng Van-giăng (hiền hậu, bao dung, vị tha) đối lập tột cùng với Gia-ve (ác quỷ, lạnh lùng, máy móc).",
                        "essence": "Làm nổi bật sức mạnh của tình thương yêu và ánh sáng nhân đạo chiến thắng cường quyền bạo lực."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Phân tích khoảnh khắc Giăng Van-giăng cúi đầu thầm thì bên tai Phăng-tin đã qua đời trong 'Người cầm quyền khôi phục uy quyền'.",
                        "steps": [
                            "Bước 1: Bối cảnh căng thẳng: tên cảnh sát Gia-ve đằng đằng sát khí lăm lăm bắt bớ, Phăng-tin vừa trút hơi thở cuối cùng trong tuyệt vọng.",
                            "Bước 2: Hành động của Giăng Van-giăng: bình thản, nghiêm trang, quyền uy của cái thiện làm tên Gia-ve hung dữ phải lùi bước sợ hãi.",
                            "Bước 3: Chi tiết huyền ảo lãng mạn: nụ cười thanh thản trên gương mặt người phụ nữ bất hạnh khi nghe lời hứa chăm sóc con gái Cô-zét.",
                            "Bước 4: Ý nghĩa: Uy quyền thực sự không thuộc về kẻ nắm giữ pháp luật cơ học mà thuộc về người có trái tim yêu thương mênh mông."
                        ],
                        "answer": "Tôn vinh chiến thắng vinh quang của tình thương nhân loại trước cái ác và sự vô cảm."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Đồng nhất người kể chuyện ngôi thứ nhất 'tôi' hoàn toàn với bản thân tác giả ngoài đời thực.",
                        "why": "Người kể chuyện 'tôi' là một hình tượng nghệ thuật do nhà văn sáng tạo ra để thực hiện vai trò trần thuật, có thể mang hư cấu."
                    }
                ]
            },
            {
                "id": "ch08",
                "title": "Bài 8: Thế giới đa dạng của thông tin",
                "description": "Văn bản thông tin, cách mạng 4.0, bảo tồn di sản văn hóa, phương tiện giao tiếp phi ngôn ngữ (hình ảnh, số liệu, sơ đồ, bản đồ tư duy).",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Phục hồi và bảo tồn di sản văn hóa Việt Nam", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Phương tiện giao tiếp phi ngôn ngữ trong văn bản thông tin", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Văn bản thông tin và Phương tiện phi ngôn ngữ",
                        "definition": "Văn bản truyền đạt thông tin khách quan, chính xác về một sự kiện, hiện tượng. Kết hợp văn bản chữ với biểu đồ, hình ảnh, sơ đồ chỉ dẫn để trực quan hóa dữ liệu.",
                        "example": "Infographic về các biện pháp phòng chống biến đổi khí hậu kết hợp số liệu phần trăm và biểu tượng đồ họa.",
                        "essence": "Gia tăng tốc độ tiếp nhận và mức độ tin cậy của thông tin trong thời đại bùng nổ dữ liệu số."
                    }
                ],
                "rules": [
                    {
                        "statement": "Tính xác thực và độ tin cậy của nguồn thông tin",
                        "meaning": "Cần đối chiếu nguồn trích dẫn uy tín, số liệu được kiểm chứng độc lập, phân biệt rõ giữa 'sự thật khách quan' và 'ý kiến chủ quan'.",
                        "example": "Thông tin khoa học phải trích nguồn từ các viện nghiên cứu, bài báo bình duyệt hoặc tổ chức quốc tế (WHO, UNESCO).",
                        "essence": "Tư duy phản biện bảo vệ người đọc trước bão tin giả và thông tin rác trên không gian mạng."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Nêu vai trò của hình ảnh minh họa và biểu đồ số liệu trong văn bản thông tin về bảo tồn di sản.",
                        "steps": [
                            "Bước 1: Hình ảnh thực tế cung cấp bằng chứng trực quan sinh động về hiện trạng của di sản (đền đài, di tích).",
                            "Bước 2: Biểu đồ số liệu lượng khách du lịch và ngân sách phục hồi giúp so sánh đối chiếu định lượng thuyết phục.",
                            "Bước 3: Tăng tính hấp dẫn thẩm mỹ, tránh sự đơn điệu và khô khan của khối văn bản chữ thuần túy."
                        ],
                        "answer": "Giúp thông tin trở nên trực quan, sinh động, chuẩn xác và có sức thuyết phục cao."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Lạm dụng hình ảnh trang trí không liên quan trực tiếp đến nội dung thông điệp chính của văn bản.",
                        "why": "Phương tiện phi ngôn ngữ trong văn bản thông tin phải có tính mục đích rõ ràng, hỗ trợ làm sáng tỏ thông tin."
                    }
                ]
            },
            {
                "id": "ch09",
                "title": "Bài 9: Hành trang cuộc sống",
                "description": "Nghị luận về một tư tưởng đạo lí, lối sống, thực hành tiếng Việt (biện pháp chêm xen, tu từ liệt kê) và chuẩn bị hành trang bước vào tương lai thế kỉ 21.",
                "lessons": [
                    {"id": "l01", "title": "Bài 1: Khát vọng tuổi trẻ và trách nhiệm công dân", "hasRealContent": True},
                    {"id": "l02", "title": "Bài 2: Thực hành viết bài văn nghị luận xã hội về một vấn đề đời sống", "hasRealContent": True}
                ],
                "concepts": [
                    {
                        "term": "Nghị luận xã hội về tư tưởng đạo lí và hiện tượng đời sống",
                        "definition": "Bàn luận, đánh giá về một quan niệm đạo đức, phẩm chất nhân cách (lòng dũng cảm, sự tự tin, lòng biết ơn) hoặc một hiện tượng xã hội nóng hổi cần giải pháp.",
                        "example": "Nghị luận về hiện tượng nghiện mạng xã hội ở giới trẻ và giải pháp xây dựng lối sống cân bằng, lành mạnh.",
                        "essence": "Bộc lộ chính kiến cá nhân, lập trường nhân sinh quan tích cực và trách nhiệm đối với cộng đồng."
                    }
                ],
                "rules": [
                    {
                        "statement": "Cấu trúc 5 bước giải quyết đề nghị luận xã hội",
                        "meaning": "Bước 1: Giải thích khái niệm trọng tâm. Bước 2: Bàn luận tính đúng đắn và biểu hiện thực tế. Bước 3: Phản đề (phê phán biểu hiện tiêu cực ngược lại). Bước 4: Nguyên nhân và giải pháp. Bước 5: Bài học nhận thức và hành động cá nhân.",
                        "example": "Khi bàn về 'Lòng dũng cảm', cần giải thích dũng cảm là gì, biểu hiện trong học tập chiến đấu, phê phán sự hèn nhát liều lĩnh, và rút ra bài học cho bản thân.",
                        "essence": "Tính toàn diện và đa chiều của tư duy phản biện."
                    }
                ],
                "workedExamples": [
                    {
                        "prompt": "Viết đoạn văn khoảng 200 chữ trình bày suy nghĩ về ý nghĩa của sự kiên trì theo đuổi ước mơ đối với học sinh lớp 10.",
                        "steps": [
                            "Bước 1: Mở đoạn: Dẫn dắt và khẳng định sự kiên trì là chìa khóa mở cánh cửa ước mơ.",
                            "Bước 2: Ý nghĩa: Kiên trì giúp vượt qua những thất bại ban đầu, rèn luyện bản lĩnh vững vàng và hoàn thiện kỹ năng.",
                            "Bước 3: Dẫn chứng tiêu biểu: Thomas Edison kiên trì thử nghiệm hàng ngàn lần trước khi phát minh ra bóng đèn dây tóc bền bỉ.",
                            "Bước 4: Phản đề: Phê phán lối sống nhanh nản chí, 'cả thèm chóng chán'.",
                            "Bước 5: Kết đoạn: Lời hứa hành động nỗ lực không ngừng mỗi ngày từ những việc học tập nhỏ nhất."
                        ],
                        "answer": "Đoạn văn logic, mạch lạc, có dẫn chứng xác thực và thông điệp truyền cảm hứng."
                    }
                ],
                "commonMistakes": [
                    {
                        "mistake": "Đưa ra lời khuyên sáo rỗng chung chung 'chúng ta phải cố gắng' mà không có dẫn chứng trải nghiệm thực tế.",
                        "why": "Bài nghị luận xã hội có sức lay động khi gắn liền với góc nhìn chân thành và những giải pháp hành động cụ thể."
                    }
                ]
            }
        ]
    }
}

# Add tieng-anh (10 units)
HUMANITIES_DATA["tieng-anh"] = {
    "id": "tieng-anh",
    "name": "Tiếng Anh",
    "icon": "🇬🇧",
    "chapters": [
        {
            "id": "ch01",
            "title": "Unit 1: Family Life",
            "description": "Vocabulary about household chores and family routines. Grammar: Present Simple vs. Present Continuous.",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Vocabulary & Pronunciation /br/, /kr/, /tr/", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Grammar: Present Simple vs. Present Continuous", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Present Simple vs. Present Continuous",
                    "definition": "Present Simple expresses habits, routines and permanent facts (always, usually, every day). Present Continuous expresses actions happening at the moment of speaking or temporary situations (now, at present, look!).",
                    "example": "My father usually cooks dinner, but today he is working late, so my mother is cooking.",
                    "essence": "The contrast between routine stability (Simple) and temporary ongoing activity (Continuous)."
                }
            ],
            "rules": [
                {
                    "statement": "Stative Verbs in Continuous Tenses",
                    "meaning": "Verbs expressing states, feelings, senses or possession (know, like, love, understand, believe, want) are normally NOT used in continuous forms.",
                    "example": "I understand the lesson now (NOT: I am understanding).",
                    "essence": "These verbs describe permanent inner mental/emotional states rather than physical dynamic actions."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Complete with the correct form of verbs: 'Be quiet! The baby (sleep) in the bedroom. She usually (sleep) for two hours in the afternoon.'",
                    "steps": [
                        "Step 1: 'Be quiet!' indicates an ongoing action right now => use Present Continuous: is sleeping.",
                        "Step 2: 'She usually' indicates a daily habit => use Present Simple: sleeps."
                    ],
                    "answer": "is sleeping - sleeps"
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Using 'am knowing' or 'am wanting' with stative verbs.",
                    "why": "Stative verbs do not describe physical actions and take simple tenses even with time markers like 'now'."
                }
            ]
        },
        {
            "id": "ch02",
            "title": "Unit 2: Humans and the Environment",
            "description": "Vocabulary about green living and carbon footprint. Grammar: Future with will vs. be going to, Passive voice.",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Vocabulary & Green Living", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Grammar: Will vs. Be going to & Passive Voice", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Future: Will vs. Be going to",
                    "definition": "'Will' is used for spontaneous decisions made at the moment of speaking and personal predictions without evidence. 'Be going to' is used for pre-existing plans and predictions based on present evidence.",
                    "example": "Look at those black clouds! It is going to rain. (Evidence). I am thirsty. - I will get you some water. (Spontaneous).",
                    "essence": "Planning and evidence separate 'be going to' from spontaneous impulse 'will'."
                }
            ],
            "rules": [
                {
                    "statement": "Passive Voice Structure",
                    "meaning": "Subject + Be (conjugated) + Past Participle (V3/ed) + (by Agent). Used when the action or object is more important than the doer.",
                    "example": "Plastic bottles are collected and recycled into eco-friendly bags.",
                    "essence": "Shifts focus from the subject doing the action to the recipient or outcome of the action."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Rewrite in the passive voice: 'People should plant more trees in urban areas.'",
                    "steps": [
                        "Step 1: Identify object: 'more trees'.",
                        "Step 2: Modal verb passive form: modal + be + V3 => 'should be planted'.",
                        "Step 3: Combine with remaining prepositional phrase: 'in urban areas'."
                    ],
                    "answer": "More trees should be planted in urban areas."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Using 'will' for a plan already arranged last week.",
                    "why": "Pre-meditated intentions and existing plans require 'be going to' or Present Continuous."
                }
            ]
        },
        {
            "id": "ch03",
            "title": "Unit 3: Music",
            "description": "Music genres, instruments and talent shows. Grammar: Compound sentences with coordinating conjunctions (FANBOYS), to-infinitives and bare infinitives.",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Vocabulary & Pronunciation /eɪ/, /aɪ/, /ɔɪ/", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Compound sentences & Infinitives (to V / V-bare)", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "To-infinitives vs. Bare Infinitives",
                    "definition": "Verbs followed by to-infinitive (want, decide, hope, promise, manage). Verbs followed by bare infinitive without 'to' (make, let, see, hear in active voice, modal verbs).",
                    "example": "The teacher made him practice the piano. She decided to enter the singing competition.",
                    "essence": "Causative and perception verbs demand bare infinitives; intention verbs demand to-infinitives."
                }
            ],
            "rules": [
                {
                    "statement": "Coordinating Conjunctions (FANBOYS)",
                    "meaning": "For, And, Nor, But, Or, Yet, So connect two independent clauses with a comma.",
                    "example": "He practiced singing every day, so he won first prize in the music contest.",
                    "essence": "Combines equal grammatical units into smooth, coherent compound ideas."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Combine the sentences using 'so' or 'but': 'The concert tickets were very expensive. We decided to buy them anyway.'",
                    "steps": [
                        "Step 1: Notice the contrast between expensive tickets and still deciding to buy.",
                        "Step 2: Use contrast conjunction 'but': add comma before 'but'."
                    ],
                    "answer": "The concert tickets were very expensive, but we decided to buy them anyway."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Using 'to' after modal verbs or 'let/make' (e.g., writing 'She let me to go').",
                    "why": "'Let' and 'make' in active voice are always followed by object + bare infinitive: 'let me go'."
                }
            ]
        },
        {
            "id": "ch04",
            "title": "Unit 4: For a Better Community",
            "description": "Community services, volunteering activities. Grammar: Past Simple vs. Past Continuous with when/while, Adjectives with -ed vs. -ing.",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Volunteer Work Vocabulary", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Past Simple vs. Past Continuous & -ed/-ing Adjectives", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Past Simple and Past Continuous with When/While",
                    "definition": "A long ongoing background action in the past (Past Continuous: was/were + V-ing) interrupted by a short, sudden action (Past Simple: V2/ed).",
                    "example": "While we were cleaning the local park, it started to rain heavily.",
                    "essence": "Past Continuous sets the movie scene; Past Simple triggers the sudden plot event."
                },
                {
                    "term": "Adjectives ending in -ed vs. -ing",
                    "definition": "-ed adjectives describe a person's inner feeling or reaction. -ing adjectives describe the characteristic of the thing or person that causes the feeling.",
                    "example": "The volunteer project was very interesting, so all students felt excited.",
                    "essence": "-ing is the cause of feeling; -ed is the receiver of feeling."
                }
            ],
            "rules": [
                {
                    "statement": "While + Past Continuous, When + Past Simple",
                    "meaning": "'While' introduces continuous duration; 'When' introduces punctual interruption.",
                    "example": "When the volunteer team arrived, the children were singing joyfully.",
                    "essence": "Time prepositions anchor grammatical aspect."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Choose the correct form: 'The children were (fascinating / fascinated) by the magic show at the charity center.'",
                    "steps": [
                        "Step 1: The subject 'children' experiences the emotion of amazement.",
                        "Step 2: Describing human feeling requires the -ed ending: fascinated."
                    ],
                    "answer": "fascinated"
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Saying 'I am very boring' when you actually mean 'I feel bored'.",
                    "why": "'I am boring' means you are a dull, uninteresting person; 'I am bored' means you feel lack of interest."
                }
            ]
        },
        {
            "id": "ch05",
            "title": "Unit 5: Inventions",
            "description": "Technological devices and AI inventions. Grammar: Present Perfect tense, Gerunds vs. Infinitives for purposes.",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Inventions & Digital Devices Vocabulary", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Present Perfect & Expressing Purpose (used for V-ing / used to V)", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Present Perfect Tense",
                    "definition": "Subject + have/has + V3/ed. Used for experiences (ever, never), actions starting in the past continuing to present (since, for), and past actions with results in the present (already, just, yet).",
                    "example": "Scientists have developed AI systems that can diagnose diseases faster than human doctors.",
                    "essence": "Bridges past actions with their ongoing relevance or consequence in the present moment."
                }
            ],
            "rules": [
                {
                    "statement": "Expressing purpose: Used to V vs. Used for V-ing",
                    "meaning": "Both express function/purpose of an invention: 'is used to + bare infinitive' OR 'is used for + V-ing'.",
                    "example": "A smartphone is used to communicate with people = A smartphone is used for communicating with people.",
                    "essence": "Equivalent grammatical structures describing instrument functionality."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Put the verb into Present Perfect or Past Simple: 'Thomas Edison (invent) the light bulb in 1879. Since then, lighting technology (improve) significantly.'",
                    "steps": [
                        "Step 1: 'in 1879' is a specific finished past time marker => use Past Simple: invented.",
                        "Step 2: 'Since then' connects past to present => use Present Perfect: has improved."
                    ],
                    "answer": "invented - has improved"
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Using Present Perfect with specific past time indicators like 'yesterday', 'in 2020', 'ago'.",
                    "why": "Specific completed time points strictly require Past Simple."
                }
            ]
        },
        {
            "id": "ch06",
            "title": "Unit 6: Gender Equality",
            "description": "Equal opportunities in education, careers and family roles. Grammar: Passive voice with modal verbs (can, must, should, may).",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Gender Equality & Careers Vocabulary", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Passive Voice with Modals (modal + be + V3)", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Passive Voice with Modal Verbs",
                    "definition": "Subject + Modal Verb (can/could/may/must/should) + be + Past Participle (V3/ed).",
                    "example": "Both men and women must be given equal opportunities in employment.",
                    "essence": "Expresses duty, necessity, or possibility with neutral objective focus."
                }
            ],
            "rules": [
                {
                    "statement": "Negative and Question Forms with Modals in Passive",
                    "meaning": "Negative: modal + not + be + V3. Question: Modal + Subject + be + V3?",
                    "example": "Gender discrimination should not be allowed in modern society.",
                    "essence": "Modal auxiliary governs the sentence polarity."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Rewrite the sentence into passive voice: 'Employers ought to treat female workers fairly.'",
                    "steps": [
                        "Step 1: Identify object: 'female workers'.",
                        "Step 2: Modal structure: ought to + be + treated fairly.",
                        "Step 3: Combine: 'Female workers ought to be treated fairly by employers.'"
                    ],
                    "answer": "Female workers ought to be treated fairly by employers."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Omitting 'be' after modal verbs in passive sentences (writing 'should treated' instead of 'should be treated').",
                    "why": "Modal verbs require bare infinitive 'be' before the past participle in all passive constructions."
                }
            ]
        },
        {
            "id": "ch07",
            "title": "Unit 7: Viet Nam and International Organisations",
            "description": "Viet Nam's active roles in UN, UNICEF, UNESCO, WTO. Grammar: Comparative and Superlative adjectives.",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: International Organisations Vocabulary", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Comparative and Superlative Adjectives", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Comparative vs. Superlative Adjectives",
                    "definition": "Comparatives compare 2 entities (short adj + -er + than / more + long adj + than). Superlatives compare 1 against a whole group (the + short adj + -est / the most + long adj).",
                    "example": "Viet Nam is becoming more active in peacekeeping missions. It is one of the most dynamic economies in Southeast Asia.",
                    "essence": "Degrees of quality across relative benchmarks."
                }
            ],
            "rules": [
                {
                    "statement": "Irregular Adjectives",
                    "meaning": "good -> better -> the best; bad -> worse -> the worst; far -> farther/further -> the farthest/furthest.",
                    "example": "Cooperation leads to better economic growth than trade barriers.",
                    "essence": "Historical etymology preserves suppletive comparative forms."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Complete: 'Joining international trade organizations has made our economy much (competitive) than before.'",
                    "steps": [
                        "Step 1: 'competitive' is a long adjective (4 syllables).",
                        "Step 2: 'than' signals comparative degree => use 'more competitive'."
                    ],
                    "answer": "more competitive"
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Double comparison: writing 'more better' or 'the most easiest'.",
                    "why": "Never use 'more' with -er adjectives, or 'most' with -est adjectives."
                }
            ]
        },
        {
            "id": "ch08",
            "title": "Unit 8: New Ways to Learn",
            "description": "Blended learning, digital platforms, educational apps. Grammar: Relative clauses with Who, Which, That, Whose.",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Digital Learning Vocabulary", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Defining Relative Clauses (Who, Which, That, Whose)", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Defining Relative Clauses",
                    "definition": "Provide essential information to identify the preceding noun. 'Who' for people, 'Which' for things/animals, 'That' for both, 'Whose' for possession.",
                    "example": "Students who use interactive learning apps tend to retain vocabulary longer.",
                    "essence": "Without the defining relative clause, the meaning of the main clause is incomplete."
                }
            ],
            "rules": [
                {
                    "statement": "No commas in Defining Relative Clauses",
                    "meaning": "Defining clauses are integrated directly without commas. 'That' cannot be used after a comma.",
                    "example": "The online platform that our school introduced is very user-friendly.",
                    "essence": "Essential restrictive identification."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Combine into one sentence using a relative pronoun: 'The software was developed by Vietnamese engineers. It helps students practice pronunciation.'",
                    "steps": [
                        "Step 1: 'It' refers to 'The software' (a thing).",
                        "Step 2: Replace 'It' with 'which' or 'that': 'The software which/that helps students practice pronunciation was developed by Vietnamese engineers.'"
                    ],
                    "answer": "The software which was developed by Vietnamese engineers helps students practice pronunciation."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Using 'which' to refer to a person (writing 'The teacher which teaches English').",
                    "why": "'Who' or 'that' must be used for human antecedents; 'which' is exclusively for inanimate objects and concepts."
                }
            ]
        },
        {
            "id": "ch09",
            "title": "Unit 9: Protecting the Environment",
            "description": "Deforestation, biodiversity conservation and global warming. Grammar: Reported speech (Statements and Questions).",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Environmental Protection Vocabulary", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Reported Speech (Backshift of tenses and pronouns)", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Reported Speech Tense Backshift",
                    "definition": "When the reporting verb is in the past (said, asked), tenses shift back one step: Present Simple -> Past Simple; Present Continuous -> Past Continuous; Will -> Would; Can -> Could.",
                    "example": "'We are planting trees,' they said. => They said that they were planting trees.",
                    "essence": "Transposing past direct utterances into contemporary indirect narrative perspectives."
                }
            ],
            "rules": [
                {
                    "statement": "Changes in time and place words in Reported Speech",
                    "meaning": "today -> that day; now -> then; yesterday -> the day before; tomorrow -> the following day; here -> there.",
                    "example": "'I will clean the beach tomorrow' => She said she would clean the beach the following day.",
                    "essence": "Temporal and spatial anchoring adjustments."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Change to reported speech: 'Why are wild animals losing their habitats?' the student asked.",
                    "steps": [
                        "Step 1: Reporting question: 'The student asked why...'.",
                        "Step 2: Wh-question retains question word 'why', followed by statement word order (Subject + Verb).",
                        "Step 3: Backshift tense from are losing to were losing."
                    ],
                    "answer": "The student asked why wild animals were losing their habitats."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Keeping question inversion in reported questions (writing 'He asked me where did I live' instead of 'where I lived').",
                    "why": "Reported questions become subordinate noun clauses and take standard statement word order (Subject + Verb)."
                }
            ]
        },
        {
            "id": "ch10",
            "title": "Unit 10: Ecotourism",
            "description": "Sustainable tourism, national parks and responsible travel. Grammar: Conditional Sentences Type 1 and Type 2.",
            "lessons": [
                {"id": "l01", "title": "Lesson 1: Ecotourism & Travel Vocabulary", "hasRealContent": True},
                {"id": "l02", "title": "Lesson 2: Conditional Sentences Type 1 & Type 2", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Conditional Sentence Type 1 vs. Type 2",
                    "definition": "Type 1: Real and possible in present/future (If + Present Simple, will + V-bare). Type 2: Unreal or hypothetical in present/future (If + Past Simple [were for all persons], would + V-bare).",
                    "example": "If tourists leave trash, they will damage the coral reef (Type 1). If I had more free time, I would join an eco-tour in Phong Nha (Type 2).",
                    "essence": "Probability separates real conditions (Type 1) from imaginary counterfactual hypotheses (Type 2)."
                }
            ],
            "rules": [
                {
                    "statement": "Use of 'were' in Conditionals Type 2",
                    "meaning": "In formal English, the subjunctive 'were' is used for all persons (I/he/she/it were) in the If-clause.",
                    "example": "If I were you, I would choose an eco-friendly homestay.",
                    "essence": "Subjunctive mood expressing non-fact."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Put verbs into correct form (Conditional Type 2): 'If people (care) more about nature, our planet (not be) in danger.'",
                    "steps": [
                        "Step 1: If-clause uses Past Simple: cared.",
                        "Step 2: Main clause uses would + V-bare: would not be."
                    ],
                    "answer": "cared - would not be"
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Putting 'will' or 'would' inside the If-clause (writing 'If it will rain' or 'If I would have money').",
                    "why": "Modal auxiliaries will/would belong in the main result clause, never in the conditional If-clause."
                }
            ]
        }
    ]
}

# Add lich-su (6 chapters)
HUMANITIES_DATA["lich-su"] = {
    "id": "lich-su",
    "name": "Lịch sử",
    "icon": "🏛️",
    "chapters": [
        {
            "id": "ch01",
            "title": "Chương 1: Lịch sử và Sử học",
            "description": "Hiện thực lịch sử và nhận thức lịch sử; Tri thức lịch sử và cuộc sống; Vai trò và phương pháp của khoa học lịch sử.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Hiện thực lịch sử và nhận thức lịch sử", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Tri thức lịch sử và cuộc sống", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Hiện thực lịch sử và Nhận thức lịch sử",
                    "definition": "Hiện thực lịch sử là toàn bộ những gì đã diễn ra trong quá khứ, tồn tại khách quan độc lập với ý muốn con người. Nhận thức lịch sử là những hiểu biết, tái hiện của con người về quá khứ qua tư liệu.",
                    "example": "Trận chiến Bạch Đằng năm 938 là hiện thực lịch sử khách quan; những trang sử ghi chép và đánh giá về chiến công của Ngô Quyền là nhận thức lịch sử.",
                    "essence": "Hiện thực lịch sử chỉ xảy ra một lần duy nhất; nhận thức lịch sử có thể thay đổi và ngày càng sâu sắc hơn theo thời gian nhờ phát hiện tư liệu mới."
                }
            ],
            "rules": [
                {
                    "statement": "Nguyên tắc cơ bản của Sử học",
                    "meaning": "Khách quan, trung thực, tiến bộ và toàn diện. Sử học phải dựa trên tư liệu có thật và được kiểm chứng khoa học.",
                    "example": "Không được xuyên tạc, bóp méo sự thật lịch sử vì bất kì mục đích chủ quan nào.",
                    "essence": "Sự thật lịch sử là linh hồn và phẩm giá của khoa học sử học."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Tại sao việc học tập và nghiên cứu lịch sử suốt đời là cần thiết đối với mỗi công dân?",
                    "steps": [
                        "Bước 1: Giúp hiểu rõ cội nguồn dân tộc, trân trọng truyền thống yêu nước và bản sắc văn hóa tổ tiên.",
                        "Bước 2: Rút ra bài học kinh nghiệm từ quá khứ để định hướng cho hiện tại và dự báo tương lai.",
                        "Bước 3: Phát triển tư duy phản biện, kỹ năng phân tích và tinh thần hội nhập quốc tế tự tin."
                    ],
                    "answer": "Bồi dưỡng lòng yêu nước, hiểu biết cội nguồn và vận dụng bài học quá khứ vào cuộc sống."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Đồng nhất nhận thức lịch sử của một cá nhân với toàn bộ hiện thực lịch sử khách quan.",
                    "why": "Nhận thức luôn bị giới hạn bởi tư liệu tìm thấy và góc nhìn chủ quan của người nghiên cứu."
                }
            ]
        },
        {
            "id": "ch02",
            "title": "Chương 2: Một số nền văn minh thế giới thời kì cổ - trung đại",
            "description": "Các nền văn minh phương Đông (Ai Cập, Lưỡng Hà, Trung Hoa, Ấn Độ) và phương Tây (Hy Lạp - La Mã, Phục hưng).",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Văn minh Ai Cập, Lưỡng Hà, Ấn Độ và Trung Hoa", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Văn minh Hy Lạp, La Mã và Văn minh thời Phục hưng", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Văn minh phương Đông và phương Tây cổ đại",
                    "definition": "Văn minh phương Đông hình thành bên các lưu vực sông lớn (sông Nin, Ấn, Hằng, Hoàng Hà), kinh tế nông nghiệp lúa nước, thể chế chuyên chế cổ đại. Văn minh phương Tây hình thành ven Địa Trung Hải, kinh tế thương nghiệp hàng hải, thể chế dân chủ chủ nô.",
                    "example": "Ai Cập có Kim tự tháp và chữ tượng hình; Hy Lạp - La Mã có đền Parthenon, Đấu trường Colosseum và nền triết học duy vật.",
                    "essence": "Điều kiện tự nhiên và phương thức sản xuất quy định đặc trưng thể chế chính trị và văn hóa của từng nền văn minh."
                }
            ],
            "rules": [
                {
                    "statement": "Đóng góp của Văn minh thời kì Phục hưng",
                    "meaning": "Đề cao giá trị con người (chủ nghĩa nhân văn), tự do cá nhân, giải phóng tư tưởng khỏi sự kìm kẹp của giáo hội thời Trung cổ.",
                    "example": "Kiệt tác hội họa Nàng Mona Lisa của Leonardo da Vinci, kịch Shakespeare.",
                    "essence": "Mở đường cho sự phát triển vượt bậc của khoa học tự nhiên và phương thức tư bản chủ nghĩa."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Nêu 4 phát minh kỹ thuật vĩ đại của văn minh Trung Hoa cổ - trung đại ảnh hưởng sâu sắc đến thế giới.",
                    "steps": [
                        "Bước 1: Giấy viết (Thái Luân cải tiến thời Hán).",
                        "Bước 2: Kỹ thuật in ấn (in mộc bản và chữ rời).",
                        "Bước 3: Thuốc súng (phục vụ quân sự).",
                        "Bước 4: La bàn (mở ra kỷ nguyên thám hiểm hàng hải vĩ đại)."
                    ],
                    "answer": "Tứ đại phát minh: Giấy, Kỹ thuật in, Thuốc súng và La bàn."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm lẫn giữa chữ số La Mã (I, V, X) với hệ thống chữ số Ả Rập (0, 1, 2... 9) có nguồn gốc từ Ấn Độ.",
                    "why": "Hệ thống 10 chữ số thập phân bao gồm số 0 do người Ấn Độ cổ đại phát minh, sau đó người Ả Rập truyền bá sang châu Âu."
                }
            ]
        },
        {
            "id": "ch03",
            "title": "Chương 3: Các cuộc cách mạng công nghiệp trong lịch sử thế giới",
            "description": "Cách mạng công nghiệp lần thứ nhất (động cơ hơi nước), lần thứ hai (điện khí hóa) và cách mạng công nghiệp 3.0, 4.0 thời đại số.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Cách mạng công nghiệp lần thứ nhất và lần thứ hai", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Cách mạng công nghiệp lần thứ ba và lần thứ tư (4.0)", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Cách mạng công nghiệp lần thứ nhất (1.0)",
                    "definition": "Khởi đầu ở nước Anh nửa sau thế kỉ XVIII, mở đầu bằng máy kéo sợi Jenny và động cơ hơi nước của James Watt, chuyển từ lao động thủ công sang lao động bằng máy móc cơ khí.",
                    "example": "Động cơ hơi nước ứng dụng vào xe lửa, tàu thủy và dệt may làm năng suất lao động tăng vọt hàng trăm lần.",
                    "essence": "Cơ khí hóa sản xuất và sự ra đời của giai cấp tư sản cùng vô sản công nghiệp."
                },
                {
                    "term": "Cách mạng công nghiệp lần thứ tư (4.0)",
                    "definition": "Khởi phát từ đầu thế kỉ XXI trên nền tảng tích hợp công nghệ số, vật lí và sinh học: Trí tuệ nhân tạo (AI), Dữ liệu lớn (Big Data), Internet vạn vật (IoT), Điện toán đám mây và Công nghệ sinh học.",
                    "example": "Nhà máy thông minh tự động hóa hoàn toàn với robot AI và dây chuyền in 3D.",
                    "essence": "Xóa mờ ranh giới giữa thế giới vật lý, kỹ thuật số và sinh học."
                }
            ],
            "rules": [
                {
                    "statement": "Tác động xã hội của các cuộc cách mạng công nghiệp",
                    "meaning": "Làm thay đổi căn bản cơ cấu kinh tế, thúc đẩy đô thị hóa nhanh chóng, đồng thời đặt ra thách thức về môi trường và an sinh việc làm.",
                    "example": "Sự xuất hiện của AI tạo ra năng suất vượt trội nhưng cũng đe dọa thay thế các công việc lao động lặp đi lặp lại.",
                    "essence": "Công nghệ là động lực giải phóng sức lao động nhưng đòi hỏi con người phải liên tục nâng cao trình độ tri thức."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "So sánh nguồn năng lượng cốt lõi giữa Cách mạng công nghiệp lần thứ nhất và lần thứ hai.",
                    "steps": [
                        "Bước 1: CMCN lần 1 (thế kỉ XVIII - XIX): Dựa trên năng lượng hơi nước và than đá đốt lò.",
                        "Bước 2: CMCN lần 2 (cuối thế kỉ XIX - đầu XX): Dựa trên năng lượng điện lực và động cơ đốt trong (dầu mỏ).",
                        "Bước 3: Ý nghĩa: Điện lực cho phép truyền tải năng lượng đi xa hàng nghìn km và thúc đẩy dây chuyền lắp ráp hàng loạt."
                    ],
                    "answer": "CMCN 1 dùng hơi nước/than đá; CMCN 2 dùng điện lực và dầu mỏ."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Cho rằng máy kéo sợi Jenny chạy bằng động cơ hơi nước.",
                    "why": "Máy kéo sợi Jenny ban đầu chạy bằng sức người quay tay; sau đó Arkwright cải tiến chạy bằng sức nước, và chỉ sau đó động cơ hơi nước của James Watt mới được tích hợp vào nhà máy dệt."
                }
            ]
        },
        {
            "id": "ch04",
            "title": "Chương 4: Văn minh Đông Nam Á thời kì cổ - trung đại",
            "description": "Cơ sở hình thành văn minh Đông Nam Á, quá trình phát triển của các vương quốc cổ và phong kiến, sự tiếp thu và bản địa hóa văn hóa Ấn Độ, Trung Hoa.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Cơ sở hình thành và phát triển văn minh Đông Nam Á", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Thành tựu văn hóa tiêu biểu của Đông Nam Á", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Văn minh nông nghiệp lúa nước Đông Nam Á",
                    "definition": "Được xây dựng trên nền tảng khí hậu nhiệt đới gió mùa ẩm, canh tác cây lúa nước, gắn liền với văn hóa xóm làng, tín ngưỡng phồn thực và sùng bái tự nhiên.",
                    "example": "Trống đồng Đông Sơn (Việt Nam) khắc họa đời sống cư dân lúa nước, hội hè chèo thuyền và chim lạc.",
                    "essence": "Bản sắc văn hóa bản địa độc đáo và bền vững trước các làn sóng văn hóa ngoại lai."
                },
                {
                    "term": "Quá trình bản địa hóa văn hóa ngoại lai",
                    "definition": "Tiếp thu các tôn giáo lớn (Phật giáo, Ấn Độ giáo, Hồi giáo) và chữ viết (Sanskrit, chữ Hán) nhưng cải biến, sáng tạo để phù hợp với tâm thức và truyền thống dân tộc.",
                    "example": "Quần thể đền tháp Ăng-co Vát (Campuchia), Tháp Bô-rô-bu-đua (Indonesia) và Chữ Nôm (Việt Nam).",
                    "essence": "'Hòa nhập nhưng không hòa tan' tạo nên tính thống nhất trong đa dạng của văn hóa Đông Nam Á."
                }
            ],
            "rules": [
                {
                    "statement": "Vị trí địa - chiến lược cầu nối của Đông Nam Á",
                    "meaning": "Nằm trên ngã tư đường giao thương hàng hải quốc tế kết nối giữa Ấn Độ Dương và Thái Bình Dương, giữa châu Á và châu Úc.",
                    "example": "Eo biển Malacca là tuyến đường buôn bán hương liệu và tơ lụa sầm uất bậc nhất thế giới cổ - trung đại.",
                    "essence": "Mở rộng giao lưu tiếp biến văn hóa và phát triển mạnh kinh tế thương mại biển."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Chứng minh sự sáng tạo độc đáo của người Việt cổ trong việc tiếp thu văn hóa Trung Hoa thời kỳ trung đại.",
                    "steps": [
                        "Bước 1: Về chữ viết: Tiếp thu chữ Hán nhưng đã sáng tạo ra chữ Nôm để ghi âm tiếng Việt.",
                        "Bước 2: Về tư tưởng: Tiếp thu Nho giáo nhưng kết hợp chặt chẽ với lòng yêu nước và Phật giáo, Đạo giáo (Tam giáo đồng nguyên).",
                        "Bước 3: Về luật pháp: Bộ luật Hồng Đức vừa tiếp thu luật Đường vừa bảo vệ quyền lợi người phụ nữ (quyền thừa kế hương hỏa)."
                    ],
                    "answer": "Người Việt luôn bản địa hóa văn hóa ngoại lai để phục vụ công cuộc tự chủ và khẳng định bản sắc dân tộc."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Cho rằng văn minh Đông Nam Á hoàn toàn là sự sao chép thụ động từ Ấn Độ và Trung Hoa.",
                    "why": "Trước khi tiếp xúc với Ấn Độ và Trung Hoa, Đông Nam Á đã có một nền văn minh bản địa nông nghiệp lúa nước rực rỡ với văn hóa đồng thau (Đông Sơn, Sa Huỳnh)."
                }
            ]
        },
        {
            "id": "ch05",
            "title": "Chương 5: Một số nền văn minh trên đất nước Việt Nam trước 1858",
            "description": "Văn minh Văn Lang - Âu Lạc, Văn minh Chăm-pa, Văn minh Phù Nam và bước phát triển rực rỡ của Văn minh Đại Việt qua các triều đại Lý, Trần, Lê sơ.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Văn minh Văn Lang - Âu Lạc, Chăm-pa và Phù Nam", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Văn minh Đại Việt thời kì Lý - Trần - Lê", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Văn minh Đại Việt",
                    "definition": "Là nền văn minh phát triển rực rỡ trong thời kì độc lập tự chủ (từ thế kỉ X đến thế kỉ XIX), kế thừa văn minh Văn Lang - Âu Lạc, tiếp thu có chọn lọc tinh hoa văn hóa bên ngoài.",
                    "example": "Kinh thành Thăng Long, trường đại học đầu tiên Quốc Tử Giám (1076), chiến thắng ba lần đánh tan quân Nguyên Mông thời Trần.",
                    "essence": "Biểu tượng đỉnh cao của tinh thần tự chủ, độc lập và sức sáng tạo văn hóa bền bỉ của dân tộc Việt Nam."
                }
            ],
            "rules": [
                {
                    "statement": "Truyền thống 'Lấy dân làm gốc' trong văn minh Đại Việt",
                    "meaning": "Tư tưởng trị nước an dân: 'Khoan thư sức dân để làm kế sâu rễ bền gốc' (Trần Hưng Đạo), 'Lật thuyền mới biết dân như nước' (Nguyễn Trãi).",
                    "example": "Chính sách ngụ binh ư nông vừa đảm bảo sản xuất nông nghiệp vừa sẵn sàng lực lượng quân sự bảo vệ tổ quốc.",
                    "essence": "Sức mạnh vô địch của toàn dân tộc bắt nguồn từ lòng dân đoàn kết."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Trình bày ý nghĩa lịch sử của việc thành lập Văn Miếu (1070) và Quốc Tử Giám (1076) thời nhà Lý.",
                    "steps": [
                        "Bước 1: Văn Miếu lập năm 1070 thờ Khổng Tử thể hiện sự coi trọng Nho giáo và đạo học.",
                        "Bước 2: Quốc Tử Giám lập năm 1076 là trường đại học đầu tiên của Việt Nam đào tạo nhân tài cho đất nước.",
                        "Bước 3: Đánh dấu bước ngoặt chuyển từ tuyển chọn quan lại theo dòng dõi quý tộc sang thi cử tuyển chọn hiền tài công khai."
                    ],
                    "answer": "Khởi đầu cho nền giáo dục đại học chính quy và khẳng định truyền thống hiếu học tôn sư trọng đạo của dân tộc."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm lẫn thời điểm lập Văn Miếu và Quốc Tử Giám sang thời nhà Trần hoặc nhà Lê.",
                    "why": "Văn Miếu lập năm 1070 và Quốc Tử Giám lập năm 1076 đều thuộc triều đại nhà Lý (thời vua Lý Thánh Tông và Lý Nhân Tông)."
                }
            ]
        },
        {
            "id": "ch06",
            "title": "Chương 6: Cộng đồng các dân tộc Việt Nam",
            "description": "Thành phần 54 dân tộc Việt Nam, sự phân bố địa bàn sinh sống, bản sắc văn hóa và truyền thống đoàn kết toàn dân tộc qua các thời kỳ lịch sử.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Các dân tộc trên đất nước Việt Nam", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Khối đại đoàn kết dân tộc và chính sách dân tộc của Đảng, Nhà nước", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Khối đại đoàn kết toàn dân tộc",
                    "definition": "Sự gắn kết bền chặt keo sơn giữa 54 dân tộc anh em cùng chung sống trên lãnh thổ Việt Nam qua hàng ngàn năm cùng dựng nước và giữ nước.",
                    "example": "Đồng bào các dân tộc thiểu số vùng Tây Bắc, Việt Bắc, Tây Nguyên kiên trung theo Đảng kháng chiến thắng lợi.",
                    "essence": "Đoàn kết là cội nguồn sức mạnh vô địch giúp dân tộc Việt Nam vượt qua mọi thảm họa thiên tai và chiến thắng mọi kẻ thù xâm lược."
                }
            ],
            "rules": [
                {
                    "statement": "Nguyên tắc chính sách dân tộc của Nhà nước Việt Nam",
                    "meaning": "Bình đẳng, đoàn kết, tôn trọng và giúp nhau cùng tiến bộ; bảo tồn và phát huy bản sắc văn hóa tốt đẹp của từng dân tộc.",
                    "example": "Ưu tiên đầu tư đường sá, trường học, trạm y tế, điện lưới quốc gia cho vùng sâu vùng xa đồng bào dân tộc thiểu số.",
                    "essence": "Thu hẹp khoảng cách phát triển kinh tế xã hội và bảo đảm công bằng xã hội."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Tại sao nói văn hóa của 54 dân tộc Việt Nam mang tính chất 'Thống nhất trong đa dạng'?",
                    "steps": [
                        "Bước 1: 'Đa dạng': Mỗi dân tộc có tiếng nói, trang phục, nhà ở, lễ hội và phong tục tập quán độc đáo riêng (nhà rông Tây Nguyên, múa khèn Mông, cồng chiêng, đờn ca tài tử).",
                        "Bước 2: 'Thống nhất': Cùng chung cội nguồn lịch sử con rồng cháu tiên, chung tình yêu quê hương đất nước, tinh thần tương thân tương ái 'lá lành đùm lá rách'.",
                        "Bước 3: Kết luận: Sự hòa quyện tạo nên bức tranh văn hóa Việt Nam phong phú, giàu bản sắc và vững bền."
                    ],
                    "answer": "Đa dạng về sắc thái văn hóa địa phương nhưng thống nhất ở cội nguồn lịch sử và tinh thần yêu nước."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng đồng bào dân tộc thiểu số chỉ sống ở miền núi phía Bắc.",
                    "why": "Các dân tộc thiểu số phân bố rộng khắp trên toàn quốc: Tây Bắc, Đông Bắc, Duyên hải miền Trung, Tây Nguyên và Đồng bằng sông Cửu Long (người Chăm, Khmer, Hoa...)."
                }
            ]
        }
    ]
}

# Add dia-li (10 chapters)
HUMANITIES_DATA["dia-li"] = {
    "id": "dia-li",
    "name": "Địa lí",
    "icon": "🌍",
    "chapters": [
        {
            "id": "ch01",
            "title": "Chương 1: Sử dụng bản đồ",
            "description": "Các phương pháp biểu hiện đối tượng địa lí trên bản đồ, ứng dụng của GPS và bản đồ số trong đời sống và sản xuất hiện đại.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Một số phương pháp biểu hiện các đối tượng địa lí trên bản đồ", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Sử dụng bản đồ trong học tập và đời sống", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Bản đồ và Hệ thống định vị toàn cầu (GPS)",
                    "definition": "Bản đồ là hình ảnh thu nhỏ tương đối chính xác của bề mặt Trái Đất lên mặt phẳng. GPS là hệ thống vệ tinh cung cấp tọa độ vị trí không gian chính xác tại mọi thời điểm.",
                    "example": "Ứng dụng gọi xe công nghệ hoặc chỉ đường Google Maps sử dụng GPS để xác định vị trí và lộ trình di chuyển tối ưu.",
                    "essence": "Số hóa không gian địa lý phục vụ quản lý giao thông, cứu nạn cứu hộ và quy hoạch phát triển đô thị."
                }
            ],
            "rules": [
                {
                    "statement": "Phương pháp kí hiệu trên bản đồ",
                    "meaning": "Dùng kí hiệu hình học, chữ hoặc tượng hình đặt chính xác tại vị trí tọa độ của đối tượng để biểu thị vị trí, chất lượng và số lượng đối tượng.",
                    "example": "Kí hiệu hình tròn màu đen biểu thị mỏ than, tam giác đen biểu thị mỏ sắt.",
                    "essence": "Mã hóa trực quan các thông tin phân bố địa lý không gian."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Trên bản đồ tỉ lệ 1 : 200.000, khoảng cách giữa hai thành phố đo được là 5 cm. Tính khoảng cách thực tế ngoài thực địa theo km.",
                    "steps": [
                        "Bước 1: Tỉ lệ 1 : 200.000 có nghĩa là 1 cm trên bản đồ tương ứng 200.000 cm ngoài thực địa.",
                        "Bước 2: Khoảng cách thực tế: d = 5 cm · 200.000 = 1.000.000 cm.",
                        "Bước 3: Đổi đơn vị: 1.000.000 cm = 10.000 m = 10 km."
                    ],
                    "answer": "Khoảng cách thực tế là 10 km."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nhầm lẫn khi đổi đơn vị từ cm sang km (chia nhầm cho 1.000 thay vì 100.000).",
                    "why": "1 km = 1.000 m = 100.000 cm."
                }
            ]
        },
        {
            "id": "ch02",
            "title": "Chương 2: Trái Đất",
            "description": "Vị trí trong Hệ Mặt Trời, chuyển động tự quay quanh trục, chuyển động quanh Mặt Trời và các hệ quả: ngày đêm, mùa, giờ trên Trái Đất.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Trái Đất trong hệ Mặt Trời và chuyển động tự quay", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Chuyển động của Trái Đất quanh Mặt Trời và các hệ quả địa lí", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Lực Coriolis (Cô-ri-ô-lít)",
                    "definition": "Là lực quán tính sinh ra do Trái Đất tự quay quanh trục từ Tây sang Đông, làm lệch hướng chuyển động của các vật thể (dòng nước, gió) trên bề mặt Trái Đất.",
                    "example": "Ở bán cầu Bắc, các dòng sông chảy bị xói mòn mạnh ở bờ bên phải theo hướng chuyển động.",
                    "essence": "Ở bán cầu Bắc vật lệch về bên phải; ở bán cầu Nam vật lệch về bên trái theo hướng di chuyển."
                }
            ],
            "rules": [
                {
                    "statement": "Hệ quả chuyển động quay quanh Mặt Trời",
                    "meaning": "Do trục Trái Đất nghiêng 66°33' với mặt phẳng quỹ đạo và không đổi phương khi chuyển động sinh ra hiện tượng các mùa trong năm và ngày đêm dài ngắn theo vĩ độ.",
                    "example": "Vào mùa hè ở bán cầu Bắc (từ 21/3 đến 23/9), bán cầu Bắc chúc về phía Mặt Trời nên có ngày dài hơn đêm.",
                    "essence": "Sự phân bố lượng nhiệt và ánh sáng mặt trời không đều theo thời gian và không gian."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Khi ở Luân Đôn (múi giờ số 0) là 6 giờ sáng ngày 1/1, thì ở Hà Nội (múi giờ số 7) và Tokyo (múi giờ số 9) là mấy giờ cùng ngày?",
                    "steps": [
                        "Bước 1: Hà Nội ở múi giờ số 7, sớm hơn Luân Đôn 7 giờ => Giờ Hà Nội = 6 + 7 = 13 giờ (1 giờ chiều ngày 1/1).",
                        "Bước 2: Tokyo ở múi giờ số 9, sớm hơn Luân Đôn 9 giờ => Giờ Tokyo = 6 + 9 = 15 giờ (3 giờ chiều ngày 1/1)."
                    ],
                    "answer": "Hà Nội là 13 giờ; Tokyo là 15 giờ ngày 1/1."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Lấy giờ Luân Đôn trừ đi số múi giờ khi tính giờ các khu vực phía Đông.",
                    "why": "Trái Đất quay từ Tây sang Đông, các khu vực phía Đông đón ánh bình minh sớm hơn nên phải CỘNG thêm chênh lệch múi giờ."
                }
            ]
        },
        {
            "id": "ch03",
            "title": "Chương 3: Thạch quyển",
            "description": "Cấu trúc Trái Đất, thuyết kiến tạo mảng, tác động của nội lực (uốn nếp, đứt gãy, núi lửa) và ngoại lực (phong hóa, bóc mòn, bồi tụ) đến địa hình.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Thạch quyển và thuyết kiến tạo mảng", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Tác động của nội lực và ngoại lực đến địa hình bề mặt Trái Đất", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Nội lực và Ngoại lực",
                    "definition": "Nội lực sinh ra từ bên trong Trái Đất (năng lượng phân rã phóng xạ, phản ứng nhiệt hạt nhân) có xu hướng làm gồ ghề bề mặt địa hình. Ngoại lực sinh ra từ bên ngoài (nắng, mưa, gió, sinh vật) có xu hướng san phẳng địa hình.",
                    "example": "Nội lực đẩy dâng tạo nên dãy núi Everest cao sừng sững; ngoại lực xói mòn bào mòn đỉnh núi qua hàng triệu năm.",
                    "essence": "Địa hình bề mặt Trái Đất là kết quả của sự tác động đồng thời và đối lập liên tục giữa nội lực và ngoại lực."
                }
            ],
            "rules": [
                {
                    "statement": "Thuyết kiến tạo mảng",
                    "meaning": "Thạch quyển gồm các mảng kiến tạo nổi trên lớp manti mềm và di chuyển chậm chạp. Nơi tiếp xúc giữa các mảng xô vào nhau hoặc tách xa nhau sinh ra động đất, núi lửa và các dãy núi uốn nếp lớn.",
                    "example": "Mảng Ấn Độ xô vào mảng Á - Âu tạo nên dãy Himalaya kỳ vĩ.",
                    "essence": "Vỏ Trái Đất không phải là một khối nguyên vẹn bất động mà luôn vận động kiến tạo liên tục."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Phân tích 3 quá trình chính của tác động ngoại lực làm biến đổi địa hình.",
                    "steps": [
                        "Bước 1: Quá trình phong hóa (lí học, hóa học, sinh học): phá hủy và làm biến đổi đá tại chỗ thành vụn bở.",
                        "Bước 2: Quá trình bóc mòn: nước chảy, gió thổi, sóng biển di chuyển các sản phẩm phong hóa rời khỏi vị trí ban đầu.",
                        "Bước 3: Quá trình vận chuyển và bồi tụ: lắng đọng vật liệu tạo nên các đồng bằng châu thổ phì nhiêu (như ĐBSCL)."
                    ],
                    "answer": "Ba quá trình liên hoàn: Phong hóa -> Bóc mòn/Vận chuyển -> Bồi tụ."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng quá trình phong hóa làm dịch chuyển đất đá đi xa hàng trăm km.",
                    "why": "Phong hóa chỉ phá hủy đá TẠI CHỖ; việc vận chuyển đất đá đi xa là nhiệm vụ của quá trình bóc mòn và dòng chảy."
                }
            ]
        },
        {
            "id": "ch04",
            "title": "Chương 4: Khí quyển",
            "description": "Nhiệt độ không khí, khí áp và các khối khí, các loại gió chính trên Trái Đất (gió Tín phong, gió Tây ôn đới, gió mùa) và sự phân bố lượng mưa.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khí quyển, nhiệt độ không khí và khí áp", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Gió và sự phân bố lượng mưa trên Trái Đất", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Gió và Quy luật thổi của gió",
                    "definition": "Gió là sự chuyển động của không khí từ nơi có khí áp cao về nơi có khí áp thấp. Chênh lệch khí áp càng lớn thì gió thổi càng mạnh.",
                    "example": "Gió mùa mùa hạ ở Việt Nam thổi từ áp cao biển Ấn Độ Dương - Thái Bình Dương vào áp thấp lục địa châu Á mang theo mưa lớn.",
                    "essence": "Khí áp là nguyên nhân trực tiếp sinh ra gió."
                }
            ],
            "rules": [
                {
                    "statement": "Quy luật giảm nhiệt độ theo độ cao",
                    "meaning": "Trong tầng đối lưu, càng lên cao không khí càng loãng, cứ lên cao 100m thì nhiệt độ không khí giảm trung bình 0.6°C.",
                    "example": "Nếu chân núi ở độ cao 0m có nhiệt độ 30°C, thì trên đỉnh núi cao 2000m nhiệt độ là 30 - 20 · 0.6 = 18°C.",
                    "essence": "Mặt đất hấp thụ bức xạ mặt trời rồi đốt nóng tầng không khí sát mặt đất trước."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Tại sườn đón gió ẩm của một dãy núi cao 3000m, chân núi có nhiệt độ 28°C. Tính nhiệt độ tại đỉnh núi.",
                    "steps": [
                        "Bước 1: Độ cao chênh lệch: h = 3000 m.",
                        "Bước 2: Ở sườn đón gió ẩm, cứ lên cao 100m nhiệt độ giảm 0.6°C => Tổng độ giảm: ΔT = (3000 / 100) · 0.6 = 30 · 0.6 = 18°C.",
                        "Bước 3: Nhiệt độ đỉnh núi: T_đỉnh = 28 - 18 = 10°C."
                    ],
                    "answer": "Nhiệt độ tại đỉnh núi là 10°C."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Áp dụng độ giảm 0.6°C/100m cho sườn khuất gió (gió phơn khô nóng).",
                    "why": "Ở sườn khuất gió khi không khí khô đi xuống, nhiệt độ tăng 1°C cho mỗi 100m xuống thấp (hiệu ứng phơn)."
                }
            ]
        },
        {
            "id": "ch05",
            "title": "Chương 5: Thủy quyển",
            "description": "Nước trên lục địa (sông, hồ, nước ngầm, băng hà), sóng biển, thủy triều, dòng biển và vai trò bảo vệ tài nguyên nước ngọt.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Thủy quyển và nước trên lục địa", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Nước biển và đại dương: Sóng, thủy triều, dòng biển", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Thủy triều",
                    "definition": "Là hiện tượng dao động thường xuyên có chu kì của các khối nước trong các biển và đại dương do lực hấp dẫn của Mặt Trăng và Mặt Trời tác dụng lên Trái Đất.",
                    "example": "Triều cường xuất hiện vào các ngày không trăng (mồng 1) và ngày trăng tròn (ngày rằm 15 âm lịch) khi Mặt Trời, Mặt Trăng và Trái Đất thẳng hàng.",
                    "essence": "Lực hút thiên thể kết hợp lực quán tính li tâm sinh ra triều dâng và triều rút."
                }
            ],
            "rules": [
                {
                    "statement": "Chế độ nước sông và nguồn cấp nước",
                    "meaning": "Sông ở vùng nhiệt đới gió mùa có chế độ nước phụ thuộc vào mùa mưa; sông ở vùng ôn đới lạnh phụ thuộc vào mùa tuyết băng tan vào mùa xuân.",
                    "example": "Sông Hồng có mùa lũ từ tháng 6 đến tháng 10 trùng với mùa mưa gió mùa mùa hạ ở miền Bắc.",
                    "essence": "Khí hậu là nhân tố quyết định trực tiếp đến chế độ dòng chảy thủy văn của sông ngòi."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Tại sao các dòng biển nóng và dòng biển lạnh lại có ảnh hưởng lớn đến khí hậu ven bờ nơi chúng đi qua?",
                    "steps": [
                        "Bước 1: Nơi có dòng biển nóng chảy qua: nước bốc hơi mạnh, không khí ẩm, gây mưa nhiều cho các vùng duyên hải ven bờ.",
                        "Bước 2: Nơi có dòng biển lạnh chảy qua: nhiệt độ nước biển thấp, không khí sát mặt nước lạnh ngưng tụ không bốc lên cao được, mưa rất ít, thường tạo thành hoang mạc ven biển (như hoang mạc Atacama, Namib)."
                    ],
                    "answer": "Dòng biển nóng gây mưa nhiều, ẩm ướt; dòng biển lạnh gây khô hạn, hình thành hoang mạc."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng triều cường xảy ra vào ngày trăng khuyết (mồng 7, 8 và 22, 23 âm lịch).",
                    "why": "Vào ngày trăng khuyết là hiện tượng TRIỀU KÉM (dao động nhỏ nhất) do Mặt Trời và Mặt Trăng vuông góc với nhau."
                }
            ]
        },
        {
            "id": "ch06",
            "title": "Chương 6: Sinh quyển và Thổ nhưỡng",
            "description": "Khái niệm đất, các nhân tố hình thành đất, giới hạn và đặc điểm của sinh quyển, các nhân tố ảnh hưởng đến sự phân bố sinh vật.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Đất và các nhân tố hình thành đất", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Sinh quyển và sự phân bố sinh vật trên Trái Đất", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Thổ nhưỡng (Đất)",
                    "definition": "Là lớp vật chất tơi xốp trên bề mặt lục địa, được đặc trưng bởi độ phì (khả năng cung cấp nước, chất dinh dưỡng, nhiệt và khí cho cây trồng sinh trưởng).",
                    "example": "Đất đỏ bazan ở Tây Nguyên phì nhiêu rất thích hợp cho việc phát triển các cây công nghiệp lâu năm như cà phê, cao su.",
                    "essence": "Đất là sản phẩm giao thoa tương tác giữa 5 nhân tố: đá mẹ, khí hậu, sinh vật, địa hình và thời gian (kèm tác động con người)."
                }
            ],
            "rules": [
                {
                    "statement": "Vai trò của sinh vật trong quá trình hình thành đất",
                    "meaning": "Cung cấp chất hữu cơ (xác thực vật, động vật phân hủy thành mùn) và phá hủy đá gốc thông qua rễ cây và vi sinh vật.",
                    "example": "Rễ cây tiết axit hòa tan đá vôi và len lỏi làm nứt vỡ đá gốc.",
                    "essence": "Sinh vật là nhân tố chủ đạo tạo nên độ phì nhiêu màu mỡ của đất."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Phân tích tác động của khí hậu đến sự hình thành đất.",
                    "steps": [
                        "Bước 1: Nhiệt độ và độ ẩm thúc đẩy quá trình phong hóa đá diễn ra nhanh hay chậm.",
                        "Bước 2: Lượng mưa quyết định quá trình hòa tan, rửa trôi hoặc tích tụ các chất dinh dưỡng trong phẫu diện đất.",
                        "Bước 3: Khí hậu chi phối gián tiếp qua việc phát triển lớp thảm thực vật cung cấp mùn cho đất."
                    ],
                    "answer": "Khí hậu tác động trực tiếp qua nhiệt ẩm và tác động gián tiếp qua giới sinh vật."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Coi đá mẹ là nhân tố cung cấp chất hữu cơ cho đất.",
                    "why": "Đá mẹ chỉ cung cấp chất khoáng vô cơ; chất hữu cơ cho đất hoàn toàn do sinh vật cung cấp."
                }
            ]
        },
        {
            "id": "ch07",
            "title": "Chương 7: Một số quy luật của lớp vỏ địa lí",
            "description": "Lớp vỏ địa lí, quy luật thống nhất và hoàn chỉnh, quy luật địa đới và quy luật phi địa đới.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Quy luật thống nhất và hoàn chỉnh của lớp vỏ địa lí", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Quy luật địa đới và quy luật phi địa đới", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Quy luật thống nhất và hoàn chỉnh",
                    "definition": "Là quy luật về mối quan hệ quy định lẫn nhau giữa các thành phần tự nhiên (đá, khí, nước, đất, sinh vật). Một thành phần thay đổi sẽ kéo theo sự thay đổi của tất cả các thành phần còn lại.",
                    "example": "Phá rừng đầu nguồn (sinh vật) -> xói mòn rửa trôi đất (thổ nhưỡng) -> sông ngòi bồi lắng lũ quét dâng cao (thủy văn) -> hạn hán gay gắt (khí hậu).",
                    "essence": "Tự nhiên là một thể thống nhất hữu cơ, con người phải dự báo trước mọi tác động khi khai thác môi trường."
                }
            ],
            "rules": [
                {
                    "statement": "Quy luật địa đới",
                    "meaning": "Sự thay đổi có quy luật của các thành phần địa lí và cảnh quan từ Xích đạo về hai Cực do Trái Đất hình cầu nhận lượng bức xạ giảm dần theo vĩ độ.",
                    "example": "Các đới khí hậu, thảm thực vật thay đổi từ xích đạo -> nhiệt đới -> cận nhiệt -> ôn đới -> hàn đới.",
                    "essence": "Góc nhập xạ của tia sáng mặt trời giảm dần từ xích đạo lên các cực."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Từ quy luật thống nhất và hoàn chỉnh, rút ra bài học gì cho con người trong việc can thiệp vào tự nhiên?",
                    "steps": [
                        "Bước 1: Trước khi xây dựng các công trình lớn (thủy điện, san lấp biển, khai thác khoáng sản), phải đánh giá tác động môi trường toàn diện.",
                        "Bước 2: Cần khai thác tài nguyên hợp lí, không chặt phá rừng đầu nguồn làm mất cân bằng sinh thái.",
                        "Bước 3: Phát triển kinh tế phải đi đôi với bảo vệ môi trường và phục hồi tài nguyên thiên nhiên."
                    ],
                    "answer": "Phải nghiên cứu kỹ mối quan hệ tương hỗ và dự báo hậu quả sinh thái trước khi can thiệp vào tự nhiên."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng quy luật đai cao (lên cao nhiệt độ giảm cảnh quan thay đổi) thuộc về quy luật địa đới.",
                    "why": "Quy luật đai cao và quy luật địa ô thuộc về quy luật PHI ĐỊA ĐỚI (do địa hình và vị trí lục địa/đại dương, không phải do vĩ độ)."
                }
            ]
        },
        {
            "id": "ch08",
            "title": "Chương 8: Địa lí dân cư",
            "description": "Gia tăng dân số, cơ cấu dân số (theo tuổi, giới, lao động), phân bố dân cư và quá trình đô thị hóa trên thế giới.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Gia tăng dân số và cơ cấu dân số thế giới", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Phân bố dân cư và quá trình đô thị hóa", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Gia tăng dân số tự nhiên và cơ học",
                    "definition": "Gia tăng tự nhiên bằng tỉ suất sinh thô trừ tỉ suất tử thô: Tg = S - T (%). Gia tăng cơ học là sự chênh lệch giữa số người nhập cư và xuất cư.",
                    "example": "Nhiều nước châu Âu có gia tăng tự nhiên âm (sinh ít hơn chết), dân số duy trì nhờ nhập cư cơ học.",
                    "essence": "Gia tăng tự nhiên quyết định sự biến động dân số của toàn bộ thế giới."
                },
                {
                    "term": "Đô thị hóa",
                    "definition": "Là quá trình kinh tế - xã hội biểu hiện ở sự tăng nhanh số lượng và quy mô các đô thị, tập trung dân cư vào các đô thị và phổ biến lối sống đô thị.",
                    "example": "Tỉ lệ dân thành thị toàn cầu đã vượt quá 55% và dự báo tiếp tục tăng mạnh tại các nước đang phát triển.",
                    "essence": "Đô thị hóa là thước đo và động lực của quá trình công nghiệp hóa, hiện đại hóa."
                }
            ],
            "rules": [
                {
                    "statement": "Cơ cấu dân số theo độ tuổi",
                    "meaning": "Cơ cấu dân số vàng: tỉ lệ người trong độ tuổi lao động (15 - 64 tuổi) lớn gấp đôi người phụ thuộc (dưới 15 và trên 65 tuổi). Già hóa dân số: tỉ lệ người trên 65 tuổi vượt quá 10%.",
                    "example": "Việt Nam đang trong thời kì dân số vàng với nguồn lao động trẻ dồi dào nhưng bắt đầu bước vào giai đoạn già hóa dân số.",
                    "essence": "Tác động sâu sắc đến chiến lược phát triển kinh tế, hệ thống an sinh xã hội và thị trường lao động."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Một quốc gia có dân số 100 triệu người, năm 2026 có tỉ suất sinh thô là 15‰ và tỉ suất tử thô là 7‰. Tính số người tăng thêm do gia tăng tự nhiên trong năm đó.",
                    "steps": [
                        "Bước 1: Tỉ suất gia tăng dân số tự nhiên: Tg = S - T = 15‰ - 7‰ = 8‰ = 0.8%.",
                        "Bước 2: Số người tăng thêm: ΔN = 100.000.000 · 0.8% = 100.000.000 · 0.008 = 800.000 người."
                    ],
                    "answer": "Dân số tăng thêm 800.000 người."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Lấy đơn vị phần trăm (%) thay vì phần nghìn (‰) khi đọc chỉ số tỉ suất sinh thô và tử thô.",
                    "why": "Tỉ suất sinh và tử thô tính trên 1.000 dân (kí hiệu ‰); khi tính tỉ suất gia tăng tự nhiên mới chia cho 10 để đổi ra %."
                }
            ]
        },
        {
            "id": "ch09",
            "title": "Chương 9: Các ngành kinh tế",
            "description": "Địa lí nông nghiệp, lâm nghiệp, thủy sản; địa lí công nghiệp; địa lí dịch vụ, giao thông vận tải, thương mại và du lịch.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Địa lí ngành nông nghiệp, lâm nghiệp và thủy sản", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Địa lí ngành công nghiệp", "hasRealContent": True},
                {"id": "l03", "title": "Bài 3: Địa lí ngành dịch vụ, giao thông và thương mại", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Các nhân tố ảnh hưởng đến sự phát triển và phân bố công nghiệp",
                    "definition": "Nhân tố tự nhiên (vị trí địa lí, khoáng sản, nước, đất) tạo tiền đề tài nguyên. Nhân tố kinh tế - xã hội (dân cư - lao động, thị trường, cơ sở hạ tầng, khoa học công nghệ, chính sách) đóng vai trò quyết định.",
                    "example": "Nhật Bản tuy nghèo tài nguyên khoáng sản nhưng nhờ lao động kỹ thuật cao, vốn và công nghệ hiện đại đã trở thành cường quốc công nghiệp hàng đầu thế giới.",
                    "essence": "Trong thời đại 4.0, nhân tố công nghệ và nguồn nhân lực chất lượng cao đóng vai trò chi phối sự phân bố sản xuất."
                }
            ],
            "rules": [
                {
                    "statement": "Chuyển dịch cơ cấu ngành kinh tế trong thời đại mới",
                    "meaning": "Giảm tỉ trọng khu vực I (nông - lâm - ngư nghiệp), tăng nhanh tỉ trọng khu vực II (công nghiệp - xây dựng) và khu vực III (dịch vụ tri thức số).",
                    "example": "Ở các nước phát triển, khu vực dịch vụ chiếm trên 70% GDP.",
                    "essence": "Phản ánh quá trình nâng cao năng suất xã hội và phát triển kinh tế bền vững."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Tại sao ngành công nghiệp chế biến lương thực thực phẩm thường được phân bố gần vùng nguyên liệu hoặc thị trường tiêu thụ?",
                    "steps": [
                        "Bước 1: Nông sản tươi sống (rau, sữa, củ quả tươi) có đặc tính dễ hư hỏng, cồng kềnh, chi phí bảo quản vận chuyển cao.",
                        "Bước 2: Phân bố gần nguồn nguyên liệu giúp giảm chi phí vận chuyển và bảo toàn độ tươi ngon của sản phẩm.",
                        "Bước 3: Phân bố gần thị trường đô thị đông dân giúp tiêu thụ sản phẩm nhanh chóng, đáp ứng nhu cầu ẩm thực thường nhật."
                    ],
                    "answer": "Nhằm tiết kiệm tối đa chi phí vận tải và bảo đảm độ tươi mới chất lượng sản phẩm."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Đánh giá tài nguyên thiên nhiên là nhân tố duy nhất quyết định sự giàu có của một ngành kinh tế.",
                    "why": "Khoa học công nghệ, chính sách và nguồn nhân lực mới là nhân tố quyết định giá trị gia tăng của sản phẩm."
                }
            ]
        },
        {
            "id": "ch10",
            "title": "Chương 10: Phát triển bền vững và Tăng trưởng xanh",
            "description": "Tác động của con người đến môi trường, ô nhiễm tài nguyên, biến đổi khí hậu toàn cầu và chiến lược tăng trưởng xanh.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Môi trường và tài nguyên thiên nhiên", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Phát triển bền vững và tăng trưởng xanh", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Phát triển bền vững (Sustainable Development)",
                    "definition": "Là sự phát triển đáp ứng được các nhu cầu của thế hệ hiện tại mà không làm tổn hại đến khả năng đáp ứng nhu cầu đó của các thế hệ tương lai trên 3 trụ cột: Kinh tế, Xã hội và Môi trường.",
                    "example": "Phát triển năng lượng tái tạo (điện gió, điện mặt trời) thay thế nhiệt điện than phát thải khí nhà kính.",
                    "essence": "Hài hòa giữa tăng trưởng kinh tế, công bằng xã hội và bảo vệ sự trong lành của môi trường sống."
                },
                {
                    "term": "Kinh tế tuần hoàn (Circular Economy)",
                    "definition": "Mô hình kinh tế nhằm loại bỏ rác thải và sử dụng tài nguyên liên tục thông qua tái sử dụng, sửa chữa, tái chế và tái sản xuất.",
                    "example": "Sản phẩm điện tử sau khi hỏng được thu gom để trích xuất các kim loại quý (vàng, đồng) làm linh kiện mới.",
                    "essence": "Biến rác thải của ngành này thành nguyên liệu đầu vào của ngành khác, tạo vòng khép kín không phát thải."
                }
            ],
            "rules": [
                {
                    "statement": "Mục tiêu phát thải ròng bằng '0' (Net Zero 2050)",
                    "meaning": "Cân bằng giữa lượng khí thải nhà kính thải ra và lượng khí được hấp thụ hoặc loại bỏ khỏi khí quyển vào năm 2050.",
                    "example": "Cam kết của Việt Nam tại Hội nghị biến đổi khí hậu COP26.",
                    "essence": "Hành động sống còn của toàn nhân loại nhằm khống chế nhiệt độ Trái Đất không tăng quá 1.5°C."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Học sinh THPT có thể thực hiện những hành động thiết thực nào để đóng góp vào mục tiêu Tăng trưởng xanh?",
                    "steps": [
                        "Bước 1: Thực hành lối sống xanh: tắt thiết bị điện khi không dùng, sử dụng phương tiện xe đạp hoặc xe buýt công cộng.",
                        "Bước 2: Giảm thiểu rác thải nhựa: mang bình nước cá nhân, túi vải khi đi chợ, phân loại rác tại nguồn.",
                        "Bước 3: Tích cực tham gia các phong trào trồng cây xanh và tuyên truyền ý thức bảo vệ môi trường trong trường học."
                    ],
                    "answer": "Tiết kiệm năng lượng, phân loại rác thải, giảm đồ nhựa dùng một lần và lan tỏa lối sống xanh."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Cho rằng bảo vệ môi trường sẽ kìm hãm sự phát triển kinh tế.",
                    "why": "Tăng trưởng xanh mở ra các ngành kinh tế mới đầy tiềm năng (năng lượng tái tạo, công nghệ sạch, du lịch sinh thái) tạo ra việc làm bền vững."
                }
            ]
        }
    ]
}

# Add gdkt-pl (9 units)
HUMANITIES_DATA["gdkt-pl"] = {
    "id": "gdkt-pl",
    "name": "GDKT & Pháp luật",
    "icon": "⚖️",
    "chapters": [
        {
            "id": "ch01",
            "title": "Chủ đề 1: Nền kinh tế và các chủ thể của nền kinh tế",
            "description": "Các hoạt động kinh tế cơ bản (sản xuất, phân phối - trao đổi, tiêu dùng) và vai trò của các chủ thể kinh tế trong xã hội.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Các hoạt động kinh tế cơ bản", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Các chủ thể của nền kinh tế", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Các chủ thể của nền kinh tế",
                    "definition": "Bao gồm: Chủ thể sản xuất (doanh nghiệp, hộ sản xuất tạo ra hàng hóa), Chủ thể tiêu dùng (người mua sử dụng hàng hóa), Chủ thể trung gian (thương nhân, siêu thị, sàn thương mại kết nối) và Chủ thể Nhà nước (quản lý, điều tiết vĩ mô).",
                    "example": "Bác nông dân trồng lúa là chủ thể sản xuất; siêu thị là chủ thể trung gian; người mua gạo về ăn là chủ thể tiêu dùng; Nhà nước quy định thuế và bình ổn giá gạo.",
                    "essence": "Mối quan hệ tương tác tuần hoàn điều hòa dòng chảy hàng hóa và tiền tệ trong nền kinh tế thị trường."
                }
            ],
            "rules": [
                {
                    "statement": "Vai trò của Nhà nước trong kinh tế thị trường",
                    "meaning": "Tạo lập môi trường pháp lí công bằng, xây dựng cơ sở hạ tầng, điều tiết nền kinh tế thông qua chính sách tài khóa và tiền tệ, khắc phục các thất bại của thị trường (ô nhiễm, độc quyền, đói nghèo).",
                    "example": "Nhà nước ban hành Luật Cạnh tranh để chống các hành vi độc quyền thao túng giá cả.",
                    "essence": "Nhà nước là bàn tay hữu hình định hướng nền kinh tế thị trường theo định hướng xã hội chủ nghĩa."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Học sinh đóng vai trò là chủ thể nào trong nền kinh tế khi mua sách vở tại cửa hàng văn phòng phẩm?",
                    "steps": [
                        "Bước 1: Học sinh dùng tiền mua dụng cụ học tập để phục vụ nhu cầu cá nhân.",
                        "Bước 2: Cửa hàng văn phòng phẩm là chủ thể trung gian bán lẻ.",
                        "Bước 3: Kết luận: Học sinh là chủ thể tiêu dùng."
                    ],
                    "answer": "Học sinh là chủ thể tiêu dùng."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng chủ thể sản xuất chỉ là các công ty xí nghiệp lớn.",
                    "why": "Mọi cá nhân, hộ gia đình sản xuất nông sản, làm đồ thủ công hay cung ứng dịch vụ nhỏ lẻ đều là chủ thể sản xuất."
                }
            ]
        },
        {
            "id": "ch02",
            "title": "Chủ đề 2: Thị trường và Cơ chế thị trường",
            "description": "Khái niệm thị trường, các chức năng của thị trường, quy luật giá trị, quy luật cung cầu và cạnh tranh trong nền kinh tế thị trường.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khái niệm và chức năng của thị trường", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Cơ chế thị trường, quy luật cung cầu và giá cả", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Cơ chế thị trường và 'Bàn tay vô hình'",
                    "definition": "Là cơ chế tự điều tiết của nền kinh tế thông qua sự tương tác giữa các quy luật kinh tế khách quan (cung cầu, giá cả, cạnh tranh), xác định giá cả và phân bổ nguồn lực sản xuất.",
                    "example": "Khi nhu cầu mua xe máy điện tăng vọt, giá xe tăng lên kích thích các nhà máy mở rộng sản xuất thêm nhiều xe máy điện.",
                    "essence": "Tín hiệu giá cả dẫn dắt người sản xuất biết nên sản xuất cái gì, sản xuất như thế nào và cho ai."
                }
            ],
            "rules": [
                {
                    "statement": "Quy luật Cung - Cầu",
                    "meaning": "Khi Cầu > Cung: Hàng hóa khan hiếm, giá cả tăng, người sản xuất mở rộng sản xuất. Khi Cung > Cầu: Hàng hóa thừa ế, giá cả giảm, người sản xuất thu hẹp sản xuất.",
                    "example": "Vào vụ mùa thu hoạch dưa hấu, cung vượt cầu làm giá dưa giảm mạnh.",
                    "essence": "Cung cầu tác động qua lại xác định giá cả cân bằng thị trường."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Người sản xuất cần vận dụng quy luật cung cầu như thế nào khi thấy giá cả một mặt hàng trên thị trường đang giảm sâu do thừa cung?",
                    "steps": [
                        "Bước 1: Giảm bớt sản lượng mặt hàng đang thừa cung để tránh tồn kho thua lỗ.",
                        "Bước 2: Cải tiến mẫu mã, nâng cao chất lượng hoặc hạ giá thành sản xuất để tăng tính cạnh tranh.",
                        "Bước 3: Chuyển dịch một phần nguồn lực sang sản xuất mặt hàng khác đang có cầu lớn."
                    ],
                    "answer": "Thu hẹp sản lượng, tiết giảm chi phí hoặc chuyển đổi mặt hàng kinh doanh phù hợp nhu cầu thị trường."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Coi cạnh tranh trong kinh tế thị trường luôn là điều tiêu cực, phá hoại.",
                    "why": "Cạnh tranh lành mạnh là động lực thúc đẩy đổi mới công nghệ, nâng cao chất lượng và hạ giá thành phục vụ người tiêu dùng."
                }
            ]
        },
        {
            "id": "ch03",
            "title": "Chủ đề 3: Ngân sách Nhà nước",
            "description": "Khái niệm, đặc điểm, vai trò của Ngân sách nhà nước; các nguồn thu và nhiệm vụ chi ngân sách; quyền và nghĩa vụ của công dân.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khái niệm và vai trò của Ngân sách nhà nước", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Quyền và nghĩa vụ của công dân đối với Ngân sách nhà nước", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Ngân sách nhà nước",
                    "definition": "Toàn bộ các khoản thu, chi của Nhà nước được dự toán và thực hiện trong một khoảng thời gian nhất định (thường là một năm) do Quốc hội quyết định để bảo đảm thực hiện các chức năng, nhiệm vụ của Nhà nước.",
                    "example": "Chi ngân sách xây dựng cầu Mỹ Thuận 2, đường cao tốc Bắc - Nam, chi trả lương cho giáo viên, bác sĩ bệnh viện công và quốc phòng an ninh.",
                    "essence": "Quỹ tiền tệ tập trung lớn nhất của quốc gia phục vụ lợi ích chung của toàn xã hội."
                }
            ],
            "rules": [
                {
                    "statement": "Nguyên tắc quản lý ngân sách nhà nước",
                    "meaning": "Thu chi ngân sách phải được Quốc hội phê chuẩn theo luật, công khai, minh bạch, tiết kiệm và chống lãng phí, tham nhũng.",
                    "example": "Báo cáo quyết toán ngân sách nhà nước hàng năm đều được công bố công khai trên các cổng thông tin chính phủ.",
                    "essence": "Mỗi đồng tiền ngân sách đều bắt nguồn từ đóng góp mồ hôi công sức của nhân dân."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Kể tên 3 nguồn thu chủ yếu và 3 nhiệm vụ chi quan trọng của Ngân sách nhà nước Việt Nam.",
                    "steps": [
                        "Bước 1: Nguồn thu: Thu từ thuế (chiếm tỉ trọng lớn nhất), thu từ phí và lệ phí, thu từ khai thác dầu khí và bán tài sản nhà nước.",
                        "Bước 2: Nhiệm vụ chi: Chi đầu tư phát triển (xây dựng giao thông, trường học, bệnh viện), chi thường xuyên (giáo dục, y tế, quốc phòng, bộ máy nhà nước), chi an sinh xã hội (trợ cấp người nghèo, bảo hiểm xã hội)."
                    ],
                    "answer": "Thu chủ yếu từ thuế, phí; Chi cho đầu tư phát triển hạ tầng, chi thường xuyên giáo dục y tế và an sinh xã hội."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Cho rằng Ngân sách nhà nước chỉ bao gồm tiền của các bộ ngành trung ương.",
                    "why": "Ngân sách nhà nước gồm ngân sách trung ương và ngân sách của chính quyền các địa phương (tỉnh, huyện, xã)."
                }
            ]
        },
        {
            "id": "ch04",
            "title": "Chủ đề 4: Thuế và Chính sách thuế",
            "description": "Khái niệm, vai trò của thuế, các loại thuế trực thu và gián thu (VAT, thu nhập cá nhân, doanh nghiệp, xuất nhập khẩu), quyền và nghĩa vụ nộp thuế.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khái niệm và các loại thuế cơ bản", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Quyền và nghĩa vụ nộp thuế của công dân", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Thuế",
                    "definition": "Là một khoản nộp bắt buộc mà các thể nhân và pháp nhân có nghĩa vụ phải nộp cho Nhà nước theo luật định, không mang tính hoàn trả trực tiếp.",
                    "example": "Khi mua một chiếc cặp sách giá 220.000đ đã bao gồm 20.000đ tiền thuế giá trị gia tăng (VAT 10%).",
                    "essence": "Thuế là nguồn thu chủ yếu nuôi sống bộ máy nhà nước và cung cấp các dịch vụ công cộng cho toàn xã hội."
                },
                {
                    "term": "Thuế trực thu và Thuế gián thu",
                    "definition": "Thuế trực thu đánh trực tiếp vào thu nhập hoặc tài sản của người nộp thuế (thuế thu nhập cá nhân, thuế thu nhập doanh nghiệp). Thuế gián thu cấu thành vào giá bán hàng hóa do người tiêu dùng cuối cùng gánh chịu (VAT, thuế tiêu thụ đặc biệt, thuế xuất nhập khẩu).",
                    "example": "Thuế tiêu thụ đặc biệt đánh vào thuốc lá, rượu bia, xe hơi sang trọng để điều tiết tiêu dùng.",
                    "essence": "Phân chia phương thức điều tiết kinh tế và thực hiện công bằng xã hội (người thu nhập cao đóng thuế nhiều hơn)."
                }
            ],
            "rules": [
                {
                    "statement": "Nghĩa vụ nộp thuế của công dân",
                    "meaning": "Nộp thuế là nghĩa vụ và quyền lợi thiêng liêng của mọi công dân và doanh nghiệp theo quy định của Hiến pháp và Luật Quản lý thuế; trốn thuế là hành vi vi phạm pháp luật hình sự.",
                    "example": "Doanh nghiệp gian lận kê khai giảm doanh thu để giảm thuế có thể bị phạt tiền gấp nhiều lần hoặc truy cứu trách nhiệm hình sự.",
                    "essence": "Nộp thuế là thể hiện lòng yêu nước và trách nhiệm xây dựng đất nước phồn vinh."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Tại sao Nhà nước đánh thuế tiêu thụ đặc biệt rất cao đối với rượu, bia và thuốc lá?",
                    "steps": [
                        "Bước 1: Rượu bia và thuốc lá là các mặt hàng gây hại cho sức khỏe con người và trật tự an toàn xã hội.",
                        "Bước 2: Đánh thuế cao làm giá bán tăng vọt, từ đó hạn chế bớt nhu cầu tiêu dùng của người dân.",
                        "Bước 3: Tăng nguồn thu cho ngân sách để tái đầu tư vào hệ thống chăm sóc sức khỏe y tế cộng đồng."
                    ],
                    "answer": "Để điều tiết hạn chế tiêu dùng các sản phẩm có hại và tăng thu ngân sách cho y tế."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng học sinh chưa đi làm thì chưa bao giờ phải đóng bất kỳ khoản thuế nào.",
                    "why": "Khi học sinh mua đồ ăn, quần áo, vé xem phim, mua sách vở thì đã gián tiếp nộp thuế giá trị gia tăng (VAT) được cộng sẵn trong hóa đơn thanh toán."
                }
            ]
        },
        {
            "id": "ch05",
            "title": "Chủ đề 5: Sản xuất kinh doanh và các mô hình kinh doanh",
            "description": "Các mô hình sản xuất kinh doanh: Hộ kinh doanh cá thể, Doanh nghiệp tư nhân, Công ty TNHH, Công ty Cổ phần, Hợp tác xã.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Sản xuất kinh doanh và các mô hình tổ chức", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Lập kế hoạch kinh doanh và khởi nghiệp", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Công ty Cổ phần và Công ty TNHH",
                    "definition": "Công ty Cổ phần có vốn điều lệ chia thành các phần bằng nhau gọi là cổ phần, có quyền phát hành cổ phiếu ra công chúng trên sàn chứng khoán. Công ty TNHH có từ 1 đến 50 thành viên, chịu trách nhiệm hữu hạn trong phạm vi số vốn góp.",
                    "example": "Tập đoàn Vinamilk, FPT là công ty cổ phần niêm yết trên sàn chứng khoán HOSE.",
                    "essence": "Chế độ trách nhiệm hữu hạn bảo vệ tài sản cá nhân của chủ sở hữu tách biệt khỏi các khoản nợ của công ty."
                }
            ],
            "rules": [
                {
                    "statement": "Đạo đức kinh doanh và trách nhiệm xã hội",
                    "meaning": "Kinh doanh không chỉ vì lợi nhuận thuần túy mà phải tuân thủ pháp luật, bảo đảm quyền lợi người tiêu dùng, bảo vệ môi trường và đóng góp cho cộng đồng.",
                    "example": "Không buôn bán hàng giả, thực phẩm bẩn tẩm hóa chất độc hại, không xả thải trộm ra sông hồ.",
                    "essence": "Uy tín và đạo đức là tài sản vô giá bảo đảm sự phát triển bền vững lâu dài của doanh nghiệp."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "So sánh trách nhiệm tài sản giữa chủ Doanh nghiệp tư nhân và cổ đông của Công ty Cổ phần khi doanh nghiệp bị phá sản vỡ nợ.",
                    "steps": [
                        "Bước 1: Chủ doanh nghiệp tư nhân chịu trách nhiệm vô hạn: phải dùng toàn bộ tài sản cá nhân để trả hết các khoản nợ của doanh nghiệp.",
                        "Bước 2: Cổ đông công ty cổ phần chịu trách nhiệm hữu hạn: chỉ chịu rủi ro mất đi số tiền tương ứng với số cổ phần mình đã mua, tài sản cá nhân riêng không bị tịch thu để trả nợ cho công ty."
                    ],
                    "answer": "Doanh nghiệp tư nhân chịu trách nhiệm vô hạn; Công ty cổ phần chịu trách nhiệm hữu hạn."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng Hộ kinh doanh cá thể có tư cách pháp nhân giống như Công ty TNHH.",
                    "why": "Hộ kinh doanh không có tư cách pháp nhân và chủ hộ phải chịu trách nhiệm vô hạn bằng toàn bộ tài sản của mình."
                }
            ]
        },
        {
            "id": "ch06",
            "title": "Chủ đề 6: Tín dụng và các dịch vụ tín dụng",
            "description": "Bản chất của tín dụng, tín dụng ngân hàng, tín dụng thương mại, tín dụng tiêu dùng và cách sử dụng dịch vụ tín dụng an toàn, tránh bẫy 'tín dụng đen'.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khái niệm và các hình thức tín dụng", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Sử dụng dịch vụ tín dụng an toàn và phòng ngừa tín dụng đen", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Tín dụng",
                    "definition": "Là quan hệ vay mượn tài sản (thường là tiền) dựa trên sự tin tưởng giữa người cho vay và người đi vay, kèm cam kết hoàn trả cả vốn lẫn lãi sau một thời hạn nhất định.",
                    "example": "Vay vốn ngân hàng 500 triệu đồng để mở rộng trang trại chăn nuôi trong thời hạn 3 năm với lãi suất 8%/năm.",
                    "essence": "Chuyển giao nguồn vốn nhàn rỗi trong xã hội sang những nơi cần vốn để đầu tư sinh lời."
                },
                {
                    "term": "Bẫy 'Tín dụng đen'",
                    "definition": "Hình thức cho vay nặng lãi phi pháp không qua hệ thống ngân hàng, thủ tục vay dễ dãi nhưng lãi suất 'cắt cổ' (hàng trăm %/năm) kèm các hành vi đòi nợ khủng bố, đe dọa vũ lực.",
                    "example": "Các app cho vay online bất hợp pháp đòi nợ bằng cách gọi điện đe dọa người thân bạn bè và ghép ảnh vu khống.",
                    "essence": "Cạm bẫy tài chính phi pháp tàn phá tài chính và tính mạng của người đi vay và gia đình."
                }
            ],
            "rules": [
                {
                    "statement": "Nguyên tắc vay tín dụng có trách nhiệm",
                    "meaning": "Chỉ vay khi thực sự cần thiết và có phương án trả nợ khả thi; đọc kĩ hợp đồng về lãi suất, phí phạt trả chậm; chỉ vay tại các tổ chức tín dụng được Ngân hàng Nhà nước cấp phép.",
                    "example": "Khoản trả nợ hàng tháng không nên vượt quá 30 - 40% tổng thu nhập hàng tháng của cá nhân.",
                    "essence": "Bảo vệ điểm tín dụng cá nhân và an toàn tài chính gia đình."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Học sinh cần làm gì khi nhận được các tin nhắn quảng cáo 'cho vay tiền nóng, giải ngân trong 5 phút không cần thế chấp'?",
                    "steps": [
                        "Bước 1: Tuyệt đối không bấm vào các đường link lạ, không tải app không rõ nguồn gốc.",
                        "Bước 2: Không cung cấp thông tin cá nhân (ảnh CCCD, số điện thoại người thân, danh bạ).",
                        "Bước 3: Chặn số và cảnh báo cho bạn bè, người thân về các cạm bẫy lừa đảo tín dụng đen."
                    ],
                    "answer": "Không bấm link, không cung cấp thông tin và cảnh giác phòng ngừa tín dụng đen."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Nghĩ rằng thẻ tín dụng (Credit Card) là thẻ chứa sẵn tiền tiết kiệm của mình.",
                    "why": "Thẻ tín dụng là tiền ngân hàng cho bạn VAY TRƯỚC để tiêu, nếu không trả hết nợ đúng hạn (thường 45 ngày) sẽ bị tính lãi suất phạt rất cao."
                }
            ]
        },
        {
            "id": "ch07",
            "title": "Chủ đề 7: Lập kế hoạch tài chính cá nhân",
            "description": "Các nguồn thu nhập cá nhân, quy tắc quản lý chi tiêu (quy tắc 50/30/20, 6 chiếc lọ), tiết kiệm và đầu tư thông minh cho tương lai.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Kế hoạch tài chính cá nhân và các mục tiêu tài chính", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Thực hành lập kế hoạch tài chính cá nhân", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Quy tắc quản lý tài chính 50/30/20",
                    "definition": "Phân bổ thu nhập thành 3 phần: 50% cho nhu cầu thiết yếu (ăn uống, học phí, tiền nhà), 30% cho mong muốn cá nhân (mua sắm, giải trí), 20% cho tiết kiệm và đầu tư dự phòng.",
                    "example": "Nếu thu nhập là 10 triệu đồng: 5 triệu cho ăn ở đi lại, 3 triệu cho giải trí bạn bè, 2 triệu gửi tiết kiệm tích lũy.",
                    "essence": "Kiểm soát chi tiêu giúp con người làm chủ đồng tiền, tránh rơi vào cảnh nợ nần và tự do tài chính."
                }
            ],
            "rules": [
                {
                    "statement": "Nguyên tắc 'Trả cho bản thân mình trước'",
                    "meaning": "Ngay khi nhận được thu nhập, hãy trích ngay một khoản tiết kiệm (10 - 20%) cất đi trước, số còn lại mới dùng để chi tiêu, thay vì chi tiêu xong thừa bao nhiêu mới tiết kiệm.",
                    "example": "Nhận tiền tiêu vặt hoặc tiền lì xì, cất ngay 20% vào tài khoản tích lũy rồi mới chi tiêu khoản còn lại.",
                    "essence": "Kỷ luật tài chính cá nhân tạo nên sự thịnh vượng lâu dài."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Bạn An có 500.000 đồng tiền tiêu vặt mỗi tháng. Hãy giúp An lập kế hoạch chi tiêu theo quy tắc 50/30/20.",
                    "steps": [
                        "Bước 1: Nhu cầu thiết yếu (50%): 500.000 · 50% = 250.000đ (tiền xăng xe, bút vở, ăn sáng phụ).",
                        "Bước 2: Mong muốn cá nhân (30%): 500.000 · 30% = 150.000đ (đi uống trà sữa, mua sách truyện yêu thích).",
                        "Bước 3: Tiết kiệm dự phòng (20%): 500.000 · 20% = 100.000đ (bỏ lợn tiết kiệm mua quà sinh nhật tặng mẹ)."
                    ],
                    "answer": "250.000đ cho nhu cầu thiết yếu, 150.000đ cho mong muốn và 100.000đ cho tiết kiệm."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Không phân biệt được giữa 'nhu cầu thiết yếu' (CẦN - Needs) và 'mong muốn nhất thời' (MUỐN - Wants).",
                    "why": "Mua một chiếc điện thoại mới chỉ vì bạn bè có trong khi máy cũ vẫn dùng tốt là MUỐN chứ không phải CẦN thiết yếu."
                }
            ]
        },
        {
            "id": "ch08",
            "title": "Chủ đề 8: Hệ thống chính trị và Hiến pháp nước CHXHCN Việt Nam",
            "description": "Cơ cấu hệ thống chính trị (Đảng, Nhà nước, Mặt trận Tổ quốc), vị trí tối cao của Hiến pháp 2013 và quyền, nghĩa vụ cơ bản của công dân.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Hệ thống chính trị nước Cộng hòa Xã hội Chủ nghĩa Việt Nam", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Hiến pháp nước CHXHCN Việt Nam và bộ máy nhà nước", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Hiến pháp",
                    "definition": "Là đạo luật cơ bản của Nhà nước, có hiệu lực pháp lí cao nhất trong hệ thống pháp luật Việt Nam. Mọi văn bản pháp luật khác (Luật, Nghị định, Thông tư) đều không được trái với Hiến pháp.",
                    "example": "Hiến pháp năm 2013 khẳng định: 'Nhà nước Cộng hòa xã hội chủ nghĩa Việt Nam là nhà nước pháp quyền xã hội chủ nghĩa của Nhân dân, do Nhân dân, vì Nhân dân'.",
                    "essence": "Hiến pháp là văn kiện chính trị - pháp lý tối cao thể hiện chủ quyền tối cao của Nhân dân."
                },
                {
                    "term": "Bộ máy Nhà nước Việt Nam",
                    "definition": "Bao gồm: Quốc hội (cơ quan đại biểu cao nhất của Nhân dân, cơ quan quyền lực nhà nước cao nhất, lập pháp); Chính phủ (cơ quan hành chính nhà nước cao nhất, hành pháp); Tòa án nhân dân và Viện kiểm sát nhân dân (cơ quan tư pháp).",
                    "example": "Quốc hội làm luật và sửa đổi luật; Chính phủ thi hành luật; Tòa án xét xử các vụ án vi phạm pháp luật.",
                    "essence": "Quyền lực nhà nước là thống nhất, có sự phân công, phối hợp và kiểm soát giữa các cơ quan lập pháp, hành pháp và tư pháp."
                }
            ],
            "rules": [
                {
                    "statement": "Quyền và nghĩa vụ cơ bản của công dân trong Hiến pháp",
                    "meaning": "Quyền không tách rời nghĩa vụ: Công dân có quyền học tập, quyền tự do ngôn luận, quyền bầu cử ứng cử... đi liền với nghĩa vụ bảo vệ Tổ quốc, nghĩa vụ tuân theo Hiến pháp và pháp luật, nghĩa vụ nộp thuế.",
                    "example": "Học sinh được hưởng quyền học tập miễn phí hoặc hỗ trợ học phí, đồng thời có nghĩa vụ học tập tốt và giữ gìn kỉ luật học đường.",
                    "essence": "Tự do trong khuôn khổ pháp luật vì sự an toàn và hạnh phúc chung của cả cộng đồng."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Cơ quan nào có thẩm quyền ban hành Hiến pháp và sửa đổi Hiến pháp nước Cộng hòa Xã hội Chủ nghĩa Việt Nam?",
                    "steps": [
                        "Bước 1: Theo Điều 69 Hiến pháp 2013: Quốc hội là cơ quan đại biểu cao nhất của Nhân dân, cơ quan quyền lực nhà nước cao nhất.",
                        "Bước 2: Chỉ duy nhất Quốc hội mới có quyền lập hiến và lập pháp (làm Hiến pháp, sửa đổi Hiến pháp, làm Luật, sửa đổi Luật)."
                    ],
                    "answer": "Quốc hội nước CHXHCN Việt Nam."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Cho rằng Chính phủ có quyền ban hành hoặc sửa đổi các điều khoản trong Hiến pháp.",
                    "why": "Chính phủ là cơ quan hành pháp (thi hành Hiến pháp và Luật), chỉ có Quốc hội mới có quyền lập hiến và lập pháp."
                }
            ]
        },
        {
            "id": "ch09",
            "title": "Chủ đề 9: Pháp luật và đời sống",
            "description": "Khái niệm, bản chất, vai trò của pháp luật trong quản lí nhà nước và đời sống xã hội; các hình thức thực hiện pháp luật và trách nhiệm pháp lí.",
            "lessons": [
                {"id": "l01", "title": "Bài 1: Khái niệm, bản chất và vai trò của pháp luật", "hasRealContent": True},
                {"id": "l02", "title": "Bài 2: Thực hiện pháp luật và các hình thức xử lí vi phạm", "hasRealContent": True}
            ],
            "concepts": [
                {
                    "term": "Pháp luật",
                    "definition": "Là hệ thống các quy tắc xử sự chung do Nhà nước ban hành hoặc thừa nhận và bảo đảm thực hiện bằng quyền lực nhà nước, nhằm điều chỉnh các quan hệ xã hội vì lợi ích của Nhà nước và toàn xã hội.",
                    "example": "Luật Giao thông đường bộ quy định người ngồi trên xe mô tô, xe gắn máy phải đội mũ bảo hiểm đạt chuẩn.",
                    "essence": "Tính quy phạm phổ biến, tính quyền lực bắt buộc chung và tính xác định chặt chẽ về mặt hình thức."
                },
                {
                    "term": "Bốn hình thức thực hiện pháp luật",
                    "definition": "1. Sử dụng pháp luật (làm những gì luật cho phép làm, quyền). 2. Thi hành pháp luật (chủ động làm những gì luật quy định phải làm). 3. Tuân thủ pháp luật (kiềm chế không làm những gì luật cấm). 4. Áp dụng pháp luật (do cơ quan nhà nước có thẩm quyền thực hiện).",
                    "example": "Học sinh đủ 16 tuổi thi lấy giấy phép lái xe (Sử dụng); đội mũ bảo hiểm khi đi xe máy (Thi hành); không vượt đèn đỏ (Tuân thủ); cảnh sát giao thông ra quyết định xử phạt vi phạm (Áp dụng).",
                    "essence": "Pháp luật đi vào đời sống thực tế thông qua hành vi ứng xử cụ thể của các chủ thể."
                }
            ],
            "rules": [
                {
                    "statement": "Các loại vi phạm pháp luật và trách nhiệm pháp lí tương ứng",
                    "meaning": "Vi phạm hình sự (tội phạm) -> Chịu trách nhiệm hình sự (tù giam, cải tạo). Vi phạm hành chính -> Xử phạt hành chính (phạt tiền, tịch thu bằng lái). Vi phạm dân sự -> Bồi thường thiệt hại tài sản. Vi phạm kỉ luật -> Kỉ luật cơ quan/nhà trường (khiển trách, đuổi học, sa thải).",
                    "example": "Học sinh đánh nhau gây thương tích có thể bị kỉ luật đình chỉ học tập và bị xử phạt hành chính hoặc truy cứu trách nhiệm hình sự nếu gây thương tích nặng.",
                    "essence": "Mọi hành vi vi phạm pháp luật đều phải gánh chịu hậu quả pháp lí tương xứng để răn đe và giáo dục."
                }
            ],
            "workedExamples": [
                {
                    "prompt": "Hành vi người tham gia giao thông vượt đèn đỏ thuộc hình thức không thực hiện đúng hình thức pháp luật nào? Vi phạm loại pháp luật nào?",
                    "steps": [
                        "Bước 1: Luật quy định cấm vượt đèn đỏ. Người đó đã làm điều luật cấm => Không tuân thủ pháp luật.",
                        "Bước 2: Hành vi này xâm hại trật tự an toàn giao thông đường bộ nhưng chưa gây hậu quả chết người => Vi phạm hành chính.",
                        "Bước 3: Hậu quả pháp lí: Bị cảnh sát giao thông ra quyết định xử phạt vi phạm hành chính (phạt tiền)."
                    ],
                    "answer": "Không tuân thủ pháp luật và là vi phạm hành chính."
                }
            ],
            "commonMistakes": [
                {
                    "mistake": "Đồng nhất 'Thi hành pháp luật' và 'Tuân thủ pháp luật'.",
                    "why": "'Thi hành' là chủ động LÀM việc luật bắt buộc (như nộp thuế, đội mũ bảo hiểm); 'Tuân thủ' là kiềm chế KHÔNG LÀM điều luật cấm (không trộm cắp, không vượt đèn đỏ)."
                }
            ]
        }
    ]
}

out_file = Path("pipeline/data_g10_humanities.py")
content = '''# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn hóa 5 môn Xã hội / Nhân văn Lớp 10 SGK Kết nối tri thức 2026-2027:
- Ngữ Văn (9 bài)
- Tiếng Anh (10 units)
- Lịch sử (6 chương)
- Địa lí (10 chương)
- GDKT & Pháp luật (9 chủ đề)
"""

true = True
false = False
null = None

HUMANITIES_SUBJECTS = ''' + json.dumps(HUMANITIES_DATA, ensure_ascii=False, indent=2) + "\n"

with open(out_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated {out_file} with {len(HUMANITIES_DATA)} subjects!")

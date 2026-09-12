# 📚 Ôn Luyện SGK 2026 – 2027 & Gia sư Trí tuệ Nhân tạo DeepTutor

> **Nền tảng tự học & ôn luyện kiến thức bám sát chương trình Giáo dục Phổ thông mới (SGK 2026 – 2027) của Bộ GD&ĐT.**  
> Phát triển bởi **N&Mstudio_Education**  
> 🌐 Website: [https://www.nmstudio.id.vn/](https://www.nmstudio.id.vn/) | 📞 Hotline / Zalo: [+84 985578385](tel:+84985578385)

---

## 🌟 Điểm nổi bật của nền tảng

1. **Bám sát SGK Bộ GD&ĐT 2026 – 2027**:
   - Hệ thống bài giảng và câu hỏi được chuẩn hóa bám sát các bộ sách Kết nối tri thức, Cánh diều, Chân trời sáng tạo.
   - Hoàn thiện 100% dữ liệu đề thi cho các môn Toán, Ngữ Văn, KHTN, Vật lí, Hóa học, Sinh học, Lịch sử - Địa lí, Tiếng Anh, Tin học, GDCD (Lớp 6 & Lớp 11).

2. **Gia sư Socratic DeepTutor AI**:
   - **Sổ tay câu sai (Mistake Bank)**: Tự động phát hiện và gom nhóm các câu hỏi học sinh làm sai để luyện tập phục hồi chuyên sâu.
   - **Chẩn đoán lỗ hổng (Knowledge Gaps)**: Phân tích chuyên sâu 3 bước sư phạm (Bản chất khái niệm – Bẫy sai thường gặp – Lời khuyên gia sư).
   - **Đánh giá cấp độ tinh thông (Mastery Level L1 - L4)**.

3. **Luyện đề phân hóa 3 cấp độ**:
   - **Đề 1**: Nhận biết & Thông hiểu (Xây nền tảng).
   - **Đề 2**: Vận dụng & Bẫy sai (Tránh mất điểm).
   - **Đề 3**: Đề thi tổng hợp (Chinh phục điểm 9 - 10).

4. **Thẻ ghi nhớ Flashcard 3D & Spaced Repetition**:
   - Tích hợp thuật toán lặp lại ngắt quãng SuperMemo SM-2 giúp học sinh ghi nhớ lâu dài kiến thức và công thức.

5. **Khu vực Phụ huynh & Tiến độ học tập**:
   - Bảng điều khiển phụ huynh bảo mật bằng mã PIN.
   - Thống kê thời lượng học tập, chuỗi ngày học liên tục (Streak), điểm thưởng XP và biểu đồ môn mạnh / yếu.
   - Hỗ trợ sao lưu Export & Import JSON dữ liệu học tập cá nhân.

6. **PWA (Progressive Web App)**:
   - Cài đặt trực tiếp như một ứng dụng Native trên iOS, Android, Tablet và Desktop mà không cần thông qua Store.
   - Tải tức thì trong 0.2 giây, hoạt động mượt mà không độ trễ.

---

## 🚀 Cấu trúc thư mục

`	ext
├── app/                  # Toàn bộ mã nguồn Web App (PWA)
│   ├── assets/           # Tài nguyên hình ảnh, 3D Icon, Mascot, Logo
│   ├── css/              # Bảng phong cách CSS giao diện chuẩn EdTech
│   ├── js/               # Động cơ Quiz, DeepTutor, Flashcard, Tiến độ
│   ├── content/          # Ngân hàng đề thi, bài học, thẻ ghi nhớ JSON
│   ├── index.html        # Trang chủ điều hướng 3 cấp học
│   ├── subject.html      # Danh mục chương & đề thi theo môn
│   ├── quiz.html         # Động cơ làm bài thi trắc nghiệm phân hóa
│   ├── lesson.html       # Trình đọc bài giảng lý thuyết chuẩn SGK
│   ├── flashcard.html    # Thẻ ghi nhớ thông minh 3D
│   ├── progress.html     # Bảng theo dõi tiến độ & thành tích
│   ├── parent.html       # Bảng điều khiển phụ huynh (PIN bảo mật)
│   └── manifest.json     # Cấu hình PWA
├── pipeline/             # Pipeline OCR & số hóa AI tự động
│   ├── batch_all_grades_ocr.py  # Script quét số hóa tự động qua Qwen2.5-VL
│   └── ocr_status.json          # Checkpoint tiến độ số hóa SGK
└── vercel.json           # Cấu hình triển khai Vercel Production
`

---

## 💻 Triển khai cục bộ (Local Development)

`ash
# Chạy HTTP Server nội bộ
python -m http.server 8080

# Truy cập trình duyệt
http://localhost:8080/app/index.html
`

---

## 📜 Bản quyền

© 2026 by **NMstudio**. Phát triển bởi **N&Mstudio_Education**.  
Toàn bộ chương trình bám sát SGK của Bộ Giáo dục và Đào tạo năm học 2026 – 2027.

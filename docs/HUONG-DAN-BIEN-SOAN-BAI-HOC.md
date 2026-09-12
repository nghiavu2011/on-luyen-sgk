# Hướng Dẫn Biên Soạn Bài Học Lý Thuyết SGK (Chuẩn GDPT 2018)

Tài liệu này hướng dẫn giáo viên và đội ngũ nội dung biên soạn các bài học lý thuyết cho Hệ thống Ôn Luyện SGK, đảm bảo tính sư phạm, trực quan và tích hợp mượt mà với hệ thống.

---

## 1. Cấu Trúc Thư Mục & Đặt Tên Tệp

Mỗi bài học là một tệp JSON riêng biệt nằm theo cấu trúc:
```
content/grade-{grade}/{subject}/{chapter}/{lessonId}.json
```
Ví dụ:
- `content/grade-06/toan/ch01/l01.json`: Bài 1, Chương 1, Toán 6
- `content/grade-06/toan/ch01/l02.json`: Bài 2, Chương 1, Toán 6
- `content/grade-11/hoa-hoc/ch01/l01.json`: Bài 1, Chương 1, Hóa học 11

Schema kiểm chuẩn: `content/schema/lesson.schema.json`.

---

## 2. Quy Định Trường Dữ Liệu

Mỗi tệp bài học gồm các trường sau:

| Trường | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `id` | string | Có | Định danh bài, vd: `toan-06-ch01-l01` |
| `title` | string | Có | Tên bài học đầy đủ theo SGK Kết nối tri thức |
| `durationMinutes` | number | Không | Thời lượng học (mặc định 15 phút) |
| `hasRealContent` | boolean | **Có** | `true` nếu đã có nội dung thật, `false` nếu đang soạn |
| `objectives` | array[string] | Có | 2–4 mục tiêu bài học cụ thể, đo lường được |
| `concepts` | array[object] | Có | Khái niệm trọng tâm (`term`, `definition`, `notation`, `note`) |
| `rules` | array[object] | Có | Quy tắc / công thức cốt lõi (`statement`, `meaning`) |
| `workedExamples` | array[object] | Có | 1–3 ví dụ mẫu từng bước (`prompt`, `steps`, `answer`) |
| `commonMistakes` | array[object] | Có | Các bẫy sai học sinh hay mắc (`mistake`, `why`) |
| `practiceRefs` | array[string] | Không | Mã đề luyện tập liên kết |

---

## 3. Quy Ước Viết Công Thức Toán & Ký Hiệu

- Sử dụng cú pháp **LaTeX** chuẩn, bọc trong cặp dấu `$ ... $` (công thức inline) hoặc `$$ ... $$` (công thức display).
- Các ký hiệu phổ biến:
  - Thuộc, không thuộc: `$\in$`, `$\notin$`
  - Tập hợp: `$\{1; 2; 3\}$` (lưu ý escape dấu ngoặc nhọn trong JSON: `\{` và `\}`)
  - Tập số tự nhiên: `$\mathbb{N}$`, `$\mathbb{N}^*$`
  - Phép tính, so sánh: `$\le$`, `$\ge$`, `$\ne$`, `$\times$`, `\cdot`
- Dấu phân cách phần tử số trong tập hợp: **bắt buộc dùng dấu chấm phẩy (`;`)**, không dùng dấu phẩy (`,`).

---

## 4. Quy Trình Xuất Bản Bài Học

1. **Khởi tạo**: Tạo tệp `lXX.json` từ mẫu `content/grade-06/toan/ch01/l01.json`.
2. **Biên soạn**: Điền nội dung chính xác từ SGK. Trong lúc đang viết, giữ `"hasRealContent": false`.
3. **Nghiệm thu**: Khi nội dung hoàn chỉnh và kiểm tra công thức KaTeX hiển thị đúng, đổi cờ `"hasRealContent": true`.
4. **Cập nhật danh mục**: Đồng bộ cờ `hasRealContent: true` trong `chapters.json` của môn học tương ứng.

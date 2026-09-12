# BẢNG KÊ KHAI DỮ LIỆU CÁ NHÂN & LƯU TRỮ (DATA INVENTORY)
*Tuân thủ Nghị định 13/2023/NĐ-CP về Bảo vệ Dữ liệu Cá nhân và Đặc tả P2-5*

---

## 1. Tổng quan Kiến trúc Dữ liệu
- **Vị trí lưu trữ:** 100% Cục bộ trên trình duyệt thiết bị người dùng (`Web Storage / localStorage`).
- **Máy chủ từ xa (Backend/Cloud):** KHÔNG gửi, không lưu trữ bất kỳ thông tin cá nhân hay hành vi làm bài nào của học sinh về máy chủ trong giai đoạn thử nghiệm mở.
- **Thời gian lưu trữ:** Tồn tại cho tới khi học sinh hoặc phụ huynh chủ động bấm nút *"Xóa toàn bộ dữ liệu học tập trên thiết bị này"* hoặc người dùng xóa bộ nhớ duyệt web (Clear Browser Cache/Site Data).

---

## 2. Chi tiết các trường dữ liệu lưu trữ

### Khóa chính: `localStorage["sgk-progress"]` (Schema Phiên bản 2)

| Trường dữ liệu | Kiểu dữ liệu | Mục đích sử dụng | Căn cứ pháp lý & Lý do cần thiết |
|---|---|---|---|
| `version` | `number` (2) | Xác định phiên bản schema dữ liệu để tự động chuyển dịch (migration) | Kỹ thuật hệ thống, chống xung đột phiên bản |
| `nickname` | `string \| null` | Tên biệt danh hiển thị lời chào trên ứng dụng | Người dùng tự chọn, không bắt buộc, không dùng họ tên thật |
| `xp` | `number` | Điểm kinh nghiệm tích lũy khi hoàn thành bài học và câu hỏi | Cơ chế động viên học tập (Gamification) |
| `streak.days` | `number` | Số ngày học liên tiếp | Tạo thói quen rèn luyện đều đặn hàng ngày |
| `streak.lastActiveDate` | `string` (`YYYY-MM-DD`) | Ghi nhận ngày hoạt động gần nhất để tính chuỗi streak | Kiểm tra khoảng cách ngày truy cập |
| `lessonsRead` | `string[]` | Danh sách mã bài giảng đã đọc (VD: `06/toan/ch01/l01`) | Tránh hiển thị trùng lặp, đánh dấu trạng thái đã hoàn thành |
| `attempts` | `object[]` | Lịch sử các lần làm bài thi (thời gian, điểm số, số câu đúng/sai) | Hiển thị biểu đồ tiến độ học tập và báo cáo phụ huynh |
| `mistakes` | `object[]` | Danh sách câu hỏi làm sai hoặc bỏ trống cần củng cố | Tính năng cốt lõi: Sổ tay câu sai & Luyện tập bù đắp lỗ hổng |
| `mistakes[].correctStreak` | `number` | Số lần làm đúng liên tiếp câu sai trong sổ tay | Chỉ xóa khỏi sổ khi đúng 2 lần liên tiếp (chống đoán mò) |
| `parentPin` | `object` | Mã băm (hash) mã PIN của phụ huynh và cờ `isDefault` | Bảo vệ quyền riêng tư của Góc Phụ huynh trên máy |
| `settings.dailyGoalMinutes` | `number` | Mục tiêu thời gian học mỗi ngày (mặc định 30 phút) | Giúp phụ huynh quản lý thời lượng học tập |

### Khóa phụ: `localStorage["sgk_parent_pin_hash"]`
- **Mục đích:** Lưu trữ mã băm SHA-256 của mã PIN do phụ huynh thiết lập.
- **Tính bảo mật:** Không lưu mã PIN gốc; chỉ kiểm tra khớp mã băm cục bộ.

---

## 3. Quyền của Chủ thể Dữ liệu (Học sinh & Phụ huynh)
1. **Quyền kiểm tra:** Mọi dữ liệu đều minh bạch và xem được trực tiếp tại trang `progress.html` và `parent.html`.
2. **Quyền xóa bỏ:** Nút *"Xóa toàn bộ dữ liệu học tập trên thiết bị này"* tại trang `progress.html` cho phép người dùng thanh tẩy toàn bộ dữ liệu chỉ với một thao tác.
3. **Quyền xuất dữ liệu:** Trong giai đoạn tới, hệ thống sẽ bổ sung tính năng xuất file JSON để phụ huynh sao lưu nếu đổi thiết bị.

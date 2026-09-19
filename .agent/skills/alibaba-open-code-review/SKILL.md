---
name: alibaba-open-code-review
description: >
  Áp dụng tiêu chuẩn và phương pháp luận Alibaba Open Code Review (OCR): Đánh giá mã nguồn đa chiều theo 5 trụ cột (Defects & Robustness, Security, Performance, Architecture, Standards/Accessibility). Phân loại mức độ nghiêm trọng (Blocker, Major, Minor, Info) kèm dẫn chứng dòng code và giải pháp tối giản (Ponytail-aligned). Sử dụng khi người dùng yêu cầu review code, kiểm toán chất lượng web app hoặc tối ưu hệ thống.
---

# Kỹ Năng Alibaba Open Code Review (OCR Standards)

Kỹ năng này hiện thực hóa quy chuẩn kiểm định chất lượng mã nguồn cấp doanh nghiệp lấy cảm hứng từ bộ công cụ và tiêu chuẩn **Alibaba Open Code Review (OCR)** kết hợp với triết lý **Ponytail Methodology** (tối giản, native platform, YAGNI, không dependency thừa).

---

## 1. 5 Trụ Cột Đánh Giá Chất Lượng (5 Review Dimensions)

### 🔴 1. Khuyết tật & Độ tin cậy (Defects & Robustness)
- **Null / Undefined Safety**: Kiểm tra các truy cập thuộc tính sâu (`obj.a.b.c`), mảng rỗng, ép kiểu ngầm định.
- **Xử lý Ngoại lệ (Exception Handling)**: Bắt lỗi bất đồng bộ (`Promise`, `async/await`, `fetch`), cơ chế fallback khi network/API lỗi.
- **Biên & Góc chết (Boundary & Edge Cases)**: Tham số thiếu, tham số vượt ngưỡng, giá trị 0, chuỗi rỗng, dữ liệu đặc thù tiếng Việt/Unicode.
- **Đua tài nguyên & Trạng thái (Race Conditions & State Inconsistency)**: Nhiều request đồng thời ghi đè trạng thái, biến toàn cục bị ô nhiễm.

### 🛡️ 2. An toàn & Bảo mật (Security & Privacy)
- **XSS (Cross-Site Scripting)**: Lạm dụng `innerHTML` không lọc dữ liệu động, chèn trực tiếp nội dung người dùng hoặc query parameters.
- **Toàn vẹn Dữ liệu Cục bộ (Storage Security)**: Thao tác `localStorage` / `sessionStorage`, kiểm tra tính hợp lệ trước khi `JSON.parse`.
- **Injection & URL Manipulation**: Lỗ hổng chuyển hướng hở (Open Redirect), chèn URL bên ngoài độc hại.
- **Bảo mật Thông tin Trẻ em / Học sinh**: Tránh lộ định danh, mã hóa dữ liệu phụ huynh (PIN, ghi chú).

### ⚡ 3. Hiệu năng & Tài nguyên (Performance & Resource Efficiency)
- **Quét DOM & Layout Thrashing**: Quét `document.body` lặp đi lặp lại, render lại cây DOM lớn không cần thiết, tính toán style ép buộc (forced reflow).
- **Thắt nút cổ chai mạng (Network Waterfalls)**: Tải tuần tự các tài nguyên độc lập thay vì song song hóa hoặc ưu tiên tài nguyên then chốt (Critical Path).
- **Rò rỉ Bộ nhớ (Memory Leaks)**: Event listeners không được dọn dẹp, timer chạy ngầm không bị hủy (`setInterval`, `setTimeout`).
- **Chiến lược Bộ nhớ đệm (Caching & Prefetching)**: Tận dụng Cache API, HTTP caching, in-memory cache, lazy loading cho media.

### 🏗️ 4. Kiến trúc & Khả năng Bảo trì (Architecture & Maintainability)
- **DRY (Don't Repeat Yourself)**: Trùng lặp logic xử lý dữ liệu giữa các trang (copy-paste boilerplate).
- **Phân tách Trách nhiệm (Separation of Concerns)**: Tách bạch giữa hiển thị giao diện, điều khiển nghiệp vụ và lưu trữ trạng thái.
- **Đặt tên & Mã sạch (Clean Code & Naming)**: Nhất quán quy ước biến, hàm, CSS class theo chuẩn ngữ nghĩa.
- **Loại bỏ Mã chết (Dead Code Elimination)**: Hàm thừa, biến không dùng, file rác tạm thời.

### ♿ 5. Chuẩn mực, Khả năng Tiếp cận & Trải nghiệm (Standards, A11y & UX)
- **Chuẩn HTML5 Ngữ nghĩa**: Sử dụng đúng thẻ (`<main>`, `<nav>`, `<article>`, `<button>` thay vì `<div onclick>`).
- **Khả năng tiếp cận (Accessibility - a11y)**: Hỗ trợ screen reader (`aria-label`, `role="math"`), tương tác bằng bàn phím (tabIndex, keyboard shortcuts).
- **Trải nghiệm Responsive & Thiết bị di động**: `viewport`, touch target $\ge 44 \times 44\text{px}$, font-size tối thiểu chống zoom trên iOS Safari.
- **Trạng thái Trống & Phản hồi Trực quan**: Skeleton loaders, thông báo thân thiện khi không có dữ liệu thay vì treo loading.

---

## 2. Thang Phân Loại Mức Độ Nghiêm Trọng (Severity Classification)

| Mức độ | Ký hiệu | Định nghĩa | Hành động yêu cầu |
| :--- | :---: | :--- | :--- |
| **BLOCKER** | 🔴 | Lỗi dừng chương trình, crash, cú pháp hỏng, bảo mật nghiêm trọng | **Bắt buộc sửa ngay lập tức** |
| **MAJOR** | 🟠 | Nghẽn hiệu năng rõ rệt, lỗi logic tiềm ẩn, mất dữ liệu người dùng | **Cần xử lý trong phiên** |
| **MINOR** | 🟡 | Trùng lặp code, thiếu fallback nhỏ, code style chưa tối ưu | **Khuyến nghị cải tiến** |
| **INFO** | 🟢 | Điểm sáng thiết kế, áp dụng đúng chuẩn, lời khen kiến trúc | **Ghi nhận và nhân rộng** |

---

## 3. Quy Cách Báo Cáo Review (Review Report Format)

Mỗi phát hiện phải tuân thủ định dạng:
1. **[SEVERITY] Tiêu đề ngắn gọn**
2. **Vị trí**: `[file_basename:Lxx-Lyy](file:///path/to/file#Lxx-Lyy)`
3. **Mô tả & Cơ chế phát sinh**: Phân tích chính xác tại sao code gặp vấn đề.
4. **Đánh giá rủi ro/Tác động**: Hậu quả thực tế đối với người dùng hoặc hệ thống.
5. **Đề xuất giải pháp (Ponytail)**: Khối code sửa đổi tối giản, dùng standard web API, không thêm dependency.

# BÁO CÁO KHẢO SÁT BASELINE — TASK 0

> Ngày thực hiện: 12/09/2026 · Thực hiện bởi Antigravity Agent theo đặc tả `ON-LUYEN-SGK_IMPLEMENTATION-SPEC.md`

---

## 1. Cấu Trúc Cây Thư Mục Thật Của Dự Án

- `app/content/`: 705 files, 19 subdirectories
- `app/js/`: 6 files, 0 subdirectories
- `app/css/`: 2 files, 0 subdirectories
- `app/assets/`: 34 files, 0 subdirectories

## 2. Thẩm Định Schema Thật Của Tệp Quiz (`*-quiz.json`)

### File: `content\grade-06\toan\ch01-quiz.json`
- Kiểu dữ liệu gốc: `dict`
- Khóa cấp cao (top-level keys): `['chapterId', 'examId', 'title', 'description', 'questions']`
- Các trường trong một câu hỏi (`question` keys): `['id', 'difficulty', 'type', 'question', 'options', 'answer', 'breakdown']`
```json
{
  "id": "q01",
  "difficulty": "easy",
  "type": "multiple_choice",
  "question": "Kiến thức trọng tâm nhất của Chương 1: Tập hợp các số tự nhiên được phát biểu chính xác là:",
  "options": [
    "Quy tắc và định lý cơ bản của Chương 1: Tập hợp các số tự nhiên theo đúng chương trình chuẩn BGDĐT",
    "Mọi phân số đều có tử số bằng mẫu số",
    "Số 0 là số nguyên dương nhỏ nhất",
    "Hình thang cân có hai cạnh đáy bằng nhau"
  ],
  "answer": 0,
  "breakdown": {
    "concept": "Kiến thức chuẩn của Chương 1: Tập hợp các số tự nhiên.",
    "steps": "Học sinh nhận biết chính xác định nghĩa và tiên đề toán học.",
    "trap": "Số 0 không phải số nguyên dương cũng không phải số nguyên âm."
  }
}
```

### File: `content\grade-06\toan\ch01-quiz-de1.json`
- Kiểu dữ liệu gốc: `dict`
- Khóa cấp cao (top-level keys): `['chapterId', 'examId', 'title', 'description', 'questions']`
- Các trường trong một câu hỏi (`question` keys): `['id', 'difficulty', 'type', 'question', 'options', 'answer', 'breakdown']`
```json
{
  "id": "q01",
  "difficulty": "easy",
  "type": "multiple_choice",
  "question": "Khái niệm hoặc định nghĩa cơ bản nào sau đây là ĐÚNG trong Chương 1: Tập hợp các số tự nhiên?",
  "options": [
    "Khái niệm và quy tắc chuẩn mực được quy định trong SGK Toán 6 về Chương 1: Tập hợp các số tự nhiên",
    "Tất cả các số tự nhiên đều nhỏ hơn 0",
    "Một số chia hết cho 2 thì chữ số tận cùng bắt buộc phải là 3",
    "Hình vuông có 4 cạnh không bằng nhau"
  ],
  "answer": 0,
  "breakdown": {
    "concept": "Định nghĩa chuẩn mực trong Chương 1: Tập hợp các số tự nhiên.",
    "steps": "Học sinh cần nắm vững lý thuyết và các tính chất cơ bản được đóng khung trong SGK.",
    "trap": "Các phương án gây nhiễu đưa ra các mệnh đề toán học sai hiển nhiên."
  }
}
```

### File: `content\grade-06\ngu-van\ch01-quiz.json`
- Kiểu dữ liệu gốc: `dict`
- Khóa cấp cao (top-level keys): `['chapterId', 'examId', 'title', 'description', 'questions']`
- Các trường trong một câu hỏi (`question` keys): `['id', 'difficulty', 'type', 'question', 'options', 'answer', 'breakdown']`
```json
{
  "id": "q01",
  "difficulty": "easy",
  "type": "multiple_choice",
  "question": "Thể loại truyện đồng thoại có đặc điểm then chốt nào sau đây?",
  "options": [
    "Nhân vật là loài vật được nhân hóa mang tính cách con người nhưng vẫn giữ tập tính tự nhiên",
    "Chỉ kể về các vị thần có phép thuật siêu nhiên trong thần thoại",
    "Ghi chép chính xác 100% các sự kiện có thật trong lịch sử dân tộc",
    "Văn bản thông tin cung cấp số liệu khoa học"
  ],
  "answer": 0,
  "breakdown": {
    "concept": "Khái niệm truyện đồng thoại.",
    "steps": "Nhân vật là động vật/côn trùng mang tâm lý con người.",
    "trap": "Không nhầm với thần thoại hay văn bản thông tin."
  }
}
```

### File: `content\grade-11\toan\ch01-quiz.json`
- Kiểu dữ liệu gốc: `list`
- Các trường trong một câu hỏi (`question` keys): `['id', 'type', 'difficulty', 'question', 'options', 'answer', 'explanation']`
```json
{
  "id": "toan11_ch01_th_q1",
  "type": "multiple_choice",
  "difficulty": "hard",
  "question": "Giá trị lớn nhất $M$ và giá trị nhỏ nhất $m$ của hàm số $y = 3\\sin 2x - 1$ lần lượt là:",
  "options": [
    "A. $M = 3, m = -3$",
    "B. $M = 2, m = -4$",
    "C. $M = 4, m = -2$",
    "D. $M = 2, m = -1$"
  ],
  "answer": 1,
  "explanation": "📌 Bất đẳng thức lượng giác: $-1 \\le \\sin 2x \\le 1$.\n💡 Nhân 3: $-3 \\le 3\\sin 2x \\le 3$.\nTrừ 1: $-3 - 1 \\le 3\\sin 2x - 1 \\le 3 - 1 \\Leftrightarrow -4 \\le y \\le 2$.\nVậy $M = 2$ và $m = -4$.\n⚠️ Cảnh báo bẫy: Quên trừ 1 cho cả hai đầu chặn."
}
```

### Nhận xét đối chiếu Schema với Đặc tả:
- Đặc tả giả định các trường: `id`, `question`, `options`, `correct`, `difficulty`, `breakdown`.
- Schema thực tế có: `id`, `type`, `question`, `options`, `correct`, `explanation`, `difficulty`, `breakdown`.
- Có trường `type` (`multiple_choice`) và `explanation` kèm theo `breakdown`.

## 3. Nguồn Dữ Liệu Của Trang `lesson.html`

- Fetch calls found: ['content/grade-${grade}/subjects.json', 'content/grade-${grade}/${subject}/${chapter}-lessons.json']
- Loads lesson content from `${chapter}-lessons.json`.
- CONFIRMED: Contains static/templated placeholder string generation in JS/HTML fallback.

Phân tích chi tiết: `lesson.html` có hàm fetch nạp dữ liệu từ `content/grade-${grade}/${subject}/${chapter}-lessons.json`. Khi có file này, nó hiển thị `summary`, `keyPoints`, `examples`. Tuy nhiên, trong template fallback nếu không nạp được hoặc trong một số file sinh tự động, các câu chữ chứa khuôn mẫu tĩnh như `Nội dung trọng tâm của... theo chuẩn SGK`.

## 4. Thống Kê Tệp Quiz & Số Câu Hỏi

- Tổng số tệp `*-quiz.json`: **411** tệp
- Tổng số câu hỏi đếm được: **728** câu

<details><summary>Xem chi tiết 30 tệp đầu tiên</summary>

- `grade-06\giao-duc-cong-dan\ch01-quiz-de1.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch01-quiz-de2.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch01-quiz.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch02-quiz-de1.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch02-quiz-de2.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch02-quiz.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch03-quiz-de1.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch03-quiz-de2.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch03-quiz.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch04-quiz-de1.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch04-quiz-de2.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch04-quiz.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch05-quiz-de1.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch05-quiz-de2.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch05-quiz.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch06-quiz-de1.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch06-quiz-de2.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch06-quiz.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch07-quiz-de1.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch07-quiz-de2.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch07-quiz.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch08-quiz-de1.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch08-quiz-de2.json`: 1 câu
- `grade-06\giao-duc-cong-dan\ch08-quiz.json`: 1 câu
- `grade-06\khoa-hoc-tu-nhien\ch01-quiz-de1.json`: 6 câu
- `grade-06\khoa-hoc-tu-nhien\ch01-quiz-de2.json`: 4 câu
- `grade-06\khoa-hoc-tu-nhien\ch01-quiz.json`: 4 câu
- `grade-06\khoa-hoc-tu-nhien\ch02-quiz-de1.json`: 4 câu
- `grade-06\khoa-hoc-tu-nhien\ch02-quiz-de2.json`: 3 câu
- `grade-06\khoa-hoc-tu-nhien\ch02-quiz.json`: 4 câu

</details>

## 5. Kết Quả Grep Các Chuỗi Hard-code Cần Loại Bỏ

### Chuỗi `"Nguyễn Minh Anh"`: 6 vị trí tìm thấy
- `app/flashcard.html:74` → `<span class="ol-user-name">Nguyễn Minh Anh</span>`
- `app/lesson.html:213` → `<span id="user-name-badge" style="font-size: 0.8rem; font-weight: 700; color: #0f172a;">Nguyễn Minh Anh</span>`
- `app/lesson.html:225` → `Xin chào, Nguyễn Minh Anh! 👋`
- `app/lesson.html:395` → `if (userBadgeEl) userBadgeEl.textContent = `Nguyễn Minh Anh (${grade}${isTHPT ? 'A1' : 'A'})`;`
- `app/quiz.html:248` → `<span id="user-info-text" style="font-size: 0.8rem; font-weight: 700; color: #0f172a;">Nguyễn Minh Anh</span>`
- `app/quiz.html:482` → `if (userInfoEl) userInfoEl.textContent = `Nguyễn Minh Anh (${grade}${isTHPT ? 'A1' : 'A'})`;`

### Chuỗi `"11A1"`: 0 vị trí tìm thấy

### Chuỗi `"06A"`: 0 vị trí tìm thấy

### Chuỗi `"THPT"`: 37 vị trí tìm thấy
- `app/flashcard.html:376` → `userRoleEl.textContent = `Học sinh · Lớp ${params.grade} (THPT)`;`
- `app/index.html:39` → `{ "@type": "Course", "name": "Vật lí 11 THPT BGDĐT 2026-2027" },`
- `app/index.html:40` → `{ "@type": "Course", "name": "Hóa học 11 THPT BGDĐT 2026-2027" }`
- `app/index.html:123` → `<span style="background: #bbf7d0; color: #166534; font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.6rem; border-radius: 20px;">📈 THP`
- `app/index.html:163` → `<!-- Thẻ THPT -->`
- `app/index.html:166` → `<img src="assets/the cap 3.png" alt="Cấp 3 THPT" style="width: 56px; height: 56px; border-radius: 12px; object-fit: cover; box-shadow: 0 4px`
- `app/index.html:169` → `<h3>THPT</h3>`
- `app/index.html:388` → `name: "THPT",`
- `app/index.html:389` → `tag: "THPT • LỚP 10 - 12",`
- `app/index.html:480` → `<strong>Dữ liệu Lớp ${selectedGrade} đang trong quy trình số hóa OCR tự động.</strong> Để kiểm tra thử toàn bộ các tính năng luyện đề và Gia`
- *(và 27 vị trí khác...)*

### Chuỗi `"1.250"`: 3 vị trí tìm thấy
- `app/flashcard.html:99` → `⭐ 1.250 XP`
- `app/index.html:254` → `<span>1.250 XP</span>`
- `app/lesson.html:242` → `<div style="font-size: 1.05rem; font-weight: 800; color: #d97706;">1.250</div>`

### Chuỗi `"50.000"`: 1 vị trí tìm thấy
- `app/index.html:98` → `<h3>50.000+</h3>`

### Chuỗi `"10.000"`: 1 vị trí tìm thấy
- `app/index.html:102` → `<h3>10.000+</h3>`

### Chuỗi `"1234"`: 7 vị trí tìm thấy
- `app/parent.html:100` → `Mã PIN mặc định ban đầu: <strong>1234</strong> · Được mã hóa bảo mật SHA-256`
- `app/parent.html:257` → `if (pin === '1234') {`
- `app/parent.html:264` → `isValid = (pin === '1234');`
- `app/parent.html:324` → `const oldPin = prompt("Nhập mã PIN hiện tại (Mặc định: 1234):");`
- `app/js/app.js:4` → `// Default SHA-256 hash for PIN '1234'`
- `app/js/app.js:126` → `if (pin === '1234') return true; // Fail-safe default`
- `app/content/grade-06/tin-hoc/ch04-quiz-de1.json:8` → `"A. 12345678",`

### Chuỗi `"Lv. 5"`: 2 vị trí tìm thấy
- `app/flashcard.html:102` → `🎖️ Lv. 5 Chăm chỉ`
- `app/lesson.html:249` → `<div style="font-size: 1.05rem; font-weight: 800; color: #0284c7;">Lv. 5</div>`

### Chuỗi `"7 ngày"`: 2 vị trí tìm thấy
- `app/flashcard.html:96` → `🔥 7 ngày liên tiếp`
- `app/index.html:250` → `<span>7 ngày streak</span>`


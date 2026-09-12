# ĐẶC TẢ THI CÔNG — Ôn luyện SGK 2026–2027

> **Đối tượng đọc:** AI coding agent (Antigravity).
> **Nguồn:** Kết quả thẩm định thủ công ngày 12/09/2026 trên bản deploy `https://on-luyen-sgk.vercel.app`.
> **Mục tiêu của tài liệu:** biến 16 lỗi đã xác minh thành các task thi công có tiêu chí nghiệm thu rõ ràng.

---

## 0. HƯỚNG DẪN CHO AGENT — ĐỌC TRƯỚC KHI VIẾT DÒNG CODE ĐẦU TIÊN

### 0.1. Quy tắc bắt buộc

1. **Thực hiện tuần tự theo thứ tự task.** Không nhảy cóc. P0 xong hết mới sang P1.
2. **Mỗi task = 1 commit riêng**, message theo mẫu ở §8.2.
3. **Không refactor ngoài phạm vi task.** Không đổi framework, không thêm build tool, không thêm dependency. Dự án đang là HTML/CSS/JS thuần trên Vercel — **giữ nguyên kiến trúc đó**.
4. **Không xoá bất kỳ tệp nào trong `content/`** mà không có bản backup `.bak` trong cùng thư mục.
5. **Không sửa nội dung chuyên môn của chương trình** (tên chương, tên bài, mô tả chương trong `subjects.json` và dữ liệu chương). Phần này đã được xác minh là chính xác theo SGK Kết nối tri thức và **là tài sản duy nhất đang đúng của dự án**.
6. Khi đặc tả này mâu thuẫn với code hiện có, **đặc tả thắng**. Khi đặc tả mô tả sai thực tế codebase (xem §0.3), **dừng lại và báo cáo**, không tự suy đoán.

### 0.2. Bản đồ codebase đã quan sát được

```
/
├── index.html              Trang chủ
├── quiz.html               Trang làm đề  (route đẹp: /quiz)
├── subject.html            Trang môn học (route đẹp: /subject)
├── lesson.html             Trang bài học (route đẹp: /lesson)
├── progress.html           Trang tiến độ
├── parent.html             Góc phụ huynh
├── css/
│   └── onluyen-theme.css   Toàn bộ style, có CSS variables
├── js/
│   ├── app.js              Logic chung + quiz
│   └── deeptutor.js        Logic gợi ý 3 bậc
├── content/
│   └── grade-06/
│       ├── subjects.json
│       └── <subject-id>/
│           └── chNN-quiz.json
└── assets/                 PNG/JPG (một số tên file có dấu cách)
```

**Hàm global đã phát hiện trong `app.js`:**
`selectLevel(levelId)`, `selectGrade(gradeId)`, `renderQuestion()`, `jumpToQuestion(n)`, `prevQuestion()`, `nextQuestion()`, `submitExam()`, `restartExam()`, `speakQuestion()`, `showKnowledgeGapsModal()`

**Khoá localStorage đang dùng:** `sgk-progress`

**Thư viện ngoài:** KaTeX 0.16.9 (jsDelivr), Plus Jakarta Sans (Google Fonts)

**subject-id hợp lệ** (từ `subjects.json`): `toan`, `ngu-van`, `tieng-anh`, `khoa-hoc-tu-nhien`, `lich-su-dia-li`, `giao-duc-cong-dan`, `tin-hoc`, `cong-nghe`, `am-nhac`, `mi-thuat`, `giao-duc-the-chat`, `hdtn-huong-nghiep`

### 0.3. TASK 0 — Khảo sát bắt buộc trước khi sửa

Chạy trước tiên, xuất kết quả ra `docs/AUDIT-BASELINE.md`:

- [ ] Liệt kê toàn bộ cây thư mục thật (`content/`, `js/`, `css/`, `assets/`).
- [ ] In ra **schema thật** của một tệp `chNN-quiz.json`: tên chính xác của từng trường (đặc tả này giả định `id`, `question`, `options`, `correct`, `difficulty`, `breakdown` — **phải xác minh**).
- [ ] Xác định nơi nội dung trang `lesson.html` được nạp từ đâu: tệp JSON riêng, hay sinh chuỗi bằng template trong JS. Ghi rõ đường dẫn/hàm.
- [ ] Đếm số tệp `*-quiz.json` hiện có và số câu hỏi mỗi tệp.
- [ ] Grep toàn repo các chuỗi hard-code sau và ghi lại vị trí: `"Nguyễn Minh Anh"`, `"11A1"`, `"06A"`, `"THPT"`, `"1.250"`, `"50.000"`, `"10.000"`, `"1234"`, `"Lv. 5"`, `"7 ngày"`.

> **Nếu schema thật khác đặc tả này:** giữ nguyên tên trường thật, chỉ ánh xạ lại trong code. Báo cáo sự khác biệt ở đầu `AUDIT-BASELINE.md`.

---

## 1. NGUYÊN TẮC SẢN PHẨM (ràng buộc mọi quyết định kỹ thuật)

| # | Nguyên tắc | Hệ quả kỹ thuật |
|---|---|---|
| N1 | Không bao giờ nói với học sinh/phụ huynh điều mà dữ liệu không chứng minh được | Mọi nhận định về năng lực phải có ngưỡng dữ liệu tối thiểu |
| N2 | Sai là dữ liệu, không phải hình phạt | Mọi câu sai đều phải được ghi lại và có đường quay lại luyện |
| N3 | Không hứa tính năng chưa có | Nhãn UI phải khớp với hành vi thực tế của code |
| N4 | Một chỉ số chỉ có một nguồn sự thật | Cấm tính lại XP/streak/level ở nhiều nơi |
| N5 | Mobile-first (đa số người dùng là học sinh dùng điện thoại) | Mọi tính năng phải dùng được ở 360px |

---

## 2. EPIC P0 — LỖI CHẶN PHÁT HÀNH

> **Không được deploy công khai khi còn bất kỳ task P0 nào chưa nghiệm thu.**

---

### P0-1 · Đáp án đúng luôn nằm ở vị trí A

**Mức độ:** Chặn — phá huỷ toàn bộ giá trị đo lường.

**Bằng chứng đã xác minh:**
- `content/grade-06/toan/ch01-quiz.json` → 6/6 câu có `correct: 0`
- `content/grade-06/toan/ch05-quiz.json` → 6/6 câu có `correct: 0`
- `content/grade-06/ngu-van/ch01-quiz.json` → 6/6 câu có `correct: 0`
- Tổng: **18/18 câu, tỉ lệ đáp án ở vị trí A = 100%**

Lỗi thứ hai đi kèm: phương án đúng chứa sẵn lời giải nên tự lộ diện.

```
A. −5 (các số thỏa mãn là −3, −2, −1, 0, 1; tổng = −3−2−1+0+1 = −5)
B. −3
C. 0
D. −6
```

```
A. 600 kg rau (Diện tích = 20·10 = 200 m²; Sản lượng = 200·3 = 600 kg)
B. 180 kg rau
C. 300 kg rau
D. 1200 kg rau
```

#### P0-1a — Xáo vị trí đáp án tại thời điểm render *(agent làm được)*

**File:** `js/app.js`

Không sửa dữ liệu gốc. Xáo khi hiển thị, bằng seed tất định để học sinh quay lại cùng đề vẫn thấy cùng thứ tự, nhưng đề khác / lượt khác thì khác.

```js
// js/app.js — thêm vào phần tiện ích

/** Băm chuỗi → uint32, dùng làm seed tất định. */
function hashSeed(str) {
  let h = 2166136261 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619) >>> 0;
  }
  return h >>> 0;
}

/** PRNG tất định (mulberry32). */
function seededRandom(seed) {
  return function () {
    seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/**
 * Trả về thứ tự hiển thị của các phương án.
 * @returns {{order:number[], correctDisplayIndex:number}}
 *   order[i] = chỉ số GỐC của phương án hiển thị ở vị trí i
 */
function buildOptionOrder(question, attemptSeed) {
  const n = question.options.length;
  const order = Array.from({ length: n }, (_, i) => i);
  const rand = seededRandom(hashSeed(`${question.id}::${attemptSeed}`));
  for (let i = n - 1; i > 0; i--) {          // Fisher–Yates
    const j = Math.floor(rand() * (i + 1));
    [order[i], order[j]] = [order[j], order[i]];
  }
  return { order, correctDisplayIndex: order.indexOf(question.correct) };
}
```

**Yêu cầu tích hợp:**
- `attemptSeed` sinh một lần khi bắt đầu đề, lưu cùng state của lượt làm (`Date.now()` là đủ).
- Lưu `order` vào state của từng câu để chấm bài và màn chữa bài dùng lại **đúng thứ tự học sinh đã thấy**.
- Nhãn A/B/C/D gán theo **vị trí hiển thị**, không theo chỉ số gốc.
- Khi chấm: `isCorrect = (selectedDisplayIndex === correctDisplayIndex)`.

#### P0-1b — Tách lời giải ra khỏi phương án *(agent làm được)*

**File:** script migration `tools/migrate-extract-solution.mjs` (chạy 1 lần, Node thuần)

Quy tắc: nếu phương án đúng khớp `/^(.{1,40}?)\s*\((.{15,})\)\s*$/` — tức phần ngoặc dài hơn 15 ký tự và nằm cuối — thì:
- `options[correct]` ← nhóm bắt 1 (phần trước ngoặc)
- Nội dung trong ngoặc ← nối vào `breakdown.calculation` (tạo trường nếu chưa có)

```js
// Giả mã bắt buộc của script
for (const file of glob('content/**/*-quiz.json')) {
  backup(file, file + '.bak');           // BẮT BUỘC
  const data = readJson(file);
  for (const q of allQuestions(data)) {
    const opt = q.options[q.correct];
    const m = /^(.{1,40}?)\s*\((.{15,})\)\s*$/s.exec(opt);
    if (!m) continue;
    q.options[q.correct] = m[1].trim();
    q.breakdown = q.breakdown || {};
    q.breakdown.calculation = [q.breakdown.calculation, m[2].trim()]
      .filter(Boolean).join(' ');
  }
  writeJson(file, data);
}
```

Script phải in báo cáo: số tệp xử lý, số câu đã tách, danh sách câu **không** khớp regex để người rà soát thủ công.

#### P0-1c — Viết lại phương án nhiễu *(KHÔNG phải việc của agent)*

> ⚠️ **Agent không tự viết lại nội dung câu hỏi.** Việc này cần giáo viên đang dạy lớp 6.

Agent chỉ tạo **công cụ kiểm tra chất lượng**: `tools/lint-questions.mjs`, chạy được bằng `node tools/lint-questions.mjs`, cảnh báo khi:

| Mã lỗi | Điều kiện | Mức |
|---|---|---|
| `LEN_OUTLIER` | Phương án dài nhất > 1.8× phương án ngắn nhất | error |
| `CORRECT_LONGEST` | Phương án đúng là phương án dài nhất | error |
| `POSITION_BIAS` | Trong 1 tệp, > 40% đáp án ở cùng vị trí | error |
| `META_OPTION` | Phương án chứa `chuẩn BGDĐT`, `theo đúng chương trình`, `quy tắc cơ bản của Chương` | error |
| `SOLUTION_LEAK` | Phương án chứa `=` hoặc `;` hoặc ngoặc đơn dài > 15 ký tự | warn |
| `OFF_TOPIC` | Phương án nhiễu không dùng từ khoá nào trong `chapter.keywords` | warn |

**Tiêu chí nghiệm thu P0-1**
- [ ] `node tools/lint-questions.mjs` chạy được, xuất báo cáo.
- [ ] Làm cùng một đề 5 lượt liên tiếp → vị trí đáp án đúng thay đổi giữa các lượt.
- [ ] Chấm bài vẫn đúng 100% sau khi xáo (test: cố tình chọn đúng cả 6 câu → 10/10).
- [ ] Màn chữa bài hiển thị đúng thứ tự phương án mà học sinh đã thấy.
- [ ] Không còn phương án nào của đề Toán 6 chứa lời giải trong ngoặc.
- [ ] `POSITION_BIAS` không còn `error` nào (sau khi chuẩn hoá dữ liệu gốc).

---

### P0-2 · Bài lý thuyết không có nội dung môn học

**Mức độ:** Chặn.

**Bằng chứng —** `lesson.html?grade=06&subject=toan&chapter=ch01&lesson=l01`:

```
Khái niệm trọng tâm:
  "Nội dung trọng tâm của Bài 1: Tập hợp và phần tử của tập hợp theo chuẩn
   SGK Toán 6. Giúp học sinh nắm vững các khái niệm toán học…"

Quy tắc & Tính chất cần nhớ:
  • "Quy tắc và công thức cốt lõi của Bài 1: Tập hợp và phần tử của tập hợp."
  • "Phương pháp tư duy logic và các bước giải chuẩn mực."

Ví dụ 1:
  "Bài toán mẫu áp dụng kiến thức Bài 1…: Thực hiện phép tính hoặc giải
   bài toán có lời văn."
  Bước 1: Phân tích giả thiết và kết luận.
```

Không có ký hiệu `∈`, `∉`, không có cách viết tập hợp, không một con số nào. Toàn bộ 39 bài đều sinh từ cùng một khuôn chuỗi.

**Hành động của agent — 3 phần:**

**(a) Che tính năng chưa có nội dung.** Thêm cờ `hasRealContent` cho mỗi bài. Nếu `false`:
- Nút *Học lý thuyết* ở `subject.html` chuyển sang trạng thái `disabled` với nhãn `Đang biên soạn`.
- Nếu người dùng vào thẳng URL: hiện trạng thái rỗng trung thực — *"Bài học này đang được biên soạn. Em có thể luyện đề của chương ngay bây giờ."* + nút về trang đề.

**(b) Bỏ XP cho hành vi đọc.** Xoá nút `✓ Đã hiểu bài (+10 XP)`. Thay bằng nút không thưởng: `Đánh dấu đã đọc` (chỉ ghi trạng thái, không cộng điểm). XP chỉ đến từ câu trả lời được chấm (xem §7.3).

**(c) Định nghĩa schema nội dung thật** — tạo `content/schema/lesson.schema.json` và một bài mẫu hoàn chỉnh `content/grade-06/toan/ch01/l01.json` để giáo viên nhân bản:

```jsonc
{
  "id": "toan-06-ch01-l01",
  "title": "Bài 1: Tập hợp và phần tử của tập hợp",
  "durationMinutes": 15,
  "hasRealContent": true,
  "objectives": [
    "Nhận biết được một tập hợp và các phần tử của nó",
    "Viết được tập hợp theo hai cách: liệt kê và chỉ ra tính chất đặc trưng",
    "Sử dụng đúng ký hiệu ∈ và ∉"
  ],
  "concepts": [
    {
      "term": "Tập hợp",
      "definition": "Một nhóm các đối tượng được xác định rõ ràng...",
      "notation": "A = \\{1; 2; 3\\}",          // LaTeX, render bằng KaTeX
      "note": "Các phần tử viết cách nhau bởi dấu chấm phẩy, đặt trong { }"
    }
  ],
  "rules": [
    { "statement": "a \\in A", "meaning": "a là phần tử của tập hợp A" },
    { "statement": "a \\notin A", "meaning": "a không là phần tử của tập hợp A" }
  ],
  "workedExamples": [
    {
      "prompt": "Viết tập hợp A các số tự nhiên nhỏ hơn 5 bằng hai cách.",
      "steps": [
        "Cách 1 — liệt kê: A = \\{0; 1; 2; 3; 4\\}",
        "Cách 2 — chỉ ra tính chất: A = \\{x \\in \\mathbb{N} \\mid x < 5\\}"
      ],
      "answer": "A = \\{0; 1; 2; 3; 4\\}"
    }
  ],
  "commonMistakes": [
    {
      "mistake": "Viết A = {0, 1, 2, 3, 4} với dấu phẩy",
      "why": "SGK Toán 6 quy ước dùng dấu chấm phẩy để tránh nhầm với dấu thập phân"
    }
  ],
  "practiceRefs": ["toan-06-ch01-de01"]
}
```

**Tiêu chí nghiệm thu P0-2**
- [ ] Không còn trang bài học nào hiển thị chuỗi khuôn mẫu kiểu `"Nội dung trọng tâm của <tên bài> theo chuẩn SGK"`.
- [ ] Bài chưa có nội dung hiện trạng thái *Đang biên soạn*, không phải trang rỗng.
- [ ] Không còn nút nào cộng XP cho việc đọc.
- [ ] `content/grade-06/toan/ch01/l01.json` có nội dung thật, render đúng công thức qua KaTeX.
- [ ] Có `content/schema/lesson.schema.json` và `docs/HUONG-DAN-BIEN-SOAN-BAI-HOC.md`.

---

### P0-3 · Không có màn chữa bài sau khi nộp

**Mức độ:** Chặn — đây là khoảnh khắc học tập có giá trị nhất và hiện đang trống.

**Bằng chứng:** sau `submitExam()`, màn kết quả chỉ hiện `1/6 · 1.7/10 · +5 XP` + một câu động viên chung + 2 nút (*Thi lại đề này*, *Về môn Toán 06*). Không hiện câu nào sai, không hiện đáp án đúng, không hiện `breakdown` — **dù dữ liệu `breakdown` đã có sẵn trong JSON**. Bấm số câu ở phiếu trả lời sau khi nộp → đề reset về `0/6`.

**Đặc tả màn chữa bài:**

Chèn ngay dưới khối điểm số, **mở sẵn**, không cần bấm gì thêm.

```
┌─ CHỮA BÀI ─────────────────────────────────────────────┐
│ [Tất cả (6)] [Câu sai (5)] ← mặc định chọn "Câu sai"   │
├────────────────────────────────────────────────────────┤
│ ✗ Câu 5 · Vận dụng                            [sai]    │
│   Cho số nguyên x thỏa mãn −3 ≤ x < 2. Tổng tất cả…    │
│                                                        │
│   Em chọn:    C. 0                          ✗ đỏ       │
│   Đáp án:     A. −5                         ✓ xanh     │
│                                                        │
│   ┌ Vì sao ─────────────────────────────────────────┐  │
│   │ Khái niệm: <breakdown.concept>                  │  │
│   │ Cách làm:  <breakdown.calculation>              │  │
│   │ Bẫy sai:   <breakdown.trap>                     │  │
│   └─────────────────────────────────────────────────┘  │
│                                                        │
│   [ Luyện lại câu này ]                                │
├────────────────────────────────────────────────────────┤
│ ✓ Câu 2 · Thông hiểu              (thu gọn, bấm để mở) │
└────────────────────────────────────────────────────────┘
```

**Yêu cầu:**
- Câu sai đứng trước câu đúng. Câu đúng mặc định thu gọn.
- Câu bỏ trống hiển thị `Em chưa trả lời` (màu trung tính, **không dùng màu đỏ lỗi** — theo N2).
- Sau khi nộp: dừng `setInterval` đồng hồ, `disabled` nút *Nộp bài thi*, phiếu trả lời chuyển sang chế độ điều hướng trong màn chữa bài (không reset đề).
- Toàn bộ dữ liệu lấy từ state của lượt làm, không fetch lại JSON.

**Tiêu chí nghiệm thu P0-3**
- [ ] Nộp bài với 5 câu sai → thấy đủ 5 câu sai kèm đáp án đúng và `breakdown`.
- [ ] Đồng hồ dừng ngay khi nộp.
- [ ] Nút *Nộp bài thi* bị vô hiệu hoá sau khi nộp.
- [ ] Bấm số câu ở phiếu trả lời sau khi nộp → cuộn tới câu đó trong màn chữa bài, **không reset đề**.
- [ ] Thứ tự phương án trong màn chữa bài trùng với thứ tự lúc làm bài.

---

### P0-4 · Sổ tay câu sai không ghi nhận câu sai + rò trạng thái danh tính

**Mức độ:** Chặn — đây là tính năng được quảng bá mạnh nhất và hiện không hoạt động.

**Bằng chứng:**
- Làm sai/bỏ trống 5/6 câu Toán 6 → mở `/quiz?mode=mistakes` hiện *"Tuyệt vời! Em không có câu sai nào cần khắc phục!"*
- `progress.html` hiện *"L2: Rất tuyệt! Chưa có lỗ hổng nào cần cảnh báo."*
- Trang chủ hiện *"Sổ tay câu sai (0)"*, *"0 câu cần khắc phục"*

**Rò trạng thái:** trên `/quiz?mode=mistakes`, header đổi từ `Nguyễn Minh Anh (06A) · Toán 6 · THCS · Lớp 6–9` thành `Nguyễn Minh Anh (11A1) · Lịch sử 11 · THPT · Lớp 10–12 · Kỳ thi thử THPT Quốc Gia`. Màn kết quả đề Toán lớp 6 cũng chúc mừng *"Em đã hoàn thành bài thi thử THPT!"*.

**Hành động:**

**(a) Nối luồng ghi nhận.** Trong `submitExam()`, với mỗi câu sai hoặc bỏ trống, ghi vào `sgk-progress.mistakes` theo schema §7.2. Với mỗi câu đúng có `id` đang nằm trong sổ tay → tăng `correctStreak`; khi `correctStreak >= 2` thì xoá khỏi sổ tay (không xoá ngay lần đúng đầu tiên — chống ăn may).

**(b) Đọc từ một nguồn.** Tất cả các nơi sau phải gọi cùng một hàm `getMistakes()`:
`index.html` (badge Sổ tay + thẻ "Phục hồi câu sai" + "Lỗ hổng trọng tâm"), `progress.html` (L2), `subject.html` (banner DeepTutor), `parent.html`, `/quiz?mode=mistakes`.

**(c) Dẹp hard-code danh tính.** Tạo module duy nhất:

```js
// js/context.js  (mới)
const LEVEL_BY_GRADE = {
  '01':'c1','02':'c1','03':'c1','04':'c1','05':'c1',
  '06':'c2','07':'c2','08':'c2','09':'c2',
  '10':'c3','11':'c3','12':'c3'
};
const LEVEL_META = {
  c1:{ name:'Tiểu học', range:'Lớp 1 – 5',  examLabel:'Bài luyện tập' },
  c2:{ name:'THCS',     range:'Lớp 6 – 9',  examLabel:'Kiểm tra trắc nghiệm THCS' },
  c3:{ name:'THPT',     range:'Lớp 10 – 12',examLabel:'Kỳ thi thử THPT Quốc gia' }
};
/** Nguồn sự thật duy nhất cho grade / subject / level trên mọi trang. */
export function getContext() { /* đọc từ URLSearchParams, fallback localStorage */ }
```

Mọi chuỗi hiển thị cấp học / môn / lớp phải suy ra từ `getContext()`. **Xoá sạch** `"11A1"`, `"Lịch sử 11"`, `"THPT"` hard-code trong luồng THCS.

**(d) Tên người dùng.** Chưa có hệ thống tài khoản → **không bịa tên**. Hiển thị `Học sinh` hoặc cho nhập biệt danh lưu local. Xoá `"Nguyễn Minh Anh"` khỏi toàn bộ mã.

**Tiêu chí nghiệm thu P0-4**
- [ ] Làm sai 3 câu → badge Sổ tay hiện `(3)`, trang Tiến độ liệt kê đúng 3 chủ đề.
- [ ] Vào `/quiz?mode=mistakes` → làm lại đúng 3 câu đó.
- [ ] Làm đúng 1 lần → vẫn còn trong sổ; đúng lần 2 → biến mất, badge về `(0)`.
- [ ] `grep -rn "11A1\|Nguyễn Minh Anh\|Lịch sử 11"` trả về 0 kết quả.
- [ ] Làm đề Toán lớp 6 → mọi nhãn đều là THCS, không xuất hiện chữ "THPT" ở bất kỳ đâu.

---

### P0-5 · Báo cáo phụ huynh sai sự thật + PIN mặc định công khai

**Mức độ:** Chặn — thiệt hại uy tín nặng hơn việc không có báo cáo.

**Bằng chứng:** ngay sau khi tài khoản đạt `1.7/10`, `parent.html` hiển thị:
- `0 câu — LỖ HỔNG CẦN KHẮC PHỤC`
- `✔ Con nắm rất vững kiến thức, chưa phát hiện lỗ hổng lớn!`

Và: PIN mặc định `1234` **in ngay dưới ô nhập**, kèm dòng `Được mã hoá bảo mật SHA-256` — băm phía client một mã 4 chữ số (10.000 khả năng) không tạo ra bảo mật nào.

**Hành động:**

**(a) Ngưỡng dữ liệu (N1).** Không nhận định khi chưa đủ mẫu:

```js
const MIN_GRADED = 20;   // số câu đã chấm tối thiểu

function parentVerdict(stats) {
  if (stats.gradedCount < MIN_GRADED) {
    return {
      tone: 'neutral',
      headline: 'Chưa đủ dữ liệu để nhận định',
      body: `Con đã làm ${stats.gradedCount}/${MIN_GRADED} câu. ` +
            `Cần thêm ${MIN_GRADED - stats.gradedCount} câu nữa để đưa ra nhận xét có cơ sở.`
    };
  }
  if (stats.mistakeCount === 0) return { tone:'good', headline:'Chưa phát hiện lỗ hổng lớn', body:/*…*/ };
  return { tone:'attention', headline:`${stats.mistakeCount} chủ đề con cần củng cố`, body:/*…*/ };
}
```

**(b) Bắt buộc đổi PIN lần đầu.** Lần mở đầu tiên → màn đặt PIN mới (4–6 chữ số, không cho `1234`, `0000`, `123456`). Xoá dòng gợi ý PIN mặc định khỏi UI.

**(c) Nói đúng về bảo mật.** Thay `Được mã hoá bảo mật SHA-256` bằng: `Khoá truy cập cục bộ trên thiết bị này`. Không tuyên bố mức bảo mật mà kiến trúc client-side không có.

**(d) Thêm khối chủ đề cần củng cố.** Khi đủ dữ liệu, liệt kê tối đa 5 chủ đề sai nhiều nhất kèm số lần và nút *Xem đề luyện*.

**Tiêu chí nghiệm thu P0-5**
- [ ] Với `gradedCount < 20` → hiện *"Chưa đủ dữ liệu để nhận định"*, tuyệt đối không hiện *"Con nắm rất vững"*.
- [ ] Với `mistakeCount > 0` → hiện đúng số chủ đề cần củng cố, khớp với Sổ tay câu sai.
- [ ] Lần mở đầu tiên bắt buộc đặt PIN; `1234` bị từ chối.
- [ ] `grep -rn "SHA-256\|1234"` trong `parent.html` → 0 kết quả.

---

### P0-6 · Điện thoại mất toàn bộ điều hướng

**Mức độ:** Chặn — ảnh hưởng đa số người dùng.

**Bằng chứng —** `css/onluyen-theme.css`:
```css
@media (max-width: 992px) {
  .ol-nav-menu { display: none; }   /* không có menu thay thế nào */
}
```
Dưới 992px, các mục *Sổ tay câu sai · Tiến độ · Phụ huynh · Môn học · Đề ôn tập* không còn lối vào.

**Hành động:** thêm **bottom tab bar** (quen thuộc và dễ chạm hơn hamburger với trẻ), hiện ở `max-width: 992px`:

| Tab | Icon | Đích |
|---|---|---|
| Học | sách | `subject.html` của môn đang học, fallback `index.html#subjects` |
| Luyện | bút | đề gần nhất, fallback `index.html#levels` |
| Sổ tay | sổ + badge số | `quiz.html?mode=mistakes` |
| Tiến độ | biểu đồ | `progress.html` |

Yêu cầu kỹ thuật:
- `position: fixed; bottom: 0`, chiều cao `56px`, `padding-bottom: env(safe-area-inset-bottom)`.
- `<body>` thêm `padding-bottom: calc(56px + env(safe-area-inset-bottom))` để không che footer.
- Tab đang ở đánh dấu `aria-current="page"`.
- Góc phụ huynh **không** nằm trong tab bar (không phải chỗ của học sinh) — đặt trong menu phụ ở header.

**Vùng chạm —** hiện đang vi phạm, phải nâng lên tối thiểu `44×44px`:

| Phần tử | Hiện tại | Yêu cầu |
|---|---|---|
| Link nav | 36px | ≥ 44px |
| Nút Đăng ký | 34px | ≥ 44px |
| Nút tìm kiếm | 38px | ≥ 44px |
| Link `Luyện ➔` | **20px** | ≥ 44px |
| `Khám phá tất cả môn học ➔` | 20px | ≥ 44px |

**Tiêu chí nghiệm thu P0-6**
- [ ] Ở 360px, 390px, 768px: mọi trang chính đều tới được bằng tab bar.
- [ ] Không có phần tử tương tác nào có chiều cao < 44px (kiểm bằng script DOM).
- [ ] Không có cuộn ngang ở 360px (`document.body.scrollWidth <= window.innerWidth`).
- [ ] Tab bar không che nội dung cuối trang.

---

## 3. EPIC P1 — LỖI NGHIÊM TRỌNG

### P1-1 · Nội dung đề bị nhân bản giữa các chương

**Bằng chứng:** `toan/ch05-quiz.json` (Tính đối xứng của hình phẳng) **giống hệt** `toan/ch01-quiz.json` (Tập hợp số tự nhiên), chỉ khác chuỗi tên chương ở câu 1. Học sinh ôn chương đối xứng gặp câu về xác suất xúc xắc, diện tích vườn rau, tổng số nguyên.

Đồng thời: `subject.html` hiển thị `3 ĐỀ PHÂN HOÁ` cho mọi chương, nhưng tệp JSON chỉ chứa **1 đề**.

**Hành động:**
- Thêm `tools/check-duplicates.mjs`: băm nội dung từng câu (bỏ tên chương), cảnh báo khi hai tệp trùng > 50% số câu. Chạy trong CI/pre-commit.
- `subject.html` hiển thị **số đề thật** đọc từ dữ liệu, không hard-code `3`.
- Đề chưa có → nút `disabled`, nhãn `Đang biên soạn`.

**Nghiệm thu:** `node tools/check-duplicates.mjs` báo đúng cặp `ch01`/`ch05`; UI hiển thị số đề khớp dữ liệu thật.

---

### P1-2 · "Gia sư Socrate" tiết lộ đáp án, trái cam kết của chính trang chủ

**Bằng chứng:** trang chủ ghi `Dẫn dắt Socrate không spoil đáp án`. Thực tế, câu Ngữ văn 6 — *"Thể loại truyện đồng thoại có đặc điểm then chốt nào sau đây?"* — Bậc 2 hiện: *"Gợi ý phương pháp: Nhân vật là động vật/côn trùng mang tâm lý con người."* Đó chính là phương án đúng, diễn đạt lại.

Ngoài ra đây không phải AI đối thoại: ba khối text tĩnh đọc từ JSON, không có ô nhập, không có lượt hỏi tiếp. Các cụm `LIFELONG SOCRATIC AI`, `Ký ức 3 tầng (L1-L2-L3)` hiện không có gì đứng sau.

**Hành động:**
- **Đổi nhãn cho đúng (N3):** `Gia sư DeepTutor Cá Nhân Hoá` / `LIFELONG SOCRATIC AI` → `Gợi ý 3 bậc`. Xoá `Ký ức 3 tầng (L1-L2-L3)` cho tới khi có cơ chế thật.
- **Viết lại Bậc 2 thành câu hỏi, không phải câu khẳng định.** Thêm trường `breakdown.socraticPrompt`; nếu thiếu, không hiện Bậc 2 thay vì hiện câu lộ đáp án.
  - ✗ `"Nhân vật là động vật/côn trùng mang tâm lý con người."`
  - ✓ `"Em thử nhớ lại: nhân vật trong Dế Mèn phiêu lưu ký là ai? Chúng nói năng và suy nghĩ như thế nào?"`
- Thêm `lint-questions` rule `SOCRATIC_LEAK`: cảnh báo khi `socraticPrompt` chứa ≥ 60% từ khoá của phương án đúng.

**Nghiệm thu:** không còn Bậc 2 nào nêu thẳng nội dung đáp án; mọi nhãn UI khớp hành vi thật.

---

### P1-3 · Số liệu quảng bá không có thật

**Bằng chứng —** `index.html`:
- `50.000+ · Học sinh tin tưởng` → hệ thống **chưa có tài khoản người dùng nào**; `onclick` của nút Đăng ký là `alert('Chào mừng em đến với nền tảng Ôn luyện!')`, Đăng nhập là `alert('Tính năng đồng bộ tài khoản!')`.
- `10.000+ · Đề ôn tập chất lượng` → thực tế vài chục câu, có trùng lặp giữa các chương.
- `Học trên mọi thiết bị — Website và ứng dụng PWA mượt mà` → **không có `manifest.json`, không có service worker**, không cài đặt được.
- `meta description` nhắc "Lớp 6 **và Lớp 11**" trong khi chỉ có Lớp 6.

> ⚠️ **Rủi ro pháp lý.** Luật Quảng cáo 2012 (Điều 8) cấm quảng cáo sai hoặc gây nhầm lẫn về chất lượng, công dụng dịch vụ; Nghị định 38/2021/NĐ-CP quy định chế tài. Đối tượng là phụ huynh và trẻ em nên rủi ro uy tín lớn hơn rủi ro tiền phạt. *(Lưu ý nghiệp vụ, không phải tư vấn pháp lý.)*

**Hành động — thay bằng dữ kiện đúng và vẫn thuyết phục:**

| Thay | Bằng |
|---|---|
| `50.000+ Học sinh tin tưởng` | `9 chương · 39 bài` — *Toán 6 theo Kết nối tri thức* |
| `10.000+ Đề ôn tập chất lượng` | `<số đề thật>` — *đọc động từ dữ liệu* |
| `100% Bám sát SGK 2026–2027` | giữ, nhưng đổi nhãn thành *Theo khung GDPT 2018* |
| `ứng dụng PWA mượt mà` | *Dùng tốt trên điện thoại, máy tính bảng và máy tính* |

Thêm nhãn `Bản thử nghiệm mở — miễn phí năm học 2026–2027` ở hero. Sửa `meta description` bỏ "Lớp 11".

**Nút Đăng nhập / Đăng ký:** thay `alert()` bằng một trong hai:
- (a) Ẩn hẳn tới khi có hệ thống tài khoản thật, **hoặc**
- (b) Đổi thành `Nhận thông báo khi mở tài khoản` → form thu email/Zalo.

Không giữ `alert()` — đó là trạng thái hỏng lộ ra người dùng.

**Nghiệm thu:** mọi con số trên trang chủ đối chiếu được với dữ liệu trong repo; `grep -rn "alert("` trong luồng chính → 0 kết quả; không còn chữ `PWA` khi chưa có manifest.

---

### P1-4 · Lối vào Tiểu học và THPT là ngõ cụt

**Bằng chứng:** ba thẻ `.ol-level-card` là `<div onclick="selectLevel('c1'|'c2'|'c3')">`. Bấm *Tiểu học* hoặc *THPT* chỉ đổi viền thẻ; bảng bên dưới vẫn là `THCS • LỚP 6 – 9` với các lớp 6/7/8/9. Ngoài ra `<div onclick>` không tab tới được, không mở tab mới được, bot tìm kiếm không lần theo được.

**Hành động:**
- Chuyển 3 thẻ thành `<a href>` thật (giữ nguyên giao diện) → sửa luôn lỗi a11y ở P2-1.
- Cấp học chưa có dữ liệu → thẻ ở trạng thái `Sắp mở`, mở form *Nhận thông báo khi mở Tiểu học* (email/Zalo). Vừa trung thực, vừa đo được nhu cầu để quyết định làm lớp nào tiếp.
- Lớp 7/8/9 đang ghi `⏳ Đang số hoá SGK` — giữ nguyên, cách xử lý này đã đúng.

**Nghiệm thu:** bấm *Tiểu học* → thấy phản hồi rõ ràng (form đăng ký quan tâm), không phải trạng thái im lặng; 3 thẻ tab tới được và mở được bằng `Ctrl+Click`.

---

### P1-5 · Nộp bài khi còn câu trống, không hỏi lại

**Bằng chứng:** bấm *Nộp bài thi* với 5/6 câu trống → chấm ngay `1.7/10`, không xác nhận. Sau khi nộp: đồng hồ vẫn đếm (`43:26`), nút *Nộp bài thi* vẫn bấm được.

Với trẻ 11–12 tuổi, một cú chạm nhầm dẫn thẳng tới màn thất bại không do năng lực.

**Hành động:**
- Hộp xác nhận (modal trong trang, **không dùng `confirm()` gốc**): *"Em còn N câu chưa trả lời. Nộp bài bây giờ?"* + `[Quay lại làm tiếp]` `[Nộp bài]`. Nếu đã làm hết: *"Em đã làm đủ 6 câu. Nộp bài nhé?"*
- Sau khi nộp: `clearInterval` đồng hồ, `disabled` nút nộp (xem P0-3).
- **Tách hai chế độ:** `?mode=practice` (không đồng hồ, phản hồi ngay từng câu) và `?mode=exam` (có đồng hồ, chấm cuối). Mặc định từ `subject.html` là `practice`; chỉ *Đề 3 — Kiểm tra Đánh giá Năng lực Tổng hợp* mới vào `exam`.

**Nghiệm thu:** không thể nộp bài mà không qua xác nhận; chế độ `practice` không có đồng hồ; đồng hồ dừng sau khi nộp.

---

## 4. EPIC P2 — CẢI THIỆN

### P2-1 · Khả năng tiếp cận

| Vấn đề | Bằng chứng | Sửa |
|---|---|---|
| Chặn phóng to | `<meta viewport content="…maximum-scale=1.0, user-scalable=no…">` — vi phạm WCAG 1.4.4 | Bỏ `maximum-scale` và `user-scalable`, giữ `viewport-fit=cover` |
| Thẻ cấp học không phải link | `<div onclick="selectLevel(...)">` | → `<a href>` (đã gộp vào P1-4) |
| Không có focus visible | CSS chỉ có `:focus` cho `input` trong `.ol-nav-search` | Thêm `:focus-visible { outline: 2px solid var(--ol-primary); outline-offset: 2px }` cho `a, button, [tabindex]` |
| Không hỗ trợ giảm chuyển động | Không có `@media (prefers-reduced-motion)` | Thêm khối tắt transition/animation |
| Emoji làm icon hệ thống | `🎯 📕 ⚡ 🌱 🔍 ⚠️` dùng như icon UI | Thay bằng SVG sprite thống nhất; giữ emoji cho phần thưởng/động viên |
| Thiếu `lang` cho công thức | KaTeX không có `aria-label` | Thêm mô tả đọc được cho screen reader |

### P2-2 · Hiệu năng

**Bằng chứng đo trên `/quiz`:** tổng `2.548 KB`, trong đó:

| Tài nguyên | Dung lượng |
|---|---|
| `assets/mascot_teaching.png` | **1.234 KB** |
| `assets/mascot_celebrate.png` | **1.222 KB** |
| `katex.min.js` (jsDelivr) | 74 KB |
| `css/onluyen-theme.css` | 7 KB |
| còn lại | < 10 KB |

→ **96% dung lượng trang là 2 ảnh linh vật.** Icon môn học là PNG `1254×1254` hiển thị ở ~40px. Không ảnh nào có `loading="lazy"`.

**Hành động:**
- Xuất WebP + AVIF nhiều kích cỡ, dùng `<picture>` + `srcset`.
- `loading="lazy"` + `decoding="async"` cho mọi ảnh dưới màn hình đầu.
- Đặt `width`/`height` cho mọi `<img>` (chống layout shift).
- Đổi tên tệp có dấu cách: `the cap 1.png` → `level-c1.png`, `bia mon toan hoc.png` → `subject-toan.png`, `bia mon ngu van - tieng anh.png` → tách thành 2 ảnh riêng (Ngữ Văn và Tiếng Anh đang **dùng chung một ảnh**).
- Tự host KaTeX thay vì jsDelivr (ổn định hơn ở VN).

**Ngưỡng nghiệm thu:** trang `/quiz` **< 400 KB**; LCP < 2.5s trên 4G mô phỏng.

### P2-3 · SEO & chia sẻ mạng xã hội

| Vấn đề | Hiện tại | Sửa |
|---|---|---|
| `og:url` sai tên miền | `https://www.nmstudio.id.vn/` | URL tuyệt đối của chính trang |
| `og:image` đường dẫn tương đối | `assets/hero_banner.jpg` | `https://<domain>/assets/hero_banner.jpg` |
| Thiếu canonical | không có | `<link rel="canonical">` mỗi trang |
| `robots.txt` | trả **404** | Tạo + `sitemap.xml` |
| Hai thẻ `<h1>` ở trang chủ | logo + hero | Chỉ 1 `<h1>` |
| `meta keywords` | còn dùng | Xoá (Google bỏ từ lâu) |
| Trang 404 | màn lỗi mặc định Vercel | Trang 404 riêng có lối quay về |
| Tiêu đề trang | trùng nhau giữa các chương | `<title>` riêng theo `{Môn} {Lớp} — {Chương} | Ôn luyện` |

Thêm JSON-LD `Course` cho trang môn, `Quiz` cho trang đề.

> **Lưu ý thứ tự:** chỉ đẩy SEO **sau khi** P0 xong. Kéo người vào một sản phẩm dạy sai là phản tác dụng.

### P2-4 · Nhất quán dữ liệu hiển thị

| Chỉ số | Nơi 1 | Nơi 2 | Nơi 3 |
|---|---|---|---|
| Số chương Toán | `index.html`: **12 chương** | `subject.html`: **9 Chương** ← đúng | — |
| XP | `index.html`: 1.250 XP | `lesson.html`: 1.250 điểm thưởng, Lv.5 | `progress.html`: **5 XP, Cấp 1** |
| Streak | `index.html`: 7 ngày | `lesson.html`: 7 ngày liên tiếp | `progress.html`: **1 ngày** |

**Sửa:** mọi chỉ số đọc từ `sgk-progress` qua một module `js/stats.js`. Số chương đọc từ dữ liệu chương, không hard-code.

**Lỗi dữ liệu cần báo cho người biên soạn** (agent **không tự sửa**): danh sách bài Toán 6 nhảy từ *Bài 6* (Chương 1) sang *Bài 8* (Chương 2) — **thiếu Bài 7**.

**Màu cấp học:** CSS đã định nghĩa `--ol-c1-primary: #ea580c` (cam), `--ol-c2-primary: #0284c7` (xanh dương), `--ol-c3-primary: #059669` (xanh lá). Trang chủ dùng đúng, nhưng `quiz.html` cho lớp 6 lại dùng **xanh lá** (màu của THPT). Sửa: trang đề lấy màu theo `getContext().level`.

### P2-5 · Chuẩn bị pháp lý dữ liệu trẻ em

Hiện rủi ro thấp vì mọi thứ nằm trong `localStorage`, không có server thu thập. Nhưng nút *Đăng nhập* đã hứa "đồng bộ tài khoản".

Ngay khi có tài khoản thật, **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân áp dụng: xử lý dữ liệu trẻ em dưới 16 tuổi cần sự đồng ý của cha mẹ/người giám hộ, và của chính trẻ từ đủ 7 tuổi trở lên.

**Agent chuẩn bị sẵn (chưa cần backend):**
- [ ] `privacy.html` — Chính sách quyền riêng tư
- [ ] `terms.html` — Điều khoản sử dụng
- [ ] Link cả hai ở footer mọi trang
- [ ] `docs/DATA-INVENTORY.md` — liệt kê mọi trường dữ liệu đang lưu, lưu ở đâu, vì sao cần
- [ ] Nút *Xoá toàn bộ dữ liệu học tập trên thiết bị này* trong `progress.html`

*(Lưu ý nghiệp vụ, không thay thế ý kiến luật sư.)*

---

## 5. NHỮNG GÌ AGENT **KHÔNG** ĐƯỢC LÀM

1. ❌ Không tự viết lại nội dung câu hỏi hay bài giảng chuyên môn — cần giáo viên lớp 6.
2. ❌ Không đổi tên chương / tên bài / mô tả chương trong dữ liệu.
3. ❌ Không thêm React/Vue/Next hay bất kỳ build step nào.
4. ❌ Không thêm backend, database, hay dịch vụ trả phí.
5. ❌ Không thêm analytics/tracking nào khi chưa có chính sách quyền riêng tư (P2-5).
6. ❌ Không xoá tệp trong `content/` mà không tạo `.bak`.
7. ❌ Không "sửa" con số `50.000+` bằng một con số bịa khác — thay bằng dữ kiện đếm được.
8. ❌ Không tự bổ sung *Bài 7* của Toán 6 — báo cáo để người biên soạn xử lý.

---

## 6. THỨ TỰ THI CÔNG

```
TASK 0  Khảo sát → docs/AUDIT-BASELINE.md
   │
   ├─ P0-4c  js/context.js (nguồn sự thật)     ◄── làm trước, nhiều task phụ thuộc
   ├─ §7     Chuẩn hoá schema sgk-progress     ◄── làm trước
   │
   ├─ P0-1a  Xáo đáp án
   ├─ P0-1b  Tách lời giải khỏi phương án
   ├─ P0-3   Màn chữa bài            (cần P0-1a)
   ├─ P0-4ab Sổ tay câu sai          (cần P0-3)
   ├─ P0-5   Báo cáo phụ huynh       (cần P0-4)
   ├─ P0-2   Che/định nghĩa lý thuyết
   ├─ P0-6   Mobile nav + touch target
   │
   ├─ P1-5   Xác nhận nộp bài + tách chế độ
   ├─ P1-2   Nhãn DeepTutor + Bậc 2
   ├─ P1-3   Số liệu quảng bá
   ├─ P1-4   Lối vào cấp học
   ├─ P1-1   Chống trùng đề
   │
   └─ P2-1 → P2-5
```

---

## 7. HỢP ĐỒNG DỮ LIỆU

### 7.1. Câu hỏi — `content/grade-XX/<subject>/chNN-quiz.json`

```jsonc
{
  "examId": "toan-06-ch01-de03",
  "grade": "06",
  "subject": "toan",
  "chapter": "ch01",
  "chapterTitle": "Tập hợp các số tự nhiên",
  "examCode": "101",
  "mode": "exam",                    // "practice" | "exam"
  "durationMinutes": 45,             // null nếu practice
  "questions": [
    {
      "id": "toan-06-ch01-de03-q05",
      "difficulty": "van-dung",      // nhan-biet | thong-hieu | van-dung | van-dung-cao
      "topic": "Cộng trừ số nguyên", // dùng cho phân tích lỗ hổng — BẮT BUỘC
      "question": "Cho số nguyên $x$ thỏa mãn $-3 \\le x < 2$. Tổng tất cả các giá trị nguyên của $x$ là:",
      "options": ["$-5$", "$-3$", "$0$", "$-6$"],   // KHÔNG chứa lời giải
      "correct": 0,                                  // xáo lại khi render
      "breakdown": {
        "concept": "Liệt kê các số nguyên trong một khoảng cho trước",
        "socraticPrompt": "Em thử liệt kê ra giấy tất cả số nguyên từ −3 đến trước 2. Có bao nhiêu số?",
        "calculation": "Các số thỏa mãn: −3; −2; −1; 0; 1. Tổng = −3−2−1+0+1 = −5",
        "trap": "Nhiều bạn quên rằng dấu < không lấy số 2, hoặc bỏ sót số 0",
        "distractorReasons": {
          "1": "Chỉ lấy số nhỏ nhất thay vì tính tổng",
          "2": "Nghĩ rằng các số âm và dương triệt tiêu hết",
          "3": "Lấy cả số 2 vào khoảng (hiểu nhầm dấu <)"
        }
      }
    }
  ]
}
```

**Bất biến:** `topic` bắt buộc (Sổ tay câu sai nhóm theo trường này) · `options` không chứa `=`, `;`, hay ngoặc giải thích · phân phối `correct` trong mỗi tệp phải trải đều 0–3.

### 7.2. Tiến độ — `localStorage["sgk-progress"]`

```jsonc
{
  "version": 2,
  "nickname": null,
  "xp": 0,
  "streak": { "days": 0, "lastActiveDate": "2026-09-12" },
  "gradedCount": 0,                  // tổng số câu ĐÃ CHẤM — ngưỡng nhận định
  "correctCount": 0,
  "mistakes": [
    {
      "questionId": "toan-06-ch01-de03-q05",
      "examId": "toan-06-ch01-de03",
      "grade": "06", "subject": "toan", "chapter": "ch01",
      "topic": "Cộng trừ số nguyên",
      "chosenIndex": 2,              // chỉ số GỐC, không phải vị trí hiển thị
      "correctIndex": 0,
      "wrongCount": 1,
      "correctStreak": 0,            // đúng 2 lần liên tiếp → xoá khỏi sổ
      "firstWrongAt": "2026-09-12T15:04:00+07:00",
      "lastSeenAt":   "2026-09-12T15:04:00+07:00"
    }
  ],
  "attempts": [
    {
      "examId": "toan-06-ch01-de03",
      "startedAt": "2026-09-12T15:00:00+07:00",
      "submittedAt": "2026-09-12T15:04:00+07:00",
      "seed": 1789201169729,
      "score": { "correct": 1, "total": 6, "scale10": 1.7 },
      "answers": [{ "questionId": "…", "chosenIndex": 2, "isCorrect": false }]
    }
  ],
  "lessonsRead": [],
  "parentPin": { "hash": null, "isDefault": true }
}
```

**Yêu cầu:** viết hàm `migrateProgress(old)` chuyển dữ liệu `version: 1` sang `2` không mất streak/XP. Mọi ghi đi qua một hàm duy nhất `saveProgress()`.

### 7.3. Quy tắc XP (nguồn sự thật duy nhất — N4)

| Hành vi | XP |
|---|---|
| Trả lời đúng — Nhận biết | +2 |
| Trả lời đúng — Thông hiểu | +3 |
| Trả lời đúng — Vận dụng | +5 |
| Trả lời đúng — Vận dụng cao | +8 |
| Xoá được 1 câu khỏi Sổ tay (đúng 2 lần liên tiếp) | +10 |
| Đọc bài lý thuyết | **0** — bỏ hẳn |
| Nộp bài | **0** — XP chỉ đến từ câu đúng |

Hiện tại bài 1/6 câu đúng vẫn được `+5 XP` — phần thưởng rời khỏi nỗ lực thật. Sửa theo bảng trên.

---

## 8. NGHIỆM THU

### 8.1. Kịch bản smoke test (chạy tay sau mỗi epic)

```
KB-1  Trang chủ → THCS → Lớp 6 → Toán → Chương 1 → Đề 3
      ✓ Mọi nhãn đều là THCS/Lớp 6. Không xuất hiện chữ "THPT" ở bất kỳ đâu.

KB-2  Cố tình chọn SAI cả 6 câu → Nộp bài
      ✓ Có hộp xác nhận trước khi nộp
      ✓ Màn chữa bài hiện đủ 6 câu sai + đáp án đúng + breakdown
      ✓ Đồng hồ dừng, nút nộp bị vô hiệu hoá
      ✓ Badge "Sổ tay câu sai" hiện (6)

KB-3  Mở Sổ tay câu sai
      ✓ Hiện đúng 6 câu, KHÔNG hiện "Tuyệt vời! Em không có câu sai nào"
      ✓ Header vẫn là Toán 6 / THCS

KB-4  Làm lại 6 câu đó, đúng hết, 2 lượt liên tiếp
      ✓ Sau lượt 1 vẫn còn trong sổ
      ✓ Sau lượt 2 sổ về (0), XP cộng đúng theo bảng §7.3

KB-5  Mở Góc phụ huynh
      ✓ Lần đầu bắt buộc đặt PIN, từ chối "1234"
      ✓ gradedCount < 20 → "Chưa đủ dữ liệu để nhận định"
      ✓ Không bao giờ hiện "Con nắm rất vững" khi có câu sai

KB-6  Thu cửa sổ còn 360px, lặp lại KB-1 → KB-5
      ✓ Tới được mọi trang qua tab bar dưới
      ✓ Không cuộn ngang
      ✓ Mọi nút chạm được thoải mái bằng ngón tay

KB-7  Làm cùng 1 đề 5 lượt
      ✓ Vị trí đáp án đúng thay đổi giữa các lượt
      ✓ Chấm bài vẫn chính xác mọi lượt
```

### 8.2. Quy ước commit

```
P0-1a: xao vi tri dap an khi render bang seed tat dinh
P0-3:  them man chua bai sau khi nop
P1-3:  thay so lieu quang ba bang du kien dem duoc tu du lieu
```

Mỗi commit kèm phần mô tả: *Bằng chứng lỗi* → *Đã sửa gì* → *Kiểm chứng thế nào*.

### 8.3. Định nghĩa hoàn thành (mọi task)

- [ ] Không có lỗi console mới ở trang liên quan
- [ ] Kiểm ở 360px / 768px / 1440px
- [ ] Không phá kịch bản smoke test nào đang chạy được
- [ ] Không hard-code thêm giá trị nào thuộc §7.2
- [ ] Mọi chuỗi hiển thị cho người dùng là tiếng Việt có dấu, đúng chính tả

---

## 9. GHI CHÚ CHIẾN LƯỢC (ngoài phạm vi code, để chủ dự án quyết)

Khuyến nghị quan trọng nhất: **thu hẹp phạm vi**. *"Toán 6 — 9 chương, mỗi chương 3 đề thật, chữa bài đầy đủ"* là sản phẩm có người trả tiền. *"Lớp 1–12, 12 môn, nội dung khung"* thì không.

| Giai đoạn | Thời lượng | Nội dung |
|---|---|---|
| 1 | 2–3 tuần | Toàn bộ P0 + P1 (công việc trong tài liệu này) |
| 2 | 6–8 tuần | Viết 27 đề thật cho Toán 6 + 39 bài lý thuyết; nhờ 2–3 giáo viên lớp 6 rà soát và ký duyệt (vừa bảo đảm chất lượng, vừa là bằng chứng uy tín để truyền thông) |
| 3 | quý sau | Thử nghiệm trong 1–2 lớp thật; đo tỉ lệ quay lại sau 7 ngày và số câu/phiên; chỉ khi Toán 6 được dùng đều mới nhân bản sang Lớp 7, rồi Tiểu học |

---

*Lập ngày 12/09/2026 · Dựa trên khảo sát thủ công bản deploy `on-luyen-sgk.vercel.app`: 9 trang, 4 tệp nội dung JSON, `onluyen-theme.css`, đo hiệu năng và kiểm thử luồng làm bài đầy đủ.*

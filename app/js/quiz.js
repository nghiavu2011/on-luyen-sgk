// Engine bài tập sư phạm đa dạng hóa: Trắc nghiệm (MCQ) & Trả lời ngắn (Short Answer)
let currentQuiz = [];
let currentIndex = 0;
let score = 0;
let earnedXP = 0;

async function initQuiz() {
    const params = getUrlParams();
    try {
        let quizFile = `${params.chapter}-quiz.json`;
        if (params.exam && (params.exam === 'de1' || params.exam === 'de2')) {
            quizFile = `${params.chapter}-quiz-${params.exam}.json`;
        }
        let res = await smartFetch(`content/grade-${params.grade}/${params.subject}/${quizFile}`);
        if (!res.ok && quizFile !== `${params.chapter}-quiz.json`) {
            res = await smartFetch(`content/grade-${params.grade}/${params.subject}/${params.chapter}-quiz.json`);
        }
        if (!res.ok) throw new Error();
        const data = await res.json();
        currentQuiz = data.questions || [];
    } catch {
        currentQuiz = [
            {
                type: "multiple_choice",
                question: "Cách viết nào sau đây là đúng về kí hiệu phần tử thuộc tập hợp?",
                options: ["A. a ⊂ M", "B. a ∈ M", "C. a = M", "D. a { M }"],
                correctIndex: 1,
                hint: "Xem lại định nghĩa kí hiệu thuộc (∈) và không thuộc (∉).",
                explanation: "Khi phần tử a nằm trong tập hợp M, ta dùng kí hiệu thuộc là 'a ∈ M'. Kí hiệu ⊂ là quan hệ giữa tập hợp con với tập hợp.",
                pitfall: "Học sinh thường nhầm lẫn giữa kí hiệu 'thuộc' (∈) dành cho phần tử và 'tập con' (⊂) dành cho tập hợp.",
                difficulty: "easy"
            },
            {
                type: "short_answer",
                question: "Cho tập hợp B = {x ∈ N* | x < 5}. Hãy tính số phần tử của tập hợp B.",
                acceptedAnswers: ["4", "bốn"],
                hint: "Lưu ý tập N* là tập hợp các số tự nhiên khác 0 (bắt đầu từ số 1).",
                explanation: "Tập hợp B gồm các số tự nhiên khác 0 và nhỏ hơn 5 là: B = {1; 2; 3; 4}. Đếm số phần tử ta được 4 phần tử.",
                pitfall: "Quên mất N* không chứa số 0, dẫn đến đếm cả số 0 thành 5 phần tử.",
                difficulty: "medium"
            }
        ];
    }

    renderQuestion();
}

function getDifficultyLabel(diff) {
    switch (diff) {
        case 'easy': return { text: 'Nhận biết', cls: 'diff-easy' };
        case 'medium': return { text: 'Thông hiểu', cls: 'diff-medium' };
        case 'hard': return { text: 'Vận dụng', cls: 'diff-hard' };
        default: return { text: 'Rèn luyện', cls: 'diff-easy' };
    }
}

function renderQuestion() {
    if (currentIndex >= currentQuiz.length) return showResult();

    const q = currentQuiz[currentIndex];
    
    // Cập nhật Header
    document.getElementById('quiz-counter').innerText = `Câu ${currentIndex + 1}/${currentQuiz.length}`;
    document.getElementById('quiz-progress').style.width = `${(currentIndex / currentQuiz.length) * 100}%`;
    document.getElementById('current-score-xp').innerText = earnedXP;

    // Phân loại dạng bài
    const isShortAnswer = q.type === "short_answer" || (!q.options && q.acceptedAnswers);
    const typeBadge = document.getElementById('question-type-badge');
    typeBadge.innerText = isShortAnswer ? "✍️ Trả lời ngắn" : "🎯 Trắc nghiệm";
    typeBadge.className = isShortAnswer ? "badge-difficulty diff-medium" : "badge-difficulty diff-easy";

    // Mức độ nhận thức sư phạm
    const diffInfo = getDifficultyLabel(q.difficulty);
    const diffBadge = document.getElementById('difficulty-badge');
    diffBadge.innerText = diffInfo.text;
    diffBadge.className = `badge-difficulty ${diffInfo.cls}`;

    // Đề bài & Gợi ý
    document.getElementById('question-text').innerText = q.question;
    const hintBox = document.getElementById('hint-container');
    hintBox.classList.add('hidden');
    hintBox.innerText = q.hint || "Đọc kĩ định nghĩa và từ khóa trong câu hỏi.";

    // Không gian tương tác (Workspace)
    const workspace = document.getElementById('interactive-workspace');
    workspace.innerHTML = '';

    if (isShortAnswer) {
        workspace.innerHTML = `
            <div class="short-answer-box">
                <input type="text" id="short-input" class="short-answer-input" placeholder="Nhập đáp số của em..." autocomplete="off">
                <button class="btn btn-primary" onclick="submitShortAnswer()">Kiểm tra</button>
            </div>
        `;
        setTimeout(() => {
            const inp = document.getElementById('short-input');
            if (inp) inp.focus();
        }, 100);
    } else {
        const optsContainer = document.createElement('div');
        optsContainer.className = 'options-grid';
        let correctIdx = q.correctIndex;
        if (correctIdx === undefined && q.answer !== undefined) {
            if (typeof q.answer === 'number') {
                correctIdx = q.answer;
            } else {
                correctIdx = (q.options || []).findIndex(o => o.trim().toLowerCase() === String(q.answer).trim().toLowerCase());
            }
        }
        if (correctIdx === undefined || correctIdx < 0) correctIdx = 0;

        optsContainer.innerHTML = (q.options || []).map((opt, idx) => `
            <button class="modern-option-btn" onclick="selectAnswer(${idx}, ${correctIdx}, this)">
                <span style="display:inline-flex; width:28px; height:28px; border-radius:6px; background:rgba(255,255,255,0.06); align-items:center; justify-content:center; font-weight:700; color:var(--primary);">${String.fromCharCode(65 + idx)}</span>
                <span>${opt.replace(/^[A-D]\.\s*/, '')}</span>
            </button>
        `).join('');
        workspace.appendChild(optsContainer);
    }

    // Ẩn vùng phản hồi cũ
    document.getElementById('feedback-zone').classList.add('hidden');

    if (window.renderMathInElement) {
        renderMathInElement(document.getElementById('question-card'), {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }
}

function toggleHint() {
    const hintBox = document.getElementById('hint-container');
    hintBox.classList.toggle('hidden');
}

// Xử lý câu trả lời trắc nghiệm
function selectAnswer(selectedIdx, correctIdx, btn) {
    const isCorrect = selectedIdx === correctIdx;
    const allBtns = document.querySelectorAll('.option-btn');
    allBtns.forEach(b => b.disabled = true);

    if (isCorrect) {
        btn.classList.add('correct');
        handleEvaluation(true, 5);
    } else {
        btn.classList.add('wrong');
        if (allBtns[correctIdx]) allBtns[correctIdx].classList.add('correct');
        handleEvaluation(false, 1); // Vẫn khích lệ 1 XP vì đã nỗ lực làm bài
    }
}

// Xử lý trả lời ngắn / điền số
function submitShortAnswer() {
    const inputEl = document.getElementById('short-input');
    if (!inputEl) return;
    const userVal = inputEl.value.trim().toLowerCase();
    if (!userVal) {
        alert("Em hãy nhập câu trả lời trước khi bấm kiểm tra nhé!");
        return;
    }

    inputEl.disabled = true;
    const q = currentQuiz[currentIndex];
    const accepted = (q.acceptedAnswers || [q.answer]).map(a => String(a).trim().toLowerCase());

    const isCorrect = accepted.includes(userVal);
    if (isCorrect) {
        inputEl.style.borderColor = "var(--success)";
        inputEl.style.background = "rgba(16, 185, 129, 0.1)";
        handleEvaluation(true, 5);
    } else {
        inputEl.style.borderColor = "var(--danger)";
        inputEl.style.background = "rgba(239, 68, 68, 0.1)";
        handleEvaluation(false, 1);
    }
}

// Hiển thị phản hồi sư phạm 3 bước
function handleEvaluation(isCorrect, xpAmount) {
    const q = currentQuiz[currentIndex];
    earnedXP += xpAmount;
    if (isCorrect) score++;

    document.getElementById('current-score-xp').innerText = earnedXP;

    const feedbackTitle = document.getElementById('feedback-title');
    const feedbackXP = document.getElementById('feedback-xp');
    
    if (isCorrect) {
        feedbackTitle.innerText = '🎉 Rất chính xác!';
        feedbackTitle.className = 'text-success';
        feedbackXP.innerText = `+${xpAmount} XP`;
    } else {
        feedbackTitle.innerText = '💡 Cần lưu ý lại:';
        feedbackTitle.className = 'text-danger';
        feedbackXP.innerText = `+${xpAmount} XP (Khích lệ)`;
    }

    document.getElementById('solution-explanation').innerText = q.explanation || "Chưa có lời giải chi tiết cho câu hỏi này.";

    const pitfallBox = document.getElementById('pitfall-box');
    if (q.pitfall) {
        pitfallBox.classList.remove('hidden');
        document.getElementById('pitfall-text').innerText = q.pitfall;
    } else {
        pitfallBox.classList.add('hidden');
    }

    document.getElementById('feedback-zone').classList.remove('hidden');
    
    if (window.renderMathInElement) {
        renderMathInElement(document.getElementById('feedback-zone'), {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }

    // Tự động cuộn xuống nhẹ nhàng để học sinh đọc lời giải
    document.getElementById('feedback-zone').scrollIntoView({ behavior: 'smooth' });
}

function nextQuestion() {
    currentIndex++;
    renderQuestion();
}

function showResult() {
    document.getElementById('task-zone').classList.add('hidden');
    document.getElementById('feedback-zone').classList.add('hidden');
    document.getElementById('result-area').classList.remove('hidden');

    document.getElementById('quiz-progress').style.width = '100%';
    document.getElementById('final-score').innerText = `${score}/${currentQuiz.length}`;
    document.getElementById('earned-xp').innerText = earnedXP;

    addXP(earnedXP);

    // Lưu tiến độ vào LocalStorage
    const params = getUrlParams();
    const state = getState();
    const key = `${params.grade}/${params.subject}/${params.chapter}`;
    state.quizScores[key] = { score, total: currentQuiz.length, xp: earnedXP, date: new Date().toISOString() };
    saveState(state);
}

document.addEventListener('DOMContentLoaded', initQuiz);

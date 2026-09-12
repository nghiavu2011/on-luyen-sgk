import os

base_dir = r"d:\antigravity_scratch\real_estate_scoring\sql\SGK\app"
os.makedirs(base_dir, exist_ok=True)
os.makedirs(os.path.join(base_dir, "css"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "js"), exist_ok=True)

files = {}

files["index.html"] = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📚 Ôn Bài</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="manifest" href="manifest.json">
</head>
<body>
    <header class="app-header">
        <h1>📚 Ôn Bài</h1>
        <p class="tagline">Học tốt mỗi ngày!</p>
        <div class="stats-bar">
            <span class="streak">🔥 <span id="streak-count">0</span> ngày</span>
            <span class="xp">⭐ <span id="xp-count">0</span> XP</span>
        </div>
    </header>

    <main class="container">
        <section id="grade-selection">
            <h2>Chọn Lớp</h2>
            <div class="grid-2">
                <div class="card grade-card" onclick="selectGrade('06')">
                    <h3>Lớp 6</h3>
                    <p>THCS</p>
                </div>
                <div class="card grade-card" onclick="selectGrade('11')">
                    <h3>Lớp 11</h3>
                    <p>THPT</p>
                </div>
            </div>
        </section>

        <section id="subject-selection" class="hidden">
            <h2>Chọn Môn Học</h2>
            <button onclick="goBack()" class="btn btn-secondary mb-3">⬅ Quay lại</button>
            <div class="grid-3" id="subject-grid">
                <!-- Subjects will be populated here -->
            </div>
        </section>
    </main>

    <nav class="bottom-nav">
        <a href="index.html" class="active">🏠 Trang chủ</a>
        <a href="progress.html">📊 Tiến độ</a>
        <a href="parent.html">👨‍👩‍👧 Phụ huynh</a>
    </nav>

    <script src="js/app.js"></script>
    <script>
        function selectGrade(grade) {
            document.getElementById('grade-selection').classList.add('hidden');
            document.getElementById('subject-selection').classList.remove('hidden');
            renderSubjects(grade);
        }

        function goBack() {
            document.getElementById('subject-selection').classList.add('hidden');
            document.getElementById('grade-selection').classList.remove('hidden');
        }

        function renderSubjects(grade) {
            const grid = document.getElementById('subject-grid');
            const subjects = [
                {id: 'toan', name: 'Toán', icon: '🔢'},
                {id: 'ngu-van', name: 'Ngữ Văn', icon: '📖'},
                {id: 'tieng-anh', name: 'Tiếng Anh', icon: '🇬🇧'}
            ];
            grid.innerHTML = subjects.map(s => `
                <a href="subject.html?grade=${grade}&subject=${s.id}" class="card subject-card">
                    <div class="subject-icon">${s.icon}</div>
                    <h4>${s.name}</h4>
                </a>
            `).join('');
        }
        
        document.addEventListener('DOMContentLoaded', updateStats);
    </script>
</body>
</html>"""

files["subject.html"] = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Môn học - 📚 Ôn Bài</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="app-header">
        <div class="header-nav">
            <button onclick="window.location.href='index.html'" class="btn-icon">⬅</button>
            <h1 id="subject-title">Môn học</h1>
        </div>
    </header>

    <main class="container" id="chapter-list">
        <div class="loading">Đang tải...</div>
    </main>

    <script src="js/app.js"></script>
    <script>
        async function init() {
            const params = getUrlParams();
            if (!params.grade || !params.subject) return window.location.href = 'index.html';
            
            document.getElementById('subject-title').innerText = params.subject.toUpperCase();
            const container = document.getElementById('chapter-list');
            
            try {
                const res = await fetch(`../content/grade-${params.grade}/${params.subject}/chapters.json`);
                if (!res.ok) throw new Error('Not found');
                const data = await res.json();
                
                container.innerHTML = data.chapters.map(ch => `
                    <div class="card chapter-card">
                        <h3>${ch.title}</h3>
                        <p>${ch.lessons ? ch.lessons.length : 0} bài học</p>
                        <div class="chapter-actions">
                            <a href="lesson.html?grade=${params.grade}&subject=${params.subject}&chapter=${ch.id}" class="btn btn-primary">📖 Bài giảng</a>
                            <a href="quiz.html?grade=${params.grade}&subject=${params.subject}&chapter=${ch.id}" class="btn btn-accent">📝 Quiz</a>
                            <a href="flashcard.html?grade=${params.grade}&subject=${params.subject}&chapter=${ch.id}" class="btn btn-secondary">🎴 Flashcard</a>
                        </div>
                    </div>
                `).join('');
            } catch (e) {
                container.innerHTML = `<div class="error">Không tìm thấy dữ liệu. Vui lòng kiểm tra lại.</div>
                <div class="card chapter-card">
                    <h3>Chương 1 (Demo)</h3>
                    <div class="chapter-actions">
                        <a href="lesson.html?grade=${params.grade}&subject=${params.subject}&chapter=ch01" class="btn btn-primary">📖 Bài giảng</a>
                        <a href="quiz.html?grade=${params.grade}&subject=${params.subject}&chapter=ch01" class="btn btn-accent">📝 Quiz</a>
                        <a href="flashcard.html?grade=${params.grade}&subject=${params.subject}&chapter=ch01" class="btn btn-secondary">🎴 Flashcard</a>
                    </div>
                </div>`;
            }
        }
        init();
    </script>
</body>
</html>"""

files["lesson.html"] = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài học - 📚 Ôn Bài</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="app-header">
        <div class="header-nav">
            <button onclick="history.back()" class="btn-icon">⬅</button>
            <h1>Bài học</h1>
        </div>
    </header>

    <main class="container lesson-container">
        <div id="lesson-content">
            <div class="loading">Đang tải...</div>
        </div>
        
        <div class="lesson-navigation">
            <button class="btn btn-secondary">⬅ Bài trước</button>
            <button class="btn btn-success" onclick="markCompleted()">Hoàn thành ✔</button>
            <button class="btn btn-primary">Bài tiếp ➡</button>
        </div>
    </main>

    <script src="js/app.js"></script>
    <script>
        function markCompleted() {
            addXP(10);
            alert('Đã hoàn thành! +10 XP');
            history.back();
        }
        
        async function init() {
            const content = document.getElementById('lesson-content');
            content.innerHTML = `
                <h2>Nội dung bài học</h2>
                <div class="summary-box">
                    <ul>
                        <li>Điểm quan trọng 1</li>
                        <li>Điểm quan trọng 2</li>
                    </ul>
                </div>
                <div class="formula-box">
                    <strong>Công thức:</strong> E = mc²
                </div>
                <p>Ví dụ minh họa chi tiết...</p>
            `;
        }
        init();
    </script>
</body>
</html>"""

files["quiz.html"] = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz - 📚 Ôn Bài</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="app-header">
        <div class="header-nav">
            <button onclick="history.back()" class="btn-icon">✖</button>
            <div class="progress-container">
                <div class="progress-bar" id="quiz-progress" style="width: 0%"></div>
            </div>
            <span id="quiz-counter">1/10</span>
        </div>
    </header>

    <main class="container quiz-container">
        <div id="quiz-area">
            <h2 id="question-text" class="question-text">Đang tải câu hỏi...</h2>
            <div id="options-container" class="options-grid"></div>
        </div>
        
        <div id="feedback-area" class="hidden">
            <h3 id="feedback-title"></h3>
            <p id="feedback-explanation"></p>
            <button class="btn btn-primary w-100" onclick="nextQuestion()">Tiếp tục ➡</button>
        </div>
        
        <div id="result-area" class="hidden text-center">
            <h2>Kết quả</h2>
            <div class="score-circle" id="final-score">0/0</div>
            <p>Đã nhận được <strong id="earned-xp">0</strong> XP!</p>
            <button class="btn btn-primary" onclick="history.back()">Hoàn thành</button>
        </div>
    </main>

    <script src="js/app.js"></script>
    <script src="js/quiz.js"></script>
</body>
</html>"""

files["flashcard.html"] = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flashcard - 📚 Ôn Bài</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="app-header">
        <div class="header-nav">
            <button onclick="history.back()" class="btn-icon">✖</button>
            <h1>Flashcard <span id="fc-counter">(1/1)</span></h1>
        </div>
    </header>

    <main class="container fc-container">
        <div class="scene">
            <div class="card flashcard" id="flashcard" onclick="flipCard()">
                <div class="card__face card__face--front" id="fc-front">
                    Mặt trước
                </div>
                <div class="card__face card__face--back" id="fc-back">
                    Mặt sau
                </div>
            </div>
        </div>
        
        <div class="fc-controls mt-4">
            <button class="btn btn-danger" onclick="markCard(false)">Chưa nhớ ✖</button>
            <button class="btn btn-success" onclick="markCard(true)">Đã nhớ ✔</button>
        </div>
    </main>

    <script src="js/app.js"></script>
    <script src="js/flashcard.js"></script>
</body>
</html>"""

files["progress.html"] = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tiến độ - 📚 Ôn Bài</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="app-header">
        <h1>📊 Tiến độ học tập</h1>
    </header>

    <main class="container">
        <div class="card">
            <h2>Thống kê tổng quan</h2>
            <div class="grid-2 text-center mt-3">
                <div class="stat-box">
                    <div class="stat-value text-accent" id="prog-xp">0</div>
                    <div class="stat-label">Tổng XP</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value text-danger" id="prog-streak">0</div>
                    <div class="stat-label">Ngày chuỗi</div>
                </div>
            </div>
        </div>
        
        <div class="card mt-3">
            <h2>Môn học</h2>
            <div id="subject-progress">
                <p>Chưa có dữ liệu học tập.</p>
            </div>
        </div>
    </main>

    <nav class="bottom-nav">
        <a href="index.html">🏠 Trang chủ</a>
        <a href="progress.html" class="active">📊 Tiến độ</a>
        <a href="parent.html">👨‍👩‍👧 Phụ huynh</a>
    </nav>

    <script src="js/app.js"></script>
    <script src="js/progress.js"></script>
</body>
</html>"""

files["parent.html"] = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phụ huynh - 📚 Ôn Bài</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header class="app-header">
        <h1>👨‍👩‍👧 Dành cho Phụ huynh</h1>
    </header>

    <main class="container">
        <div id="pin-screen" class="card text-center">
            <h2>Nhập mã PIN</h2>
            <p>Mã mặc định: 1234</p>
            <input type="password" id="pin-input" class="pin-input" maxlength="4">
            <button class="btn btn-primary mt-3 w-100" onclick="checkPin()">Xác nhận</button>
            <p id="pin-error" class="text-danger mt-2 hidden">Mã PIN sai!</p>
        </div>
        
        <div id="parent-dashboard" class="hidden">
            <div class="card">
                <h2>Hoạt động gần đây</h2>
                <p>Thời gian học hôm nay: <strong>45 phút</strong></p>
                <div class="progress-container mt-2 mb-3">
                    <div class="progress-bar bg-success" style="width: 75%"></div>
                </div>
                <h3>Điểm mạnh:</h3>
                <p class="text-success">Toán học, Tiếng Anh</p>
                <h3 class="mt-2">Cần cải thiện:</h3>
                <p class="text-danger">Ngữ Văn</p>
            </div>
            <button class="btn btn-secondary w-100 mt-3" onclick="logout()">Thoát</button>
        </div>
    </main>

    <nav class="bottom-nav">
        <a href="index.html">🏠 Trang chủ</a>
        <a href="progress.html">📊 Tiến độ</a>
        <a href="parent.html" class="active">👨‍👩‍👧 Phụ huynh</a>
    </nav>

    <script src="js/app.js"></script>
    <script>
        function checkPin() {
            if (document.getElementById('pin-input').value === '1234') {
                document.getElementById('pin-screen').classList.add('hidden');
                document.getElementById('parent-dashboard').classList.remove('hidden');
            } else {
                document.getElementById('pin-error').classList.remove('hidden');
            }
        }
        function logout() {
            document.getElementById('pin-input').value = '';
            document.getElementById('parent-dashboard').classList.add('hidden');
            document.getElementById('pin-screen').classList.remove('hidden');
        }
    </script>
</body>
</html>"""


files["css/style.css"] = """
:root {
    --primary: #4F46E5;
    --primary-hover: #4338CA;
    --accent: #F59E0B;
    --success: #10B981;
    --danger: #EF4444;
    --bg-color: #F3F4F6;
    --card-bg: #FFFFFF;
    --text-main: #1F2937;
    --text-muted: #6B7280;
    --border: #E5E7EB;
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg-color: #111827;
        --card-bg: #1F2937;
        --text-main: #F9FAFB;
        --text-muted: #9CA3AF;
        --border: #374151;
    }
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: system-ui, -apple-system, sans-serif;
    background-color: var(--bg-color);
    color: var(--text-main);
    line-height: 1.5;
    padding-bottom: 70px;
}

/* Typography */
h1, h2, h3, h4 { margin-bottom: 0.5rem; }
a { text-decoration: none; color: inherit; }

/* Layout */
.container { padding: 1rem; max-width: 600px; margin: 0 auto; }
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.grid-3 { display: grid; grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); gap: 1rem; }
.mt-2 { margin-top: 0.5rem; }
.mt-3 { margin-top: 1rem; }
.mt-4 { margin-top: 1.5rem; }
.mb-3 { margin-bottom: 1rem; }
.w-100 { width: 100%; }
.text-center { text-align: center; }
.hidden { display: none !important; }

/* Header */
.app-header {
    background-color: var(--primary);
    color: white;
    padding: 1rem;
    text-align: center;
    position: sticky;
    top: 0;
    z-index: 10;
}
.header-nav { display: flex; align-items: center; justify-content: space-between; }
.header-nav h1 { font-size: 1.25rem; margin: 0; flex: 1; text-align: center; }
.stats-bar {
    display: flex; justify-content: center; gap: 1rem;
    background: rgba(255,255,255,0.2);
    border-radius: 20px;
    padding: 0.25rem 1rem;
    margin-top: 0.5rem;
    font-size: 0.9rem;
    font-weight: bold;
}

/* Cards */
.card {
    background: var(--card-bg);
    border-radius: 12px;
    padding: 1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border: 1px solid var(--border);
}
.grade-card { text-align: center; cursor: pointer; transition: transform 0.2s; }
.grade-card:hover { transform: translateY(-2px); border-color: var(--primary); }
.subject-card { text-align: center; display: block; }
.subject-icon { font-size: 2.5rem; margin-bottom: 0.5rem; }

/* Buttons */
.btn {
    display: inline-block;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    border: none;
    font-weight: 600;
    cursor: pointer;
    text-align: center;
    transition: opacity 0.2s;
}
.btn:active { opacity: 0.8; }
.btn-primary { background: var(--primary); color: white; }
.btn-secondary { background: var(--border); color: var(--text-main); }
.btn-accent { background: var(--accent); color: white; }
.btn-success { background: var(--success); color: white; }
.btn-danger { background: var(--danger); color: white; }
.btn-icon { background: none; border: none; color: white; font-size: 1.5rem; cursor: pointer; }

/* Progress */
.progress-container {
    background: rgba(0,0,0,0.2);
    border-radius: 10px;
    height: 8px;
    flex: 1;
    margin: 0 1rem;
    overflow: hidden;
}
.app-header .progress-container { background: rgba(255,255,255,0.3); }
.progress-bar { background: var(--accent); height: 100%; transition: width 0.3s ease; }
.bg-success { background: var(--success) !important; }

/* Bottom Nav */
.bottom-nav {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    background: var(--card-bg);
    display: flex;
    justify-content: space-around;
    padding: 0.75rem 0;
    border-top: 1px solid var(--border);
    box-shadow: 0 -1px 3px rgba(0,0,0,0.05);
}
.bottom-nav a {
    text-align: center;
    font-size: 0.8rem;
    color: var(--text-muted);
    flex: 1;
}
.bottom-nav a.active { color: var(--primary); font-weight: bold; }

/* Subject/Chapter */
.chapter-card { margin-bottom: 1rem; }
.chapter-actions { display: flex; gap: 0.5rem; margin-top: 1rem; flex-wrap: wrap; }
.chapter-actions .btn { flex: 1; min-width: 100px; padding: 0.5rem; font-size: 0.9rem; }

/* Lesson */
.summary-box { background: rgba(79, 70, 229, 0.1); padding: 1rem; border-left: 4px solid var(--primary); border-radius: 0 8px 8px 0; margin: 1rem 0; }
.formula-box { background: rgba(245, 158, 11, 0.1); padding: 1rem; border: 1px dashed var(--accent); border-radius: 8px; margin: 1rem 0; text-align: center; font-size: 1.1rem;}
.lesson-navigation { display: flex; justify-content: space-between; margin-top: 2rem; }

/* Quiz */
.options-grid { display: grid; gap: 0.75rem; margin-top: 1.5rem; }
.option-btn {
    background: var(--card-bg);
    border: 2px solid var(--border);
    padding: 1rem;
    border-radius: 8px;
    text-align: left;
    font-size: 1rem;
    cursor: pointer;
    color: var(--text-main);
}
.option-btn.correct { background: var(--success); color: white; border-color: var(--success); animation: bounce 0.5s; }
.option-btn.wrong { background: var(--danger); color: white; border-color: var(--danger); animation: shake 0.5s; }
.score-circle {
    width: 120px; height: 120px;
    border-radius: 50%;
    background: var(--primary);
    color: white;
    display: flex; align-items: center; justify-content: center;
    font-size: 2rem; font-weight: bold;
    margin: 2rem auto;
}

/* Flashcard */
.scene { width: 100%; height: 300px; perspective: 1000px; }
.card.flashcard {
    width: 100%; height: 100%;
    position: relative;
    transition: transform 0.6s;
    transform-style: preserve-3d;
    cursor: pointer;
    padding: 0;
    border: none;
    box-shadow: none;
    background: transparent;
}
.card.flashcard.is-flipped { transform: rotateY(180deg); }
.card__face {
    position: absolute;
    width: 100%; height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    display: flex; align-items: center; justify-content: center;
    padding: 2rem;
    text-align: center;
    border-radius: 16px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    font-size: 1.25rem;
    background: var(--card-bg);
    border: 1px solid var(--border);
}
.card__face--back { transform: rotateY(180deg); background: rgba(79, 70, 229, 0.05); }
.fc-controls { display: flex; gap: 1rem; justify-content: center; }
.fc-controls .btn { flex: 1; max-width: 150px; }

/* Parent */
.pin-input { font-size: 2rem; text-align: center; letter-spacing: 0.5rem; width: 150px; padding: 0.5rem; margin: 1rem auto; display: block; border: 1px solid var(--border); border-radius: 8px; background: var(--bg-color); color: var(--text-main); }
.text-danger { color: var(--danger); }
.text-success { color: var(--success); }
.text-accent { color: var(--accent); }
.stat-box { background: var(--bg-color); padding: 1rem; border-radius: 8px; }
.stat-value { font-size: 1.5rem; font-weight: bold; }

/* Animations */
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}
@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
}
"""

files["js/app.js"] = """
// Core utilities
const STATE_KEY = 'sgk-progress';

function getUrlParams() {
    const params = new URLSearchParams(window.location.search);
    return Object.fromEntries(params.entries());
}

function getState() {
    const defaultState = {
        xp: 0,
        streak: 0,
        lastLogin: null,
        completedLessons: [],
        quizScores: {}
    };
    try {
        const stored = localStorage.getItem(STATE_KEY);
        return stored ? JSON.parse(stored) : defaultState;
    } catch {
        return defaultState;
    }
}

function saveState(state) {
    localStorage.setItem(STATE_KEY, JSON.stringify(state));
}

function addXP(amount) {
    const state = getState();
    state.xp += amount;
    saveState(state);
    updateStats();
}

function updateStats() {
    const state = getState();
    const xpEl = document.getElementById('xp-count');
    const streakEl = document.getElementById('streak-count');
    
    // Streak logic
    const today = new Date().toDateString();
    if (state.lastLogin !== today) {
        if (state.lastLogin === new Date(Date.now() - 86400000).toDateString()) {
            state.streak += 1;
        } else if (state.lastLogin) {
            state.streak = 1;
        } else {
            state.streak = 1;
        }
        state.lastLogin = today;
        saveState(state);
    }
    
    if (xpEl) xpEl.innerText = state.xp;
    if (streakEl) streakEl.innerText = state.streak;
}

// init on load
document.addEventListener('DOMContentLoaded', updateStats);
"""

files["js/quiz.js"] = """
let currentQuiz = [];
let currentIndex = 0;
let score = 0;

const mockQuiz = [
    { q: "1 + 1 = ?", options: ["1", "2", "3", "4"], answer: 1, explanation: "Một cộng một bằng hai." },
    { q: "Thủ đô của Việt Nam?", options: ["Hà Nội", "Hồ Chí Minh", "Đà Nẵng", "Huế"], answer: 0, explanation: "Hà Nội là thủ đô của VN." }
];

async function initQuiz() {
    // Attempt fetch, fallback to mock
    try {
        const params = getUrlParams();
        const res = await fetch(`../content/grade-${params.grade}/${params.subject}/quiz-${params.chapter}.json`);
        if (!res.ok) throw new Error();
        const data = await res.json();
        currentQuiz = data.questions || mockQuiz;
    } catch {
        currentQuiz = mockQuiz;
    }
    
    renderQuestion();
}

function renderQuestion() {
    if (currentIndex >= currentQuiz.length) return showResult();
    
    const q = currentQuiz[currentIndex];
    document.getElementById('question-text').innerText = q.q || q.question;
    document.getElementById('quiz-counter').innerText = `${currentIndex + 1}/${currentQuiz.length}`;
    document.getElementById('quiz-progress').style.width = `${((currentIndex) / currentQuiz.length) * 100}%`;
    
    const optsContainer = document.getElementById('options-container');
    const opts = q.options || q.choices;
    const ansIdx = q.answer !== undefined ? q.answer : q.correctIndex;
    
    optsContainer.innerHTML = opts.map((opt, idx) => `
        <button class="option-btn" onclick="selectAnswer(${idx}, ${ansIdx}, this)">${opt}</button>
    `).join('');
    
    document.getElementById('feedback-area').classList.add('hidden');
}

function selectAnswer(selectedIdx, correctIdx, btn) {
    const isCorrect = selectedIdx === correctIdx;
    
    const allBtns = document.querySelectorAll('.option-btn');
    allBtns.forEach(b => b.disabled = true);
    
    if (isCorrect) {
        btn.classList.add('correct');
        score++;
        document.getElementById('feedback-title').innerText = '🎉 Chính xác!';
        document.getElementById('feedback-title').className = 'text-success';
    } else {
        btn.classList.add('wrong');
        allBtns[correctIdx].classList.add('correct');
        document.getElementById('feedback-title').innerText = '❌ Sai rồi!';
        document.getElementById('feedback-title').className = 'text-danger';
    }
    
    const q = currentQuiz[currentIndex];
    document.getElementById('feedback-explanation').innerText = q.explanation || "Không có giải thích.";
    document.getElementById('feedback-area').classList.remove('hidden');
}

function nextQuestion() {
    currentIndex++;
    renderQuestion();
}

function showResult() {
    document.getElementById('quiz-area').classList.add('hidden');
    document.getElementById('feedback-area').classList.add('hidden');
    document.getElementById('result-area').classList.remove('hidden');
    
    document.getElementById('quiz-progress').style.width = '100%';
    document.getElementById('final-score').innerText = `${score}/${currentQuiz.length}`;
    
    const xp = score * 5;
    document.getElementById('earned-xp').innerText = xp;
    addXP(xp);
}

document.addEventListener('DOMContentLoaded', initQuiz);
"""

files["js/flashcard.js"] = """
let cards = [];
let currentCard = 0;

const mockCards = [
    { front: "Apple", back: "Quả táo" },
    { front: "Dog", back: "Con chó" },
    { front: "Cat", back: "Con mèo" }
];

async function initFlashcards() {
    try {
        const params = getUrlParams();
        const res = await fetch(`../content/grade-${params.grade}/${params.subject}/flashcards-${params.chapter}.json`);
        if (!res.ok) throw new Error();
        const data = await res.json();
        cards = data.cards || mockCards;
    } catch {
        cards = mockCards;
    }
    
    renderCard();
}

function renderCard() {
    if (cards.length === 0) return;
    if (currentCard >= cards.length) {
        alert("Bạn đã ôn xong bộ thẻ này! +10 XP");
        addXP(10);
        history.back();
        return;
    }
    
    document.getElementById('flashcard').classList.remove('is-flipped');
    
    const c = cards[currentCard];
    document.getElementById('fc-front').innerText = c.front;
    document.getElementById('fc-back').innerText = c.back;
    
    document.getElementById('fc-counter').innerText = `(${currentCard + 1}/${cards.length})`;
}

function flipCard() {
    document.getElementById('flashcard').classList.toggle('is-flipped');
}

function markCard(known) {
    if (known) addXP(1); // 1 xp per card
    currentCard++;
    setTimeout(renderCard, 300); // Wait for transition if needed
}

document.addEventListener('DOMContentLoaded', initFlashcards);
"""

files["js/progress.js"] = """
function loadProgress() {
    const state = getState();
    document.getElementById('prog-xp').innerText = state.xp;
    document.getElementById('prog-streak').innerText = state.streak;
}
document.addEventListener('DOMContentLoaded', loadProgress);
"""

files["js/spaced-repetition.js"] = """
// Simple SM-2 implementation
function calculateSM2(quality, repetitions, easiness, interval) {
    if (quality < 3) {
        repetitions = 0;
        interval = 1;
    } else {
        if (repetitions === 0) interval = 1;
        else if (repetitions === 1) interval = 6;
        else interval = Math.round(interval * easiness);
        repetitions++;
    }
    
    easiness = easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02));
    if (easiness < 1.3) easiness = 1.3;
    
    return { repetitions, easiness, interval };
}
"""

files["manifest.json"] = """{
  "name": "Ôn Bài",
  "short_name": "Ôn Bài",
  "description": "Ứng dụng ôn tập SGK nhanh chóng và hiệu quả",
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "#F3F4F6",
  "theme_color": "#4F46E5",
  "icons": [
    {
      "src": "data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📚</text></svg>",
      "sizes": "192x192",
      "type": "image/svg+xml"
    }
  ]
}"""

for filename, content in files.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully created {len(files)} files in {base_dir}")

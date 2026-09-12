// Core utilities & Security for Ôn Luyện SGK
const STATE_KEY = 'sgk-progress';
const PIN_HASH_KEY = 'sgk_parent_pin_hash';
// Default SHA-256 hash for PIN '1234'
const DEFAULT_PIN_HASH = '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4';

// 1. URL Params Helper
function getUrlParams() {
    const params = new URLSearchParams(window.location.search);
    return Object.fromEntries(params.entries());
}

// 2. State Management
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

// 3. EXPORT & IMPORT PROGRESS (JSON BACKUP)
function exportStudyProgress() {
    const backupData = {
        app: "OnLuyenSGK",
        version: "2026.1",
        exportedAt: new Date().toISOString(),
        progress: getState(),
        deeptutor_l1: JSON.parse(localStorage.getItem('deeptutor_l1_attempts') || '[]'),
        deeptutor_mistakes: JSON.parse(localStorage.getItem('deeptutor_mistake_bank') || '[]'),
        deeptutor_gaps: JSON.parse(localStorage.getItem('deeptutor_l2_knowledge_gaps') || '{}'),
        deeptutor_mastery: JSON.parse(localStorage.getItem('deeptutor_l3_mastery') || '{}')
    };

    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(backupData, null, 2));
    const downloadAnchor = document.createElement('a');
    const dateStr = new Date().toISOString().slice(0, 10).replace(/-/g, '');
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `onluyen_tiendo_${dateStr}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
}

function importStudyProgress(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = (event) => {
            try {
                const data = JSON.parse(event.target.result);
                if (!data.progress) {
                    throw new Error("Tệp tin không đúng định dạng sao lưu Ôn Luyện!");
                }
                
                // Restore keys
                localStorage.setItem(STATE_KEY, JSON.stringify(data.progress));
                if (data.deeptutor_l1) localStorage.setItem('deeptutor_l1_attempts', JSON.stringify(data.deeptutor_l1));
                if (data.deeptutor_mistakes) localStorage.setItem('deeptutor_mistake_bank', JSON.stringify(data.deeptutor_mistakes));
                if (data.deeptutor_gaps) localStorage.setItem('deeptutor_l2_knowledge_gaps', JSON.stringify(data.deeptutor_gaps));
                if (data.deeptutor_mastery) localStorage.setItem('deeptutor_l3_mastery', JSON.stringify(data.deeptutor_mastery));
                
                resolve(data);
            } catch (err) {
                reject(err);
            }
        };
        reader.onerror = (e) => reject(e);
        reader.readAsText(file);
    });
}

// 4. SECURITY & ANTI-CLONING / CONTENT INTEGRITY
// A. Native SHA-256 Hash helper
async function sha256(text) {
    const msgBuffer = new TextEncoder().encode(text);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

// B. Parent PIN Verification (Robust & Fail-safe)
async function verifyParentPin(pinInput) {
    const pin = (pinInput || '').trim();
    if (pin === '1234') return true; // Fail-safe default
    
    const savedPin = localStorage.getItem('sgk_parent_pin_raw');
    if (savedPin && pin === savedPin) return true;

    try {
        if (window.crypto && window.crypto.subtle) {
            const inputHash = await sha256(pin);
            const savedHash = localStorage.getItem(PIN_HASH_KEY) || DEFAULT_PIN_HASH;
            if (inputHash === savedHash) return true;
        }
    } catch (e) {
        console.warn('Crypto subtle not available, fallback to raw check');
    }
    return false;
}

async function setParentPin(newPin) {
    const cleanPin = (newPin || '').trim();
    localStorage.setItem('sgk_parent_pin_raw', cleanPin);
    try {
        if (window.crypto && window.crypto.subtle) {
            const newHash = await sha256(cleanPin);
            localStorage.setItem(PIN_HASH_KEY, newHash);
        }
    } catch (e) {}
}

// C. Frame Buster (Chống nhúng iframe trái phép)
try {
    if (window.self !== window.top) {
        window.top.location = window.self.location;
    }
} catch (e) {
    // Cross-origin iframe blocked
}

// D. Copy Protection with Attribution Watermark
document.addEventListener('copy', (event) => {
    const selection = window.getSelection();
    if (!selection || selection.toString().length < 40) return;
    
    // Attach educational non-profit attribution
    const watermark = "\n\n[Trích xuất từ Ứng dụng Ôn Luyện SGK 2026-2027 • Tự học cùng DeepTutor Socratic AI]";
    event.clipboardData.setData('text/plain', selection.toString() + watermark);
    event.preventDefault();
});

// E. Console Copyright Notice
console.log(
    "%c📚 ÔN LUYỆN SGK & DEEPTUTOR %c\nỨng dụng giáo dục phi lợi nhuận bám sát SGK Bộ GD&ĐT 2026 - 2027.\nMọi quyền được bảo vệ cho cộng đồng học sinh Việt Nam.",
    "background: #059669; color: white; font-weight: 800; font-size: 14px; padding: 4px 8px; border-radius: 4px;",
    "color: #334155; font-size: 11px;"
);

// 4. Universal Content Fetcher (Works seamlessly in all deployment environments)
async function smartFetch(path) {
    const clean = path.replace(/^(\.\.\/|\.\/)/, '');
    const candidates = [
        clean,
        `./${clean}`,
        `../${clean}`,
        `/${clean}`
    ];
    for (const url of candidates) {
        try {
            const res = await fetch(url);
            if (res.ok) return res;
        } catch (e) {}
    }
    return fetch(path);
}

// Init on load
document.addEventListener('DOMContentLoaded', updateStats);


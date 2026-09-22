// Core utilities & Security for Ôn Luyện SGK
var STATE_KEY = window.STATE_KEY || 'sgk-progress';
var PIN_HASH_KEY = window.PIN_HASH_KEY || 'sgk_parent_pin_hash';
// Default SHA-256 hash for PIN '1234'
var DEFAULT_PIN_HASH = window.DEFAULT_PIN_HASH || '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4';

// 0. XSS Prevention & Sanitization Helpers (Alibaba OCR Standards)
function escapeHTML(str) {
    if (str === null || str === undefined) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}
window.escapeHTML = escapeHTML;

function sanitizeGrade(grade) {
    if (!grade) return '06';
    const clean = String(grade).replace(/[^0-9]/g, '');
    const num = parseInt(clean, 10);
    if (isNaN(num) || num < 1 || num > 12) return '06';
    return String(num).padStart(2, '0');
}
window.sanitizeGrade = sanitizeGrade;

function sanitizeSubject(subject) {
    if (!subject) return 'toan';
    const clean = String(subject).toLowerCase().replace(/[^a-z0-9_-]/g, '');
    return clean || 'toan';
}
window.sanitizeSubject = sanitizeSubject;

function sanitizeParam(val, fallback) {
    if (fallback === undefined) fallback = '';
    if (val === null || val === undefined) return fallback;
    return String(val).replace(/[<>"'&]/g, '').trim();
}
window.sanitizeParam = sanitizeParam;

// 1. URL Params Helper
function getUrlParams() {
    const params = new URLSearchParams(window.location.search);
    const result = {};
    for (const [key, value] of params.entries()) {
        result[key] = sanitizeParam(value);
    }
    return result;
}

// 2. State Management (Ủy quyền thống nhất cho stats.js v2 - Single Source of Truth)
function getState() {
    if (typeof window.getProgress === 'function') {
        return window.getProgress();
    }
    const defaultState = {
        version: 2,
        xp: 0,
        streak: { days: 1, lastActiveDate: null },
        gradedCount: 0,
        correctCount: 0,
        mistakes: [],
        attempts: [],
        lessonsRead: [],
        parentPin: { hash: null, isDefault: true }
    };
    try {
        const stored = localStorage.getItem(STATE_KEY);
        return stored ? JSON.parse(stored) : defaultState;
    } catch {
        return defaultState;
    }
}

function saveState(state) {
    if (typeof window.saveProgress === 'function') {
        return window.saveProgress(state);
    }
    try {
        localStorage.setItem(STATE_KEY, JSON.stringify(state));
    } catch (e) {}
}

function addXP(amount) {
    if (typeof window.addXP === 'function' && window.addXP !== addXP) {
        return window.addXP(amount);
    }
    const state = getState();
    state.xp = (state.xp || 0) + (amount || 0);
    saveState(state);
    updateStats();
}

function updateStats() {
    if (typeof window.updateUIStats === 'function') {
        return window.updateUIStats();
    }
    const state = getState();
    const xpEl = document.getElementById('xp-count');
    const streakEl = document.getElementById('streak-count');
    const streakDays = (state.streak && typeof state.streak.days === 'number') ? state.streak.days : (typeof state.streak === 'number' ? state.streak : 1);
    if (xpEl) xpEl.innerText = (state.xp || 0).toLocaleString('vi-VN');
    if (streakEl) streakEl.innerText = streakDays;
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

// B. FNV-1a Synchronous Hash helper (Nguồn sự thật dùng chung cho PIN phụ huynh)
function hashLocalPin(str) {
    let h = 0x811c9dc5;
    for (let i = 0; i < str.length; i++) {
        h ^= str.charCodeAt(i);
        h = Math.imul(h, 0x01000193);
    }
    return 'lpin_' + (h >>> 0).toString(16);
}
window.hashLocalPin = hashLocalPin;

// Dọn dẹp khóa plaintext cũ nếu còn tồn tại trong localStorage (Ponytail Security)
try {
    localStorage.removeItem('sgk_parent_pin_raw');
} catch (e) {}

// C. Parent PIN Verification (Robust, Non-bypassable)
async function verifyParentPin(pinInput) {
    const pin = (pinInput || '').trim();
    if (!pin) return false;

    const p = window.getProgress ? window.getProgress() : null;
    const isCustomPin = p && p.parentPin && !p.parentPin.isDefault && p.parentPin.hash;

    // Chưa đặt PIN riêng: chấp nhận PIN mặc định 1234
    if (!isCustomPin) {
        return pin === '1234';
    }

    // Đã đặt PIN riêng: CẤM tuyệt đối bypass 1234, chỉ chấp nhận hash hợp lệ
    const targetHash = p.parentPin.hash;
    if (hashLocalPin(pin) === targetHash) return true;

    try {
        if (window.crypto && window.crypto.subtle) {
            const inputHash = await sha256(pin);
            if (inputHash === targetHash) return true;
        }
    } catch (e) {}

    return false;
}

async function setParentPin(newPin) {
    const cleanPin = (newPin || '').trim();
    if (!cleanPin) return;

    try {
        localStorage.removeItem('sgk_parent_pin_raw');
    } catch (e) {}

    const hash = hashLocalPin(cleanPin);
    const p = window.getProgress ? window.getProgress() : { version: 2 };
    p.parentPin = {
        hash: hash,
        isDefault: false
    };
    if (window.saveProgress) {
        window.saveProgress(p);
    } else {
        localStorage.setItem(STATE_KEY, JSON.stringify(p));
    }
}

// C. Frame Buster & Copy Protection đã được tập trung hóa chuyên nghiệp trong js/security-protect.js


// E. Console Copyright Notice
console.log(
    "%c📚 ÔN LUYỆN SGK & DEEPTUTOR %c\nỨng dụng giáo dục phi lợi nhuận bám sát SGK Bộ GD&ĐT 2026 - 2027.\nMọi quyền được bảo vệ cho cộng đồng học sinh Việt Nam.",
    "background: #059669; color: white; font-weight: 800; font-size: 14px; padding: 4px 8px; border-radius: 4px;",
    "color: #334155; font-size: 11px;"
);

// 4. Universal Content Fetcher with high-speed in-memory & working-path caching
const _smartFetchCache = new Map();
let _smartBasePrefix = null;

async function smartFetch(path) {
    const clean = path.replace(/^(\.\.\/|\.\/)/, '');
    
    // 1. Instantaneous in-memory cache hit
    if (_smartFetchCache.has(clean)) {
        const cachedData = _smartFetchCache.get(clean);
        return new Response(JSON.stringify(cachedData), {
            status: 200,
            headers: { 'Content-Type': 'application/json' }
        });
    }

    // 2. Candidates prioritizing learned prefix
    const prefixes = _smartBasePrefix !== null 
        ? [_smartBasePrefix, '', './', '../', '/'] 
        : ['', './', '../', '/'];
        
    const uniqueCandidates = [...new Set(prefixes.map(p => p ? `${p}${clean}` : clean))];

    for (const url of uniqueCandidates) {
        try {
            const controller = typeof AbortController !== 'undefined' ? new AbortController() : null;
            const timeoutId = controller ? setTimeout(() => controller.abort(), 5000) : null;
            const fetchOpts = controller ? { signal: controller.signal } : {};
            const res = await fetch(url, fetchOpts);
            if (timeoutId) clearTimeout(timeoutId);
            if (res.ok) {
                const prefix = url.substring(0, url.length - clean.length);
                _smartBasePrefix = prefix;
                
                try {
                    const cloned = res.clone();
                    const data = await cloned.json();
                    _smartFetchCache.set(clean, data);
                } catch (e) {}
                
                return res;
            }
        } catch (e) {}
    }
    return fetch(path);
}

// Init on load
document.addEventListener('DOMContentLoaded', updateStats);


// ================= DETERMINISTIC OPTION SHUFFLING (P0-1a) =================
function hashSeed(str) {
  let h = 2166136261 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 16777619) >>> 0;
  }
  return h >>> 0;
}

function seededRandom(seed) {
  return function () {
    seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function buildOptionOrder(question, attemptSeed) {
  const n = (question.options || []).length;
  const order = Array.from({ length: n }, (_, i) => i);
  const qSeedId = question.id || question.question || 'q';
  const rand = seededRandom(hashSeed(`${qSeedId}::${attemptSeed}`));
  for (let i = n - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [order[i], order[j]] = [order[j], order[i]];
  }
  const originalCorrect = (question.correct !== undefined ? question.correct : (question.answer !== undefined ? question.answer : 0));
  return { order, correctDisplayIndex: order.indexOf(originalCorrect) };
}

window.hashSeed = hashSeed;
window.seededRandom = seededRandom;
window.buildOptionOrder = buildOptionOrder;


// ==========================================
// P0-6: MOBILE BOTTOM TAB BAR INJECTION
// ==========================================
function setupBottomTabBar() {
    if (window.self !== window.top) return;

    const existing = document.getElementById('ol-mobile-tabbar');
    if (existing) existing.remove();

    const path = window.location.pathname.toLowerCase();
    // Khong hien tab bar tren goc phu huynh vi day la goc rieng cua cha me
    if (path.includes('parent.html')) return;

    const isSubject = path.includes('subject.html') || path.includes('lesson.html');
    const isMistakes = window.location.search.includes('mode=mistakes');
    const isQuiz = path.includes('quiz.html') && !isMistakes;
    const isProgress = path.includes('progress.html');
    const isHome = path.endsWith('index.html') || path === '/' || path.endsWith('/app/') || path.endsWith('/app');

    const ctx = (window.getContext ? window.getContext() : null) || { grade: '06', subject: 'toan' };
    const grade = ctx.grade || '06';
    const subject = ctx.subject || 'toan';

    const mistakes = (window.getMistakes ? window.getMistakes() : []);
    const mistakeCount = mistakes.length;

    const nav = document.createElement('nav');
    nav.id = 'ol-mobile-tabbar';
    nav.className = 'ol-bottom-tabbar';
    nav.setAttribute('aria-label', 'Điều hướng chính ứng dụng');

    const hocActive = isSubject;
    const luyenActive = isQuiz;
    const sotayActive = isMistakes;
    const tiendoActive = isProgress;

    nav.innerHTML = `
        <a href="subject.html?grade=${grade}&subject=${subject}" class="ol-tab-item ${hocActive ? 'active' : ''}" ${hocActive ? 'aria-current="page"' : ''}>
            <span class="ol-tab-icon">📖</span>
            <span>Học</span>
        </a>
        <a href="quiz.html?grade=${grade}&subject=${subject}&chapter=ch01" class="ol-tab-item ${luyenActive ? 'active' : ''}" ${luyenActive ? 'aria-current="page"' : ''}>
            <span class="ol-tab-icon">✍️</span>
            <span>Luyện</span>
        </a>
        <a href="quiz.html?mode=mistakes&grade=${grade}&subject=${subject}" class="ol-tab-item ${sotayActive ? 'active' : ''}" ${sotayActive ? 'aria-current="page"' : ''}>
            <span class="ol-tab-icon">📕</span>
            <span>Sổ tay</span>
            ${mistakeCount > 0 ? `<span class="ol-tab-badge" id="mobile-tab-mistake-badge">${mistakeCount}</span>` : ''}
        </a>
        <a href="progress.html" class="ol-tab-item ${tiendoActive ? 'active' : ''}" ${tiendoActive ? 'aria-current="page"' : ''}>
            <span class="ol-tab-icon">📊</span>
            <span>Tiến độ</span>
        </a>
    `;

    document.body.appendChild(nav);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupBottomTabBar);
} else {
    setupBottomTabBar();
}

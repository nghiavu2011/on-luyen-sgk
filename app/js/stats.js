/**
 * js/stats.js — Nguồn sự thật duy nhất cho tiến độ (sgk-progress v2), XP, Streak, và Sổ tay câu sai.
 * Tuân thủ nghiêm ngặt Đặc tả §7 (ON-LUYEN-SGK_IMPLEMENTATION-SPEC.md).
 */

var STATE_KEY = window.STATE_KEY || 'sgk-progress';
var DEFAULT_PIN_HASH = window.DEFAULT_PIN_HASH || '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4';

const XP_TABLE = {
  'nhan-biet': 2,
  'thong-hieu': 3,
  'van-dung': 5,
  'van-dung-cao': 8,
  'easy': 2,
  'medium': 3,
  'hard': 5,
  'expert': 8,
  'clear_mistake': 10
};

function getTodayIso() {
  const d = new Date();
  return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
}

function getDefaultProgress() {
  return {
    version: 2,
    nickname: 'Học sinh',
    xp: 0,
    streak: { days: 1, lastActiveDate: getTodayIso() },
    gradedCount: 0,
    correctCount: 0,
    mistakes: [],
    attempts: [],
    lessonsRead: [],
    parentPin: { hash: null, isDefault: true }
  };
}

function migrateProgress(old) {
  if (!old || typeof old !== 'object') return getDefaultProgress();
  if (old.version === 2 && old.streak && typeof old.streak === 'object') return old;

  const today = getTodayIso();
  const res = getDefaultProgress();

  if (typeof old.xp === 'number') res.xp = old.xp;
  if (old.nickname) res.nickname = old.nickname;

  // Migrate Streak
  if (typeof old.streak === 'number') {
    res.streak = { days: Math.max(1, old.streak), lastActiveDate: today };
  } else if (old.streak && typeof old.streak.days === 'number') {
    res.streak = old.streak;
  }

  // Migrate mistakes from localStorage or old state
  let rawMistakes = [];
  try {
    const rawDT = localStorage.getItem('deeptutor_mistake_bank');
    if (rawDT) rawMistakes = JSON.parse(rawDT);
  } catch (e) {}
  if (Array.isArray(old.mistakes)) {
    rawMistakes = [...rawMistakes, ...old.mistakes];
  }

  const mmap = new Map();
  for (const m of rawMistakes) {
    const qid = m.questionId || m.id;
    if (!qid || mmap.has(qid)) continue;
    mmap.set(qid, {
      questionId: qid,
      examId: m.examId || '',
      grade: m.grade || '06',
      subject: m.subject || 'toan',
      chapter: m.chapter || 'ch01',
      topic: m.topic || (m.breakdown && m.breakdown.concept) || 'Chủ đề rèn luyện',
      chosenIndex: m.chosenIndex !== undefined ? m.chosenIndex : 0,
      correctIndex: m.correctIndex !== undefined ? m.correctIndex : (m.answer !== undefined ? m.answer : 0),
      wrongCount: m.wrongCount || 1,
      correctStreak: m.correctStreak || 0,
      firstWrongAt: m.firstWrongAt || new Date().toISOString(),
      lastSeenAt: m.lastSeenAt || new Date().toISOString()
    });
  }
  res.mistakes = Array.from(mmap.values());

  if (Array.isArray(old.attempts)) res.attempts = old.attempts;
  if (Array.isArray(old.lessonsRead)) res.lessonsRead = old.lessonsRead;
  else if (Array.isArray(old.completedLessons)) res.lessonsRead = old.completedLessons;

  if (typeof old.gradedCount === 'number') {
    res.gradedCount = old.gradedCount;
    res.correctCount = old.correctCount || 0;
  } else if (res.attempts.length > 0) {
    res.gradedCount = res.attempts.reduce((acc, a) => acc + (a.score ? a.score.total : 0), 0);
    res.correctCount = res.attempts.reduce((acc, a) => acc + (a.score ? a.score.correct : 0), 0);
  }

  if (old.parentPin && old.parentPin.hash) {
    res.parentPin = old.parentPin;
  } else {
    const storedPin = localStorage.getItem('sgk_parent_pin_hash');
    if (storedPin) {
      res.parentPin = { hash: storedPin, isDefault: storedPin === DEFAULT_PIN_HASH };
    }
  }

  res.version = 2;
  return res;
}

function getProgress() {
  try {
    const raw = localStorage.getItem(STATE_KEY);
    if (!raw) {
      const initP = getDefaultProgress();
      saveProgress(initP);
      return initP;
    }
    return migrateProgress(JSON.parse(raw));
  } catch (e) {
    return getDefaultProgress();
  }
}

function saveProgress(progress) {
  if (!progress) return;
  progress.version = 2;
  try {
    localStorage.setItem(STATE_KEY, JSON.stringify(progress));
    // Đồng bộ ngược lại cho DeepTutor mistake bank nếu cần
    if (Array.isArray(progress.mistakes)) {
      localStorage.setItem('deeptutor_mistake_bank', JSON.stringify(progress.mistakes));
    }
    updateUIStats();
  } catch (e) {}
}

function addXP(amount) {
  if (!amount || amount <= 0) return;
  const p = getProgress();
  p.xp += amount;
  saveProgress(p);
}

function updateUIStats() {
  const p = getProgress();
  
  // Update streak date
  const today = getTodayIso();
  if (p.streak.lastActiveDate !== today) {
    const yesterday = new Date(Date.now() - 86400000);
    const yStr = yesterday.getFullYear() + '-' + String(yesterday.getMonth() + 1).padStart(2, '0') + '-' + String(yesterday.getDate()).padStart(2, '0');
    if (p.streak.lastActiveDate === yStr) {
      p.streak.days += 1;
    } else {
      p.streak.days = 1;
    }
    p.streak.lastActiveDate = today;
    saveProgress(p);
  }

  const xpEls = document.querySelectorAll('#xp-count, .xp-val');
  xpEls.forEach(el => el.textContent = p.xp.toLocaleString('vi-VN'));

  const streakEls = document.querySelectorAll('#streak-count, .streak-val');
  streakEls.forEach(el => el.textContent = p.streak.days);

  const hXp = document.getElementById('header-xp-text');
  if (hXp) hXp.textContent = `${p.xp.toLocaleString('vi-VN')} XP`;

  const hStreak = document.getElementById('header-streak-text');
  if (hStreak) hStreak.textContent = `${p.streak.days} ngày streak`;

  const lessonStat = document.getElementById('lesson-user-stat');
  if (lessonStat) lessonStat.textContent = `${p.xp.toLocaleString('vi-VN')} điểm thưởng · Lv. ${Math.floor(p.xp / 100) + 1}`;

  // Update Mistake Badges (P0-4b: Đọc từ một nguồn duy nhất)
  const mistakeCount = (p.mistakes || []).length;
  
  const navMistakeBadge = document.getElementById('nav-mistake-count');
  if (navMistakeBadge) {
    navMistakeBadge.textContent = mistakeCount;
    navMistakeBadge.style.display = mistakeCount > 0 ? 'inline-block' : 'none';
  }

  const dtMistakeCountEl = document.getElementById('dt-mistake-count');
  if (dtMistakeCountEl) dtMistakeCountEl.textContent = mistakeCount;

  const dtCardMistakesText = document.getElementById('dt-card-mistakes-text');
  if (dtCardMistakesText) dtCardMistakesText.textContent = `${mistakeCount} câu cần khắc phục`;

  const progDtMistakes = document.getElementById('prog-dt-mistakes');
  if (progDtMistakes) progDtMistakes.textContent = mistakeCount;

  const parentMistakeEl = document.getElementById('parent-mistake-count');
  if (parentMistakeEl) parentMistakeEl.textContent = `${mistakeCount} câu`;
}

// Single source of truth for Mistakes
function getMistakes(grade, subject) {
  const p = getProgress();
  let list = p.mistakes || [];
  if (grade) {
    const gNorm = String(grade).padStart(2, '0');
    list = list.filter(m => String(m.grade).padStart(2, '0') === gNorm);
  }
  if (subject) {
    list = list.filter(m => m.subject === subject);
  }
  return list;
}


/**
 * P0-4a: Ghi nhận câu trả lời vào Sổ tay câu sai (mistakes) tuân thủ schema §7.2:
 * - Sai hoặc bỏ trống: ghi vào sgk-progress.mistakes hoặc tăng wrongCount, reset correctStreak = 0.
 * - Đúng và có trong sổ: tăng correctStreak.
 * - correctStreak >= 2: xoá khỏi sổ tay (chống ăn may) và thưởng 10 XP (§7.3).
 */
function recordQuestionResult(q, chosenDisplayIdx, isCorrect, meta = {}) {
  const p = getProgress();
  const qid = q.id || q.question;
  const grade = meta.grade || q.grade || '06';
  const subject = meta.subject || q.subject || 'toan';
  const chapter = meta.chapter || q.chapter || 'ch01';
  const examId = meta.examId || q.examId || '';

  const origCorrect = (q.correct !== undefined ? q.correct : (q.answer !== undefined ? q.answer : 0));
  const origChosen = (chosenDisplayIdx !== undefined && q._displayOrder) 
    ? q._displayOrder[chosenDisplayIdx] 
    : (chosenDisplayIdx !== undefined ? chosenDisplayIdx : -1);

  if (!p.mistakes) p.mistakes = [];
  let existingIdx = p.mistakes.findIndex(m => m.questionId === qid || m.id === qid);
  let cleared = false;
  const nowIso = new Date().toISOString();

  if (isCorrect) {
    if (existingIdx >= 0) {
      p.mistakes[existingIdx].correctStreak = (p.mistakes[existingIdx].correctStreak || 0) + 1;
      p.mistakes[existingIdx].lastSeenAt = nowIso;
      if (p.mistakes[existingIdx].correctStreak >= 2) {
        p.mistakes.splice(existingIdx, 1);
        cleared = true;
        p.xp += (XP_TABLE.clear_mistake || 10);
      }
    }
  } else {
    // Sai hoặc bỏ trống
    if (existingIdx >= 0) {
      p.mistakes[existingIdx].wrongCount = (p.mistakes[existingIdx].wrongCount || 1) + 1;
      p.mistakes[existingIdx].correctStreak = 0;
      p.mistakes[existingIdx].chosenIndex = origChosen;
      p.mistakes[existingIdx].lastSeenAt = nowIso;
    } else {
      p.mistakes.push({
        id: qid,
        questionId: qid,
        examId: examId,
        grade: String(grade).padStart(2, '0'),
        subject: subject,
        chapter: chapter,
        topic: q.topic || (q.breakdown && q.breakdown.concept) || 'Chủ đề rèn luyện',
        question: q.question,
        options: q.options || [],
        correct: origCorrect,
        breakdown: q.breakdown || {},
        explanation: q.explanation || '',
        difficulty: q.difficulty || 'nhan-biet',
        chosenIndex: origChosen,
        correctIndex: origCorrect,
        wrongCount: 1,
        correctStreak: 0,
        firstWrongAt: nowIso,
        lastSeenAt: nowIso
      });
    }
  }

  saveProgress(p);
  return { cleared };
}

/**
 * Ghi nhận một lượt nộp bài thi (attempt) theo schema §7.2
 */
function recordExamAttempt(attemptData) {
  const p = getProgress();
  if (!p.attempts) p.attempts = [];

  p.attempts.push(attemptData);
  if (p.attempts.length > 50) p.attempts.shift(); // Giữ 50 lượt gần nhất

  if (attemptData.score) {
    p.gradedCount = (p.gradedCount || 0) + (attemptData.score.total || 0);
    p.correctCount = (p.correctCount || 0) + (attemptData.score.correct || 0);
  }

  saveProgress(p);
}

// Global exposure
window.getProgress = getProgress;
window.saveProgress = saveProgress;
window.getState = getProgress;
window.saveState = saveProgress;
window.addXP = addXP;
window.getMistakes = getMistakes;
window.updateUIStats = updateUIStats;
window.XP_TABLE = XP_TABLE;
window.recordQuestionResult = recordQuestionResult;
window.recordExamAttempt = recordExamAttempt;

document.addEventListener('DOMContentLoaded', updateUIStats);

/**
 * js/context.js — Nguồn sự thật duy nhất cho grade, subject, level và người dùng.
 * Bám sát đặc tả P0-4c (ON-LUYEN-SGK_IMPLEMENTATION-SPEC.md).
 */

const LEVEL_BY_GRADE = {
  '01': 'c1', '02': 'c1', '03': 'c1', '04': 'c1', '05': 'c1',
  '06': 'c2', '07': 'c2', '08': 'c2', '09': 'c2',
  '10': 'c3', '11': 'c3', '12': 'c3'
};

const LEVEL_META = {
  c1: { id: 'c1', name: 'Tiểu học', range: 'Lớp 1 – 5', examLabel: 'Bài luyện tập Tiểu học', primaryColor: '#ea580c' },
  c2: { id: 'c2', name: 'THCS', range: 'Lớp 6 – 9', examLabel: 'Kiểm tra trắc nghiệm THCS', primaryColor: '#0284c7' },
  c3: { id: 'c3', name: 'THPT', range: 'Lớp 10 – 12', examLabel: 'Kỳ thi thử THPT Quốc gia', primaryColor: '#059669' }
};

/**
 * Nguồn sự thật duy nhất cho grade / subject / level trên mọi trang.
 * Đọc từ URLSearchParams, fallback localStorage.
 */
function getContext() {
  const params = new URLSearchParams(window.location.search);
  
  let rawGrade = params.get('grade') || localStorage.getItem('sgk_selected_grade') || '06';
  let grade = String(rawGrade).replace(/[^0-9]/g, '');
  if (!grade || parseInt(grade, 10) < 1 || parseInt(grade, 10) > 12) grade = '06';
  if (grade.length === 1) grade = '0' + grade; // chuẩn hóa 6 -> 06
  
  let rawSubject = params.get('subject') || localStorage.getItem('sgk_selected_subject') || 'toan';
  let subject = String(rawSubject).toLowerCase().replace(/[^a-z0-9_-]/g, '') || 'toan';

  let rawChapter = params.get('chapter') || 'ch01';
  let chapter = String(rawChapter).replace(/[^a-z0-9_-]/gi, '') || 'ch01';

  let rawLesson = params.get('lesson') || 'l01';
  let lesson = String(rawLesson).replace(/[^a-z0-9_-]/gi, '') || 'l01';

  let rawExam = params.get('exam') || '';
  let exam = String(rawExam).replace(/[^a-z0-9_-]/gi, '');

  let rawMode = params.get('mode') || (exam ? 'exam' : 'practice');
  let mode = String(rawMode).replace(/[^a-z0-9_-]/gi, '') || 'practice';
  
  const levelId = LEVEL_BY_GRADE[grade] || 'c2';
  const level = LEVEL_META[levelId];
  
  // Nickname: không bịa tên 'Nguyễn Minh Anh'. Dùng nickname người dùng đặt hoặc 'Học sinh'
  let nickname = 'Học sinh';
  try {
    const raw = localStorage.getItem('sgk-progress');
    if (raw) {
      const p = JSON.parse(raw);
      if (p.nickname && p.nickname.trim()) nickname = p.nickname.trim();
    }
  } catch (e) {}

  return {
    grade,
    subject,
    chapter,
    lesson,
    exam,
    mode,
    levelId,
    level,
    nickname,
    isTHCS: levelId === 'c2',
    isTHPT: levelId === 'c3',
    isTieuHoc: levelId === 'c1'
  };
}

function setNickname(name) {
  if (!name || !name.trim()) return;
  try {
    const raw = localStorage.getItem('sgk-progress');
    const p = raw ? JSON.parse(raw) : {};
    p.nickname = name.trim();
    localStorage.setItem('sgk-progress', JSON.stringify(p));
  } catch (e) {}
}

// Expose to window for vanilla HTML scripts
window.LEVEL_BY_GRADE = LEVEL_BY_GRADE;
window.LEVEL_META = LEVEL_META;
window.getContext = getContext;
window.setNickname = setNickname;

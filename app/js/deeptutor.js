/**
 * DeepTutor Core Engine (v1.0)
 * Triết lý: Dịch vụ gia sư cá nhân trọn đời (HKUDS/DeepTutor)
 * - Three-Layer Memory Architecture (L1: Trace, L2: Knowledge Gaps, L3: Mastery)
 * - Socratic Scaffolding (Gợi ý từng bước, không spoil đáp án)
 * - Mistake Notebook & 1-Click Remediation Practice
 * - Native Lightweight Gamification (Confetti canvas, Web Speech API)
 * - Nguyên tắc: Ponytail (Zero dependencies, Native Platform Only)
 */

const DeepTutor = (function() {
    const STORAGE_PREFIX = 'deeptutor_';
    const KEY_L1 = STORAGE_PREFIX + 'l1_attempts';
    const KEY_MISTAKES = STORAGE_PREFIX + 'mistake_bank';
    const KEY_L2 = STORAGE_PREFIX + 'l2_knowledge_gaps';
    const KEY_L3 = STORAGE_PREFIX + 'l3_mastery';

    function _readJSON(key, defaultVal) {
        try {
            const raw = localStorage.getItem(key);
            return raw ? JSON.parse(raw) : defaultVal;
        } catch (e) {
            return defaultVal;
        }
    }

    function _writeJSON(key, val) {
        try {
            localStorage.setItem(key, JSON.stringify(val));
        } catch (e) {
            console.warn('DeepTutor storage quota exceeded', e);
        }
    }

    // ==========================================
    // 1. THREE-LAYER MEMORY: L1 TRACE & ATTEMPTS
    // ==========================================
    function recordAttempt(question, userAnsIdx, isCorrect, context = {}) {
        const attempts = _readJSON(KEY_L1, []);
        const attemptEntry = {
            id: question.id || ('q_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4)),
            questionText: (question.question || '').substring(0, 100),
            userAns: userAnsIdx,
            correctAns: question.answer,
            isCorrect: isCorrect,
            concept: (question.breakdown && question.breakdown.concept) || 'Kiến thức chung',
            trap: (question.breakdown && question.breakdown.trap) || '',
            difficulty: question.difficulty || 'medium',
            grade: context.grade || '06',
            subject: context.subject || 'toan',
            chapter: context.chapter || 'ch01',
            timestamp: Date.now()
        };

        // Giới hạn 200 lượt gần nhất để nhẹ bộ nhớ
        attempts.unshift(attemptEntry);
        if (attempts.length > 200) attempts.length = 200;
        _writeJSON(KEY_L1, attempts);

        // Cập nhật Sổ tay câu sai (Mistake Bank)
        _updateMistakeBank(question, userAnsIdx, isCorrect, context);

        // Cập nhật L2 Knowledge Gaps & L3 Mastery
        _updateL2Gaps(attemptEntry);
        _updateL3Mastery(attemptEntry);

        return attemptEntry;
    }

    // ==========================================
    // 2. MISTAKE NOTEBOOK & REMEDIATION
    // ==========================================
    function _updateMistakeBank(question, userAnsIdx, isCorrect, context) {
        let mistakes = _readJSON(KEY_MISTAKES, []);
        const qId = question.id || question.question;

        const existingIdx = mistakes.findIndex(m => (m.id === qId || m.question === question.question));

        if (!isCorrect) {
            // Thêm hoặc tăng số lần sai
            if (existingIdx >= 0) {
                mistakes[existingIdx].wrongCount = (mistakes[existingIdx].wrongCount || 1) + 1;
                mistakes[existingIdx].lastMissed = Date.now();
                mistakes[existingIdx].lastUserAns = userAnsIdx;
            } else {
                mistakes.push({
                    id: qId,
                    question: question.question,
                    options: question.options,
                    answer: question.answer,
                    explanation: question.explanation,
                    breakdown: question.breakdown,
                    difficulty: question.difficulty || 'medium',
                    grade: context.grade || '06',
                    subject: context.subject || 'toan',
                    chapter: context.chapter || 'ch01',
                    wrongCount: 1,
                    addedAt: Date.now(),
                    lastMissed: Date.now(),
                    lastUserAns: userAnsIdx
                });
            }
        } else {
            // Nếu học sinh trả lời đúng một câu đang nằm trong sổ tay câu sai -> Khắc phục thành công!
            if (existingIdx >= 0) {
                mistakes.splice(existingIdx, 1);
            }
        }

        _writeJSON(KEY_MISTAKES, mistakes);
    }

    function getMistakeBank(grade = null, subject = null) {
        if (window.getMistakes) {
            return window.getMistakes(grade, subject);
        }
        let mistakes = _readJSON(KEY_MISTAKES, []);
        if (grade) {
            const gNorm = String(grade).padStart(2, '0');
            mistakes = mistakes.filter(m => String(m.grade).padStart(2, '0') === gNorm);
        }
        if (subject) {
            mistakes = mistakes.filter(m => m.subject === subject);
        }
        return mistakes;
    }

    function removeMistake(qId) {
        let mistakes = _readJSON(KEY_MISTAKES, []);
        mistakes = mistakes.filter(m => m.id !== qId && m.question !== qId);
        _writeJSON(KEY_MISTAKES, mistakes);
    }

    function clearMistakes() {
        _writeJSON(KEY_MISTAKES, []);
    }

    // ==========================================
    // 3. THREE-LAYER MEMORY: L2 KNOWLEDGE GAPS
    // ==========================================
    function _updateL2Gaps(attempt) {
        const gaps = _readJSON(KEY_L2, {});
        const key = `${attempt.subject}__${attempt.concept}`;

        if (!gaps[key]) {
            gaps[key] = {
                concept: attempt.concept,
                subject: attempt.subject,
                grade: attempt.grade,
                wrongCount: 0,
                correctCount: 0,
                trap: attempt.trap || '',
                lastUpdated: Date.now()
            };
        }

        if (attempt.isCorrect) {
            gaps[key].correctCount++;
        } else {
            gaps[key].wrongCount++;
            if (attempt.trap) gaps[key].trap = attempt.trap;
        }
        gaps[key].lastUpdated = Date.now();
        _writeJSON(KEY_L2, gaps);
    }

    function getKnowledgeGaps(topN = 5) {
        const gaps = _readJSON(KEY_L2, {});
        const list = Object.values(gaps)
            .filter(g => g.wrongCount > 0)
            .sort((a, b) => (b.wrongCount / (b.wrongCount + b.correctCount + 0.1)) - (a.wrongCount / (a.wrongCount + a.correctCount + 0.1)));
        return list.slice(0, topN);
    }

    // ==========================================
    // 4. THREE-LAYER MEMORY: L3 MASTERY LEVEL
    // ==========================================
    function _updateL3Mastery(attempt) {
        const mastery = _readJSON(KEY_L3, {});
        const sub = attempt.subject || 'chung';

        if (!mastery[sub]) {
            mastery[sub] = { total: 0, correct: 0, points: 0, level: '🌱 Tập sự' };
        }

        mastery[sub].total++;
        if (attempt.isCorrect) {
            mastery[sub].correct++;
            mastery[sub].points += (attempt.difficulty === 'hard' || attempt.difficulty === 'expert') ? 15 : 10;
        }

        const rate = (mastery[sub].correct / mastery[sub].total) * 100;
        if (mastery[sub].total >= 30 && rate >= 85) {
            mastery[sub].level = '👑 Bậc thầy';
        } else if (mastery[sub].total >= 15 && rate >= 75) {
            mastery[sub].level = '⭐ Thành thạo';
        } else if (mastery[sub].total >= 5 && rate >= 55) {
            mastery[sub].level = '🚀 Đang tiến bộ';
        } else {
            mastery[sub].level = '🌱 Tập sự';
        }

        _writeJSON(KEY_L3, mastery);
    }

    function getMasteryProfile() {
        return _readJSON(KEY_L3, {});
    }

    // ==========================================
    // 5. SOCRATIC SCAFFOLDING TUTOR HINTS
    // ==========================================
    function getSocraticHints(question) {
        const concept = (question.breakdown && question.breakdown.concept) || 'Đọc kĩ đề bài';
        const steps = (question.breakdown && question.breakdown.steps) || (question.explanation || '');
        const trap = (question.breakdown && question.breakdown.trap) || '';

        // Tạo 3 bậc gợi ý sư phạm Socrate:
        return [
            {
                step: 1,
                title: '🎯 Bậc 1: Định vị vùng kiến thức',
                content: `Câu hỏi này kiểm tra chuyên sâu về: <strong>${concept}</strong>. Hãy dừng lại 5 giây và nhớ lại định nghĩa hoặc quy tắc quan trọng nhất của phần này.`
            },
            {
                step: 2,
                title: '💡 Bậc 2: Hướng giải quyết từng bước',
                content: steps ? `Gợi ý phương pháp: ${steps.split('.')[0]}.` : `Quan sát kỹ các dữ kiện đã cho và đối chiếu từng phương án để loại trừ.`
            },
            {
                step: 3,
                title: '⚠️ Bậc 3: Cảnh báo bẫy ngụy biện (Self-check)',
                content: trap ? `Học sinh thường hay nhầm ở điểm này: <em>"${trap}"</em>. Em có đang phạm phải lỗi suy luận này không?` : `Kiểm tra lại xem phương án em chọn có thỏa mãn tất cả điều kiện của câu hỏi chưa!`
            }
        ];
    }

    // ==========================================
    // 6. NATIVE GAMIFICATION & INTERACTION
    // ==========================================
    // Pure Canvas Confetti (zero dependencies, ~40 lines)
    function triggerConfetti() {
        let canvas = document.getElementById('deeptutor-confetti-canvas');
        if (!canvas) {
            canvas = document.createElement('canvas');
            canvas.id = 'deeptutor-confetti-canvas';
            canvas.style.position = 'fixed';
            canvas.style.top = '0';
            canvas.style.left = '0';
            canvas.style.width = '100vw';
            canvas.style.height = '100vh';
            canvas.style.pointerEvents = 'none';
            canvas.style.zIndex = '99999';
            document.body.appendChild(canvas);
        }

        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const colors = ['#059669', '#10b981', '#3b82f6', '#f59e0b', '#ec4899', '#8b5cf6'];
        const particles = [];
        for (let i = 0; i < 75; i++) {
            particles.push({
                x: canvas.width / 2,
                y: canvas.height / 2 + 50,
                r: Math.random() * 6 + 4,
                d: Math.random() * 75,
                color: colors[Math.floor(Math.random() * colors.length)],
                tilt: Math.floor(Math.random() * 10) - 10,
                tiltAngleIncremental: (Math.random() * 0.07) + 0.05,
                tiltAngle: 0,
                vx: (Math.random() - 0.5) * 16,
                vy: (Math.random() - 0.7) * 18,
                gravity: 0.35
            });
        }

        let animationFrame;
        let frameCount = 0;

        function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {
                p.tiltAngle += p.tiltAngleIncremental;
                p.y += (Math.cos(p.d) + 3 + p.r / 2) / 2 + p.vy;
                p.x += Math.sin(p.d) * 2 + p.vx;
                p.vy += p.gravity;
                p.tilt = Math.sin(p.tiltAngle - (frameCount / 3)) * 15;

                ctx.beginPath();
                ctx.lineWidth = p.r;
                ctx.strokeStyle = p.color;
                ctx.moveTo(p.x + p.tilt + (p.r / 2), p.y);
                ctx.lineTo(p.x + p.tilt, p.y + p.tilt + (p.r / 2));
                ctx.stroke();
            });

            frameCount++;
            if (frameCount < 120) {
                animationFrame = requestAnimationFrame(draw);
            } else {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                if (canvas.parentNode) canvas.parentNode.removeChild(canvas);
            }
        }
        draw();
    }

    // Native Web Speech API (Giọng đọc sư phạm)
    function speak(text) {
        if (!('speechSynthesis' in window)) return;
        window.speechSynthesis.cancel();
        // Làm sạch mã latex trước khi đọc
        const clean = text.replace(/\$+/g, '').replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, '$1 phần $2');
        const utterance = new SpeechSynthesisUtterance(clean);
        utterance.lang = 'vi-VN';
        utterance.rate = 0.95;
        window.speechSynthesis.speak(utterance);
    }

    // Public API
    return {
        recordAttempt,
        getMistakeBank,
        removeMistake,
        clearMistakes,
        getKnowledgeGaps,
        getMasteryProfile,
        getSocraticHints,
        triggerConfetti,
        speak
    };
})();

window.DeepTutor = DeepTutor;

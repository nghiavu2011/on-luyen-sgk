/**
 * tools/lint-questions.mjs — Công cụ kiểm tra chất lượng câu hỏi trắc nghiệm
 * Tuân thủ Đặc tả P0-1c (ON-LUYEN-SGK_IMPLEMENTATION-SPEC.md)
 */
import fs from 'node:fs';
import path from 'node:path';

const ROOT_DIR = path.resolve('app/content');

function findQuizFiles(dir, files = []) {
  if (!fs.existsSync(dir)) return files;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      findQuizFiles(full, files);
    } else if (entry.isFile() && entry.name.includes('-quiz') && entry.name.endsWith('.json') && !entry.name.endsWith('.bak')) {
      files.push(full);
    }
  }
  return files;
}

const META_KEYWORDS = ['chuẩn BGDĐT', 'theo đúng chương trình', 'quy tắc cơ bản của Chương', 'theo quy định của SGK'];

const quizFiles = findQuizFiles(ROOT_DIR);
console.log(`\n🔍 Đang chạy lint trên ${quizFiles.length} tệp quiz trong app/content...\n`);

let totalQuestions = 0;
const errors = [];
const warnings = [];

for (const file of quizFiles) {
  let content;
  try {
    content = JSON.parse(fs.readFileSync(file, 'utf-8'));
  } catch (err) {
    errors.push({ file, rule: 'PARSE_ERROR', msg: err.message });
    continue;
  }

  let questions = [];
  if (Array.isArray(content)) questions = content;
  else if (content && Array.isArray(content.questions)) questions = content.questions;

  const positionCount = { 0: 0, 1: 0, 2: 0, 3: 0 };
  const relFile = path.relative(process.cwd(), file);

  for (let i = 0; i < questions.length; i++) {
    totalQuestions++;
    const q = questions[i];
    const qid = q.id || `q_${i}`;
    const opts = q.options || [];
    const correctIdx = q.correct !== undefined ? q.correct : (q.answer !== undefined ? q.answer : 0);

    if (opts.length === 0) continue;
    positionCount[correctIdx] = (positionCount[correctIdx] || 0) + 1;

    // Rule: LEN_OUTLIER
    const lengths = opts.map(o => String(o).trim().length);
    const minLen = Math.min(...lengths);
    const maxLen = Math.max(...lengths);
    if (minLen > 0 && maxLen > 1.8 * minLen && maxLen > 30) {
      errors.push({
        file: relFile,
        questionId: qid,
        rule: 'LEN_OUTLIER',
        msg: `Phương án dài nhất (${maxLen} ký tự) > 1.8× phương án ngắn nhất (${minLen} ký tự)`
      });
    }

    // Rule: CORRECT_LONGEST
    if (lengths[correctIdx] === maxLen && maxLen > minLen + 15) {
      errors.push({
        file: relFile,
        questionId: qid,
        rule: 'CORRECT_LONGEST',
        msg: `Phương án đúng (${maxLen} ký tự) dài hơn đáng kể các phương án khác`
      });
    }

    // Rule: META_OPTION
    for (const opt of opts) {
      for (const kw of META_KEYWORDS) {
        if (String(opt).includes(kw)) {
          errors.push({
            file: relFile,
            questionId: qid,
            rule: 'META_OPTION',
            msg: `Phương án chứa cụm từ siêu dữ liệu cấm: "${kw}"`
          });
        }
      }
    }

    // Rule: SOLUTION_LEAK
    for (const opt of opts) {
      const s = String(opt);
      const hasLongParen = /\([^)]*?[;=][^)]*?\)/.test(s) || (/\([^)]*?\)/.test(s) && s.length > 40 && /\([^\)]{15,}\)/.test(s));
      if (hasLongParen) {
        warnings.push({
          file: relFile,
          questionId: qid,
          rule: 'SOLUTION_LEAK',
          msg: `Phương án có dấu hiệu rò rỉ lời giải: "${s.slice(0, 50)}..."`
        });
      }
    }
  }

  // Rule: POSITION_BIAS
  if (questions.length >= 4) {
    for (const [pos, count] of Object.entries(positionCount)) {
      const ratio = count / questions.length;
      if (ratio > 0.4) {
        errors.push({
          file: relFile,
          rule: 'POSITION_BIAS',
          msg: `Trong tệp gốc, ${(ratio * 100).toFixed(1)}% đáp án ở vị trí ${['A', 'B', 'C', 'D'][pos] || pos} (> 40%). Cần shuffle lúc render (P0-1a).`
        });
      }
    }
  }
}

console.log('='.repeat(60));
console.log(`📋 KẾT QUẢ KIỂM TRA LINT (${totalQuestions} câu hỏi trong ${quizFiles.length} tệp):`);
console.log(`   ❌ Lỗi (Errors): ${errors.length}`);
console.log(`   ⚠️ Cảnh báo (Warnings): ${warnings.length}`);
console.log('='.repeat(60));

if (errors.length > 0) {
  console.log('\n❌ DANH SÁCH LỖI TIÊU BIỂU (TOP 10):');
  for (const e of errors.slice(0, 10)) {
    console.log(`   - [${e.rule}] ${e.file}${e.questionId ? ` (${e.questionId})` : ''}: ${e.msg}`);
  }
}

if (warnings.length > 0) {
  console.log('\n⚠️ DANH SÁCH CẢNH BÁO TIÊU BIỂU (TOP 5):');
  for (const w of warnings.slice(0, 5)) {
    console.log(`   - [${w.rule}] ${w.file}${w.questionId ? ` (${w.questionId})` : ''}: ${w.msg}`);
  }
}
console.log('\n');

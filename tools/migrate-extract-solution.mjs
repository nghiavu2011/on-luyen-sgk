/**
 * tools/migrate-extract-solution.mjs — Tách lời giải ra khỏi phương án
 * Tuân thủ Đặc tả P0-1b (ON-LUYEN-SGK_IMPLEMENTATION-SPEC.md)
 */
import fs from 'node:fs';
import path from 'node:path';

const ROOT_DIRS = [
  path.resolve('content'),
  path.resolve('app/content')
];

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

let totalFilesProcessed = 0;
let totalFilesModified = 0;
let totalQuestionsExtracted = 0;
const unextractedQuestions = [];

const SOLUTION_REGEX = /^(.{1,40}?)\s*\((.{15,})\)\s*$/s;

for (const rootDir of ROOT_DIRS) {
  const quizFiles = findQuizFiles(rootDir);
  console.log(`\n🔍 Đang quét thư mục: ${rootDir} (${quizFiles.length} tệp quiz)`);

  for (const file of quizFiles) {
    totalFilesProcessed++;
    let content;
    try {
      content = JSON.parse(fs.readFileSync(file, 'utf-8'));
    } catch (err) {
      console.error(`⚠️ Lỗi đọc JSON: ${file}: ${err.message}`);
      continue;
    }

    let questions = [];
    if (Array.isArray(content)) {
      questions = content;
    } else if (content && Array.isArray(content.questions)) {
      questions = content.questions;
    } else {
      continue;
    }

    let fileModified = false;

    for (let i = 0; i < questions.length; i++) {
      const q = questions[i];
      if (!q.options || !Array.isArray(q.options)) continue;
      const correctIdx = q.correct !== undefined ? q.correct : (q.answer !== undefined ? q.answer : 0);
      const opt = q.options[correctIdx];

      if (typeof opt !== 'string') continue;

      const m = SOLUTION_REGEX.exec(opt);
      if (m) {
        // Tách lời giải:
        // options[correct] = phần trước ngoặc
        // breakdown.calculation = phần trong ngoặc
        q.options[correctIdx] = m[1].trim();
        q.breakdown = q.breakdown || {};
        q.breakdown.calculation = [q.breakdown.calculation, m[2].trim()]
          .filter(Boolean)
          .join(' ');

        fileModified = true;
        totalQuestionsExtracted++;
      } else if (opt.includes('(') && opt.length > 30) {
        unextractedQuestions.push({
          file: path.relative(process.cwd(), file),
          questionId: q.id || `q_${i}`,
          optionText: opt
        });
      }
    }

    if (fileModified) {
      // BẮT BUỘC: tạo bản backup .bak trước khi ghi
      const bakFile = file + '.bak';
      if (!fs.existsSync(bakFile)) {
        fs.copyFileSync(file, bakFile);
      }
      fs.writeFileSync(file, JSON.stringify(content, null, 2), 'utf-8');
      totalFilesModified++;
    }
  }
}

console.log('\n' + '='.repeat(60));
console.log('📊 BÁO CÁO MIGRATION P0-1b:');
console.log(`   • Tổng số tệp quiz đã rà soát: ${totalFilesProcessed}`);
console.log(`   • Số tệp có chỉnh sửa và tạo .bak: ${totalFilesModified}`);
console.log(`   • Tổng số câu hỏi đã tách lời giải: ${totalQuestionsExtracted}`);
console.log(`   • Số câu nghi ngờ cần rà soát thủ công: ${unextractedQuestions.length}`);

if (unextractedQuestions.length > 0) {
  console.log('\n⚠️ Danh sách câu có ngoặc dài nhưng không khớp regex:');
  for (const item of unextractedQuestions.slice(0, 10)) {
    console.log(`   - [${item.file} / ${item.questionId}]: ${item.optionText.slice(0, 80)}...`);
  }
}
console.log('='.repeat(60) + '\n');

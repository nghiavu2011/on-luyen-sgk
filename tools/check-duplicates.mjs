/**
 * tools/check-duplicates.mjs — Quét và phát hiện đề bị nhân bản giữa các chương
 * Tuân thủ Đặc tả P1-1 (ON-LUYEN-SGK_IMPLEMENTATION-SPEC.md)
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const targetDirs = ['content', 'app/content'].map(d => path.resolve(d)).filter(d => fs.existsSync(d));
const ROOT_DIR = targetDirs[0] || path.resolve('content');

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

function normalizeText(str) {
  if (!str) return '';
  return String(str)
    .toLowerCase()
    .replace(/(chương|chủ đề|bài)\s*\d+[^:.,;]*[:.,;-]?/gi, '')
    .replace(/[\s\p{P}\p{S}]+/gu, '');
}

function hashQuestion(q) {
  const normQ = normalizeText(q.question || q.title || '');
  const normOpts = (q.options || []).map(normalizeText).sort().join('|');
  const raw = `${normQ}:::${normOpts}`;
  return crypto.createHash('sha256').update(raw).digest('hex').slice(0, 16);
}

const quizFiles = findQuizFiles(ROOT_DIR);
console.log(`\n🔍 Đang quét kiểm tra trùng lặp trên ${quizFiles.length} tệp quiz...\n`);

// Phân nhóm theo môn học và khối lớp (ví dụ: grade-06/toan)
const groups = new Map();
for (const file of quizFiles) {
  const rel = path.relative(ROOT_DIR, file).replace(/\\/g, '/');
  const parts = rel.split('/');
  if (parts.length >= 2) {
    const groupKey = `${parts[0]}/${parts[1]}`;
    if (!groups.has(groupKey)) groups.set(groupKey, []);
    groups.get(groupKey).push({ file, rel, name: parts[parts.length - 1] });
  }
}

const crossChapterDuplicates = [];
const intraChapterDuplicates = [];
let totalPairsCompared = 0;

for (const [groupKey, files] of groups.entries()) {
  const parsedFiles = [];
  for (const item of files) {
    try {
      const data = JSON.parse(fs.readFileSync(item.file, 'utf-8'));
      const questions = Array.isArray(data) ? data : (Array.isArray(data.questions) ? data.questions : []);
      if (questions.length === 0) continue;
      
      const hashes = new Set();
      const questionMap = new Map();
      questions.forEach((q, idx) => {
        const h = hashQuestion(q);
        hashes.add(h);
        questionMap.set(h, { index: idx + 1, text: q.question || '' });
      });

      // Lấy chapter id (vd: ch01, ch02...)
      const chMatch = item.name.match(/(ch\d+)/i);
      const chapter = chMatch ? chMatch[1].toLowerCase() : '';

      parsedFiles.push({
        ...item,
        title: data.title || '',
        chapter,
        questions,
        hashes,
        questionMap
      });
    } catch (e) {
      // bỏ qua file lỗi parse
    }
  }

  for (let i = 0; i < parsedFiles.length; i++) {
    for (let j = i + 1; j < parsedFiles.length; j++) {
      totalPairsCompared++;
      const fileA = parsedFiles[i];
      const fileB = parsedFiles[j];

      let commonCount = 0;
      const commonQuestions = [];
      for (const h of fileA.hashes) {
        if (fileB.hashes.has(h)) {
          commonCount++;
          commonQuestions.push(fileA.questionMap.get(h));
        }
      }

      const minLen = Math.min(fileA.questions.length, fileB.questions.length);
      const ratio = minLen > 0 ? (commonCount / minLen) : 0;

      if (ratio > 0.5) {
        const item = {
          groupKey,
          fileA: fileA.rel,
          fileB: fileB.rel,
          chapterA: fileA.chapter,
          chapterB: fileB.chapter,
          titleA: fileA.title,
          titleB: fileB.title,
          commonCount,
          totalA: fileA.questions.length,
          totalB: fileB.questions.length,
          ratio,
          sampleQuestions: commonQuestions.slice(0, 2)
        };

        if (fileA.chapter && fileB.chapter && fileA.chapter !== fileB.chapter) {
          crossChapterDuplicates.push(item);
        } else {
          intraChapterDuplicates.push(item);
        }
      }
    }
  }
}

console.log('='.repeat(72));
console.log(`📋 BÁO CÁO TRÙNG LẶP NỘI DUNG ĐỀ THI (So sánh ${totalPairsCompared} cặp đề trong ${groups.size} môn)`);
console.log(`   🚨 Cặp đề trùng liên chương (Cross-Chapter): ${crossChapterDuplicates.length}`);
console.log(`   ⚠️ Cặp đề trùng nội bộ chương (Intra-Chapter/Placeholder): ${intraChapterDuplicates.length}`);
console.log('='.repeat(72));

if (crossChapterDuplicates.length > 0) {
  console.log('\n🚨 PHÁT HIỆN TRÙNG LẶP LIÊN CHƯƠNG NGHIÊM TRỌNG:');
  // Ưu tiên hiển thị Toán 6
  const toan6Dups = crossChapterDuplicates.filter(d => d.groupKey === 'grade-06/toan');
  const otherDups = crossChapterDuplicates.filter(d => d.groupKey !== 'grade-06/toan');

  const showList = [...toan6Dups, ...otherDups];
  showList.slice(0, 15).forEach((d, idx) => {
    console.log(`\n[#${idx + 1}] [${d.groupKey}] ${d.chapterA.toUpperCase()} ➔ ${d.chapterB.toUpperCase()}`);
    console.log(`    • Tệp A: ${d.fileA}`);
    console.log(`    • Tệp B: ${d.fileB}`);
    console.log(`    • Trùng: ${d.commonCount}/${Math.min(d.totalA, d.totalB)} câu (${(d.ratio * 100).toFixed(1)}%)`);
    if (d.sampleQuestions.length > 0) {
      console.log(`    • Câu trùng: "${d.sampleQuestions[0].text.slice(0, 75)}..."`);
    }
  });

  if (showList.length > 15) {
    console.log(`\n... và còn ${showList.length - 15} cặp đề trùng liên chương khác.`);
  }

  // Báo cáo nghiệm thu đặc tả P1-1
  const ch01ch05 = crossChapterDuplicates.find(d => 
    d.groupKey === 'grade-06/toan' && 
    ((d.chapterA === 'ch01' && d.chapterB === 'ch05') || (d.chapterA === 'ch05' && d.chapterB === 'ch01'))
  );
  if (ch01ch05) {
    console.log('\n------------------------------------------------------------------------');
    console.log(`🎯 [P1-1 NGHIỆM THU] Phát hiện chính xác trùng lặp Toán 6 giữa ch01 và ch05:`);
    console.log(`   - ${ch01ch05.fileA} <==> ${ch01ch05.fileB}`);
    console.log(`   - Tỷ lệ trùng lặp: ${(ch01ch05.ratio * 100).toFixed(1)}% (${ch01ch05.commonCount} câu)`);
    console.log('------------------------------------------------------------------------');
  }
} else {
  console.log('\n✅ Không phát hiện trùng lặp liên chương.');
}
console.log('\n');

# -*- coding: utf-8 -*-
import json
from pathlib import Path

base = Path('.')
for folder in ['content', 'app/content']:
    count = 0
    for grade in ['grade-05', 'grade-06', 'grade-07', 'grade-08', 'grade-09', 'grade-10', 'grade-11', 'grade-12']:
        gdir = base / folder / grade
        assert gdir.exists(), f'{gdir} does not exist'
        with open(gdir / 'subjects.json', encoding='utf-8') as f:
            json.load(f)
            count += 1
        for sdir in gdir.iterdir():
            if sdir.is_dir():
                for jf in sdir.glob('*.json'):
                    with open(jf, encoding='utf-8') as f:
                        json.load(f)
                        count += 1
    print(f'Checked {folder}: {count} JSON files 100% valid.')

with open('content/grades.json', encoding='utf-8') as f:
    g1 = json.load(f)
with open('app/content/grades.json', encoding='utf-8') as f:
    g2 = json.load(f)

print("Grades in content:", [g['id'] for g in g1['grades']])
print("Grades in app/content:", [g['id'] for g in g2['grades']])
print("All integrity checks PASSED!")

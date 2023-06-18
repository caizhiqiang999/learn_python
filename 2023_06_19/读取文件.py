from pathlib import Path

path = Path('test.txt')
# 读中文，得加encoding='utf-8'
# 读英文，则不需要
contents = path.read_text(encoding='utf-8')
print(contents)
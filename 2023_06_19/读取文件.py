from pathlib import Path

path = Path('test.txt')
# 读中文，得加encoding='utf-8'
# 读英文，则不需要
contents = path.read_text(encoding='utf-8')
print(contents)

# 读取文件中各行 splitlines()
contents_list = contents.splitlines()
for content in contents_list:
  print(content)

# 注意，在读取文件时，python将所有文件都解释为字符串
# 要想作为数值使用，得通过int()等函数转化
from pathlib import Path

path = Path('write.txt')
# 写入文件，必须是字符串，中文要加第二个参数
path.write_text('真的勇士，敢于直面惨淡的人生，敢于正视淋漓的鲜血', encoding='utf-8')

# 写入多行
content = '你是谁\n'
content += "我也不知道\n"
path.write_text(content, encoding='utf-8')

# 在写入时，如果文件存在，则会覆盖
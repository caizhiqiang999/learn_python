name = ['caizhiqiang', 'caina', 'wanghyuan']

# 注意缩进
for item in name:
  print(item)

# range()用来生成一系列的数，左闭右开，接受第三个参数：步长
for number in range(1, 7):
  print(number)

for number in range(1, 100, 20):
  print(number)

# list()，可以将range()的结果直接转为列表
print(list(range(1, 11)))
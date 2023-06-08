age = input('请输入你的年龄: ')
print(age)

# 下面代码会报错！！！
# if age < 18:
#   print('aaa')

# 注意，input返回值是一个字符串，如果想转为数字类型：int()

age = int(age)
if age < 18:
  print('aaa')
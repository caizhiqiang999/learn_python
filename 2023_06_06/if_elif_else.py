score = 100

if score < 20:
  print('成绩极差！')
elif score < 60:
  print('成绩差！')
elif score < 80:
  print('成绩一般！')
else:
  print('成绩优秀！')

if score:
  print('score')

# 对于0 None "" '' [] () {} python都会返回False
import random

# 这个模块中有一个有趣的函数
# randint()，他将两个整数作为参数，并随机返回一个位于这两个整数之间(含)的整数
# number = random.randint(1, 4)
# print(number)

# choice()，他将一个列表或元组作为参数，返回其中的一个元素
list = ['hahaha', 3, 56, '777']
item = random.choice(list)
print(item)
# 1.基本使用
# class Cat:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def running(self):
#     print(f'{self.name}正在奔跑！')

#   def eating(self):
#     print(f'{self.name}正在吃东西！')

# cat = Cat('大白', 3)
# cat.running()

# 2.有些属性无需通过形参来定义，可直接在__init__()中指定即可
# class Cat:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     # 直接指定
#     self.height = 1.88

# 3.修改属性的值
class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    # 直接指定
    self.height = 1.88

cat = Cat('大白', 3)
print(cat.height)
cat.height = 4.55
print(cat.height)
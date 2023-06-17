class Person:
  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height

  def running(self):
    print(f'{self.name}正在跑步！')

  def eating(self):
    print(f'{self.name}正在吃饭！')

# 关于老师职称的类
class FirstTeacher:
  def __init__(self):
    self.title = '一级教师，获奖多次'

class Teacher(Person):
  def __init__(self, name, age, height):
    # 继承父类属性
    super().__init__(name, age, height)
    # 将实例用作属性
    # 当在给老师这个类添加细节时，发现有些专门针对于老师职称的东西
    # 我们可以直接将这些东西提取出来，放到FirstTeacher类中
    # 并将其实例作为Teacher类的属性
    self.first_teacher = FirstTeacher()

  def teaching(self):
    print(f'{self.name}正在上课！')

  # 重写父类方法
  def running(self):
    print(f'{self.name}正在跑步，跑地飞快！')

teacher = Teacher('魏亚军', 50, 1.60)

print(teacher.name, teacher.age, teacher.height)
teacher.running()
teacher.eating()

print(teacher.first_teacher.title)
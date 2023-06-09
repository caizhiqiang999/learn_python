# 定义一个最简单的函数
def get_name(first_name, last_name):
  name = first_name + last_name
  print(name)

get_name('cai', 'zhiqiang')

# 关键字实参：可以不关心参数顺序
get_name(last_name='na', first_name='cai')

# 默认值和返回值
def get_area(width=100, height=100):
  area = width * height
  return area

area = get_area(300)
print(area)

# 传递任意数量的实参
# python会将参数封装到一个元组中
def print_fruits(*fruits):
  print(fruits)

print_fruits('apple', 'pear', 'banana')

# 有位置实参放前面
def make_pizza(size, *tooppings):
  print(size)
  print(tooppings)

# 使用任意数量的关键字实参
def student_message(name, age, **student):
  student['name'] = name
  student['age'] = age
  return student

student = student_message('caina', 18, height=1.6, weight=110)
print(student)
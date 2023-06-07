people = {
  'name': 'caina',
  'age': 18,
  'hobby': 'basketball'
}

print(people['hobby'])
# 添加键值对
people['height'] = 1.88
print(people)
# 修改键值对
people['name'] = 'caizhiqiang'
print(people)
# 删除键值对
del people['hobby']
print(people)

# 使用get()来访问值，接收第一个参数为键，第二个参数是当键不存在时返回的值，如果没有，返回None
print(people.get('name'))
print(people.get('hobby'))

caina = {
  'name': 'caina',
  'age': 15,
  'height': 1.60
}

print(caina.items())
# 遍历字典的键值对
for key, value in caina.items():
  print(f'{key}:{value}\n')
# 遍历所有的键
for key in caina.keys():
  print(key)
# 如果想按特定顺序遍历键
for key in sorted(caina.keys()):
  print(key)

# 遍历所有的值
for value in caina.values():
  print(value)
# 想对遍历的值去重 set()
for value in set(caina.values()):
  print(value)

# 集合和列表的区别：当{}内没有键值对时，很可能是集合，集合存储的元素没有顺序

# 列表中可以存储字典，字典中可以存储列表等，和js类似
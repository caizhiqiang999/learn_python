# 列表表示和索引相关的东西与js相同

name = ['caizhiqiang', 'caina', 'caixiaodie']
# 可以通过索引-1访问最后一个元素，-2访问倒数第二个元素...
print(name[-1])
print(name[-2])

# 追加元素 append() 类似于js中的push()
name.append('xijingping')
print(name)

# 插入元素 insert()
# 在索引1的位置插入liqiang
name.insert(1, 'liqiang')
print(name)

# 删除元素
# 知道索引，可以用del
del name[1]
print(name)
# 删除列表最后一个元素pop() 该方法会将删除的元素返回
last_name = name.pop()
print(last_name)

# 可以给pop()传递参数，删除任意位置的元素
first_name = name.pop(0)
print(first_name)
print(name)

# 根据值进行删除 remove()，该方法只会删除第一个指定的值，如果值出现多次，则需要使用循环
name.remove('caina')
print(name)

# sort()方法对列表进行永久排序
ages = [23, 66, 78, 43, 19]
# 顺序排列
ages.sort()
print(ages)
# 倒序排列
ages.sort(reverse = True)
print(ages)

# sorted()会对列表进行临时排序，不影响原列表
score = [98, 67, 89, 92, 59]
print(sorted(score))
print(sorted(score, reverse = True))
print(score)

# 反转列表
score.reverse()
print(score)

# 获取列表长度
print(len(score))

# 操作列表的其他方法
score = [98, 67, 89, 92, 59]
# index()：返回第一个匹配元素的索引位置
print(score.index(89)) # 2
# count()：返回指定元素在列表中出现的次数
print(score.count(98)) # 1
print(score.count(9)) # 0
# max()：返回列表中最大的元素  min()：返回列表中最小的元素  sum()：返回列表中所有元素的总和
print(max(score))
print(min(score))
print(sum(score))
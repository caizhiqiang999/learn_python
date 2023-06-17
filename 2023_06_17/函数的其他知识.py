# 整个模块导入
# import function

# name = function.get_name('cai', 'zhiqiang')
# print(name)

# 按需导入
# from function import get_name

# name = get_name('cai', 'zhiqiang')
# print(name)

# 起别名
# import function as fun

# name = fun.get_name('cai', 'zhiqiang')
# print(name)

# 给函数起别名
from function import get_name as gn

name = gn('cai', 'zhiqiang')
print(name)
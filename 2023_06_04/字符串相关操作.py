d = 'asdfsfFASOGFNdsfaFFAFG'
# 输出大写
print(d.upper())
# 输出小写
print(d.lower())

# f字符串
a = 'Cai'
b = 'Zhiqiang'
full_name = f'{a} {b}'
print(full_name)

# 制表符\t 换行符\n
print('\tJavaScript\n\tC\n\tJava\n\tPython')

# 删除字符串空白 rstrip() lstrip() strip()
name = '  两情若是长久时 '
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 删除前缀  删除后缀
url = 'http://localhost'
print(url.removeprefix('http://'))
print(url.removesuffix('localhost'))

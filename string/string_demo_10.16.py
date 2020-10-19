#字符串：
"""字符串运算符 10.16"""
"""
s1 = "abc"
s2 = "abc"
s3 = '''  
abc'''  # 不换行干嘛用三引号呢


print(id(s1), id(s2), id(s3))  #  前两个一样 后一个不一样，三引号与但双引号占用内存不同(前提：'''内容有换行)
print(s1 == s2)   # 等号比较内容
print(s1 is s2)
print(s2 == s3)   # 如果三引号有换行 则内容不同
print(s2 is s3)
"""

"""s1 = input("请输入")  # 'abc'
s2 = input("请输入")  # 'abc'
# input 底层做了处理 内存地址不同
print(s1 == s2)   # 等号比较内容 True
print(s1 is s2)   # is比较内存地址 False
"""

"""
# 字符串的运算符：+ *
s3 = s1 + s2  # + 相当于拼接
s4 = s1 * 5
print(s3)
print(s4)

# in 在...里面 not in 不在... 里面
name = 'sten'
result = 'tv' in name  # 返回值为True False
print(result)

# % 字符串的格式化
print('%s说：大家好好学习！' % name )

# r 保留原格式 转义字符则无效

# [] [:] 列表 切片
filename = 'picture'
print(filename[0:3])

"""

# [start:end:方向和步长]
s = 'abcde'
print(s[::-1])  # 字符串倒序 -1表示逆序
print(s[::2])   # 最后一个表示步长

# 练习 hello world
#逆序输出 world 正序输出hello 逆序输出hello world  打印oll 打印llo wo
s1 = 'hello world'
print(s1[-1:-6:-1])
print(s1[0:5])
print(s1[::-1])
print(s1[4:1:-1])
print(s1[2:8])   
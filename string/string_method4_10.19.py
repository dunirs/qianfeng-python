
"""

# isalpla() 是否是纯字母  isdigit() 是否是纯数字
s = 'abcd'
result = s.isalpha()
print(result)
s = '99'
result = s.isdigit()
print(result)

sum = 0
i = 1
while i<=3:
    num = input('请输入数字：')
    if num.isdigit():
        num = int(num)
        sum += num
        print('第{}个数字累加成功！'.format(i))
        i += 1
    else:
        print('不是数字')

print(sum)
"""

# jion() 拼接 用指定元素完成拼接 返回字符串
# 与 + 不同的地方在于 jion可以指定用什么拼接
s = 'abc'
result = '-'.join(s)
print(result)
list1 = ['1', '2', 'a', 'c']
result = ''.join(list1)
print(result)


# strip lstrip rstrip
# 截掉空格 去除两边 左 右
s = 'ss    '
result = s.rstrip()
print(result+'9')


# 分割字符串：split() 返回列表
s = 'hello world 22'
result = s.split()
print(result)

# count() 求字符串里指定元素个数
c = s.count(' ')
print(c)


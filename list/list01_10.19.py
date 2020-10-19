"""
# 声明
names = ['jack', 'tom', 'lucy']  # 列表
comuter_brands = ['hp', 'dell', 'thinkpad', 'lenovo', 'mac', '神州']
# 地址
print(id(names))
print(id(comuter_brands))  # 即使是空的也会有一个地址

# 查 ：通过下标
# 元素的获取：下标
print(names[0])

# 遍历 结合循环
for i in names:
    print(i, end=' ')
"""

brands = ['hp', 'dell', 'thinkpad', '华为', 'lenovo', 'mac', '神州']
# 改
brands[-1] = 'HASEE'  # 赋值
print(brands)

# HUAWEI
s = brands.index('华为')  # 范围指定元素下标
brands[s] = 'HUAWEI'
print(brands)

"""# 删除 del
del brands[2]
print(brands)

s = brands.pop(2)  # pop与del不同的是pop还可以返回要删除的元素
print(brands)
print(s)
"""

#  边删边遍历 不能简单的用for循环，应该与下标结合着用  或者用while
# 同时删除 hp mac
"""l = len(brands)
i = 0
while i<l:
    if 'hp' in brands[i] or 'mac' in brands[i]:
        del brands[i]
        l -= 1
    i +=1

print(brands)
"""
for item in brands:
    if 'hp' in item or 'mac' in item:
        del brands[brands.index(item)]

print(brands)

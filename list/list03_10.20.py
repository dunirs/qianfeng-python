# 字符串 切片操作
# s='abcdefg'  s[2:5]  -->cde
# 标号：
list1 = ['jack', 10, 11.1]

# 列表也支持切片 同理用标号 返回结果也是列表
# list[start,end.step] 开始 结尾 步长 负数为反方向
print(list1[-1::-1])


# 列表的添加
# 创建一个空列表
singers = []
# name = input('请输入你喜欢的歌手：')

# 列表函数的使用 ：append extend insert
# append() 末尾追加
# extend() 输入 abc 则变成 ['a', 'b', 'c']
# 使用场景 把一个列表添加到另一个列表中
# singers.extend(name)
# print(singers)

# 列表合并 +
singer = singers + list1
# print(singer)

# insert 插入 指定位置添加
singers.insert(1, 'bbb')
# print(singers)


# 产生10个随机数 ，将其保存到列表中

"""
步骤：
1如何产生随机数
2.10个数字产生
3.将随机数放到列表中
4.打印列表
"""

import random
random_list = []  # 存放随机数
# for i in range(10):   # 循环10次
#     ran = random.randint(1, 11)  # 产生1-100的随机数
#     random_list.append(ran)
# print(random_list)

# 产生10个不同的随机数
i = 0
while i < 10:
    ran = random.randint(1, 20)  # 产生1-20的随机数
    if ran not in random_list:
        random_list.append(ran)
        i += 1
print(random_list)


# 找出最大值   最大值
print(max(random_list))
print(min(random_list))

# 自定义求最大值
maxvalue = random_list[0]    # 假设最大值为 第一个
for value in random_list:
    if maxvalue < value:
        maxvalue = value
print(maxvalue)

maxvalue1 = sorted(random_list,reverse=True)[-1]    # 对列表进行排序
print(random_list)
print(maxvalue1)

random_list.sort(reverse=True)    # sort 改变原列表；   sorted 不改变原列表 注意 sort 与 sorted 用法不一样        reverse=True   递减排序
print(random_list)
maxvalue2 = random_list[-1]
print(maxvalue2)


# 求和
sum1 = sum(random_list)
print(sum1)


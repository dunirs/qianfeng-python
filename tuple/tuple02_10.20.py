# 拆包
t1 = (4, 7, 3)
# 拆包过程遇到的两种错误
# a, b = t1  # ValueError: too many values to unpack (expected 2)
# a, b, c, d = t1  # ValueError: not enough values to unpack (expected 4, got 3)

a, b, c = t1
print(a, b, c)


# 变量个数与元组个数不一致
t2 = (1, 2, 3, 4, 5)
a, *b, c = t2
print(a, c, b)  # *b参考指针 b返回一个列表

t3 = (9,)
a, *b = t3
print(a, b)

# 字符串与列表同理也可使用这种方式
# 列表 元组 前面加* 就相当于拆包


"""
元组:
1.符号：（1,2,3） 
2.关键字 ：tuple
3.元组的元素只能获取，不能增删改

符号：
+ 
*
is  not is
in not in

系统函数：
max()
min()
sum()
len()
sorted()  返回的是列表
tuple()  元组类型的强制转换

元组自带的函数
index()
count()

拆装包
"""




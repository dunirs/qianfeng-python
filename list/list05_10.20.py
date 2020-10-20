# 列表函数
"""
添加：append extend insert
删除： del list[index]
       remove()   移除第一个匹配到的元素 返回值为None 找不到则报异常
       pop()      默认从末尾删除 返回值为被删除的元素 或者指定下标删除
       clear      清除列表，里面所有元素都被删除 ，无返回值

"""

hotpot_list = ['海底捞', '张亮麻辣烫', '呷哺呷哺', '热辣一号', '宽板凳']
hotpot_list.append('张亮麻辣烫')
print(hotpot_list)
hotpot_list.remove('张亮麻辣烫')  # remove 移除第一个匹配到的元素
print(hotpot_list)
pop1 = hotpot_list.pop()
print(hotpot_list)

# 列表翻转 reserve()

# 排序: sort()
"""
sorted(list)
list.sort()
"""

list1 = [4, 8, 7, 3]
list1.sort()
print(list1)

# 次数 count()
weapons = {'刀': 500, '枪': 1000, '剑': 400, '棍': 300}
print(weapons['刀'])
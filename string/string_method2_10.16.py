# 查找相关的，替换
# find() rfind() lfind index rindex lindex replace

s1 = 'index lucy lucky goods'
position = s1.find('l')  # 返回第一次找到位置 ，返回-1则表示没找到
print(position)
p = s1.find('l', position+1, len(s1))  # 指定查找开始 结束位置
print(p)

p1 = s1.rfind('l')  # 从右侧找


s1.index('l', position+1, len(s1))  # 用法与find一样 在找不到是会报一个异常 而不是返回-1

# 替换
# replace(new,old,[max]) max选填 替换最大次数
s2 = s1.replace(' ', '-')
print(s2)
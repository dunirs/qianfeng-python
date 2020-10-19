
"""# 字符串内建函数： encode decode
# 编码  网络应用 （中文一般会涉及到编码问题）
msg = '你好'  # 中文的
# gbk 中文  gb2312 简体中文
result = msg.encode('utf-8')  # 默认utf-8
print(result)

#解码
msg1 = result.decode('utf-8')  # 默认utf-8
print(msg1)
"""

# 字符串内建函数 ： startswith() endswith 返回值为布尔类型
# 判断是否为xxx开头或结尾

filename = 'text.txt'
result = filename.endswith('txt')  # 判断是否为 txt结尾
print(result)

s = 'hello'
result = s.startswith('H')  # 不区分大小写

# 应用：文件上传 只能上传图片
path = input('请选择文件：')  # 返回路径 E:\Pycharm\千锋python\banner2.jpg
# 分析 ：要上传的文件 —> 文件名 —> 通过文件名判断是否为图片类型
p = path.rfind('\\')  # 一个\是转义字符 ，所以用两个 \\
filename = path[p+1:]
print(filename)
# 判断是否为图片类型
if filename.endswith('jpg') or filename.endswith('png'):
    print('允许上传')
else:
    print('只能上传图片')

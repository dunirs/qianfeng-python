# 字符串的内建函数
# 第一部分：大小写相关
# capitalize title upper lower
message = 'zhaorui is a beautiful girl'
mas=message.capitalize()  # 将第一个字符大写
print(mas)

mas = message.title()  # 每个单词首字母大写；

mas = message.upper()  # 每个字符全部大写

mas = message.lower()  # 每个字母全部小写
# 案例：    验证码案例
s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
# 四个随机数
code = ''
import random
for i in range(4):  # 4个for循环
    ran = random.randint(0, len(s)-1)
    code = code + s[ran]
print(code)
# 提示用户输入验证码
user_input = input('请输入验证码：')
if user_input.lower() == code.lower():
    print('验证码输入正确！')
else:
    print('验证码输入错误!')

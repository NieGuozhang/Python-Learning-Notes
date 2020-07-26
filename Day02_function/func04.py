# 函数综合应用
'''
    用户登录部分
    输入用户名
    输入密码
    输入验证码   ----》封装成一个函数
'''

import random


def generate_checkcode(n):
    s = '0987654321qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s) - 1)
        code += s[ran]
    return code


def login():
    username = input('输入用户名：')
    password = input('输入密码：')

    # 得到一个验证码
    code = generate_checkcode(5)
    print('验证码是：', code)
    code_input = input('输入验证码：')
    # 验证
    if code.lower() == code_input.lower():
        # 验证码输入正确
        if username == 'nieguozhang' and password == '123456':
            print('用户登陆成功！')
        else:
            print('用户名或密码有误！')
    else:
        print('验证码输入有误！')


login()

# global 申明全局变量的关键字
# 局部变量 全局变量

# s = 'abcd'
name = '月月'


def func():
    s = 'abcd'
    s += 'X'
    print(s)


def func1():
    # global name
    name = '小月月'
    print(name)


func1()
print(name)

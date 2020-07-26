# 闭包
# 在函数中提出的概念，
'''
条件：
    1、外部函数中定义了内部函数
    2、外部函数有返回值
    3、返回的值是：内部函数名
    4、内部函数引用了外部函数的变量

格式：
    def 外部函数（）：
        ...
        def 内部函数():
            ...
        return 内部函数名
'''


def func():
    a = 100

    def inner_func():
        b = 99
        print(a, b)

    return inner_func


x = func()
# x就是内部函数, x()
x()
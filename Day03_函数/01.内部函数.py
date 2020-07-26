# 内部函数
'''
特点：
    1、可以访问外部函数的变量
    2、内部函数可以修改外部函数的可变类型的变量, 比如：list1
    3、内部函数修改全局不可变变量时，需要在内部函数申明 global 变量名
    4、内部函数修改外部不可变变量时，需要在内部函数申明 nonlocal 变量名
    5、locals()查看本地变量有哪些，以字典的形式输出
        globals()查看全局变量有哪些，以字典形式输出
'''


def func():
    # 申明变量
    n = 100  # 局部变量
    list1 = [1, 2, 8, 4]  # 局部变量

    # 申明内部函数
    def inner_func():
        nonlocal n
        # 对list1里面的元素进行+5操作
        for index, value in enumerate(list1):
            list1[index] = value + n
        list1.sort()
        # 修改n变量
        n += 100

    inner_func()
    print(list1)
    print(n)


func()

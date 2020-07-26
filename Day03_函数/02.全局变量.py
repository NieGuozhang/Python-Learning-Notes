a = 100  # 全局变量
print(globals())


def func():
    b = 99

    def inner_func():
        global a
        nonlocal b
        c = 88
        b += 1
        c += 12
        a += 10
        # 尝试打印abc的值
        print(a, b, c)
        print(locals())

    inner_func()
    # 使用函数locals()内置函数j进行查看，可以看到在当期函数中申明的内容有哪些。
    # locals()是一个字典。key: value
    print(locals())


func()

def a():
    #b()
    print('AAAAAAAA')


def b():
    a()
    print('BBBBBBBB')


def c():
    b()
    print('CCCCCCCC')


c()
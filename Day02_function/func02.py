isLogin = False


def add_shoppingcart(goodsName):
    global isLogin
    if isLogin:
        if goodsName:
            # 登录的
            print('成功将{}加入到购物车中！'.format(goodsName))
        else:
            print('没有选中任何商品。')
    else:
        # 没有登录
        # print()
        answer = input('用户没有登录！是否重新登录？（yes/no）')
        if answer == 'yes':
            # 登录
            username = input('输入用户名：')
            password = input('输入密码：')

            # 调用login
            isLogin = login(username, password)  # 函数里面是可以调用另一个函数
            print('isLogin,', isLogin)
        else:
            print('很遗憾，不能添加任何商品！')


def login(username, password):
    if username == 'nieguozhang' and password == '123456':
        # print('登陆成功！')
        return True
    else:
        # print('用户名或密码错误！')
        return False


username = input('输入你的用户名：')
password = input('输入你的密码：')
isLogin = login(username, password)

add_shoppingcart('阿玛尼唇釉')

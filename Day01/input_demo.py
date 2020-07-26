# name = input()
#
# print(name)

# name = input('请输入你的名字：')  # 阻塞式
#
# print(name)
''''
练习：
游戏：捕鱼达人

输入参与游戏者用户名：
输入密码：

充值：500
'''
print('''
******************
      捕鱼达人
******************
    ''')

username = input('输入参与游戏者用户名：')
password = input('输入密码：')

print('%s请充值才能参与游戏！'% username)

coins = input('请充值：')
print('%s充值成功！当前游戏币是：%d'% (username, int(coins)))


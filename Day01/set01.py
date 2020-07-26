import random

list1 = []

for i in range(20):
    ran = random.randint(1, 20)
    list1.append(ran)

print(list1)

s1 = set()  # 创建空集合，只能使用set()

s2 = {1, 2}

print(set(list1))

s1.add('hello')
s1.add('world')
print(s1)


# add() 添加一个元素
# update()

t1 = ('aa', 'bb')
s1.update(t1)
print(s1)

s1.add(t1)
print(s1)


# 删除
# print(s1.remove('hello'))
s1.remove('aa')
print(s1)
import random

list1 = []

for i in range(10):
    ran = random.randint(1, 20)
    list1.append(ran)
print(list1)

t1 = tuple(list1)
print(t1)
print(t1[::-1])

# 最大值 最小值
print(max(t1))
print(min(t1))

# 求和
print(sum(t1))

# 求长度
print(len(t1))

# 元组中的函数
# index()
# count()

print(t1.index(4))
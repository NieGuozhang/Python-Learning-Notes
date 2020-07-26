l1 = [5, 1, 2, 3, 0, 9]
l2 = [4, 5, 3, 0]

s1 = set(l1)
s2 = set(l2)

# 对称差集
s = (s1 | s2) - (s1 & s2)
print(s)

result = s1 ^ s2  # 两个列表不一样的元素 symmetric——difference
print(result)

result = s1 & s2
print(result)
x = [1, 4, 3, 5, 2]
y = [1, 4, 3, 5, 2]

x.sort()
print(x)

# sortedはlist自体を変更しない
print(sorted(y))
print(y)

# 逆順
print(sorted(y, reverse=True))


x = ['1', '4', 3, 1, '1']
# int型の値として評価する
print(sorted(x, key=lambda v: int(v)))

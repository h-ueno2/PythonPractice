from itertools import zip_longest
x = [1, 2, 3]
y = [4, 5, 6]
zip(x, y)

print(list(zip(x, y)))

x = [1, 2, 3]
y = [4, 5, 6, 7]
z = [8, 9]
# 短いイテラブルに合わせる
print(list(zip(x, y, z)))

# 短い場合に埋めることができる
print(list(zip_longest(x, y, z, fillvalue=0)))

def gen_function(n):
    print('start')
    while n:
        print(f'yield: {n}')
        yield n
        n -= 1


gen = gen_function(3)
next(gen)
next(gen)
next(gen)


def gen_function(n):
    while n:
        yield n
        n -= 1


for i in gen_function(2):
    print(i)

print([i for i in gen_function(5)])

print(max(gen_function(5)))


# これはリスト内包表記
x = [1, 2, 3, 4, 5]
listcomp = [i**2 for i in x]  # メモリ上に値を持っている
print(listcomp)

# これはジェネレータ式
gen = (i**2 for i in x)
print(gen)  # あくまで式のため、値を持っていない
print(list(gen))  # リスト化して最後の要素まで計算する
print(list(gen))  # 計算し終えているため空が返却

# ジェネレータ式のみの場合は内包表記を省略可
print(max(i**3 for i in x))

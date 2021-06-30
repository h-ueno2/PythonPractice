y = 100

def foo(x):
    y = x * 2
    return y
print(foo(1))
print(foo(2))
print(y)

def hoge(ary):
    ary.append(10)
    return
ary = [1, 2, 3]
hoge(ary)
print(ary)

def g(x):
    def f(y):
        return x * y #xはg()の引数
    return f # 関数fを返す

gg = g(2)
print(gg(3))
hh = g(10)
print(hh(4))


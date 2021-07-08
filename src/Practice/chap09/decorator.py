from functools import wraps
from dataclasses import dataclass
from functools import lru_cache
from time import sleep


# @lru_cache(maxsize=32)  # 32回分までキャッシュ
# def heavy_function(n):
#     sleep(1)  # 重たい処理
#     return n + 1


# print(heavy_function(2))
# print(heavy_function(2))


@dataclass(frozen=True)
class Fruit:
    # @dataclassをつけると__init__や__repr__が自動で追加される
    # frozen=Trueにすると__setattr__も自動で作成される（読み取り専用となる）
    name: str
    price: int = 0


apple = Fruit(name='apple',  price=128)
print(apple)


def deco1(f):
    print('deco1 called')

    def wrapper():
        print('before exec')
        v = f()  # ここで渡されてきた元の関数を実行する。
        print('after exec')
        return v
    return wrapper


@deco1
def func():
    print('exec')
    return 1


print(func.__name__)
print(func())

# 引数を受け取る場合にも対応させる


def deco2(f):
    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)  # ここで渡されてきた元の関数を実行する。
        print('after exec')
        return v
    return wrapper


@deco2
def func(x, y):
    print('exec')
    return 1


print(func(1, 2))


# デコレータ自身も引数を受け取るパターン
def deco3(z):
    def _deco3(f):
        def wrapper(*args, **kwargs):
            print('before exec', z)
            v = f(*args, **kwargs)  # ここで渡されてきた元の関数を実行する。
            print('after exec', z)
            return v
        return wrapper
    return _deco3


@deco3(z=3)
def func(x, y):
    print('exec')
    return 1


print(func(1, 2))


def deco4(f):
    @wraps(f)  # もとの関数を引数にとるデコレータ→ 関数の名前やDocstringを元の関数で置き換える
    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)  # ここで渡されてきた元の関数を実行する。
        print('after exec')
        return v
    return wrapper


def func():
    """funcです！！
    """
    print('exec')


print(func.__name__)
print(func.__doc__)

from dataclasses import dataclass
from functools import lru_cache
from time import sleep


@lru_cache(maxsize=32)  # 32回分までキャッシュ
def heavy_function(n):
    sleep(1)  # 重たい処理
    return n + 1


print(heavy_function(2))
print(heavy_function(2))


@dataclass(frozen=True)
class Fruit:
    # @dataclassをつけると__init__や__repr__が自動で追加される
    # frozen=Trueにすると__setattr__も自動で作成される（読み取り専用となる）
    name: str
    price: int = 0


apple = Fruit(name='apple',  price=128)
print(apple)

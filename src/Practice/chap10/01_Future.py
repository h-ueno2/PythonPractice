from concurrent.futures import (
    ThreadPoolExecutor,
    Future
)


def func():
    # 非同期に行いたい処理
    return 1


# 非同期で行いたい処理をThreadPoolExecutor().submit()に渡す
# Futreクラスのインスタンスが返却される
future = ThreadPoolExecutor().submit(func)
print(isinstance(future, Future))

# submitに渡した関数の結果を返却
print(future.result())

# 処理の状態確認
print(future.done())
print(future.running())
print(future.cancelled())

from contextlib import contextmanager


class ContextManager:
    # 前処理
    def __enter__(self):
        print('__enter__ was caled')

    # 後処理
    def __exit__(self, exc_type,  exc_value, traceback):
        print('__exit__ was called')
        print(f'{exc_type=}')
        print(f'{exc_value=}')
        print(f'{traceback=}')


with ContextManager():
    print('inside the block')


class ContextManager:
    # 前処理
    def __enter__(self):
        # return した値がasキーワードに渡される
        return 1

    # 後処理
    def __exit__(self, exc_type,  exc_value, traceback):
        pass


with ContextManager() as f:
    print(f)


class Point:
    def __init__(self,  **kwargs) -> None:
        self.value = kwargs

    def __enter__(self):
        print('__enter__ was called')
        return self.value

    def __exit__(self, exc_type,  exc_value, traceback):
        print('__exit__  was called')
        print(self.value)


with Point(x=1, y=2) as p:
    print(p)
    p['z'] = 3


@contextmanager
def point(**kwargs):
    print('__enter__ was called')
    value = kwargs
    try:
        # yield以前が前処理
        yield value  # as に渡る
        # yield以後が後処理
    except Exception as e:
        # エラー時はこちらも呼ばれる
        print(e)
        raise
    finally:
        print('__exit__ was called')
        print(value)


with Point(x=1, y=2) as p:
    print(p)
    p['z'] = 3

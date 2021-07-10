from concurrent import futures
import sys
import time
import os
from concurrent.futures import (
    ProcessPoolExecutor,
    as_completed
)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
    else:
        return a


def elapsed_time(f):
    # 処理時間を計測するためのデコレータ
    def wrapper(*args,  **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}:  {time.time() - st}')
        return v
    return wrapper


@elapsed_time
def get_sequential(nums):
    for num in nums:
        print(fibonacci(num))


@elapsed_time
def get_multi_process(nums):
    with ProcessPoolExecutor() as e:
        futures = [e.submit(fibonacci, num) for num in nums]
        for future in as_completed(futures):
            print(future.result())


def main():
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    get_multi_process(nums)


if __name__ == "__main__":
    main()

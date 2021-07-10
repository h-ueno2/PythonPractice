import threading

from concurrent.futures import (
    ThreadPoolExecutor,
    wait
)


def count_up(counter):
    for _ in range(1000000):
        counter.increment()


class ThreadSafeCounter:
    # ロックを用意する。
    lock = threading.Lock()

    def __init__(self):
        self.count = 0

    def increment(self):
        with self.lock:
            # 排他制御したい一連の処理をこのブロック内に書く
            self.count = self.count + 1


counter = ThreadSafeCounter()
threads = 2
with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up, counter) for _ in range(threads)]
    done, not_done = wait(futures)

print(f'{counter.count=:,}')

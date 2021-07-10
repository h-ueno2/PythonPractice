from concurrent import futures
from concurrent.futures import(
    ThreadPoolExecutor,
    as_completed
)

import time
from urllib import request
from pathlib import Path
from hashlib import md5
urls = [
    'https://twitter.com',
    'https://facebook.com',
    'https://google.com'
]


def download(url):
    req = request.Request(url)
    name = md5(url.encode('utf-8')).hexdigest()
    file_path = './' + name
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path


def elapsed_time(f):
    # 処理時間を計測するためのデコレータ
    def wrapper(*args,  **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}:  {time.time() - st}')
        return v
    return wrapper


@elapsed_time
def get_multi_thread():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download, url) for url in urls]
        for future in as_completed(futures):
            print(future.result())


print(get_multi_thread())

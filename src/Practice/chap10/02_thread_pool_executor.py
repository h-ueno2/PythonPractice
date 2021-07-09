
from urllib import request
from pathlib import Path
from hashlib import md5
urls = [
    'https://twitter.com',
    'https://facebook.com',
    'https://instagram.com'
]


def download(url):
    req = request.Request(url)
    name = md5(url.encode('utf-8')).hexdigest()
    file_path = './' + name
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path


print(download(urls[0]))

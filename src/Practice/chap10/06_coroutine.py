import asyncio
import random


async def call_web_api(url):
    print(f'send a request: {url}')

    # web apiの代わりにSleepを使用。
    await asyncio.sleep(random.random())
    print(f'got a response: {url}')
    return url


async def async_download(url):
    # awaitを使ってコルーチンを呼び出す
    response = await call_web_api(url)
    return response

result = asyncio.run(async_download('https://twitter.com'))
print(result)


async def main():
    task = asyncio.gather(
        async_download('https://twitter.com'),
        async_download('https://twitter.com'),
        async_download('https://twitter.com')
    )
    return await task
result = asyncio.run(main())
print(result)

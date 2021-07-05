from typing import Iterable


def chain(iterables):
    for iterable in iterables:
        for v in iterable:
            yield v

# 上と下は同じ結果となる


def chain(iterables):
    for iterable in iterables:
        yield from (v for v in iterable)


iterables = ('python', 'book')
print(list(chain(iterables)))

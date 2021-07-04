# __len__
from collections import defaultdict


class A:
    def __len__(self):
        return 5


a = A()
print(len(a))


# __str__ and __repr__
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


p = Point(1, 2)
print(p)


# __bool__
class QueryParams:
    def __init__(self, params) -> None:
        self.params = params

    def __bool__(self) -> bool:
        return bool(self.params)


query = QueryParams({})
print(bool(query))  # false

query = QueryParams({'key': 'value'})
print(bool(query))  # true
query


# __call__
class Adder:
    def __init__(self) -> None:
        self._values = []

    def add(self, x):
        self._values.append(x)

    def __call__(self) -> int:
        return sum(self._values)


adder = Adder()
adder.add(1)
adder.add(3)
print(adder())


# __iter__
class Iterable:
    def __init__(self, num) -> None:
        self.num = num

    def __iter__(self):
        return iter(range(self.num))


print([(val) for val in Iterable(3)])


# __next__
class Reverser:
    def __init__(self, x) -> None:
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.x.pop()
        except IndexError:
            raise StopIteration()


print([val for val in Reverser([1, 2, 3])])


# __getitem__,  __setitem__

class CountDict:
    def __init__(self) -> None:
        self._data = {}
        self._get_count = defaultdict(int)
        self._set_count = defaultdict(int)

    def __getitem__(self, key):
        self._get_count[key] += 1
        return self._data[key]

    def __setitem__(self, key, value):
        self._set_count[key] += 1
        self._data[key] = value

    @property
    def count(self):
        return {
            'set': list(self._set_count.items()),
            'get': list(self._get_count.items()),
        }


c = CountDict()
c['x'] = 1
print(c['x'])
c['x'] = 2
c['x'] = 3
print(c.count)


# __contains__
class OddNumbers:
    def __contains__(self, item):
        try:
            return item % 2 == 1
        except:
            return False


odds = OddNumbers()
print(1 in odds)
print(4 in odds)

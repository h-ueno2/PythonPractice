from collections import UserDict
from collections import abc

d = {}  # 空の辞書作成

print(isinstance(d, dict))
print(isinstance(d,  object))
print(isinstance(d, (list, int, dict)))

print(issubclass(dict, object))
print(issubclass(bool, (list, int, dict)))


def get_value(obj, key):
    if not isinstance(obj, abc.Mapping):
        raise ValueError
    return obj[key]


class MyDict(UserDict):
    pass


my_dict = MyDict()
my_dict['a'] = 1
print(my_dict['a'])

# dictのサブクラスではないため、ここでエラーになる
print(get_value(my_dict, 'a'))

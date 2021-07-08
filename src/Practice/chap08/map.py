x = {1, 4, 3, 5, 2}
print(list(map(lambda i: i*10, x)))

keys = ('q', 'limit', 'page')
values = ('python', 10, 2)

print(list(map(lambda k, v: f'{k}={v}',  keys, values)))
print('?'+'&'.join(map(lambda k, v: f'{k}={v}',  keys, values)))

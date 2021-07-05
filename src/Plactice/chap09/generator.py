def gen_function(n):
    print('start')
    while n:
        print(f'yield: {n}')
        yield n
        n -= 1


gen = gen_function(3)
next(gen)
next(gen)
next(gen)


def gen_function(n):
    while n:
        yield n
        n -= 1


for i in gen_function(2):
    print(i)

print([i for i in gen_function(5)])

print(max(gen_function(5)))

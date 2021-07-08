x = (1, 4, 3, 5, 2)

print(filter(lambda i: i > 3,  x))
print(list(filter(lambda i: i > 3,  x)))

x = (1, 0, None, 2, [], 'python')
print(list(filter(None,  x)))

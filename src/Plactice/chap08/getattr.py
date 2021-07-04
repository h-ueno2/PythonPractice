class Mutable:
    def __init__(self, attr_map):
        for k, v in attr_map.items():
            setattr(self, str(k), v)


m = Mutable({'a': 1, 'b': 2})
print(m.a)
1

# 属性の取得
attr = 'b'
print(getattr(m, attr))

# 属性の削除
delattr(m, 'a')
# m.a

text = 'python'
instance_method = getattr(text, 'upper')

print(instance_method)

print(instance_method())

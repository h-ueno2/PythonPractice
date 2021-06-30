# -- coding:utf-8 --

class my_class:
    # 初期化
    def __init__(self, v):
        self.value = v

    # 加算
    def add(self, v):
        self.value += v
    
    # 減算
    def sub(self, v):
        self.value -= v
    
    def get_value(self):
        return self.value
    
obj1 = my_class(100)
obj2 = my_class(1000)
obj1.add(10)
obj2.sub(30)
print(obj1.get_value(), obj2.get_value())
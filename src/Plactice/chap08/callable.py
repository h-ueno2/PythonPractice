
# callable()
print(callable(isinstance))
print(callable(Exception))
print(callable(''.split))


class Threshold:
    def __init__(self, threshold):
        self.threshold = threshold

    def __call__(self, x):
        return self.threshold < x


threshold = Threshold(2)
print(threshold(3))
print(callable(threshold))

from typing import Text


class TextField:
    def __set_name__(self, owner, name):
        print(f'__set_name__ was called')
        print(f'{owner=}, {name=}')
        self.name = name

    def __set__(self, instance, value):
        print('__set__ was called')
        if not isinstance(value, str):
            raise AttributeError('must be str')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print('__get__ was called')
        return instance.__dict__[self.name]


class Book:
    title = TextField()


# __set_name__ was called
book = Book()

book.title = 'Python Practice Book'

notebook = Book()
notebook.title = 'Notebook'


book.title
notebook.title


class TextField:
    # __get__のみ実装
    def __init__(self, value) -> None:
        if not isinstance(value, str):
            raise AttributeError('must be str')
        self.value = value

    def __set_name__(self, owner, name):
        print(f'__set_name__ was called')
        print(f'{owner=}, {name=}')
        self.name = name

    def __get__(self, instance, owner):
        print('__get__ was called')
        return self.value


class Book:
    title = TextField('Python Practice Book')

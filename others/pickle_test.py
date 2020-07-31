import pickle
from typing import Any, SupportsIndex
import sys 

def get_company():
    print('get company')
    return 'Prime Data'


class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.company = get_company()
        print('init')

    def __reduce__(self) -> str | tuple[Any, ...]:
        print('reduce')
        return super().__reduce__() 

    def __reduce_ex__(self, __protocol: SupportsIndex) -> str | tuple[Any, ...]:
        print('reduce ex')
        return super().__reduce_ex__(__protocol)

    def hello(self):
        print('hello', self.name, self.age)


def serialize():
    s = Student('khanh', 31)
    s.name = "nhat anh"
    fname = sys.argv[1] 

    with open(fname, 'wb') as f:
        pickle.dump(s, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    serialize()

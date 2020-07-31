import pickle
import sys
from typing import Any, SupportsIndex


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
        

if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'rb') as f:
        obj = pickle.load(f)
        obj.hello()
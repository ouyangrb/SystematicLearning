# 可迭代对象 iterable：str list tuple dict set range
# 迭代器 reversed zip enumerate filter map (迭代器一定是可迭代对象）

# from typing import Iterable, Iterator
#
# print(issubclass(str, Iterable))  # 判断str是否继承可迭代对象
# print(issubclass(dict, Iterable))
# print(issubclass(dict, Iterator))  # False
#
# print(issubclass(Iterator, Iterable))  # 迭代器继承了可迭代对象

# 可迭代对象：满足以下条件之一
# 支持迭代协议（有__iter__()方法
# 支持序列协议（有__getitem__()方法，且数字参数从0开始
print('__iter__' in dir(str) or '__getitem__' in dir(str))  # True 用这种方式判断是否可迭代对象

# 迭代器：同时满足下面两个魔术方法：__iter__()和__next__()方法
print('__iter__' in dir(map) and '__next__' in dir(map))  # True

class Mylist:
    def __init__(self, iterable=(), /):
        *self.iterable, = iterable
    def __str__(self):
        return f'{self.iterable}'
    def __len__(self):
        i =0
        for i, _ in enumerate(self.iterable, start=1):
            pass
        return i
    def __getitem__(self, item):
        return self.iterable[item]


lst = Mylist()
print(lst)
lst = Mylist((1, 2, 3))
print(lst)
print(len(lst))
for i in lst:
    print(i)
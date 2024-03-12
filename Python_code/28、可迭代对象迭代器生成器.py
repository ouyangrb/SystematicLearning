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
# print('__iter__' in dir(str) or '__getitem__' in dir(str))  # True 用这种方式判断是否可迭代对象

# 迭代器：同时满足下面两个魔术方法：__iter__()和__next__()方法
# print('__iter__' in dir(map) and '__next__' in dir(map))  # True


# # 示例1：通过__getitem__对可迭代对象iterable进行遍历的解释
# class Mylist:
#     def __init__(self, iterable=(), /):
#         *self.iterable, = iterable
#     def __str__(self):
#         return f'{self.iterable}'
#     def __len__(self):
#         i =0
#         for i, _ in enumerate(self.iterable, start=1):
#             pass
#         return i
#     def __getitem__(self, item):
#         return self.iterable[item]
#
#
# lst = Mylist()
# print(lst)
# lst = Mylist((1, 2, 3))
# print(lst)
# print(len(lst))
# '''
# 当对iterable进行迭代时，会先调用__iter__方法，如果没有该方法，则自动调用__getitem__(self.item)方法,
# 此时item形参从0开始+1，每次返回值给i，当__getitem__中抛出Indexerror或stopiteration，for循环处理该
# 异常，循环停止
# '''
#
# # 自动机制执行循环
# for i in lst:
#     print(i)
#
# # 手动调用__getitem__方法
# item = 0
# while True:
#     try:
#         i = lst.__getitem__(item)
#         print(i)
#     except (IndexError, StopIteration):
#         break
#     item += 1


# 示例2：通过__iter__对可迭代对象iterable进行遍历的解释
class ListIter:  # 列表迭代器
    def __init__(self, obj):  # ListIter(self)中self传给obj
        self.obj = obj
        self.index = 0
    def __iter__(self):
        pass
    def __next__(self):
        try:
            ret = self.obj.iterable[self.index]
            self.index += 1  # 执行一次，修该一次实例属性self.index = 0
            return ret
        except IndexError:  # 抛出索引异常
            raise StopIteration

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
    def __iter__(self):
        return ListIter(self)  # 返回一个迭代器实例对象
    def __getitem__(self, item):
        return self.iterable[item]


lst = Mylist((1, 2, 3, 4))
# # 自动机制执行循环,会先调用__iter__方法
# '''
# 当对iterable进行迭代时，会先调用__iter__方法，返回一个迭代器对象，然后开始循环，每次循环时都会用该迭代器对象
# 自动调用__next__方法，该方法的返回值赋值给i，当__next__中抛出stopiteration，for循环处理该异常，循环停止
# '''
#
for i in lst:
    print(i)
#
# # 手动调用__iter__方法
# iter_obj = lst.__iter__()  # 等价于这行 iter_obj = iter(lst) iter是内置函数
# while True:
#     try:
#         i = iter_obj.__next__()
#         print(i)
#     except StopIteration:
#         break


# # 示例3：通过__iter__对迭代器iterator进行遍历的解释
# from typing import Iterable
# class ListIter:  # 列表迭代器
#     def __init__(self, obj: Iterable):
#         self.obj = obj
#         self.index = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         try:
#             ret = self.obj.iterable[self.index]  # self.index 在第一次遍历就到了最大索引位置，第二次就停止迭代
#             self.index += 1  # 执行一次，修该一次实例属性self.index = 0
#             return ret
#         except IndexError:  # 抛出索引异常
#             raise StopIteration
#
# class Mylist:  #列表可迭代对象
#     def __init__(self, iterable=(), /):
#         *self.iterable, = iterable
#     def __str__(self):
#         return f'{self.iterable}'
#     def __len__(self):
#         i = 0
#         for i, _ in enumerate(self.iterable, start=1):
#             pass
#         return i
#     def __iter__(self):
#         return ListIter(self)  # 返回一个迭代器实例对象
#     def __getitem__(self, item):
#         return self.iterable[item]
#
#
# lst = Mylist((1, 2, 3, 4))
# # 自动机制执行循环,会先调用__iter__方法
# '''
# 当对iterator进行迭代时，会先调用自己的__iter__方法，返回一个迭代器实例对象，然后开始循环，每次循环时都会用该迭代器对象
# 自动调用__next__方法，该方法的返回值赋值给i，当__next__中抛出stopiteration，for循环处理该异常，循环停止
# '''
# iter_obj = ListIter(lst)
# for i in iter_obj:
#     print(i)
#
# # 手动调用__iter__方法
# iter_obj = iter_obj.__iter__()  # 每次调用__iter__,返回自身
# while True:
#     try:
#         i = iter_obj.__next__()
#         print(i)
#     except StopIteration:
#         break
# # 迭代器每个元素只能用一次（迭代器里面实现__iter__的意义）

# 生成器：
# # # 自定义函数：
# def func():
#     print(1)
#     return 2
#     print(3)  # 以下的这几行没有意义，上面的return已经返回掉了
#     return 4
#     print(5)

# # 调用函数：执行函数体
# ret = func()
# print(ret)

# # 生成器函数：
# def func():
#     print(1)
#     yield 2  # 第一次运行在这里挂起
#     print(3)
#     yield 4
#     print(5)
# '''
# 调用生成器函数：不会执行函数体，而是返回一个生成器对象（是一个迭代器）
# 当该生成器对象调用__next__方法时，才会开始执行函数体，当遇到yield，把后面的数据就是返回给调用方，然后
# 程序在此处挂起，直到下一次用__next__时，又从该挂起出继续执行，知道遇到下一个yeild，以此类推...
# 最后，当程序执行没有遇到yeild时，会抛出StopIteration停止迭代错误
# '''
#
# ret = func()
# # print(ret)  # <generator object func at 0x0000025F39614EB0>
# # # 生成器继承迭代器，迭代器继承自可迭代对象
# # print(ret.__next__())
# # print('***')
# # print(ret.__next__())
# # print('***')
# # print(ret.__next__())
# for i in ret:
#     print('i=', i)

# # 列表推导式
# lst = [x**2 for x in range(3)]
# print(lst)  # [0, 1, 4]
#
# # 生成器表达式
# gen = (x**2 for x in range(3))
# print(gen)  # <generator object <genexpr> at 0x00000207FFE549E0> 生成器实例对象
# # print(list(gen))  # [0, 1, 4]
# print(sum(gen))  # 5
# print(sum(gen))  # 0 用完了就没有了


# iter内置函数 相当于调用__iter__
# lst = [1, 2, 3]
# print(iter(lst))  # 返回一个可迭代对象

# next内置函数 相当于调用__next__

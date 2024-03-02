# 参数或（和）返回值是其他函数的函数--->高阶函数
# 1、filter（function, iterable)
# 把iterable逐个传入function，把结果是true的iterable留下，返回一个迭代器
lst = [1, True, False, (), 'hello', None, 0, '']
res = filter(None, lst)  # 等价于 res = filter(bool, lst)
print(list(res))  # [1, True, 'hello']

lst = [1, True, False, (), 'hello', None, 0, '']
res = filter(lambda x: print(123), lst)
print(list(res))  # 8个123  一个空[]

# 2、map（func, *iterables) *表示不定长参数
# 类似拉链操作，从迭代器对象中拿东西传入到函数中，返回迭代器
lst1 = [1, 2, 3, 4]
lst2 = [2, 1, 4, 3]
# print(lst1+lst2)  # [1, 2, 3, 4, 2, 1, 4, 3]
res = map(lambda x, y: x+y, lst1, lst2)
print(res)  # <map object at 0x0000022ECD5FDEB0> map是个迭代器
print(list(res))  # [3, 3, 7, 7]

# 3、reduce(function,iterable[,initial])   python3之后不是内置函数了
from functools import reduce
def func(a,b):
    return a * b
def func1(a,b):
    return a + b
lst = [2, 1, 3, 4]
print(reduce(func, lst))  # 24 实现列表里面的各个元素累乘
print(reduce(func1, lst))  # 10 实现列表里面的各个元素累加

print(reduce(func, lst, 100))  # 2400  100先传进去给a，

# 实现列表的sum方法
def my_sum(iterable, /, start=0):
    return reduce(lambda x, y: x+y, iterable, start)
lst = [1, 2, 3]
print(my_sum(lst))  # 6


# 递归函数（了解）

def get_rabits(m):
    if m < 2:
        return 1
    return get_rabits(m-1) + get_rabits(m-2)
print(get_rabits(30))  # 计算慢

# 递归深度一般有限制1000
import sys
print(sys.getrecursionlimit())  # 1000

sys.setrecursionlimit(1200)
print(sys.getrecursionlimit())  # 1200放宽限度

# 用字典存储值，解决递归计算慢的问题
store = {}
def get_rabits(m):
    if m < 2:
        return 1
    if m in store:  # 每一次递归的结果都存放
        return store[m]
    res = get_rabits(m-1) + get_rabits(m-2)
    store[m] = res  # 每一次的结果存放字典中
    print(store)
    return res
print(get_rabits(10))
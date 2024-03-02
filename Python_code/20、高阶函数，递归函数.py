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

# 3、reduce
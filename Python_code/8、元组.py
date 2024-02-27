tup = ()
tup2 = (123,)  # 一个元素的元组，一定要加上，

tup3 = 1, 2, 3  # 封包，也是一个元组 注意：元组不可变
tup4 = (4, 5, [1, 2])
tup4[2].append(3)
print(tup4)  # (4, 5, [1, 2, 3]) 元组里面的列表可以变

string = 'hello'
print(tuple(string))  # ('h', 'e', 'l', 'l', 'o') 可迭代对象转元组

# 元组对象方法
# 1、count 查找元素出现的次数
# 2、index 查找元素索引位置


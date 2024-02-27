# lst = [122, 22, 55, 66]
# lst2 = lst  # 指向同一个地址
# lst[-2] = 999
# print(lst)  # [122, 22, 999, 66]  列表原地操作（inplace），
# print(lst2)  # [122, 22, 999, 66]  跟着变
#
# # 封包：当多个数据赋值给同一个变量时， 会把他们打包成一个元组
# a = 1, 2, 3, 4
# print(a)  # (1, 2, 3, 4)

# lst = [122, 22, 55, 66]
# '''
# 切片格式：lst[start: end: step] = iterable
# '''
# lst[:2] = [5, 6, 9]  # [5, 6, 55, 66] 整体替换
# print(lst)
# lst[:2] = (111, 222)  # [111, 222, 9, 55, 66] 元组是可迭代对象
# print(lst)
# lst[:2] = 333, 444  # [333, 444, 9, 55, 66] 封包成元组
# print(lst)

# lst = [122, 22, 55, 66]
# lst[1:1] = [123]
# print(lst)  # [122, 123, 22, 55, 66] 切片实现插入元素的效果
# lst[len(lst):] = [999]
# print(lst)  # [122, 123, 22, 55, 66, 999] 末尾插入

# lst = [1, 2, 3, 4, 5, 6]
# lst[1:4:2] = 'ab'  # 把索引是1和3 的元素换掉
# print(lst)  # [1, 'a', 3, 'b', 5, 6]

# # list([iterable]) 把一个可迭代对象转列表
# string = 'hello'
# new_list = list(string)
# print(new_list)  # ['h', 'e', 'l', 'l', 'o']
# new_str = str(new_list)   # 把这一整个对象变成字符串，语法 str（object=‘’）
# print(new_str)  # "['h', 'e', 'l', 'l', 'o']"
# print(''.join(new_list))  # hello 用join可以返回

# ==================列表对象方法======================================
# 1、单元素追加 append 原地操作 （字符串和数值是不可变的，对应新建操作）
# 列表、字典、元组、集合是可变的，对应原地操作，效率会更高
lst = [1, 2, 3, 4]
print(lst.append(5))  # None 没有返回值
print(lst)  # [1, 2, 3, 4, 5]

# 2、extend（iterable） 批量元素追加
lst = [1, 2, 3, 4]
lst.extend('abc')
print(lst)  # [1, 2, 3, 4, 'a', 'b', 'c']

# 3、insert 插入
lst = [1, 2, 3, 4]
lst.insert(1, 'b')  # [1, 'b', 2, 3, 4]
print(lst)

# 4、sort（[key],reverse=False)
lst = [1, -2, 8, 9, 3, 4]
lst.sort()
print(lst)  # [-2, 1, 3, 4, 8, 9] 升序
lst.sort(reverse=True)
print(lst)  # [9, 8, 4, 3, 1, -2] 降序
lst.sort(key=abs)  # key是一个函数，排序的值经过函数再觉得排序次序
print(lst)  # [1, -2, 3, 4, 8, 9]

# 5、sorted(iterable,[key],reverse=Flalse 对可迭代对象进行排序
# sort是列表的对象方法，sorted是一个内置函数，可以直接调用
lst = sorted([9, 5, 6])
print(lst)  # [5, 6, 9]  新建操作有返回值

# 6、reverse 单纯倒过来
lst = [1, -2, 8, 9, 3, 4]
print(lst[::-1])  # [4, 3, 9, 8, -2, 1] 新建操作
lst.reverse()  # 原地操作
print(lst)  # [4, 3, 9, 8, -2, 1]

# 7、reversed(seq) 内置函数，返回的是一个迭代器
lst = [1, -2, 8, 9, 3, 4]
res = reversed(lst)
print(res)  # <list_reverseiterator object at 0x0000022F076EDFD0>返回一个地址
print(list(res))  # [4, 3, 9, 8, -2, 1] 转列表操作可以看到
# 迭代器一定是可迭代对象，可迭代对象不一定是迭代器

# 8、count 元素出现的次数

# 9、index 返回第一个找到元素的索引

# 10、pop 要删除元素的索引，原地修改列表并返回被删除的元素

# 11、remove（x）删除值位x的元素，无返回值，找不到删除的元素就报错

# 12、copy（）
lst = [1, -2, 8, 9, 3, 4]
new_lst = lst.copy()
print(lst)  # [1, -2, 8, 9, 3, 4] 浅拷贝

# 13、clear 清空 等价于del()  del是个关键字
lst = [1, -2, 8, 9, 3, 4]
del lst[:]
print(lst)  # []
# 14、
# # 一、while 循环
# # 1、 while 判断语句：
# #     执行语句
#
# # 2、 while True：不清楚循环终止条件时用
# # 3、 break 只终止所在的循环
# # 4、 while....else...组合：执行完while再执行else
# count1 = 0
# while count1 < 5:
#     print(count1, '小于5')
#     count1 += 1
# else:
#     print(count1, '大于或等于5')
#
# # 5、while的嵌套循环， 九九乘法口诀表，里面对齐用到了制表符\t

# 二、for循环
# 格式1：
# for 变量（可1个或多个） in 可迭代对象：
#     执行语句

# res = reversed([1, 2, 3])
# print(sum(res))  # 6 迭代器第一次求和
# print(sum(res))  # 0 迭代器第二次求和
#
# res = reversed([1, 2, 3])
# print(tuple(res))  # (3, 2, 1) 迭代器转元组
# print(sum(res))  # 0 迭代器里面的东西用了一次就没有了

# 字符串、列表、字典、元组、集合，都是可迭代对象，都可以被遍历
# 字符串、列表、元组才是序列，可以切片和索引
# 数字 字符串、元组是不可变数据
# 集合里面只能放不可变数据类型
# (5)的数是整数5，（5，）这样才是元组
# [5],[5,]这两个都是列表
#
# set1 = {4, 5, (5, 6)}
# print(type(set1))
# for i in set1:
#     print(i)

# 格式二： for  in   else 组合

# 一般知道循环次数用for循环，不知道循环次数用while

# 枚举，内置函数 enumerate 返回一个（索引，元素值）组成的元组的迭代器
# 注意：reversd 和zip（拉链操作） 返回的也是迭代器（迭代器一定是可迭代对象，可迭代对象不一定是迭代器（比如列表、元组等）

string = 'hello'
obj = enumerate(string)  # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
print(list(obj))

string1 = 'hello'
obj2 = enumerate(string1, 100)  # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
print(list(obj2))  # [(100, 'h'), (101, 'e'), (102, 'l'), (103, 'l'), (104, 'o')]

for item in string:  # 遍历得到值
    print(item)
for i in range(len(string)):  # 得到索引
    print(i)
for i, item in enumerate(string):  # 得到索引和值
    print(i, item)  # i和item从元组里面赋值，这里发生了序列赋值


# 循环控制语句：
# break 干掉所在的循环
# continue 程序执行到continue时，不再继续执行continue下面的语句，继续到下一次循环

# 列表推导式、字典推导式、集合推导式，这三个都是可变数据类型

# # 1、列表推导式：
# lst = [x for x in range(4)]
# print(lst)  # [0, 1, 2, 3]
#
# lst = [x**2 for x in range(4)]
# print(lst)  # [0, 1, 4, 9]
#
# lst = [(x, y) for x in range(4) for y in 'he' if x % 2]
# print(lst)  # [(1, 'h'), (1, 'e'), (3, 'h'), (3, 'e')]
# # 上面等价于下面(从左往右拆分）：
# lst = []
# for x in range(4):
#     for y in 'he':
#         if x % 2:  # x是奇数
#             lst.append([x, y])
# print(lst)  # [[1, 'h'], [1, 'e'], [3, 'h'], [3, 'e']]

# 推导式的嵌套，略

# 2、字典推导式 {k：vfor子句}
#
# dic = {k: k**2 for k in range(3)}
# print(dic)  # {0: 0, 1: 1, 2: 4}
#
# dic = {k: v for k in range(3) for v in range(4, 6)}
# print(dic)  # {0: 5, 1: 5, 2: 5}
# # 等价于
# dic = {}
# for k in range(3):
#     for v in range(4,6):
#         dic[k] = v
# print(dic)  # {0: 5, 1: 5, 2: 5}
#
# # 3、集合推导式 {exp for子句）
#
# set1 = {x**2 for x in range(4)}
# print(set1)  # {0, 1, 4, 9}
#
# # pass关键字，用来临时占位，空操作，写程序时候用用等价于 用 ...表示
# for i in range(4):
#     pass
# for i in range(4):
#     ...

for _ in range(5):  # _表示拿到的这个值我们不需要，更加python
    pass

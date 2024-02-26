# 索引访问某个元素，切片访问某个片段，索引和切片是访问序列的两种方式

# string1 = 'world'
# print(string1[2])  # r 正向索引
# print(string1[-3])  # r 反向索引
# print(string1[1:3:1])  # or
# print(string1[1:3])  # or左闭区间，右开区间，步长1通常省略
# print(string1[-4:-2])  # or 反向切片
# print(string1[:])  # 默认是0到len(string1)
# print(string1[3:0:-1])  # lro -1从右到左步长为1的切片

lst = [[1, 2, 3],
       [4, 5, 6]]  # 这里就是隐式的行拼接
print(lst[0])  # 索引降维 [1, 2, 3]
print(lst[0:1])  # 切片不降维 [[1, 2, 3]]

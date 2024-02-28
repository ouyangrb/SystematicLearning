# # 1、格式一
# if 判断条件：
#     执行语句
#
# # 2、格式二
# if 判断条件：
#     执行语句1
# else：
#     执行语句2
#
# # 3、格式三  从上往下判断
# if 判断条件1：
#     执行语句1
# elif 判断条件2：
#     执行语句2
# elif 判断条件3：
#     执行语句3
# else ：        # else可以不要
#     执行语句4

# 4、三元表达式（三目表达式）
score = 88
print('666') if score > 80 else print('not good')
res = '777' if score > 80 else 'not good'
print(res)

# 5、条件语句的嵌套

# range内置函数,range是不可变的序列，是iterable
obj = range(8)
print(obj)  # range(0, 8)
print(list(obj))  # [0, 1, 2, 3, 4, 5, 6, 7] 把可迭代对象转列表
obj = range(1, 8, 2)  # 1到8，步长2

# 6、random模块

import random
# print(random.random())  # 0.23945678756150535
# print(random.randint(2, 4))  # 3  2到4随机一个整数
# print(random.uniform(2, 4))  # 返回随机浮点数
# print(random.uniform(4, 2))
print(random.choice([1, 2, 3, 4]))  # 随机从序列里面取个数
print(random.sample([2, 1, 3, 4, 5], 3))  # [3, 5, 4] 取三个样

lst = [1, 2, 3, 4]
random.shuffle(lst)  # 随机打乱,原地操作
print(lst)

print(random.randrange(2, 8, 2))  # 2到8步长2，随机取一个数

random.seed()  # 随机数种子



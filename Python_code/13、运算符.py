# # 一、算术运算符
# a = 5
# b = 2
# print(a//b)  # 2 整除，向下取整
#
# import math  # math里面有很多数学方面的方法
# math.floor(-2.5)  # -3 向下取整
#
# print(8 % 3)  # 2 取模
# print(-8 % 3)  # 1
#
# # 二、比较运算符
# # == >= <= > < !=
# # c = b == d  # 先执行== ， 赋值运算符= 等级最低
#
# # 三、赋值运算符
# # =
# # += -= *= （增强赋值）
#
# # 列表，元组，字符串，可以有以下操作
# a = [1, 2]
# b = [5, 6]
# print(a+b)  # [1, 2, 5, 6]
# print(a*2)  # [1, 2, 1, 2]
#
# # 海象赋值 := 可以在表达式里面进行赋值
# string = 'hello'
# print((length := len(string)) + 5)  # :=的优先级低，括号起来
# print(f'string的长度是{length}')
#
# # a, b, c = 1, 2, 3  # 序列赋值，右边是一个可迭代对象
# a, b, c = 'hel'  # 这种赋值是同时进行的
# a , b = b, a #  a和b交换数值
#
# a = b = c =999  # 多目标赋值

# 四、逻辑运算符 优先级 not > and > or
# 布尔与运算：左边为假时返回左边，否则返回右边
# a = [1]
# b = '123'
# print(a and b)  # 123

# 布尔或运算：左边为真时返回左边，否则返回右边
# a = [1]
# b = '123'
# print(a or b)  # [1]

# 布尔非运算：返回布尔值，如果后面跟着的数据bool判定为True，则返回False，否则返回True
a = [1]
print(not a)  # False

# 内置函数  all(iterable)  any（iterable)

# 五、成员运算符：比较的是值是否相同，相当于 ==
# in 在其中
# not in 不在其中
print('h' in 'hillo')  # True
print('h' not in 'hillo')  # False
print(0 in [1, False])  # True False就是0

# 六、身份运算符：比较的是地址id是否相同，地址相同，值肯定相同了
# is
# is not

# 七、位运算符（二进制操作）见课件
dict2 = {(1, 2): 456}
print(dict2)
tup = (1, 2, 3)
print(tup[0:2])

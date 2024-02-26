# print(r'www.abc./dd/ddd')  # 加一个r里面不会发生转义

num1 = 1.0
print(type(num1))  # <class 'float'>查看类型

# 关于整数的强制转换 int([x],base=10)
print(int())  # 0
print(int('123'))  # 123
print(int('10101', 2))  # 21

# 除了数字0，空字符串，空列表，空字典，空元组，空集合，关键字（False和None）判定为False，其他都为True
# 关键字None的意思是什么都没有
print(bool())  # False
print(bool(0))  # False
print(bool(None))  # False


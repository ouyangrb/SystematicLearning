# # str\list\tuple\dict\set 本身就是类
# print(isinstance(1.23, float))  # True
# range(3, 9)  # range是一个类的实例化
#
# string = 'hello'
# print(isinstance(string, str))  # string是str的实例化
# print(string.replace('l', 'r'))
#
# print(dict.fromkeys('hello'))  # 字典的类方法
# print({1: 2}.fromkeys('hello'))  # 字典的实例调用类方法
# print(type({1: 2}).fromkeys(('hello')))  # 类调用类方法

# dir内置函数，查看类里面包含的属性和方法

# 错误分两类：语法错误和异常
'''
这些内置错误类型都在builtins模块里面（builtins模块里面有map/filter/zip/enumerate/reversed等其他类）
ZeroDivisionError 除0异常
KeyError 键异常
ValueError 值异常
IndexError 索引异常
RecursionError 递归异常
NameError 名字异常....等等

调用zip，map本身就是在实例化类
'''

# import builtins
# print(dir(builtins))  # 查看builtins.py里面的类

# # 错误处理方式1：try......except........笼统异常
# def func(a, b):
#     try:
#         res = a / b
#         print(res)
#     except:
#         print("除0错误")
# func(2, 0)  # 除0错误

# 错误处理方式2：try......except....except....
# def func(a, b):
#     try:
#         res = a / b
#         print(res)
#     except ZeroDivisionError:
#         print("除0错误")
#     except TypeError:  # 可以接多个except，try执行成功不再执行except，执行了一个except就函数返回
#         print('类型异常')
#     except (ZeroDivisionError, TypeError):
#         print("除0错误或类型异常")
# func(2, '1')

# # 错误处理方式2：try......except....嵌套
# def func(a, b):
#     try:
#         try:
#             res = a / b
#             print(res)
#         except ZeroDivisionError:
#             print("除0错误")
#     except:
#         print("除0异常之外的错误")
# func(2, '1')

# # 错误处理方式3：try......except....else
# def func(a, b):
#
#     try:
#         res = a / b
#         print(res)
#     except ZeroDivisionError:
#         print("除0错误")
#     else:
#         print("try中没有异常")  # try顺利执行后，才会执行else
# func(2, 0)

# 错误处理方式4：try......except....as
# def func(a, b):
#
#     try:
#         res = a / b
#         print(res)
#     except ZeroDivisionError as e:  # 等价于 e = ZeroDivisionError('division by zero')
#         print(e)  # e 就是一个实例对象
#     else:
#         print("try中没有异常")  # try顺利执行后，才会执行else
# func(2, 0)  # division by zero

# 错误处理方式5：try......except....else...finally...
# def func(a, b):
#     try:
#         # exit()  # 哪怕直接推出程序，finally都要执行
#         res = a / b
#         print(res)
#     except ZeroDivisionError:
#         print("除0错误")
#     else:
#         print("try中没有异常")  # try顺利执行后，才会执行else
#     finally:
#         print("永远执行这个finally")
# func(2, 0)

# # 6、raise抛出异常
# def div(a, b):
#     if b == 0:
#         raise ZeroDivisionError('除0错误')  # 抛出错误，程序中断
#     return a / b
# div(1, 0)

# 7、自定义异常，一般用系统内置的就够了，见视频课件
class Myerror1:
    def __init__(self, info=''):
        self.info = info
    def __str__(self):  # __str__返回值一定是str类型，当实例对象被转成字符串时，会用实例对象自动调用该方法
        return str(self.info)
e1 = Myerror1(123456)
print(e1)  # 当实例对象被转成字符串时(print会把e1转成字符串输出），会用实例对象自动调用该方法


# # 8、断言
# import random
# num = random.randint(1, 10)
# print(num)
# assert num % 2 == 1, 'num 不是基数'
# print(f'{num}是基数')





# 特殊方法--魔术方法：官方定义好的，自己不能定义，特殊情况下被自动调用

# 1、__init__  类新建实例对象时被调用

# 2、__call__  实例对象 像函数一样被调用时候，自动调用__call__方法
# class A:
#     def __call__(self):
#         print('__call__函数被调用')
# # a = A()
# # a()  # 对象的实例被调用时候，自动调用__call__方法

# 3、__getitem__  实例对象  被索引，切片，遍历 时 被调用
# class A:
# #     def __getitem__(self, item):
# #         return 'hello'
# # a = A()
# # print(a[0])  # a这个实例对象传给__getitem__的self，0传给 item
# # print(a[1: 3: 2])  # slice(1, 3, 2) 得到一个切片的实例对象，slice是builtins里面的针对切片的内置函数
# # for i in a:  # 遍历一次实例，就调用一次__getitem方法，item自动从0开始+1递增，把return的东西给i
# #       print(i)

# 4、__len__ 实例对象 求长度时被调用，要求返回必须是整数类型
print('__len__' in dir(list))  # True

# 5、__repr__\__str__ 实例对象转字符串时，方法被调用，要求返回必须是字符串

class Mylist:
    def __init__(self, iterable=()):  # 初始方法，传一个可迭代对象，默认是一个元组
        *self.lst, = iterable  # 传参解包，self.lst 得到一个列表
    def __getitem__(self, item):
        return self.lst[item]
    def __str__(self):
        return f'{self.lst}'  # f格式化确保返回的是字符串
    def __len__(self):
        i = 0
        for i, _ in enumerate(self.lst, start=1):
            pass
        return i
new_list = Mylist('hello')  # 实例化得到实例对象new_list
# print(new_list)  # 类里面没有__str__方法的话，会得到一个地址
print(new_list)  # ['h', 'e', 'l', 'l', 'o'] print有转字符串操作，实例对象被转字符串操作时自动调用__str__， __str__中返回类型必须是字符串
print(new_list[3])  # 索引自动调用__getitem方法，实例对象new_list传给self，3传给item，
print(new_list[1:5])  # ['e', 'l', 'l', 'o'],item是slice（1：5：None）的实例对象
for i in new_list:  # 遍历一次，调用一次__getitem方法，item自动加1把self.lst[item]的值返回给i
    print(i)
print(len(new_list))  # 自动调用__len__方法


# 实现分数运算魔术方法巩固，详细见视频，


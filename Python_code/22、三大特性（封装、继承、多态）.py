# 封装:
'''
1、类属性和实例属性在前面有__，表示被私有化，只能类内部调用，外部不能被调用
2、类方法和实例方法在前面有__，表示被私有化，只能类内部调用，外部不能被调用

'''

# 继承：所有类的基类是object
'''
1、单继承：类的（属性和方法），先找自己，再找父类要，父类没有找object基类
2、多继承：先找自己的，再按照继承的顺序从左往右找父类的
3、子类无法继承父类的私有属性和私有方法
# '''
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# # class D(A, B):  # 多类继承
# #     pass
# B()  # A这个类实例化过程中，先调用构造方法__new__,它本身类里面没有实现__new__方法，
# #从父类A中找，也没有，最后在object基类中找到，object基类中的__new__,又调用__init__，它里面也没有
# #再从父类B中找，也没有，最后从object中找到，调object基类中的__init__
#
#
# # 子类重写父类方法
# class Animal:
#     def __init__(self, food):
#         self.food = food
#     def eat(self):
#         print(f'动物吃{self.food}')
#
# class Dog(Animal):
#     def eat(self):
#         print(f'狗吃{self.food}')
# dog = Dog('骨头')
# dog.eat()  # 子类调用重写父类的子类方法
# super(Dog, dog).eat()   # super是一个内置函数:用dog（实例化类）调用Dog类的父类的eat方法
#
#
# # 2、 与继承相关的两个内置函数
# # isinstance(object,classinfo) 是不是它的或者子类的实例对象，是就返回true
# print(isinstance(dog, Dog))

# issubclass  判断是否子类

# 3、内置函数
# delattr 删除属性
# getattr 获取对应的属性
# hasattr 判断类里是否有该属性
# setattr(teacher1, 'grade', '二年级') 动态定义属性

# 4、多态性: 多个类有相同的类方法名（这里是change）
# class Apple():
#     def change(self):
#         print(f'我变成苹果汁了')
# class Banana():
#     def change(self):
#         print(f'我变成香蕉汁了')
# class Juice:
#     def work(self, fruit):  # 传一个类实例进来
#         return fruit.change()   # change函数实现不同类方法的调用
# a = Apple()
# b = Banana()
# Juice().work(a)
# Juice().work(b)
# 闭包函数：
'''
嵌套函数
外部函数的返回值是内部函数的引用
内部函数使用到了外部函数的变量/参数
'''
#
# def outer(a):
#     b = 3
#     def inner(c):
#         return a +b + c
#     print(locals())  # {'inner': <function outer.<locals>.inner at 0x0000025C079D8700>, 'a': 2, 'b': 3}
#     return inner
# f = outer(2)
# print(f(4))
# print(f.__closure__[0].cell_contents)  # outer函数被调用后里面的变量a b暂时存放地址

# 装饰器 不改变原来函数的功能，只是在原来函数上增加额外的功能
'''
装饰器用函数和类去实现
使代码更加优雅，结构更加清晰
将实现特定功能的代码封装成装饰器，提高代码的复用率
'''

# # 版本1：
# import time
#
# def timer(f, s):
#     start = time.time()
#     f(s)
#     end = time.time()
#     print(f'消耗时间{end-start}秒')
# def machine(secs):
#     print('设备开始运行')
#     time.sleep(secs)
#     print('机器运行结束')
#
# timer(machine, 2.5)

# # 版本2：闭包
# import time
#
# def timer(f):
#     def inner(s):
#         start = time.time()
#         f(s)
#         end = time.time()
#         print(f'消耗时间{end-start}秒')
#     return inner
# def machine(secs):
#     print('设备开始运行')
#     time.sleep(secs)
#     print('机器运行结束')
#
# # f = timer(machine)
# # f(2.5)
# machine  = timer(machine)
# machine(2.5)

# 版本2：装饰器（通过函数来实现的）
import time

def timer(f):
    def inner(s):
        start = time.time()
        f(s)
        end = time.time()
        print(f'消耗时间{end-start}秒')
    return inner
'''
当被装饰的函数定义好时，会把它作为实参传递给装饰器来调用，即
timer（machine）-->inner
machine 再指向 inner
'''
@timer  # 装饰器函数   可以计算任何一个函数的运行时间
def machine(secs):  # 被装饰的函数   函数引用machine会传给timer里面的f
    print('设备开始运行')
    time.sleep(secs)
    print('机器运行结束')

machine(2.5)
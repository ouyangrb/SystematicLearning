# 闭包函数：
'''
嵌套函数
外部函数的返回值是内部函数的引用
内部函数使用到了外部函数的变量/参数
'''

def outer(a):
    b = 3
    def inner(c):
        return a +b + c
    print(locals())  # {'inner': <function outer.<locals>.inner at 0x0000025C079D8700>, 'a': 2, 'b': 3}
    return inner
f = outer(2)
print(f(4))
print(f.__closure__[0].cell_contents)  #


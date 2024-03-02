# 命名空间（名称到对象的映射）：内置、局部、全局三种，不同命名空间是相互独立的
# 程序执行先从局部找变量，再从全局找，最后从内置找
# 1、内置命名空间
# builtins.py 在这个模块找，当前环境下的不同.py文件都在这里找
# import builtins
# print(dir(builtins))  print函数本身就是在内置命名空间里面

# 2、全局命名空间：模块名、函数、全局变量

# 3、局部命名空间:函数里面，调用完就被释放掉
import random, copy
# def func1(arg1, arg2):
#     num = 666
#     # print(globals())  # 查找全局命名空间里面的变量
#     print(locals())  # 查找局部变量{'arg1': 222, 'arg2': 333, 'num': 666}
# num = 111
# func1(222, 333)

# 4、eval 把传入里面的字符串当作python程序来执行，有返回值，只能放单行字符串
string = 'abs(-4)'
print(eval(string))  # 4
# 5、exec 把传入里面的字符串当作python程序来执行，无返回值
string = 'print(abs(-4))'
exec(string) # 4

string = '''
import random
num = random.randint(1, 10)
print(num)
'''
exec(string)  # exec 可以放多行字符串

a = 1
b = 2
def func3():
    a = 9
    print(a + b)  # b在局部找不到会，在全局找
func3()

# 6、作用域
# 局部作用域  local   L
# 闭包函数外的函数中 enclosing  E
# 全局作用域 global  G
# 内建（置）作用域 built—in  B

'''
闭包函数三要素：
-嵌套函数
-外部函数的返回值是内部函数的引用
-内部函数用到了外部函数的变量或参数
'''
def outer(a):
    b = 2  # 作用域：闭包函数外的函数中 enclosing  E
    def inner(c):
        return c + b + a  # 局部作用域  local   L
    return inner  # 返回引用（返回一个地址）
f = outer(1)
print(f(2))  # 5


# 注意：
lst = [1, 2]
lst1 = lst.append(3)  # append 没有返回值，就是返回None（什么都没有）
print(lst1)  # None
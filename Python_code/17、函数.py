def add(a, b) -> int:  # -> int 提示词语，提示函数的返回值类型是int
    print(a + b)
add(1, 2)  # 调用函数
print(add)  # 引用函数，返回一个地址 <function add at 0x000001E7E733F3A0>
fun = add  # 函数可以像变量一样去引用，这里fun和add都指向同一个地址
print(fun)  # <function add at 0x0000027A9F1CF3A0>
fun(1, 2)  # 3

# return 关键字 一是把结果返回给调用方，二是结束函数的执行

# 2、文档注释
def my_abs(x):
    '''放回参数的绝对值'''
    return -x if x < 0 else x
my_abs(-9)

def my_abs1(x):
   """
   :param x: 随意输入的值
   :return: tuple
   """
   return -x if x < 0 else x

my_abs1(-9)
print(my_abs1.__doc__)  # 文档注释在这个属性里面

# help()  # 查找帮助
# help（print） 直接指定帮助内容

# 和数学相关的内置函数 function，本质是个def开头的函数
# abs(x)
# max
# min()
# pow() 幂次方
# round() 四舍五入
# sum
# divmod 取模求余
# 假如这些内置函数不够用的话，从math模块导入

# 3、类型标注，期望传入什么类型参数,
def add(num1: int, num2: int) -> int:
    return num1 + num2

print(add.__annotations__)  # 这里查看类型标注
# {'num1': <class 'int'>, 'num2': <class 'int'>, 'return': <class 'int'>}



#python3.5以后有个typing包，里面有很多数据类型，就是为了类型标注时用(内置的类型不多）
from typing import Iterable, Callable, List
def my_sum(iterable:Iterable):
    pass

# 3、参数传递（就是传引用，传可变和不可变数据类型是有区别的）见课件

# 4、参数分类
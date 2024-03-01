# 多个值赋给一个变量时，python自动将这些值封装成元组，这个特性称为封包
a = 1, 2, 3, 4
print(a)  # (1, 2, 3, 4)

# 解包，可迭代对象都支持解包
# 1、赋值的解包
a, *b, c, d = 1, 2, 3, 4, 5
print(a)  # 1
print(b)  # [2, 3]
print(c)  # 4
print(d)  # 5


_, *part2, _ = 'helloworld'
print(part2)  # ['e', 'l', 'l', 'o', 'w', 'o', 'r', 'l']

a, *b, c, d = 1, 2, 3
print(b)  # []

# 2、函数传参的解包,在可迭代对象前面加*，就是把迭代对象打散
# 单*针对可迭代对象的解包
def func(a, b, c):
    print(a, b, c)

lst = [1, 2, 3]
# func(lst)  # 报错
func(*lst)  # 1 2 3
# 双**专门针对字典的解包
def func(a, b, c):
    print(a, b, c)

dic = {'a': 1, 'b': 2, 'c': 3}
func(**dic)
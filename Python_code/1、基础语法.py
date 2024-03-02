# # 1、三元表达式(三目表达式）
# score = 100
# print('ok') if score == 100 else print('ng')
#
# # ctrl+/ 批量注释
# # shift  +  ctrl  +  - 折叠代码
# # shift  +  ctrl  +  + 展开代码
#
# # 2、显示的行拼接
# exp = 1 + 2 + 3\
#     + 4 + 5  # “\"续行符
# print(exp)
#
# # 3、隐式行拼接
# lst = [1, 2,
#        3,
#        4]
# print(lst)  # [1, 2, 3, 4]
#
# # 4、引用计数
# a = 999
# b = a  # 999在内存里面被引用了2次
# a = 888
# b = a
# print(a, b)

# # 5、三种变量书写方法：变量只能数值、字母、下划线组成（不能用数字开头）
# this_num = 999  # 下划线
# thisNum = 999  # 小驼峰法
# ThisNum = 999  # 大驼峰法

# # 6、查看关键字方法
# help('keywords')  # 查询关键字
# import keyword
# print(keyword.kwlist)

# # 7、查询内置函数名
import builtins
for i in dir(builtins):
    print(i)

# 8、定义常量一般全部大写（常量和变量用法一样）
# PI = 3.14159


# # 1、replace替换  从左到右寻找替换
# string = 'helloworld'
# new_string = string.replace('l', 'x')
# print(new_string)  # hexxoworxd得到新的地址 字符串和数字是不可变的数据，（任何操作后）对应的地址都不发生变化（即对应新建地址操作）
# print(string)  # helloworld
#
# new_string1 = string.replace('l', 'x', 2)
# print(new_string1)  # hexxoworld 替换前两个ll
#
# print(string.replace('l', 'x').replace('x', 'l', 1))  # helxoworxd 先把三个ll全换成x，再把前面的x换回l
# print(string[::-1].replace('l', 'x', 2)[::-1])  # helxoworxd 先倒序，再换两个，再倒序
# print(string.replace('l', ''))  # heoword 把l全部去掉，换成空
#
#
# # 2、strip 左右寻找需要删除的字符 lstrip 从左边找  rstrip 从右边找
# string = 'hellow ele'
# print(string.strip('he'))  # llow el 从左右两边找，找到就删除，找不到就停止

# 3、center 居中填充 rjust 居右填充  ljust居左填充
string = 'hello'
print(string.center(9, 'd'))  # 把hello放中间，两边填充d，也可默认填空格
print(string.center(9))

# 4、str.partition(sep) sep 是分隔符
# partition 从左找，找到就分割  rpartition 从右找，找到就分割
string = 'hello world'
print(string.partition('l'))  # ('he', 'l', 'lo world') 返回元组

# 5、str.starstwith 是否以什么开头 endswith 是否以什么结尾

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
# string = 'hello'
# print(string.center(9, 'd'))  # 把hello放中间，两边填充d，也可默认填空格
# print(string.center(9))
#
# # 4、str.partition(sep) sep 是分隔符
# # partition 从左找，找到就分割  rpartition 从右找，找到就分割
# string = 'hello world'
# print(string.partition('l'))  # ('he', 'l', 'lo world') 返回元组

# # 5、str.starstwith 是否以什么开头 endswith 是否以什么结尾
# string = 'hello world'
# print(string.startswith('h'))
# print(string.startswith('wo', 6))  # True 从第6个字符开始计算
# print(string.startswith(('he', 'dd', 'de')))  # True 是否以元组中的其中一个开头
# # endswith 以什么结尾

# 6、str.isalnum() 如果字符串中的所有字符都是字母、文字或数字，则返回True
# str.isalpha() 如果字符串中的所有字符都是字母、文字，则返回True
# str.isdigit() 如果字符串中的所有字符都是数字，则返回True
# str.isspace() 如果字符串中的所有字符都是空白符（空格、换行符、制表符），则返回True

# # 7、str.split() 字符串分割
# string = 'hello world'
# print(string.split('ll'))  # ['he', 'o world'] 返回一个列表
# print(string.split('l'))  # ['he', '', 'o wor', 'd'] 找到3个‘l’，被分成4部分，列表里面有4个元素
# # str.rsplit 从右边找

# 8、str.join(iterable)  字符串、列表、元组、字典、集合都是可迭代对象
a = '\\'  # 单个反斜杠
s1 = 'hello world'
print(a.join(s1))  # h\e\l\l\o\ \w\o\r\l\d
s2 = ['1', '2', '3']
print(a.join(s2))  # 1\2\3
s3 = ('1', '2')
print(a.join(s3))
s4 = {'身高': 170, '体重': 60}  # 身高\体重 字典取键
print(a.join(s4))
s5 = {'1', '2', '5', '1'}  # 5\1\2 去重，集合无序
print(a.join(s5))

# 9、str.count() 查找某个字符出现的次数
# str.find()
# str.rfind() 查找，返回索引

# 10、大小写转换等，具体看课件
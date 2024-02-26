# 三种格式化方法
name = 'lilei'
age = 18

# # 硬凑
# print(name, ',您好!您的年龄是:', age, sep='')
# # 1、%格式化

# print('%s,您好!您的年龄是:%s' % (name, age))  # %s是占位符
# PI = 3.141592653
# print('%.2f' % PI)  # 3.14 转浮点型，保留2位小数
# print('%10.2f' % PI)  # 长度是10，右对齐
# print('%-10.2f' % PI)  # 长度是10，左对齐
# print('%+.2f' % PI)  # +3.14 显示符号
# print('%010.2f' % PI)  # 0000003.14前面填充0

# 2、format函数格式化
print('{},您好!您的年龄是:{}'.format(name, age))
print('{1},您好!您的年龄是:{0}'.format(age, name))  # 根据序号来选参数
print('{h},您好!您的年龄是:{a}'.format(a=age, h=name))
print('{0},您好!您的年龄是:{0}'.format(age, name))
print('{h},您好!您的年龄是:{a}'.format(a=age+1, h=name))
print('{:.2f}'.format(3.14159))  # 3.14精确到小数点后两位

# 3、f-string格式化
print(f'{name},您好!您的年龄是:{age}')  # 占位符里面直接填数据就可以
print(f'{name},您好!您的年龄是:{age:.2f}')  # 保留两位小数
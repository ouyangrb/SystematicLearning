# while 循环
# 1、 while 判断语句：
#     执行语句

# 2、 while True：不清楚循环终止条件时用
# 3、 break 只终止所在的循环
# 4、 while....else...组合：执行完while再执行else
count1 = 0
while count1 < 5:
    print(count1, '小于5')
    count1 += 1
else:
    print(count1, '大于或等于5')

# 5、while的嵌套循环， 九九乘法口诀表，里面对齐用到了制表符\t
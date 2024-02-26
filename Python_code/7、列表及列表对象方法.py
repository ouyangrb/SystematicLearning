lst = [122, 22, 55, 66]
lst2 = lst  # 指向同一个地址
lst[-2] = 999
print(lst)  # [122, 22, 999, 66]  列表原地操作（inplace），
print(lst2)  # [122, 22, 999, 66]  跟着变

# 封包：当多个数据赋值给同一个变量时， 会把他们打包成一个元组
a = 1, 2, 3, 4
print(a)  # (1, 2, 3, 4)

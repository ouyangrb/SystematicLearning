'''
numpy 多维度科学计算
pandas  数据分析（表格型）
matplotlib 可视化
pytorch 和numpy很像，实现了数据的互通，功能很相识
'''
import numpy as np

# 1、查看版本号
# print(np.__version__)

# 2、ndarray 数据类型用 np.array 的创建
# lst = [1, 2, 3]  # array-like参数，可以是列表，元组，range（），一个标量
# arr = np.array(lst)
# print(lst)
# print(arr)
# print(isinstance(arr, np.ndarray))  # ndarray是一个类，arr是它的一个实例对象
# print('__iter__' in dir(arr) and '__getitem__' in dir(arr))  # 判断arr是一个可迭代对象

# lst = [[1, 2, 3], [4, 5, 6]]
# arr = np.array(lst)
# print(lst)
# print(arr)  # 二维数组

# lst = [[1, 2, 3], [4, 5, 6.]]
# arr = np.array(lst)  # 数组arr是一个ndarray类
# print(lst)  # 列表里面的整数数据类型不变
# print(arr)  # 二维数组整数类型全部变为folat，

# 3、ndarray.dtype 方法
# lst = [[1, 2, 3], [4, 5, 6.]]
# arr = np.array(lst, dtype=np.int32)  # arr是一个ndarray类
# print(lst)  # 列表里面的整数数据类型不变
# print(arr)  # 二维数组全部变为np.int32
# print(arr.dtype)  # int32 ndarray类的实例方法，返回arr这个实例的数据类型

# lst = [[1, 2, 3], [4, 5, 6, 7]]
# print(lst)
# arr = np.array(lst)
# print(arr)
# print(arr.dtype)  # lst形状不一样，报错

# 4、ndarray.shape方法
lst = [[1, 2, 3, 8], [4, 5, 6, 7]]
arr = np.array(lst)
print(arr.shape)  # (2, 4) 形状是2行4列，二维可以这样记忆，多维高维建议不要这样记忆

lst = [[[1, 2], [3, 8], [4, 5], [6, 7]]]
arr = np.array(lst, dtype= np.int32)
print(arr.shape)  # (1, 4, 2) 注意是个元组
print(arr.ndim)  # 3 维度或轴的数量
print(arr.size)  # 8 数组元素的总个数=shape里面相乘  8 = 1*4*2
print(arr.itemsize) # 4个字节大小  数组中元素的大小以字节为单位

lst = [1, 2, 3, 4]
arr = np.array(lst)
print(arr.shape)  # (4,) 注意是个元组

lst = 111  # 标量
arr = np.array(lst)
print(arr.shape)  # () 注意是个空元组
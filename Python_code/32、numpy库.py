'''
numpy 多维度科学计算
pandas  数据分析（表格型）
matplotlib 可视化
pytorch 和numpy很像，实现了数据的互通，功能很相识
'''
import numpy as np
# 一、数组的基本知识
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
# lst = [[1, 2, 3, 8], [4, 5, 6, 7]]
# arr = np.array(lst)
# print(arr.shape)  # (2, 4) 形状是2行4列，二维可以这样记忆，多维高维建议不要这样记忆
#
# lst = [[[1, 2], [3, 8], [4, 5], [6, 7]]]
# arr = np.array(lst, dtype= np.int32)
# print(arr.shape)  # (1, 4, 2) 注意是个元组
# print(arr.ndim)  # 3 维度或轴的数量
# print(arr.size)  # 8 数组元素的总个数=shape里面相乘  8 = 1*4*2
# print(arr.itemsize) # 4个字节大小  数组中元素的大小以字节为单位
#
# lst = [1, 2, 3, 4]
# arr = np.array(lst)
# print(arr.shape)  # (4,) 注意是个元组
#
# lst = 111  # 标量
# arr = np.array(lst)
# print(arr.shape)  # () 注意是个空元组

# 5、np.asarray 返回视图情况
# lst = [1, 2, 3]
# arr1 = np.array(lst)
# arr2 = np.asarray(lst)
# lst[-1] = 4
# print(lst)
# print(arr1)
# print(arr2)
#
# arr0 = np.array([1, 2, 3])
# arr1 = np.array(arr0)
# arr2 = np.asarray(arr0) # 返回视图条件1：形参arr0是数组
# arr0[-1] = 4
# print(arr0)
# print(arr1)
# print(arr2)  # [1 2 4] arr2跟着arr0变化，arr2返回的是一个视图
#
# arr0 = np.array([1, 2, 3])
# arr1 = np.array(arr0)
# arr2 = np.asarray(arr0, dtype=np.int64)  # 返回视图条件2：形参arr0类型和arr2一致
# arr0[-1] = 4
# print(arr0)
# print(arr1)
# print(arr2)  # arr2和arr0类型不一样，不会跟着变

# # 6、np.copy() 返回一个数组   arr.copy()  # 实例对象arr调用对象方法
# lst = [1, 2, 3]
# print(np.copy(lst))  # [1 2 3] 拷贝之后一定是ndarray
#
# arr = np.array([1, 2, 3])  # np包调用copy函数  （可以传任何的array-like（列表，元组，数组等） 返回一个数组
# arr2 = arr.copy()  # 实例对象arr调用对象方法，返回一个新数组 （只能用数组实例对象调用）
# print(arr2)  # [1 2 3]

# 7、np.fromiter 只能适用一维，用的少

# 8、np.empty()  创建未初始化的数组，未初始化意思是每次打印数值是随机的
# print(np.empty((3, 2)))  # 默认是np.float64
#
# # 9、np.empty_like() 模仿数组形状创建出新的数组
# arr0 = np.array([[1, 2], [3, 4]])
# print(np.empty_like(arr0))

# 10、np.zeros（） np.zeros_like()  创建全0数组
# 11、np.ones() np.ones_like
# 12、np.full()  np.full_like
# print(np.full((3, 2), 8))  # 创建全8数组
# 13、np.eye 创建单位矩阵
# print(np.eye(6, dtype=np.int32))
# print(np.eye(6, 4))
# 24、np.identity() 只能是二维方阵

# 25、从数值范围创建数组 np.arange()
# print(list(range(1, 8, 2)))  # [1, 3, 5, 7] range()返回一个可迭代对象
# print(list(range(8, 1, -2)))  # [8, 6, 4, 2]也可以从大大小
#
# print(np.arange(1, 8, 2))  # [1 3 5 7]
# print(np.arange(8, 1, -2))  # [8 6 4 2]
#
# # print(list(range(1., 8., 2.)))  # 报错range里面不能是float
# print(np.arange(1., 8., 2.1))  # [1.  3.1 5.2 7.3] 不报错
# print(np.arange(1, 8, 2, dtype=np.float64))  # [1. 3. 5. 7.]
#
# arr0 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# print(arr0.shape)  # (8,)
# arr1 = np.reshape(arr0, (2, 4))  # np包reshape函数调用，返回一个新数组
# print(arr1.shape)  # (2, 4)
# arr2 = np.reshape(arr0, (2, 1, 4, 1))
# print(arr2.shape)  # (2, 1, 4, 1) reshape保证数组实例的size属性不变
#
# print(arr2.reshape((2, 4)).shape)  # (2, 4) arr2.reshape 实例对象调用对象方法
#
# arr3 = np.reshape(arr0, (-1, 2))  # -1表示让数组在这个维度上自行推断
# print(arr3.shape)  # (4, 2)
#
# arr4 = np.reshape(arr2, (8,))  # 这四行等价，扁平化操作
# arr5 = np.reshape(arr2, (-1,))
# arr6 = np.reshape(arr2, 8)
# arr7 = np.reshape(arr2, -1)
# print(arr5.shape)  # (8,)
# print(arr5)  # [1 2 3 4 5 6 7 8]
# print(arr6)  # [1 2 3 4 5 6 7 8]
# print(arr7)  # [1 2 3 4 5 6 7 8]
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# new_arr = np.reshape(lst, (2, 4))  # reshape方法调用可直接传列表、元组、数组
# print(new_arr)
#
# print(np.arange(24))  #  0到24步长默认是1 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
# print(np.arange(24).reshape((2, 3, 4)))
#
# # 26、np.linspace()获取等差数组 np.logspace()获取等比数组
#
# arr = np.array(8)  # 标量
# print(arr.shape)  # ()

# 二、数组的基本运算
# # 1、广播机制：标量都可以广播、后缘维度一致可以广播、后缘一致前缘维度是1、
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr + 2)  # 广播机制，逐元素加2
# print(arr % 2)
# print(arr > 2)
#
#
# a = np.arange(2).reshape(2, 1)
# b = np.arange(12).reshape((2, 1, 2, 3))
# print(a)
# print(b)
# print(a + b)  # 广播机制

# 三、索引和切片 numpy里面是ndarray类型   pytorch里面是tensor（张量）类型
# 1、数组支持和列表类似的索引和切片操作
# arr = np.arange(2, 9)
# print(arr)  # [2 3 4 5 6 7 8]
# item = arr[-2]  # **数组切片有返回值，新建操作（和列表一致）**
# arr[-2] = 9  # 可以理解为arr实例属性的修改
# print(arr)  # [2 3 4 5 6 9 8]
# print(item)  # 7

# arr = np.arange(2, 9)
# arr1 = arr[1: -1]  # **数组切片是视图操作，跟着arr一块变 （列表切片是新建操作）**
# print(arr1)  # [3 4 5 6 7]
# arr[-2] = 9
# print(arr1)  # [3 4 5 6 9]
#
# arr = np.arange(2, 9)
# arr[1:4] = [11, 12, 13]
# print(arr)  # [ 2 11 12 13  6  7  8]
# arr[1:4] = 10
# print(arr)  # [ 2 10 10 10  6  7  8] 数组切片也会广播
# arr[1:4] = [10]
# print(arr)  # [ 2 10 10 10  6  7  8] 数组切片也会广播

# 数组和列表类似的索引和切片
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr)
# print(arr[1][0])  # 3
# print(arr[:2][1:2])  # [[3,4]] 切片不降维

# 重点：
# 数组特有的：针对维度的索引和切片操作
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr[1, 0])  # 索引
# print(arr[0:2, 1:2])  # 切片

# 特殊索引
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# #
# print(arr[[1, 0, 1]])  # 等价于 arr[1],arr[0],arr[1]的结果组成一个更高维度的数组（该操作不降低维度）
# # 花式索引，等价于arr[1, 0],arr[0,1],arr[2,0]的结果组成一个更高维度的数组
# print(arr[[1, 0, 2], [0, 1, 0]])  # [3 2 5]
# # 布尔索引 对应True的留下，False的删除，掩码的感觉
# print(arr[[True, False, True]])
# # 逐个元素的掩码
# print(arr[arr > 3])  # [4 5 6] 理解如下:
# print(arr > 3)
# '''
# [[False False]
#  [False  True]
#  [ True  True]]
# '''
# print(arr[[[False, False], [False,  True], [True,  True]]])  # [4 5 6]

# 四、常用np包函数方法
# 1、np.reshape() arr.reshape() 都是新建数组
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr.reshape((1, 6)))  # [[1 2 3 4 5 6]] np.reshape()处理的形参对象更多
# # np.resize() 是新建数组  arr.resize()是原地操作，对size大小不做要求，可填充
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(np.resize(arr, (1, 6)))  # [[1 2 3 4 5 6]]
# print(np.resize(arr, (1, 9)))  # [[1 2 3 4 5 6 1 2 3]] np.resize会重复使用前面的数据 size不用保持一致
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# arr.resize((2, 3))
# print(arr)
# arr.resize((2, 5))  # 对size元素个数无要求，少了就补0
# print(arr)
#
# # 2、ndarray.flatten() 扁平化
# arr = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr.flatten())  # [1 2 3 4 5 6]

# 3、ndarray.T 转置
# 4、np.swapaxes(arr, 0, 2) 交换轴
# 5、np.transpose 既有转置和交换轴的功能，用的较多
arr = np.array([[1, 2], [3, 4], [5, 6]]).reshape((1, 2, 3))
print(arr.shape)
arr1 = np.transpose(arr, (1, 2, 0))
print(arr1.shape)  # (2, 3, 1)

# 6、np.expand_dims 增加1维度，size不会改变，增加维度
arr = np.array(8)
print(arr.shape)  # () 标量的shape
print(np.expand_dims(arr, axis=0).shape)  # (1,) 增加1维
print(np.expand_dims(arr, axis=(0, 1)).shape)  # (1, 1) 标量增加2维

arr = np.arange(24).reshape((2, 3, 4))
print(np.expand_dims(arr, axis=1).shape)  # (2, 1, 3, 4)

# 7、np.squeeze() 指定轴删除维度1，或者把维度是1的全部删除，降维
# 8、np.concatenate(a1, a2) 拼接

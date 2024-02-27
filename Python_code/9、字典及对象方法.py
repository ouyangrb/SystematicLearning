# 键值对
# 字典的健是唯一的，如果健重复，对应的值会被覆盖更新；值没有这个特点
# 字典的健必须是不可变的数据类型，值没有要求
# 字典是可变的，字典不是序列，不能用索引和下标去切片


dic = {'name': 'lilei', 'age': 18}
print(len(dic))  # 2 可以求长度#
# 访问
print(dic['name'])
# 修改
dic['age'] = 25
print(dic)  # {'name': 'lilei', 'age': 25}
dic['weight'] = 60
print(dic)  # {'name': 'lilei', 'age': 25, 'weight': 60} 新增键值对

# zip操作 zip(*iterable) 传多个可迭代对象
# 拉链操作
iter1 = 'abcd'
iter2 = [1, 2, 5]
res = zip(iter1, iter2)
print(res)  # 迭代器 <zip object at 0x000001A2C6750480>
print(list(res))  # [('a', 1), ('b', 2), ('c', 5)]


# 创建字典的几种方法
# 1、dic = {'name': 'lilei', 'age': 18}
# 2、
dic = {}
dic['name'] = 'lilei'
dic['age'] = 25
print(dic)
# 3、内中函数dict(iterable)
dic1 = dict([('name', 'lilei'), ('age', 95)])
print(dic1)

dic2 = dict(zip(['name', 'age'], ['lilei', 66] ))
print(dic2)  # {'name': 'lilei', 'age': 66}

# 4、
dic3 = dict({'name': 'lilei', 'age': 58})
print(dic3)
# 5、
print(dict(name='lilei', age=26))  # {'name': 'lilei', 'age': 26}

# 6、 类方法创建 不常用
print(type(dic) == dict)  # True 字典的类型是dict
# dict float bool complex list str tuple 本质都是class（类）
print(type(dic).fromkeys('abcd', '123'))  # {'a': '123', 'b': '123', 'c': '123', 'd': '123'}


# 字典的对象方法
# 1、keys（）返回所有健的值
# 2、get() 拿到指定健的值
# 3、 update 更新
dic4 = dict({'name': 'lilei', 'age': 58})
dic4.update({'weight': 65})
dic4.update(weight=66, gender='male')
dic4.update([('weight', 33), ('age', 88)])
dic4.update(zip(('weight', 'age'), (99, 100)))
print(dic4)

# 4、pop() 删除键值对，找不到对应的健会放回提示值
# 5、popitem() 移除最后一个键值对
# 6、setdefault ()当健存在，返回对应的值； 当健不存在时候，会新增键值对
# 7、copy（）浅拷贝 clear（）清空


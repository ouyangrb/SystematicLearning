# 集合元素的唯一性，相同的元素会去重
set1 = {2, 1, 3, 8, 7}
print(set1)  # {1, 2, 3, 7, 8} 集合是无序的
print(type(set1))  # <class 'set'>

empty_set = set()  # 只能这样创建空集合

string = 'aasdf'
print(set(string))  # {'f', 'd', 's', 'a'}

# 集合元素必须是不可变的数据类型
# 集合不是序列，不能索引和切片

frozenset()  # 冻结集合，不可变的

# 集合一般用来去重和关系测试
lst = [1, 2, 3, 3, 4]
print(list[set(lst)])  # list[{1, 2, 3, 4}]

# 父集，子集，并集，交集，对称差
# print（set1 > set2）  # 判断是否为父集
# print(set1 & set2)  # 求交集 ；|求交集 ； -求差集 ； ^ 求对称差（并集-交集）

# 集合对象方法 见课件

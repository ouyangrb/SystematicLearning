# # 备份时候用到拷贝
# a = [111, 222, 333]
#
# # 列表浅拷贝的三种方式
# b = a.copy()
# print(b)
# b = a[:]
# import copy
# b = copy.copy(a)
#
# # 深拷贝
# b = copy.deepcopy(a)

'''
浅拷贝（复制一份数据）：（发生浅拷贝的意思是id不同，id相同就是引用
会发生copy的数据类型有： list， dict， set
不会发生copy的数据类型有： numpy， str， tuple

小结：
如果被拷贝的数据本身是可变的数据类型，那么该拷贝会发生；否则，为引用关系
浅层拷贝对于该数据内部的元素不发生拷贝，都为引用关系
'''

import copy
'''
深拷贝：（内部存在可变数据类型，都会发生拷贝）
会发生copy的数据类型有： list， dict， set， tuple（内部存在可变数据）
不会发生copy的数据类型有： numpy， str， tuple（内部不存在可变数据）

小结：
如果被拷贝的数据本身是可变的数据类型，或者其内部包含有可变数据类型，发生拷贝
如果被拷贝的数据本身是不可变的数据类型，或者其内部不包含有可变数据类型，为引用关系
'''
aa = [12, [12]]
bb = copy.deepcopy(aa)
print(id(aa[0]))
print(id(bb[0]))
print(id(aa[1]))
print(id(bb[1]))
# class Person:
#     def __init__(self, name, school, age):
#         self.name = name
#         self.school = school
#         self.age = age
#         self.show()
#     def show(self):
#         print(f'我是{self.name},我今年{self.age}')
# class Student(Person):
#     count = 0
#     def __init__(self, name, school, age, department):
#         self.department = department
#         super(Student, self).__init__(name, school, age)
#         Student.count += 1
#         self.show2()
#     def show2(self):
#         print(f'我在{self.department}')
#
# a = Student('LILEI', '_', 18, '学生部门1')
# b = Student('LILEI', '_', 20, '学生部门2')
# print(f'报道人数是:{Student.count}')




class ListIter:  # 列表迭代器,迭代器要同时实现__iter__，__next__方法

    def __init__(self, iterator):
        self.iterator = iterator
        self.index = 0
    def __iter__(self):
        pass
    def __next__(self):
        try:
            ret = self.iterator.iterable[self.index]  # self.index 在第一次遍历就到了最大索引位置，第二次就停止迭代
            self.index += 1  # 执行一次，修该一次实例属性self.index = 0
            return ret
        except IndexError:  # 抛出索引异常
            raise StopIteration
class Mylist:
    def __init__(self, iterable=(), /):
        *self.iterable, = iterable
    def __str__(self):
        return f'{self.iterable}'
    def __getitem__(self, item):  # 更希望这个执行索引和切片
        return self.iterable[item]
    def __len__(self):
        i = 0
        for i, _ in enumerate(self.iterable, 1):
            pass
        return i
    def __iter__(self):  # 迭代过程中优先找__iter__方法，该方法需要返回一个迭代器，所以要新建一个迭代器
        return ListIter(self)
lst = [1, 2, 3]
my_list = Mylist(lst)
# print(my_list)
# print(len(my_list))

for i in my_list:
    print(i)
# print(my_list[0])
# print(my_list[1:3])
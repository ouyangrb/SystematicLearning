class Person:
    def __init__(self, name, school, age):
        self.name = name
        self.school = school
        self.age = age
        self.show()
    def show(self):
        print(f'我是{self.name},我今年{self.age}')
class Student(Person):
    count = 0
    def __init__(self, name, school, age, department):
        self.department = department
        super(Student, self).__init__(name, school, age)
        Student.count += 1
        self.show2()
    def show2(self):
        print(f'我在{self.department}')

a = Student('LILEI', '_', 18, '学生部门1')
b = Student('LILEI', '_', 20, '学生部门2')
print(f'报道人数是:{Student.count}')

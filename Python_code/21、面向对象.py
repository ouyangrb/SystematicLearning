# 类, 类对象; 所有类都默认继承object, 一般不写, object可以称之为父类, 基类, 超类
class Teacher(object):

    school = '深兰大学'  # 2、类属性(类变量)

    # 方法: 类当中的函数，函数在类里面就是方法
    # 魔术方法(特殊方法): 官方定义好的（自己不能定义）, 以两个下划线开头并且以两个下划线结尾的方法
    # 魔术方法的特点: 一般不需要主动调用, 在特定情况下, 自动调用
    def __init__(self, name, age, address):
        # 1、实例属性(实例变量)
        self.name = name            # teacher1.name = '老李'              teacher2.name = '老张'
        self.age = age              # teacher1.age = 37                   teacher2.age = 38
        self.address = address      # teacher1.address = '威宁路37号'       teacher2.address = '威宁路38号'

    def init(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def teach(self, course):  # 对象方法: 第一个参数位隐式的接收了实例对象
        print(f'{self.name}正在授{course}课')

    @classmethod  # 类方法装饰器
    def teach(cls, course):  # 类方法: 第一个参数位隐式的接收了类对象
        print(f'{cls.school}的老师正在授{course}课')

    @staticmethod  # 静态方法装饰器
    def teach(course):
        print(f'{Teacher.school}的老师正在授{course}课')


"""
0、每次实例化时, 会自动调用__new__(cls)方法（该方法在父类object中）, 把要实例化的类对象和其他的实参打包, 其中类对象作
为实参传递给cls, 然后__new__方法会根据该类对象创建出一个实例对象(obj), __new__再去调用
__init__(self)方法, 把刚刚创建的实例对象(obj)作为实参传递给self, 把打包的其他实参传递给
__init__方法里面的其他形参, __init__再对该实例对象进行属性的初始化操作(inplace), 最后
再由__new__返回初始化之后的实例对象(obj)

所以__init__必须返回None, 我们把__new__称之为构造方法, 把__init__称之为初始化方法
"""

teacher1 = Teacher('老李', 37, '威宁路37号')  # 实例化返回一个实例对象
teacher2 = Teacher('老张', 38, '威宁路38号')

""" 类方法的调用规则: 既可以用类对象去调用(推荐), 也可以用实例对象去调用 """
# Teacher.teach('英语')
# teacher1.teach('数学')  # 本质上 type(teacher1).teach('数学')

""" 静态方法的调用规则: 既可以用类对象去调用(推荐), 也可以用实例对象去调用 """
# Teacher.teach('英语')
# teacher1.teach('数学')


""" 对象方法的调用规则: 只能用实例对象去调用 """
# teacher1.teach('数学')  # 等价于 Teacher.teach(teacher1, '数学')  不推荐
# teacher2.teach('语文')  # 等价于 Teacher.teach(teacher2, '数学')  不推荐

# teacher2.__init__('张三疯', 48, '威宁路38号')
# print(teacher2.name)
# print(teacher2.age)
# print(teacher2.address)

""" 3、实例属性调用规则: 只能用实例对象去调用 """
# print(getattr(teacher1, 'names', 'laoli'))
# print(teacher1.age)
# print(teacher2.age)

""" 4、类属性调用规则: 既可以用类对象去调用(推荐用类方法调用), 也可以用实例对象去调用
    当实例属性名和类属性名相同时, 实例对象优先调用实例属性 """
# print(getattr(Teacher, 'school', 'laoli'))
# print(Teacher.school)
# print(teacher1.school)  # 本质 用type类型调用   print(type(teacher1).school)
# print(teacher2.school)  # 本质 print(type(teacher2).school)

""" 5、修改实例属性: 只能用实例对象访问到该属性, 再重新赋值 """
# print(teacher1.age)
# teacher1.age = 47
# print(teacher1.age)

""" 6、修改类属性: 只能用类对象访问到该属性, 再重新赋值 """
# print(Teacher.school)
# Teacher.school = '深兰教育'
# print(Teacher.school)
# print(teacher1.school)
# print(teacher2.school)

""" 7、动态定义实例属性: 当实例对象修改的属性不存在时, 会新增一个该实例属性 """
# setattr(teacher1, 'grade', '二年级')
# print(teacher1.grade)

# print(teacher1.school)
# teacher1.school = '深兰教育'
# print(teacher1.school)
# print(Teacher.school)
# print(teacher2.school)

""" 8、动态定义类属性: 当类对象修改的属性不存在时, 会新增一个该类属性 """
# setattr(Teacher, 'department', '教学部')
# print(Teacher.department)

# print(Teacher.eat)
# Teacher.eat = 'rice'
# print(Teacher.eat)
# print(teacher1.eat)
# print(teacher2.eat)

""" 9、删除属性 """
# delattr(Teacher, 'school')  # 等价于 del Teacher.school
# del Teacher.eat
# # print(Teacher.eat)
# del teacher1.age
# print(teacher2.age)

""" 判断属性是否存在 """
# print(hasattr(Teacher, 'schools'))
# print(hasattr(teacher1, 'ages'))

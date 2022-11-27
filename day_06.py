"""
第六天学习
"""
# 面向对象进阶
"""
@property装饰器
之前我们讨论过Python中属性和方法访问权限的问题，虽然我们不建议将属性设置为私有的，
但是如果直接将属性暴露给外界也是有问题的，比如我们没有办法检查赋给属性的值是否有效。
我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，
那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。如果要做到这点，
就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器，getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器，setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f"{self._name}正在玩飞行棋")
        else:
            print(f"{self._name}正在玩斗地主")


"""
__slots__魔法
我们讲到这里，不知道大家是否已经意识到，Python是一门动态语言。通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，
可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
"""


class Person_2(object):
    __slots__ = ('_name', "_age", "_gender")

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器，getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器，setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f"{self._name}正在玩飞行棋")
        else:
            print(f"{self._name}正在玩斗地主")


"""
静态方法和类方法
之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，
通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，
因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象方法，
因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），
所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题
"""
from math import sqrt


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


"""
和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，
它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），
通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
"""
from time import *


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


"""
继承和多态
刚才我们提到了，可以在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，
在实际开发中，我们经常会用子类对象去替换掉一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则。
"""


class Person_3(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print(f"{self._name}正在愉快的玩耍")

    def watch_av(self):
        if self._age <= 18:
            print(f"{self._name}只能观看《熊出没》")
        else:
            print(f"{self._name}正在观看爱情片！")


class Student(Person_3):
    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print(f"{self._grade}的{self._name}正在学习{course}")


class teacher(Person_3):
    def __init__(self, name, age, title):
        self._name = name
        self._age = age
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print(f"{self.name}{self._title}正在讲{course}")


"""
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override）。
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，
不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。
"""
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print(f"{self._nickname}:汪汪汪。。。")


class Cat(Pet):
    def make_voice(self):
        print(f"{self._nickname}:喵喵喵。。。")


"""
综合案例：
"""
# 案例1：奥特曼打小怪兽
from abc import *
from random import *


class Fighter(object):
    """攻击者"""
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """必杀技"""
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击"""
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
                return True
            else:
                return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return f"~~~{self._name}奥特曼~~~\n\
                生命值：{self._hp}\n\
                魔法值：{self._mp}"


class Monster(Fighter):
    """小怪兽"""
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return f"~~~{self._name}小怪兽~~~\n\
                生命值：{self._hp}"


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
        else:
            return False


def select_alive_one(monsters):
    """选中一只活着的怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """显示奥特曼与小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end=' ')


# 工资结算系统
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import *


# 员工类
class Employee(object, metaclass=ABCMeta):
    def __init__(self, name):
        # 初始化
        self._name = name

    @property
    def name(self):
        # 访问属性
        return self._name

    @abstractmethod
    def get_salary(self):
        # 获得月薪
        pass


# 部门经理类
class Manager(Employee):  # 部门经理类(继承员工类)
    def get_salary(self):
        # 重写月薪方法
        return 15000.0


# 程序员类
class Programmer(Employee):  # 程序员类(继承员工类)
    def __init__(self, name, working_hour=0):  # 定义程序员名称与工作时长，定义默认时长为0
        super.__init__(name)
        self._working_hour = working_hour

    @property
    # 访问工作时长属性
    def working_hour(self):
        return self._working_hour

    @working_hour.setter  # 修改工作时长方法
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        # 重写月薪方法
        return self._working_hour * 150


# 销售员类
class Salesman(Employee):  # 销售员类(继承员工类)
    def __init__(self, name, sales=0):  # 初始化销售员的姓名以及销售额，销售额设置默认为0
        super().__init__(name)
        self._sales = sales

    @property
    # 访问销售额属性
    def sales(self):
        return self._sales

    @sales.setter
    # 修改销售额属性
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        # 重写月薪方法
        return 1200 + self._sales * 0.5

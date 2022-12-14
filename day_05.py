"""
第五天学习
"""


# 面向对象编程基础
# 定义类
class Student(object):
    # 初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, scoure_name):
        print('%s正在学习%.s' % (self.name, scoure_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》' % self.name)
        else:
            print('%s正在观看岛国爱情大电影' % self.name)


# 私有属性
class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


"""
练习
"""


# 练习1：定义一个类描述数字时钟
class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
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
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置"""
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量"""
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离"""
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))

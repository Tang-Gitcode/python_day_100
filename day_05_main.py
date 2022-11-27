from day_05 import Student
from day_05 import Test
from day_05 import Clock
from day_05 import Point
from time import sleep


def main_Student():
    stu1 = Student('唐展豪', 21)
    stu1.study('程序与设计')
    stu1.watch_movie()
    stu2 = Student('某某', 17)
    stu2.study('思想与政治')
    stu2.watch_movie()


def main_Test():
    test = Test('hello')
    # test.__bar()
    # print(test.__foo)
    test._Test__bar()
    print(test._Test.__foo)


def main_clock():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


def main_move():
    p1 = Point(1, 5)
    p2 = Point()
    print(p1, p2)
    p2.move_by(-1, 2)
    print(p2)
    p1.distance_to(p2)
    print(p1)


if __name__ == '__main__':
    # main_Student()
    # main_Test()
    # main_clock()
    main_move()

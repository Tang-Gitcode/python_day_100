from day_06 import Person
from day_06 import Triangle
from day_06 import Clock
from day_06 import Person_3, Student, teacher
from day_06 import Pet, Dog, Cat
from day_06 import Fighter, Ultraman, Monster, select_alive_one, is_any_alive, display_info
from time import sleep
from abc import *
from random import *
from day_06 import Person_3


def main_play():
    person = Person('唐展豪', 16)
    person.play()
    person.age = 18
    person.play()


def main_play_2():
    person = Person('唐展豪', 16)
    person.play()
    person._gender = '男'
    # person.age = 18
    # person.play()


def main_valid():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(f"周长为：{t.perimeter()}")
        print(f"面积为：{t.area()}")
    else:
        print('无法构成三角形')


def main_lcock():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


def main_person_3():
    person = Student('唐展豪', 21, "高三")
    person.study('数学')
    t = teacher("某某", 17, '砖家')
    t.teach('Python程序设计')
    t.watch_av()


def main_Pet():
    pets = [Dog('大黄'), Cat('凯蒂')]
    for pet in pets:
        pet.make_voice()


def main_fighter():
    u = Ultraman('骆昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)  # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    # main_play()
    # main_play_2()
    # main_valid()
    # main_lcock()
    # main_person_3()
    # main_Pet()
    main_fighter()
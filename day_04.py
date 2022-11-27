"""
第四天学习
"""
# 字符串和常用数据结构
import sys

s1 = '\'hello world!\''
s2 = '\n\\hello world!\\\n'
print(s1, s2, end='')

# \后面跟八进制或十六进制字符来表示字符，也可以跟unicode字符编码来表示字符
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

# 字符串前面加r说明不希望\后面的字符转义
s1 = r'\'helloworld!\''
s2 = r'\n\\helloworld!\n\\'
print(s1, s2)

# Python为字符串类型提供了非常丰富的运算符，我们可以使用+运算符来实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），我们也可以用[]和[
# :]运算符从字符串取出某个字符或某些字符（切片运算）
s1 = 'hello' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)
str2 = 'abc123456'
print(str2[2])
print(str2[2:5])
print(str2[2:])
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])

# 我们还可以通过一系列的方法来完成对字符串的处理
str1 = 'hello, world!'
# 计算字符串长度
print(len(str1))
# 获取首字母大写的拷贝
print(str1.capitalize())
# 获取每个单词首字母大写的拷贝
print(str1.title())
# 获的字符串变大写后的拷贝
print(str1.upper())
# 从字符串中查询字串的位置
print(str1.find('or'))
print(str1.find('shit'))
# 检查字符串是否已指定字符串开头
print(str1.startswith('He'))
print(str1.startswith('hel'))
# 检查字符串中是否已指定字符串结尾
print(str1.endswith('!'))
# 将字符串以指定的宽度居中，并在两边填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.ljust(50, '-'))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())
# 检查字符串是否由字母构成
print(str2.isalpha())
# 检查字符串是否以数字和字符串构成
print(str2.isalnum())
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪两边空格之后的拷贝
print(str3.strip())

# 格式化输出字符串
a, b = 5, 10
print('%d*%d=%d' % (a, b, a * b))
# 字符串提供的方法来输出字符串
print('{0}*{1}={2}'.format(a, b, a * b))
# Python 3.6以后，格式化字符串还有更为简洁的书写方式，就是在字符串前加上字母f
print(f'{a}*{b}={a * b}')

# 使用列表
list1 = [1, 3, 5, 7, 100]
print(list1)
list2 = ['hello'] * 3
print(list2)
print(len(list1))
print(list1[1])
print(list1[4])
print(list1[-1])
print(list1[-3])
list1[2] = 300
print(list1)

# 通过循环用下标遍历列表元素
for i in range(len(list1)):
    print(list1[i], end=',')
print()
# 通过for循环遍历列表元素
for j in list1:
    print(j, end=',')
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for i, j in enumerate(list1):
    print(j, [i])

# 如何向列表中添加元素以及如何从列表中移除元素
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200)
list1.insert(1, 400)
print(list1)
# 合并两个列表
list1 += [1000, 2000]
print(list1)
print(len(list1))
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)
# 从指定位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)
# 清空列表元素
list1.clear()
print(list1)

# 和字符串一样，列表也可以做切片操作，通过切片操作我们可以实现对列表的复制或者将列表中的一部分取出来创建出新的列表
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4)
# 可以通过反向切片操作来获得倒转后的列表拷贝
fruits5 = fruits[::-1]
print(fruits5)

# 列表排序
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# 正序排列
print(sorted(list1))
# 倒序排列
print(sorted(list1, reverse=True))
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
print(sorted(list1, key=len))
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

# 生成式和生成器
# 我们还可以使用列表的生成式语法来创建列表
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
f = [x ** 2 for x in range(1, 1000)]
print(f)
# 查看对象占用内存的字节数
print(sys.getsizeof(f))
# 创建一个生成器对象而不是一个列表
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
for i in f:
    print(i, end=',')
print()


# Python中还有另外一种定义生成器的方式，就是通过yield关键字将一个普通函数改造成生成器函数。
def lib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for i in lib(20):
        print(i, end=',')


if __name__ == '__main__':
    main()

print()
"""
使用元组
Python中的元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，
不同之处在于元组的元素不能修改，在前面的代码中我们已经不止一次使用过元组了。顾名思义，
我们把多个元素组合到一起就形成了一个元组，所以它和列表一样可以保存多条数据。
"""
# 定义元组
t = ('骆昊', 38, True, '四川成都')
# 打印元组数据
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for i in t:
    print(i, end=' ')
print()
# 重新给元组赋值
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转换为列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = '32'
print(person)
# 将列表转化为元组
person_tuple = tuple(person)
print(person_tuple)

"""
使用集合
Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。
"""
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
# 打印集合
print(set1)
# 计算集合的长度
print('length=', len(set1))
# 创建集合的构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 向集合添加元素和向集合删除元素
set1.add(4)
print(set1)
set1.add(5)
print(set1)
set1.update([11, 12])
print(set1)
set1.discard(5)
print(set1)
if 4 in set2:
    set2.remove(4)
    print(set2)
print(set1, set2)
print(set3.pop())
print(set3)

# 集合的成员、交集、并集、差集等运算
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)  # 交集
print(set1 | set2)  # 并集
print(set1 - set2)  # 差集
print(set1 ^ set2)  # 对称
# 判断子集和超集
print(set2 <= set1)
print(set3 <= set1)
print(set1 >= set2)
print(set1 >= set3)

"""
使用字典
字典是另一种可变容器模型，Python中的字典跟我们生活中使用的字典是一样一样的，它可以存储任意类型对象，
与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开。
"""
# 创建字典的字面量语法
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# 打印字典
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
print(items1)
# 通过zip函数将两个序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
print(items2)
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items3)
# 通过键可以获取字典中对应的值
print(scores['骆昊'])
print(scores['狄仁杰'])
# 对字典中所有的键值进行遍历
for i in items3:
    print(f'{i}:{items3[i]}', end=' ')
print()
# 更新字典中的元素
scores['白元芳'] = 87
print(scores)
scores['诸葛王朗'] = 71
print(scores)
scores.update(冷面=67, 方启鹤=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值，但是可以设置默认值
print(scores.get('武则天', 60))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores)
print(scores.pop('骆昊', 100))
print(scores)
# 清空字典
print(scores.clear())
print(scores)

"""
练习
1.在屏幕上显示跑马灯文字
"""
# import os
# import time
# def main():
#     content = '北京欢迎你为你开天辟地......'
#     while True:
#         #清理屏幕上的输出
#         os.system('cls')
#         print(content)
#         #强制休眠200毫秒
#         time.sleep(200)
#         content = content[1:] + content[0]
#
# if __name__ == '__main__':
#     main()

# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random


def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    main()


# 练习6：打印杨辉三角
def main():
    num = int(input('请输入行数: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()

"""
综合案例
案例1：双色球选号。
"""
from random import *


def display(balls):
    # 输出列表中双色球的号码
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    # 随机选一组号码
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()

"""
综合案例2：
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    persons = [True] * 30
    content, index, number = 0, 0, 0
    while content < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[number] = False
                content += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end=' ')
    print()


if __name__ == '__main__':
    main()

"""
综合案例3：井字棋游戏
"""
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()

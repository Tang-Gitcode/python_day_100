"""
4.循环结构
"""
# for-in循环
# 用for 循环实现1-100求和
# 第一种方法：
# 定义和的初始值为0
sum = 0
# 将变量设为i,并将每个变量循环相加
for i in range(1, 101):
    sum = sum + i
print(f'1-100的和为：{sum}')

# 第二种方法：
sum = 0
for i in range(101):
    sum += i
print(f'1-100的和为：{sum}')

# 实现1-100偶数求和
sum = 0
for i in range(100, 0, -2):
    sum = sum + i
print(f'1-100的偶数和为：{sum}')

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)

# while循环
# import random
#
# ran_num = random.randint(1, 100)
# acount = 0
# while True:
#     acount += 1
#     num = int(input('请输入你要猜的数字'))
#     if num > ran_num:
#         print('猜大了！')
#     elif num < ran_num:
#         print('猜小了！')
#     else:
#         print('恭喜你，猜对了！')
#         break
# print(f'你总共猜了{acount}次')
# if acount > 7:
#     print('你的智商明显不够用！')
# else:
#     print('你真聪明！')

# 九九乘法表
# for i in range(1, 10):
#     print(end='\n')
#     for j in range(1, i + 1):
#         print(f'{j}*{i}={i*j}', end='\t')
# print()
#
# # 练习1：输入一个正整数判断是不是素数。
# from math import sqrt
#
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)
#
# #
# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就交换x和y的值
# if x > y:
#     # 通过下面的操作将y的值赋给x, 将x的值赋给y
#     x, y = y, x
# # 从两个数中较小的数开始做递减的循环
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break

# 练习3：打印三角形
for i in range(1, 6):
    print()
    for j in range(1, i + 1):
        print('*', end='')
print()

"""
5:构造程序逻辑
"""
# 百钱百鸡问题：公鸡:5/只，母鸡：3元/只，小鸡：1元/三只，问：100元买100只鸡能买公鸡、母鸡、小鸡各多少只？
# 设公鸡x只，母鸡y只，那么小鸡有100-x-y只
for x in range(1, 21):
    for y in range(1, 34):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print(f'公鸡有：{x}只，母鸡有{y}只，小鸡有{z}只。')

# 赌博游戏。
# 说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，
# 玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
# 玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
# import random
# acount = 0
# state = False
# while True:
#     acount += 1
#     NO_1 = random.randint(1, 7)
#     NO_2 = random.randint(1, 7)
#     first = NO_1 + NO_2
#     print(f'第{acount}次摇骰子的点数为{first}')
#     if acount == 1 and first == 7 or 11:
#         print('玩家获胜！')
#         break
#     elif acount == 1 and first == 2 or 3 or 12:
#         print('庄家获胜！')
#         break
#     else:
#         state = True
#         while state:
#             acount += 1
#             NO_3 = random.randint(1, 7)
#             NO_4 = random.randint(1, 7)
#             sum = NO_3 + NO_4
#             if sum == first:
#                 print('玩家获胜！')
#                 break
#             else:
#                 continue

# 练习1：生成斐波那契数列的前20个数。
num = 0
i = 1
for _ in range(20):
    num, i = i, num+i
    print(f'前20个数为：{num}',end=' ')




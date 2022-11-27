"""
第三天学习
6.函数
"""

# 函数的参数
import random

def random_num(n=2):    # n=2，设置n的默认值为2
    total = 0
    for _ in range(n):
        total += random.randint(1, 6)
        return total
# print(sum())

def add(a=0,b=0,c=0):
    return a+b+c
print(random_num())
print(random_num(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(c=100,a=32,b=-3))

# 函数传递可变参数

def add(*args):
    acount = 0
    for i in args:
        acount += i
        return acount
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,3,5,7))
print(add(1,3,5,7,9))

# 用模块管理函数
def foo():
    print('hello world!')

def foo():
    print('hello python!')

foo()

# 变量作用域
# def foo():
#     a = 'hello'
#     def foo_1():
#         b = True
#         print(a)
#         print(b)
#         print(c)
#     foo_1()
# if __name__ == '__main__':
#     c = 100
#     foo()
def foo():
    a = 'hello'
    def foo_1():
        nonlocal a
        a='python'
        b = True
        print(a)
        print(b)
        print(c)
    foo_1()
if __name__ == '__main__':
    a='python'
    c = 100
    foo()

"""第七天学习"""

# 文件和异常

# def main():
#     f=None
#     try:
#         f = open('C:/Users/Administrator/Desktop/经销商.xlsx','r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')
#     finally:
#         if f:
#             f.close()

# def main():
#     try:
#         with open('C:/Users/Administrator/Desktop/经销商.xlsx','r', encoding='utf-8') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')
import time

# def main():
#     # 一次性读取全部文件
#     with open('C:/Users/Administrator/Desktop/1.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#     # 通过for-in 循环逐行读取
#     with open('C:/Users/Administrator/Desktop/1.txt', mode='r') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#         print()
#     # 读取文件按行读取到列表中
#     with open('C:/Users/Administrator/Desktop/1.txt') as f:
#         lines = f.readlines()
#         print(lines)
# from math import sqrt
#
#
# def is_prinme(n):
#     # 判断素数的函数
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False


# def main():
#     filenames = ('a.txt', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, 'w', encoding='utf-8'))
#         for number in range(1, 10000):
#             if is_prinme(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写入文件时发生错误！')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('操作完成！')

# # 读写二进制文件
# def main():
#     try:
#         with open('C:/Users/Administrator/Desktop/imgs/01.jpg', 'rb') as f1:
#             data = f1.read()
#             print(type(data))
#         with open('C:/Users/Administrator/Desktop/imgs/正面.jpg', 'wb')as f2:
#             f2.write(data)
#     except FileNotFoundError as e:
#         print(e, '指定的文件无法打开！')
#     except IOError as e:
#         print(e, '读写文件时出现错误')
#     print('程序执行结束！')


# # 读写json文件
# import json
#
#
# def main():
#     mydict = {
#         "name": "骆昊",
#         "age": 38,
#         "qq": 957658,
#         "friends": ["王大锤", "白元芳"],
#         "cars": [
#             {"brand": "BYD", "max_speed": 180},
#             {"brand": "Audi", "max_speed": 280},
#             {"brand": "Benz", "max_speed": 320}
#         ]
#     }
#     try:
#         with open('data.json', 'w', encoding='utf-8')as f:
#             json.dump(mydict, f)
#     except IOError as e:
#         print(e, '写入文件是出现错误！')
#     print("保存数据完成！")


import requests
import json
def main():
    res=requests.get('https://apis.tianapi.com/bulletin/index?key=f483a7c7e960174b6322256a0561ed5c')
    res_model=json.loads(res.text)
    # print(res_model)
    for news in res_model['result']["list"]:
        print(f"{news['title']}:{news['digest']}")


if __name__ == '__main__':
    main()

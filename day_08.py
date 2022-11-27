"""
第八天学习
"""

# 使用正则表达式
# """
# 验证输入用户名和QQ号是否有效并给出对应的提示信息
#
# 要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
# """
# import re
#
#
# def main():
#     while True:
#         username = input("请输入用户名：")
#         m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
#         if not m1:
#             print('请输入有效的用户名！')
#             continue
#         else:
#             break
#
#     while True:
#         qq = input('请输入QQ号：')
#         m2 = re.match(r'^[1-9]\d{4,11}$', qq)
#         if not m2:
#             print('请输入有效的QQ号！')
#             continue
#         else:
#             break
#     if m1 and m2:
#         print('你输入的信息是有效的！')
# """例子2：从一段文字中提取出国内手机号码。"""
# import re
#
#
# def main():
#     # 创建正则表达式，匹配符合的手机号
#     nums = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     info = '''
#     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也是110或119，王大锤的手机号才是15600998765。
#     '''
#     # 查找所有匹配并保存到一个列表中
#     count_num_info = re.findall(nums, info)
#     print(count_num_info)
#     print('-------------------------------分割线-------------------------------')
#     # 通过迭代器取出匹配对象并获得匹配的内容
#     for temp in nums.finditer(info):
#         print(temp.group())
#     print("-------------------------------分割线----------------------------------")
#     m = nums.search(info)
#     while m:
#         print(m.group())
#         m = nums.search(info, m.end())


# for i in range(45):
#     print(i)
# if __name__ == '__main__':
#     main()


lists = ['http://st.helitong.cn/temp/2022-11-26/c3b5eb8838e04d3f997c493b0e4720a8.png',
         'http://st.helitong.cn/temp/2022-11-26/d9745f91543d4f18a34b503234714a9f.png']
list = []
for i in lists:
# a='http://st.helitong.cn/temp/2022-11-26/c3b5eb8838e04d3f997c493b0e4720a8.png'
    list.append(i)
    print(list)
# lists=["1","2"]
# for i in lists:
#     print(i)
#     # list_data=i.split("\n")
#     print(list.append(a))
'''
day02 语言元素
'''

# 赋值运算符
a = 10
b = 3
a += b
a *= a+2
print(a)

# 比较运算符与逻辑运算符的使用
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 = ', flag0)
print('flag1 = ', flag1)
print('flag2 = ', flag2)
print('flag3 = ', flag3)
print('flag4 = ', flag4)
print('flag5 = ', flag5)

# 练习1：将华氏温度转换为摄氏度
f = float(input('请输入华氏温度：'))
c = (f-32)/18
print(f'{f: .2f}华氏温度 = {c: .2f}摄氏温度')

# 练习2：输入圆的半径计算圆的面积与周长
r = int(input('请输入半径：'))
# 面积计算公式：
s = 3.14 * (r**2)
# 周长计算公式
c = 2*3.14*r
print(f'半径为{2}的圆的面积为：{s},周长为{c}')

# 练习3：输入年份判断是不是闰年
year = int(input('请输入年份：'))
if year % 4 == 0:
    print(f'{year}年是闰年')
else:
    print(f'{year}年不是闰年')



'''
03.分支结构
'''
# if语句的使用
user = input('请输入账号：')
pwd = input('请输入密码：')

if user == '123' and pwd == 't123':
    print('身份验证成功！')
else:
    print('身份验证失败！')

# if嵌套
x = int(input('x= '))
if x > 1:
    y = 3*x-5
elif x >= 1:
    y = x+2
else:
    y = 5 * x + 3
print(f'f({x})={f: .2f}')

# 嵌套分支结构
x = int(input('x= '))
if x > 1:
    y = 3*x-5
else:
    if x >= 1:
        y = x+2
    else:
        y = 5 * x + 3
print(f'f({x})={f: .2f}')

# 练习1：英寸与厘米互换
um = float(input('请输入长度：'))
cm = input('请输入单位：')
if cm == 'in' or cm == '英寸':
    print('{0}英寸={1}厘米'.format(um, um * 2.54))
elif cm == 'cm' or cm == '厘米':
    print('{0}厘米={1}英寸'.format(um, (um / 2.54)))
else:
    print('请输入正确的单位')

# 练习2：百分制成绩转换为等级制成绩
score = float(input('请输入成绩：'))

if score >= 80 and score <= 100:
    print('成绩优秀')
elif score >= 60 and score <80:
    print('成绩合格')
else:
    print('成绩不合格')

# 练习3：输入三边长，如果能构成三角形就计算周长和面积
a = float(input('请输入第一条边长：'))
b = float(input('请输入第二条边长：'))
c = float(input('请输入第三条边长：'))

# 通过两边之和大于等于第三条边，两边只差小于第三条边判断是否能组成三角形
if a+b >= c or a+c >= b or b+c >= a or a-b <= c or a-c <= b or b-c <= a:
    num = a + b + c
    p = (a + b + c) / 2
    sum = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f'周长为：{num}\n面积为：{sum}')
else:
    print('不能构成三角形')

#-*-coding:utf-8-*-
#@Time  :2019/1/11 10:28
#@File  :class_函数.py

# 学会写函数，提高代码的复用性，解放劳动力的第一步
# 自定义函数和内置函数
# 内置函数：input len type isdigit print

#函数名命名：标识符：字母数字下划线组成，不能以数字开头，不能用关键字，不能和python的其他函数重名

# def radio_machine():
#     # 这是一个复读机函数，完成复读功能
#     print('只会说你好!')
#     return
# res=radio_machine()
# print(res)

# def add():
#     '这是一个加法函数，完成两个数相加的功能'
#     a=1
#     b=2
#     c=a+b #函数代码块
#     print('{}+{}的值是{}'.format(a,b,c))
#     return 1>2 #return不是必须写的，如果后面没有表达式，可以不写
#     #return 后面可以跟多个表达式
# res=add()
# print(res)

# return后面返回==0，返回None
# return后面返回==1，返回对应值
# return后面返回>1个表达式，返回tuple--元组
# def add(a,b): #a,b形式/位置参数
#     c=a+b
#     return c
# 求任意两数之和
# print(add(2,2))
# print(add(101,55)+10086)

#请完成任意5个整数和的相加
# '定义函数，完成5个整数的相加功能'
# def add(a,b,c,d,e):
#     sum=a+b+c+d+e
#     return sum #返回求和结果
# print(add(1,2,3,4,5))
# def robot():
#     print('你好呀！')
#     #隐式的添加一个没有任何表达式的return
#     #当你调用函数的时候，才会生效
# print(robot())
# # 调用函数就是执行函数的代码块

# str = u"2009"
# print(str.isnumeric())

# l=(1,2,3)
# l[0]=0
# print(l)
# not and or优先级
# print(0 or 1 and 0 ) #判断出and优先级高于or

#要实现一个从整数m到n累加求和的函数(n>m)
# def add(m,n,k):
#     # 实现一个从m到n累加求和的函数
#     count_1=0
#     for i in range(m,n,k):
#         count_1+=i
#     print('计算结果是：{}'.format(count_1))
#     return count_1
#       #return 标识代码已经结束，后面的代码不再执行
# add(1,10,2)

# 函数的参数可以>=0个，都可以
# t=[0,1,2,3,4]
# print(t.pop(0)) #pop为列表删除索引为0的元素的函数
#                 #查看pop函数定义方法：1：ctrl+B 2:ctrl+点击鼠标左键
# print(t) #输出新的列表


















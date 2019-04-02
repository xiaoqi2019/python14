#-*-coding:utf-8-*-
#@Time  :2019/1/17 14:02
#@Author:xiaoqi
#@File  :class_内置函数.py
# l1=[1,2,3]
# l1[0]=2
# print(l1)
# d_1={'name':'monica'}
# d_1['name']='mingzi'
# print(d_1)
#字符串，元组有序不可更改，只有列表以及字典的值可以修改

#***字符串的内置函数***
# s='ha12Haha'
# print(s.count('h'))
# print(s.index('h'))
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.swapcase())
# print(s.isdigit())
# print(s.find('h'))
# print(':'.join(s))


# ***元组的内置函数***
# t=('hello',1,2,3,1)
# print(t.count(1))  #返回括号中值出现的次数：2
# print(t.index(1))  #返回括号中元素第一次出现的索引位置：1

#列表
# L=[1,2,3,4,5]
# L.reverse()
# print(L)
# L.clear()
# print(L)

#函数先定义再调用
#变量的作用域：全局变量 局部变量
#函数内 局部变量
#函数外 全局变量

# def  robot_cat(*args):
#     print(args)
#     for i in args:
#         print('2019年我想实现很多愿望，比如有：{}'.format(i))
# robot_cat('薪资翻倍！','身边的家人都幸福快乐！','攒很多很多的钱！','妹妹可以找到顺心的工作！',
#           '姐姐可以留在北京获得更高的收入！')
# a=[['薪资翻倍！','身边的人幸福快乐！'],['攒很多很多的钱！','妹妹可以找到顺心的工作！']]
# robot_cat(*a)
# b={'name':'xiaoxi','city':'changsha'}
# robot_cat(*b)

# def discount(min,max):
#     while True:
#         price=input('请问您的购买的价格是：')
#         if price.isdigit():
#             price=int(price)
#             if  min<=price<=max:
#                 print('恭喜您，您可以享受10%的折扣，折扣后价格是：{}'.format('%.4f'%(price * 0.9)))
#             elif price>max:
#                 print('恭喜您，您可以享受20%的折扣，折扣后价格是：{}'.format('%.4f'%(price * 0.8)))
#             else:
#                 print('很遗憾，您还无法享受折扣，加油！')
#             break
#         else:
#             print('请输入数字！')
# discount(50,100)
#********************************************
# 小练习
# num=input('请输入一个四位数：')
# L=[]
# for i in num:
#     i=(int(i)+5)%10
#     L.append(i)
# L.reverse()
# print(L)
# s=''
# for i in L:
#     s+=str(i)
# print(s)
# user_info={'admin':'lemon','huahua':'123456'}
# i=0
# while i<3:
#     username = input('请输入用户名：')
#     if username in user_info:
#         j=0
#         while True:
#             if j<3:
#                 pwd = input('请输入密码：')
#                 if pwd==user_info[username]:
#                     print('登陆成功！')
#                     break
#                 else:
#                     j+=1
#                     print('密码错误！您还有{}次机会'.format(3-j))
#     else:
#         i+=1
#         print('用户名不存在，您还有{}次机会！'.format(3-i))
#     break

# s='Hello123'
# print(s.count('l'))
# print(s.find('ello'))
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.replace('l','@',1))
# print(s.split('l',3))
# print(s.strip('H'))
# L=['hello',1,3,4,5,5]
#****列表增加元素的内置函数
# L.insert(0,'qiqi') #可以选择位置插入元素
# print(L)
# L.append('路人') #追加到列表后面
# print(L)
# L.extend(['456','789']) #可以增加多个，可以合并列表
# print(L)
#******修改元素
# L[0]='hi'
# print(L)
#查询元素，切片
L=[1,3,4,5,5]
# print(L[0::2])
#列表的删除元素
# L.pop(-3) #删除指定索引位置的列表元素
# print(L)

# L.sort() #为都是数字的列表元素进行排序，默认升序，假如括号里面加上reverse=True，那么为降序，若为False则为升序
# print(L)
#*******字典的内置函数、
d={1:'666',
   1.01:'xixi',
   (1,2,3):[6,7,8]}
#修改value元素
# d[1.01]='haha'
# print(d)
#字典的删除
# d.pop(1)
# print(d)
# print(d.popitem())#随即删除一组数据
# print(d)



















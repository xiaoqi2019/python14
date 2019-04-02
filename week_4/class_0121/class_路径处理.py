# -*-coding:utf-8-*-
#@Time  :2019/1/28 15:03
#@Author:xiaoqi
#@File  :class_路径处理.py
#相对路径，绝对路径
#相对路径
# file=open('py14.txt',encoding='utf-8')
# print(file.read())
#绝对路径
#涉及到转译，双斜杠\\或者R或者r
# file=open('C:\\Users\朱泽剑\PycharmProjects\python14\week_4\class_0121\py14.txt',encoding='utf-8')
# print(file.read())
# file=open(R'C:\Users\朱泽剑\PycharmProjects\python14\week_4\class_0121\py14.txt',encoding='utf-8')
# print(file.read())
# file=open(r'C:\Users\朱泽剑\PycharmProjects\python14\week_4\class_0121\py14.txt',encoding='utf-8')
# print(file.read())

#把py14.txt文件拉至week_4下面，路径发生变化
# file=open(r'C:\Users\朱泽剑\PycharmProjects\python14\week_4\py14.txt',encoding='utf-8')
# print(file.read())
#如果用相对路径呢？ ../返回所在目录的上一级目录
# file=open('../py14.txt',encoding='utf-8')
# print(file.read())
#把py14.txt文件拉至python14目录下面，路径发生变化
#../返回所在目录的上一级目录两个，说明返回两个层级目录
# file=open('../../py14.txt',encoding='utf-8')
# print(file.read())
# 如果用绝对路径实现呢？
# file=open('C:\\Users\朱泽剑\PycharmProjects\python14\py14.txt',encoding='utf-8')
# print(file.read())


#引入模块，完成对文件的处理
# import os
#获取路径的三个函数
# path_1=os.getcwd() #获取当前文件所在目录
# print(path_1)
# path_2=os.path.realpath(__file__) #__file__表示当前文件,获取当前文件的绝对路径
# print(path_2)
# path_3=os.path.basename(__file__) #获取当前文件名
# print(path_3)


#切割路径
# path_2=os.path.realpath(__file__) #__file__表示当前文件,获取当前文件的绝对路径
# #一层一层切割
# print(os.path.split(path_2))
# print(os.path.split(path_2)[0])
# print(os.path.split(os.path.split(path_2)[0])[0])
# print(os.path.split(os.path.split(os.path.split(path_2)[0])[0])[0])

#字符串的拼接
# path_2=os.path.realpath(__file__)
# print(path_2)
# path_3=os.path.split(path_2)[0]
# print(path_3)

#路径的拼接函数
# path_4=os.path.join(path_3,'py14.txt')
# print(path_4)

# 加号也是拼接
# path_4=path_3+'/test14.txt'
# print(path_4)
# file=open(path_4,encoding='utf-8')
# print(file.read())

import os
#单层创建文件夹
# os.mkdir(r'C:\Users\朱泽剑\PycharmProjects\python14\week_4\class_0121'+'./file2')
#多层创建文件夹
# os.makedirs(r'C:\Users\朱泽剑\PycharmProjects\python14\week_4\class_0121'+'/file4'+'/file4_4')
# path_1=os.path.join(r'C:\Users\朱泽剑\PycharmProjects\python14\week_4\class_0121','file4','file4_4')
# print(path_1)
#删除文件夹，不能多层删除
# os.rmdir(r'C:\Users\朱泽剑\PycharmProjects\python14\week_4\class_0121\file3\file3_3')
file_list=os.listdir(os.getcwd())
print(file_list)
for file in file_list:
    if os.path.isdir(file): #判断是否是文件夹
        print('{},是一个文件夹'.format(file))
    elif os.path.isfile(file): #判断是否是文件
        print('{},是一个文件'.format(file))
# os.mkdir('file2')
# os.rmdir('file2')











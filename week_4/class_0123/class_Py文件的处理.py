#-*-coding:utf-8-*-
#@Time  :2019/1/29 14:30
#@Author:xiaoqi
#@File  :class_Python文件的处理.py
file=open('test15.txt','r+',encoding='utf-8')
"""
定义一个函数

"""
# print(file.read(2)) #读取指定元素的个数
# for i in range(1,20): #读取指定行
#     res=file.readline()
#     if i ==3:
#         print(res)
# res=file.readlines() #读取所有内容，以列表形式输出，每行作为列表的一个元素
# print(res)
#模式：’r‘为只读，不可写入
# print(file.read())
# file.write('hello')
#模式：’r+‘为读写，
print(file.read())
file.write('hello:python')

# file.seek(0,0)

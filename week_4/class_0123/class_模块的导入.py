#-*-coding:utf-8-*-
#@Time  :2019/1/31 11:16
#@Author:xiaoqi
#@File  :class_模块的导入.py

#*************
# import
#除了顶级目录，要拿到目标函数，需要一层一层剥开
# import week_4.class_0123.class_模块函数
# week_4.class_0123.class_模块函数.eat()


#*************
# import ...as...
#当你导入的文件路径超长时或者导入的模块名字很长时可以使用
# import week_4.class_0123.class_模块函数 as hello
# hello.eat()

#*************
# from .路径..import..函数名.可以具体到函数名以及类名，但是至少要到模块名
# from week_4.class_0123.class_模块函数 import eat

#*************
# from ..路径..import *
# from week_4.class_0123.class_模块函数 import *
# eat('娃哈哈','优乐美')
# student_info('14','七月','18')

#*************
# from..路径..import..函数名..as..函数名别名..
# from week_4.class_0123.class_模块函数 import student_info as ai
# ai('14','33','18')

# import os
# file_list=os.listdir()
# print(file_list)

# with open('test14.txt','w',encoding='utf-8') as file:
#     file.write('如懿传！')
# print('2: ',file.closed)

# file=open('test14.txt','w',encoding='utf-8')
# file.write('如懿传！')
# file.close()
# print('2: ',file.closed)


















 
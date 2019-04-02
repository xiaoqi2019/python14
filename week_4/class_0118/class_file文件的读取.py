#-*-coding:utf-8-*-
#@Time  :2019/1/18 14:05
#@Author:xiaoqi
#@File  :class_file文件的读取.py
file=open('python14.txt',encoding='utf-8') #打开这个文件，存在变量file里面
# print(file.read()) #读取文件中的所有内容，保持格式

# print(file.read(5)) #读取指定长度的内容
# print(file.readline()) #按行读取，每次只能读取一行的内容
# print('******************************')
# print(file.readline())
#有中文的时候 注意设置编码为utf-8

#小练习，读出前10行
# for i in range(10):
#     print(file.readline())
#方法2：
# i=0
# while i<10:
#     print(file.readline())
#     i+=1

#读出5-8行的诗句
# for i in range(1,11,1):
#     if 5<=i<=8:
#         print(file.readline())
#     else:
#         file.readline()
# print(file.read())#读取文件中所有内容，按照格式输出
# print(file.readlines()) #读取文件中所有内容，返回列表，每一行都是列表的一个元素
# for item in file.readlines():
#     print(item)























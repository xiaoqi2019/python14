#-*-coding:utf-8-*-
#@Time  :2019/2/15 14:09
#@Author:xiaoqi
#@File  :add_function.py

def add(a,b):
     '''完成a+b的操作，并返回a+b'''
     return a+b

def add_2(*args):
    sum=0
    for item in args:
        sum+=item
    return sum


def add_5_position_fun(a,b,c,d,e):
    print(a+b+c+d+e)

if __name__=='__main__': #程序执行的入口，只有运行当前py页，才可以运行
    print(add_2(1,2,3,4,5))
# add_5_position_fun(1,2,3,4,5)
# print(add_2(1,2,3))

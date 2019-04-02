#-*-coding:utf-8-*-
#@Time  :2019/2/19 12:17
#@Author:xiaoqi
#@File  :class_classes and objects.py

class MathMethod:
    '''这是一个方法类'''
    #初始化参数
    def __init__(self,a,b):
        self.a=a
        self.b=b

    #方法
    def add_method(self):
        '''实现两个数相加'''
        print(self.a+self.b)

    def sub_method(self):
        '''实现两个数相减'''
        print(self.a-self.b)

    def mul_method(self):
        '''实现两个数相乘'''
        print(self.a*self.b)

    def div_method(self):
        '''实现两个数相除'''
        print(self.a/self.b)

if __name__=='__main__':
    # 调用：实例化
    t=MathMethod(2,3)#传参
    t.add_method()#调用类的相加函数
    t.sub_method()#调用类的相减函数

    # 调用：实例化
    p=MathMethod(4,2)#传参
    p.mul_method()#调用类的相乘函数
    p.div_method()#调用类的相除函数



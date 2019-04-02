#-*-coding:utf-8-*-
#@Time  :2019/2/19 15:26
#@Author:xiaoqi
#@File  :class_inheritance.py
#为什么用继承？提高复用性
#具体到类名
from week_5.class_0215.math_method import MathMethod
class MathMethodNew:
    c=10
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self):
        return self.a+self.b+self.c

    @classmethod
    def sub(cls):
        return cls.c+10

    def add_args(self,*args):
        sum=0
        for item in args:
            sum+=item
        return sum

if __name__ == '__main__':
    res=MathMethodNew(2,3).add_args(1,2,3,4,5)
    print(res)







#测试代码
# if __name__=='__main__':
#     #方法1
#     t=MathMethod(2,3)
#     t.add_method()
#     #方法2
#     MathMethod(2,3).add_method()


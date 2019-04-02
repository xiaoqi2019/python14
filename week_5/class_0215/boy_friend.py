#-*-coding:utf-8-*-
#@Time  :2019/2/19 14:18
#@Author:xiaoqi
#@File  :boy_friend.py


class BoyFriend:
    '''这是一个男朋友类'''
    # 初始化函数，类通过初始化参数传参
    def __init__(self,age,height,name):
        self.age=age
        self.height=height
        self.name=name
    #属性
    # sex='男'
    # age=28
    # height=180
    # name='胡歌'

    #函数
    def sport(self,sport_type):#self，类里面函数的标志，表示对象本身
        print(self.name+'喜欢的运动：{}'.format(sport_type))#类的属性可以在类的函数内部进行调用
        # self.coding() #类的函数可以在函数之间调用

    # 类函数，可以被类和对象调用
    @classmethod
    def cook(cls):
        print(cls().name+'上得厅堂，下得厨房！')

    # 对象函数，只能被对象调用
    def coding(self):
        print(self.name+'打得了豺狼，写的了代码！')

    # 静态函数，可以被类和对象调用
    @staticmethod
    def info():#要写在类里面，但是和类里面的其他函数和属性没有调用关系
        print('这是个人信息！')

#创建一个实例/对象
p=BoyFriend()
# print('类外面打印对象p：',p)
# print('我男朋友的名字是：{}'.format(p.name))
p.sport('游泳')#对象函数只可以被对象调用


# p.cook()#类函数可以被对象调用
# BoyFriend.cook()#类函数可以被类调用
#
# BoyFriend.info()#静态函数可以被类调用
# p.info()#静态函数可以被对象调用

#调用多个对象
# t=BoyFriend()
# print('类外面打印对象t：',t)
p=BoyFriend(22,170,'小件')
p.sport('游泳')



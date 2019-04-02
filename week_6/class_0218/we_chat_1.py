#-*-coding:utf-8-*-
#@Time  :2019/2/20 16:08
#@Author:xiaoqi
#@File  :we_chat1.py
from week_6.class_0218.we_chat import WeChat
import random
class WeChat_1:
    '''这是新一代的微信类'''
    def send_red_bag(self,money,numbers=1,stat=1):
        '''money:是发送红包的总金额 范围是0.01-200
            numbers:红包个数 1 1个 x指定个数
            stat:状态 1表示平分 2表示随机'''
        if 0.01<=money<=200:
            if numbers!=1:
                if stat==1:#均分
                    print('共计发红包{}个，每个红包金额{}元'.format(numbers,money/numbers))
                else:#不均分,个数还是指定的
                    pass
            else:
                print('发包一个，金额为{}'.format(money))
        else:
            print('金额必须在0.01-200之间')
if __name__=='__main__':
    t=WeChat_1
    t.send_red_bag(0,2,2)


 
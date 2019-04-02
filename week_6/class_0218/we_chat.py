#-*-coding:utf-8-*-
#@Time  :2019/2/20 16:01
#@Author:xiaoqi
#@File  :we_chat.py
class WeChat:
    '''这是一个微信类'''
    #属性
    year='2011'
    company='腾讯'
    PM='张小龙'

    #函数
    def add_friends(self):
        '''添加好友'''
        print('具有添加好友的功能')

    def send_msg(self,msg):
        '''发送信息'''
        print('发送信息：',msg)

if __name__=='__main__':
    t=WeChat() #调用：实例化
    print(t.company)
    print(t.PM)
    t.add_friends()
    t.send_msg('你好，我是小七雅！')
 
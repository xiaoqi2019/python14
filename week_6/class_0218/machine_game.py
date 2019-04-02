#-*-coding:utf-8-*-
#@Time  :2019/2/19 19:32
#@Author:xiaoqi
#@File  :machine_game.py

# 1：人和机器猜拳游戏写成一个类，有如下几个函数：
# 1）函数1：选择角色1 曹操 2张飞 3 刘备
# 2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
# 3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
# 4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。
# 5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束

#老师讲解后自己coding：
import random
class HumanVsPc:
    '''这是一个人和机器进行猜拳游戏的类'''
    '''初始化函数传参'''
    def __init__(self):
        self.fist_dict={'1':'剪刀','2':'石头','3':'布'}

    def role_choice(self):
        '''函数1：选择角色1 曹操 2张飞 3 刘备'''
        print('人机猜拳游戏开始啦！欢迎进入！！！')
        while True: #while循环，直到输入正确的角色编号
            role_dict = {'1': '曹操', '2': '张飞', '3': '刘备'}
            role_num = input('选择角色1 曹操 2张飞 3 刘备：')  # 控制台选择角色
            if role_num in role_dict.keys(): #判断选择是否在字典里面
                print('恭喜你选择角色成功，选择的角色是：{}！'.format(role_dict[role_num])) #输出选择角色结果
                return role_dict[role_num] #返回角色名称，有了return,就不需要写break，程序自动终止
            else: #判断输入不在字典里面
                print('输入错误，请重新选择角色编号！') #需要重新选择

    def role_fist(self,role):
        '''函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字'''
        while True: #循环，直到选择正确的拳头标号
            human_fist_num=input('{}猜拳开始:1剪刀 2石头 3布：'.format(role)) #控制台输入猜拳选择编号
            if human_fist_num in self.fist_dict.keys(): #判断猜拳在字典里面，引入初始化函数里面的字典fist_dict
                print('{}猜拳：{}！'.format(role,self.fist_dict[human_fist_num])) #打印猜拳名称
                return human_fist_num #返回猜拳名称，方便其他函数调用
            else: #判断猜拳输入不在字典fist_dict里面
                print('猜拳输入错误，请重新输入！') #打印结果

    def pc_fist(self):
        '''函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果'''
        pc_fist_num=str(random.randint(1,3)) #使用随机数，随机产生1-3中的任意一个，并进行类型转换
        print('PC出拳：{}！'.format(self.fist_dict[pc_fist_num])) #打印出拳名称
        return pc_fist_num #返回出拳结果，方便其他函数调用

    def fist_vs(self):
        '''函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,
            然后提示用户是否继续？按y继续，按n退出。
            最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束'''
        role= self.role_choice()  # 定义选择角色的结果
        human_win_sum=0 #定义human赢的次数初始为0
        pc_win_sum=0 #定义pc赢的次数初始为0
        epual_sum=0 #定义平局次数初始为0
        while True:
            human_res_num=self.role_fist(role) #定义human猜拳结果编号
            pc_res_num=self.pc_fist() #定义pc出拳结果
            if human_res_num==pc_res_num: #判断出拳一样，平局
                print('本局对战结果：人机平局！') #打印平局结果
                epual_sum+=1 #平局次数累加
            elif (int(human_res_num) - int(pc_res_num)) in [1,-2]: #判断角色赢
                #判断角色赢情况：（角色:1剪刀，pc:3布，角色：2石头：pc：1剪刀，角色：3布，pc：2石头）编号相减为1和-2
                print('本局对战结果：{}赢！'.format(role)) #打印结果
                human_win_sum+=1 #角色赢的次数累加
            else: #判断pc赢
                print('本局对战结果：PC赢!') #打印结果
                pc_win_sum+=1 #pc赢的次数累加
            while True: #是否继续输入循环
                whether_continue=input('是否继续？按y继续，按n退出:') #控制台选择是否继续
                if whether_continue=='y': #判断选择继续
                    break #终止此循环
                elif whether_continue=='n': #判断选择退出
                    print('{}赢{}局,PC赢{}局,平局{}次,游戏结束!'.format(role,human_win_sum,pc_win_sum,epual_sum))
                    exit() #退出程序
                else: #判断选择错误，需要重新选择
                    print('输入错误，请重新选择！') #打印需要继续输入

if __name__=='__main__':
    h=HumanVsPc()
    # h.role_choice()
    # h.role_fist()
    h.fist_vs()




# #引入随机数
# import random
# class MachineGame:
#     '''这是一个人和机器猜拳游戏的类'''
#     #属性
#     year=2019
#     author='xiaoqi'
#     def __init__(self,role=None,choice=None,computer_res=None):
#         self.role=role
#         self.choice=choice
#         self.computer_res=computer_res
#
#     #函数
#     def role_choice(self):
#         '''函数1：选择角色1 曹操 2张飞 3 刘备'''
#         print('进入游戏成功，人机猜拳游戏开始啦！！！')
#         while True:
#             # 控制台输入选择的角色，直到输入正确
#             self.role=input('请选择角色1曹操 2张飞 3刘备：')
#             #判断输入数字
#             if self.role.isdigit():
#                 #判断选择角色1
#                 if int(self.role)==1:
#                     print('您选择的角色是曹操，选择成功！')
#                     break
#                 ##判断选择角色2
#                 elif int(self.role)==2:
#                     print('您选择的角色是张飞，选择成功！')
#                     break
#                 # 判断选择角色3
#                 elif int(self.role)==3:
#                     print('您选择的角色是刘备，选择成功！')
#                     break
#                 else:
#                     print('数字输入不正确，请重新输入：')
#             #判断输入非数字
#             else:
#                 print('请输入数字！')
#
#     def role_mora(self):
#         '''函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字'''
#         while True:
#             # 控制台输入
#             self.choice=input('请输入一个1-3的数字1剪刀 2石头 3布：')
#             #判断输入数字
#             if (self.choice).isdigit():
#                 #判断输入1剪刀
#                 if int(self.choice)==1:
#                     print('您输入的是1剪刀!')
#                     break
#                 # 判断输入2石头
#                 elif int(self.choice)==2:
#                     print('您输入的是2石头!')
#                     break
#                 # 判断输入3布
#                 elif int(self.choice)==3:
#                     print('您输入的是3布!')
#                     break
#                 else:
#                     print('您输入有误，请重新输入1-3的数字！')
#             #判断输入非数字
#             else:
#                 print('请输入数字！')
#
#     def computer_punch(self):
#         '''函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果'''
#         self.computer_res=random.randint(1, 3) #产生1-3随机数
#         # 判断电脑出拳随机结果1剪刀
#         if self.computer_res==1:
#             #打印结果
#             print('电脑出拳结果是：1剪刀!')
#         # 判断电脑出拳随机结果2石头
#         elif self.computer_res==2:
#             #打印结果
#             print('电脑出拳结果是：2石头!')
#         # 判断电脑出拳随机结果3布
#         elif self.computer_res==3:
#             #打印结果
#             print('电脑出拳结果是：3布!')
#
#     def punch_against(self):
#         '''函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,
#         然后提示用户是否继续？按y继续，按n退出。最后结束的时候输出结果 角色赢几局
#         电脑赢几局，平局几次 游戏结束'''
#         role_win=0#定义变量角色赢的次数
#         computer_win=0#定义变量电脑赢的次数
#         sum_equal=0#定义平局次数变量
#         while True:
#             self.role_choice() #调用角色选择函数
#             self.role_mora() #调用角色猜拳函数
#             self.computer_punch() #调用电脑出拳函数
#             if int(self.choice)==self.computer_res: #判断平局
#                 print('平局！') #打印结果
#                 sum_equal+=1 #平局次数累加
#             elif self.choice=='1' and self.computer_res==3:#判断人赢的情况
#                 print('人赢！') #打印结果
#                 role_win+=1 #角色赢的次数累加
#             elif self.choice=='2' and self.computer_res==1:#判断人赢的情况
#                 print('人赢！') #打印结果
#                 role_win+=1 #角色赢的次数累加
#             elif self.choice=='3' and self.computer_res==2:#判断人赢的情况
#                 print('人赢！') #打印结果
#                 role_win+=1 #角色赢的次数累加
#             else:
#                 print('人输了！') #打印结果
#                 computer_win+=1 #机器赢的次数累加
#             while True: #是否继续的循环
#                 continue_choice=input('是否继续？按y继续，按n退出：') #控制台输入是否继续游戏
#                 if continue_choice=='y': #选择继续
#                     break #终止此循环
#                 elif continue_choice=='n': #选择退出
#                     print('角色赢{}局，电脑赢{}局，平局{}次，游戏结束！'.format(role_win,computer_win,sum_equal)) #打印结果
#                     exit() #退出程序
#                 else: #判断是否继续输入错误的情况
#                     print('输入有误，请重新输入!')
#
# #测试代码
# if __name__=='__main__':
#     p=MachineGame() #创建一个对象
#     p.punch_against() #调用函数4


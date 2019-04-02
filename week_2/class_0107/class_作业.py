#-*-coding:utf-8-*-
# 1.根据你输入的数据，来进行判断学生的成绩。输入数据函数：input()

# 输入学生的成绩
# score=int(input('请输入学生的成绩：'))
# #判断如果成绩是否在0-100正常范围之内
# if score<0 or score>100:
#     # 不在范围之内做出判断
#     print('您输入的成绩不在正常范围内！')
# #判断成绩是否大于90，是否优秀
# elif score>90:
#     print('优秀！')
# #判断成绩是否大于80
# elif score>80:
#     print('良好！')
# # 判断成绩是否及格
# elif score>=60:
#     print('及格！')
# # 其余便是不及格情况
# else:
#     print('不及格！')


# 2、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。编写一程序，询问
# 购买价格，再显示出折扣（%10或20%）和最终价格
# 控制台输入购买价格
def discount():
    money=float(input('请输入购买价格：'))
    # 判断享受10%折扣的情况
    if 50<=money<=100 :
        final =money * 0.9
        # 输出折扣后的价格
        print("恭喜您，可以享受10%的折扣,最终价格为",float('%0.4f'%final))
        # 判断享受20%折扣的情况
    elif money>100:
        final=money*0.8
        # 输出折扣后的价格
        # print("恭喜您，可以享受20%的折扣，最终价格为{}".format('%.4f'%final))
        print("恭喜您，可以享受20%的折扣，最终价格为",float('%0.4f'%final))
        # 其余不享受折扣的情况
    else:
        print("很遗憾，您购买的金额不足，暂时还无法享受折扣！")
discount()

# 3、输入一个数，判断一个数n能同时被3和5整除
# 控制台输入一个数
# n=int(input("请输入一个数："))
# # 判断是否同时可以被3和5整除
# if n%3==0 and n%5==0:
#     # 输出结果
#     print("{}能同时被3和5整除".format(n))
# # 判断不能同时被3和5整除的情况
# elif n%3!=0 or n%5!=0:
#     # 输出结果
#     print("{}不能同时被3和5整除".format(n))


# 4、输入一个年份，输出是否为闰年，闰年条件：能被4整除但不能被100整除，
# 或者能被400整除的年份都是闰年
# 输入年份
# year=int(input("请输入一个年份："))
# # 判断是否是闰年的情况1：能被4整除但不能被100整除
# if year%4==0 and year%100!=0:
#     # 输出结果
#     print('{}年为闰年'.format(year))
# # 判断是否是闰年的情况2：能被400整除
# elif year%400==0:
#     # 输出结果
#     print('{}年为闰年'.format(year))
# # 判断其余情况均不是闰年
# else:
#     print('{}年不是闰年'.format(year))


# 5、一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，
# 十位与千位相同。 根据判断打印出相关信息。
# 输入一个五位数
# a=input('请输入一个5位数：')
# # 判断是回文数的情况
# if a.isdigit() and len(a)==5: #判断是否输入的纯数字且为5位
#     if a[0]==a[-1] and a[1]==a[-2] and int(a[0])!=0:
#         print('{}是回文数'.format(a))
#     else: # 判断不是回文数的情况
#         # 输出结果
#         print('{}不是回文数'.format(a))
# else:
#     print('请输入5位数字！')


# 6、生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印
# bigger。小了，则打印less。如果相等，则打印equal
# 生成一个0至9内的随机数字
# import random
# a=int(random.randint(0,9))
# # 输入一个数字
# num=int(input('请输入一个数字：'))
# # 输入数字比随机数大
# if num>a:
#     print('bigger，随机数是{}'.format(a))
# # 输入数字比随机数小
# elif num<a:
#     print('less，随机数是{}'.format(a))
# # 输入数字等于随机数
# elif num==a:
#     print('equal，随机数是{}'.format(a))


# 7、写一个餐厅菜单显示程序：（大概的设计模式如下） 请自己设计一个数据存
# 储这些菜单，然后根据你从客户端输入的数据去进行菜名的读取。
# 设计字典存储菜单
# dishes={
#        '平价菜':{'手撕包菜':'10元','大白菜':'10元','土豆丝':'10元','炒莴笋':'10元','上海青':'10元',
#              '青椒炒茄子':'10元','焖白豆腐':'10元','干豆角炒鸡':'15元'},
#        '凉菜':{'凉拌黄瓜':'8元','凉拌皮蛋':'9元'},
#        '小锅现炒':{'大盆花菜':'16元','长豆角鲮鱼':'19元', '酸萝卜耳尖':'22元'}
#         }
# # 输入菜名
# while True:
#     dishes_type=input('请输入菜品类目：1:平价菜，2：凉菜，3：小锅现炒：')
#     dishes_type=int(dishes_type)
#     if  dishes_type in [1,2,3]:
#         dish_name=input('请输入您想选择的菜名：')
#         if dishes_type==1 and dish_name in dishes['平价菜']:
#             print('平价菜：{}价格为{}'.format(dish_name,dishes['平价菜'][dish_name]))
#             break
#         elif dishes_type==2 and dish_name in dishes['凉菜']:
#             print('凉菜：{}价格为{}'.format(dish_name,dishes['凉菜'][dish_name]))
#             break
#         elif dishes_type==3 and dish_name in dishes['小锅现炒']:
#             print('小锅现炒：{}价格为{}'.format(dish_name,dishes['小锅现炒'][dish_name]))
#             break
#         else:
#             print('不好意思，您输入的菜品不在相应的菜品类目里，请重新输入!')
#     else:
#         print('您输入的菜品类目不正确，请重新输入！')
#         continue #不写也是一样的








# name=input('请输入菜名：')
# # 判断输入菜为平价菜
# if name in d_cd['平价菜'].keys():
#     # 输出价格
#     price=d_cd['平价菜'][name]
#     print('有这道菜，{}价格为{}！'.format(name,price))
# # 判断输入菜为凉菜
# elif name in d_cd['凉菜'].keys():
#     # 输出价格
#     price=d_cd['凉菜'][name]
#     print('有这道菜，{}价格为{}！'.format(name,price))
# #判断输入菜为小锅现炒
# elif name in d_cd['小锅现炒'].keys():
#     # 输出价格
#     price=d_cd['小锅现炒'][name]
#     print('有这道菜，{}价格为{}!'.format(name,price))
# # 判断没有这道菜
# else:
#     # 输出结果
#     print('不好意思，没有这道菜！')

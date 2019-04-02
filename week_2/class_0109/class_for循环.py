#-*-coding:utf-8-*-
# for循环：有限次数循环(不会进入死循环)
#什么时候用for循环：一般题目中给出确定的循环次数的，或者有嵌套循环的
# 作用：
# 1：遍历元素或者是利用遍历元素的次数来控制循环
# 2：可以控制循环次数
# 可以用来遍历的数据类型：str tuple  list dict---目前所学
# 还有很多数据类型，只要是可迭代的（有多个元素），就可以用for循环来遍历
# 可迭代的数据类型：数据里面允许存在多个元素或者0个
# s='python14'
# for item in s:#依次访问字符串里的每个元素，in后面必须是可迭代的，不可以放整数，字符串，列表，元组，字典都可以
#     print(item)
# s={'name':'小雪','age':18}
# for i in s:
#     print(i)#遍历字典时，默认遍历的是key

#课堂练习
# 预习视频：课堂练习询问10个人，只有满足年龄在10到12岁之间（包含）的女生，才可以加入足球队，
# 否则就没有资格，统计有资格的总人数
# count=0 #记录符合条件的人数
# for i in '1234567890': #遍历字符串循环10次
#     age=int(input('同学请问您的年龄是：'))
#     sex=input('同学方便填写一下您的性别吗？f(女) or m（男）: ')
#     if  10<=age<=12 and sex=='f': #判断可以加入足球队的条件
#         print('恭喜您可以加入女子足球队！')
#         count+=1
#     else:#其他不能加入的输出
#         print('很遗憾，您还不能加入！')
# print('有资格加入的总人数：{}'.format(count)) #打印有资格的总人数

# 嵌套for循环
# d={'name':{'boboji':'钵钵鸡','snow':'小雪'},
#    'score':[99,100]}
# for i in d:
#     print(d[i])
#     for j in d[i]:
#         print(j)

#课堂练习
#把下面每个元素都遍历出来
# L=[[1,2,3,4,5,6,7,8],[9,0,1]]
# for i in L:#首先遍历列表的元素
#     for j in i:#再次遍历列表元素的元素
#         print(j,end='')#输出每个元素,取消换行
#         print('')#输出每个元素换行

# 控制台输入购买价格
# money=int(input('请输入购买价格：'))
# # 判断享受10%折扣的情况
# if money>=50 and money<=100:
#     final =money * 0.9
#     # 输出折扣后的价格
#     print("恭喜您，可以享受10%的折扣,最终价格为{}".format(final))
# # 判断享受20%折扣的情况
# elif money>100:
#     final=money*0.8
#     # 输出折扣后的价格
#     print("恭喜您，可以享受20%的折扣，最终价格为{}".format(final))
# # 其余不享受折扣的情况
# else:
#     print("很遗憾，您购买的金额不足，暂时还无法享受折扣！")

price = int(input('请问售价是多少：'))
if price>=50 and price<=100:
    price = price*(1-0.1)
elif price>100:
    price = price*(1-0.2)
print('最终价格为: {}'.format(int(price)))
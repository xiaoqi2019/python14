#-*-coding:utf-8-*-
# while循环：无限次数循环
#什么时候用while循环：一般是循环次数不确定时，循环条件为一个比较运算或者逻辑运算时
# 预习视频：课堂练习询问10个人，只有满足年龄在10到12岁之间（包含）的女生，才可以加入足球队，
# 否则就没有资格，统计有资格的总人数
# 方法1：
# count=0
# for i in range(1,11):
#     age = input('同学，请问你今年多大了？')
#     if age.isdigit():
#         age=int(age)
#         if  10<=age<=12:
#             sex = input('方便填写一下你的性别吗？')
#             if sex=='f':
#                 print('恭喜你，可以加入球队！')
#                 count+=1
#             else:
#                 print('很遗憾，您不符合要求！')
#         else:
#             print('很遗憾，您不符合要求！')
#     else:
#         print('很遗憾，您不符合要求！')
# print('满足条件的总人数是：{}'.format(count))
# 方法2：
# count=0
# i=0
# while i<10:
#     i+=1
#     age = input('同学，请问你今年多大了？')
#     if age.isdigit():
#         age=int(age)
#         if  10<=age<=12:
#             sex = input('方便填写一下你的性别吗？')
#             if sex=='f':
#                 print('恭喜你，可以加入球队！')
#                 count+=1
#             else:
#                 print('很遗憾，您不符合要求！')
#         else:
#             print('很遗憾，您不符合要求！')
#     else:
#         print('很遗憾，您不符合要求！')
# print('满足条件的总人数是：{}'.format(count))
# 方法3：
# count=0
# i=0
# while i<10:
#     i+=1
#     age = input('同学，请问你今年多大了？')
#     if age.isdigit():
#         age=int(age)
#         sex = input('方便填写一下你的性别吗？')
#         if  10<=age<=12 and sex=='f':
#             print('恭喜你，可以加入球队！')
#             count+=1
#         else:
#                 print('很遗憾，您不符合要求！')
#     else:
#         print('很遗憾，您不符合要求！')
# print('满足条件的总人数是：{}'.format(count))
# 方法4：
# count=0
# i=0
# while True:
#     i+=1
#     if i<10:
#         age = input('同学，请问你今年多大了？')
#         if age.isdigit():
#             age=int(age)
#             sex = input('方便填写一下你的性别吗？')
#             if  10<=age<=12 and sex=='f':
#                 print('恭喜你，可以加入球队！')
#                 count+=1
#             else:
#                     print('很遗憾，您不符合要求！')
#         else:
#             print('很遗憾，您不符合要求！')
#     else:
#         break
# print('满足条件的总人数是：{}'.format(count))

money=float(input('请输入购买价格：'))
# 判断享受10%折扣的情况
if 50<=money<=100:
    final =money * 0.9
    # 输出折扣后的价格
    print("恭喜您，可以享受10%的折扣,最终价格为{:.4f}".format(final)) #保留小数点后4位
# 判断享受20%折扣的情况
elif money>100:
    final=money*0.8
    # 输出折扣后的价格
    '''
    保留小数点后4位，('%.4f'%final)表示小数点后规范的保留4位
    float('%.4f'%final)表示去除无效0后小数点后最后4位，注意二者区别
    '''
    # print("恭喜您，可以享受20%的折扣，最终价格为{}".format('%.4f'%final))
    print('恭喜您，可以享受20%的折扣，最终价格为',float('%.4f'%final))
# 其余不享受折扣的情况
else:
    print("很遗憾，您购买的金额不足，暂时还无法享受折扣！")

# a = 1.23456789
# b = "%.4f" % a
# print('hahhah'+a+',a)
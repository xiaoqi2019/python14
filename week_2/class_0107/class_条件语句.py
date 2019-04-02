#-*-coding:utf-8-*-
# 简单的条件判断语句
# 1：if...else...
# sex=input('请输入你的性别：')
# if sex=='女':
#     print('一起shopping吧！')
# else:
#     print('一起打球吧！')
# task_score=int(input('请输入你的分数：'))
# absence=int(input('请输入你的缺勤次数：'))
# if task_score==100 and absence==0:
#     print('恭喜你，荣获班级之星！')
# else:
#     print('不好意思，你的分数是{}，缺勤{}次，离班级之星还有一定的距离，加油！'.format(task_score,absence))

# 空数据，如空字符串，空列表，空字段，空元组都是代表False
# 非空 对应 1 True
# d={}
# if d:
#     print("我最喜欢你了！")
# else:
#     print("我不喜欢你！")

# 3:if.条件..elif.条件..else...
# name=input('请输入你对象的名字：')
# height=int(input('请输入你对象的身高：'))
# if name=='马云':
#     print('这样的对象挺好的')
# elif name!='马云':
#     if height>=175:
#         print('这样的对象挺好的！')
#     else:
#         print('我没啥好说的')

# 红绿灯
# color=input('请输入你看到的灯的颜色：')
# if color=='red':
#     print('请不要动！')
# elif color=='green':
#     print('可以顺利通行！')
# elif color=='yellow':
#     print('请等一等！')
# else:
#     print('你是色盲吗？')

# score=int(input('请输入你的分数：'))
# if score<0 or score>100:
#     print('你的分数不在正常范围之内!')
# elif score>90:
#     print('优秀！')
# elif score>80:
#     print('良好！')
# elif score>=60:
#     print('及格！')
# else:
#     print('不及格！')

# 课堂练习：登录功能：用户名和密码存在{'name':'huahua','pwd':'123456'}
# 字典中，通过控制台输入用户名和密码判读是否正确，
# 然后给出对应的提示消息：登录成功 OR 用户名或密码错误
# 方法1：
# d={'name':'huahua','pwd':'123456'}
# name=input('请输入用户名：')
# pwd=(input('请输入密码：'))
# if name==d['name'] and pwd==d['pwd']:
#     print('登陆成功')
# else:
#     print('用户名或密码错误!')
# 方法2：
# d={'name':'huahua','pwd':'123456'}
# 相当于我们存在数据库里面的用户信息。
# name=input('请输入用户名：')
# if name==d['name']:
#     pwd=input('请输入密码：')
#     if pwd==d['pwd']:
#         print('登陆成功！')
#     else:
#         print('密码错误！')
# else:
#     print('用户名错误！')

# 方法3：
# d={'name':'huahua','pwd':'123456','nancy':'234567'}
# name=input('请输入用户名：')
# if name in d.keys():
#     pwd=input('请输入密码：')
#     if pwd==d[name]:
#         print('登陆成功！')
#     else:
#         print('密码错误！')
# else:
#     print('用户名错误！')











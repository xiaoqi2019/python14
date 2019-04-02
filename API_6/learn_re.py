#-*-coding:utf-8-*-
# 什么是正则表达式，用来规范的查找需要的字符串
# 组成：原义字符串和元字符
# 如何用python来解析
# 使用场景
# 1：规范查找需要的字符串
# 2：用来检测输入的字符串是否符合某些规范，如邮箱，手机号，身份证号等
import re
# target="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
#原义字符串的查找
# p = 'normal_user'
# m = re.search(p,target) #在目标字符串里面根据正则表达式来查找，有匹配的字符串就返回
# print(m)
# print(m.group())
# p2='#(.*?)#'
# ms=re.search(p2,target)
# print(ms.group()) #不传参时返回表达式和字符串一起
# print(ms.group(1)) #传参时只返回符合的字符串，相当于一个search()

# mm=re.findall(p2,target) #在目标字符串里面根据正则表达式来查找，返回所有匹配的字符串以列表形式
# print(mm)
# mr=re.match(p2,target) #仅仅只从目标字符串的开头位置开始匹配，有就返回，没有就返回None
# print(mr)

# target2=re.sub(p2,'15910298856',target,count=1) #count默认0，不指定指替换所有符合要求的字符串，指定count=1代表替换一次
# print(target2)
# target3=re.sub(p2,'123456',target2,count=1)
# print(target3)
from API_6.common.get_data import GetData
#使用循环
# target="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
target="{'mobilephone':'#normal_user#','pwd':'123456'}"
p2='#(.*?)#'
for i in re.findall(p2,target):
    if i=='normal_user':
        target=re.sub(p2,str(getattr(GetData,'MOBILEPHONE')),target,count=1)
    if i=='normal_pwd':
        target=re.sub(p2,str(getattr(GetData,'MEMBER_PWD')),target)
print(target)

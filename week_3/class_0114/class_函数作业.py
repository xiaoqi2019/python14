#-*-coding:utf-8-*-
#@Time  :2019/1/15 15:11
#@Author:xiaoqi
#@File  :class_函数作业.py

# 新手练习题：
# 1、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
# def judge_len(*args):
#     for item in args:
#         if isinstance(item,str): #判断对象类型为字符串
#             if len(item)>5: #长度大于5
#                 print('字符串:{}长度大于5'.format(item))
#             else: #长度小于5
#                 print('该字符串:{}长度小于5'.format(item))
#         elif isinstance(item,list):
#             if len(item)>5:
#                 print('该列表:{}长度大于5'.format(item))
#             else:  # 长度小于5
#                 print('该列表:{}长度小于5'.format(item))
#         elif isinstance(item, tuple):
#             if len(item) > 5:
#                 print('该元组:{}长度大于5'.format(item))
#             else:  # 长度小于5
#                 print('该元组:{}长度小于5'.format(item))
#         else:
#             print('该函数不支持该{}类型的判断！'.format(type(item)))
# judge_len('123',{'name':'lucy','age':'18'},[1,2,3],(1,2,3,45,5))


# def len_01(a):
#     '''定义一个函数，实现判断用户输入的对象长度是否大于5'''
#     if len(a)>5: #长度大于5
#         print('该用户传入的对象:{}长度大于5'.format(a))
#     else: #长度小于5
#         print('该用户传入的对象:{}长度小于5'.format(a))
#     return
# len_01('abc')
# len_01('012345')
# len_01('')


# 2、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
# def judge_list(L):
#     if isinstance(L,list):
#         if len(L)>2:
#             # print('新列表为{}'.format(L[:2]))
#             return L[:2]
#         else:
#             print('该列表长度小于2')
#     else:
#         print('该函数不支持该{}数据类型判断'.format(type(L)))
# print(judge_list([1,2,3]))
# judge_list((1,2,3))


# def new_list(l):
#     '''定义一个函数，实现检查传入的是否是列表，正并判断如果列表长度大于2，只保留前两个长度的内容，返回新内容'''
#     if type(l)==list: #判断是是列表
#         if len(l)>2: #判断列表长度大于2
#             L_ne=l[0:2:1] #切片，保留列表的前个元素
#             print('列表{}保留前两个长度后的新列表为：{}'.format(l,L_ne)) #输出新列表
#             return L_ne
#         else: #列表长度小于2
#             print('您输入的列表长度没有超过2！')
#     elif type(l)!=list: #判断不是列表
#         print('请传入正确的列表！')
# new_list([])
# new_list([1,2])
# new_list([1,2,3])
# new_list('abc')


# 3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，
# 则添加到字典中，并返回新的字典。

#方法1：
# import random
# def get_key(d,s):
#     while True:
#         key=s+str(random.randint(1,100))
#         if key in d.keys():
#             continue
#         else:
#             break
#     return key
#
# def judge_dict(d,s):
#     if s in d.values():
#         print('字符串:{},是字典:{}的值'.format(s,d))
#     else:
#         key=get_key(d,s)
#         d[key]=s
#         print('新的字典是：{}'.format(d))
#     return d
# judge_dict({'1':2,"3":4},'python')

#方法2：
# def dic_new(d,s):
#     '''实现判断字符串是否是字典中的值，不是的话，添加到字典中，并返回新的字典！'''
#     if s in dict(d).values(): #在字典里
#         print('字符串:{}在字典:{}里面'.format(s,d))
#     else: #不在字典里
#         d['new_key']=s #字符串添加到字典中
#         print('字符串不在字典中！新的字典是：{}'.format(d))
#         return d
# dic_new({1:2,3:4},5)
# dic_new({1:2,3:4},4)
# dic_new({'name':'lucy',3:4},'lucy')



# 4、一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别
# （m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出
# 满足条件的总人数。

# def football_join(x,y,k,sex='f'):
#     '''定义一个函数，实现询问用户的性别（m表示男性，f表示女性）和年龄，然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出
#     满足条件的总人数。
#     x表示能加入的最小年龄
#     y表示能加入的最大年龄
#     k表示询问次数
#     sex='f'指定组建队伍的性别为女
#     '''
#     count=0 #记录符合条件的总人数
#     a=0 #记录询问次数
#     while a<10:
#         a+=1
#         age=int(input('请问你您的年龄：'))
#         sex=input('您的性别：')
#         if x<=age<=y and sex=='f':
#             count+=1
#             print('恭喜可以加入！')
#     print('总人数：{}'.format(count))
# football_join(10,18,10,'m')



# def join_ch(x,y,k):
#     '''定义函数，实现筛选年龄从x岁到Y岁的小女孩，一共询问k次，最后输出满足条件的总人数'''
#     sum=0 #总人数初始值为0
#     for i in range(1,k+1): #遍历k次
#         age=int(input('请问同学你多大了？'))
#         sex=input('同学方便填写一下你的性别吗？（m表示男性，f表示女性）：')
#         if  x<=age<=y and sex=='f': #判断是否符合要求
#             sum+=1 #计算人数
#             print('恭喜同学，可以加入我们！')
#         else: #不符加入的情况
#             print('很遗憾，您暂时加入不了！')
#     print('可以加入的总人数为{}人'.format(sum)) #输出总人数
#     return sum
# join_ch(10,12,3)
# 方法2：
# def join_ch(x,y,k):
#     '''定义函数，实现筛选年龄从x岁到Y岁的小女孩，一共询问k次，最后输出满足条件的总人数'''
#     sum=0 #总人数初始值为0
#     i=0
#     while i<k: #循环k次
#         i+=1
#         age=int(input('请问同学你多大了？'))
#         sex=input('同学方便填写一下你的性别吗？（m表示男性，f表示女性）：')
#         if  x<=age<=y and sex=='f': #判断是否符合要求
#             sum+=1 #计算人数
#             print('恭喜同学，可以加入我们！')
#         else: #不符加入的情况
#             print('很遗憾，您暂时加入不了！')
#     print('可以加入的总人数为{}人!'.format(sum)) #输出总人数
#     return sum
# join_ch(10,12,3)




# 进阶提升题：

# 1：请用自己目前所学实现指定字符串大写转小写，小写变大写，并且将字符串变为镜像字符串，镜像的意思是：
# 大写的’A’变为’Z’,’大写的‘B‘变成‘Y,小写的’’’b’变为’y 。目前要求处理的示范字符串是：
# ”sdSdsfdAdsdsdfsfdsdASDSDFDSFa” 需要提供至少2种不同的解决方法。
# 方法一：
# s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
# print('原字符串是：',s)
# s1=s.swapcase() #转换大小写
# print('调整大小后的字符串是：',s1)
# intable='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# outtable='ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
# b=str.maketrans(intable,outtable) #制定翻译表，定义字符串的转换
# s2=s1.translate(b) #使用翻译表进行翻译
# print('镜像字符串是：',s2)

# 方法二：
# s='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
# s1=s.swapcase() #转换大小写
# print('转换大小写后的字符串是：',s1)
# new_s='' #定义新的空字符串
# for i in s1: #遍历转换大小写后的字符串
#     if i.isupper():
#         i=chr(155-ord(i)) #大写替换成镜像字母
#         new_s+=i #赋值
#     elif i.islower():
#         i=chr(219-ord(i)) #小写替换成镜像字母
#         new_s+=i #赋值
# print('镜像字符串为：',new_s)


# 根据编码范围判断是中文汉字的函数
# def is_chinese(uchar):
#     if uchar >= u'\u4E00' and uchar <= u'\u9FA5':
#         return True
#     else:
#         return False
# print(is_chinese('张'))

# 2：搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串： 我的是名字是lemon,今年5岁。 语法分析后得到结果如下：
# 数字：5
# 中文：我的名字是、今年、岁
# 拼音：lemon
# 符号：，。 请编写程序实现该词法分析功能。



def split_str(s):
    """按类别打印出字符串中的元素"""
    ch, digit, en, symbol = '', '', '', ''
    # 定义一个变量i,作为s的索引
    i = 0
    for item in s:
        # 判断是否为中文
        if u'\u4e00' <= item <= u'\u9fff':
            # 判断item的下一个元素是否为中文
            if u'\u4e00' <= s[i+1] <= u'\u9fff':
                ch += item
                i += 1
            else:
                ch = ch+item+'、'
                i += 1
        # 判断是否为字母 字母的ASCII值在65-90 或者 97-122之间
        elif 65 <= ord(item) <= 90 or 97 <= ord(item) <= 122:
            if 65 <= ord(s[i + 1]) <= 90 or 97 <= ord(s[i + 1]) <= 122:
                en = en + item
                i += 1
            else:
                en = en + item + '、'
                i += 1
        # 判断是否为数字
        elif item.isdigit():
            if s[i+1].isdigit():
                digit += item
                i += 1
            else:
                digit = digit+item+'、'
                i += 1
        else:
                symbol += item
                i += 1
    print('数字：{}'.format(digit.strip('、')))
    print('中文：{}'.format(ch.strip('、')))
    print('拼音：{}'.format(en.strip('、')))
    print('符号：{}'.format(symbol.strip('、')))

a = '我的是名字是lemon,今年5岁。'
split_str(a)

# def analysis_new(a):
#     '''定义函数，实现分类处理功能'''
#     num = ''
#     zhongwen = ''
#     pinyin = ''
#     fuhao = ''
#     for i in a: #遍历字符串中每个元素
#         if i.islower() or i.isupper(): #判断是字母
#             pinyin+=i
#         elif i >= u'\u4e00' and i<= u'\u9fa5': #判断是中文
#             zhongwen+=i
#         elif str(i).isdigit(): #判断是数字
#             num+=i
#         else: #其他的标点符号
#             fuhao+=i
#     print('数字是：',num)
#     print('拼音是：',pinyin)
#     print('中文是：',zhongwen)
#     print('符号是：',fuhao)
# analysis_new('你好！我是xiaoqi,年龄20！有事可以@我，xiexie')











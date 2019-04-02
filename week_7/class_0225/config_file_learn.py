#-*-coding:utf-8-*-
#@Time  :2019/2/26 15:03
#@Author:xiaoqi
#@File  :config_file_learn.py
#什么是配置文件 .conf .ini .config .properties .xml
#怎么写配置文件---[section] option value
#怎么读取配置文件---引入模块和类

#引入模块
from configparser import ConfigParser
#创建对象
cf=ConfigParser()
#打开配置文件read()类似open()函数
cf.read('lemon.conf',encoding='utf-8')

#读取配置文件的内容
#读取方法1：
# res=cf.get('StudentName','stu_1')
#读取方法2：
res=cf['StudentName']['stu_1']
print(res)
print(type(res))#配置文件里面读取出来的数据都是字符串
print(type(eval(res)))#把括号内的数据变成原本的数据类型

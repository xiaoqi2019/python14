#-*-coding:utf-8-*-
#@Time  :2019/2/26 15:00
#@Author:xiaoqi
#@File  :config_class.py

#写一个配置类 有以下几个函数：
#1：读取整数
#2：读取浮点数
#3：读取布尔值
#4：读取其他类型的数据 list tuple dict eval（）
#5：读取字符串

from configparser import ConfigParser
class ReadConfig:
    '''这是一个配置类，读取各种类型的数据'''
    def __init__(self,file_name,section,option):
        self.cf=ConfigParser()
        self.cf.read(file_name,encoding='utf-8')
        self.section=section
        self.option=option

    def get_int(self):
        '''函数1：读取整数'''
        value=self.cf.getint(self.section,self.option)
        return value

    def get_float(self):
        '''函数2：读取浮点数'''
        value=self.cf.getfloat(self.section,self.option)
        return value

    def get_bool(self):
        '''函数3：读取布尔值'''
        value=self.cf.getboolean(self.section,self.option)
        return value

    def get_data(self):
        '''函数4：读取其他类型的数据list tuple dict'''
        value=self.cf.get(self.section,self.option)
        return eval(value)

    def get_str(self):
        '''函数5：读取字符串'''
        value=self.cf.get(self.section,self.option)
        return value

if __name__=='__main__':
    res=ReadConfig('lemon.conf','TestCase','button').get_data()
    print(type(res))







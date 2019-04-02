from configparser import ConfigParser
class ReadConfig:
    '''这是一个读取控制执行哪些测试用例配置文件的类'''
    def __init__(self,file_name,section,option):
        '''初始化函数，对配置文件名字，section，option参数化'''
        self.cf=ConfigParser()
        self.cf.read(file_name,encoding='utf-8')
        self.section=section
        self.option=option
    def get_int(self):
        '''读取整数'''
        value=self.cf.getint(self.section,self.option)
        return value
    def get_float(self):
        '''读取浮点数'''
        value=self.cf.getfloat(self.section,self.option)
        return value
    def get_bool(self):
        '''读取布尔值'''
        value=self.cf.getboolean(self.section,self.option)
        return value
    def get_data(self):
        '''读取其他类型，如列表，字典，元组'''
        value=self.cf.get(self.section,self.option)
        return eval(value) #转换成该数据原本的类型
    def get_str(self):
        '''读取字符串'''
        value=self.cf.get(self.section,self.option)
        return value
if __name__=='__main__':
    button=ReadConfig('xiaoqi.conf','TestCase','button').get_str()
    print(button)


from configparser import ConfigParser
from API_4.common import project_path
class ReadConfig:
    '''这是一个读取配置文件的类，完成配置文件不同类型数据的读取'''
    def __init__(self,file_name,section,option):
        self.section=section
        self.option=option
        self.cf=ConfigParser()
        self.cf.read(file_name,encoding='utf-8')

    def get_int(self):
        '''获取整数类型的值'''
        value=self.cf.getint(self.section,self.option)
        return value

    def get_float(self):
        '''获取浮点类型的值'''
        value=self.cf.getfloat(self.section,self.option)
        return value

    def get_bool(self):
        '''获取布尔类型的值'''
        value=self.cf.getboolean(self.section,self.option)
        return value

    def get_data(self):
        '''获取列表，字典，元组类型的值'''
        value=self.cf.get(self.section,self.option)
        return eval(value)
    def get_str(self):
        '''获取字符串类型的值'''
        value=self.cf.get(self.section,self.option)
        return value
#测试代码
if __name__=='__main__':
    s=ReadConfig(project_path.new_conf_path,'CASE','case_id').get_str()
    dict_1=eval(s)
    print(dict_1)
    # print(type(dict_1))
    # for i in dict_1:
    #     print(i)
    #     print(dict_1[i])
    #     print(type(dict_1[i]))






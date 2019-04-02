from configparser import ConfigParser
from API_1.common import project_path
class ReadConfig:
    '''这是一个配置类，完成各种数据类型的读取，并返回读取的值'''
    def __init__(self,file_name,section,option):
        '''初始化函数：定义参数
        file_name: 配置文件名字
        section: 配置文件的片区名
        option: 配置文件选项名'''
        self.cf=ConfigParser() #实例化
        self.cf.read(file_name,encoding='utf-8') #读取配置文件
        self.section=section
        self.option=option

    def get_int(self):
        '''该函数完成获取整数型的数据'''
        value=self.cf.getint(self.section,self.option)
        return value
    def get_float(self):
        '''该函数完成获浮点数的数据'''
        value=self.cf.getfloat(self.section,self.option)
        return value
    def get_bool(self):
        '''该函数完成获取布尔值的数据'''
        value=self.cf.getboolean(self.section,self.option)
        return value
    def get_data(self):
        '''该函数完成获取列表，字典，元组的数据'''
        value=self.cf.get(self.section,self.option)
        return eval(value)
    def get_str(self):
        '''该函数完成获取字符串的数据'''
        value=self.cf.get(self.section,self.option)
        return value
#测试代码
if __name__=='__main__':
    value=ReadConfig(project_path.conf_path,'CASE','case_id').get_data()
    print(value)
    print(type(value))





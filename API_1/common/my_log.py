import logging
from API_1.common.read_config import ReadConfig
from API_1.common import project_path
#创建日志收集器
class MyLog:
    '''这是一个日之类，根据Bug级别输入不同的日志信息，可以在配置文件里面自定义'''
    def __init__(self):
        self.logger_name=ReadConfig(project_path.conf_path,'LOG','logger_name').get_str()
        self.formatter=ReadConfig(project_path.conf_path,'LOG','formatter').get_str()
        self.stream_level=ReadConfig(project_path.conf_path,'LOG','stream_level').get_str()
        self.file_level = ReadConfig(project_path.conf_path, 'LOG', 'file_level').get_str()

    def my_log(self,logger_level,msg):
        '''函数：完成日志比对级别后输出对应日志内容，级别，文件名可以配置
        logger_level ：日志收集器的级别
        msg: 日志信息'''
        my_logger=logging.getLogger(self.logger_name)
        my_logger.setLevel(logger_level)
        #定义格式
        formatter=logging.Formatter(self.formatter)
        #输出渠道到控制台
        ch=logging.StreamHandler()
        ch.setLevel(self.stream_level)
        ch.setFormatter(formatter)
        #输出渠道到文本
        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')
        fh.setLevel(self.file_level)
        fh.setFormatter(formatter)
        #添加输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        #判断级别
        if logger_level=='DEBUG':
            my_logger.debug(msg)
        elif logger_level=='INFO':
            my_logger.info(msg)
        elif logger_level=='WARNING':
            my_logger.warning(msg)
        elif logger_level=='ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
        #移除输出渠道
        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)

    def debug(self,msg):
        '''输出DEBUG级别的日志信息
        msg:日志信息'''
        self.my_log('DEBUG',msg)
    def info(self,msg):
        self.my_log('INFO',msg)
    def warning(self, msg):
        self.my_log('DEBUG', msg)
    def error(self, msg):
        self.my_log('ERROR', msg)
    def critical(self, msg):
        self.my_log('CRITICAL', msg)

#测试代码
if __name__=='__main__':
    MyLog().info('这是一条info信息！')






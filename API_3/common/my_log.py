import logging
from API_3.common import project_path
from API_3.common.read_config import ReadConfig
class MyLog:
    '''这是一个日之类，完成日志可配置级别的收集'''
    def __init__(self):
        self.logger_name=ReadConfig(project_path.conf_path,'LOG','logger_name').get_str()
        self.stream_level=ReadConfig(project_path.conf_path,'LOG','stream_level').get_str()
        self.file_level=ReadConfig(project_path.conf_path,'LOG','file_level').get_str()
        self.formatter=ReadConfig(project_path.conf_path,'LOG','formatter').get_str()
    #配置日志收集器的名字
    def my_log(self,logger_level,msg):
        my_logger=logging.getLogger(self.logger_name)
        my_logger.setLevel(logger_level)
        #设置日志输出形式
        formatter=logging.Formatter(self.formatter)

        #设置日志输出渠道--控制台
        ch=logging.StreamHandler()
        ch.setLevel(self.stream_level)
        ch.setFormatter(formatter)
        #设置日志输出渠道--文本文件
        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')
        fh.setLevel(self.file_level)
        fh.setFormatter(formatter)
        #添加输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if logger_level=='DEBUG': #判断日志收集级别是DEBUG
            my_logger.debug(msg)
        elif logger_level=='INFO':
            my_logger.info(msg)
        elif logger_level=='WARNING':
            my_logger.warning(msg)
        elif logger_level=='ERROR':
            my_logger.error(msg)
        else: #判断日志收集级别是CRITICAL
            my_logger.critical(msg)
        #移除输出渠道
        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)

    def debug(self,msg):
        '''函数：收集debug级别日志'''
        self.my_log('DEBUG',msg)
    def info(self,msg):
        '''函数：收集info级别的日志'''
        self.my_log('INFO',msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)
if __name__=='__main__':
    MyLog().info('这是一条INFO信息！')
    MyLog().debug('这是一条debug信息！')
    MyLog().error('这是一条error信息！')









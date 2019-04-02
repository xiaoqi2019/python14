import logging
from week_8.class_0307.read_config import ReadConfig
#创建日志收集器
class MyLog:
    def __init__(self):
        self.logger_name=ReadConfig('xiaoqi.conf','LOG','logger_name').get_str()
        self.formatter=ReadConfig('xiaoqi.conf','LOG','formatter').get_str()
        self.stream_level=ReadConfig('xiaoqi.conf','LOG','stream_level').get_str()
        self.file_name=ReadConfig('xiaoqi.conf','LOG','file_name').get_str()
        self.file_level=ReadConfig('xiaoqi.conf','LOG','file_level').get_str()

    def my_log(self,logger_level,msg):
        my_logger=logging.getLogger(self.logger_name)
        my_logger.setLevel(logger_level)
        #设置日志输出形式
        formatter = logging.Formatter(self.formatter)
        #指定日志输出渠道--文本文件
        fh=logging.FileHandler(self.file_name,encoding='utf-8')
        fh.setLevel(self.file_level)
        fh.setFormatter(formatter)
        #指定日志输出渠道--控制台
        ch=logging.StreamHandler()
        ch.setLevel(self.stream_level)
        ch.setFormatter(formatter)

        my_logger.addHandler(fh)
        my_logger.addHandler(ch)
        #日志内容
        if logger_level=='DEBUG':
            my_logger.debug(msg)
        elif logger_level=='INFO':
            my_logger.info(msg)
        elif logger_level == 'WARNING':
            my_logger.warning(msg)
        elif logger_level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
        #关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)
    def info(self,msg):
        self.my_log('INFO',msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def error(self, msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__=='__main__':
    MyLog().error('这是一条error信息！')
    MyLog().info('这是一条info信息！')




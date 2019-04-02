# 结合配置文件类实现日志类的可配置
import logging
from week_7.class_0225.read_config import ReadConfig
class MyLog:
    def __init__(self):
        self.logger_name=ReadConfig('log.conf','LOG','logger_name').get_str()
        self.logger_level=ReadConfig('log.conf','LOG','logger_level').get_str()
        self.formatter=ReadConfig('log.conf','LOG','formatter').get_str()
        self.stream_level=ReadConfig('log.conf','LOG','stream_level').get_str()
        self.file_name=ReadConfig('log.conf','LOG','file_name').get_str()
        self.file_level=ReadConfig('log.conf','LOG','file_level').get_str()

    def my_log(self,msg):
        #第一步 创建日志收集器和设定级别和输出格式
        my_logger=logging.getLogger(self.logger_name)# 创建一个日志收集器
        my_logger.setLevel(self.logger_level)# 设置日志收集器的级别
        # 设置日志输出格式

        formatter = logging.Formatter(self.formatter)
        #第二步 创建日志输出渠道和设置级别
        #创建控制台输出渠道
        ch=logging.StreamHandler()
        ch.setLevel(self.stream_level)
        ch.setFormatter(formatter)
        #创建文本输出渠道
        fh=logging.FileHandler(self.file_name,encoding='utf-8')#文本输出渠道文件形式有两种.txt /.log
        fh.setLevel(self.file_level)
        fh.setFormatter(formatter)


        #第三步 日志收集器和输出渠道对接(注意：使用之后要移除)
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if self.logger_level=='DEBUG':
            my_logger.debug(msg)
        elif self.logger_level=='INFO':
            my_logger.info(msg)
        elif self.logger_level == 'WARNING':
            my_logger.warning(msg)
        elif self.logger_level=='ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        #第四步，移除输出渠道
        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)

#定义输出debug信息的函数
    # def debug(self,msg):
    #     self.my_log('DEBUG',msg)#调用my_log函数
    # def info(self,msg):
    #     self.my_log('INFO',msg)
    # def warning(self,msg):
    #     self.my_log('WARNING',msg)
    # def error(self,msg):
    #     self.my_log('ERROR',msg)
    # def critical(self,msg):
    #     self.my_log('CRITICAL',msg)

if __name__=='__main__':
    #对类进行实例化调用其函数
    ml=MyLog()
    ml.my_log('这是一条信息5')
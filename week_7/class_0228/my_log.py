# python有一个自带的日志系统 logging
# import logging
# root logger 收集日志的容器 如果不定义一个logger，那么久默认使用root logger
# handlers 渠道两种：控制台console 文本file_handler 默认渠道：console
# pre-defined format按照提前设置好的格式输出

# logging.debug('这是一个debug信息')
# logging.info('这是一个info信息')
# logging.warning('这是一个warning信息')
# logging.error('这是一个error信息')
# logging.critical('这是一个critical信息')

# 三步走：定义日志收集的容器，设置输出渠道，设置输出格式，输出对接
# 日志手机级别和输出级别取交集，也就是级别筛选两次
#日志五个级别:由低到高 DEBUG INFO WARNING ERROR CRITICAL

# 封装成日志类，参数化：对日志级别和信息进行参数化
# 编写一个日志类，能够实现输出文件到指定文件和console

import logging
from week_7.class_0225.read_config import ReadConfig
class MyLog:
    def my_log(self,level,msg):
        '''函数1'''
        #第一步 创建日志收集器和设定级别和输出格式
        my_logger=logging.getLogger('python14')# 创建一个日志收集器
        my_logger.setLevel(level)# 设置日志收集器的级别
        # 设置日志输出格式
        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-%(filename)s-%(name)s-日志信息:%(message)s')

        #第二步 创建日志输出渠道和设置级别
        #创建控制台输出渠道
        ch=logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)
        #创建文本输出渠道
        fh=logging.FileHandler('test.log',encoding='utf-8')#文本输出渠道文件形式有两种.txt /.log
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)


        #第三步 日志收集器和输出渠道对接(注意：使用之后要移除)
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        #第四步，移除输出渠道
        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)

#定义输出debug信息的函数
    def debug(self,msg):
        self.my_log('DEBUG',msg)#调用my_log函数
    def info(self,msg):
        self.my_log('INFO',msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__=='__main__':
    #对类进行实例化调用其函数
    MyLog().debug('这是一个debug信息！')
    MyLog().info('这是一条info信息！')
    MyLog().warning('这是一条warning信息！')












































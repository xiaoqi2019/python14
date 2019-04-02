#-*-coding:utf-8-*-
from mysql import connector
from API_6.common.read_config import ReadConfig
from API_6.common import project_path
class DoMySql:
    '''这是一个操作数据库的类，专门对数据库进行读取操作'''
    def do_msql(self,query,flag=1):
        '''query：sql查询语句
        flag：标志1 获取一条数据，2 获取多条数据'''
        db_config=ReadConfig(project_path.conf_path,'DB','db_config').get_data()#获取配置文件里面数据库信息
        cnn=connector.connect(**db_config) #连接数据库
        cursor=cnn.cursor() #获取游标，获取操作数据库的权限
        cursor.execute(query) #执行sql语句
        if flag==1:
            res=cursor.fetchone() #获取一条数据，以元组形式输出
        else:
            res=cursor.fetchall() #获取多条数据，以列表嵌套元组形式输出
        cnn.close()
        return res
if __name__=='__main__':
    query='select LeaveAmount from member where MobilePhone=15910298856'
    print(DoMySql().do_msql(query,2))


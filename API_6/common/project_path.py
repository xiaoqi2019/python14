#-*-coding:utf-8-*-
import os
#保存路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#测试数据路径
case_path=os.path.join(project_path,'test_cases','test_api.xlsx')
#配置文件路径
conf_path=os.path.join(project_path,'conf','test.conf')
#日志输出渠道
log_path=os.path.join(project_path,'test_result','test_log','test.log')
#测试报告路径
report_path=os.path.join(project_path,'test_result','test_report','test.html')
#新的配置文件路径
new_conf_path=os.path.join(project_path,'conf','test_new.conf')

#测试代码
if __name__=='__main__':
    print(project_path)
    print(case_path)
    print(conf_path)
    print(log_path)
    print(report_path)
    print(new_conf_path)
import os

#文件的路径放到这里
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]#当前文件目录切割两次

#测试用例的路径
case_path=os.path.join(project_path,'test_cases','test_api.xlsx')#拼接两次拿到测试用例路径

#日志路径
log_path=os.path.join(project_path,'test_result','test_log','test.log')

#报告路径
report_path=os.path.join(project_path,'test_result','test_report','test_report.html')

#配置文件路径
conf_path=os.path.join(project_path,'conf','case.conf')


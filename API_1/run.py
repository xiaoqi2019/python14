# 3）新建一个run.py文件，在这里面完成Excel数据的读取以及完成用例的执行，
# 并写回测试结果到Excel文档里面。 至此已经完成了接口自动化测试的第一步。
import unittest
from API_1.test_cases.test_cases import TestCases
from API_1.common import project_path
import HTMLTestRunnerNew
#创建测试套件
suite=unittest.TestSuite()
#加载测试用例
loader=unittest.TestLoader()
#按照测试模块加载用例
suite.addTest(loader.loadTestsFromTestCase(TestCases)) #加载测试用例类
#输出测试报告
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='2019年度计划报告',
                                            description='2019年的第一份报告',
                                            tester='xiaoqi')
    runner.run(suite)




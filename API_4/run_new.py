import unittest
from API_4.test_cases import test_cases_new
from API_4.common import project_path
import HTMLTestRunnerNew

#测试套件实例化
suite=unittest.TestSuite()
#加载测试用例
loader=unittest.TestLoader()
#添加测试用例
suite.addTest(loader.loadTestsFromModule(test_cases_new))
# suite.addTest(loader.loadTestsFromModule(test_register))
# suite.addTest(loader.loadTestsFromModule(test_login))
# suite.addTest(loader.loadTestsFromModule(test_recharge))
# suite.addTest(loader.loadTestsFromModule(test_withdraw))
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='2019年3月测试报告',
                                            description='2019年的第三份报告',
                                            tester='xiaoqi')
    runner.run(suite)


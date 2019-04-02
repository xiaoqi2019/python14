#-*-coding:utf-8-*-
import unittest
#from API_3.test_cases import test_recharge
# from API_3.test_cases import test_register
# from API_3.test_cases import test_login
# from API_3.test_cases import test_withdraw
from API_3.test_cases import test_addloan
#from API_3.test_cases import test_bidloan
# from API_3.test_cases import test_getloanlist
# from API_3.test_cases import test_GetInvestsByMemberId
# from API_3.test_cases import test_GetInvestsByLoanId
from API_3.common import project_path
import HTMLTestRunnerNew

#测试套件实例化
suite=unittest.TestSuite()
#加载测试用例
loader=unittest.TestLoader()
#添加测试用例
# suite.addTest(loader.loadTestsFromModule(test_register))
# suite.addTest(loader.loadTestsFromModule(test_login))
#suite.addTest(loader.loadTestsFromModule(test_recharge))
# suite.addTest(loader.loadTestsFromModule(test_withdraw))
suite.addTest(loader.loadTestsFromModule(test_addloan))
#suite.addTest(loader.loadTestsFromModule(test_bidloan))
# suite.addTest(loader.loadTestsFromModule(test_getloanlist))
# suite.addTest(loader.loadTestsFromModule(test_GetInvestsByMemberId))
# suite.addTest(loader.loadTestsFromModule(test_GetInvestsByLoanId))

with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='2019年3月测试报告',
                                            description='2019年的第三份报告',
                                            tester='xiaoqi')
    runner.run(suite)


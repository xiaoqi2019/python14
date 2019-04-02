import unittest
import HTMLTestRunnerNew
# from week_7.class_0301.class_unittest_learn import *
from week_7.class_0301 import class_unittest_learn
suite=unittest.TestSuite() #测试套件，收集存储用例

# 方法1：
# suite.addTest(TestAdd('test_001')) #测试用例的实例
# suite.addTest(TestAdd('test_002'))
# suite.addTest(TestSub('test_two_positive'))

loader=unittest.TestLoader()
#方法2：通过测试类来添加
# suite.addTest(loader.loadTestsFromTestCase(TestAdd))
# suite.addTest(loader.loadTestsFromTestCase(TestSub))
#方法3：通过测试模块来添加
suite.addTest(loader.loadTestsFromModule(class_unittest_learn))

with open('test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='2019年的自动化测试报告',
                                            description='2019年的第一份报告',
                                            tester='小七')
    runner.run(suite)#执行测试套件里面添加的用例

# with open('test.txt','w',encoding='utf-8') as file:
#     runner=unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2) #测试报告类TextTestRunner实例化
#     runner.run(suite)#执行测试套件里面添加的用例
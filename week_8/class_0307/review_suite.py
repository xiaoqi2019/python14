import unittest
#from week_8.class_0307.review_unittest import *
from week_8.class_0307 import review_unittest
import HTMLTestRunnerNew
#创建测试套件
suite=unittest.TestSuite()
#方法2：
loader=unittest.TestLoader()
#按照测试模块添加用例
suite.addTest(loader.loadTestsFromModule(review_unittest))
#按照测试类添加用例
# suite.addTest(loader.loadTestsFromTestCase(review_unittest.TestAdd))
# suite.addTest(loader.loadTestsFromTestCase(review_unittest.TestSub))

with open('test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=1,
                                            title='2019测试报告',
                                            description='2019年的第一份报告',
                                            tester='xiaoqi')
    runner.run(suite)

#方法1：
#添加测试用例
# suite.addTest(TestAdd('test_001'))
# suite.addTest(TestAdd('test_002'))
# with open('test.txt','w',encoding='utf-8') as file:
#     runner=unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
#     runner.run(suite)

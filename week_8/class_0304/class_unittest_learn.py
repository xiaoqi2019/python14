
#测试用例===准备好 类TestCase
#执行用例 套件TestSuite
# 测试报告类TextTestRunner  一致pass 不一致Failed  测试结果

#开始对加法进行单元测试
import unittest #引入单元测试模块
from ddt import ddt,data,unpack
test_data_1=[[1,2,3],
             [3,-2,1],
             [-1,-2,-3],
             [0,0,0]]
@ddt
class TestAdd(unittest.TestCase):
    def setUp(self):
        print('------开始执行测试用例了------')
    def tearDown(self):
        print('------测试用例执行完毕------')
    @data(*test_data_1)
    def test_001(self,L): #两个正数相加
        a=L[0]
        b=L[1]
        c=a+b
        try:
            self.assertEqual(L[2],c) #调用父类的断言函数
        except AssertionError as e:
            print('测试用例执行失败，错误信息是：{}'.format(e))
            raise e
        print('测试结果是:{}'.format(c))





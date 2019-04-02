
#测试用例===准备好 类TestCase
#执行用例 套件TestSuite
# 测试报告类TextTestRunner  一致pass 不一致Failed  测试结果

#开始对加法进行单元测试
import unittest #引入单元测试模块
from week_7.class_0228.my_log import MyLog
class TestAdd(unittest.TestCase): #继承编写测试用例的类
    def setUp(self):
        print('------开始执行测试用例了------') #测试用例执行前的准备工作，比如环境部署，数据库连接，每执行一条测试用例就执行一次
    def tearDown(self):
        print('------测试用例执行完毕------') #用例执行完毕的清场工作，如断开数据库连接，每执行一条测试用例就执行一次
    def test_001(self): #两个正数相加
        a=1
        b=2
        expected=3
        c=a+b
        try:
            self.assertEqual(expected,c) #调用父类的断言函数
        except AssertionError as e:
            print('001测试用例执行失败，错误信息是：{}'.format(e))
            # raise e
            MyLog().error(e)
        print('两个正数相加的结果是:{}'.format(c))
    def test_002(self): #两个负数相加
        a=-1
        b=-2
        expected = -3
        c=a+b
        try:
            self.assertEqual(expected,c) #调用父类的断言函数
        except AssertionError as e:
            print('002测试用例执行失败，错误信息是：{}'.format(e))
            raise e
        print('两个负数相加的结果是:{}'.format(c))
    def test_003(self): #一正一负相加
        a=1
        b=-2
        c=a+b
        expected =-1
        try:
            self.assertEqual(expected,c) #调用父类的断言函数
        except AssertionError as e:
            print('003测试用例执行失败，错误信息是：{}'.format(e))
            raise e
        print('一正一负相加的结果是:{}'.format(c))
    def test_004(self): #两个0相加
        a=0
        b=0
        c=a+b
        expected =0
        try:
            self.assertEqual(expected,c) #调用父类的断言函数
        except AssertionError as e:
            print('004测试用例执行失败，错误信息是：{}'.format(e))
            raise e
        print('两个0相加的结果是:{}'.format(c))

class TestSub(unittest.TestCase):
    def setUp(self):
        print('------开始执行测试用例了------')
    def tearDown(self):
        print('------测试用例执行完毕------')
    def test_two_positive(self): #两个正数相减
        a=1
        b=2
        c=a-b
        expected =-1
        try:
            self.assertEqual(expected,c) #调用父类的断言函数
        except AssertionError as e:
            print('两个正数相减用例执行失败，错误信息是：{}'.format(e))
            raise e
        print('两个正数相减的结果是:{}'.format(c))
    def test_two_negative(self): #两个负数相减
        a=1
        b=2
        c=a-b
        expected =-1
        try:
            self.assertEqual(expected,c) #调用父类的断言函数
        except AssertionError as e:
            print('两个负数相减用例执行失败，错误信息是：{}'.format(e))
            raise e
        print('两个负数相减的结果是:{}'.format(c))
    def test_positive_negative(self): #一正一负相减
        a=3
        b=-2
        c=a-b
        expected =5
        try:
            self.assertEqual(expected,c) #调用父类的断言函数
        except AssertionError as e:
            print('一正一负相减用例执行失败，错误信息是：{}'.format(e))
            raise e
        print('一正一负相减的结果是:{}'.format(c))
    def test_two_zero(self): #两个0相减
        a=0
        b=0
        c=a-b
        expected =0
        try:
            self.assertEqual(expected,c) #调用父类的断言函数
        except AssertionError as e:
            print('两个0相减用例执行失败，错误信息是：{}'.format(e))
            raise e
        print('两个0相减的结果是:{}'.format(c))




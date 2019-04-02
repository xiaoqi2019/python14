import unittest
from week_8.class_0307.my_log import MyLog
class TestAdd(unittest.TestCase):
    def setUp(self):
        print('------开始执行测试用例！------')
    def tearDown(self):
        print('------用例执行完毕！------')
    def test_001(self):
        a=1
        b=2
        excepted=3
        c=a+b
        try:
            self.assertEqual(c,excepted)
        except Exception as e:
            print('错误信息是：{}'.format(e))
            raise e
        print('两个正数相加的结果是：{}'.format(c))
    def test_002(self):
        a=-1
        b=-2
        excepted=-3
        c=a+b
        try:
            self.assertEqual(c,excepted)
        except Exception as e:
            MyLog().error(e)
        print('两个负数相加的结果是：{}'.format(c))
class TestSub(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例！')
    def tearDown(self):
        print('用例执行完毕！')
    def test_two_positive(self):
        a=1
        b=2
        excepted=3
        c=a-b
        try:
            self.assertEqual(c,excepted)
        except Exception as e:
            MyLog().error(e)
        print('两个正数相减的结果是：{}'.format(c))
    def test_two_negative(self):
        a=-1
        b=-2
        excepted=-3
        c=a-b
        try:
            self.assertEqual(c,excepted)
        except Exception as e:
            MyLog().error(e)
        print('两个负数相减的结果是：{}'.format(c))
import unittest
from ddt import ddt,data,unpack
# a=(1,2,3)
test_data_1=[[1,2,4],[3,-2,1]]
test_data_2=[{'a':1,'b':2,'excepted':3},{'a':3,'b':-2,'excepted':1}]

#对列表进行拆分
@ddt #装饰测试类
class TestPrintMsg(unittest.TestCase):
    @data(*test_data_1) #装饰测试用例
    def test_001(self,x):
        print('我在执行第{}条测试用例'.format(x))
        print('a:',x)
        a=x[0]
        b=x[1]
        c=a+b
        print('c:',c)
        self.assertEqual(c,x[2])

#对字典进行拆分
# @ddt #装饰测试类
# class TestPrintMsg(unittest.TestCase):
#     @data(*test_data_2) #装饰测试用例
#     def test_001(self,dict):
#         print('我在执行第{}条测试用例'.format(dict))
#         print('a:',dict)
#         c=dict['a']+dict['b']
#         print('c:',c)
#         self.assertEqual(c,dict['excepted'])

@ddt
class TestPrintMsg(unittest.TestCase):
    @data(*test_data_2)
    @unpack
    def test_0002(self,a,b,excepted):
        c=a+b
        try:
            self.assertEqual(c,excepted)
        except AssertionError as e:
            print('断言错误：{}'.format(e))
        # print('c:',c)

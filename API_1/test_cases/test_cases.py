from API_1.common.http_request import HttpRequest
from API_1.common.do_excel import DoExcel
from API_1.common import project_path
from API_1.common.my_log import MyLog
from ddt import ddt,data,unpack
import unittest
import warnings
import requests

#思考问题：如何分开模块执行用例呢？可不可以在单元测试里面区分模块
#单元测试去等同于run文件的作用
test_data = DoExcel(project_path.case_path,'test_case','tel').read_excel()

@ddt #引入装饰器
class TestCases(unittest.TestCase):
    '''该类执行测试用例'''

    def setUp(self):#执行用例前的准备工作
        self.de=DoExcel(project_path.case_path,'test_case','tel')

    def tearDown(self):#执行用例后的清场工作
        pass

    @data(*test_data)
    def test_cases(self,case):
        '''函数：完成用例执行'''
        global test_result
        global res_1

        warnings.simplefilter('ignore', ResourceWarning) #过warnings库来忽略掉相关告警
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])

        #开始执行用例
        MyLog().info('---正在执行{}模块第{}条用例，用例名称：{}'.format(case['Moudle'],case['CaseId'], case['Title']))
        MyLog().info('测试数据是：{}'.format(case))

        res_1=requests.get( 'http://47.107.168.87:8080/futureloan/mvc/api/member/login',{'mobilephone':'15910298856', 'pwd':'123456'})
        print(res_1.text)
        print(res_1.cookies)
        resp=HttpRequest().http_request(method,url,param,res_1.cookies)
        print(resp.json())
        # if case['Moudle'] =='recharge':
        #     res1 = HttpRequest().http_request('post','http://47.107.168.87:8080/futureloan/mvc/api/member/login',{'mobilephone':'15910298856','pwd':'123456'})
        #     print(res1.text)
        #     print(res1.cookies)
        #     resp = HttpRequest().http_request(method,url,param,cookies=res1.cookies)
        # else:
        #     resp=HttpRequest().http_request(method,url,param,cookies=None)
        print(eval(case['ExceptedResult']))
        try:
            self.assertEqual(resp.json(),eval(case['ExceptedResult']))
            test_result='Pass'
        except AssertionError as e:
            test_result='Failed'
            MyLog().error('结果比对出错了，错误是{}'.format(e))
            raise e#处理完异常之后  不要留在家里 要抛出去！ raise e
        finally:
            #写回结果
            self.de.write_back(case['CaseId']+1,8,resp.text)
            self.de.write_back(case['CaseId']+1,9,test_result)
        MyLog().info('实际结果是：{}'.format(resp.json()))
        MyLog().info('通过情况：{}'.format(test_result))
#记得鼠标放到末尾行执行用例！


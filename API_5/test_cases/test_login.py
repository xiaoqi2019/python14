#-*-coding:utf-8-*-
import unittest
from ddt import ddt,data,unpack
from API_5.common.http_request import HttpRequest
from API_5.common.my_log import MyLog
from API_5.common.do_excel import DoExcel
from API_5.common import project_path
import warnings
#测试登陆接口
test_data=DoExcel(project_path.case_path,'login').read_excel('LoginCASE')
COOKIES=None
@ddt #引入ddt
class TestCases(unittest.TestCase):
    '''该类执行测试用例'''
    def setUp(self):
        MyLog().info('执行用例前的准备工作！')
        self.de=DoExcel(project_path.case_path,'login')
    def tearDown(self):
        MyLog().info('执行用例后的清场工作！')
    @data(*test_data)
    def test_cases(self,case):
        '''函数：完成用例的执行'''
        global test_result
        global COOKIES
        warnings.simplefilter('ignore',ResourceWarning) # 过warnings库来忽略掉相关告警
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])

        #开始执行用例
        MyLog().info('开始执行模块{}第{}条用例：{}'.format(case['Moudle'],case['CaseId'],case['Title']))
        MyLog().info('测试数据：{}'.format(case['Params']))

        resp=HttpRequest().http_request(method,url,param,cookies=COOKIES)
        MyLog().info('实际结果是：{}'.format(resp.json()))
        if resp.cookies:
            COOKIES=resp.cookies
        try:
            self.assertEqual(resp.json(),eval(case['ExceptedResult']))
            test_result='Pass'
        except AssertionError as e:
            test_result='Failed'
            MyLog().error('用例执行出错，错误信息{}'.format(e))
            raise e #处理完异常之后  不要留在家里 要抛出去！ raise e
        finally:
            self.de.write_back(case['CaseId']+1,9,resp.text)
            self.de.write_back(case['CaseId']+1,10,test_result)
        MyLog().info('测试通过情况：{}'.format(test_result))








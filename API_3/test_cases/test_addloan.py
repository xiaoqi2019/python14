import unittest
from ddt import ddt,data,unpack
from API_3.common.http_request import HttpRequest
from API_3.common.my_log import MyLog
from API_3.common.do_excel import DoExcel
from API_3.common import project_path
from API_3.common.get_data import GetData
import warnings

#测试充值接口
test_data=DoExcel(project_path.case_path,'add_loan').read_excel('AddLoanCASE')

@ddt #引入ddt
class TestCases(unittest.TestCase):
    '''该类执行测试用例'''
    def setUp(self):
        MyLog().info('执行用例前的准备工作！')
        self.de=DoExcel(project_path.case_path,'add_loan')
    def tearDown(self):
        MyLog().info('执行用例后的清场工作！')
    @data(*test_data)
    def test_cases(self,case):
        '''函数：完成用例的执行'''
        global test_result
        warnings.simplefilter('ignore',ResourceWarning) # 过warnings库来忽略掉相关告警
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])

        #开始执行用例
        MyLog().info('开始执行模块{}第{}条用例：{}'.format(case['Moudle'],case['CaseId'],case['Title']))
        MyLog().info('测试数据：{}'.format(case['Params']))

        resp=HttpRequest().http_request(method,url,param,cookies=getattr(GetData,'COOKIE'))#动态传入COOKIE的值
        MyLog().info('实际结果是：{}'.format(resp.json()))
        #http请求发生之后再加判断，判断是否产生了cookies
        if resp.cookies: #如果产生了，动态传给类属性COOKIE
            setattr(GetData,'COOKIE',resp.cookies)  #动态更改属性COOKIE的值
        try:
            self.assertEqual(resp.json(),eval(case['ExceptedResult']))
            test_result='Pass'
        except AssertionError as e:
            test_result='Failed'
            MyLog().error('用例执行出错，错误信息{}'.format(e))
            raise e #处理完异常之后  不要留在家里 要抛出去！ raise e
        finally:
            self.de.write_back(case['CaseId']+1,8,resp.text)
            self.de.write_back(case['CaseId']+1,9,test_result)
        MyLog().info('测试通过情况：{}'.format(test_result))








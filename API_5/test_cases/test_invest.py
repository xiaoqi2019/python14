#-*-coding:utf-8-*-
import unittest
from ddt import ddt,data,unpack
from API_5.common.http_request import HttpRequest
from API_5.common.my_log import MyLog
from API_5.common.do_excel import DoExcel
from API_5.common import project_path
from API_5.common.get_data import GetData
from API_5.common.do_mysql import DoMySql
import warnings

#测试充值接口
test_data=DoExcel(project_path.case_path,'invest').read_excel('BidLoanCASE')

@ddt #引入ddt
class TestCases(unittest.TestCase):
    '''该类执行测试用例'''
    def setUp(self):
        MyLog().info('执行用例前的准备工作！')
        self.de=DoExcel(project_path.case_path,'invest')
    def tearDown(self):
        MyLog().info('执行用例后的清场工作！')
    @data(*test_data)
    def test_cases(self,case):
        '''函数：完成用例的执行'''
        global test_result
        global leave_amount_1 #定义投标前余额
        global leave_amount_2 #定义投标后余额
        # global bid_amount #定义投标额
        global different_amount #定义投标前后余额差额
        warnings.simplefilter('ignore',ResourceWarning) # 过warnings库来忽略掉相关告警
        method=case['Method']
        url=case['Url']
        if 'loanid' in case['Params']: #判断参数里面是否有loanid，如果有替换掉
            param=eval(case['Params'].replace('loanid',str(getattr(GetData,'LOANID'))))
            # print(getattr(GetData,'LOANID'))
        else:
            param=eval(case['Params'])

        #开始执行用例
        MyLog().info('开始执行模块{}第{}条用例：{}'.format(case['Moudle'],case['CaseId'],case['Title']))
        MyLog().info('测试数据：{}'.format(case['Params']))

        resp=HttpRequest().http_request(method,url,param,cookies=getattr(GetData,'COOKIE'))#动态传入COOKIE的值
        MyLog().info('实际结果是：{}'.format(resp.json()))

        #获取用户充值前余额的初始值
        if case['CaseId']==1:
            leave_amount=DoMySql().do_msql(eval(case['Sql'])['sql'],1)[0] #获得充值前用户余额
            setattr(GetData,'LEAVE_AMOUNT',leave_amount)
            print('投资前余额：{}'.format(leave_amount))
        elif case['CaseId']==2:
            leave_amount_2=DoMySql().do_msql(eval(case['Sql'])['sql'],1)[0] #获得充值后用户余额
            setattr(GetData,'LEAVE_AMOUNT_AFTER',leave_amount_2)
            print('投资后余额：{}'.format(leave_amount_2))
            try:
                self.assertEqual(resp.json(), eval(case['ExceptedResult']))
                try:
                    self.assertEqual(getattr(GetData,'LEAVE_AMOUNT_AFTER')-getattr(GetData,'LEAVE_AMOUNT'),float(eval(case['Params'])['amount']))
                    test_result='Pass'
                except Exception as e:
                    MyLog().error('投资前后差额和实际投资数额不相等，错误信息：{}'.format(e))
                    test_result = 'Failed'
                    raise e
            except AssertionError as e:
                test_result = 'Failed'
                MyLog().error('用例执行出错，错误信息{}'.format(e))
                raise e  # 处理完异常之后  不要留在家里 要抛出去！ raise e

        #http请求发生之后再加判断，判断是否产生了cookies
        if resp.cookies: #如果产生了，动态传给类属性COOKIE
            setattr(GetData,'COOKIE',resp.cookies)  #动态更改属性COOKIE的值

        if case['CaseId']!=2:
            try:
                self.assertEqual(resp.json(),eval(case['ExceptedResult']))
                test_result = 'Pass'
            except AssertionError as e:
                test_result='Failed'
                MyLog().error('用例执行出错，错误信息{}'.format(e))
                raise e #处理完异常之后  不要留在家里 要抛出去！ raise e

        self.de.write_back(case['CaseId']+1,9,resp.text)
        self.de.write_back(case['CaseId']+1,10,test_result)
        MyLog().info('测试通过情况：{}'.format(test_result))








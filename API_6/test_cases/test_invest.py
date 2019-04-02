#-*-coding:utf-8-*-
import unittest
from ddt import ddt,data,unpack
from API_6.common.http_request import HttpRequest
from API_6.common.my_log import MyLog
from API_6.common.do_excel import DoExcel
from API_6.common import project_path
from API_6.common.get_data import GetData
from API_6.common.do_mysql import DoMySql
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
        global before_amount
        global after_amount
        warnings.simplefilter('ignore',ResourceWarning) # 过warnings库来忽略掉相关告警
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])
        # if 'loanid' in case['Params']: #判断参数里面是否有loanid，如果有替换掉
        #     param=eval(case['Params'].replace('loanid',str(getattr(GetData,'LOANID'))))
        #     # print(getattr(GetData,'LOANID'))
        # else:
        #     param=eval(case['Params'])
        #判断并取出投资前的余额
        if case['Sql']!=None:
            sql=eval(case['Sql'])['sql'] #取出查询余额的sql语句
            before_amount=DoMySql().do_msql(sql,1)[0]

        #开始执行用例
        MyLog().info('开始执行模块{}第{}条用例：{}'.format(case['Moudle'],case['CaseId'],case['Title']))
        MyLog().info('测试数据：{}'.format(case['Params']))
        resp=HttpRequest().http_request(method,url,param,cookies=getattr(GetData,'COOKIE'))#动态传入COOKIE的值
        MyLog().info('实际结果是：{}'.format(resp.json()))

        #http请求发生之后再加判断，判断是否产生了cookies
        if resp.cookies: #如果产生了，动态传给类属性COOKIE
            setattr(GetData,'COOKIE',resp.cookies)  #动态更改属性COOKIE的值

        # 判断并取出投资后的余额
        if case['Sql'] != None:
            sql = eval(case['Sql'])['sql']  # 取出查询余额的sql语句
            after_amount = DoMySql().do_msql(sql, 1)[0]

        try:
            #再加一个断言，与的关系
            if case['CaseId']==2:
                invest_amount=param['amount']
                excepted_amount=float(before_amount)-float(invest_amount)
                self.assertEqual(excepted_amount,float(after_amount))
            self.assertEqual(resp.json(), eval(case['ExceptedResult']))
            test_result = 'Pass'
        except Exception as e:
            test_result='Failed'
            MyLog().error('用例执行出错，错误信息{}'.format(e))
            raise e #处理完异常之后  不要留在家里 要抛出去！ raise e

        self.de.write_back(case['CaseId']+1,9,resp.text)
        self.de.write_back(case['CaseId']+1,10,test_result)
        MyLog().info('测试通过情况：{}'.format(test_result))








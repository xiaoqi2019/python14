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
test_data=DoExcel(project_path.case_path,'recharge').read_excel('RechargeCASE')

@ddt #引入ddt
class TestCases(unittest.TestCase):
    '''该类执行测试用例'''
    def setUp(self):
        MyLog().info('执行用例前的准备工作！')
        self.de=DoExcel(project_path.case_path,'recharge')
    def tearDown(self):
        MyLog().info('执行用例后的清场工作！')
    @data(*test_data)
    def test_cases(self,case):
        '''函数：完成用例的执行'''
        global test_result
        global before_amount #定义重置后期望余额
        global after_amount
        global excepted_amount
        warnings.simplefilter('ignore',ResourceWarning) # 过warnings库来忽略掉相关告警
        method=case['Method']
        url=case['Url']
        param=eval(case['Params'])
        #取出充值前余额
        if case['Sql']!=None:
            sql=eval(case['Sql'])['sql']
            before_amount=DoMySql().do_msql(sql,1)[0]

        #开始执行用例
        MyLog().info('开始执行模块{}第{}条用例：{}'.format(case['Moudle'],case['CaseId'],case['Title']))
        MyLog().info('测试数据：{}'.format(case['Params']))
        resp=HttpRequest().http_request(method,url,param,cookies=getattr(GetData,'COOKIE'))#动态传入COOKIE的值
        MyLog().info('实际结果是：{}'.format(resp.json()))

        #http请求发生之后再加判断，判断是否产生了cookies
        if resp.cookies: #如果产生了，动态传给类属性COOKIE
            setattr(GetData,'COOKIE',resp.cookies)  #动态更改属性COOKIE的值

        #获取用户充值后余额
        if case['Sql']!=None:
            sql=eval(case['Sql'])['sql']
            after_amount=DoMySql().do_msql(sql,1)[0]

        try:
            #再加一个充值前后余额对比的断言
            #判断第二条验证充值正常的用例多一条断言
            if case['CaseId']==2:
                charge_amount=param['amount']
                excepted_amount=float(before_amount)+float(charge_amount)
                self.assertEqual(excepted_amount,float(after_amount))
            # 判断期望结果里面存在变量参数excepted_amount，存在就替换成期望余额
            if case['ExceptedResult'].find('excepted_amount')>-1:
                case['ExceptedResult']=case['ExceptedResult'].replace('excepted_amount',str(excepted_amount)) #接收期望余额
            self.assertEqual(resp.json(), eval(case['ExceptedResult']))
            test_result='Pass'
        except Exception as e:
            test_result='Failed'
            MyLog().error('用例执行出错，错误信息{}'.format(e))
            raise e #处理完异常之后  不要留在家里 要抛出去！ raise e

        self.de.write_back(case['CaseId']+1,9,resp.text)
        self.de.write_back(case['CaseId']+1,10,test_result)
        MyLog().info('测试通过情况：{}'.format(test_result))








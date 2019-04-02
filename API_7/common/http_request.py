#-*-coding:utf-8-*-
import requests
from API_7.common.my_log import MyLog
class HttpRequest:
    '''这是一个完成不同请求的类'''
    def http_request(self,method,url,param,cookies):
        '''函数：根据方法完成不同的请求
        method:方法名
        url: 请求地址
        param：请求参数'''
        global resp
        if method.upper()=='GET':
            try:
                resp=requests.get(url,params=param,cookies=cookies) #完成get方式的请求，传递cookies
            except Exception as e:
                MyLog().error('请求出错了，错误信息：{}'.format(e))
        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param,cookies=cookies) #完成post方式的请求，传递cookies
            except Exception  as e:
                MyLog().error('请求出错了，错误信息：{}'.format(e))
        else:
            MyLog().info('不支持该请求！')
            resp=None
        return resp

#测试代码
if __name__=='__main__':
    resp=HttpRequest().http_request('post','http://47.107.168.87:8080/futureloan/mvc/api/member/register',{'mobilephone':'15900000000','pwd':'123456','regname':'xiaoqi'},cookies=None)
    print(resp.text)
    print(resp.json())



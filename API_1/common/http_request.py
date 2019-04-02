#1：根据提供的注册登录接口，完成注册登录接口的请求，至少每个接口有5条用例，每个接口要至少有一个正向用例。
#2：要求如下：
# 1）http请求类（可以根据传递的method--get/post完成不同的请求），要求有返回值。
# 2）测试用例的数据存储在Excel中，并编写一个从Excel中读取数据的测试类，包含的
# 函数能够读取测试数据，并且能够写回测试结果，要求有返回值。
# 3）新建一个run.py文件，在这里面完成Excel数据的读取以及完成用例的执行，
# 并写回测试结果到Excel文档里面。 至此已经完成了接口自动化测试的第一步。
import requests
class HttpRequest:
    '''该类完成http的get和post请求，并返回结果'''
    def http_request(self,method,url,param,cookies=None):
        '''根据请求方法来决定发起get请求和post请求
        method: get post http的请求方式
        url: 发送请求的接口地址
        param: 随接口发送的请求参数 以字典格式传递
        rtype:有返回值，返回结果是响应报文
        '''
        if method.upper()=='GET':
            try:
                resp=requests.get(url,params=param,cookies=None)
            except Exception as e:
                print('get方式请求出错了：'.format(e))
        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param,cookies=None)
            except Exception as e:
                print('post请求方式出错了：'.format(e))
        else:
            print('不支持该种请求方式')
            resp=None
        return resp

#测试代码
if __name__=='__main__':
    hr=HttpRequest()
    url='http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    param={'mobilephone':'13459268463','pwd':'123456'}
    resp=hr.http_request(method='get',url=url,param=param)
    print(resp)
    # print(resp.text)
    print(resp.json())
    # print(resp.cookies)
    # print(resp.request.headers)

#-*-coding:utf-8-*-
#@Time  :2019/2/19 17:19
#@Author:xiaoqi
#@File  :http_requests.py
# requests模块 pip install requests
# python拿来主义

#2：编写一个类：你们自行去设计，要求写一个类， 初始化函数 对象函数 包含
#根据你不同的选择完成get请求 OR post请求 ，其中url 需要做参数化，并且最后要拿到响应结果

#老师讲解后自己coding
import requests
class HttpRequest:
    def __init__(self,url,method='get'):
        self.url=url
        self.method=method

    def requests_method(self):
        if self.method.lower()=='get':
            print('正在发起get请求：')
            try:
                resp=requests.get(self.url)
            except Exception as e:
                print('错误信息：',e)
        else:
            print('正在发起post请求：')
            resp=requests.post(self.url)
        return resp.text#返回结果
res=HttpRequest('http://www.baidu.com','post').requests_method()
print(res)



















#引入requests模块
# import requests
# class RequestClass:
#     '''这是一个完成对不同的url地址完成不同请求的类'''
#     #初始化参数，类通过初始化参数进行传url地址
#     def __init__(self,url):
#         self.url=url
#
#     #对象函数，完成为url地址的get请求
#     def method_get(self):
#         res=requests.get(self.url)#调用requests模块的get请求方法
#         print(res.text)
#
#     #对象函数，完成为url地址的post请求
#     def method_post(self):
#         res=requests.post(self.url)#调用requests模块的post请求方法
#         print(res.text)
#
# #实例化
# if __name__=='__main__':
#     p=RequestClass('http://baidu.com')#传参
#     p.method_get()#调用get方法
#     p.method_post()#调用post方法
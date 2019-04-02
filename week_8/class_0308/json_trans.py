import json
import requests
# s='{"status":0,"code":"20110","data":null,"msg":"手机号码已被注册"}'
# print(type(s))
# value=json.loads(s) #字符串转成字典格式
# print(value)
# print(type(value))
# print('-------------------------------------')
# new=json.dumps(value,ensure_ascii=False) #字典转成字符串格式
# print(new)
# print(type(new))
# s={'status': 0, 'code': '20110', 'data': None, 'msg': '手机号码已被注册'}
# s='{"status":0,"code":"20110","data":null,"msg":"手机号码已被注册"}'
# print(type(s))
# s1='{"status":0,"code":"20110","msg":"手机号码已被注册"}'
# print(type(s1))
# print(s1 in s)
# url_register='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
# param={'mobilephone':'15910298856','pwd':'123456'}
# headers={'User-Agent': 'Mozilla/5.0'}
# resp_1=requests.get(url=url_register,params=param,headers=headers)
# print(resp_1.text) #字符串格式
# print(resp_1.json()) #字典格式
# print('cookies:',resp_1.cookies)
# print('响应头',resp_1.headers)
# print('状态码：',resp_1.status_code)
# print('请求头：',resp_1.request.headers)

#测试充值接口
# url_invest='http://47.107.168.87:8080/futureloan/mvc/api/member/bidLoan'
# param_2={'memberId':'1123563','pwd':'123456','loanId':'17979','amount':'200'}
# resp_2=requests.post(url_invest,data=param_2,cookies=resp_1.cookies)
# print(resp_2.text)
# print(resp_2.cookies)

# # -*- coding:utf-8 -*-
# #获取cookie
# import requests
# import json
#
# url = "https://www.baidu.com/"
# r = requests.get(url)
#
# #将RequestsCookieJar转换成字典
# c = requests.utils.dict_from_cookiejar(r.cookies)
#
# print(r.cookies)
# print(c)
#
# for a in r.cookies:
#     print(a.name,a.value)
# print('----------------------------------------------')
# res_1 = requests.get( 'http://47.107.168.87:8080/futureloan/mvc/api/member/login',{'mobilephone':'15910298856', 'pwd':'123456'})
# print(res_1.text)
# print(res_1.cookies)
# resp = requests.post('http://47.107.168.87:8080/futureloan/mvc/api/member/recharge',{'mobilephone':'15910298856','amount':'100'},cookies=res_1.cookies)
# print(resp.text)
a=100.55
print(int(a))










#-*-coding:utf-8-*-
from API_7.common.read_config import ReadConfig
from API_7.common import project_path
import re
class GetData:
    '''可以用来动态的更改，删除，获取数据'''
    COOKIE=None

    loanid=None #新添加的标id的初始值

    normal_user=ReadConfig(project_path.conf_path,'DATA','normal_user').get_str() #定义初始用户正常登陆的手机号
    normal_pwd=ReadConfig(project_path.conf_path,'DATA','normal_pwd').get_str() #定义初始用户正常操作的用户id号
    normal_member_id=ReadConfig(project_path.conf_path,'DATA','normal_member_id').get_str() #定义用户常用的密码

def replace(target):
    '''函数：通过正则表达式完成参数里面的变量替换'''
    p='#(.*?)#'
    while re.search(p,target): #查找参数的字符串就匹配，有就返回True
        m=re.search(p,target)
        key=m.group(1) #返回匹配的字符串
        value=getattr(GetData,key) #拿到我们要去替换的值
        target=re.sub(p,value,target,count=1) #值的替换
    return target #返回新的字符串


if __name__=='__main__':
    target="{'mobilephone':'#normal_user#','pwd':'#normal_pwd#','memberid':'#normal_member_id#'}"
    res=replace(target)
    print(res)




    # print(GetData.COOKIES) #获取属性值
    # print(GetData().COOKIES)
    # print(getattr(GetData,'COOKIES'))#第一个参数是类名，第二个参数是属性名,获取类属性的值
    # print(setattr(GetData,'COOKIES','123456')) #修改属性值
    # print(setattr(GetData,'name','xiaoqi')) #添加类属性值
    # print(getattr(GetData,'COOKIES')) #重新获取
    # print(getattr(GetData,'name'))
    # print(delattr(GetData,'COOKIES'))
    # print(getattr(GetData,'COOKIES'))
    # print(setattr(GetData,'COOKIES','123456'))

    # print(getattr(GetData,'COOKIES'))
    # print(hasattr(GetData,'COOKIES')) #判断是否存在属性，结果为True或者False


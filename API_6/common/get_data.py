#-*-coding:utf-8-*-
class GetData:
    '''可以用来动态的更改，删除，获取数据'''
    COOKIE=None

    LOANID=None #新添加的标id的初始值

    MOBILEPHONE=15910298856 #定义初始用户正常登陆的手机号
    MEMBERID=1123563 #定义初始用户正常操作的用户id号
    MEMBER_PWD=123456 #定义用户常用的密码




if __name__=='__main__':
    # print(GetData.COOKIES) #获取属性值
    # print(GetData().COOKIES)
    # print(getattr(GetData,'COOKIES'))#第一个参数是类名，第二个参数是属性名,获取类属性的值
    # print(setattr(GetData,'COOKIES','123456')) #修改属性值
    # print(setattr(GetData,'name','xiaoqi')) #添加类属性值
    # print(getattr(GetData,'COOKIES')) #重新获取
    # print(getattr(GetData,'name'))
    # print(delattr(GetData,'COOKIES'))
    # print(getattr(GetData,'COOKIES'))
    print(setattr(GetData,'COOKIES','123456'))

    # print(getattr(GetData,'COOKIES'))
    # print(hasattr(GetData,'COOKIES')) #判断是否存在属性，结果为True或者False


class GetData:
    '''可以用来动态的更改，删除，获取数据'''
    COOKIE=None
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


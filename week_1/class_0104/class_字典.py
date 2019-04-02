#-*-coding:utf-8-*-
# 字典：dict{}
# d={}
# print(type(d))
# 字典的数据类型：key:value形式的
# key：不可变数据类型--》整数，浮点数，布尔值，元组，字符串
# value：任意数据类型--》整数，浮点数，布尔值，元组，字符串，列表，字典
# 字典是可变的，无序的，没有索引
# d={1:'666',
#    1.01:"这是华华老师的视力",
#    True:[1,2,3,4,5],
#    (1,2,3):[6,7,8],
#    'name':('jizi','钵钵鸡','行进着','和姑娘')}
# print(d)
# 输出结果，666不见了
# 因为：1代表True,0代表False
# key必须是唯一的，出现0和False，1和True不可以同时出现，出现四个任一都要引起注意
# d={1:'666',
#    1.01:"这是华华老师的视力",
#    False:[1,2,3,4,5],
#    (1,2,3):[6,7,8],
#    'name':('jizi','钵钵鸡','行进着','和姑娘'),
#    'hello':'你的大头鬼',
#    (2,3,4):(5,6)}
# print(d)#输出正确，输出顺序不确定
# 取值：取值方式：字典名[key]，根据key取值
# print(d[1.01])
# print(d['name'])
# print(d[(2,3,4)])
# 字典里面可以放字典吗？
# d={1:'666',
#    1.01:"这是华华老师的视力",
#    False:[1,2,3,4,5],
#    (1,2,3):[6,7,8],
#    'name':('jizi','钵钵鸡','行进着','和姑娘'),
#    'hello':'你的大头鬼',
#    (2,3,4):(5,6),
#    'class14':{1: '666',
#     1.01: "这是华华老师的视力",
#     False: [1, 2, 3, 4, 5],
#     (1, 2, 3): [6, 7, 8],
#     'name': ('jizi', '钵钵鸡', '行进着', '和姑娘'),
#     'hello': '你的大头鬼',
#     (2, 3, 4): (5, 6)}
#    }
# print(d)
# print(d['class14'])
# print(d['class14']['name'])
# # value值可以修改
# d['class14']['name']='不想要昵称'
# print(d)

d={"name":'华华',
   'hobby':'学Python',
   'age':18,
   'score':{'en':120,'math':99.99,'ch':'A'},
   'friend':['bay max','小CC','如意'],
   True:'good_man',
   0.02:'python',
   False:'这个value对应的key是布尔值',
   (1,2,3):'我就是元组大大！！！',
   0:'这是真爱呀',
   1:'socre is 99.9'}
# print(d)
# 输出结果：
# {'name': '华华', 'hobby': '学Python', 'age': 18, 'score': {'en': 120, 'math': 99.99, 'ch': 'A'}, 'friend': ['bay max', '小CC', '如意'], True: 'socre is 99.9', 0.02: 'python', False: '这是真爱呀', (1, 2, 3): '我就是元组大大！！！'}
# 原因：True和1是等效的，前面的把后面的给覆盖掉了，False和0同理

dict_01={'name':'xiaoqi','age':'26','sex':'female'}
# dict_01.pop('name') #删除相应key的键值对
# print(dict_01)
# dict_01.popitem() #默认删除最后面一对键值
# print(dict_01)
# dict_01.clear() #清除字典里面所有值
# print(dict_01)
# dict_01.copy() #copy字典
# print(dict_01)
dict_01.items()
print(dict_01.keys())
print(type(dict_01.keys()))
for i in dict_01:
   print(i)



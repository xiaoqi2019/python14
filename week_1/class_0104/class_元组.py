#-*-coding:utf-8-*-
# 元组：tuple()
# 空元组
# t=()
# print(type(t))
# 元组里面的数据可以是任意类型：整型，浮点型，字符串，元组，列表，字典都可以
# t=(1,0.03,True,'hello',(8,'lemon',99.9))
t=()
print(type(t))
# print(len(t))
# print(type(t))# 这个时候元组类型发生了变化
# 所以当元组只有一个元素时，后面需要加一个英文逗号保持元组的属性
t=(0,)
print(t)
print(type(t))
#元组取值(同字符串)，有索引，从0开始，有正序和倒序
# t=(1,0.03,True,'hello',(8,'lemon',99.9))
# print(type(t))
# print(t[0])
# print(t[-1])
# 元组也支持切片
# 取索引为偶数位的值
print(t[::2])
# print(t[::-1])
# print(len(t))
# print(type(t))
# print(str(t))
# print(t[-1:-5:-1])
# 取嵌套元素的值，假如取lemon
# print(t[4][-2])
# 想取0.01这个值呢？
# t_2=(1,0.03,True,'hello',(8,'lemon',99.9,(1,'ok',0.01)))
# print(t_2[4][3][-1])
# 特殊的逗号：除了在字符串里面算作一个元素，其他的都是用来分隔的。
# 元组是一个有序不可变的数据类型，字符串也是，一旦尝试修改值就会报错
# t[4][-2]=9
# s='1,2,4'
# s[-1]=3
# print(s)  # 报错：TypeError: 'str' object does not support item assignment
# 特殊情况
# t=(1,0.03,True,'hello',(8,'lemon',99.9),['刘晴','行者无疆'])
# t[-1][0]='小明'
# print(t)
#结果：(1, 0.03, True, 'hello', (8, 'lemon', 99.9), ['小明', '行者无疆'])
# 为什么成功呢？因为你这时候修改的是列表的元素


t=(1,3,1,'hello',True,(1,2,3,666,'Python'))
#取值元组最后一个元素里面的Python字符闯怎么取值
print(t[-1][-1])
print(t.count(3)) #计算元素3在元组里面出现的个数
print(t.index(1)) #查询元素1在元组里面第一次出现的索引位置










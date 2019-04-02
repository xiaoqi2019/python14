#-*-coding:utf-8-*-
# 列表：list[]
#空列表 查看数据类型
list=[]
print(type(list))
# 只有一个元素时也是列表（只有在元组里面存在：元组中只有一个元素时后面必须加逗号）
L=['hello']
print(type(L))
# 列表里面的数据可以是任意类型
L=[1,0.03,True,'hello',(8,'lemon',99.9),['刘晴','行者无疆']]
# 取值：行者无疆
print(L[5][-1])
# 取值：行
# print(L[-1][-1][0])
# 元组切片
# print(L[::2])
# 列表是一个有序可变数据类型，可以进行修改
# L[-1][-1]='爱'
# print(L)
# 假如三个层级
# L[-1][-1][-1]='爱'
# print(L) #报错：TypeError: 'str' object does not support item assignment（因为你修改的是字符串的元素）

t=[1,2,3,4,5,6,1]
# print(t.pop())#删除指定索引位置的元素，不指定默认删除最后一个
# print(t)
# t.remove(1) #移除指定的元素，只是移除第一个出现的
# print(t)
# t.clear() #清除列表内所有元素
# print(t)
t.copy() #copy列表所有元素
print(t)

#取出完整的列表
# print(t[::1])
# #倒序输出列表
# print(t[::-1])
# t.sort() #默认升序
# print(t)
# t.sort(reverse=True) #降序排列
# print(t)
#取偶数位/奇数位的列表元素怎么取
# print(t[::2])
# print(t[1::2])
# t.reverse() #反向排序
# print(t)
# t.append(7) #追加一个元素在列表后面
# print(t)
# t.insert(1,0) #在索引位置为1的元素那插入元素0
# print(t)
# t.extend((1,2,3)) #追加元素到列表里面
# print(t)
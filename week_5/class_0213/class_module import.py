#-*-coding:utf-8-*-
#@Time  :2019/2/15 14:01
#@Author:xiaoqi
#@File  :class_模块导入.py
 #导入 多种方式讲解 import

# 方法1：常用
# import week_5.class_0213.add_function
# res=week_5.class_0213.add_function.add(1,2)
# print(res)

#  方法2：
# import week_5.class_0213.add_function as t
# res=t.add(1,2)
# print(res)

# 方法3：常用
# from..路径..import..模块名或者函数名（或者*代表所有的函数）..（as ..函数别名..）
# from week_5.class_0213.add_function import add,add_2
# res=add(2,4)
# print(res)

# 方法4：
# from...import....as...给函数取别名
from week_5.class_0213.add_function import add_5_position_fun as a5
# a5(1,2,3,4,5)

# import week_3.class_0116.class_内置函数
# from week_3.class_0116 import class_内置函数
# from week_3.class_0116.class_内置函数 import *

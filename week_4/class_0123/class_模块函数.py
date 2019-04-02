#-*-coding:utf-8-*-
#@Time  :2019/1/31 11:23
#@Author:xiaoqi
#@File  :class_模块函数.py

def student_info(num,name,offer):
    print('{}期的{}同学拿到了{}k的offer!!!恭喜恭喜！！'.format(num,name,offer))
def eat(*food_name):
    food_name_str=''
    for item in food_name:
        food_name_str+=item
        food_name_str+='、'
    food_name_str=food_name_str.strip('、')
    print('最喜欢吃：{}'.format(food_name_str))
if __name__=='__main__':
    eat('鸭翅','猪蹄','辣条')
 
#-*-coding:utf-8-*-
# 定义：成对的单引号，双引号，三引号（单引/双引）
# c='''好激动啊，今天要开始学习字符串啦！'''
# print(type(c))
# print(len(c))
# print(c[0])
# print(c[-1])
# print(c[::])
# print(c[12:15]) 步长：默认值为1
# print(c[-5:-2:1])
# 取偶数位
# print(c[2::-2])
# print(c[-1::-1])
year=2019
dreame_1='减肥15斤'
dream_2='去泰国旅游'
dream_3='加薪15k'
dream_4=173.5
print(type(year))
# 非常普通的输出
print(year,'我的梦想1是:',dreame_1,'我的梦想2是:',dream_2,'我的梦想3是:',dream_3,'我的梦想4是:',dream_4)
print(year,'我的梦想1是:'+dreame_1+' 我的梦想2是:'+dream_2+' 我的梦想3是:'+dream_3+' 我的梦想4是:',dream_4)
# str()表示可以转变你的数据类型-->字符串
# print(str(year)+'我的梦想1是:'+dreame_1+'我的梦想2是:'+dream_2+'我的梦想3是:'+dream_3+'我的梦想4是:'+str(dream_4))
# 格式化输出
# 保持你的格式，最好的输出方式就是三引号
# 如下：假如指定顺序{}内数字表示format（）括号内字符串位置，0,1,2,3，4
# 不指定顺序，就是默认的从0开始到最后，按照顺序赋值
# 有的给值，有的不给值----绝对不行！！！
print("{}年，我有4个梦想，分别是：梦想一：{}，梦想二：{}，梦想三：{}，梦想四：{}"
      .format(year,dreame_1,dream_2,dream_3,dream_4))
print('''{}年，我有4个梦想，分别是：
梦想一：{}
梦想二：{}
梦想三：{}
梦想四：{}
'''.format(year,dreame_1,dream_2,dream_3,dream_4))

s='HhWER23l123l0123'
print(s[::2])#取字符串的奇数位
print(s[1::2])#取字符串的偶数位
# print(s[::-2])
# print(s.capitalize())#首字母大写
# print(s.count('3')) #计算括号内元素在字符串中有几个
# print(s.find('n')) #计算元素n在字符串中第一次出现的位置
# print(s.index('n'))#同上
# print(s.islower())#判断字符串内字母是否全是小写
print(s.isdigit())
print(s.join(['ab', 'pq','rs'])) #将字符串s放到列表内给的元素中间，返回一个新的字符串
print(s.split('l',2)) #将字符串以l为边界切2次，成了三部分
print(s.swapcase()) #大小写替换
print(s.replace('H','h',2)) #将字符串内元素h替换成h2次

ss='qwetel123'
st='123'
# print('tel' in ss)
print(ss.replace('tel',st))
print(st)






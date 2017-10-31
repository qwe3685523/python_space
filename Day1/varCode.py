# -*- coding:utf-8 -*-
# 这是单行注释

msg = '''
多行注释
这么写
'''
# print msg
# msg = '''-----用户输入-----'''
# print msg
# username = input("input username:")
# msg = '''-----用户输入结束-----'''
##print msg
# print "userName is",username
# info = '''格式化字符串'''
# print info
# raw_input--和python3里面的input一样  python2里面的input 接收什么格式 就是什么格式
name = raw_input("name:")
print type(name)
age = raw_input("age:")
print type(age)
job = raw_input("job:")
print type(job)
# 普通格式化
info = '''----info of %s----
Name:%s
Age:%s
job:%s
''' % (name, name, age, job)
print info
# 官方推荐的格式化
info2 = '''----info of {_name}----
Name:{_name}
Age:{_age}
job:{_job}
'''.format(_name=name, _age=age, _job=job)
#格式化的新的一种
print info2
info3 = '''----info of {0}----
Name:{0}
Age:{1}
job:{2}
'''.format(name,age,job)
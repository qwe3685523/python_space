# -*- coding: utf-8 -*-
# 变量可以指向函数
# 函数的参数可以接受变量
# 一个函数可以接受另一个函数作为参数
#能接收函数做参数的函数就是高阶函数
#将系统求绝对值的abs 函数指向函数f
f = abs
#此时f 指向就是求绝对值的方法
d=f(-20)
print(d) 
#将len指向abs   调用abs  是求长度的方法 
abs  = len
d=abs([0,2,3])
print(d)
#demo 
abs = f
#定义一个函数接收 基本类型和函数 返回结算结果
def add (x,y,f):
	return f(x)+f(y)
print(add(-8,7,abs))
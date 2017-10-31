# -*- coding: utf-8 -*-
# reduce()函数也是Python内置的一个高阶函数。
# reduce()函数接收的参数和 map()类似，
# 一个函数 f，一个list，但行为和 map()不同，
# reduce()传入的函数 f 必须接收两个参数，
# reduce()对list的每个元素反复调用函数f，并返回最终结果值。
# reduce()还可以接收第3个可选参数，作为计算的初始值
# 输入：[2, 4, 5, 7, 12]
# 输出：2*4*5*7*12的结果
def prod(x,y):
    return x*y
print reduce(prod,[2,4,5,7,12])

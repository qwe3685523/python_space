# -*- coding:utf-8 -*-
# 变量
# 变量的赋值是直接指向变量所指向地址的更替，不存储变量本身的存储地址，所有在赋值过程中变量赋值的变更不影响先前使用过他的变量的值
name = 999
name2 = name
name = 888
# name2 value 还是999，因为name2赋值时指向的是name所存储的999的位置，所以当name的值指向变更为888后  name2的不变
# 常量python中没有常量的概念 要使用常量时用大写的变量代替常量来使用  注意本质上他还是个变量  我们人为的的约束自己不去进行这个变量的赋值更改
PIE = 555;
name = "Alex"
name2 = name
name = "zzzs"
print PIE - 5
print name2
# 字符编码

# -*- coding: utf-8 -*-
# map 方法的用法
# map()是 Python 内置的高阶函数，它接收一个函数和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
# demo
def format_name(s):
    # title() 将首字母变为大写，其他变为小写
    # capitalize（）Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。
    # upper() 转为大写  lower() 转为小写
    # return s.capitalize()
    # return s[0].upper() + s[1:].lower()
    return s.title();


L = ["sNams", "ascsfT", "TsgSF"]
s = map(format_name, L)
print s

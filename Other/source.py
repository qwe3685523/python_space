# -*- coding: utf-8 -*-
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

a = "请输入分数 \n"
str=input(a)
for i in d:
    if d[i] == str:
       print i
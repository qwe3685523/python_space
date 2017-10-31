# -*- coding:utf-8 -*-
# 导入密文标准块
import getpass

# username = raw_input("username:")
# password = getpass.getpass("password")
#
# if username == "zy" and password == "123456":
#     print "Login Success welcome {name} Login".format(name=username)
# else:
#     if username == "zy":
#         print "password is error"
#     else:
#         print "username is error"
#     print "Login Error"
'''if else And else if'''
myAge = 26

'''while 循环   
    和java不同的地方 while 可以接 else
'''
# count = 0
# while count < 3:
#     inputAge = input("AGE:")
#     if myAge == inputAge:
#         print "Good Job ,You guessed my age"
#         break
#     elif myAge > inputAge:
#         print "My Age Is Bigger than Input"
#     elif myAge < inputAge:
#         print "My Age Is Small than Input"
#     count = count + 1
# else:
#     print "you have tride too many times ... fuck off"
'''for循环
    for也带else
'''
# a = [5, 9, 6, 2]
# for i in a:
#     if i==2:
#         print "有 2 "
#         break
#     print i
# else:
#     print "走完了"
# for i in range(0,10,8):
#     print i
# for i in range(3):
#     inputAge = input("AGE:")
#     if myAge == inputAge:
#         print "Good Job ,You guessed my age"
#         break
#     elif myAge > inputAge:
#         print "My Age Is Bigger than Input"
#     elif myAge < inputAge:
#         print "My Age Is Small than Input"
# else:
#     print "you have tride too many times ... fuck off"
# count = 0
# while count < 3:
#     inputAge = int(raw_input("AGE:"))
#     if myAge == inputAge:
#         print "Good Job ,You guessed my age"
#         break
#     elif myAge > inputAge:
#         print "My Age Is Bigger than Input"
#     elif myAge < inputAge:
#         print "My Age Is Small than Input"
#     count += 1
#     if count == 3:
#         countintput = raw_input("Dou you want guess...")
#         if countintput != "n":
#             count = 0
# else:
#     print "Exit_System"
'''
break  结束整个循环
continue 跳出此次循环
'''
# for i in range(10):
#     print "------", i
#     for j in range(0, 10):
#         if j < 3:
#             print j
#         else:
#             break
for i in range(2,8):
    print i
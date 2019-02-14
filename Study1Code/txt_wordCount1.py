#!/usr/bin/env python
# encoding: utf-8

"""
@author: XuLongjia
@software: Sublime
@file: prase_pdf.py
@time: 2017/3/3 0003 11:16
@purpose: 读取txt并统计字数和数字
"""

import re                                           #导入正则表达式的包
f = open("C:/users/xu/desktop/ibm.txt","rt")        #读入年报文档
str_1=f.read()                                      #把整个txt变成一个字符串
str_1=str_1.replace(' ','')                         #把字符串中的空格全部去掉
print("该年报的字数为：{}".format(len(str_1)))      #输出年报总字数
str_num=re.findall(r"\d+\.?\d*",str_1)              #用正则表达式找出所有的数字
print("该年报一共有{}个数字".format(len(str_num)))  #输出年报所有的数字的个数
rate=len(str_num)/len(str_1)
print("数字占比为：{}".format(rate))
f.close()

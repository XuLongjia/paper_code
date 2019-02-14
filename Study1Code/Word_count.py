#!/usr/bin/env python
# encoding: utf-8

"""
@author: XuLongjia
@software: Sublime
@file: prase_pdf.py
@time: 2017/3/3 0003 11:16
@purpose: wrod count\
"""


import re
path=r'D:\xu\桌面\output25.txt'
with open(path,'rt',encoding='utf-8') as f:
        s=f.readlines()
        count=0
        for i in s:
                ls_1=[]
                re_str=re.split(r'[\s\,\.\:\;]',i)
                for j in re_str:
                        if j!='':
                                ls_1.append(j)
                count=count+len(ls_1)
print(count)
                

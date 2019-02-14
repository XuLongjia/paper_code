#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: rename.py
@time: 2018年11月2日15:55:41
@purpose: 重命名每个txt文件
"""

import os
import re

def main():
	path='D:/xu/桌面/10K/'  

	#获取该目录下所有文件，存入列表中
	f=os.listdir(path)
	for i in f:
		oldname = path + i
		ls = re.split('_',i)
		newname = path + ls[0][0:4] + '_' + ls[4] +'.txt'
		os.rename(oldname,newname)


		s= ls[0][0:4] + '_' + ls[4]
		print(i,"======>",s)

if __name__ == '__main__':
	main()



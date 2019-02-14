#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: phrase_count.py
@time: 2018年11月5日17:38:19
@purpose: 之前用nltk统计单词的词频，但是里面有几个短语的词频无法统计，本程序使用字符串匹配的方法统计那几个短语的词频
"""


import os
import numpy as np
import pandas as pd 

with open(file = 'phrase.txt',mode="rt") as f:
	phraseList = f.readlines()   #读入主题词
	phraseList = [phrase.strip() for phrase in phraseList]   #清除每个单词结尾的\n

columns = phraseList.copy()
res_csv = pd.DataFrame(columns = columns, dtype =int)


def main():	
	path = 'D:/xu/桌面/study2_text/10K/2017/'  
	corpus = os.listdir(path)
	for file in corpus:
		with open(file = path + file, mode="rt",encoding='utf-8',errors='ignore') as f:
			text = f.read()
			res = [text.count(phrase) for phrase in phraseList]
			res_csv.loc[file] = res
			print(file + ' ====> 统计完成!')
	res_csv.to_csv('2017_phrase.csv',index = True)

if __name__ == '__main__':
	main()
#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: data_score.py
@time: 2018年12月6日22:21:58
"""
import os
import pandas as pd
from nltk.tokenize import word_tokenize    #分词函数  

def main():
	with open('score.txt',encoding = 'utf-8') as f:
		ls = f.readlines()
	ls.pop(0)
	ls = [i.strip('\n') for i in ls]

	path= 'ceo_letter/'
	corpus = os.listdir(path)    #返回一个列表，保存所有文件的路径
	for file in corpus:
		with open(file = path + file, mode="rt",encoding='utf-8',errors='ignore') as f:
			text = f.read()
			tokens = word_tokenize(text)  #进行分词，形成一个list
			total_word = len(tokens)
			total_topicword = 0
			topic_word_ls = [test.count(i) for i in ls]   #形成一个列表，存放每个关键词的计数

	print(corpus[:10])
	#print(ls)

if __name__ == '__main__':
	main()
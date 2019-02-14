#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: 10-K.py
@time: 2018-11-5 15:45:47
@purpose: 统计所有文本（包括10-K和CEO致股东信的词频，数字个数以及主题词的频率）
"""

import numpy as np
import pandas as pd
import re
import os 
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize    #分词函数  
from nltk import FreqDist  #nltk中的词频统计函数
# sent_tokenize是分句函数 
# WordPuncttokenizer可以将文本变成单词和标点符号

with open(file = 'topicWord.txt',mode="rt") as wordFile:
	topicWords = wordFile.readlines()   #读入主题词
	topicWords = [word.strip() for word in topicWords]   #清除每个单词结尾的\n

# 存放结果的思路，创建一个pandas 的dataframe的数据框,然后一行一行往里添加，索引即为文件名file
columns = topicWords.copy()
columns.append('digits_num')
columns.append('word_num')
res_csv = pd.DataFrame(columns = columns,dtype = int )  #创建一个空的DataFrame,用来存放结果
# pandas.DataFrame( data, index, columns, dtype, copy)



def cleanText(text):
	lemmatizer = WordNetLemmatizer()   # 创建 lemmatizer对象 
	tokens = word_tokenize(text)  #进行分词，形成一个list
	tokens = [token.lower() for token in tokens]  #变成小写
	digits = [token for token in tokens if token.replace('.','').isdigit()]  #提取所有的数字
	tokens = [word for word in tokens if word.isalpha()]   #滤除不是字母的标记
	tokens = [lemmatizer.lemmatize(word) for word in tokens]  # 词形还原，默认n可调v
	return tokens,digits


def main():
	path= 'D:/xu/桌面/doc/'  #'D:/xu/桌面/study2_text/CEO致股东信 txt版本/'
	corpus = os.listdir(path)    #返回一个列表，保存所有文件的路径
	for file in corpus:
		with open(file = path + file, mode="rt",encoding='utf-8',errors='ignore') as f:
			text = f.read()   # text 读入所有的文本 一个很长很长的字符串
			tokens,digits = cleanText(text)   #调用cleanText函数,返回两个list
			# len(tokens)+len(digits) 是字数  len(digits) 是数字的个数
			res = [tokens.count(topicWord) for topicWord in topicWords]  #创建res列表，遍历查询每个主题词的频率
			res.append(len(digits))  #存放数字个数
			res.append(len(digits) + len(tokens))  #存放这份文档的总词数
			res_csv.loc[file] = res  #将统计结果添加到DataFrame中
			print(file + ' ====> 统计完成!')
	res_csv.to_csv('result_CEO.csv',index = True)  #输出csv文件


if __name__ == '__main__':
	main()
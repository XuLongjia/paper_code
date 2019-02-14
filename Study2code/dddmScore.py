#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: dddmScore.py
@time: 2018年11月5日21:42:56
@prupose: 根据study1得出的LDA的doc-topic matrix 和 topic-word matrix ，根据文本统计出来的词频，计算论文中自定义的DDDM-score 用来测量企业的数据驱动型能力
"""

import numpy as np 
import pandas as pd 

def main():
	with open('topic_word/13+3/word_freq_nor.txt',mode="rt") as f:
		word_freq = np.array([float(pro.strip()) for pro in f.readlines()])  #去掉\n → 转float → 转 numpy.array

	with open('topic_word/13+3/topic_pro.txt',mode = 'rt') as f:
		topic_pro = np.array([float(pro.strip()) for pro in f.readlines()]) #去掉\n → 转float → 转 numpy.array

	csv = pd.read_csv('topic_word/13+3/10k_result_2017.csv',sep = ',')  #读入数据   每次运行程序注意更改
	csv.drop(['digits_num', 'word_num'],axis = 1,inplace = True) #删掉最后两列
	data = csv.as_matrix()  #所有的数据（每个300多行,290列）转成matrix的形式

	for row in data:
		ls = [j for j in row[1:161]]   #索引开头为1  结尾为总列数+1  这一行的目的是去掉数据的索引，然后形成一个list
		product = list(np.array(ls) * word_freq)   #ls是词频，word_freq 是 单词概率，二者对应元素分别相乘 
		topic = []
		while len(product) != 0:
			tmp = [product.pop(0) for i in range(10)] #每十个元素变成一个list
			topic.append(sum(tmp))  #把十个数的求和append 到topic这个list中
		res = topic_pro.dot(topic)  #向量乘法，两个向量都是29维的
		print(res)  #或者保存下来，然后输出到文件

if __name__ == '__main__':
	main()
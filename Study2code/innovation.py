#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: innovation.py
@time: 2018年12月3日10:47:49
@purpose: 计算薛老师提到的那个firm's innovation and exploration performance
"""

import numpy as np 
import pandas as pd 
import statsmodels.api as sm 

def main():
	df = pd.read_csv('innovation/innovation17.csv',sep = ',')  #读入数据
	df = df.dropna(axis=0,how='any')   #将有空值的行删掉
	'''num	gvkey	fyear	y	x1	x2	x3	x4 '''
	y = np.array(df[['y']])
	x = df[['x1','x2','x3','x4']]
	x = x.values   #dataframe 转换成 ndarray
	x = sm.add_constant(x)  #添加常数项
	reg = sm.OLS(y,x).fit()  #进行OLS回归
	#print(reg.summary())	  #所有指标
	#print(reg.bse)          #每个变量的方差
	#print(reg.params)		#每个变量的系数
	y_hat = x.dot(reg.params)   #计算y的预测值

	y = y.flatten()
	residual = y - y_hat
	df['residual'] = residual
	df.to_csv('innovation/res_17.csv', encoding = 'gbk',index = True)  #输出索引

if __name__ == '__main__':
	main()
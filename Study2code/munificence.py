#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: munificence.py
@time: 2018年11月26日11:26:25
@purpose: 计算munificence 和 dynamism ；分别使用naics_3 naics_4 sic_2 为行业分类标准
"""

import numpy as np 
import pandas as pd 
import statsmodels.api as sm 

def growth(ncs_df):  #传入ncs_df 这个dataframe，然后计算muni和dyna
	ncs_df = ncs_df.dropna(axis = 0,how ='any')   #删除有空值的
	x = np.array(ncs_df['fyear'].unique())   #自变量
	y = np.array(ncs_df.groupby(['fyear'])['sale'].sum())  #因变量
	y = np.log(y)  #对数化
	x = sm.add_constant(x)  #添加常数项，自动将一维array变成2维的array
	res = sm.OLS(y,x).fit()  #进行OLS回归
	return np.exp(res.params[1]),np.exp(res.bse[1])  #params[0] 与bse[0]是常数项的系数与方差

def main():
	df = pd.read_csv('ic/muni.csv',sep = ',')  #读入数据
	df = df[df['fyear'] >= 2013]
	df = df[df['fyear'] <= 2017]  #选择年份  2008-2012 一共五年
	del_list = ['gvkey','datadate','at','ci','lt','opeps','revt','teq','xad',
	'xrd','cik','mkvalt','prcc_f','log_sale','log_revt','naics','naics_4','sic','sic_2']
	# 行业分类标准： naics_3  naics_4  sic_2
	# 只留 fyear sale sic_2
	df = df.drop(del_list, axis = 1)  #删除这些字段
	res = pd.DataFrame(columns = ["munificence", "dynamics"])  #创建空dataframe存放结果
	for ncs_3 in df['naics_3'].unique():  	#以naics_3的所有不同值进行循环
		ncs_df = df[df['naics_3'] == ncs_3]   #选择一个行业，创建新的dataframe 叫做ncs_df 进行计算
		# 创建一个函数growth，传入ncs_df 这个dataframe，返回muni和dyna
		muni,dyna = growth(ncs_df)
		res.loc[ncs_3] = [muni,dyna]  #插入值
	print(res)
	#res.to_csv('ic/naics_3_res.csv', encoding = 'gbk',index = True)  #输出索引


if __name__ == '__main__':
	main()
   
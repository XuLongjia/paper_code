#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: naics4_hhi.py
@time: 2018年11月13日15:49:17
@purpose: 使用naics的前四位计算赫芬达尔指数，之前使用的是前三位
"""

import numpy as np 
import pandas as pd 
df = pd.read_csv("apa.csv",sep=",")  #读入数据
df = df[df['fyear'] == 2012]
df = df.dropna(axis=0,how='any')   #将有空值的行删掉
#columns如下： gvkey	fyear	revt	sale	naics	naics_4
# My_Frame['sort_id'] = My_Frame['salary'].groupby(My_Frame['dep_id']).rank()   参考这个格式
df['sort'] = df['sale'].groupby(df['naics_4']).rank(ascending=False)   #按照nacis_4分组，然后按照sale降序排序
df = df[df['sort'] <= 50]      #将销售额排名在50以后的公司删掉
tmp = df.groupby(['naics_4'])['sale'].sum()    #按naics_4进行分组,然后将sale求和，生成一个Series
tmp = tmp.to_frame()  #将Series 转换成了 DataFrame
tmp['naics_4'] = tmp.index   #将tmp的index变成新的一列
tmp =tmp.reset_index(drop= True)  #将原来的索引删除
tmp = tmp.rename(columns={'sale':'sum_sale'})   #将tmp的列进行重命名
res = pd.merge(df, tmp, on=['naics_4'], how='left')   #相当于SQL中的leftjoin
res.eval('share=sale/sum_sale',inplace = True)  #生成新列：市场份额 share
res.eval('share_sqrt = share * share',inplace = True)  #生成新列：市场份额的平方
output = res.groupby(['naics_4'])['share_sqrt'].sum()  #输出结果
print(output)
#output.to_csv('2017_res.csv', encoding = 'gbk',index = True)  #输出结果
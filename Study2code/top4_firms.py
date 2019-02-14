#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: naics4_hhi.py
@time: 2018年11月13日16:30:19
@purpose: 计算每个行业（naics_4)的前四个公司市场份额，值越大代表竞争越不激烈，复杂度不高，活力小
"""

#columns如下： gvkey	fyear	revt	sale	naics	naics_4
#ind.csv columns gvkey,datadate,fyear,revt,sale,naics,naics_4
import numpy as np 
import pandas as pd 
df = pd.read_csv("apa.csv",sep = ",")  #读入数据
df = df[df['fyear'] == 2012]  #2012-2017依次计算 
df = df.dropna(axis=0,how='any')   #将有空值的行删掉
df['sort'] = df['sale'].groupby(df['naics_4']).rank(ascending=False)   #按照nacis_4分组，然后按照sale降序排序

tmp1 = df.groupby(['naics_4'])['sale'].sum()    #按naics_4进行分组,然后将sale求和，生成一个Series
tmp1 = tmp1.to_frame()  #将Series 转换成了 DataFrame
tmp1['naics_4'] = tmp1.index   #将tmp的index变成新的一列
tmp1 =tmp1.reset_index(drop= True)  #将原来的索引删除
tmp1 = tmp1.rename(columns={'sale':'sum_sale'})   #将tmp的列进行重命名

df = df[df['sort'] <= 4]      #每个行业只留下销售额top4的公司，注意，也可能少于4个
tmp2 = df.groupby(['naics_4'])['sale'].sum()    #下面四行操作如上
tmp2 = tmp2.to_frame()  #
tmp2['naics_4'] = tmp2.index   #
tmp2 =tmp2.reset_index(drop= True)  #
tmp2 = tmp2.rename(columns={'sale':'top4_sale'})   #将tmp的列进行重命名

res = pd.merge(tmp1, tmp2, on=['naics_4'], how='left')   #相当于SQL中的leftjoin
res.eval('complexity = top4_sale/sum_sale',inplace = True)  #生成新列：市场份额 share
print(res)
#res.to_csv('2017_res.csv', encoding = 'gbk',index = True)  #输出结果

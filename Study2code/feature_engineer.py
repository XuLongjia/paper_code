#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: featrue_engineer.py
@time: 2018年11月15日20:22:46
@prupose: 根据最终的panel data的dddm_score 和 ceo_dddm_score 进行特征工程的处理
"""

import numpy as np 
import pandas as pd 
df = pd.read_csv('panel_data.csv', sep = ',')  #读入数据
#df = df.dropna(axis=0,how='any')   #将有空值的行删掉
df.to_csv('tmp_csv.csv', encoding = 'gbk',index = True)  #输出结果

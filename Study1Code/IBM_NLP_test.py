#!/usr/bin/python
# -*- coding: utf-8 -*- 

"""
@author: XuLongjia
@software: Sublime
@file: IBM_NLP_test.py
@time: 2018年4月
@prupose: 主题和概念提取
"""

import json
import glob
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features  
from watson_developer_cloud.natural_language_understanding_v1 import CategoriesOptions
from watson_developer_cloud.natural_language_understanding_v1 import ConceptsOptions
from watson_developer_cloud.natural_language_understanding_v1 import EmotionOptions
from watson_developer_cloud.natural_language_understanding_v1 import EntitiesOptions
from watson_developer_cloud.natural_language_understanding_v1 import KeywordsOptions
from watson_developer_cloud.natural_language_understanding_v1 import MetadataOptions
from watson_developer_cloud.natural_language_understanding_v1 import RelationsOptions
from watson_developer_cloud.natural_language_understanding_v1 import SemanticRolesOptions
from watson_developer_cloud.natural_language_understanding_v1 import SentimentOptions

#先把所有需要处理的pdf文档用acrobat X1 pro转换成txt格式
b=glob.glob("D:/【xu】/桌面/11/*.txt")
#读取该目录下所有的txt文档，保存在b(list)中
print("该目录下有{}个文档".format(len(b)))
print('分别为:')
for i in b:
    print(i)
print('\n')
num=1
for i in b:
    f=open(i,'rt',errors='ignore')
    doc_as_str=f.read()
    f.close()
    print("开始分析第{}篇文档.............".format(num))
    
    #输入凭证
    natural_language_understanding = NaturalLanguageUnderstandingV1(
    username='c7f87944-d2a3-47c1-96ee-e5e90b8e8a5c',
    password='t6TMuI8taTsU',
    version='2018-03-16')  #The current version is 2018-03-16
    #输出特征
    response = natural_language_understanding.analyze(
    text=doc_as_str,
    features=Features(keywords=KeywordsOptions(sentiment=False,emotion=False,limit=50),
                      concepts=ConceptsOptions(limit=10)
                      )
                                                      )
    f=open('D:\\【xu】\\桌面\\output.txt','a')
    f.write('\n\n')
    f.write('下面是第{}篇文档的输出:'.format(num))
    f.write('\n\n')
    json.dump(response,fp=f,indent=2)           #将分析结果写入txt文档
    f.close()
    print("第{}篇文档分析完成！".format(num))
    print('\n')
    num=num+1
    #print(json.dumps(response, indent=2))
print("=======================所有文档分析完成！=====================")    


#Features中包括如下选项：
#归类：categories=CategoriesOptions()
#概念:concepts=ConceptsOptions(limit=3)
    #limit:默认8个，最多50个
#情绪：emotion=EmotionOptions(targets=['apples','oranges'],document=True)
    #输出target中的子字符串的情绪
    #ducument可以设置成False，表示不输出整篇文档的情绪
#实体:entities=EntitiesOptions(emotion=False,mentions=False,sentiment=False,limit=20)
    #enmotion可设置成Ture,表示输出识别出来的实体的情绪,sentiment也是同理
    #mentions设置成True表示返回实体的location
    #limit:默认50，最大250
    #可自定义模型
#关键词：keywords=KeywordsOptions(sentiment=True,emotion=False,limit=2)
    #limit:默认50，最大250
#元数据：metadata=MetadataOptions()
    #输出author name, title, RSS/ATOM feeds, prominent page image, and publication date
    #HTML or webpage input only
#关系识别：relations=RelationsOptions()
    #识别两个实体之间的关系
    #可定义模型
#语义角色：semantic_roles=SemanticRolesOptions(entities=False,keywords=False,limit=20)
    #识别句子的(subject)、谓(action)、宾(object form)
    #entites设置成True可识别subject和object的实体信息
    #keywords设置成Ture可输出subject和object的关键词信息
    #limit：默认50
#情感倾向：sentiment=SentimentOptions(targets=['stocks'],document=Ture)
    #document和targets选项功能同上

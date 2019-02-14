#!/usr/bin/env python
# encoding: utf-8

"""
@author: XuLongjia
@software: Sublime
@file: prase_pdf.py
@time: 2017/3/3 0003 11:16
"""

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
#获取文档对象
fp=open('test_pdf.pdf','rb')
#创建一个与文档关联的解释器
parser=PDFParser(fp)
#PDF文档对象
doc=PDFDocument()
#连接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)
#初始化文档
doc.initialize('')  #接受密码，没有的话用一个空字符串表示
#创建PDF资源管理器
resource=PDFResourceManager()
#参数分析器
laparam=LAParams()
#创建一个聚合器，把PDF资源管理器和参数分析器连接到一起
device=PDFPageAggregator(resource,laparams=laparam)
#创建PDF页面解释器，接收资源管理器和聚合器
interpreter=PDFPageInterpreter(resource,device)
ls=[] #创建一个字符串接受内容
#使用文档对象得到页面的集合
for page in doc.get_pages():
    interpreter.process_page(page) #使用页面解释器来读取
    layout=device.get_result() #使用聚合器来获得内容

    for out in layout:
        if hasattr(out,'get_text'):
            ls.append(out.get_text())
            print(out.get_text())
text_1=''.join(ls)
text_num=len(text_1.split())
print("该文档的总字数为：{}".format(text_num))
            

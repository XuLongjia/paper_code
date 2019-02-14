#!/usr/bin/python
#-*- coding: utf-8 -*-

#1、具体需要的模块导入
import os
import sys
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfparser import PDFPage
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter,PDFTextExtractionNotAllowed
from pdfminer.layout import *
#from pdfminer.pdfparser.PDFSyntaxError import *
import re

#2、批量读取文档，并创建批量的写文件
#（看需求，这里要求每一个pdf文件解析成文本后单独存放一个文件）
#这里使用了os模块读取目录的函数listdir()，其中i是目录下的文件名称。 
#s_dir='E:\\program\\pdf\\file'
s_dir='D:\\【xu】\\桌面\\pdf_to_txt\\pdf'

for i in os.listdir(s_dir):
    if os.path.isfile(os.path.join(s_dir,i)):
        print(i)
        wfile=i.split('.')[0]
        fp = open(os.path.join(s_dir,i), 'rb')
        #w_file=open('D:\\【xu】\\桌面\\pdf_to_txt\\pdf\\result\\%s.txt'%wfile,'a+')
        w_file=open('D:\\【xu】\\桌面\\pdf_to_txt\\pdf\\%s.txt'%wfile,'a+')

#3、创建文件解析器
#具体的代码含义，都进行了注释
#创建一个PDF文档解析器对象
        try:
            parser = PDFParser(fp)
#创建一个PDF文档对象存储文档结构
#提供密码初始化，没有就不用传该参数
#document = PDFDocument(parser, password)
            document = PDFDocument(parser)
#检查文件是否允许文本提取
            if not document.is_extractable:
                raise PDFTextExtractionNotAllowed
#创建一个PDF资源管理器对象来存储共享资源
#caching = False不缓存
            rsrcmgr = PDFResourceManager(caching = False)
# 创建一个PDF设备对象
            laparams = LAParams()
# 创建一个PDF页面聚合对象
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#创建一个PDF解析器对象
            interpreter = PDFPageInterpreter(rsrcmgr, device)
#处理文档当中的每个页面

# doc.get_pages() 获取page列表
#for i, page in enumerate(document.get_pages()):
#PDFPage.create_pages(document) 获取page列表的另一种方式
            replace=re.compile(r'\s+');
# 循环遍历列表，每次处理一个page的内容
            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
    # 接受该页面的LTPage对象
                layout=device.get_result()
    # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
    # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
                for x in layout:
        #如果x是水平文本对象的话
                    if(isinstance(x,LTTextBoxHorizontal)):
                        text=re.sub(replace,'',x.get_text())
                        if len(text)!=0:
                            w_file.write(text.encode('utf-8'))
                        #print text
                print ("success")
        except:
            print ("skip null file!")

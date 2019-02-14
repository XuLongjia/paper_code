#below is the complete R code#
library(readr)
library(stringr)
#读入整个语料库的大list
corpus_split <- str_split(read_lines(file.choose()),",") 

#删除停用词，降低维度
library(jiebaRD)
library(jiebaR)
library(pbapply)
#读入停用词向量
stop_w<-read_lines(file.choose())
#删除停用词，更新corpus_split
corpus_split <- pbsapply(corpus_split,function(corpus){
  filter_segment(corpus,stop_w)
})

#词性还原
library(koRpus.lang.en,koRpus)
library(data.table)
library(textstem)
corpus_split<-pbsapply(corpus_split,lemmatize_words)

#统计语料库的单词，table格式，names&as.numeric
vocab<-table(unlist(corpus_split)) 
doc_length<-unlist(lapply(corpus_split,length))

#创建tdm矩阵的函数
creat_tdm<-function(corpus_split){
  word_vec<-names(table(unlist(corpus_split)))    #提取语料库中所有单词组成的向量
  count_vec<-as.numeric(table(unlist(corpus_split)))    #提取语料库中所有单词计数的向量
  tdm<-matrix(0,nrow=length(word_vec),ncol=length(corpus_split),dimnames=list(word_vec,paste("doc_",1:length(corpus_split),sep="")))
  doc_id<-1   #定义文档索引
  for (i in corpus_split){
    i_names<-names(table(i))
    i_num<-as.numeric(table(i))
    index<-1    #i_names和i_num这两个向量的索引
    while(index<=length(i_names)){
      tdm[i_names[index],doc_id]<-i_num[index]
      index<-index+1
    }    #这个while循环就是把第doc_id个文档的词频写入到tdm矩阵中
    index<-1    #把索引重新变成1
    doc_id<-doc_id+1   #更新文档索引
  }
  return(tdm)
}
#创建tdm矩阵
tdm<-creat_tdm(corpus_split)
rm(corpus_split,creat_tdm,stop_w)

#创建了一个slam版的dtm矩阵，用于后续LDA处理
library(slam)
dtm<-as.simple_triplet_matrix(t(tdm))  
rm(tdm)
#接下来选择最优主题个数

library(topicmodels)

#FindTopicsNumber_plot(opt_topic)
#opt_topic<-rbind(delta_0.5,opt_topic)
#write.csv(result_617,"output_617.csv")

#LDA
LDA_Gibbs_29 = LDA(dtm,k = 29, method = "Gibbs",control = list(seed = 66,delta=0.1))  

#输出 主题单词矩阵
write.csv(t(exp(LDA_Gibbs_29@beta)),"topic_word.csv")
#输出单词
write.csv(LDA_Gibbs_29@terms,"word.csv")
#然后把输出的第二个csv文件粘贴到第一个csv文件的第一列，单词顺序是不变的
#文件输出的地址在“文档”里

#每个Topic前10个Term
#terms(LDA_Gibbs, 10)
#最可能的主题文档
#Topic <- topics(LDA_Gibbs, 1)

library(LDAvis)
#创建一个json对象，用来接下来的画图
json<-createJSON(phi = exp(LDA_Gibbs_33@beta), theta = LDA_Gibbs_33@gamma, 
                 doc.length = doc_length, 
                  vocab = names(vocab), term.frequency = as.numeric(vocab),
                 R=30,lambda.step = 0.01,mds.method = jsPCA,
                 plot.opts = list(xlab="PC1",ylab="PC2"))
#上面这个需要更改 phi 这个参数、R、vocab、term.frequency

#画图
serVis(json,open.browser = TRUE)      

rm(corpus_split,dtm,doc_length,stop_w,creat_tdm,vocab)
save.image("k=33.RData")
rm(list=ls())
load("k=30.RData")
rm(LDA_Gibbs_30,json)

#serVis(article.josn,out.dir = "shuchushishi",open.browser = FALSE)
#jsPCA(exp(LDA_Gibbs@beta))
#library(parallel)
#cl <- makeCluster(2)
#json<-createJSON(phi = exp(LDA_Gibbs@beta), theta = LDA_Gibbs@gamma, doc.length = doc_length, vocab = names(vocab), term.frequency = as.numeric(vocab),cluster = cl)
#serVis(json)   


#接下来进行聚类分析
#data<-as.data.frame(t_w)  #把文档-词汇矩阵转换成dataframe形式的
#data.scale<-scale(x)
#d<-dist(data.scale,method="euclidean")
#fit<-hclust(d,method="ward.D2")
#plot(fit)


#data<-as.data.frame(phi)
#cl<-kmeans(scale(data),5)



#LDA运行完后,输出仅有短语的矩阵
TWmatrix<-t(exp(LDA_Gibbs@beta))
rownames(TWmatrix)<-LDA_Gibbs@terms
index<-unlist(lapply(strsplit(LDA_Gibbs@terms," "),length))
TWmatrix_v2<-TWmatrix[index>1,]
write.csv(TWmatrix_v2,"only_phrase.csv")
# https://blog.csdn.net/qq_34494334/article/details/79360835
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() # 创建 lemmatizer对象 
lemmatizer.lemmatize('dogs')


# https://www.jb51.net/article/128325.htm
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem('fishing')  #输出 ‘fish'



https://www.yiibai.com/ai_with_python/ai_with_python_nltk_package.html
nltk 易百教程  里面提到了很多词形还原的算法



https://yq.aliyun.com/articles/225721
秒懂！看机器学习如何净化处理文本
过滤停止词
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)


#测试用的单词列表
words = ['One', 'morning,', 'when', 'Gregor', 'Samsa', 'woke', 'from', 'troubled', 'dreams,', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed', 'into', 'a', 'horrible', 'vermin.', 'He', 'lay', 'on', 'his', 'armour-like', 'back,', 'and', 'if', 'he', 'lifted', 'his', 'head', 'a', 'little', 'he', 'could', 'see', 'his', 'brown', 'belly,', 'slightly', 'domed', 'and', 'divided', 'by', 'arches', 'into', 'stiff', 'sections.', 'The', 'bedding', 'was', 'hardly', 'able', 'to', 'cover', 'it', 'and', 'seemed', 'ready', 'to', 'slide', 'off', 'any', 'moment.', 'His', 'many', 'legs,', 'pitifully', 'thin', 'compared', 'with', 'the', 'size', 'of', 'the', 'rest', 'of', 'him,', 'waved', 'about', 'helplessly', 'as', 'he', 'looked.', '"What\'s', 'happened', 'to', 'me?"', 'he', 'thought.', 'It', "wasn't", 'a', 'dream.', 'His', 'room,', 'a', 'proper', 'human']


freq = FreqDist(tokens)    #freq是一个字典 dict(key:value)
for key,val in freq.items():
	print(str(key) + ':' + str(val))

Python NLTK 自然语言处理入门与例程
https://cloud.tencent.com/developer/article/1043114


nltk学习 小杰的个人博客
http://www.coderjie.com/blog/8658d836c36111e6841d00163e0c0e36
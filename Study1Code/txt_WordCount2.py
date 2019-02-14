import glob
import re
b=glob.glob("C:/Users/xu/Desktop/corpus/*.txt")  #获得所有的txt文件
print("该目录下有如下txt文件:\n")
for j in b:
    print(j)
    
print('\n')

for i in b:
    f = open(i,"rt",errors='ignore')             #依次读取每个txt文件
    str_ar=f.read()                               #写入一个字符串中
    f.close()

    i_1=i.replace("C:/Users/xu/Desktop/corpus\\","")
    i_2=i_1.replace(".txt",'')                #提取公司名称,用字符串i_2表示
    
    word_num_ar=len(str_ar.split())

    print("{}年报的总字数为：{}".format(i_2,word_num_ar))
    
    numeric=re.findall(r"\d+\.?\d*",str_ar)     #提取年报中的所有数字
    print("{}出现的数字个数：{}".format(i_2,len(numeric)))
    
    rate=len(numeric)/word_num_ar              #计算数字占比
    print("数字占比为：{}".format(rate))
    print('\n')
    

    
    
    
    

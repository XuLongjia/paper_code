import glob
d=glob.glob("D:\\xu\\桌面\\84\\*.txt")
for i in d:
    f=open(i,'rt',errors='ignore')
    doc_as_str=f.read()
    f.close()
    doc_as_str=doc_as_str.replace('\n','')
    f=open('D:\\xu\\桌面\\ibm.txt','a')
    f.write(doc_as_str+'\n')
    f.close()
    

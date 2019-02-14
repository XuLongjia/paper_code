#读取某一目录下面所有的txt文件，每一个txt文件名都是列表a中的一个元素


def dell(str1):
    str1=str1.replace("C:/users/xu/desktop\\","")
    str1=str1.replace(".txt",'')
    return str1
import glob
b=glob.glob("C:/users/xu/desktop/*.txt")
a=list(map(dell,b))
print(a)


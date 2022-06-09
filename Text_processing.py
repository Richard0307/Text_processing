from array import array
from posixpath import split
import numpy as np
import pandas as pd
import jieba 
import jieba.analyse
import encodings
import nltk 
import binascii
from file_read_backwards import FileReadBackwards

a = "哎，鹅，听说你超级喜欢小游戏的！你是吗？"
b = jieba.lcut(a)
# 去停用词函数
stopword = []
with open('C:\\Users\\Richard\\Desktop\\COM3110 代码\\test\\stopword.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        l = line.strip()
        if l == '\\n': # 换行符
            l = '\n'
        if l == '\\u3000':# 制表符
            l = '\u3000'
        
        stopword.append(l)

x = np.array(b)
y = np.array(stopword)
z = x[~np.in1d(x,y)]
k = [i for i in x if len(i)>1]

# 抽取关键词 打标签，关键词提取

# 词频统计
x = jieba.lcut(a)
y = pd.DataFrame(x).groupby(0).size().sort_values(ascending=False)[:5]
# print(y)

### 案例：分析Python互联网招聘信息中的需求关键字
with open('C:\\Users\\Richard\\Desktop\\COM3110 代码\\test\\work.txt','r',encoding='utf-8') as f:
    txt = f.read()

x = jieba.lcut(txt)
stopword = []
with open('C:\\Users\\Richard\\Desktop\\COM3110 代码\\stopword.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        l = line.strip()
        if l == '\\n': # 换行符
            l = '\n'
        if l == '\\u3000': # 制表符
            l = '\u3000'
        stopword.append(l)

y = np.array(x)
z = np.array(stopword)
m = y[~np.in1d(y,z)]
k = [i for i in m if len(i)>1]
# print(k)
filepath = ("C:\\Users\\Richard\\Desktop\\COM3110 代码\\test\\work.txt")

with open (filepath,'r',encoding='utf-8') as f:
    lines_in_file = f.read()

    nltk_tokens = nltk.word_tokenize(lines_in_file)

# print(nltk_tokens)
# print("Numbers of words:",len(nltk_tokens))

text = b"Simply Easy Learning"

# Coverting binary to ascii
data_b2a = binascii.b2a_uu(text)
# print("**Binary to Ascii ** \n")
# print(data_b2a)
# with open (filepath,'r',encoding='utf-8') as BigFile:
#     data = BigFile.readlines()
    
#     for i in range (len(data)):
        # print("Line NO.",i)
        # print(data[i])

with FileReadBackwards (filepath,encoding='utf-8') as BigFile:
    for line in BigFile:
        print(line)
from array import array
import numpy as np
import pandas as pd
import jieba 
import jieba.analyse
import encodings 

a = "哎，鹅，听说你超级喜欢小游戏的！你是吗？"
b = jieba.lcut(a)
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
k = [i for i in z if len(i)>1]
print(k)

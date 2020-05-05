import sys
import os
import xlwt
import numpy as np
import pandas as pd
from jiwer import wer

def eachFile(filepath):
    pathDir = os.listdir(filepath)
    return  pathDir

def readfile(name):
    fopen = open(name,'r')
    cou = 0
    for lines in fopen.readlines():
        cou = cou + 1
        lines = lines.replace("\n","").split(",")
        lines_1 = list(lines)
    fopen.close()
    return cou

path = os.path.dirname(os.path.abspath('..'))
print(path)
origin_txt_path = path + '/dataset/text/textwithoutwakewords.txt'
origin_txt = pd.read_csv(origin_txt_path,header=None,names=['content'])
print(origin_txt)

real_text_path = path + '/test_result/baidu/16k/without_wake_words'
pathDir = eachFile(real_text_path)

ch = []
le = []
le.append(0)

for allDir in pathDir:
    child = real_text_path + '/' + allDir
    ch.append(child)
    readfile(child)
    le.append(readfile(child))


#用le记录一个txt有多少行，方便下一个文件读取的时候不会在写入时覆盖
for i in range(1, len(le)):
    le[i] = le[i] + le[i-1]
    #print(le)

file = xlwt.Workbook(encoding='utf-8')
sheet = file.add_sheet('asr')

for i in range(len(ch)):
    k = le[i] + 1
    print(k)
    with open(ch[i]) as f1:
        print(ch[i])
        for lines in f1.readlines():
            lines = lines.replace("\n", "").split(",")
            lines_1 =list(lines)
            i = 0
            for line in lines_1:
                sheet.write(k,i,line)
                i = i +1
            k = k + 1
        f1.close()
file.save(real_text_path + '/result.xls')






'''
f = open(origin_txt_path,"r")
origin_txt = f.readlines()
print(origin_txt)
'''

'''
error = wer(ground_truth, hypothesis)
print(error)
'''

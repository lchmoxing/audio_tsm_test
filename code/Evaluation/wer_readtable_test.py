import sys
import os
import xlwt
import numpy as np
import pandas as pd
from jiwer import wer

# path = os.path.dirname(os.path.abspath('..')) 

path = os.getcwd()
for k in range(0,10):
    baidu_text_path = path + '/baidu_with_wake_words' + str(k) +'.csv'
    all_txt = pd.read_csv(baidu_text_path)
    origin_text = all_txt['origin']
    result_text = all_txt.drop(['origin'],axis=1)
    wer_text = result_text

    for index, row in result_text.iteritems():
        for i in range(0, len(row)):
            wer_text.loc[i][index] = wer(origin_text[i],result_text.loc[i,index])
    print(wer_text)
    wer_text.to_csv("./wer_with_wake_words" + str(k) + ".csv", index=False)

 


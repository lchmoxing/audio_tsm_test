import os
import cmudict
import pandas as pd
import nltk

nltk.download('punkt')
prondict = cmudict.dict()
path = os.path.dirname(os.path.abspath('.'))

text_path = path + '/ASR/baidu/baidu_with_wake_words0.csv'

#F:\github\audio_tsm_test\code\ASR\baidu

def split_tran(txt):
    txt_revise = txt.replace(",", '').replace(".", '')
    split_result = nltk.word_tokenize(txt_revise)
    for i in range(len(split_result)):
        split_result[i] = prondict[split_result[i].lower()]
    return split_result



all_txt = pd.read_table(text_path)
#all_txt.columns = ['origin']
print(all_txt)
'''
tran = []
for index, row in all_txt.iterrows():
    tran.append(split_tran(row['origin']))
all_txt['tran'] = tran
all_txt.to_excel("split_tran.xlsx")
'''

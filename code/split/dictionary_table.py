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

all_txt = pd.read_csv(text_path)
name = list(all_txt.columns.values)
df = pd.DataFrame(columns = name)

tran_tmp = []
for index, row in all_txt.iteritems():
    for i in range(len(row)):
        if row[i] != 'error':
            tran_tmp.append(split_tran(row[i]))
        else:
            tran_tmp.append('')
    df[index] = tran_tmp
    tran_tmp = []
df.to_excel("tran_0.xlsx")

'''
for index, row in all_txt.iteritems():
    if row[count] != "error":
        tran_tmp.append(split_tran(row['origin']))
'''
'''
tran = []
for index, row in all_txt.iterrows():
    tran.append(split_tran(row['origin']))
all_txt['tran'] = tran
all_txt.to_excel("split_tran.xlsx")
'''

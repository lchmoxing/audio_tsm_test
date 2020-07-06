import os
import cmudict
import pandas as pd
import nltk

nltk.download('punkt')
prondict = cmudict.dict()
path = os.path.dirname(os.path.abspath('..'))
text_path = path + '/dataset/speech_origin/text/textwithwakewords.txt'

def split_tran(txt):
    txt_revise = txt.replace(",", '').replace(".", '')
    split_result = nltk.word_tokenize(txt_revise)
    for i in range(len(split_result)):
        split_result[i] = prondict[split_result[i].lower()]
    return split_result

all_txt = pd.read_table(text_path, header=None)
all_txt.columns = ['origin']

tran = []
for index, row in all_txt.iterrows():
    tran.append(split_tran(row['origin']))
all_txt['tran'] = tran
all_txt.to_excel("split_tran.xlsx")

'''
test_txt = 'Okay Google, navigate to my home'
test_txt_revise = test_txt.replace(",",'')
split_result =  nltk.word_tokenize(test_txt_revise)
print(split_result)
for i in range(len(split_result)):
    split_result[i] =  prondict[split_result[i].lower()]
print(split_result)
'''

print(prondict['i'])
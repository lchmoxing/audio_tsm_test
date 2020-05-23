import os
import cmudict
import pandas as pd
import nltk

nltk.download('punkt')

prondict = cmudict.dict()
path = os.path.dirname(os.path.abspath('..'))
text_path = path + '/dataset/speech_origin/text/textwithwakewords.txt'

all_txt = pd.read_table(text_path,header=None)
#print(all_txt)

#tokenize = lambda x: nltk.word_tokenize[x]
#all_txt['split'] = all_txt(tokenize)
#print(all_txt)


#result = prondict['speech']
test_txt = 'Okay Google, navigate to my home'
test_txt_revise = test_txt.replace(",",'')
split_result =  nltk.word_tokenize(test_txt_revise)
print(split_result)
for i in range(len(split_result)):
    split_result[i] =  prondict[split_result[i]]

print(split_result)
#result = nltk.word_tokenize('Okay Google, navigate to my home.')
#print(type(result))
#print(result)
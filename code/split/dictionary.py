import os
import nltk
import cmudict
import ssl
import pandas as pd
nltk.download('punkt')

prondict = cmudict.dict()
path = os.path.dirname(os.path.abspath('..'))
text_path = path + '/dataset/text/textwithwakewords.txt'

all_txt = pd.read_table(text_path,header=None)
#print(all_txt)

#tokenize = lambda x: nltk.word_tokenize[x]
#all_txt['split'] = all_txt(tokenize)
#print(all_txt)


#result = prondict['speech']
teset_txt =
result = nltk.word_tokenize('Okay Google, navigate to my home.')
print(type(result))
print(result)
import os
import sys
import cmudict
import pandas as pd


path = os.path.dirname(os.path.abspath('..'))
text_path = path + '/dataset/text/textwithwakewords.txt'
print(text_path)
all_txt = pd.read_table(text_path,header=None)
print(all_txt)


prondict = cmudict.dict()
result = prondict['speech']
print(result)
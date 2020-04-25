import sys
import os
import numpy as np
from jiwer import wer

path = os.path.dirname(os.path.abspath('..'))
origin_txt_path = path + '/dataset/text/textwithoutwakewords.txt'

f = open(origin_txt_path,"r")
origin_txt = f.readlines()
print(origin_txt)



error = wer(ground_truth, hypothesis)

print(error)
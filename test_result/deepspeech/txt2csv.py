import os
import numpy as np
import pandas as pd
import random
import sys

path = sys.path[0]
print(sys.path[0])
# print(os.path.abspath('txt2csv.py'))
os.chdir(sys.path[0])
txt_path = os.getcwd() + r'\test_results61' 
# print(txt_path)
txt_list = os.listdir(txt_path)
txt_list.sort(key=lambda x: str(x[:-4])) 
# print(txt_list)
csv_file = []
# print(txt_path+'\\' +txt_list[0])
results = pd.DataFrame({"sentence_num":range(1,11)})
for txt in txt_list:
    (filename,extension) = os.path.splitext(txt)
    f = open(txt_path+'\\' +txt)
    csv_file = f.read().splitlines()
    # print(csv_file)#.strip('\n').split(',')
    filename = pd.DataFrame({filename:csv_file})
    # print(filename)
    results = pd.concat([results,filename], axis =1 )
results.to_csv(path + r"\results.csv", index=False)
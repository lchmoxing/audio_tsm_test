import os
import numpy as np
import pandas as pd
import random
import sys

# path = sys.path[0]
# print(sys.path[0])
# # print(os.path.abspath('txt2csv.py'))
# os.chdir(sys.path[0])
# txt_path = os.getcwd() + r'\628juzi' 
# print(txt_path)
txt_path = r"C:\Users\qinhong\Documents\GitHub\audio_tsm_final\audio92\9.8test_text"
txt_list = os.listdir(txt_path)
print(txt_list)
txt_list.sort(key=lambda x: int(x[:-4])) 
csv_file = []
# print(txt_path+'\\' +txt_list[0])
results = pd.DataFrame({"sentence_num":range(1,2)})
# results = pd.DataFrame({"sentence_num":range(1,2)})
for txt in txt_list:
    (filename,extension) = os.path.splitext(txt)
    print(filename[0:-4])
    f = open(txt_path+'/' +txt)
    csv_file = f.read().splitlines()
    filename = pd.DataFrame({filename:csv_file})
    results = pd.concat([results,filename], axis =1 )
results.to_csv(txt_path + "/result.csv", index=False)
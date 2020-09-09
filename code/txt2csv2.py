### txt在文件夹中的文件夹中
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
# txt_path = "D:/projects/voice/DS_10283_2651/VCTK-Corpus/VCTK-Corpus/txt"
txt_path = "C:/Users/qinhong/Desktop/yuyin_final/50g数据集/测试结果（含2.0）"

txt_folders = os.listdir(txt_path)
# print(txt_folders)
for txt_folder in txt_folders: 
    # print(txt_folder)
    if(os.path.isdir(os.path.join(txt_path,txt_folder))):
        txt_list = os.listdir(os.path.join(txt_path,txt_folder))
        txt_list.sort(key=lambda x: str(x[:-4])) 
        csv_file = []
        # print(txt_path+'\\' +txt_list[0])
        results = pd.DataFrame({"sentence_num":range(1,2)})
        # results = pd.DataFrame({"sentence_num":range(1,2)})
        for txt in txt_list:
            (filename,extension) = os.path.splitext(txt)
            f = open(os.path.join(txt_path,txt_folder)+'/' +txt)
            csv_file = f.read().splitlines()
            filename = pd.DataFrame({filename:csv_file})
            results = pd.concat([results,filename], axis =1 )
        results.to_csv("C:/Users/qinhong/Desktop/yuyin_final/50g数据集/测试结果（含2.0）/" + txt_folder+".csv", index=False)
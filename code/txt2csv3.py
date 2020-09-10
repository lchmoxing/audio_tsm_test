### txt在文件夹中的文件夹中的文件夹
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
txt_path = "C:/Users/qinhong/Desktop/yuyin_final/10g数据集/测试结果"

txt_folders = os.listdir(txt_path)#p223
# print(txt_folders)
for txt_folder in txt_folders:
    print(txt_folder)
    txt_subfolder_path = os.path.join(txt_path,txt_folder)
    txt_subfolders = os.listdir(txt_subfolder_path)#origin ffmpeg
    # print(txt_subfolders)
    origin_csv_file = []
    ola_csv_file = []
    wsola_csv_file = []
    phasevotor_csv_file = []
    ffmpeg_csv_file = []
    sentence_num_csv_file = []
    for txt_subfolder in txt_subfolders:
        results = pd.DataFrame()
        print(txt_subfolder)
        if(os.path.isdir(os.path.join(txt_subfolder_path,txt_subfolder))):
            txt_list = os.listdir(os.path.join(txt_subfolder_path,txt_subfolder))#audio
            txt_list.sort(key=lambda x: str(x[:-4])) 
            text_file = ''
            # csv_file = []
            # print(txt_path+'\\' +txt_list[0])
            # results = pd.DataFrame({"sentence_num":range(1,2)})
            for txt in txt_list:
                (filename,extension) = os.path.splitext(txt)
                # print(os.path.join(txt_subfolder_path,txt_subfolder)+'/' +txt)
                f = open(os.path.join(txt_subfolder_path,txt_subfolder)+'/' +txt)
                sentence_num_csv_file.append(txt[5:-4])
                text_file = f.read()
                # print(text_file)
                if str(txt_subfolder) == 'origin':
                    origin_csv_file.append(text_file)
                if str(txt_subfolder) == 'ola':
                    ola_csv_file.append(text_file)
                if str(txt_subfolder) == 'wsola':
                    wsola_csv_file.append(text_file)
                if str(txt_subfolder) == 'phasevoctor':
                    phasevotor_csv_file.append(text_file)
                if str(txt_subfolder) == 'ffmpeg':
                    ffmpeg_csv_file.append(text_file)
                # print(csv_file)
                # filename = pd.DataFrame({filename:csv_file})
    results['sentence num'] = pd.Series(sentence_num_csv_file)
    results['ola'] = pd.Series(ola_csv_file) 
    results['wsola'] = pd.Series(wsola_csv_file) 
    results['ffmpeg'] = pd.Series(ffmpeg_csv_file) 
    results['origin'] = pd.Series(origin_csv_file) 
    results['phasevoctor'] = pd.Series(phasevotor_csv_file) 
    results.to_csv("C:/Users/qinhong/Desktop/yuyin_final/10g数据集/测试结果/" + txt_folder+".csv", index=False,mode = 'w')
    print("write successfully")
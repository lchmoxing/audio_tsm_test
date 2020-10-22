
# coding: utf-8

import os
import pandas as pd
import numpy as np
import cmudict
import nltk

nltk.download('punkt')
prondict = cmudict.dict()
dir_path = os.path.abspath('.')
exl_path = dir_path + r'/sum_100.csv'
print(exl_path)
df = pd.read_csv(exl_path,engine='python',keep_default_na=False)

str_list= []
pro_origin_list =[]
pro_result_list = []
same_list = []
char_rep_rate_list =[]
char_full_list = []

def split_tran(txt):
    txt_revise = txt.replace(",", '').replace(".", '')
    split_result = nltk.word_tokenize(txt_revise)
    for i in range(len(split_result)):
        split_result[i] = prondict[split_result[i].lower()]
        if split_result[i]:
            split_result[i] = split_result[i][0]
    return split_result

def list_str(list_tmp):
    result_str = ""
    for i in range(len(list_tmp)):
        str_tmp = [str(j) for j in list_tmp[i]]
        str_join_tmp = ' '.join(str_tmp)
        result_str = result_str + " " + str_join_tmp
    return result_str

for index, row in df.iterrows():
    list_origin = split_tran(row["Origin"])
    list_result = split_tran(row["Result"])

    pro_origin_list.append(list_str(list_origin))
    pro_result_list.append(list_str(list_result))
    # str_tmp = ''
    # if row["Origin"] == row["Result"]:
    #     same_list.append(1)
    # else:
    #     same_list.append(0)
    #
    # for i in row['Result']:
    #     for j in row['Origin'].lower():
    #         if i == j:
    #             str_tmp = ''.join([str_tmp,i])
    #             break
                # str_diff_tmp = ''.join([str_tmp,i])
    #             # char_full_list.append(0)
    #             # break
    # # print(str_tmp)
    # str_list.append(str_tmp)
    # if str_tmp == row['Result']:
    #     char_full_list.append(1)
    # else:
    #     char_full_list.append(0)
    # char_rep_rate = len(str_tmp.replace(" ", ""))/len(str(row['origin']).replace(" ", ""))
    # char_rep_rate_list.append(char_rep_rate)
df['pro_origin'] = pro_origin_list
df['pro_result'] = pro_result_list
# df['same'] = same_list
# df['align'] = str_list

# same_number = len(df[df['same'].isin(1)])
# df['char_rate'] = char_rep_rate_list
# df['char_full'] = char_full_list

df.to_csv('result_100.csv')

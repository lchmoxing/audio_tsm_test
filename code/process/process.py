
# coding: utf-8

import os
import pandas as pd
import numpy as np

dir_path = os.path.abspath('.')
exl_path = dir_path + r'/result_200.csv'
print(exl_path)
df = pd.read_csv(exl_path,keep_default_na=False)

str_list= []
pho_str_list = []
pro_origin_list =[]
pro_result_list = []
char_same_list = []
pro_same_list = []
char_full_list = []
pho_full_list =[]
char_rate_list = []
pho_rate_list = []
char_diffnum_list = []
pho_diffnum_list = []

for index, row in df.iterrows():
    str_tmp = ''
    pho_tmp = ''
    count_char = 0
    count_pho = 0
    if row['Origin'].replace(",", '').replace(".", '').strip() == row['Result']:
        char_same_list.append(1)
    else:
        char_same_list.append(0)

    if row['pro_origin'].replace(",", '').replace(".", '') == row['pro_result']:
        pro_same_list.append(1)
    else:
        pro_same_list.append(0)

    origin_tmp = set(row['Result'])
    result_tmp = set(row['Origin'].lower())
    str_tmp = ''.join([str_tmp, origin_tmp & result_tmp])
    # for i in row['Result']:
    #     if i in row['Origin'].lower():
    #         str_tmp = ''.join([str_tmp, i])
    #     else:
    #         count_char = count_char+1
    char_diffnum_list.append(count_char)
        # for j in row['Origin'].lower():
        #     if i == j:
        #         str_tmp = ''.join([str_tmp,i])
        #         break
    str_list.append(str_tmp)
    if str_tmp == row['Result']:
        char_full_list.append(1)
    else:
        char_full_list.append(0)
    char_rate_list.append(len(str_tmp)/len(row['Origin'].lower()))


    origin_pho_list_tmp = row['pro_origin'].split()
    result_pho_list_tmp = row['pro_result'].split()

    # for i in result_pho_list_tmp:
    #     if i in origin_pho_list_tmp:
    #         pho_tmp = ' '.join([pho_tmp, i])
    #     else:
    #         count_pho = count_pho + 1
        # for j in origin_pho_list_tmp:
        #     if i == j:
        #         pho_tmp = ' '.join([pho_tmp,i])
        #         break
    pho_diffnum_list.append(count_pho)
    pho_str_list.append(pho_tmp)

    if pho_tmp == row['pro_result']:
        pho_full_list.append(1)
    else:
        pho_full_list.append(0)
    pho_rate_list.append(len(pho_tmp) / len(row['pro_origin'].lower()))
    # char_rep_rate = len(str_tmp.replace(" ", ""))/len(str(row['origin']).replace(" ", ""))
    # char_rep_rate_list.append(char_rep_rate)
# char_same_list.append(df.loc[:,'char_same'].value_counts())
# pro_same_list.append(df.loc[:,'pro_same'].value_counts())
df['char_same'] = char_same_list
df['pro_same'] = pro_same_list
df['char_align'] = str_list
df['pho_align'] = pho_str_list
df['char_full'] = char_full_list
df['pho_full'] = pho_full_list
df['char_diffnum'] = char_diffnum_list
df['pho_diffnum'] = pho_diffnum_list
df['char_rate'] = char_rate_list
df['pho_tate'] = pho_rate_list

df['char_same_num'] = df.loc[:,'char_same'].value_counts()
df['pro_same_num'] = df.loc[:,'pro_same'].value_counts()
df['char_full_sum'] = df.loc[:,'char_full'].value_counts()
df['pho_full_sum'] = df.loc[:,'pho_full'].value_counts()

# print(df.loc[:,'char_same'].value_counts())
# print(df.loc[:,'pro_same'].value_counts())
# same_number = len(df[df['same'].isin(1)])
# df['char_rate'] = char_rep_rate_list


df.to_csv('subresult_200.csv')

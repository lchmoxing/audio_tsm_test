import os
import cmudict
import pandas as pd
import nltk
import Levenshtein

nltk.download('punkt')
prondict = cmudict.dict()
path = os.path.dirname(os.path.abspath('.'))

# text_path = path + '/ASR/baidu/baidu_with_wake_words0.csv'

#F:\github\audio_tsm_test\code\ASR\baidu

# def split_tran(txt):
#     txt_revise = txt.replace(",", '').replace(".", '')
#     split_result = nltk.word_tokenize(txt_revise)
#     for i in range(len(split_result)):
#         split_result[i] = prondict[split_result[i].lower()]
#     # print(split_result)
#     pro_list = [item[0] for item in split_result]
#     # print(pro_list)
#     return pro_list
#
# def list_str(list_tmp):
#     result_str = ""
#     for i in range(len(list_tmp)):
#         str_tmp = [str(j) for j in list_tmp[i]]
#         str_join_tmp = ' '.join(str_tmp)
#         result_str = result_str + " " + str_join_tmp
#     return result_str

a = "I want to take a picture"
b = "coire"
split_result = prondict[b]
print(split_result)
# c = "hello"
#
# list_a = split_tran(a)
# list_b= split_tran(b)
# list_c = split_tran(c)
#
# str_a = list_str(list_a)
# str_b = list_str(list_b)
# str_c = list_str(list_c)

# result_word = Levenshtein.ratio(a, b)
# # result_word_1 = Levenshtein.ratio(a, c)
# # result_pho = Levenshtein.ratio(str_a, str_b)
# # result_pho_1 = Levenshtein.ratio(str_a, str_c)
# print(result_word)
# print(result_word_1)
# print(result_pho)
# print(result_pho_1)
# str_a =[str(i) for i in a]
# str_b =[str(i) for i in b]
# print(str_a)
# print(str_b)
# a_1 = ' '.join(a)
# b_1 = ' '.join(b)
# print(a_1)
# print(b_1)
# c = Levenshtein.ratio(a, b)
# print(c)
# all_txt = pd.read_csv(text_path)
# name = list(all_txt.columns.values)
# df = pd.DataFrame(columns = name)
#
# tran_tmp = []
# for index, row in all_txt.iteritems():
#     for i in range(len(row)):
#         if row[i] != 'error':
#             tran_tmp.append(split_tran(row[i]))
#         else:
#             tran_tmp.append('')
#     df[index] = tran_tmp
#     tran_tmp = []
# df.to_excel("tran_0.xlsx")

'''
for index, row in all_txt.iteritems():
    if row[count] != "error":
        tran_tmp.append(split_tran(row['origin']))
'''
'''
tran = []
for index, row in all_txt.iterrows():
    tran.append(split_tran(row['origin']))
all_txt['tran'] = tran
all_txt.to_excel("split_tran.xlsx")
'''
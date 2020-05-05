from jiwer import wer
import os
import numpy as np
import pandas as pd

filename = r'C:\github_code\audio_tsm_test\code\ASR\kdxf\kdxf2.csv'
path = r'C:\github_code\audio_tsm_test\code\ASR\kdxf\kdxf3.csv'
data = pd.read_csv(filename)
ground_truth = data['ground_truth'].tolist()
# print(data['ground_truth'].tolist())
# ola = data['ola0.25'].tolist()

asr_wer = []
for i in data:
    hypothesis = data[i].tolist()
    error = wer(ground_truth,hypothesis)
    for m,n in zip(ground_truth,hypothesis):
        error = wer(m, n)
        asr_wer.append(error)
        print(error)
    df[i] = asr_wer
    df.to_csv(path, mode = 'a', index = False)
    asr_wer.clear()
# print(data['origin'])
# print(type(data['origin']))
# ground_truth = data['ground_truth']
# print(ground_truth)
# path = os.getcwd()
# print(path)
# ground_truth_path = os.path.join(path + r"\dataset\text\textwithwakewords.txt")
# hypothesis_path = os.path.join(path + r"\test_result\kdxf\16k\with_wake_words")

# ground_truth = []
# with open(ground_truth_path,'r') as orgin_file:
#     for file in orgin_file.readlines():
#         file = file.strip("\n")
#         ground_truth.append(file)
#         # print(ground_truth)

# filelist = []
# for i in os.listdir(hypothesis_path):
#     filelist.append(i)

# hypothesis = []
# for file in filelist:
#     os.chdir(hypothesis_path)
#     imgname = os.path.splitext(file)[0]
#     asr_file = open(file)
#     for i in asr_file.readlines():
#         i = i.strip("\n")
#         hypothesis.append(i)
#     for i in range(0,len(ground_truth)):
#         error = wer(ground_truth[i], hypothesis[i])
#         print(error)
#     hypothesis = []
# ground_truth = open("sample.txt") 
# wer = jiwer.wer(ground_truth, hypothesis)
# mer = jiwer.mer(ground_truth, hypothesis)
# wil = jiwer.wil(ground_truth, hypothesis)
# ground_truth = ["hello world","A"]
# hypothesis = ["world ","A"]
# for m, n in zip(ground_truth,hypothesis):
#     print(m,n)
#     error = wer(m, n)
#     print(error)
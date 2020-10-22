

import os
import pandas as pd

path = os.path.dirname(os.path.abspath('.'))
dir_path = os.path.abspath('.')

text_path = dir_path + r'\data.xlsx'
data = pd.read_excel(text_path)

sum_exl = pd.DataFrame(columns = ["Result", "Sequence", "Speed", "Origin",'audio_num','Type'])
exl_path = dir_path + '/sum_50.csv'
sum_exl.to_csv(exl_path)

dir = dir_path + r'\50'
subdir_list = os.listdir(dir)
#print(len(subdir))
type_list = []

for i in range(len(subdir_list)):
    excel_path = dir + '/' + str(subdir_list[i])
    audio_num = os.path.splitext(subdir_list[i])[0]
    df = pd.read_csv(excel_path)
    df['Origin'] = (data.iloc[int(audio_num) - 1][1]).lower().replace("’","'")
    df.loc[1,'audio_num'] = audio_num
    df.loc[1,'Type'] = df.ix[len(df) - 1,0]
    df.drop([len(df) - 1], inplace=True)
    # print((data.iloc[int(audio_num) - 1][1]))
    # print(df)
    df.to_csv('sum_50.csv', mode='a', header=False)




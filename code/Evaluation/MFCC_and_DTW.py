###pip install librosa
###pip install --ignore-installed llvmlite
###cannot import name 'comb'解决方法：
###修改lib\site-packages\sklearn\model_selection\_split.py中from scipy.misc import comb为from scipy.special import comb
###修改lib\site-packages\sklearn\metrics\cluster\supervised.py中from scipy.misc import comb为from scipy.special import comb

import librosa
import librosa.display
import matplotlib
import matplotlib.pyplot as plt
from dtw import dtw
from numpy.linalg import norm
import numpy as np
import pandas as pd
import os

#Loading audio files
path =os.path.abspath('..')
path =os.path.dirname(path)
print(path) 
for num in range(1, 11):
    phasevoctor = []
    ola = []
    wsola = []
    speed = []
    for i in np.arange(0.25, 3, 0.25):
        ### audio without wake words
        # audio_origin = path + '/dataset/speech_origin/without_wake_words/' + str(num) +'.wav'
        # audio_phasevoctor = path + '/dataset/speech_TSM/without_wake_words/phasevoctor' + str(i) + '_' + str(num) +'.wav'
        # audio_ola = path + '/dataset/speech_TSM/without_wake_words/ola' + str(i) + '_' + str(num) +'.wav'
        # audio_wsola = path + '/dataset/speech_TSM/without_wake_words/wsola' + str(i) + '_' + str(num) +'.wav'
        ### audio with wake words
        audio_origin = path + '/dataset/speech_origin/with_wake_words/' + str(num) +'.wav'
        audio_phasevoctor = path + '/dataset/speech_TSM/with_wake_words/phasevoctor' + str(i) + '_' + str(num) +'.wav'
        audio_ola = path + '/dataset/speech_TSM/with_wake_words/ola' + str(i) + '_' + str(num) +'.wav'
        audio_wsola = path + '/dataset/speech_TSM/with_wake_words/wsola' + str(i) + '_' + str(num) +'.wav'
        y1, sr1 = librosa.load(audio_origin) 
        y2, sr2 = librosa.load(audio_phasevoctor) 
        y3, sr3 = librosa.load(audio_ola)
        y4, sr4 = librosa.load(audio_wsola)  

        mfcc1 = librosa.feature.mfcc(y1, sr1)
        mfcc2 = librosa.feature.mfcc(y2, sr2)
        mfcc3 = librosa.feature.mfcc(y3, sr3)
        mfcc4 = librosa.feature.mfcc(y4, sr4)
        # dist1, cost1, acc_cost1, path1 = dtw(mfcc1.T, mfcc1.T, dist=lambda x, y: norm(x - y, ord=1))
        dist2, cost2, acc_cost2, path2 = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
        dist3, cost3, acc_cost3, path3 = dtw(mfcc1.T, mfcc3.T, dist=lambda x, y: norm(x - y, ord=1))
        dist4, cost4, acc_cost4, path4 = dtw(mfcc1.T, mfcc4.T, dist=lambda x, y: norm(x - y, ord=1))
        phasevoctor.append(dist2)
        ola.append(dist3)
        wsola.append(dist4)
        speed.append(i)
    locals()['pdf'+ str(num)]= pd.DataFrame({"sentence" + str(num):phasevoctor})
    locals()['odf'+ str(num)]= pd.DataFrame({"sentence" +str(num):ola})
    locals()['wdf'+ str(num)]= pd.DataFrame({"sentence" +str(num):wsola})
pdf0 = pd.DataFrame({"speed" : speed})
odf0 = pd.DataFrame({"speed" : speed})
wdf0 = pd.DataFrame({"speed" : speed})
pdf = pd.concat([pdf0,pdf1,pdf2,pdf3,pdf4,pdf5,pdf6,pdf7,pdf8,pdf9,pdf10], axis =1 )
odf = pd.concat([odf0,odf1,odf2,odf3,odf4,odf5,odf6,odf7,odf8,odf9,odf10], axis =1 )
wdf = pd.concat([wdf0,wdf1,wdf2,wdf3,wdf4,wdf5,wdf6,wdf7,wdf8,wdf9,wdf10], axis =1 )
# ### audio without wake words
# pdf.to_csv(path + "/dataset/wo_phasevoctor_mfcc.csv", index=False)
# odf.to_csv(path + "/dataset/wo_ola_mfcc.csv", index=False)
# wdf.to_csv(path + "/dataset/wo_wsola_mfcc.csv", index=False)
### audio with wake words
pdf.to_csv(path + "/dataset/w_phasevoctor_mfcc.csv", index=False)
odf.to_csv(path + "/dataset/w_ola_mfcc.csv", index=False)
wdf.to_csv(path + "/dataset/w_wsola_mfcc.csv", index=False)
print("successfully!")
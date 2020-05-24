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

y1, sr1 = librosa.load('C:/Users/73936/Desktop/voice_speech/dataset/1.wav')
y2, sr2 = librosa.load('C:/Users/73936/Desktop/voice_speech/dataset/ola0.5_1.wav')
import os

#Loading audio files
path =os.path.abspath('..')
path =os.path.dirname(path)
path1 =os.path.dirname(path)
print(path1)
audio_origin = path1 + '/dataset/speech_origin/without_wake_words/' + str(1) +'.wav'
audio_phasevoctor = path1 + '/dataset/speech_TSM/without_wake_words/phasevoctor' + str(1.0) + '_' + str(1) +'.wav'
# audio_ola = path1 + '/dataset/speech_TSM/without_wake_words/ola' + str(i) + '_' + str(num) +'.wav'
# audio_wsola = path1 + '/dataset/speech_TSM/without_wake_words/wsola' + str(i) + '_' + str(num) +'.wav'
y1, sr1 = librosa.load(audio_origin) 
y2, sr2 = librosa.load(audio_phasevoctor) 

plt.subplot(1, 3, 1)
mfcc1 = librosa.feature.mfcc(y1, sr1)
librosa.display.specshow(mfcc1)
plt.subplot(1, 3, 2)
mfcc2 = librosa.feature.mfcc(y2, sr2)
librosa.display.specshow(mfcc2)

dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T, dist=lambda x, y: norm(x - y, ord=1))
print('Normalized distance between the two sounds:', dist)
plt.subplot(1, 3, 3)
plt.imshow(cost.T, origin='lower', cmap='gray', interpolation='nearest')
plt.plot(path[0], path[1], 'w')
plt.xlim((-0.5, cost.shape[0]-0.5))
plt.ylim((-0.5, cost.shape[1]-0.5))
plt.show()
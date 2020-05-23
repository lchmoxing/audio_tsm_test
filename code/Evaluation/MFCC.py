import librosa
import librosa.display
import matplotlib.pyplot as plt
from dtw import dtw
from numpy.linalg import norm
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

#Showing multiple plots using subplot
plt.subplot(1, 2, 1) 
mfcc1 = librosa.feature.mfcc(y1,sr1)   #Computing MFCC values
librosa.display.specshow(mfcc1)

plt.subplot(1, 2, 2)
mfcc2 = librosa.feature.mfcc(y2, sr2)
librosa.display.specshow(mfcc2)

dist, cost, path = dtw(mfcc1.T, mfcc2.T)
print("The normalized distance between the two : ",dist)   # 0 for similar audios 

plt.imshow(cost.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
plt.plot(path[0], path[1], 'w')   #creating plot for DTW

plt.show()  #To display the plots graphically
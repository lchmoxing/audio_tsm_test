import Baidu_ASR 
import os

path =os.path.abspath('..')
path =os.path.dirname(path)
path1 =os.path.dirname(path)
print(path1)
audio = path1 + '/dataset/speech_TSM/without_wake_words/wsola' + str(0.5) + '_' + str(1) +'.wav'
Baidu_ASR.baidu_asr(audio)
print("succed!")
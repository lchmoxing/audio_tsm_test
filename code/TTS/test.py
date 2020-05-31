###pip install gTTS
###written by qhjiang 
from gtts import gTTS
from pydub import AudioSegment
import ffmpeg

AudioSegment.converter = "C:/software/ffmpeg-20200218-ebee808-win64-static/ffmpeg-20200218-ebee808-win64-static/bin/ffmpeg.exe"

# filename = "C:/Users/73936/Desktop/voice_speech/dataset/text/textwithoutwakewords.txt"
num = 0

filename_mp3 = 'D:/github/audio_tsm_test/dataset/speech_origin/with_wake_words/' + str(1) +'.mp3'
filename_wav = 'D:/github/audio_tsm_test/' + str(1) +'.wav'
AudioSegment.from_mp3(filename_mp3).export(filename_wav, format = "wav")

print("The dataset has been successfully generated!")

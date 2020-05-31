###pip install gTTS
###written by qhjiang 
from gtts import gTTS
from pydub import AudioSegment
import ffmpeg

# AudioSegment.converter = "C:/software/ffmpeg-20200218-ebee808-win64-static/ffmpeg-20200218-ebee808-win64-static/bin/ffmpeg.exe"
filename = "D:/github/audio_tsm_test/dataset/speech_origin/text/textwithwakewords.txt"
# filename = "C:/Users/73936/Desktop/voice_speech/dataset/text/textwithoutwakewords.txt"
num = 0

with open(filename) as text_object:
    for text in text_object:
        text = text.strip()
        print(text)
        tts = gTTS(text, lang = 'en')
        num +=1
        # filename_mp3 = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) +'.mp3'
        # filename_wav = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) +'.wav'
        # filename_mp3 = 'C:/Users/73936/Desktop/voice_speech/dataset/speech_origin/without_wake_words/' + str(num) +'.mp3'
        # filename_wav = 'C:/Users/73936/Desktop/voice_speech/dataset/speech_origin/without_wake_words/' + str(num) +'.wav'
        filename_mp3 = 'D:/github/audio_tsm_test/dataset/speech_origin/with_wake_words/16k/' + str(num) +'.mp3'
        filename_wav = 'D:/github/audio_tsm_test/dataset/speech_origin/with_wake_words/16k' + str(num) +'.wav'
        # ffmpeg.input('filename_mp3').output('filename_mp3', ar=16000).run()
        tts.save(filename_mp3)
        AudioSegment.from_mp3(filename_mp3).export(filename_wav, format = "wav")
        # tts.save('C:/Users/73936/Desktop/voice_speech/dataset/%d.mp3'%(num))
        # AudioSegment.from_mp3('C:/Users/73936/Desktop/voice_speech/dataset/%d.mp3'%(num)).export('C:/Users/73936/Desktop/voice_speech/dataset/%d.wav'%(num),format = "wav")
# tts = gTTS('hello', lang='en')
# tts.save('C:/Users/73936/Desktop/voice_speech/hello.mp3')
# path_file = 'C:/Users/73936/Desktop/voice_speech/hello.mp3'
# print(path_file)
# song = AudioSegment.from_file(path_file,format='mp3')
# song.export('C:/Users/73936/Desktop/voice_speech/heLlo.wav', format = 'wav')
print("The dataset has been successfully generated!")

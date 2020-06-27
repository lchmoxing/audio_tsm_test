
###pip install baidu-aip
###written by qhjiang 
from aip import AipSpeech
from pydub import AudioSegment

APP_ID = '18493239'
API_KEY = 'T5sA7FUN2803vZfVURRG8Fz0'
SECRET_KEY = 'KHG7i6cS8Dksy2oSIDSGl0k1rHbC1L8L'
AudioSegment.converter = "C:/software/ffmpeg-20200218-ebee808-win64-static/ffmpeg-20200218-ebee808-win64-static/bin/ffmpeg.exe"
filename = "C:/Users/73936/Desktop/voice_speech/dataset/text/oppo.txt"
num = 0

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
with open(filename,'r', encoding='UTF-8') as text_object:
    for text in text_object:
        text = text.strip()
        result = client.synthesis(text, 'zh', 1, { 'vol': 5,'per':3 }) 
        filename_mp3 = 'C:/Users/73936/Desktop/speech/' + str(num) +'.mp3'
        filename_wav = 'C:/Users/73936/Desktop/speech/' + str(num) +'.wav'
        if not isinstance(result, dict): 
            with open(filename_mp3, 'wb') as f: 
                f.write(result)
                num +=1
        AudioSegment.from_mp3(filename_mp3).export(filename_wav, format = "wav")
print("The dataset has been successfully generated!")
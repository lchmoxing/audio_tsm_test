import os
import sys
# from ffmpeg import audio

# def ffmpeg_tsm(speed, audio_path, finish_path):
#     audio_file = os.listdir(audio_path)
#     for i, audio1 in enumerate(audio_file):
#         print(audio_path+audio1)
#         audio.a_speed(audio_path+audio1,'"' + speed + '"', finish_path+audio1 )

# ffmpeg_tsm(1.5,'C:/Users/qinhong/Desktop/dataset719','C:/Users/qinhong/Desktop/dataset719')

audio_path = 'C:/Users/qinhong/Desktop/dataset719/'
finish_path = 'C:/Users/qinhong/Desktop/dataset719/'

def run():
    audio_file = os.listdir(audio_path)
    for i,audio1 in enumerate(audio_file):
        #print(audio_path+audio1)     
        cmd = "ffmpeg -n -i "+audio_path+audio1+" -filter:a atempo=1.25 "+finish_path+"1.25x"+audio1
        print(cmd)
        os.system(cmd)
        #audio.a_speed(audio_path+audio1, "2", finish_path+"2x"+audio1)
run()
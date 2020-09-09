### writted by qinhong jiang
### 通过 av filter 中的 atempo 来实现：ffmpeg -i input.mkv -filter:a "atempo=2.0" -vn output.mkv
### atempo filter 配置区间在0.5和2.0之间，如果需要更高倍，可以使用多个 atempo filter 串在一起来实现，下面是实现4倍的参考：ffmpeg -i input.mkv -filter:a "atempo=2.0,atempo=2.0" -vn output.mkv
import os
import sys
# from ffmpeg import audio

# def ffmpeg_tsm(speed, audio_path, finish_path):
#     audio_file = os.listdir(audio_path)
#     for i, audio1 in enumerate(audio_file):
#         print(audio_path+audio1)
#         audio.a_speed(audio_path+audio1,'"' + speed + '"', finish_path+audio1 )

# ffmpeg_tsm(1.5,'C:/Users/qinhong/Desktop/dataset719','C:/Users/qinhong/Desktop/dataset719')

input_path = 'C:/Users/qinhong/Desktop/dataset719/'
output_path = 'C:/Users/qinhong/Desktop/dataset719/'

def run(input_path, output_path, speed):
    audio_file = os.listdir(input_path)
    for i,audio1 in enumerate(audio_file):
        #print(audio_path+audio1)     
        # cmd = "ffmpeg -i "+audio_path+audio1+' -filter:a "atempo=2.0" -vn '+finish_path+"2.0x"+audio1
        cmd = "ffmpeg -i "+input_path+audio1+' -filter:a ' + "atempo="+ str(speed) + " -vn " + output_path+ str(speed) + "x"+audio1
        # cmd = "ffmpeg -i "+audio_path+audio1+" -filter:a atempo=1.25 "+finish_path+"1.25x"+audio1
        print(cmd)
        os.system(cmd)
        #audio.a_speed(audio_path+audio1, "2", finish_path+"2x"+audio1)
run(input_path, output_path, speed=2.0)
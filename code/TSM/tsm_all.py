### writted by qinhong jiang
### 通过 av filter 中的 atempo 来实现：ffmpeg -i input.mkv -filter:a "atempo=2.0" -vn output.mkv
### atempo filter 配置区间在0.5和2.0之间，如果需要更高倍，可以使用多个 atempo filter 串在一起来实现，下面是实现4倍的参考：ffmpeg -i input.mkv -filter:a "atempo=2.0,atempo=2.0" -vn output.mkv
import os
import sys
import numpy as np
# from ffmpeg import audio

from audiotsm import phasevocoder, ola, wsola
from audiotsm.io.wav import WavReader, WavWriter

# def ffmpeg_tsm(speed, audio_path, finish_path):
#     audio_file = os.listdir(audio_path)
#     for i, audio1 in enumerate(audio_file):
#         print(audio_path+audio1)
#         audio.a_speed(audio_path+audio1,'"' + speed + '"', finish_path+audio1 )

# ffmpeg_tsm(1.5,'C:/Users/qinhong/Desktop/dataset719','C:/Users/qinhong/Desktop/dataset719')

input_path = 'C:/Users/qinhong/Desktop/dataset719/1/'
output_path = 'C:/Users/qinhong/Desktop/dataset719/1/'

def tsm_ffmpeg(input_path, output_path, speed):
    audio_file = os.listdir(input_path)
    for i,audio1 in enumerate(audio_file):
        #print(audio_path+audio1)     
        # cmd = "ffmpeg -i "+audio_path+audio1+' -filter:a "atempo=2.0" -vn '+finish_path+"2.0x"+audio1
        cmd = "ffmpeg -i "+input_path+audio1+' -filter:a ' + "atempo="+ str(speed) + " -vn " + output_path + audio1[:-4] +"_"+str(speed)+'.wav'
        # cmd = "ffmpeg -i "+audio_path+audio1+" -filter:a atempo=1.25 "+finish_path+"1.25x"+audio1
        print(cmd)
        os.system(cmd)
        #audio.a_speed(audio_path+audio1, "2", finish_path+"2x"+audio1)

def tsm_three_kinds(ca_type,i,input_path,output_path):
    input_filenames = os.listdir(input_path)
    for input_filename in input_filenames:
        with WavReader(input_path + input_filename) as reader:
            output_filename = output_path +str(i) + "x" + input_filename[:-4]+'.wav'
            with WavWriter(output_filename, reader.channels, reader.samplerate) as writer_tsm:
                if (ca_type == phasevocoder):
                    tsm = phasevocoder(reader.channels, speed=i)
                if (ca_type == ola):
                    tsm = ola(reader.channels, speed=i)
                if (ca_type == wsola):
                    tsm = wsola(reader.channels, speed=i)
                tsm.run(reader, writer_tsm)
        print("audio_tsm successfully")

if __name__ == '__main__':
    # main()
    # tsm_ffmpeg(input_path, output_path, speed=2)
    # tsm_three_kinds(wsola,2.0,input_path, output_path)
    input_path = '/home/usslab/Documents/qinhong/dataset72916k/origin/'
    output_path = '/home/usslab/Documents/qinhong/dataset72916k/ffmpeg/'
    for speed in np.arange(0.5, 2.0, 0.25):
        speed = round(speed,2)
        tsm_ffmpeg(input_path, output_path, speed)
### writted by qinhong jiang
### -acodec pcm_s16le pcm_s16le 16bits 编码器
### -ac 1 单声道
### -ar 16000 16000采样率

import os
import sys

# def convert_16k(input_path,output_path):
#     audio_folders = os.listdir(input_path)
#     # print(audio_file)
#     for audio_folder in audio_folders:
#         # print(audio)
#         input_folder = os.path.join(input_path,audio_folder)
#         print(input_folder)
#         output_folder = os.path.join(output_path,audio_folder)
#         print(output_folder)
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)
#         if(os.path.isdir(input_folder)):
#             audio_file = os.listdir(input_folder)
#             for i,audio in enumerate(audio_file):
#                 cmd = "ffmpeg -i "  + input_folder+'/'+audio + " -ar 16000 " + output_folder+'/'+audio
#                 os.system(cmd)
#         # for audio in enumerate(audio_file):
#         #     #print(audio_path+audio1)
#         #     cmd = "ffmpeg -i "  + audio_path+audio + " -ar 16000 " + finish_path+"16k"+audio
#         #     print(cmd) 
#         #     os.system(cmd)

# convert_16k('/home/usslab/Documents/qinhong/VCTK-Corpus/wav48/','/home/usslab/Documents/qinhong/VCTK-Corpus/wav16/')

def mp3towav_convert_16k(input_path,output_path):
    audio_files = os.listdir(input_path)
    # print(audio_file)
    for audio_file in audio_files:
        # print(audio)
        if audio_file[-4:] == '.mp3':
            input_file = os.path.join(input_path,audio_file)
            print(input_file)
            output_file = output_path+'/'+audio_file[:-4]+'.wav'
            print(output_file)
            cmd = "ffmpeg -i "  + input_file + " -acodec pcm_s16le -ac 1 -ar 16000 " + output_file
            os.system(cmd)
            # for audio in enumerate(audio_file):
            #     #print(audio_path+audio1)
            #     cmd = "ffmpeg -i "  + audio_path+audio + " -ar 16000 " + finish_path+"16k"+audio
            #     print(cmd) 
            #     os.system(cmd)
# mp3towav_convert_16k('C:/Users/qinhong/Desktop/dataset719/1','C:/Users/qinhong/Desktop/dataset719/1')
mp3towav_convert_16k(r'C:\Users\qinhong\Desktop\audio92\phonetic',r'C:\Users\qinhong\Desktop\audio92\phonetic16k')
import os
from pydub import AudioSegment
import wave
import numpy as np
import shutil
import random
from audiotsm import phasevocoder, ola, wsola
from audiotsm.io.wav import WavReader, WavWriter


# def audio_split(file_path, split_time):
#     for i in range(len(file_path))
#         FileName = files[i]
#         print("CutFile File Name is ",FileName)
#         f = wave.open(r"" + FileName, "rb")
#         params = f.getparams()
#         # print(params)
#         nchannels, sampwidth, framerate, nframes = params[:4]
#         CutFrameNum = int(framerate * split_time)

#         # print("CutFrameNum=%d" % (CutFrameNum))
#         #     # print("nchannels=%d" % (nchannels))
#         #     # print("sampwidth=%d" % (sampwidth))
#         #     # print("framerate=%d" % (framerate))
#         #     # print("nframes=%d" % (nframes))
#         str_data = f.readframes(nframes)
#         f.close()  # 将波形数据转换成数组

#         wave_data = np.fromstring(str_data, dtype=np.short)
#         # print(np.shape(wave_data))
#         # wave_data.shape = -1, 2
#         # print(np.shape(wave_data))
#         wave_data = wave_data.T
#         temp_data = wave_data.T
#         # print(np.shape(temp_data))
#         # StepNum = int(CutFrameNum/2)
#         StepNum = CutFrameNum
#         StepTotalNum = 0
#         count = 0
#         while StepTotalNum < nframes:
#             FileName = result_dir + '/' + files[i][:-4] + '_' + str(count + 1) + ".wav"
#             temp_dataTemp = temp_data[StepNum*(count):StepNum*(count + 1)]

#             count = count + 1
#             StepTotalNum = count * StepNum
#             temp_dataTemp.shape = 1, -1
#             temp_dataTemp = temp_dataTemp.astype(np.short)  # 打开WAV文档
#             f = wave.open(FileName, "wb")  #
#             # 配置声道数、量化位数和取样频率
#             f.setnchannels(nchannels)
#             f.setsampwidth(sampwidth)
#             f.setframerate(framerate)
#             # 将wav_data转换为二进制数据写入文件
#             f.writeframes(temp_dataTemp.tostring())
#             f.close()
#     print("audio_split successfully")

def audio_split(input_file_path, split_time):
    wav_time =AudioSegment.from_file(input_file_path).duration_seconds
    wav_time = int(wav_time * 1000)
    # print(wav_time)
    start_time = 0
    end_time = split_time
    sound = AudioSegment.from_wav(input_file_path)
    (filepath,tempfilename) = os.path.split(input_file_path)
    for i in range(1,(wav_time//split_time+2)):
        output_file_path = filepath + '\speech_split' +'\\' + tempfilename[:-4] + '\\' + str(i) + '.wav'
        word = sound[start_time:end_time]
        word.export(output_file_path,format='wav')
        start_time += split_time
        end_time += split_time

def audio_join(input_dir, output_dir):
    join_sound_lists = AudioSegment.empty()
    for i in range(len(os.listdir(input_dir))):
        filename = input_dir + '\\'  +str(i + 1) + '.wav'
        join_sound_lists += AudioSegment.from_wav(filename)
    join_sound_lists.export(output_dir, format="wav")
    print("audio_join successfully")

def audio_tsm(ca_type,i,input_filename,output_filename):
    with WavReader(input_filename) as reader:
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
    path = r"D:\github\audio_tsm_test\dataset\speech_origin\without_wake_words"
    src = r"D:\github\audio_tsm_test\dataset\speech_origin\without_wake_words\speech_split" 
    dst = r"D:\github\audio_tsm_test\dataset\speech_split_tsm_join\split_orgin"
    dst2 = r"D:\github\audio_tsm_test\dataset\speech_split_tsm_join\split_test"
    if(os.path.exists(dst)):
        shutil.copytree(dst, dst2)
        for i in range(1,11):
            join_input_path = dst2 + '\\' + str(i)
            join_output_path = dst2 + '\\' + str(i) + '.wav'
            print(len(os.listdir(join_input_path)))
            for j in range(len(os.listdir(join_input_path))):
                tsm_path = dst2 + '\\' + str(i) +'\\' + str(j+1) + '.wav'
                if (j <=10):
                    audio_tsm(ola, 0.9, tsm_path, tsm_path)
                    # random.randint(0,9)random.uniform(0.5,1.5)
            audio_join(join_input_path,join_output_path)
    else: 
        for i in range(1,11):
            input_path = path + '\\' + str(i) + '.wav'
            split_path = path + '\speech_split' + '\\' + str(i)
            audio_split(input_path,50)
        shutil.copytree(src, dst)
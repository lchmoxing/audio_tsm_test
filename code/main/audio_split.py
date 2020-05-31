import os
from pydub import AudioSegment
import wave
import numpy as np


#path = os.path.dirname(os.path.abspath('.'))
#ffmpeg_path = path + '/third_party/ffmpeg/ffmpeg-20200218-ebee808-win64-static/bin/ffmpeg.exe'
#file_test = './ola1.0_1.wav'
CutTimeDef = 0.1

def CutFile(countNum,file_test):
    print("CutFile File Name is ", file_test)
    f = wave.open(file_test, "rb")
    params = f.getparams()
    # print(params)
    nchannels, sampwidth, framerate, nframes = params[:4]
    CutFrameNum = int(framerate * CutTimeDef)

    # print("CutFrameNum=%d" % (CutFrameNum))
    #     # print("nchannels=%d" % (nchannels))
    #     # print("sampwidth=%d" % (sampwidth))
    #     # print("framerate=%d" % (framerate))
    #     # print("nframes=%d" % (nframes))
    str_data = f.readframes(nframes)
    f.close()  # 将波形数据转换成数组

    wave_data = np.fromstring(str_data, dtype=np.short)
    # print(np.shape(wave_data))
  #  wave_data.shape = -1, 2
   # print(np.shape(wave_data))
    wave_data = wave_data.T
    temp_data = wave_data.T
    # print(np.shape(temp_data))
 #   StepNum = int(CutFrameNum/2)
    StepNum = CutFrameNum
    StepTotalNum = 0;
    count = 0
    result_dir = os.getcwd() +'/split_result'
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    while StepTotalNum < nframes:
        # print("Stemp=%d" % (count))
        FileName = result_dir + '/' + str(countNum) + '_' + str(count + 1) + ".wav"
        # print(FileName)
        temp_dataTemp = temp_data[StepNum*(count):StepNum*(count + 1)]

        count = count + 1;
        StepTotalNum = count * StepNum;
        temp_dataTemp.shape = 1, -1
        temp_dataTemp = temp_dataTemp.astype(np.short)  # 打开WAV文档
        f = wave.open(FileName, "wb")  #
        # 配置声道数、量化位数和取样频率
        f.setnchannels(nchannels)
        f.setsampwidth(sampwidth)
        f.setframerate(framerate)
        # 将wav_data转换为二进制数据写入文件
        f.writeframes(temp_dataTemp.tostring())
        f.close()
    print("Split Run Over")
if __name__ == '__main__':
    CutFile(file_test)
    print("Run Over")


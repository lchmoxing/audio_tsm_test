import audio_split
import audio_join
import audio_tsm
import audio_asr
import os
import numpy as np

path = os.getcwd()
path1 = os.path.dirname(os.path.abspath('.'))
path2 = os.path.dirname(os.path.abspath('..'))

ffmpeg_path = path1 + '/third_party/ffmpeg/ffmpeg-20200218-ebee808-win64-static/bin/ffmpeg.exe'
#read origin
# with_wake_words
origin_file_dir = path2 + '/dataset/speech_origin/with_wake_words/'
origin_file_list = os.listdir(origin_file_dir)
# without_wake_words
#origin_file_dir = path2 + '/document/speech_origin/without_wake_words/'

split_file_dir = path + '/split_result/'
print(split_file_dir)
join_file_path= path + '/join1.wav'


if __name__ == '__main__':
    countNum = 0
    for file in origin_file_list:
        if '.wav' in file:
            wav_tmp_path = origin_file_dir + '/' + file
            audio_split.CutFile(countNum, wav_tmp_path)
            countNum += 1

    tsm_start = 0.8
    tsm_end = 1.2
    tsm_step = 0.05
    for i in range(0,countNum):
        tsm_dir = split_file_dir + '/' + str(i)
        print(tsm_dir)
        for j in range(1, len(os.listdir(tsm_dir))):
            # if j % 4 == 0:
            #     print(j)
                for k in np.arange( tsm_start, tsm_end, tsm_step):
                    tsmtmp_wav = tsm_dir + '/' + str(i) + '_' + str(j) +'.wav'
                    audio_tsm.f_phasevoctor(tsmtmp_wav, k, tsm_dir)
                    audio_tsm.f_ola(tsmtmp_wav, k, tsm_dir)
                    audio_tsm.f_wsola(tsmtmp_wav, k, tsm_dir)


    #     audio_tsm.f_phasevoctor(file_test, i)
    # file_test = './ola1.0_1.wav'
    # audio_split.CutFile(file_test)
    # for i in np.arange(0.75, 1.5, 0.25):
    #     audio_tsm.f_phasevoctor(file_test, i)
    # audio_join.Joinfile(split_file_dir)
    # result = audio_asr.baidu_asr(join_file_path)
 #   print(result)
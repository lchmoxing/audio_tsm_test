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

split_file_dir = path + '/result/'
join_file_path= path + '/join1.wav'


if __name__ == '__main__':
    countNum = 0
    for file in origin_file_list:
        if '.wav' in file:
            wav_tmp_path = origin_file_dir + '/' + file
            audio_split.CutFile(countNum, wav_tmp_path)
            countNum += 1

    tsm_start = 0.75
    tsm_end = 1.5
    tsm_step = 0.25
#    for i in np.arange( tsm_start, tsm_end, tsm_step):

    #     audio_tsm.f_phasevoctor(file_test, i)
    # file_test = './ola1.0_1.wav'
    # audio_split.CutFile(file_test)
    # for i in np.arange(0.75, 1.5, 0.25):
    #     audio_tsm.f_phasevoctor(file_test, i)
    # audio_join.Joinfile(split_file_dir)
    # result = audio_asr.baidu_asr(join_file_path)
 #   print(result)
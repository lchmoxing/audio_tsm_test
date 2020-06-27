import os
import numpy as np
import client

prefix = '/home/usslab/qinhong/deepspeech/speech_TSM/with_wake_words/'
for i in np.arange(0.25, 0.5, 0.25):
    for num in range(1, 10):
        audio_origin = '/home/usslab/qinhong/deepspeech/speech_TSM/without_wake_words/' + str(num) +'.wav'
        audio_phasevoctor = '/home/usslab/qinhong/deepspeech/speech_TSM/without_wake_words/phasevoctor'+ str(i) + '_' + str(num) +'.wav'
        audio_ola = '/home/usslab/qinhong/deepspeech/speech_TSM/without_wake_words/ola' + str(i) + '_' + str(num) +'.wav'
        audio_wsola = '/home/usslab/qinhong/deepspeech/speech_TSM/without_wake_words/wsola' + str(i) + '_' + str(num) +'.wav'

        # command = 'python client.py --model deepspeech-0.7.1-models.pbmm --scorer deepspeech-0.7.1-models.scorer --audio '+ prefix + wav
        command = 'python ./client.py --model /home/usslab/qinhong/deepspeech/deepspeech-0.7.1-models.pbmm --scorer /home/usslab/qinhong/deepspeech/deepspeech-0.7.1-models.scorer --audio '+ audio_phasevoctor
        print(command)
        os.system(command)
        # print(client.main())
# for wav in os.listdir(prefix):
#     if '.wav' in wav :
#         # command = 'python client.py --model deepspeech-0.7.1-models.pbmm --scorer deepspeech-0.7.1-models.scorer --audio '+ prefix + wav
#         command = 'python ./client.py --model /home/usslab/qinhong/deepspeech/deepspeech-0.7.1-models.pbmm --scorer /home/usslab/qinhong/deepspeech/deepspeech-0.7.1-models.scorer --audio '+ prefix + wav
#         print(command)
#         os.system(command)

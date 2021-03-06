from audiotsm import phasevocoder, ola, wsola
from audiotsm.io.wav import WavReader, WavWriter
import numpy as np

num = 0
for num  in range(0,121):
    num +=1
    # output_phasevoctor_half = 'C:/Users/73936/Desktop/voice_speech/dataset/phasevoctor0.5_' + str(num) +'.wav'
    # output_phasevoctor_one = 'C:/Users/73936/Desktop/voice_speech/dataset/phasevoctor1.0_' + str(num) +'.wav'
    # output_phasevoctor_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/dataset/phasevoctor1.5_' + str(num) +'.wav'
    # output_phasevoctor_twice = 'C:/Users/73936/Desktop/voice_speech/databset/phasevoctor2.0_' + str(num) +'.wav'
    for i in np.arange(0.5, 2.0, 0.25):
        i = round(i,2)
        input_filename = '/home/usslab/Documents/qinhong/dataset72916k/origin/' + str(num) +'.wav'
        output_phasevoctor = '/home/usslab/Documents/qinhong/dataset72916k/phasevoctor/' + str(num) + '_' + str(i) +'.wav'
        output_ola = '/home/usslab/Documents/qinhong/dataset72916k/ola/' + str(num) + '_' + str(i) +'.wav'
        output_wsola = '/home/usslab/Documents/qinhong/dataset72916k/wsola/' + str(num) + '_' + str(i) +'.wav'
        with WavReader(input_filename) as reader:
            print(num)
            print(i)
            with WavWriter(output_phasevoctor, reader.channels, reader.samplerate) as writer_phase:
                tsm = phasevocoder(reader.channels, speed=i)
                tsm.run(reader, writer_phase)
        with WavReader(input_filename) as reader:
            print(num)
            print(i)
            with WavWriter(output_ola, reader.channels, reader.samplerate) as writer_ola:
                tsm = ola(reader.channels, speed=i)
                tsm.run(reader, writer_ola)
        with WavReader(input_filename) as reader:
            print(num)
            print(i)
            with WavWriter(output_wsola, reader.channels, reader.samplerate) as writer_wsola:
                tsm = wsola(reader.channels, speed=i)
                tsm.run(reader, writer_wsola)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_phasevoctor_half, reader.channels, reader.samplerate) as writer:
    #         tsm = phasevocoder(reader.channels, speed=0.5)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_phasevoctor_one, reader.channels, reader.samplerate) as writer:
    #         tsm = phasevocoder(reader.channels, speed=1.0)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_phasevoctor_oneandhalf, reader.channels, reader.samplerate) as writer:
    #         tsm = phasevocoder(reader.channels, speed=1.5)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_phasevoctor_twice, reader.channels, reader.samplerate) as writer:
    #         tsm = phasevocoder(reader.channels, speed=2.0)
    #         tsm.run(reader, writer)
            
    # output_ola_half = 'C:/Users/73936/Desktop/voice_speech/dataset/ola0.5_' + str(num) +'.wav'
    # output_ola_one = 'C:/Users/73936/Desktop/voice_speech/dataset/ola1.0_' + str(num) +'.wav'
    # output_ola_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/dataset/ola1.5_' + str(num) +'.wav'
    # output_ola_twice = 'C:/Users/73936/Desktop/voice_speech/dataset/ola2.0_' + str(num) +'.wav'
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_ola_half, reader.channels, reader.samplerate) as writer:
    #         tsm = ola(reader.channels, speed=0.5)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_ola_one, reader.channels, reader.samplerate) as writer:
    #         tsm = ola(reader.channels, speed=1.0)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_ola_oneandhalf, reader.channels, reader.samplerate) as writer:
    #         tsm = ola(reader.channels, speed=1.5)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_ola_twice, reader.channels, reader.samplerate) as writer:
    #         tsm = ola(reader.channels, speed=2.0)
    #         tsm.run(reader, writer)
    # output_wsola_half = 'C:/Users/73936/Desktop/voice_speech/dataset/wsola0.5_' + str(num) +'.wav'
    # output_wsola_one = 'C:/Users/73936/Desktop/voice_speech/dataset/wsola1.0_' + str(num) +'.wav'
    # output_wsola_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/dataset/wsola1.5_' + str(num) +'.wav'
    # output_wsola_twice = 'C:/Users/73936/Desktop/voice_speech/dataset/wsola2.0_' + str(num) +'.wav'
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_wsola_half, reader.channels, reader.samplerate) as writer:
    #         tsm = ola(reader.channels, speed=0.5)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_wsola_one, reader.channels, reader.samplerate) as writer:
    #         tsm = ola(reader.channels, speed=1.0)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_wsola_oneandhalf, reader.channels, reader.samplerate) as writer:
    #         tsm = ola(reader.channels, speed=1.5)
    #         tsm.run(reader, writer)
    # with WavReader(input_filename) as reader:
    #     print(num)
    #     with WavWriter(output_wsola_twice, reader.channels, reader.samplerate) as writer:
    #         tsm = ola(reader.channels, speed=2.0)
    #         tsm.run(reader, writer)

print("Successfully")
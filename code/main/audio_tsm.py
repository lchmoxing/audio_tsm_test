from audiotsm import phasevocoder, ola, wsola
from audiotsm.io.wav import WavReader, WavWriter
import numpy as np
import os

def f_phasevoctor(input_filename,i, tsm_dir):
    dir = tsm_dir + '/phasevoctor'
  #  print(dir)
    if not os.path.exists(dir):
        os.mkdir(dir)
    i = round(i,2)
    output_phasevoctor = dir + '/' + str(i) + '.wav'
  #  print(output_phasevoctor)
    with WavReader(input_filename) as reader:
#        print(i)
        with WavWriter(output_phasevoctor, reader.channels, reader.samplerate) as writer_phase:
            tsm = phasevocoder(reader.channels, speed=i)
            tsm.run(reader, writer_phase)
    print("PVTSM Run Over")

def f_ola(input_filename,i, tsm_dir):
    dir = tsm_dir +'/ola'
    if not os.path.exists(dir):
        os.mkdir(dir)
    i = round(i,2)
    output_ola = dir + '/' + str(i) + '.wav'
    with WavReader(input_filename) as reader:
#        print(i)
        with WavWriter(output_ola, reader.channels, reader.samplerate) as writer_ola:
            tsm = ola(reader.channels, speed=i)
            tsm.run(reader, writer_ola)

def f_wsola(input_filename,i,tsm_dir):
    dir = tsm_dir +'/wsola'
    if not os.path.exists(dir):
        os.mkdir(dir)
    i = round(i,2)
    output_wsola = dir + '/'  + str(i) + '.wav'
    with WavReader(input_filename) as reader:
#        print(i)
        with WavWriter(output_wsola, reader.channels, reader.samplerate) as writer_wsola:
            tsm = wsola(reader.channels, speed=i)
            tsm.run(reader, writer_wsola)


if __name__ == '__main__':
    file = './ola0.5_1.wav'
    for i in np.arange(0.75, 1.5, 0.25):
        f_phasevoctor(file, i)
    print("Run Over")
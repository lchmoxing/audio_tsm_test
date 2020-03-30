import matplotlib.pyplot as plt
import thinkdsp
import thinkplot
import numpy as np

def waveform1(audio_type):
    ### the same audio and the same algorithm, origin and 11 different audio speed
    for num in range(0,10):
        num +=1
        plt.figure(num)
        plt.title("phasecotor_1")
        ax = plt.subplot(3, 4, 1)
        ax.set_title("origin")
        audio_origin = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) + '.wav'
        wave=thinkdsp.read_wave(audio_origin)
        wave.plot()
        for i in np.arange(0.25, 3.0, 0.25):
            n = int(i/0.25 +1)
            ax = plt.subplot(3, 4, n)
            ax.set_title('%.2f' % i)
            audio = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/' + str(audio_type) + str(i) + '_' + str(num) +'.wav'
            wave=thinkdsp.read_wave(audio)
            wave.plot()
            plt.tight_layout()
            # audio_ola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/ola' + str(i) + '_' + str(num) +'.wav'
            # audio_wsola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/wsola' + str(i) + '_' + str(num) +'.wav'
        plt.savefig('C:/github_code/audio_tsm_test/audio_plot/waveform/differentspeed/' + str(audio_type) + '_' + str(num) + '.png')
        plt.clf()
def waveform2():
    ### the same audio and the speed, origin and 3 different algorithm
    for num in range(0,10):
        num +=1
        # plt.figure(num)
        # plt.title("phasecotor_1")
        for i in np.arange(0.25, 3.0, 0.25):
            # n = int(i/0.25 +1)
            ax = plt.subplot(2, 2, 1)
            ax.set_title("origin")
            audio_origin = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) + '.wav'
            wave=thinkdsp.read_wave(audio_origin)
            wave.plot()
            ax = plt.subplot(2, 2, 2)
            ax.set_title("phasevoctor")
            audio_phasevoctor = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/phasevoctor' + str(i) + '_' + str(num) +'.wav'
            wave=thinkdsp.read_wave(audio_phasevoctor)
            wave.plot()
            ax = plt.subplot(2, 2, 3)
            ax.set_title("ola")
            audio_ola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/ola' + str(i) + '_' + str(num) +'.wav'
            wave=thinkdsp.read_wave(audio_ola)
            wave.plot()
            ax = plt.subplot(2, 2, 4)
            ax.set_title("wsola")
            audio_wsola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/wsola' + str(i) + '_' + str(num) +'.wav'
            wave=thinkdsp.read_wave(audio_wsola)
            wave.plot()
            plt.tight_layout()           
            plt.savefig('C:/github_code/audio_tsm_test/audio_plot/waveform/differentalgorithm/' + str(i) + '_' + str(num) + '.png')
            plt.clf()

def wavespectrum1(audio_type):
    ### the same audio and the same algorithm, origin and 11 different audio speed
    for num in range(0,10):
        num +=1
        plt.figure(num)
        # plt.title("phasecotor_1")
        ax = plt.subplot(3, 4, 1)
        ax.set_title("origin")
        audio_origin = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) + '.wav'
        wave = thinkdsp.read_wave(audio_origin)
        spectrum = wave.make_spectrum()
        spectrum.plot()
        # thinkplot.show()
        for i in np.arange(0.25, 3.0, 0.25):
            n = int(i/0.25 +1)
            ax = plt.subplot(3, 4, n)
            ax.set_title('%.2f' % i)
            audio = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/' + str(audio_type) + str(i) + '_' + str(num) +'.wav'
            wave = thinkdsp.read_wave(audio)
            spectrum = wave.make_spectrum()
            spectrum.plot()
            plt.tight_layout()
            # audio_ola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/ola' + str(i) + '_' + str(num) +'.wav'
            # audio_wsola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/wsola' + str(i) + '_' + str(num) +'.wav'
        plt.savefig('C:/github_code/audio_tsm_test/audio_plot/spectrum/differentspeed/' + str(audio_type) + '_' + str(num) + '.png')
        plt.clf()

    # wave=thinkdsp.read_wave('C:/Users/73936/Desktop/voice_speech/dataset/1.wav')
    # spectrum=wave.make_spectrum()
    # spectrum.plot()
    # thinkplot.show()

def wavespectrum2():
    ### the same audio and the speed, origin and 3 different algorithm
    for num in range(0,10):
        num +=1
        # plt.figure(num)
        # plt.title("phasecotor_1")
        for i in np.arange(0.25, 3.0, 0.25):
            # n = int(i/0.25 +1)
            ax = plt.subplot(2, 2, 1)
            ax.set_title("origin")
            audio_origin = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) + '.wav'
            wave=thinkdsp.read_wave(audio_origin)
            spectrum = wave.make_spectrum()
            spectrum.plot()
            ax = plt.subplot(2, 2, 2)
            ax.set_title("phasevoctor")
            audio_phasevoctor = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/phasevoctor' + str(i) + '_' + str(num) +'.wav'
            wave=thinkdsp.read_wave(audio_phasevoctor)
            spectrum = wave.make_spectrum()
            spectrum.plot()
            ax = plt.subplot(2, 2, 3)
            ax.set_title("ola")
            audio_ola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/ola' + str(i) + '_' + str(num) +'.wav'
            wave=thinkdsp.read_wave(audio_ola)
            spectrum = wave.make_spectrum()
            spectrum.plot()
            ax = plt.subplot(2, 2, 4)
            ax.set_title("wsola")
            audio_wsola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/wsola' + str(i) + '_' + str(num) +'.wav'
            wave=thinkdsp.read_wave(audio_wsola)
            spectrum = wave.make_spectrum()
            spectrum.plot()
            plt.tight_layout()           
            plt.savefig('C:/github_code/audio_tsm_test/audio_plot/spectrum/differentalgorithm/' + str(i) + '_' + str(num) + '.png')
            plt.clf()

waveform1("phasevoctor")
waveform1("ola")
waveform1("wsola")
waveform2()
wavespectrum1("phasevoctor")
wavespectrum1("ola")
wavespectrum1("wsola")
wavespectrum2()
print("successfully!")


# wave=thinkdsp.read_wave(filename)
# wave.plot()
# plt.show()
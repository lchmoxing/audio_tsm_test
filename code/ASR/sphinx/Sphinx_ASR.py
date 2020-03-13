#/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

from pydub import AudioSegment
import numpy as np
# obtain audio from the microphone
r = sr.Recognizer()
###speech from microphone
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
# audio_file = r'C:/Users/73936/Desktop/voice_speech/english.wav'
# song = AudioSegment.from_wav(audio_file)
# song.export("audio.wav", format = "wav")
# with sr.AudioFile('audio.wav') as source:
#     audio = r.record(source)
#     print(audio) 

# with sr.AudioFile(audio_file) as source:
#     audio = r.record(source)
#     print(audio)

# recognize speech using Sphinx
def sphinx_asr(audio, filename):
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        with open(filename, 'a') as file_object:
            file_object.write(r.recognize_sphinx(audio) + '\n')
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        with open(filename, 'a') as file_object:
            file_object.write("Sphinx could not understand audio!" + '\n')
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
        with open(filename, 'a') as file_object:
            file_object.write("Sphinx error." + '\n')

# recognize speech using Google Speech Recognition
def google_asr(audio, filename):
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        with open(filename, 'a') as file_object:
            file_object.write(r.recognize_google(audio) + '\n')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        with open(filename, 'a') as file_object:
            file_object.write("Google Speech Recognition could not understand audio!" + '\n')
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        with open(filename, 'a') as file_object:
            file_object.write("Could not request results from Google Speech Recognition service." + '\n')

# sphinx_asr(audio, filename)
num = 0
for num in range(0, 10):
    num +=1
    audio_origin = 'C:/github_code/audio_tsm_test/dataset/speech_origin/without_wake_words/' + str(num) +'.wav'
    sphinx_asr_origin = 'C:/github_code/audio_tsm_test/test_result/sphinx/without_wake_words/sphinx_origin.txt'
    with sr.AudioFile(audio_origin) as source:
        audio = r.record(source)
        print(audio)
        sphinx_asr(audio, sphinx_asr_origin)
        # google_asr(audio, google_asr_origin)
    for i in np.arange(0.25, 3.0, 0.25):
        # audio_origin = 'C:/Users/73936/Desktop/voice_speech/dataset/' + str(num) +'.wav'
        # audio_phasevoctor = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/phasevoctor' + str(i) + '_' + str(num) +'.wav'
        # audio_ola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/ola' + str(i) + '_' + str(num) +'.wav'
        # audio_wsola = 'C:/github_code/audio_tsm_test/dataset/march_speech_tsm/wsola' + str(i) + '_' + str(num) +'.wav'

        # sphinx_asr_origin = 'C:/github_code/audio_tsm_test/test_result/sphinx_origin.txt'
        # # google_asr_origin = 'C:/github_code/audio_tsm_test/test_result/google_origin.txt'
        # sphinx_asr_phasevoctor = 'C:/github_code/audio_tsm_test/test_result/sphinx/sphinx_asr_phasevoctor' + str(i) + '.txt'
        # sphinx_asr_ola = 'C:/github_code/audio_tsm_test/test_result/sphinx/sphinx_asr_ola' + str(i) + '.txt'
        # sphinx_asr_wsola = 'C:/github_code/audio_tsm_test/test_result/sphinx/sphinx_asr_wsola' + str(i) + '.txt'


        
        audio_phasevoctor = 'C:/github_code/audio_tsm_test/dataset/without_speech_tsm/phasevoctor' + str(i) + '_' + str(num) +'.wav'
        audio_ola = 'C:/github_code/audio_tsm_test/dataset/without_speech_tsm/ola' + str(i) + '_' + str(num) +'.wav'
        audio_wsola = 'C:/github_code/audio_tsm_test/dataset/without_speech_tsm/wsola' + str(i) + '_' + str(num) +'.wav'

        # google_asr_origin = 'C:/github_code/audio_tsm_test/test_result/google_origin.txt'
        sphinx_asr_phasevoctor = 'C:/github_code/audio_tsm_test/test_result/sphinx/without_wake_words/sphinx_asr_phasevoctor' + str(i) + '.txt'
        sphinx_asr_ola = 'C:/github_code/audio_tsm_test/test_result/sphinx/without_wake_words/sphinx_asr_ola' + str(i) + '.txt'
        sphinx_asr_wsola = 'C:/github_code/audio_tsm_test/test_result/sphinx/without_wake_words/sphinx_asr_wsola' + str(i) + '.txt'
        # sphinx_asr_phasevoctor_half = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_phasevoctor0.5.txt'
        # sphinx_asr_phasevoctor_one = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_phasevoctor1.0.txt'
        # sphinx_asr_phasevoctor_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_phasevoctor1.5.txt'
        # sphinx_asr_phasevoctor_twice = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_phasevoctor2.0.txt'
        # sphinx_asr_ola_half = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_ola0.5.txt'
        # sphinx_asr_ola_one = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_ola1.0.txt'
        # sphinx_asr_ola_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_ola1.5.txt'
        # sphinx_asr_ola_twice = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_ola2.0.txt'
        # sphinx_asr_wsola_half = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_wsola0.5.txt'
        # sphinx_asr_wsola_one = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_wsola1.0.txt'
        # sphinx_asr_wsola_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_wsola1.5.txt'
        # sphinx_asr_wsola_twice = 'C:/Users/73936/Desktop/voice_speech/test_result/sphinx/sphinx_asr_wsola2.0.txt'

        # google_asr_phasevoctor_half = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_phasevoctor0.5.txt'
        # google_asr_phasevoctor_one = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_phasevoctor1.0.txt'
        # google_asr_phasevoctor_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_phasevoctor1.5.txt'
        # google_asr_phasevoctor_twice = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_phasevoctor2.0.txt'
        # google_asr_ola_half = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_ola0.5.txt'
        # google_asr_ola_one = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_ola1.0.txt'
        # google_asr_ola_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_ola1.5.txt'
        # google_asr_ola_twice = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_ola2.0.txt'
        # google_asr_wsola_half = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_wsola0.5.txt'
        # google_asr_wsola_one = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_wsola1.0.txt'
        # google_asr_wsola_oneandhalf = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_wsola1.5.txt'
        # google_asr_wsola_twice = 'C:/Users/73936/Desktop/voice_speech/test_result/google/google_asr_wsola2.0.txt'


        with sr.AudioFile(audio_phasevoctor) as source:
            audio = r.record(source)
            print(audio)
            sphinx_asr(audio, sphinx_asr_phasevoctor)
            # google_asr(audio, google_asr_phasevoctor)
        with sr.AudioFile(audio_ola) as source:
            audio = r.record(source)
            print(audio)
            sphinx_asr(audio, sphinx_asr_ola)
            # google_asr(audio, google_asr_phasevoctor)
        with sr.AudioFile(audio_wsola) as source:
            audio = r.record(source)
            print(audio)
            sphinx_asr(audio, sphinx_asr_wsola)
            # google_asr(audio, google_asr_phasevoctor)

        # with sr.AudioFile(audio_origin) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_origin)
        #     google_asr(audio, google_asr_origin)

        # with sr.AudioFile(audio_phasevoctor_half) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_phasevoctor_half)
        #     google_asr(audio, google_asr_phasevoctor_half)
        # with sr.AudioFile(audio_phasevoctor_one) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_phasevoctor_one)
        #     google_asr(audio, google_asr_phasevoctor_one)
        # with sr.AudioFile(audio_phasevoctor_oneandhalf) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_phasevoctor_oneandhalf)
        #     google_asr(audio, google_asr_phasevoctor_oneandhalf)
        # with sr.AudioFile(audio_phasevoctor_twice) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_phasevoctor_twice)
        #     google_asr(audio, google_asr_phasevoctor_twice)

        # with sr.AudioFile(audio_ola_half) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_ola_half)
        #     google_asr(audio, google_asr_ola_half)
        # with sr.AudioFile(audio_ola_one) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_ola_one)
        #     google_asr(audio, google_asr_ola_one)
        # with sr.AudioFile(audio_ola_oneandhalf) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_ola_oneandhalf)
        #     google_asr(audio, google_asr_ola_oneandhalf)
        # with sr.AudioFile(audio_ola_twice) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_ola_twice)
        #     google_asr(audio, google_asr_ola_twice)

        # with sr.AudioFile(audio_wsola_half) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_wsola_half)
        #     google_asr(audio, google_asr_wsola_half)
        # with sr.AudioFile(audio_ola_one) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_wsola_one)
        #     google_asr(audio, google_asr_wsola_one)
        # with sr.AudioFile(audio_wsola_oneandhalf) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_wsola_oneandhalf)
        #     google_asr(audio, google_asr_wsola_oneandhalf)
        # with sr.AudioFile(audio_wsola_twice) as source:
        #     audio = r.record(source)
        #     print(audio)
        #     sphinx_asr(audio, sphinx_asr_wsola_twice)
        #     google_asr(audio, google_asr_wsola_twice)


# # recognize speech using Google Cloud Speech
# GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
# try:
#     print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
# except sr.UnknownValueError:
#     print("Google Cloud Speech could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Cloud Speech service; {0}".format(e))

# # recognize speech using Wit.ai
# WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
# try:
#     print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
# except sr.UnknownValueError:
#     print("Wit.ai could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Wit.ai service; {0}".format(e))

# # recognize speech using Microsoft Bing Voice Recognition
# BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
# except sr.UnknownValueError:
#     print("Microsoft Bing Voice Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# # recognize speech using Microsoft Azure Speech
# AZURE_SPEECH_KEY = "INSERT AZURE SPEECH API KEY HERE"  # Microsoft Speech API keys 32-character lowercase hexadecimal strings
# try:
#     print("Microsoft Azure Speech thinks you said " + r.recognize_azure(audio, key=AZURE_SPEECH_KEY))
# except sr.UnknownValueError:
#     print("Microsoft Azure Speech could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Microsoft Azure Speech service; {0}".format(e))

# # recognize speech using Houndify
# HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
# HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
# try:
#     print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
# except sr.UnknownValueError:
#     print("Houndify could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Houndify service; {0}".format(e))

# # recognize speech using IBM Speech to Text
# IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
# IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
# try:
#     print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
# except sr.UnknownValueError:
#     print("IBM Speech to Text could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from IBM Speech to Text service; {0}".format(e))

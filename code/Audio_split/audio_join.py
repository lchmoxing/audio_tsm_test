import os
from pydub import AudioSegment

path = os.path.abspath('.')
print(path)
file_dir = path + '/result/'

#get file's name
file_list = []
join_sound_lists = AudioSegment.empty()

for i in range(len(os.listdir(file_dir))):
    filename = path+'/result/testresult' + str(i+1) + '.wav'
    join_sound_lists += AudioSegment.from_wav(filename)
join_sound_lists.export("join1.wav", format="wav")
# for file in os.listdir(file_dir):
#     file_list.append(os.path.join(file_dir, file))
#print(file_list)

# for file in file_list:
#     print(file)
#     join_sound_lists += AudioSegment.from_wav(file)
#print(type(join_sound_lists))
# join_sound_lists.export("join1.wav", format="wav")
'''
#get the audio files
sounds = []
for file in file_list:
    sounds.append(AudioSegment.from_wav(file))

join_sound_lists = AudioSegment.empty()
for sound in sounds:
    join_sound_lists += sound
print(type(join_sound_lists))
'''
#join_sound_lists.export("join.wav", format="wav")
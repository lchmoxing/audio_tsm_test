import os
from pydub import AudioSegment

def Joinfile(file_dir):
    join_sound_lists = AudioSegment.empty()
    for i in range(len(os.listdir(file_dir))):
        filename = file_dir + '/testresult' + str(i + 1) + '.wav'
        join_sound_lists += AudioSegment.from_wav(filename)
    join_sound_lists.export("join1.wav", format="wav")
    print("Join Run Over")
if __name__ == '__main__':
    Joinfile(file_dir)
    print("Run Over")


# for file in os.listdir(file_dir):
#     file_list.append(os.path.join(file_dir, file))
#print(file_list)

# for file in file_list:
#     print(file)
#     join_sound_lists += AudioSegment.from_wav(file)
#print(type(join_sound_lists))
# join_sound_lists.export("join1.wav", format="wav")

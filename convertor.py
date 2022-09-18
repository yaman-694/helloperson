from os import path
from pydub import AudioSegment

# files
url = 'https://sync.api.cloudconvert.com/v2/jobs'

with open(r"D:\OneDrive - Amity University\Documents\Sound Recordings\Recording (2).m4a", 'rb') as wav:

src = input("In: ")
dst = input("Out: ")

# convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
from pydub import AudioSegment
m4a_audio = AudioSegment.from_file("Recording.m4a", format="m4a")
m4a_audio.export("audio1.wav", format="wav")


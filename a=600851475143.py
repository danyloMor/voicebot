import os
import speech_recognition as sr
import soundfile as sf
from pydub import AudioSegment
from pydub.playback import play
src=r"C:\Users\MOROZ\Desktop\voices\1.ogg"
dst=r'C:\Users\MOROZ\Desktop\voices\1.wav'
sound=AudioSegment.from_ogg(src)
sound.export(dst, format='wav')
r = sr.Recognizer()
harvard = sr.AudioFile(r'C:\Users\MOROZ\Desktop\voices\1.wav')
if "1.wav".endswith('.wav'):
    with harvard as source:
            audio = r.record(source)
text=r.recognize_google(audio,key=None,language='ru-RU')
file = open(r"C:\Users\MOROZ\Desktop\voices\1.txt", "w")
file.write(text)
file.close()
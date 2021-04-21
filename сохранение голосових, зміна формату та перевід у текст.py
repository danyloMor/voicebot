import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import soundfile as sf
n=1
path = ("voices")
for file in os.listdir("voices"):
    if file.endswith(".ogg"):
        n=str(n)
        src=path+'/'+file
        dst=path+'/'+n+".wav"
        sound=AudioSegment.from_ogg(src)
        sound.export(dst, format='wav')
        os.remove(path+'/'+file)
        n=int(n)
        n+=1
    else:
        continue
n=1
for file in os.listdir("voices"):
    n=str(n)
    r = sr.Recognizer()
    harvard = sr.AudioFile('voices/'+file)
    if file.endswith('.wav'):
        with harvard as source:
            audio = r.record(source)
            text=r.recognize_google(audio,key=None,language='ru-RU')
            file = open(path+"/"+n+".txt", "w")
            file.write(text)
            file.close()
    n=int(n)
    n+=1
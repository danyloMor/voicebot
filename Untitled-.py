import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import soundfile as sf
path, dirs, files = next(os.walk(r"C:\Users\MOROZ\Desktop\voices"))
file_count = len(files)
n=1
path = (r"C:\Users\MOROZ\Desktop\voices")
for file in os.listdir(r"C:\Users\MOROZ\Desktop\voices"):
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
for file in os.listdir(r"C:\Users\MOROZ\Desktop\voices"):
    n=str(n)
    r = sr.Recognizer()
    harvard = sr.AudioFile('C:/Users/MOROZ/Desktop/voices/'+file)
    if file.endswith('.wav'):
        with harvard as source:
            audio = r.record(source)
            text=r.recognize_google(audio,key=None,language='ru-RU')
            file = open(path+"/"+n+".txt", "w")
            file.write(text)
            file.close()
    n=int(n)
    n+=1
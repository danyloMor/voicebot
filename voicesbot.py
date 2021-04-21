import os
import telebot
import requests
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import soundfile as sf
bot = telebot.TeleBot('1691365384:AAGlZLcR_i4UKT4htvp66LcGhI6eSi3t4Ho')
@bot.message_handler(content_types=['voice'])
def get_text_messages(message):
    if message.voice:
        i=message.id
        cid = message.chat.id
        path = ("voices/")
        n=1
        n=str(n)
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('voices/' + n + '.ogg', 'wb') as new_file:
            new_file.write(downloaded_file)
        for file in os.listdir("voices"):
            if file.endswith(".ogg"):
                n=str(n)
                src=path+file
                dst=path+n+".wav"
                sound=AudioSegment.from_ogg(src)
                sound.export(dst, format='wav')
                os.remove(path + file)
                n=int(n)
                n+=1
            else:
                continue
    else:
        bot.send_message(chat_id=cid, text="send me a voice")       
    n=1
    for file in os.listdir("voices"):
        n=str(n)
        r = sr.Recognizer()
        harvard = sr.AudioFile(path + file)
        if file.endswith('.wav'):
            with harvard as source:
                audio = r.record(source)
                text=r.recognize_google(audio,key=None,language='ru-RU')
                bot.send_message(chat_id=cid,reply_to_message_id=i, text=text)
    for file in os.listdir("voices"):
        if file.endswith('.wav'):
            os.remove(path + file)
    n=int(n)
    n+=1
bot.polling(none_stop=True, interval=0)

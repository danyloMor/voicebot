import os
import telebot
import requests
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import soundfile as sf
from time import time
bot = telebot.TeleBot('1691365384:AAGlZLcR_i4UKT4htvp66LcGhI6eSi3t4Ho')
@bot.message_handler(content_types=['voice'])
def get_text_messages(message):
    if message.voice:
        n=1
        n=str(n)
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('voices/' + n + '.ogg', 'wb') as new_file:
            new_file.write(downloaded_file)
bot.polling(none_stop=True, interval=0)

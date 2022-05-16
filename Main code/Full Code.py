from pytube import YouTube
import os
import subprocess
import telebot
import time
from threading import Thread
import re
token = '5365565899:AAF-y6x0Mke_ESblkVk7RXthMGCam99_sFQ'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!!\n'
                                      '\n'
                                      'Чтобы скачать музыку с YouTube - отправьте ссылку на видео.')


def timer(message, a):
    global val
    val = True
    link = a
    i=0
    while val == True:
        time.sleep(1)
        i+=1
        bot.edit_message_text(chat_id=message.chat.id, message_id=a.message_id, text=f"Прошло {i} секунд. \n"
                                                                                     f"\n"
                                                                                     f"Скачиваю - {name}")

@bot.message_handler(commands=['download'])
def some_func(message, text, yt_var):
    global name
    global val
    global path
    try:
        yt = yt_var
        name = yt.title
        name_up = re.sub("[$|@|&|.|:|!|#|№|^|?|*|=|+|>|<|/|;|~|`|'|ﾉ]", "", name)
        path = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    except:
        val = False
        error_message(message)
    def convert_video_to_audio_ffmpeg(video_file, name_file, prevent_error):
        #try:
        ext = os.path.splitext(video_file)
        a = subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{name_file}.mp3"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
        if a == 1:
            b = subprocess.call(["ffmpeg", "-y", "-i", prevent_error, f"{name_file}.mp3"],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.STDOUT)
            if b == 1:
                subprocess.call(["ffmpeg", "-y", "-i", path, f"{name_file}.mp3"],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.STDOUT)
    vf = f"{path}"
    prev_er_vf = f"{path}"
    convert_video_to_audio_ffmpeg(vf, name_up, prev_er_vf)
    try:
        file_name_audio = f"{name_up}.mp3"
        audio = open(r'{0}'.format(file_name_audio), 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
        val = False
    except:
        val = False
        error_message(message)
    try:
        os.remove(vf)
        val = False
    except:
        pass
    try:
        os.remove(prev_er_vf)
        val = False
    except:
        pass
    os.remove(file_name_audio)
    val = False



def error_message(message):
    bot.send_message(message.chat.id, "Что-то пошло не так. \n"
                                      "Повторите попытку")

@bot.message_handler()
def any_message(message):
    text = message.text
    rev = 'https://www.youtube.com/'
    rev_second = "https://youtu.be/"
    if rev in text or rev_second in text:
        yt = YouTube(text)
        duration = yt.length
        if duration < 600:
            msg = bot.send_message(message.chat.id, 'Пожалуйста, подождите...')
            th = Thread(target=timer, args=(message, msg))
            th2 = Thread(target=some_func, args=(message, text, yt))
            th.start()
            th2.start()
            return
        elif duration >= 600:
            bot.send_message(message.chat.id, "Видео должно быть менее 10 минут.")
    else:
        bot.send_message(message.chat.id, text="Неправильная ссылка")

if __name__ == "__main__":
    print('We work')
    bot.polling()


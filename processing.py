import telebot
import pytube
import time
from threading import Thread
def any_message(message):
    text = message.text

    #correctness check

    rev = 'https://www.youtube.com/'
    rev_second = "https://youtu.be/"
    if rev in text or rev_second in text:

        #If the length of a video is more than 10 mins then we send the messsage of it

        yt = YouTube(text)
        duration = yt.length
        if duration < 600:

            #To run the timer we turn to Thread and make 2 branches (timer and the main process)
            #active at the same time.

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
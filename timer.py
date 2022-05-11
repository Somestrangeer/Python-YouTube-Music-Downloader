import telebot
import time


def timer(message, a):
    global val   #to control the finction
    val = True
    link = a
    i=0
    while val == True:
        time.sleep(1)
        i+=1
        bot.edit_message_text(chat_id=message.chat.id, message_id=a.message_id, text=f"Прошло {i} секунд. \n"
                                                                                     f"\n"
                                                                                     f"Скачиваю - {name}")
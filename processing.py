import telebot
import pytube
import time
from threading import Thread

@bot.message_handler()
def any_message(message):
	text = message.text
	correctLink1 = 'https://www.youtube.com/'
	correctLink2 = "https://youtu.be/"
	correctLin3 = "https://music.youtube.com/"

	if correctLink1 in text or correctLink2 in text or correctLin3 in text:
		try:
			yt = YouTube(text)
			duration = yt.length

			name = getSet()
			name.setName(yt.title)

			boolTimer = getSet()
			boolTimer.setBoolTimer(True)

			if duration < 600:
				user_id = getSet()
				user_id.setID(message.from_user.id)

				bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
				waitMsg = bot.send_message(message.chat.id, 'Пожалуйста, подождите...')

				checkPermission = primeSub().addUpdateUser(user_id)

				if checkPermission == True:
					threadOne = Thread(target=timer().start, args=(message, waitMsg, name, boolTimer))
					threadTwo = Thread(target=startDownloadVideo().Download, args=(message, text, yt, name, boolTimer))
					threadOne.start()
					threadTwo.start()
					return
				else:
					bot.delete_message(chat_id=message.chat.id, message_id=waitMsg.message_id)
					error_message(message)
					return
			else:
				bot.send_message(message.chat.id, text="Видео должно быть менее 10 минут")
		except:
			bot.send_message(message.chat.id, text="Некорректная ссылка")
	else:
	    bot.send_message(message.chat.id, text="Неправильная ссылка")

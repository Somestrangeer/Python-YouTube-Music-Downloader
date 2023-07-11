class timer:
	def start(self, message, waitMsg, name, boolTimer):
		seconds = 0
		self.name = name
		self.boolTimer = boolTimer
		while self.boolTimer.getBoolTimer() == True:
			time.sleep(1)
			seconds += 1
			bot.edit_message_text(chat_id=message.chat.id, message_id=waitMsg.message_id, text=f"Прошло {seconds} секунд. \n"
																							f"\n"
																							f"Скачиваю - {self.name.getName()}")
		bot.delete_message(chat_id=message.chat.id, message_id=waitMsg.message_id)

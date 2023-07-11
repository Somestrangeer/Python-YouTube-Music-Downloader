import telebot
import subprocess
import os
import re
import pytube

class startDownloadVideo:
	@bot.message_handler(commands=['download'])
	def Download(self, message, text, yt, name, boolTimer):
		self.path = getSet()

		self.path.setPath(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download())

		self.audioFile = f"{name.getName()}.mp3"
		subprocess.call(["ffmpeg", "-i", self.path.getPath(), self.audioFile])

		bot.send_audio(message.chat.id, audio=open(self.audioFile, 'rb'), title=self.audioFile.replace(".mp3", ''))
		boolTimer.setBoolTimer(False)
		os.remove(self.audioFile)
		os.remove(self.path.getPath())

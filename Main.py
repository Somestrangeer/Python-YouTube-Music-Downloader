import telebot
import subprocess
import os
import re
import pytube


def some_func(message, text, yt_var):
    global name #make it global to schow a title to a user
    global val #make it global to close or finish the loop
    try:
        yt = yt_var
        name = yt.title #We get a video's name
        name_up = re.sub("[$|@|&|.|:|!|#|№|^|?|*|=|+|>|<|/|;|~|`|']", "", name) #We make the title more correct

        #We download a video

        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    except:

        #If we get an error, we close the loop and redirect to other function

        val = False
        error_message(message)
    def convert_video_to_audio_ffmpeg(video_file, name_file, output_ext="mp3"):
        try:
            ext = os.path.splitext(video_file)
            subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{name_file}.{output_ext}"],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.STDOUT)
        except:
            val = False
            error_message(message)

    vf = f'{name_up}.mp4'
    convert_video_to_audio_ffmpeg(vf, name_up)
    try:
        file_name_audio = f"{name_up}.mp3"
        audio = open(r'{0}'.format(file_name_audio), 'rb') #open converted file
        val = False    #finish the loop
        bot.send_audio(message.chat.id, audio) 
        audio.close()
        os.remove(vf)
        os.remove(file_name_audio)
    except:
        val = False
        error_message(message)
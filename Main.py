import telebot
import subprocess
import os
import re
import pytube


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

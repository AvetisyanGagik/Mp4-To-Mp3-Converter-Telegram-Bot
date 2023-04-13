from pytube import YouTube
import moviepy.editor
import telebot




def download_and_convert_to_mp3(link):
    # Download mp4 file
    global yt
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    # Try except isn't necessary
    try:
        yt.download()
    except:
        print("An error has occurred!!!")
    print("Success!!")

    # Converting to mp3
    video = moviepy.editor.VideoFileClip(f'{yt.title}.mp4')
    audio = video.audio
    audio.write_audiofile(f'{yt.title}.mp3')




# Start command
bot = telebot.TeleBot('Token')
@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.chat.id,'Hi, give me a link')

# Like echo
@bot.message_handler(func = lambda m: True)
def get_message(message):
    music_link = message.text
    download_and_convert_to_mp3(music_link)
    file = open(f'{yt.title}.mp3', 'rb')
    bot.send_audio(message.chat.id, file)


bot.polling(non_stop=True)



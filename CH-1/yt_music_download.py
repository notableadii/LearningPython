import yt_dlp
from colorama import Fore, Back, Style
from time import sleep

print(Fore.RED +'''
/$$     /$$ /$$$$$$$$       /$$$$$$$   /$$$$$$  /$$      /$$ /$$   /$$ /$$        /$$$$$$   /$$$$$$  /$$$$$$$ 
|  $$   /$$/|__  $$__/      | $$__  $$ /$$__  $$| $$  /$ | $$| $$$ | $$| $$       /$$__  $$ /$$__  $$| $$__  $$
 \  $$ /$$/    | $$         | $$  \ $$| $$  \ $$| $$ /$$$| $$| $$$$| $$| $$      | $$  \ $$| $$  \ $$| $$  \ $$
  \  $$$$/     | $$         | $$  | $$| $$  | $$| $$/$$ $$ $$| $$ $$ $$| $$      | $$  | $$| $$$$$$$$| $$  | $$
   \  $$/      | $$         | $$  | $$| $$  | $$| $$$$_  $$$$| $$  $$$$| $$      | $$  | $$| $$__  $$| $$  | $$
    | $$       | $$         | $$  | $$| $$  | $$| $$$/ \  $$$| $$\  $$$| $$      | $$  | $$| $$  | $$| $$  | $$
    | $$       | $$         | $$$$$$$/|  $$$$$$/| $$/   \  $$| $$ \  $$| $$$$$$$$|  $$$$$$/| $$  | $$| $$$$$$$/
    |__/       |__/         |_______/  \______/ |__/     \__/|__/  \__/|________/ \______/ |__/  |__/|_______/                                                                                                       
      ''')

url = input(Fore.WHITE + "Paste the YouTube video link: ")
print(Fore.CYAN + "Processing the URL... Please wait.")
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(Fore.GREEN + "🎵 Audio downloaded as MP3!")
sleep(2)
print(Fore.RED + "Closing the program...")
sleep(2)
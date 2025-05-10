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
sleep(2)
# Ask user for YouTube link
url = input( Fore.WHITE + "Enter YouTube video URL: ")
print(Fore.CYAN + "Processing the URL... Please wait.")
# Set up download options
ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s'  # Saves the file with video title
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# print("🎉 Download complete!")
print(Fore.GREEN + "🎉 Video downloaded successfully!")
sleep(2)
print(Fore.RED + "Closing the program...")
sleep(2)
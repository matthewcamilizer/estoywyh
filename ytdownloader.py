import os
import sys

from pytube import YouTube
from colorama import init, Fore
from urllib.parse import urlparse
init()

def is_url(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme) ##if invalid, scheme will be empty and return false

while True:
    selected_video = input("YouTube URL:")
    if selected_video.lower() =="exit":
        sys.exit()
    if is_url(selected_video):
        break
    print(Fore.RED + "invalid URL, please enter a valid one. or enter " + Fore.BLUE + "exit" + Fore.RED + " to quit" + Fore.RESET)
    
while True:
    DOWNLOAD_FOLDER = input("enter folder to download:")
    if DOWNLOAD_FOLDER.lower() =="exit":
        sys.exit()
    if os.path.isdir(DOWNLOAD_FOLDER):
        break
    print(Fore.RED + "invalid folder, please enter a valid one. or enter " + Fore.BLUE + "exit" + Fore.RED + "  to quit" + Fore.RESET)
    
try:         
    video_obj = YouTube(selected_video)
    stream = video_obj.streams.filter(file_extension="mp4").get_highest_resolution()
    print('downloading...')
    stream.download(DOWNLOAD_FOLDER)
    print('\n\nfinished!\n\n')
    
except:
    print('\n\ndownload failed\n\n')
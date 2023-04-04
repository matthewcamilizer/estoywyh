import os
import sys
#pip install pytube#

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
    print("\n\n"+ "just see " + Fore.YELLOW + "'mime type'"  + Fore.RESET +  "and" +Fore.YELLOW + "'type'" + Fore.RESET + "in the given details" + "\n\n", video_obj.streams)
    file_type = print("\nwhich file type you wanna download? (please enter", end=" ")
    file_type = print(Fore.YELLOW + "video" + Fore.RESET, end=" ")
    file_type = print("or", end=" ")
    file_type = print(Fore.YELLOW + "audio" + Fore.RESET, end=" ")
    file_type = print("or enter", end=" ")
    file_type = print(Fore.YELLOW + "exit" + Fore.RESET, end=" ")
    file_type = print("to close)", end=" ")
    file_type = input().lower()
    
    if file_type == "video":
        print("\n\nwhich file format (this is", end=' ')
        print(Fore.YELLOW + "mime type"  + Fore.RESET +  " in the given details) you wanna download? (enter", end=' ')
        print(Fore.YELLOW + "mp4" + Fore.RESET, end=' ')
        print("or", end=' ')
        print(Fore.YELLOW + "webm" + Fore.RESET, end=' ')
        print("):", end=' ')
        file_format = input().lower()
        if file_format == "mp4":
            stream = video_obj.streams.filter(file_extension="mp4").get_highest_resolution()
        elif file_format == "webm":
            stream = video_obj.streams.filter(file_extension="webm").get_highest_resolution()
        elif file_format == "exit":
            sys.exit()
        else:
            print("please enter 'mp4' or 'webm', or enter ")
            print(Fore.YELLOW + "exit " + Fore.RESET)
            print("to close")
    elif file_type == "audio":
        print("\n\nwhich file format (this is", end=' ')
        print(Fore.YELLOW + "'mime type'"  + Fore.RESET +  " in the given details) you wanna download? (enter", end=' ')
        print(Fore.YELLOW + "mp4" + Fore.RESET, end=' ')
        print("or", end=' ')
        print(Fore.YELLOW + "webm" + Fore.RESET, end=' ')
        print("):", end=' ')
        file_format = input().lower()
        if file_format == "mp4":
            stream = video_obj.streams.filter(only_audio=True, file_extension="mp4").first()
        elif file_format == "webm":
            stream = video_obj.streams.filter(only_audio=True, file_extension="webm").first()
        elif file_format == "exit":
            sys.exit()
        else:
            print("please enter 'mp4' or 'webm', or enter ")
            print(Fore.YELLOW + "exit " + Fore.RESET)
            print("to close")
    print('downloading..., and the terminal will auto close after finishing')
    stream.download(DOWNLOAD_FOLDER)
    print('\n\nfinished!\n\n')
    
except:
    print('\n\ndownload failed\n\n')
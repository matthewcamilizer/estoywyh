import json, requests
from NCMGet import getSong

APIPath = "https://music.163.com/api/v3/playlist/detail?id="
reqAPI = input(r"enter your playlist here: ")
APIBase = reqAPI.find("playlist?id=")+len("playlist?id=")
getAPI = reqAPI[APIBase:]
req = APIPath + getAPI

tracks = json.loads(requests.get(req).text)['playlist']['trackIds']
title = json.loads(requests.get(req).text)['playlist']['name']
author = json.loads(requests.get(req).text)['playlist']['creator']['nickname']

songs = []
print("The playlist is: {} by {}\nAnd there are {} songs\n".format(title,author,len(tracks)))
while True:
    try:
        for count, t in enumerate(tracks, start=1):
            Songreq = "https://music.163.com/song?id={}".format(t['id'])
            print('Number: {}'.format(count))
            song_instance = getSong.get_song_instance(Songreq)
            print('URL: {}\n'.format(Songreq))
            songs.append(song_instance)
        print("\nLoad finished and the songs are\n")
        for r in songs:
            print(r)
        break
    except:
        print("\nError while loading and the {} songs are\n".format(len(songs)))
        for r in songs:
            print(r)
        break

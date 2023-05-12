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
print("The playlist is: {} by {}\nAnd the number of total song is: {}".format(title,author,len(tracks)))
while True:
    try:
        for t in tracks:
            Songreq = "https://music.163.com/song?id={}".format(t['id'])
            song_instance = getSong.get_song_instance(Songreq)
            songs.append(song_instance)
        print("load finished and the songs are")
        for r in songs:
            print(r)
        break
    except:
        print("error while loading and the songs are")
        for r in songs:
            print(r)
        break

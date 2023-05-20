import json, requests, os, datetime, re
from NCMGet import getSong

req=''
title=''
author=''
final=''
current_datetime = datetime.datetime.now()
ff=current_datetime.strftime('%Y-%m-%d')

#https://music.163.com/api/album/{}
SavePath = input("Enter the path to save logs, Leave blank if need no logs: ")
APIPath = "https://music.163.com/api/v3/playlist/detail?id="
ALBUMpath = "https://music.163.com/api/album/"
reqAPI = input(r"enter your URL here: ")
if "playlist" in reqAPI:
    req = APIPath + re.search(r"playlist\?id=([^\W]+)", reqAPI).group(1)
    tracks = json.loads(requests.get(req).text)['playlist']['trackIds']
    title = json.loads(requests.get(req).text)['playlist']['name']
    author = json.loads(requests.get(req).text)['playlist']['creator']['nickname']

if "album" in reqAPI:
    req = ALBUMpath+re.search(r"album\?id=([^\W]+)", reqAPI).group(1)
    print(requests.get(req).text)
    print(req)
    tracks = json.loads(requests.get(req).text)['album']['songs']
    title = json.loads(requests.get(req).text)['album']['name']
    author = json.loads(requests.get(req).text)['album']['artist']['name']


songs = []
FailedLoad =[]
print("\nThe playlist is: {} by {}\n\n{} songs\n".format(title,author,len(tracks)))

for count, t in enumerate(tracks, start=1):
    Songreq = "https://music.163.com/song?id={}".format(t['id'])
    print('Number: {}'.format(count))
    try:
        song_instance = getSong.get_song_instance(Songreq)
    except:
        print("Error while loading song of {}".format(Songreq))
        FailedLoad.append(Songreq)
        continue
    print('URL: {}\n'.format(Songreq))
    songs.append(song_instance)

if(len(songs) == len(tracks)):
    print("\nCongrats! All of the songs are here!\n")
else:
    print("\nPartly loaded. And {} of {} songs are:\n".format(len(songs), len(tracks)))
for r in songs:
    if SavePath:
        with open(os.path.join(SavePath, f"NCM exported {ff}.log"), 'a', encoding='utf-8') as e:
            e.write('\n'+r+'\n')
    print(r)
if FailedLoad:
    print("the failed URLs are here.")
    for ct, f in enumerate(FailedLoad, start=1):
        print("\n{}:\n{}".format(ct, f))
        if SavePath:
            with open(os.path.join(SavePath, f"NCM failed export {ff}.log"), 'a', encoding='utf-8') as e:
                e.write('\n'+f+'\n')

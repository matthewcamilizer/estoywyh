import json, requests, re
from QQGet import getSong

url = input(r'Enter URL: ')
getAPI=''
pattern = r"id=(.+)"
if "u?__=" in url:
    request = requests.get(url, allow_redirects=False)
    redPath = request.headers.get('location')
    match = re.search(pattern, redPath)
if "id=" in url:
    match = re.search(pattern, url)
getAPI = match.group(1)

req = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?cv=10000&ct=19&newsong=1&tpl=wk&id={}&g_tk=5381&platform=mac&g_tk_new_20200303=5381&loginUin=0&hostUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqspaframe.json&needNewCode=0".format(getAPI)
print(req)

tracks = json.loads(requests.get(req).text)['data']['cdlist'][0]['songlist']
title = json.loads(requests.get(req).text)['data']['cdlist'][0]['dissname']
author = json.loads(requests.get(req).text)['data']['cdlist'][0]['nick']

songs = []
print("The playlist is {} by {}\nAnd there are {} songs\n".format(title,author,len(tracks)))
while True:
    try:
        for count, t in enumerate(tracks, start=1):
            Songreq = "https://y.qq.com/n/ryqq/songDetail/{}".format(t['file']['media_mid'])
            print('Number: {}'.format(count))
            song_instance = getSong.get_song_instance(Songreq)
            print('URL: {}\n'.format(Songreq))
            songs.append(song_instance)
        print("\nCongrat! All of the songs are here!\n")
        for r in songs:
            print(r)
        break
    except:
        print("\nError while loading and the {} of {} songs are\n".format(len(songs),len(tracks)))
        for r in songs:
            print(r)
        break

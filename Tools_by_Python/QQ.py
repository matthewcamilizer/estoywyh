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
FailedLoad =[]
print("The playlist is {} by {}\nAnd there are {} songs\n".format(title,author,len(tracks)))

for count, t in enumerate(tracks, start=1):
    Songreq = "https://y.qq.com/n/ryqq/songDetail/{}".format(t['mid'])
    print('Number: {}'.format(count))
    try:
        song_instance = getSong.get_song_instance(Songreq)
    except:
        print("Load song {} failed!".format(t['name']))
        FailedLoad.append({"number":count,"song":t['name'],"artist":t['singer'][0]['name'], "URL":Songreq})
        continue
    print('URL: {}\n'.format(Songreq))
    songs.append(song_instance)
if(len(songs) == len(tracks)):
    print("\nCongrats! All of songs are here!")
else:
    print("\nPartly loaded. And the {} songs are:\n".format(len(songs)))
for r in songs:
    print(r)
if FailedLoad:
    print("\nthe following songs load failed: ")
    for f in FailedLoad:
        print("Number: {}\n{} - {}\nURL: {}".format(f["number"],f["artist"],f["song"],f["URL"] ))


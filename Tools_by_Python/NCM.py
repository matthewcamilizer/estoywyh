import sys
sys.dont_write_bytecode = True

import json, requests, os, datetime, re
from NCMGet import getSong
from NewFile import newfile

req=exp=SavePath=''
title=''
author=''
final=''
current_datetime = datetime.datetime.now()
ff=current_datetime.strftime('%Y-%m-%d')


reqAPI = input("\n"+r'输入网易云歌单链接: ')
EnterPath = input("\n"+r"如果需要导出记录, 请输入保存路径并按Enter(或直接按Enter跳过): ")
APIPath = "https://music.163.com/api/v3/playlist/detail?id="
ALBUMpath = "https://music.163.com/api/album/"
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

if EnterPath:
    exp=os.path.join(EnterPath, "歌单导出")
    if not os.path.exists(exp):
        os.mkdir(exp)
    NCM=os.path.join(exp, "网易云")
    if not os.path.exists(NCM):
        os.mkdir(NCM)
    SavePath=NCM

songs = []
FailedLoad =[]
Uris=[]
FailedUris=[]

try:
    for count, t in enumerate(tracks, start=1):
        Songreq = "https://music.163.com/song?id={}".format(t['id'])
        print(f"\n第{count}首: ")
        try:
            song_instance = getSong.get_song_instance(Songreq)
            Uris.append(Songreq)
        except:
            print("歌曲: {} 导出失败\n".format(Songreq))
            FailedLoad.append(Songreq)
            continue
        print('歌曲链接: {}\n'.format(Songreq))
        songs.append(song_instance)

    print("\n歌单: {} 作者: {}\n\n共有{}首歌\n".format(title,author,len(tracks)))
    if(len(songs) == len(tracks)):
        print(f"\n网易云歌单: {title} 的所有歌曲导出完成!\n")
    else:
        print("\n部分歌曲导出失败 已导出: {}首 歌曲总数: {}首\n".format(len(songs), len(tracks)))
    if SavePath:
        logFile=newfile(SavePath, f"网易云 - {author} 的 {title} {ff}.txt")
        for count, (r, u) in enumerate(zip(songs, Uris),start=1):
            with open(logFile, 'a', encoding='utf-8') as e:
                if e.tell()==0:
                    e.write(f"{ff}\n作者:{author}\n歌单:{title}\n链接:{reqAPI}\n\n")
                e.write(f"第{count}首:\n{r}\n{u}\n\n")

    if FailedLoad:
        print("导出失败歌曲的链接: ")
        for ct, f in enumerate(FailedLoad, start=1):
            print("\n第{}首:\n{}".format(ct, f))
        if SavePath:
            logFile=newfile(SavePath, f"网易云导出失败的歌单 - {title} - {author} {ff}.txt")
            for ct, f in enumerate(FailedLoad, start=1):
                with open(logFile, 'a', encoding='utf-8') as e:
                    if e.tell()==0:
                        e.write(f"{ff}\n作者: {author}\n歌单:{title}\n链接: {reqAPI}\n\n")
                    e.write(f"第{ct}首: {f}\n\n")

except Exception as e:
    print("出错啦!",e)
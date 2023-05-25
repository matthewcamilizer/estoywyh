import json, requests, re, os, datetime
from QQGet import getSong
from NewFile import newfile

current_datetime = datetime.datetime.now()
ff=current_datetime.strftime('%Y-%m-%d')


url = input("\n"+r'输入歌单链接: ')
EnterPath = input("\n"+r"如果需要导出记录, 请输入保存路径并按Enter(或直接按Enter跳过): ")
getAPI=SavePath=''
pattern = r"id=([^\W]+)"
pattern2 = r"playlist/([^\W]+)"
if "u?__=" in url:
    request = requests.get(url, allow_redirects=False)
    redPath = request.headers.get('location')
    getAPI = re.search(pattern, redPath).group(1)
if "playlist/" in url and not "id=" in url:
    getAPI = re.search(pattern2, url).group(1)
if "id=" in url and not "playlist/" in url:
    getAPI = re.search(pattern, url).group(1)



req = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?cv=10000&ct=19&newsong=1&tpl=wk&id={}&g_tk=5381&platform=mac&loginUin=0&hostUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqspaframe.json&needNewCode=0".format(getAPI)

tracks = json.loads(requests.get(req).text)['data']['cdlist'][0]['songlist']
title = json.loads(requests.get(req).text)['data']['cdlist'][0]['dissname']
author = json.loads(requests.get(req).text)['data']['cdlist'][0]['nick']


print("作者: {} 歌单: {}\n 有{}首歌\n".format(title,author,len(tracks)))
if EnterPath:
    exp=os.path.join(EnterPath, "歌单导出")
    if not os.path.exists(exp):
        os.mkdir(exp)
    QM=os.path.join(exp, "QQ音乐")
    if not os.path.exists(QM):
        os.mkdir(QM)
    SavePath=QM

try:
    songs=[]
    Uris=[]
    for count, t in enumerate(tracks, start=1):
        Songreq = "https://y.qq.com/n/ryqq/songDetail/{}".format(t['mid'])
        print('第{}个:'.format(count))
        song_instance = getSong.get_song_instance(Songreq)
        print('链接: {}\n'.format(Songreq))
        songs.append(song_instance)
        Uris.append(Songreq)
    if SavePath:
        logFile=newfile(SavePath, f"QQ音乐 - {author}的{title} {ff}.txt")
        for count, (s,u) in enumerate(zip(songs, Uris),start=1):
            with open(logFile, 'a', encoding='utf-8') as f:
                if f.tell()==0:
                    f.write(f"{ff}\n作者: {author}\n歌单: {title}\n链接: {url}\n\n")
                f.write(f"第{count}首:\n{s}\n{u}\n\n")
except Exception as e:
    print("出错啦!",e)
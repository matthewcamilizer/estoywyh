#-*- coding: utf-8 -*-
import requests, json, html, os, datetime, re, sys
from NewFile import newfile
from naming import Fuck
sys.dont_write_bytecode=True

def ExportQQ(url, EnterPath):
    dt=datetime.datetime.now()
    ff=dt.strftime('%Y-%m-%d')

    TitleFuck=[]
    AuthorFuck=[]
    sTitleFuck=[]
    sAuthorFuck=[]

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
    API = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?cv=10000&ct=19&newsong=1&tpl=wk&id={}&g_tk=5381&platform=mac&loginUin=0&hostUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqspaframe.json&needNewCode=0".format(getAPI)

    try:
        response=requests.get(API)
        req=html.unescape(response.text)
        soup = json.loads(req)
        track=soup['data']['cdlist'][0]
        Author=Fuck(track['nick'], AuthorFuck, sAuthorFuck)[0] #Fuck naming
        Title=Fuck(track['dissname'], TitleFuck, sTitleFuck)[0] #Fuck naming
        PlaylistURL=f"https://y.qq.com/n/ryqq/playlist/{track['disstid']}"
        rAuthor=track['nick']
        rTitle=track['dissname']
        Songs=track['songlist']
        Store_Artists=[]
        Store_Songs=[]
        Store_URL=[]

        if EnterPath:
            exp=os.path.join(EnterPath, "歌单导出")
            if not os.path.exists(exp):
                os.mkdir(exp)
            QM=os.path.join(exp, "QQ音乐")
            if not os.path.exists(QM):
                os.mkdir(QM)
            SavePath=QM

        for s in Songs:
            sa=[]
            artists=s['singer']
            for a in artists:
                sa.append(a['name'])
            Store_Artists.append(", ".join(sa))
            Store_Songs.append(s['name'])
            Store_URL.append(s['mid'])

        for count, (a, b,c ) in enumerate(zip(Store_Artists, Store_Songs, Store_URL), start=1):
            print(f"\n第{count}首:\n{a}  •  {b}\nhttps://y.qq.com/n/ryqq/songDetail/{c}\n")
            
        if SavePath:
            logFile=newfile(SavePath, f"QQ音乐 - {Author}的{Title} {ff}.txt")
            for count, (s,u) in enumerate(zip(Store_Songs, Store_URL),start=1):
                with open(logFile, 'a', encoding='utf-8') as f:
                    if f.tell()==0:
                        f.write(f"{ff}\n作者: {rAuthor}\n歌单: {rTitle}\n链接: {PlaylistURL}\n\n")
                        if TitleFuck or AuthorFuck:
                            f.write(f"\n因为如下符号不允许出现在文件名中''\\', '/', ':', '?', '*', '\"', '<', '>', '|'\n\n所以我统一替换为\u2022\n")
                            if TitleFuck:
                                f.write(f"因此歌单原名是 '{rTitle}', 而不是 '{rTitle}'\n替换的符号为{', '.join([fuck for fuck in sTitleFuck])}\n\n")
                            if AuthorFuck:
                                f.write(f"因此作者原名是 '{Author}', 而不是 '{rAuthor}'\n替换的符号为{', '.join([fuck for fuck in sAuthorFuck])}\n\n")
                    f.write(f"第{count}首:\n{s}\n{u}\n\n")
        print(f"\n\nQQ音乐: {Title}导出完成!\n共有{len(Store_Songs)}首歌\n")
    except Exception as e:
        print("出错啦!",e)

    dt=datetime.datetime.now()
    ff=dt.strftime('%Y-%m-%d')

    TitleFuck=[]
    AuthorFuck=[]
    sTitleFuck=[]
    sAuthorFuck=[]

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
    API = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_playlist_cp.fcg?cv=10000&ct=19&newsong=1&tpl=wk&id={}&g_tk=5381&platform=mac&loginUin=0&hostUin=0&format=json&inCharset=GB2312&outCharset=utf-8&notice=0&platform=jqspaframe.json&needNewCode=0".format(getAPI)

    try:
        response=requests.get(API)
        req=html.unescape(response.text)
        soup = json.loads(req)
        track=soup['data']['cdlist'][0]
        Author=Fuck(track['nick'], AuthorFuck, sAuthorFuck)[0] #Fuck naming
        Title=Fuck(track['dissname'], TitleFuck, sTitleFuck)[0] #Fuck naming
        PlaylistURL=f"https://y.qq.com/n/ryqq/playlist/{track['disstid']}"
        rAuthor=track['nick']
        rTitle=track['dissname']
        Songs=track['songlist']
        Store_Artists=[]
        Store_Songs=[]
        Store_URL=[]

        if EnterPath:
            exp=os.path.join(EnterPath, "歌单导出")
            if not os.path.exists(exp):
                os.mkdir(exp)
            QM=os.path.join(exp, "QQ音乐")
            if not os.path.exists(QM):
                os.mkdir(QM)
            SavePath=QM

        for s in Songs:
            sa=[]
            artists=s['singer']
            for a in artists:
                sa.append(a['name'])
            Store_Artists.append(", ".join(sa))
            Store_Songs.append(s['name'])
            Store_URL.append(s['mid'])

        for count, (a, b,c ) in enumerate(zip(Store_Artists, Store_Songs, Store_URL), start=1):
            print(f"\n第{count}首:\n{a}  •  {b}\nhttps://y.qq.com/n/ryqq/songDetail/{c}\n")
            
        if SavePath:
            logFile=newfile(SavePath, f"QQ音乐 - {Author}的{Title} {ff}.txt")
            for count, (s,u) in enumerate(zip(Store_Songs, Store_URL),start=1):
                with open(logFile, 'a', encoding='utf-8') as f:
                    if f.tell()==0:
                        f.write(f"{ff}\n作者: {rAuthor}\n歌单: {rTitle}\n链接: {PlaylistURL}\n\n")
                        if TitleFuck:
                            f.write(f"因为如下符号不允许出现在文件名中''\\', '/', ':', '?', '*', '\"', '<', '>', '|''\n\n所以我统一替换为\u2022\n所以歌单原名是 '{rTitle}', 而不是 '{rTitle}'\n替换的符号为{', '.join([fuck for fuck in sTitleFuck])}\n\n")
                        if AuthorFuck:
                            f.write(f"因为如下符号不允许出现在文件名中''\\', '/', ':', '?', '*', '\"', '<', '>', '|''\n\n所以我统一替换为\u2022\n所以作者原名是 '{Author}', 而不是 '{rAuthor}'\n替换的符号为{', '.join([fuck for fuck in sAuthorFuck])}\n\n")
                    f.write(f"第{count}首:\n{s}\n{u}\n\n")
        print(f"\n\nQQ音乐: {Title}导出完成!\n共有{len(Store_Songs)}首歌\n")
    except Exception as e:
        print("出错啦!",e)
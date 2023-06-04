import sys
sys.dont_write_bytecode = True

import json, requests, os, datetime, re, random
from NCMGet import getSong
from NewFile import newfile
from naming import Fuck


def ExportNCM(reqAPI, EnterPath):
    req=exp=SavePath=''
    title=''
    author=''
    final=''
    current_datetime = datetime.datetime.now()
    ff=current_datetime.strftime('%Y-%m-%d')

    TitleFuck=[]
    AuthorFuck=[]
    sTitleFuck=[]
    sAuthorFuck=[]

    APIPath = "https://music.163.com/api/v3/playlist/detail?id="
    try:
        print("等一下...\n")
        captions=["好耶! 歌单导完啦! ","全部弄好了, 但是好饿...", "ZZY ZZY ZZY",
        "导出完成", "任务已完成! That's The Motto!", "在音乐的花园里, 种歌曲的种子, 得歌单的花...",
        "任务完成了, 如果你认识ZZY, 麻烦说一声把我微信黑名单解了"]
        re.search(r"playlist\?id=([^\W]+)", reqAPI).group(1)
        req = APIPath + re.search(r"playlist\?id=([^\W]+)", reqAPI).group(1)
        tracks = json.loads(requests.get(req).text)['playlist']['trackIds']
        rAuthor=json.loads(requests.get(req).text)['playlist']['creator']['nickname']
        rTitle=json.loads(requests.get(req).text)['playlist']['name']
        author=Fuck(rAuthor, AuthorFuck, sAuthorFuck)[0] #Fuck naming
        title=Fuck(rTitle, TitleFuck, sTitleFuck)[0] #Fuck naming


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
                            if TitleFuck or AuthorFuck:
                                e.write(f"\n因为如下符号不允许出现在文件名中 \\ / : ? * \" < > |\n\n所以我统一替换为\u2022\n")
                                if TitleFuck:
                                    e.write(f"因此歌单原名是 '{rTitle}', 而不是 '{rTitle}'\n替换的符号为{' '.join([fuck for fuck in sTitleFuck])}\n\n")
                                if AuthorFuck:
                                    e.write(f"因此作者原名是 '{Author}', 而不是 '{rAuthor}'\n替换的符号为{' '.join([fuck for fuck in sAuthorFuck])}\n\n")
                        e.write(f"第{count}首:\n{r}\n{u}\n\n")

            if len(FailedLoad)==0:
                print(captions[random.randint(0, len(captions)-1)])
            if len(FailedLoad)!=0:
                print(f"\n\n这个链接: {reqAPI} 有导出失败的歌曲, 可能因版权下架了或是其他事情用不了这些歌曲\n\n")
                for ct, f in enumerate(FailedLoad, start=1):
                    print("\n第{}首:\n{}".format(ct, f))
                if SavePath:
                    logFile=newfile(SavePath, f"网易云导出失败的歌单 - {title} \u2022 {author} {ff}.txt")
                    for ct, f in enumerate(FailedLoad, start=1):
                        with open(logFile, 'a', encoding='utf-8') as e:
                            if e.tell()==0:
                                e.write(f"{ff}\n作者: {author}\n歌单:{title}\n链接: {reqAPI}\n\n")
                            e.write(f"第{ct}首: {f}\n\n")
                print("上面是这些导出失败的歌曲")
        
        except Exception as e:
            print(f"出错啦!\n{e}")
    except:
        a=r"album\?id="
        at=r"/artist"
        if at in reqAPI:
            print(f"{reqAPI}这货看起来像是来自某个歌手页面? 但小小的花园里只容得下歌单的种子呐")
        elif a in reqAPI:
            print(f"这个是专辑的种子==||: {reqAPI}\n但这是歌单的花园呐")
        else:
            ccc=["只能导出歌单, 这是个啥啊...?ヽ⁠༼⁠⁰⁠o⁠⁰⁠；⁠༽⁠ノ","睁大眼睛确认了N遍, 这货我不认识啊⁠⊙ ⁠_ ⁠ ◎ ⁠)", "抱歉, 这个种子太丑了, 只专一于歌单的我不认识╮⁠(⁠╯⁠_⁠╰⁠)⁠╭"]
            ca=["难道花园里的种子变异了?", "我还是去吃点饭吧", "算了算了睡觉去了"]
            print(f"{ccc[random.randint(0, len(ccc)-1)]}\n{reqAPI}\n{ca[random.randint(0, len(ca)-1)]}\n")

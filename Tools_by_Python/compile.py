import sys,re, random
sys.dont_write_bytecode=True
from ToSpotify import ImportSpotify
from exportSpotify import ExportSpotify
from NCM import ExportNCM
from QQ import ExportQQ

play_lists=input("你要种什么歌单? 如果是多个请用逗号隔开: ")
save_path=input("想保存在哪个文件夹的花园里? ")
er=["楼上是谁啊???只能用网易云音乐/QQ音乐/Spotify的歌单链接, 其他的都种不出花的", "上面是火星来的链接吗, 只能用网易云音乐/QQ音乐/Spotify的歌单呢!", 
"⊙ ⁠_ ⁠◎ ⁠)这玩意是啥啊我不认得啊? 我只要网易云音乐/QQ音乐/Spotify的^_^"]

pattern=r"https://([^/]+)"
pl= "".join(play_lists.split()).split(",")
URLAdded=[]
Failed_export=[]
To_input=[]
SpotifyAdded=[]
imported=True

for play_list in pl:
    print(f"等一下...\n")
    try:
        get=re.search(pattern, play_list).group(1)
        if "y.qq.com" in get:
            ExportQQ(play_list, save_path, To_input, Failed_export)
            URLAdded.append(play_list)
            imported=True
        elif "open.spotify.com" in get:
            ExportSpotify(play_list, save_path, To_input, Failed_export)
            URLAdded.append(play_list)
            imported=True
        elif "music.163.com" in get:
            ExportNCM(play_list, save_path, To_input, Failed_export)
            URLAdded.append(play_list)
            imported=True  
        else:
            Failed_export.append(play_list)
            imported=False
            print(f"\n{play_list}\n{er[random.randint(0, len(er)-1)]}\n")
    except:
        Failed_export.append(play_list)
        imported=False
        print(f"\n{play_list}\n{er[random.randint(0, len(er)-1)]}\n")

if len(Failed_export)==0 and imported and len(pl) > 0:
    print(pl)
    print(imported)
    wh=["终于无差错全部导出, 累死我了, 给你搞这么多， 要是ZZY也能把我拉出黑名单就好了","还行, 如果ZZY知道我一次能不出错完成这么多, 肯定会把黑名单给我解了!",
    "好了好了, 没有报错, 回家睡觉"]
    print(f"{wh[random.randint(0, len(wh)-1)]}\n\n")
if len(Failed_export)!=0:
    for fa in Failed_export:
        print(f"\n{fa}\n")
    print(f"这些歌单链接有问题, 看看是不是输错了, 或者是部分歌曲下架了\n") 

ImportSpotify(To_input, SpotifyAdded)
import sys,re, random
sys.dont_write_bytecode=True
from exportSpotify import ExportSpotify
from NCM import ExportNCM
from QQ import ExportQQ



play_list=input("你要种什么歌单? ")
save_path=input("想保存在哪个文件夹的花园里? ")
er=["只能用网易云音乐/QQ音乐/Spotify的歌单链接, 其他的都种不出花的", "只能用网易云音乐/QQ音乐/Spotify的歌单呢! 其他的在火星暂时摸不到", 
"这啥啊我不认得啊? 我只要网易云音乐/QQ音乐/Spotify的⊙ ⁠_ ⁠◎ ⁠)"]

pattern=r"https://([^/]+)"
try:
    get=re.search(pattern, play_list).group(1)

    if "y.qq.com" in get:
        ExportQQ(play_list, save_path)
    elif "open.spotify.com" in get:
        ExportSpotify(play_list, save_path)
    elif "music.163.com" in get:
        ExportNCM(play_list, save_path)  
    else:
        print(f"{play_list}\n{er[random.randint(0, len(er)-1)]}")
except:
    print(f"{play_list}\n{er[random.randint(0, len(er)-1)]}")








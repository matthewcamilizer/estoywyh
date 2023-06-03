import sys,re
sys.dont_write_bytecode=True
from exportSpotify import ExportSpotify
from NCM import ExportNCM
from QQ import ExportQQ



play_list=input("输入歌单链接(非歌单链接则不能导出) :")
save_path=input("输入日志保存路径: ")

pattern=r"https://([^/]+)"
get=re.search(pattern, play_list).group(1)

if "y.qq.com" in get:
    ExportQQ(play_list, save_path)
elif "open.spotify.com" in get:
    ExportSpotify(play_list, save_path)
elif "music.163.com" in get:
    ExportNCM(play_list, save_path)  
else:
    print(f"invalid URL to export playlists\n{play_list}")








import os, base64, requests, json, re, datetime
from requests import post, get


current_datetime = datetime.datetime.now()
ff=current_datetime.strftime('%Y-%m-%d')


client_id = "348de570cabd4bbdabb3eb80b2be3b54"
client_secret = "f6282eee472c4add954af47b5f5379c2"
#tp = "https://api.spotify.com/v1/playlists/3dpaAexEtkFHiQvLeNzNjw"
#https://api.spotify.com/v1/albums/3nG37CdJEbz1c7KrOOQn4Z
base_tp = r"https://api.spotify.com/v1/"
ttp = input(r"Enter Spotify URL here: ")
path = input(r"Enter path to save log or press ENTER to skip: ")
playlist=r"playlist/([^\W]+)"
album=r"album/([^\W]+)"
sp=re.search(playlist, ttp)
sa=re.search(album, ttp)
tp=""

if "playlist" in ttp:
    tp = f"{base_tp}playlists/{sp.group(1)}"
if "album" in ttp:
    tp = f"{base_tp}albums/{sa.group(1)}"

def get_token():
    auth_str=client_id+":"+client_secret
    auth_bytes=auth_str.encode("utf-8")
    auth_64=str(base64.b64encode(auth_bytes),"utf-8")

    u="https://accounts.spotify.com/api/token"
    h={"Authorization":"Basic "+auth_64,"Content-Type":"application/x-www-form-urlencoded"}
    d={"grant_type":"client_credentials"}
    r=post(u,headers=h,data=d)
    json_result=json.loads(r.content)
    print(json_result)
    tk=json_result["access_token"]
    return tk
token = get_token()

def get_auth_token(tkk):
    return {"Authorization":"Bearer "+tkk}

store_track=[]
store_song=[]
store_artist=[]
logFile=''
title=''
author=''


def APIget(ttk):
    h=get_auth_token(ttk)
    re=get(tp,headers=h)
    json_re=json.loads(re.content)["tracks"]["items"]
    if "playlist" in tp:
        title=json.loads(re.content)['name']
        author=json.loads(re.content)['owner']['display_name']
        for j in json_re:
            for k,jj in j['track'].items():
                store_track.append((k,jj))
        for key, value in store_track:
            if key=='name':
                store_song.append(value)
            if key=='artists':
                artists=[]
                for jjj in value:
                    artists.append(jjj['name'])
                store_artist.append(", ".join(artists))
        if path:
            logFile=os.path.join(path, f"{title} by {author} from Spotify {ff}")        
            if os.path.exists(f"{logFile}.log"):
                user_input=input('The file already exists. Press Y to create a new file or append to the existing file )')
                if user_input.upper()=='Y':
                    for artist, song in zip(store_artist, store_song):
                        with open(f"{logFile}(1).log", 'a', encoding='utf-8') as f:
                            if f.tell()==0:
                                f.write(f"{title} by {author}\n{ff}\n")
                            f.write('\n'+f"{artist} - {song}"+'\n')
                else:
                    for artist, song in zip(store_artist, store_song):
                        with open(f"{logFile}.log", 'a', encoding='utf-8') as f:
                            if f.tell()==0:
                                f.write(f"{title} by {author}\n{ff}\n")
                            f.write('\n'+f"{artist} - {song}"+'\n')
            else:
                for artist, song in zip(store_artist, store_song):
                    with open(f"{logFile}.log", 'a', encoding='utf-8') as f:
                        if f.tell()==0:
                            f.write(f"{title} by {author}\n{ff}\n")
                        f.write('\n'+f"{artist} - {song}"+'\n')

    if "album" in tp:
        title=json.loads(re.content)['name']
        author=json.loads(re.content)['artists'][0]['name']
        for j in json_re:
            for k,jj in j.items():
                store_track.append((k,jj))
        for key, value in store_track:
            if key=='name':
                store_song.append(value)
            if key=='artists':
                artists=[]
                for jjj in value:
                    artists.append(jjj['name'])
                store_artist.append(", ".join(artists))
        if path:
            logFile=os.path.join(path, f"{title} by {author} from Spotify {ff}")        
            if os.path.exists(f"{logFile}.log"):
                user_input=input('The file already exists. Press Y to create a new file or append to the existing file )')
                if user_input.upper()=='Y':
                    for artist, song in zip(store_artist, store_song):
                        with open(f"{logFile}(1).log", 'a', encoding='utf-8') as f:
                            if f.tell()==0:
                                f.write(f"{title} by {author}\n{ff}\n")
                            f.write('\n'+f"{artist} - {song}"+'\n')
                else:
                    for artist, song in zip(store_artist, store_song):
                        with open(f"{logFile}.log", 'a', encoding='utf-8') as f:
                            if f.tell()==0:
                                f.write(f"{title} by {author}\n{ff}\n")
                            f.write('\n'+f"{artist} - {song}"+'\n')
            else:
                for artist, song in zip(store_artist, store_song):
                    with open(f"{logFile}.log", 'a', encoding='utf-8') as f:
                        if f.tell()==0:
                            f.write(f"{title} by {author}\n{ff}\n")
                        f.write('\n'+f"{artist} - {song}"+'\n')

APIget(token)
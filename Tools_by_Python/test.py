import os, base64, requests, json
from requests import post, get

client_id = "d97e9b6c652b4a2780787a0de9f5fef5"
client_secret = "08403632e6aa4ffe813741c1dab279c5"
tp = "https://api.spotify.com/v1/playlists/3dpaAexEtkFHiQvLeNzNjw"


def get_token():
    auth_str=client_id+":"+client_secret
    auth_bytes=auth_str.encode("utf-8")
    auth_64=str(base64.b64encode(auth_bytes),"utf-8")

    u="https://accounts.spotify.com/api/token"
    h={"Authorization":"Basic "+auth_64,"Content-Type":"application/x-www-form-urlencoded"}
    d={"grant_type":"client_credentials"}
    r=post(u,headers=h,data=d)
    json_result=json.loads(r.content)
    tk=json_result["access_token"]
    return tk
token = get_token()

def get_auth_token(tkk):
    return {"Authorization":"Bearer "+tkk}

store_track=[]
store_song=[]
store_artist=[]

def get_playlist(ttk):
    h=get_auth_token(ttk)
    re=get(tp,headers=h)
    json_re=json.loads(re.content)["tracks"]["items"]
    for j in json_re:
        for k,jj in j['track'].items():
            store_track.append((k,jj))
    for key, value in store_track:
        if key=='name':
            store_song.append(value)
        if key=='artists':
            for jjj in value:
                store_artist.append(jjj['name'])
    for artist, song in zip(store_artist, store_song):
        print(f"{artist} - {song}")



get_playlist(token)
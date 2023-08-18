import requests, re, sys, json, spotipy
sys.dont_write_bytecode=True
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from dotenv import dotenv_values
import googleapiclient.discovery

c={
    **dotenv_values(".env.zzyily")
}

client_id = c['sp_cid']
client_secret = c['sp_cs']
h = c['header']

def get_ncm(song_name):
    a=requests.get(f"https://music.163.com/api/search/get/?csrf_token=hlpretag=&hlposttag=&s={song_name}&type=1&offset=0&total=true&limit=20", headers=h).text
    b=json.loads(a)
    result=b['result']['songs']
    song=f"https://music.163.com/song?id={result[0]['id']}"
    song_inapp=f"https://y.music.163.com/m/song?id={result[0]['id']}"

    return song,song_inapp

def get_Spotify(song_name):
    # Set up the authentication credentials
    credentials = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret,)
    sp = spotipy.Spotify(client_credentials_manager=credentials)

    results = sp.search(q=song_name, type='track', limit=1)
    return results['tracks']['items'][0]['external_urls']['spotify'], results['tracks']['items'][0]['uri']

def get_bilibili(song_name):
    a=requests.get(f"https://api.bilibili.com/x/web-interface/search/all/v2?page=1&keyword={song_name}", headers=h).text
    b=json.loads(a)

    bili=b['data']['result'][11]['data'][0]['arcurl']
    pattern=r"/video/av([^\W]+)"
    aid=re.search(pattern, bili).group(1)
    ebili=f"https://player.bilibili.com/player.html?aid={aid}&muted=false&autoplay=false"

    return bili, ebili

yt_api=c['yt_api']
def search_youtube(song):
    youtube = googleapiclient.discovery.build(serviceName='youtube', version='v3', developerKey=yt_api)
    res=youtube.search().list(part='snippet', q=f"{song} (audio)", maxResults=1, type='video')
<<<<<<< HEAD
=======
    response=res.execute()
    return return f"https://youtu.be/{response['items'][0]['id']['videoId']}"
>>>>>>> 6abd1081ce4b0010de4b342d2fe821bcc5c58e56

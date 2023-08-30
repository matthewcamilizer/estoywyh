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
    """_
    song, song in-app, artist
    """
    a=requests.get(f"https://music.163.com/api/search/get/?csrf_token=hlpretag=&hlposttag=&s={song_name}&type=1&offset=0&total=true&limit=20", headers=h).text
    b=json.loads(a)
    result=b['result']['songs']
    song=f"https://music.163.com/song?id={result[0]['id']}"
    song_inapp=f"https://y.music.163.com/m/song?id={result[0]['id']}"
    artist=f"https://music.163.com/artist?id={result[0]['artists'][0]['id']}"
    return song,song_inapp, artist

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
    
    bilibili=bili.replace("http://","https://")

    return bilibili, ebili

yt_api=c['yt_api']
def search_youtube(song_name,n):
    youtube = googleapiclient.discovery.build(serviceName='youtube', version='v3', developerKey=api)
    res=youtube.search().list(part='snippet', q=song_name, maxResults=n, type='video')
    response=res.execute()

    vid=[]
    channel=[]
    title=[]
    date=[]
    author=[]
    img=[]
    raw={}


    for i in response['items']:
        title.append(i['snippet']['title'])
        author.append(i['snippet']['channelTitle'])
        date.append(i['snippet']['publishTime'])
        vid.append(f"youtu.be/{i['id']['videoId']}")
        channel.append(f"youtube.com/channel/{i['snippet']['channelId']}")
        img.append(i['snippet']['thumbnails']['medium']['url'])

    for index, (t,a,d,v,c,i) in enumerate(zip(title, author, date, vid, channel, img), start=1):
        raw.update({f"video{index}":{"title":t,"author":a, "date":d, "vid":v, "channel":c, "img":i}})

    return raw

async def recognize_song(f):
    shazam = Shazam()
    out = await shazam.recognize_song(f)
    return out


"""
def get_Spotify(song_name):
    translator = str.maketrans('', '', string.punctuation + string.whitespace)
    cleaned_song_name = song_name.translate(translator).lower()

    credentials = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret,)
    sp = spotipy.Spotify(client_credentials_manager=credentials)
    tracks_in_album={}
    input_exists = False

    path = os.path.dirname(__file__)
    cache_file_path = os.path.join(path, 'cache.py')

    c=''
    # Read the existing content and check if the input value exists
    if os.path.exists(cache_file_path):
        with open(cache_file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line=eval(line)
                if cleaned_song_name in line['input'].translate(translator).lower():
                    input_exists = True
                    results=line['values']
                    artist = results[0]
                    artist_url=results[1]
                    album_url=results[2]
                    album_name=results[3]
                    cover_url=results[4]
                    release_date=results[5]
                    total_tracks=results[6]
                    a=results[7]
                    for t in a.items():
                        tracks_in_album[t[0]]={"song": f"{t[1]['song']}", "number":f"{t[1]['number']}", "url": f'{t[1]["url"]}', "duration": f"{t[1]['duration']}"}
                    

                    return artist, artist_url, album_url, album_name, cover_url, release_date, total_tracks, tracks_in_album


    results = sp.search(q=song_name, type='album', limit=1)
    album_id = results['albums']['items'][0]['uri']
    results = sp.album(album_id=album_id)

    artist = results['artists'][0]['name']
    artist_url=results['artists'][0]['external_urls']['spotify']
    album_url=results['external_urls']['spotify']
    album_name=results['name']
    cover_url=results['images'][0]['url']
    release_date=results['release_date']
    total_tracks=results['total_tracks']
    a=results['tracks']['items']

    for t in a:
        minutes=t['duration_ms']//60000
        seconds=int(int(t['duration_ms']%60000)/1000)
        seconds = f"0{seconds}" if seconds < 10 else seconds
        song=f"{t['name']}" if "'" not in t['name'] else f'{t["name"]}'

        tracks_in_album[f"{t['track_number']}"]={'song': song, 'number':f'{t["track_number"]}', 'url': f'{t["external_urls"]["spotify"]}', 'duration': f'{minutes}:{seconds}'}

    entry = {"input": f"{song_name}", "values": (f"{artist}", f'{artist_url}', f'{album_url}', f"{album_name}", f'{cover_url}', f"{release_date}", f"{total_tracks}", tracks_in_album)}


    # If the input value doesn't exist, add the entry to the cache file
    if not input_exists:
        with open(cache_file_path, 'a') as f:
            f.write(f"{entry}\n")

    return artist, artist_url, album_url, album_name, cover_url, release_date, total_tracks, tracks_in_album

"""
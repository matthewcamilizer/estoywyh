import sys, os
sys.dont_write_bytecode=True
import spotipy
from spotipy.oauth2 import SpotifyOAuth

cache_file=os.path.join(os.getcwd(), ".cache")

sp_oauth = SpotifyOAuth(
    client_id='348de570cabd4bbdabb3eb80b2be3b54',
    client_secret='f6282eee472c4add954af47b5f5379c2',
    redirect_uri='https://www.baidu.com/',
    scope = 'playlist-modify-public',
    show_dialog=True
)
sp = spotipy.Spotify(auth_manager=sp_oauth)

playlist_name = input("enter a playlist name: ")
playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=playlist_name, public=True)

song_list=[s.strip() for s in input(f"enter songs you want to add to {playlist_name} (separated by a comma): ").split(",")]

for song in song_list:
    results = sp.search(q=song, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        sp.playlist_add_items(playlist['id'], [track['uri']])
        print(f"Added '{track['name']}' by {', '.join([artist['name'] for artist in track['artists']])} to the playlist.")
    else:
        print(f"No results found for '{song}'.")

print("Songs added to the playlist successfully.")
#remove cache
if os.path.exists(cache_file):
    os.remove(cache_file)



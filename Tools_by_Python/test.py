import spotipy, os
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"  # Customize the scope according to your needs
redirect_uri = "https://www.baidu.com/"  # Replace with your desired redirect URI

playlist_name=input("enter playlist: ")
#username=input("enter username: ")

sp_oauth = spotipy.oauth2.SpotifyOAuth(
    client_id="348de570cabd4bbdabb3eb80b2be3b54",
    client_secret="f6282eee472c4add954af47b5f5379c2",
    redirect_uri=redirect_uri,
    scope=scope,
    show_dialog=True
)

auth_url=sp_oauth.get_authorize_url()

#response = input("Enter the URL you were redirected to: ")
response = ""
code = sp_oauth.parse_response_code(response)
token_info = sp_oauth.get_access_token(code)
access_token = token_info['access_token']
sp = spotipy.Spotify(auth=access_token)

# Create the playlist
playlist = sp.user_playlist_create(
    user=sp.current_user()['display_name'],
    name=playlist_name,
    public=True
)

uris = []
song_list=["tiesto - the motto","10:35","havana"]
for song in song_list:
    results = sp.search(q=song, limit=1, type="track")
    if results['tracks']['items']:
        track=results['tracks']['items'][0]
        uris.append(track['uri'])
sp.playlist_add_items(playlist['id'], uris)

if os.path.exists(".cache"):
    os.remove(".cache")

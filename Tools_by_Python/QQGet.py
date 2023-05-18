import requests
from bs4 import BeautifulSoup

class getSong():
    @staticmethod
    def get_song_instance(reqSong):
        h = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        keep = requests.session().get(reqSong, headers=h).content
        soup = BeautifulSoup(keep, 'html.parser')

        artist = soup.find('a',{'class':'data__singer_txt'}).text
        name = soup.find('h1',{'class':'data__name_txt'}).text
        print("{} - {}".format(artist,name))
        requests.session().close()
        return f"{artist} - {name}"

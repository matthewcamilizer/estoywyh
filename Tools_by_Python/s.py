from ShazamAPI import Shazam
import os,sys
sys.dont_write_bytecode=True

def identify_song(ee):
    #ee=input("enter path: ")
    to=[]
    res=[]
    for f in os.listdir(ee):
        if f.endswith(".mp3"):
            to.append(f) 

    for tt in to:
        to_get=os.path.join(ee,tt)
        try:
            what = open(to_get, 'rb').read()
            shazam = Shazam(what)
            here = shazam.recognizeSong()
            get = f"{next(here)[1]['track']['subtitle']} - {next(here)[1]['track']['title']}"
            res.append(get)
        except:
            res.append(f"no matched results found for {to_get}")

    return ', '.join(res)

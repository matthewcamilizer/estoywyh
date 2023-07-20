from ShazamAPI import Shazam
import os

ee=input("enter path: ")
to=[]
for f in os.listdir(ee):
    if f.endswith(".mp3"):
        to.append(f) 

res=[]
for tt in to:
    what = open(os.path.join(ee,tt), 'rb').read()
    shazam = Shazam(what)
    here = shazam.recognizeSong()
    get = f"{next(here)[1]['track']['subtitle']} - {next(here)[1]['track']['title']}"
    res.append(get)

print(', '.join(res))

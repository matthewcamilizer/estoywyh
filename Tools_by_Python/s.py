from ShazamAPI import Shazam
import os,sys
sys.dont_write_bytecode=True

ee=input("enter path: ")
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
        print(f"no matched results found for {to_get}")
        res.append(f"nothing for {to_get}")

print(', '.join(res))

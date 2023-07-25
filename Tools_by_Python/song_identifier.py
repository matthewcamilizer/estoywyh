from ShazamAPI import Shazam
import os, sys
sys.dont_write_bytecode=True


to_identify=input("input a .mp3 or .m4a file: ")
if to_identify.endswith(".mp3") or to_identify.endswith(".m4a"):
    what = open(to_identify, 'rb').read()
    try:
        shazam = Shazam(what)
        I_See=next(shazam.recognizeSong())[1]
        print(f"{I_See['track']['subtitle']} \u2022 {I_See['track']['title']}")
    except:
        print("no match found")
else:
    print("please input a .mp3 or .m4a file to continue")

"""
to_get=[]

p=input("enter path for identifying: ")
get=os.walk(p)
for r, d, files in get:
    for f in files:
        if f.endswith(".mp3") or f.endswith(".m4a"):
            to_get.append(os.path.join(p,f))

for s in to_get:
    what = open(s, 'rb').read()
    try:
        shazam = Shazam(what)
        I_See=next(shazam.recognizeSong())[1]
        print(f"{I_See['track']['subtitle']} \u2022 {I_See['track']['title']}")
    except Exception as e:
        print(e)

"""





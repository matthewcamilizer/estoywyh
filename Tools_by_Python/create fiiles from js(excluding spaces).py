import json
import os


while True:
    checkjs = input(r"input file to retrive: ")
    if os.path.splitext(checkjs)[1] == '.js':
        break
    else:
        print('invalid')

path = os.path.dirname(checkjs)
with open(checkjs, encoding='utf-8') as f:
    data = f.read()

ToRetrieve = json.loads(data.split("=")[1].strip()[:-1])

for i, ToR in enumerate(ToRetrieve):
    TxtFile = os.path.join(path,f'{ToR["hash"]}.txt')
    with open(TxtFile, "w", encoding='utf-8') as f:
        f.write(json.dumps(ToR))



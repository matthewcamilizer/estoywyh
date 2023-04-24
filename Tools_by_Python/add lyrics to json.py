import os

drive = input("input the path: ")

for root, dirs, files in os.walk(drive):
    for filename in files:
        if filename.endswith(".txt"):
            filepath = os.path.join(drive,filename)
            with open(filepath, 'r', encoding = 'utf-8') as f:
                lines = f.readlines()
                ##read all lines in the file and return them as a list
                lyrics = ''.join(lines)
                formatted_lyrics ='\n'.join(["\t" + fr'''{{"start":"", "end":"" , "text": "{line.strip()}"}},''' for line in lyrics.split('\n')])

                base_name, _ = os.path.splitext(filename)
                jsoutput = os.path.join(drive, f"{base_name}.json")
                with open(jsoutput, "w") as ff:
                    ff.write("{" + fr'''"{base_name}":''' + '\n' +'\t' + "{" + fr'''"lyrics": [
    {formatted_lyrics}
]'''+ "}" + "}")




for i in range(1, 51):
    filename = fr"C:\\Users\\Administrator\\Documents\\Tencent Files\\604338927\\FileRecv\\新建文件夹\\lyrics{i}.txt"
    with open(filename, "w") as f:
        # write the lyrics to the file
        #f.write(fr"const lyrics = " + "[\n      " + "{" + " start: , end: , text: " + '""' + " },\n      " + "{" + " start: , end: , text: " + '""' +
        #" }\n];")
        f.write(fr'''const lyrics = [
        {{ start: 0, end: 6, text: "" }},
        {{ start: 6, end: 12, text: "" }},
        {{ start: 12, end: 18, text: "" }},
        {{ start: 18, end: 24, text: "" }},
        {{ start: 24, end: 30, text: "" }}
        ];''')




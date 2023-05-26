import sys, os
sys.dont_write_bytecode = True

path=input(r"path: ")
fmt="."+input("format: ")
add_change=input("contents to add: ")
if "\\n" in add_change:
    add_change = add_change.replace("\\n", os.linesep)


for pyf in os.listdir(path):
    if pyf.endswith(fmt):
        addfile=os.path.join(path,pyf)
        with open (addfile, 'r+', encoding='utf-8') as f:
            content=f.read()
            f.seek(0,0)
            f.write(add_change + content)
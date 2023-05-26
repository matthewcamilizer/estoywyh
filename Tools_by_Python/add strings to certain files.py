import sys, os
sys.dont_write_bytecode = True

path=input(r"path: ")

for pyf in os.listdir(path):
    if pyf.endswith('.py'):
        addfile=os.path.join(path,pyf)
        with open (addfile, 'r+', encoding='utf-8') as f:
            content=f.read()
            f.seek(0,0)
            f.write("import sys\nsys.dont_write_bytecode = True\n" + content)
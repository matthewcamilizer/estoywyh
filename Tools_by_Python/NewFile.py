import sys
sys.dont_write_bytecode = True

import os

def newfile(path, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = os.path.join(path,filename)

    while os.path.exists(new_filename):
        new_filename = f"{os.path.join(path,base)}({counter}){extension}"
        counter += 1
    return new_filename


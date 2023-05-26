import sys
sys.dont_write_bytecode = True

import os
import shutil

cnm = r"C:\Users\Administrator\Documents\Tencent Files\604338927\FileRecv\1.3 estoywyh\estoywyh\static"
folders = ["sla", "slb", "slc", "sld", "sle"]
subfolders = ["songs", "scripts", "canvas"]

# Create a set to hold the directory names
dir_names = set()

# Traverse the directory tree and add directory names to the set
for f in folders:
    for sub in subfolders:
        dir_path = os.path.join(cnm, f, sub)
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            dir_names.add(os.path.basename(dir_path))

# Loop through the set of directory names and remove them
for dir_name in dir_names:
    for f in folders:
        for sub in subfolders:
            dir_path = os.path.join(cnm, f, sub, dir_name)
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                shutil.rmtree(dir_path)

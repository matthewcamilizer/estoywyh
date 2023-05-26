import sys
sys.dont_write_bytecode = True

import os

cnm = r"C:\Users\Administrator\Documents\Tencent Files\604338927\FileRecv\1.3 estoywyh\estoywyh\static"
folders = ["sla", "slb", "slc", "sld", "sle"]
subfolders = ["jjs"]

for f in folders:
    for sub in subfolders:
        op = os.path.join(os.path.join(cnm, f), sub)
        os.makedirs(op)
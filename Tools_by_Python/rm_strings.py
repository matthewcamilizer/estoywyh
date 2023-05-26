import sys
sys.dont_write_bytecode = True

import os

# Set the directory path containing the files you want to rename
directory = 'C:\\Users\\Administrator\\Documents\\Tencent Files\\604338927\\FileRecv\\1.3 estoywyh\\estoywyh\\static\\sla\\images'

# Loop over all files in the directory
for filename in os.listdir(directory):
    # Check if the file ends with 'abc.ico'
    if filename.endswith(' - 副本.ico'):
        # Construct the new file name by slicing off the 'abc' part
        new_filename = filename[:-9] + '.jpg'
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

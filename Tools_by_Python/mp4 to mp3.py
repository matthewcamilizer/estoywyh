import sys
sys.dont_write_bytecode = True

import os
import subprocess

# Set the output directory
output_dir = input("enter the output path: ")

# Set the format to convert to
output_format = "mp3"

# Prompt the user to enter the input filenames
input_files = input("Enter the names of the songs to convert, separated by commas: ").split(",")


# Loop over the input files and convert each one
for input_file in input_files:
    # Get the input file path
    input_path = input_file.strip()

    # Create the output file path by replacing the extension
        # the os.path.basename means the only file name without path #
    output_file = os.path.splitext(os.path.basename(input_file))[0] + "." + output_format
    output_path = os.path.join(output_dir, output_file)
    # Run the ffmpeg command to convert the file
    command = ["ffmpeg", "-i", input_path, "-vn", "-acodec", "libmp3lame", "-qscale:a", "2", output_path]
    # subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(command)
    print("the command is: ",command)
# input.mp4  output.mp3

print("Conversion complete and input_path is", input_path)

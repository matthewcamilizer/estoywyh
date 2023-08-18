import subprocess, base64, sys, os
from flask import Response
sys.dont_write_bytecode=True


#u="https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/8c/64/55/8c645545-fb91-7133-2cd8-a62b909c7f4b/dj.ktfmmnjq.jpg/400x400cc.jpg"


"""
pipe:0 - send out put to stdin
pipe:1 - send out put to stdout
pipe:2 - send out put to stderr
"""

class base64:
    def __init__(self,Input,Format,Output):
        self.Input=Input
        self.Format=Format
        self.Output=Output


    def b64_convert_o(i, u):

        #args u must be a video or image file, or relative online source 

        try:
            proc = subprocess.run(f'ffmpeg -i "{i}" -i "{u}" -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 -f mp3 pipe:1', stdout=subprocess.PIPE)

            # Base64 encode stdout
            encoded = base64.b64encode(proc.stdout).decode("utf-8")

            # encoded now contains the base64 string
            return Response(json.dumps(encoded, ensure_ascii='false'), content_type='application/json, utf-8')
        except Exception as e:
            return Response(json.dumps(e, ensure_ascii='false'), content_type='application/json, utf-8')

    def b64_convert_io(file, i2):
        try:
            ffmpeg_process = subprocess.Popen(f'ffmpeg -i pipe:0 -i "{i2}" -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 -f mp3 pipe:1', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            # Write the video data to the subprocess's standard input
            stdout_data, _ = ffmpeg_process.communicate(input=file)

            # Wait for the subprocess to finish
            ffmpeg_process.wait()

            final_result = base64.b64encode(stdout_data).decode("utf-8")

            return Response(json.dumps(final_result, ensure_ascii='false'), content_type='application/json, utf-8')
        except Exception as e:
            return Response(json.dumps(e, ensure_ascii='false'), content_type='application/json, utf-8')


class basic:
    def __init__(self,Input,Format,Output):
        self.Input=Input
        self.Format=Format
        self.Output=Output

    def basic_convert(self, u):
        """
        convert anything to .mp3, argument 'u' must be video or image for further a cover image
        """
        try:
            a=subprocess.run(f'ffmpeg -i "{self.Input}" -i "{u}" -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 {self.Output}')
            b=base64.b64encode(a).decode('utf-8')
            return Response(json.dumps(b, ensure_ascii='false'), content_type='application/json, utf-8')
        except Exception as e:
             return Response(json.dumps(e, ensure_ascii='false'), content_type='application/json, utf-8')


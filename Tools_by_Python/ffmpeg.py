import subprocess, base64, sys, os, asyncio, json
sys.dont_write_bytecode=True


#u="https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/8c/64/55/8c645545-fb91-7133-2cd8-a62b909c7f4b/dj.ktfmmnjq.jpg/400x400cc.jpg"


"""
pipe:0 - send out put to stdin
pipe:1 - send out put to stdout
pipe:2 - send out put to stderr
"""

class b64:
    def __init__(self,Input,Format=None,Output=None):
        self.Input=Input
        self.Format=Format
        self.Output=Output


    async def b64_convert_o(self, u):
        """
        b64 data
        """
        #args u must be a image file, or relative online source 

        try:
            proc = subprocess.Popen(f'ffmpeg -i "{self.Input}" -i "{u}" -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 -f mp3 pipe:1', stdout=subprocess.PIPE)

            proc.wait()
            # Base64 encode stdout
            encoded = base64.b64encode(proc.stdout).decode("utf-8")

            # encoded now contains the base64 string
            return encoded
        except Exception as e:
            return e

    async def b64_convert_io(self, i2=None):
        """
        b64 data
        """
        try:
            if i2:
                ffmpeg_process = subprocess.Popen(f'ffmpeg -i pipe:0 -i "{i2}" -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 -f mp3 pipe:1', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            else:
                ffmpeg_process = subprocess.Popen(f'ffmpeg -i pipe:0 -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 -f mp3 pipe:1', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            # Write the video data to the subprocess's standard input
            stdout_data, _ = ffmpeg_process.communicate(input=self.Input)

            ffmpeg_process.wait()
            #base64.b64encode
            final_result = base64.b64encode(stdout_data).decode("utf-8")
            
            return final_result
        except Exception as e:
            return e


class basic:
    def __init__(self,Input,Format,Output):
        self.Input=Input
        self.Format=Format
        self.Output=Output

    async def basic_convert(self, u):
        """
        convert anything to .mp3, argument 'u' must be video or image for further a cover image
        """
        try:
            a= subprocess.run(f'ffmpeg -i "{self.Input}" -i "{u}" -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 {self.Output}')
            b=base64.b64encode(a).decode('utf-8')
            
            return b
        except Exception as e:
            return e


import subprocess, base64


#u="https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/8c/64/55/8c645545-fb91-7133-2cd8-a62b909c7f4b/dj.ktfmmnjq.jpg/400x400cc.jpg"

class base64:
    def b64_convert(i, u):

        #args u must be a video or image file, or relative online source 

        """
        pipe:0 - send out put to stdin
        pipe:1 - send out put to stdout
        pipe:2 - send out put to stderr
        """
        try:
            proc = subprocess.run(f'ffmpeg -i "{i}" -i "{u}" -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 -f mp3 pipe:1', stdout=subprocess.PIPE)

            # Base64 encode stdout
            encoded = base64.b64encode(proc.stdout).decode("utf-8")

            # encoded now contains the base64 string
            return encoded
        except Exception as e:
            return e

class basic:
    def basic_convert(i,u,f):
        """
        convert anything to .mp3, argument 'u' must be video or image for further a cover image
        """
        try:
            subprocess.run(f'ffmpeg -i "{i}" -i "{u}" -c:a libmp3lame -c:v copy -map 0:a -map 1 -id3v2_version 3 {f}')
            return f"file saved as {f}"
        except Exception as e:
            return e

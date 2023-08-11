from flask import Flask, Response
from pytube import YouTube
import io, json, base64


@app.route('/video', methods=['GET'])
def get_video(url):
    print("0")
    yt = YouTube(url)

    info=f"{yt.author} \u2022 {yt.title}"

    video_stream = yt.streams.get_highest_resolution()

    print("1")
    # Create an in-memory file buffer
    file_buffer = io.BytesIO()

    # Download the video into the file buffer
    print("2")
    video_stream.stream_to_buffer(file_buffer)


    print("3")
    #set to the beginning of the downloaded video content
    file_buffer.seek(0)

    #get the raw binary value in file buffer
    buffer_b64 = base64.b64encode(file_buffer.getvalue()).decode('utf-8')

    print("4")
    # Return the file buffer as a response
    get={
      'file': buffer_b64,
      'info': info
    }
    
    print("5")
    return Response(json.dumps(get, ensure_ascii='false'), content_type='application/json;utf-8')

import rrytapi
import os
#JVKE Autumn url: https://youtube.com/watch?v=QegcGsE9tYE
DST_DIR="/Volumes/RRP515/Rsongs"
INPUT_FILE="playlist_songs/JVKE---this-is-what-autumn-feels-like_251.weba.mp3"
#INPUT_FILE="rrytapi_downloads/JVKE_-_this_is_what_autumn_feels_like_140.m4a"
rrytapi.convert_audio(
    INPUT_FILE,
    os.path.join(DST_DIR,os.path.basename(INPUT_FILE))+".wav",
    frame_rate=44100)
video=rrytapi.get_video("https://www.youtube.com/watch?v=PEM0Vs8jf1w")
from pydub import AudioSegment
from rrytapi.utils import TimeIt
import os
INPUT_FILE="playlist_songs/JVKE---this-is-what-autumn-feels-like_251.weba.mp3"
DST_DIR="/Volumes/RRP515/Rsongs"

OUTPUT_FILE=os.path.join(DST_DIR,os.path.basename(INPUT_FILE))+".mp3"
ti=TimeIt()
audio=AudioSegment.from_file(INPUT_FILE)
ti.print("from_file")
audio=audio.set_frame_rate(44100)
ti.print("set_frame_rate")
help(audio)
audio.export(OUTPUT_FILE,format="mp3")
ti.print("export")
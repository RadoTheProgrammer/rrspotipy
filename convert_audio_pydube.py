from pydub import AudioSegment
import os
from rrytapi.utils import TimeIt
ti=TimeIt()
INPUT_FILE="playlist_songs/JVKE---this-is-what-autumn-feels-like_251.weba.mp3"
DST_DIR="/Volumes/RRP515/Rsongs"

OUTPUT_FILE=os.path.join(DST_DIR,os.path.basename(INPUT_FILE))+".wav"
audio=AudioSegment.from_file(INPUT_FILE)
ti.print("from_file")
audio=audio.set_frame_rate(44100)
ti.print("set_frame_rate")
audio.export(OUTPUT_FILE,format="wav")
ti.print("export")
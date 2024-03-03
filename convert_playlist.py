PLAYLIST_DIR="../../my_favourite_songs"
DONE_DIR="../../my_favourite_songs_done"
DEST_DIR="/Volumes/RRP515/Rsongs"
ASK=False
import rrspotipy
import rrytapi
import os

playlist = rrspotipy.Playlist.from_dir(PLAYLIST_DIR)
playlist.verif()
for file in playlist:
    #dest_file=os.path.join(DEST_DIR,os.path.basename(file+".wav"))
    #if os.path.exists(dest_file):
    #    continue
    #print(file)
    try:
        print(file)
        if ASK:
            dest_name=input()
        else:
            dest_name=None

        if not dest_name:
            dest_name=os.path.basename(file)

        dest_file=os.path.join(DEST_DIR,dest_name+".wav")

        rrytapi.convert_audio(file,dest_file,frame_rate=44100)
        os.rename(file,os.path.join(DONE_DIR,os.path.basename(file)))
    except Exception as err:
        print(err)
        continue
    #os.rename(file,"done-"+file)


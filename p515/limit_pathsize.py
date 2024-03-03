import rrspotipy

DIR="/Volumes/RRP515/Rsongs"
playlist=rrspotipy.Playlist.from_dir(DIR)
playlist.verif()
for file in playlist:
    if len(file)>70:
        print(file)
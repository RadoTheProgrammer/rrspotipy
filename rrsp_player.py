

import src.rrspotipy as rrspotipy

FILE="/Volumes/RRUSB/Rsongs/JVKE---this-is-what-autumn-feels-like_251.weba.mp3"

playlist=rrspotipy.Playlist([FILE])
with rrspotipy.Pygame():
    playlist.start()
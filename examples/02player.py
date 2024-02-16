import rrspotipy
FILE="my_favourite_songs/JVKE---this-is-what-autumn-feels-like_251.weba.mp3"

playlist=rrspotipy.Playlist([FILE])
with rrspotipy.Pygame():
    playlist.start()
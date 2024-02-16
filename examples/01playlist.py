
import rrspotipy

DIR="my_favourite_songs"

playlist=rrspotipy.Playlist.from_dir(DIR)
playlist.verif()
playlist.shuffle()
print(f"Total duration: {playlist.get_total_duration()}")
with rrspotipy.Pygame():
    playlist.start()
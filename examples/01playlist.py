
import rrspotipy

DIR="/Users/alain/RR/Rsongs"

playlist=rrspotipy.Playlist.from_dir(DIR)
playlist.verif()
playlist.shuffle()
print(f"Total duration: {playlist.get_total_duration()}")
with rrspotipy.Pygame():
    playlist.start()
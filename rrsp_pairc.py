

import src.rrspotipy as rrspotipy

DIR="/Volumes/RRUSB/Rsongs"

playlist=rrspotipy.Playlist.from_dir(DIR)
playlist.verif()
print(f"Total duration: {playlist.get_total_duration()}")
with rrspotipy.Pygame():
    print(playlist.pairwise_comparison())
DIR="my_favourite_songs"

import rrspotipy

playlist=rrspotipy.Playlist.from_dir(DIR)
playlist.verif()
playlist.shuffle()

playlist.to_dir(DIR+"2",symlink_mode=True)
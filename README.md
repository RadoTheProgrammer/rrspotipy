

# RRSpotipy

This project is to play playlist of songs

## Installation

After git cloned a repository, you can install the python project using

```

pip install .
```

## Usage

Here's an example usage of RRSpotipy:

```python

import rrspotipy

DIR="my_favourite_songs"

playlist=rrspotipy.Playlist.from_dir(DIR)
playlist.verif()
playlist.shuffle()
print(f"Total duration: {playlist.get_total_duration()}")
with rrspotipy.Pygame():
    playlist.start()
```

To get more examples usages, take a look at the examples directory.

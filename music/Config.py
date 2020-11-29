import os

class Config:
    #  Absolute Path to the directory where songs are
    songs_dir = os.path.join (os.environ['HOME'], 'ndisk')

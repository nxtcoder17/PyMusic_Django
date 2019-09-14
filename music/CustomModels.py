# I don't need a Database, cause i will be reading stuffs from a file

from pathlib import Path
import os

# Imports for gstreamer
import gi
gi.require_version ("Gst", '1.0')
gi.require_version ("GstBase", '1.0')
from gi.repository import Gst
import threading
import random
import time

from music.Config import Config

class Song:
    def __init__(self):
        self.MUSIC_DIR = Path(Config.songs_dir)
        Gst.init (None)
        self.player = Gst.ElementFactory.make ("playbin", "player")
        self.folders = []
        self.songs = []
        self.t = None
        self.title = ""

    def fetch (self, dir):
        """
        fetch(): call requires a param dir and retrun
        """
        folders = []
        songs = []
        assert dir is not None, "fetch() call without <dir> argument"
        for file in dir.iterdir():
            if file.is_file():
                songs.append (file)
            elif file.is_dir():
                folders.append (file)
        return folders, songs

    def fetch_songs(self):
        """ Fetch songs only, usually from songs folder"""
        if len(self.songs) == 0:
            for file in self.MUSIC_DIR.joinpath ("./songs").iterdir():
                if file.is_file():
                    self.songs.append (file)
        return self.songs

    def play_song (self, song_path):
        self.title = str(song_path).split('/')[-1]
        if self.player is not None:
            self.player.set_state (Gst.State.NULL)
        self.player.set_property ("uri", "file://"+str(song_path))

        if self.t is None:
            self.t = threading.Thread (target=self.worker_thread)
            self.t.start()

        self.player.set_state (Gst.State.PLAYING);

    
    def pause_song (self):
        self.player.set_state (Gst.State.PAUSED);

    def resume_song (self):
        self.player.set_state (Gst.State.PLAYING);

    def stop_song (self):
        self.player.set_state (Gst.State.NULL);

    def worker_thread (self):
        while True:
            self.bus = self.player.get_bus()
            self.msg = self.bus.timed_pop_filtered (Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)
            # The above line, holds the thread inactive till the time one of the Error occurs
            if self.msg:
                t = self.msg.type
                if t == Gst.MessageType.EOS:
                    # Stream Ended
                    # Play a random song
                    self.play_song (random.choice (self.songs))


if __name__ == '__main__':
    song = Song()
    songs = song.fetch_songs()
    print (songs)

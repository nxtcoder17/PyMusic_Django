from django.shortcuts import render
from music.CustomModels import Song
from music.Config import Config

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path

# Create your views here.

# View: maintains song instance that helps access Song methods
song = Song()
is_paused = False;      # is_paused variable to check if the song is currently paused or playing

def index (request):
    songs = song.fetch_songs()
    context = {
        'songs': songs,
        'show_folder': False,
    }
    return render (request, 'music/index.html', context)

def folders (request):
    dir_path = request.GET.get ('dir', Config.songs_dir)
    dir_path = Path (dir_path)
    folders, songs = song.fetch(dir_path)
    context = {
        'songs': songs,
        'folders': folders,
        'show_folder': True,
    }
    return render (request, 'music/index.html', context)

def favicon (request):
    return HttpResponse (open("music/images/favicon.ico").read(), content_type='image/png')

@csrf_exempt
def play (request):
    file = request.POST.get ('song')
    song.play_song (file)
    return HttpResponseRedirect ('/music/')
    # return HttpResponse (f"data: {song.play_song (file)}\n\n", content_type='text/event-stream')

@csrf_exempt
def pause (request):
    global is_paused
    if not is_paused:
        is_paused = True
        song.pause_song ()
    else:
        is_paused = False
        song.resume_song()
    return HttpResponseRedirect ('/music/')

@csrf_exempt
def iter_dir(request):
    dir_path = request.POST.get('dir')
    folders, songs = song.fetch_songs (dir= dir_path)
    context = {
        'songs': songs,
        'folders': folders,
    }
    # return HttpResponse (f"<p> Iter_Dir called </p>", content_type='text/html')
    return render(request, 'music/index.html', context)

@csrf_exempt
def cli_play(request):
    file = request.POST.get('song')
    song.play_song(Path(file))
    return HttpResponseRedirect('/music/')


def stream (request):
    # return HttpResponse
    return HttpResponse (f"data: {song.title}\n\n", content_type='text/event-stream')



from django.shortcuts import render
from music.CustomModels import Song

from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# View: maintains song instance that helps access Song methods
song = Song()
is_paused = False;      # is_paused variable to check if the song is currently paused or playing

def index (request):
    songs = song.fetch_songs()
    context = {
        'songs': songs,
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

def stream (request):
    # return HttpResponse
    return HttpResponse (f"data: {song.title}\n\n", content_type='text/event-stream')

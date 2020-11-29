from django.urls import path
from music import views

urlpatterns = [
    path('', views.index, name='index'),
    path('folders', views.folders, name='folders'),
    path('play', views.play, name='play'),
    path('stream', views.stream, name='stream'),
    path('pause', views.pause, name='pause'),
    path('iter_dir', views.iter_dir, name='iter_dir'),
    path("cli_play", views.cli_play, name='cli_play'),
]

from django.urls import path
from music import views

urlpatterns = [
    path ('', views.index, name='index'),
    path ('play', views.play, name = 'play'),
    path ('stream', views.stream, name='stream'),
    path ('pause', views.pause, name='pause'),
]

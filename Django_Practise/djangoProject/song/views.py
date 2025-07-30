from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Song
from django.db.models import Q
# Create your views here.
@login_required
def songs(request):
    songs=Song.objects.all()
    song=request.GET.get("song")
    year=request.GET.get("year")
    artist=request.GET.get("artist")
    album=request.GET.get("album")
    if song:
        # songs=songs.filter(song__icontains=song)
        songs=songs.filter(Q(song__icontains=song) | Q(artist__icontains=song))
    if year:
        # songs=Song.objects.filter(year=year)
        songs=songs.filter(year=year)
    if artist:
        # songs=Song.objects.filter(artist__icontains=artist)
        songs=songs.filter(artist__icontains=artist)
    if album:
        # songs=Song.objects.filter(album__icontains=album)
        songs=songs.filter(album__icontains=album)
    return render(request,"song/songs.html",{"songs":songs})
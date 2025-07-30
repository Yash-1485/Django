from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):
    movies=Movie.objects.all()
    if request.method=="POST":
        title=request.POST.get('title')
        year=request.POST.get('year')
        director=request.POST.get('director')
        if title:movies=Movie.objects.filter(title__icontains=title)
        if year:movies=Movie.objects.filter(year__icontains=year)
        if director:movies=Movie.objects.filter(director__icontains=director)
    return render(request,'moviefind.html', {"movies":movies})
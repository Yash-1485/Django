from django.shortcuts import render, redirect
from .models import Event

# Create your views here.
def events(request):
    events=Event.objects.all().order_by("date")
    
    search=request.GET.get("q")
    if search:
        events=events.filter(name__icontains=search)
    return render(request,"events.html",{"events":events})

def event(request,id):
    event=Event.objects.get(pk=id)
    return render(request,'event.html',{"event":event})

def delete(request,id):
    event=Event.objects.get(pk=id)
    event.delete()
    return redirect("events.events")
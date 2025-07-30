from django.shortcuts import render, redirect
from .models import Workshop

# Create your views here.
def workshops(request):
    workshops=Workshop.objects.all()
    search=request.GET.get("q")
    if search:
        workshops=workshops.filter(title__icontains=search)
    return render(request,"workshops/upcoming_workshops.html",{"workshops":workshops})

def delete(request,id):
    workshop=Workshop.objects.get(pk=id)
    workshop.delete()
    return redirect("workshops.upcoming")

def workshop(request,id):
    workshop=Workshop.objects.get(pk=id)
    return render(request,"workshops/workshop.html",{"workshop":workshop})
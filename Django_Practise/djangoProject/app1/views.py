from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def appView1(request):
    return HttpResponse("AppView1")

def appView2(request):
    return HttpResponse("<h1>AppView2</h1>")
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is homepage")
    return render(request,"index.html")

def about(request):
    # return HttpResponse("This is about page")
    return render(request,"about.html")

def contact(request):
    # return HttpResponse("This is contact page")
    return render(request,"contact.html")
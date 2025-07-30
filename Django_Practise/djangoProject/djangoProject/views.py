from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse("This is a about page")

def contact(request):
    return HttpResponse("This is a contact page")
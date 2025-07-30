from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def form(request):
    form=UserForm()
    return render(request,"form.html",{"form":form})
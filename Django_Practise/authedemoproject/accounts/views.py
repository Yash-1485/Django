from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect("login")
    else:
        form=UserCreationForm()
    return render(request,"accounts/signup.html",{"form":form})

def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")
    else:
        form=AuthenticationForm()
    return render(request,"accounts/login.html",{"form":form})

@login_required
def user_logout(request):
    logout(request)
    return render(request,"accounts/logout.html")

def dashboard(request):
    return render(request,"accounts/dashboard.html")
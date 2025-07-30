from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Student

# Create your views here.
def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect("login")
    else:
        form=UserCreationForm()
    return render(request,"authentication/signup.html",{"form":form})

def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
    else:
        form=AuthenticationForm()
    return render(request,"authentication/login.html",{"form":form})

def user_logout(request):
    logout(request)
    return redirect("login")

def home(request):
    students=Student.objects.all().order_by("-dob")
    name=request.GET.get('name')
    roll=request.GET.get('roll')
    birthdate=request.GET.get('birthdate')
    
    if name:
        students=students.filter(name__icontains=name)
    if roll:
        students=students.filter(roll__icontains=roll)
    if birthdate:
        students=students.filter(dob__icontains=birthdate)
    return render(request,"student/home.html",{"stu":students})

@login_required
def information(request,rollno):
    student=Student.objects.get(roll=rollno)
    return render(request,"student/student_info.html",{"student":student})
from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def students(request):
    students=Student.objects.all()
    return render(request,"students/students.html",{"students":students})

def add_student(request):
    if request.method=="POST":
        name=request.POST.get("name")
        roll=request.POST.get("roll")
        email=request.POST.get("email")
        student=Student(name=name,roll=roll,email=email)
        student.save()
        return redirect("add")
    return render(request,'students/add_student.html')

def edit_student(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        roll=request.POST.get("roll")
        email=request.POST.get("email")
        student=Student.objects.get(pk=id)
        student.name=name
        student.roll=roll
        student.email=email
        student.save()
        return redirect('home')
    student=Student.objects.get(pk=id)
    return render(request,"students/edit_student.html",{"student":student})
    
def delete_student(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect("home")
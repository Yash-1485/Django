from django.shortcuts import render, redirect
from .models import Student

def upload_image(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        Student.objects.create(name=name, image=image)
        return redirect('/')
    students = Student.objects.all()
    return render(request, 'upload.html', {'students': students})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def courseHome(request):
    courseName="Python"
    topicName="Django"
    duration=1000
    data={
        "courseName":courseName,
        "topicName":topicName,
        "duration":duration,
        "age":20
    }
    return render(request,'course/course.html',{"data":data})
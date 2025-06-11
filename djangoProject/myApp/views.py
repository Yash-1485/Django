from django.shortcuts import render

# Create your views here.
def myApp(request):
    return render(request,'myApp/index.html')
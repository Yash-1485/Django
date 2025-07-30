from django.shortcuts import render
from .models import Speaker

# Create your views here.
def speakers(request):
    speakers=Speaker.objects.all()
    
    search=request.GET.get("q")
    if search:
        speakers=speakers.filter(name__icontains=search)
    return render(request,"speakers/speakers.html",{"speakers":speakers})

def speaker(request,id):
    speaker=Speaker.objects.get(pk=id)
    return render(request,"speakers/speaker_details.html",{"speaker":speaker})
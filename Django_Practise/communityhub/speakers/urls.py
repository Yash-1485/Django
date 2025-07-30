from django.urls import path
from . import views

urlpatterns=[
    path("",views.speakers,name="speakers.speakers"),
    path("detail/<int:id>/",views.speaker,name="speakers.speaker"),
]
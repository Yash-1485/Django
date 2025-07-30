from django.urls import path
from . import views

urlpatterns=[
    path("", views.courseHome, name="course.home")
]
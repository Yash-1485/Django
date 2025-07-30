from django.urls import path
from . import views

urlpatterns=[
    path("",views.workshops,name="workshops.upcoming"),
    path("delete/<int:id>",views.delete,name="workshops.delete"),
    path("detail/<int:id>",views.workshop,name="workshops.workshop"),
]
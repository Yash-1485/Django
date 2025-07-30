from django.urls import path
from . import views

urlpatterns=[
    path("appView1/",views.appView1),
    path("appView2/",views.appView2)
]
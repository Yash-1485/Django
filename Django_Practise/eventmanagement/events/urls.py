from django.urls import path
from . import views

urlpatterns=[
    path("",views.events,name="events.events"),
    path("<int:id>/",views.event,name="events.event"),
    path("delete/<int:id>/",views.delete,name="events.delete"),
]
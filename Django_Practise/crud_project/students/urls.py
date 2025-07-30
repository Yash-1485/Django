from django.urls import path
from . import views

urlpatterns = [
    path("",views.students,name="home"),
    path("students/add/",views.add_student,name="add"),
    path("students/edit/<int:id>/",views.edit_student,name="edit"),
    path("students/delete/<int:id>/",views.delete_student,name="delete"),
]

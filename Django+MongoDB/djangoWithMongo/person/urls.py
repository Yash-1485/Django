from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='person.index'),
    path("create/",views.add_person,name='person.index'),
    path("find/",views.get_all_persons,name='person.index')
]

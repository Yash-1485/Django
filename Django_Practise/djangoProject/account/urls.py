from django.urls import path
from . import views

urlpatterns=[
    path('signup/',views.signup,name="account.signup"),
    path('login/',views.user_login,name="account.login"),
    path('logout/',views.user_logout,name="account.logout"),
]
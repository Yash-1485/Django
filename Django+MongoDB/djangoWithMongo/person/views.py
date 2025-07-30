from django.shortcuts import render
from .models import Users
from django.http import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.

def index(request):
    return HttpResponse("App is running")

def add_person(request):
    records={
        "fullName":"Ilaben",
        "email":"ila@gmail.com",
        "password":'12345678'
    }
    user=Users(**records)
    user.save()
    return HttpResponse("Person added successfully")

def get_all_persons(request):
    users = Users.objects()
    user_list = []

    for user in users:
        u = user.to_mongo().to_dict()
        u['_id'] = str(u['_id'])  # Convert ObjectId to string
        user_list.append(u)

    return JsonResponse(user_list, safe=False)
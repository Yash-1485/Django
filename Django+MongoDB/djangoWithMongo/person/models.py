# from django.db import models
# from db_connection import db
# # Create your models here.

# person=db['user']

from mongoengine import *
import datetime
from db_connection import *

from mongoengine import Document, StringField, BooleanField, DateTimeField, ListField, URLField
import datetime

class Users(Document):
    fullName = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)

    bio = StringField(default="")
    profilePic = URLField(default="https://avatar.iran.liara.run/public/2.png")
    location = StringField(default="")
    isOnboarded = BooleanField(default=False)

    friends = ListField(StringField(), default=[])

    createdAt = DateTimeField(default=datetime.datetime.utcnow)
    updatedAt = DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'collection': 'users',
        'indexes': ['email'],
        'ordering': ['-createdAt'],
        'auto_create_index': True,
        'strict':False
    }

    def save(self, *args, **kwargs):
        self.updatedAt = datetime.datetime.utcnow()
        return super(Users, self).save(*args, **kwargs)

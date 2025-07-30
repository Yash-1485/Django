from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=8)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):return self.name
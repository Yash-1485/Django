from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.EmailField()
    dob=models.DateField(default=datetime.now)
    image=models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.name
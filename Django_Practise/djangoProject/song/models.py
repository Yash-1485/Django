from django.db import models

# Create your models here.
class Song(models.Model):
    song=models.CharField(max_length=200)
    year=models.IntegerField(max_length=4,default=2025)
    artist=models.CharField(max_length=200,default="anonymous")
    album=models.CharField(max_length=200)
    
    def __str__(self):
        return self.song
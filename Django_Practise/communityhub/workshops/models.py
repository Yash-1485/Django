from django.db import models

# Create your models here.
class Workshop(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateField()
    venue=models.CharField(max_length=200)
    speaker_name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
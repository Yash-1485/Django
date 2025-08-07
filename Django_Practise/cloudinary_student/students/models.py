from django.db import models
from cloudinary.models import CloudinaryField
class Student(models.Model):
    name = models.CharField(max_length=100)
    # image = models.CloudinaryField(upload_to='my_images')
    image = CloudinaryField('image', folder='student_images')

    def __str__(self):
        return self.name
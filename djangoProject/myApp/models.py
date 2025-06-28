from django.db import models
from django.utils import timezone

# Create your models here.
class Chai(models.Model):

    CHAI_CHOICES=[
        ("ML","MASALA"),
        ("GN","GINGER"),
        ("PL","PLAIN"),
        ("KW","KIWI"),
        ("EL","ELAICHI")
    ]

    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="chais/")
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_CHOICES)
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    COURSE_CHOICES = [
        (1,'1-KURS'),
        (2,'2-KURS'),
        (3,'3-KURS'),
        (4,'4-KURS')
    ]
    degree = models.SmallIntegerField(choices=COURSE_CHOICES,verbose_name='KURS')
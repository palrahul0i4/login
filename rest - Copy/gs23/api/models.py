from operator import mod
from django.db import models

# Create your models here.

class  Student(models.Model):
    name=models.CharField(max_length = 100)
    roll=models.IntegerField()
    project=models.CharField(max_length = 70)
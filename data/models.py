from turtle import title
from django.db import models

# Create your models here.

class Data(models.Model):
    title = models.CharField(max_length=30)
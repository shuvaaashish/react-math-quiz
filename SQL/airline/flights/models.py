from django.db import models

# Create your models here.
class Flight(models.Model):
    origin=models.CharField(max_length=64)

from django.db import models

# Create your models here.

class Jbnu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    belt = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    jurl = models.CharField(max_length=50)
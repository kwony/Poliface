from django.db import models
from django.utils import timezone


class Politician(models.Model):
    name = models.CharField(max_length=200)
    party = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    namu_link = models.CharField(max_length=1000)
    count = models.IntegerField()
    age = models.IntegerField()
    political_preference = models.CharField(max_length=200)
    shot_history = models.TextField()

class Picture(models.Model):
    picture = models.ImageField()

class User_Info(models.Model):
    living_area = models.CharField(max_length=200)
    political_preference = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    age = models.IntegerField()

class Photo(models.Model):
    image = models.ImageField(upload_to = 'pic_folder', default='pic_folder/example.jpg')

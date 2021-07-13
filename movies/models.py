from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=150)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='movieimg')
    genre = models.ManyToManyField(Genre)        



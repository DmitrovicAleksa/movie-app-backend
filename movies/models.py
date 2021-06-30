from django.db import models

GENRE_CHOICES = (
    ('A','Action'),
    ('D','Drama'),
    ('C','Comedy'),
    ('H','Horror'),
    ('R','Romance')
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='movies')
    genre = models.CharField(choices=GENRE_CHOICES,max_length=1)
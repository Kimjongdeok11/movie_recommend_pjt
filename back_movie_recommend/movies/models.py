from django.db import models
from django.conf import settings

# Create your models here.

class Actors(models.Model):
    actor_id = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    profile_path = models.CharField(max_length=150)
    department = models.CharField(max_length=150)

class Genre(models.Model):
    name = models.CharField(max_length=150)
    
class Movie(models.Model):
    movie_id = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    overview = models.TextField()
    poster_path = models.TextField(max_length=150)
    popularity = models.CharField(max_length=150)
    vote_average = models.CharField(max_length=150)
    video = models.CharField(max_length=150)
    backdrop_path = models.CharField(max_length=150)
    adult = models.BooleanField(initial=False)
    release_date = models.CharField(max_length=150)
    runtime = models.CharField(max_length=150)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actors)



class Review(models.Model):
    rank = models.CharField(max_length=150)
    content = models.CharField(max_length=150)
    user = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_field=False)
    updated_at = models.DateField(auto_now_add=True)
    movie_id = models.ForeignKey(Movie, on_delte=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delte=models.CASCADE)

class Comment(models.Model):
    create_at = models.DateTimeField(auto_field=False)
    updated_at = models.DateField(auto_now_add=True)
    review_comment = models.CharField(max_length=150)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delte=models.CASCADE)
    rank = models.ForeignKey(Review, on_delte=models.CASCADE)
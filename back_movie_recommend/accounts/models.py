from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    pass

class Like(models.Model):
    like = models.ManyToManyField(User, symmetrical=False)
    movie_id = models.ForeignKey(Movie, on_delte=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delte=models.CASCADE)

class Comment(models.Model):
    review = models.Model(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
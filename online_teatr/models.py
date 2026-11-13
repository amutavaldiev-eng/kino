from django.db import models

 
class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    name = models.CharField(max_length=200)
    caption = models.TextField()
    image = models.ImageField(upload_to='images/')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)



class Comment(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

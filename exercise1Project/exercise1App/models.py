from django.db import models

# Create your models here.


# Create a Book model with name, pageNumber, genre, and publishDate attributes

class Book(models.Model):
    name = models.CharField(max_length = 50)
    pageNumber = models.IntegerField()
    genre = models.CharField(max_length = 50)
    publishDate = models.DateField()




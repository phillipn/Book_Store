from __future__ import unicode_literals
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ..login.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('-created_at',)

class Review(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rating = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5)))
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ('-created_at',)
        unique_together = ('user', 'book')

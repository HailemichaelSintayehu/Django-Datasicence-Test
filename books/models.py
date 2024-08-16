from django.db import models
from django.contrib.auth import get_user_model

from authors.models import Author


class Series(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    series_id = models.CharField(max_length=100, unique=True)
    note = models.TextField(blank=True, null=True)
    series_works_count = models.CharField(max_length=100)
    primary_work_count = models.CharField(max_length=100)
    numbered = models.CharField(max_length=100)
    works =  models.JSONField(default=list)
    def __str__(self):
        return self.title
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    isbn = models.CharField(max_length=13, blank=True, null=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)
    asin = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True)
    average_rating = models.FloatField(default=0.0)
    rating_dist = models.JSONField(default=dict)  # Store rating distribution as a dictionary
    ratings_count = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    publication_date = models.CharField(max_length=20, blank=True, null=True)
    original_publication_date = models.CharField(max_length=20, blank=True, null=True)
    format = models.CharField(max_length=50, blank=True, null=True)
    edition_information = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True, related_name='books')
    series_position = models.CharField(max_length=10, blank=True, null=True)
    shelves = models.JSONField(default=list)  # Store shelves as a list of dictionaries
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='favorites')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        unique_together = ('user', 'book')
    

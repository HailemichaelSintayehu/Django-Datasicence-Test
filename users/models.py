from django.contrib.auth.models import AbstractUser
from django.db import models
from books.models import Book

class CustomUser(AbstractUser):
    favorite_books = models.ManyToManyField(Book, related_name='favorited_by', blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Set a unique related name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Set a unique related name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )

from django.contrib import admin

from authors.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_rating', 'ratings_count', 'fans_count')

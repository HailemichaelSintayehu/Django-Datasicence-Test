from django.contrib import admin

from books.models import Book, Series

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_rating', 'ratings_count', 'publication_date', 'num_pages')
    list_filter = ('language', 'publisher')
    search_fields = ('title', 'authors__name')


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'series_id')
    search_fields = ('title',)
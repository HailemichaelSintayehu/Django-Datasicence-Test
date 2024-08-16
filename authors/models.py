from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    fans_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    ratings_count = models.IntegerField(default=0)
    text_reviews_count = models.IntegerField(default=0)
    work_ids = models.JSONField(default=list)  
    book_ids = models.JSONField(default=list)  

    def __str__(self):
        return self.name


# Books Endpoints:

# GET /api/books/ - List all books.
# GET /api/books/:id/ - Retrieve a book by ID.
# POST /api/books/ - Create a new book.
# PUT /api/books/:id/ - Update a book.
# DELETE /api/books/:id/ - Delete a book.
# GET /api/books/?search=query - Search for books.
# Authors Endpoints:

# GET /api/authors/ - List all authors.
# GET /api/authors/:id/ - Retrieve an author by ID.
# POST /api/authors/ - Create a new author.
# PUT /api/authors/:id/ - Update an author.
# DELETE /api/authors/:id/ - Delete an author.
# Favorites and Recommendations:

# POST /api/books/:id/add_to_favorites/ - Add a book to favorites.
# POST /api/books/:id/remove_from_favorites/ - Remove a book from favorites.
# GET /api/books/recommendations/ - Get book recommendations.
# Authentication:

# POST /api/register/ - Register a new user.
# POST /api/token/ - Login and get JWT tokens.
# POST /api/token/refresh/ - Refresh JWT tokens.
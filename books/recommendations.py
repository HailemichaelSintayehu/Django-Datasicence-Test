from .models import Book
from django.db.models import Q

def get_recommendations(user):
    favorite_books = user.favorite_books.all()
    
    if not favorite_books:
        return Book.objects.all()[:5]

    author_ids = set(favorite_books.values_list('authors__id', flat=True))
    
    recommended_books = Book.objects.filter(authors__id__in=author_ids).exclude(id__in=favorite_books).distinct()
    
    if recommended_books.count() < 5:
        title_keywords = [book.title.split() for book in favorite_books]
        title_keywords = set([word for sublist in title_keywords for word in sublist])
        
        additional_books = Book.objects.filter(
            Q(title__icontains=list(title_keywords)) |
            Q(authors__id__in=author_ids)
        ).exclude(id__in=favorite_books).distinct()
        
        recommended_books = (recommended_books | additional_books).distinct()[:5]

    return recommended_books[:5]
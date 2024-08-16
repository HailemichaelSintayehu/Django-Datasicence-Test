from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Book
from authors.models import Author

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(name='Author 1', bio='Bio of Author 1')
        self.book = Book.objects.create(title='Book 1', author=self.author, description='Description 1', published_date='2023-01-01')

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)

    def test_add_to_favorites(self):
        response = self.client.post(f'/api/books/{self.book.id}/add_to_favorites/')
        self.assertEqual(response.status_code, 200)

    def test_recommendations(self):
        response = self.client.get('/api/books/recommendations/')
        self.assertEqual(response.status_code, 200)

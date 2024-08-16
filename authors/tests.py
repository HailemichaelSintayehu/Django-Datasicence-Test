from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Author

class AuthorAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(name='Author 1', bio='Bio of Author 1')

    def test_get_authors(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, 200)

    def test_get_author_by_id(self):
        response = self.client.get(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Author 1')

    def test_create_author(self):
        response = self.client.post('/api/authors/', {'name': 'Author 2', 'bio': 'Bio of Author 2'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Author.objects.count(), 2)

    def test_update_author(self):
        response = self.client.put(f'/api/authors/{self.author.id}/', {'name': 'Updated Author', 'bio': 'Updated Bio'})
        self.assertEqual(response.status_code, 200)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, 'Updated Author')

    def test_delete_author(self):
        response = self.client.delete(f'/api/authors/{self.author.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Author.objects.count(), 0)

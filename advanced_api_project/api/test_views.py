from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Create author and books
        self.author = Author.objects.create(name='J.K. Rowling')
        self.book1 = Book.objects.create(title='Book One', publication_year=2001, author=self.author)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2003, author=self.author)

        self.books_url = reverse('book-list')
        self.book_detail_url = lambda pk: reverse('book-detail', args=[pk])

    def test_list_books(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "publication_year": 2010,
            "author": self.author.id
        }
        response = self.client.put(self.book_detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        response = self.client.get(self.books_url + '?publication_year=2001')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get(self.books_url + '?search=Book%20One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year_desc(self):
        response = self.client.get(self.books_url + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2003)

    def test_unauthenticated_create_book(self):
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(self.books_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) 
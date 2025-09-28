from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


#  ListView – Retrieve all books
class BookListView(generics.ListAPIView):
    """
    API endpoint to list all books.
    Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView – Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    API endpoint to get a single book by ID.
    Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


#  CreateView – Add a new book
class BookCreateView(generics.CreateAPIView):
    """
    API endpoint to create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# 📘 UpdateView – Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    API endpoint to update a book by ID.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


#  DeleteView – Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    API endpoint to delete a book by ID.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] 

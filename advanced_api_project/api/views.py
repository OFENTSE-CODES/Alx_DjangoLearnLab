from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    - GET: Retrieve a list of all books.
    - POST: Create a new book (requires authentication).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a single book.
    - GET: Retrieve a single book by its ID.
    - PUT/PATCH: Update a book's information.
    - DELETE: Delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication for any modification

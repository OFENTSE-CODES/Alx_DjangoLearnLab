from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -------------------------------
# Public Views (read-only)
# -------------------------------

class BookListView(generics.ListAPIView):
    """
    List all books.
    Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID.
    Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# -------------------------------
# Restricted Views (authenticated)
# -------------------------------

class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book by ID.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

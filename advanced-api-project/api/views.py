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


from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering.

    - Filter by title, author, publication_year
    - Search by title and author name
    - Order by title and publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields for searching
    search_fields = ['title', 'author__name']

    # Fields for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ---------------------------
# CRUD Views for Book Model
# ---------------------------

class BookListView(generics.ListAPIView):
    """
    GET /books/
    Retrieves a list of all books.
    Accessible to all users (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retrieves a specific book by its ID.
    Accessible to all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    POST /books/
    Creates a new book instance.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<id>/
    Updates an existing book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/
    Deletes a book instance.
    Only accessible to authenticated users.
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
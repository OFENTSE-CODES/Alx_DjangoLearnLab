from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ----------------------------
# BOOK VIEWS USING GENERIC VIEWS
# ----------------------------

class BookListView(generics.ListAPIView):
    """
    Retrieves all books (Read-only).
    Accessible to everyone (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Accessible to everyone (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Restricted to authenticated users.
    Custom behavior: logs which user created the book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Custom hook: log creator
        print(f"Book created by user: {self.request.user}")
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Restricted to authenticated users.
    Custom behavior: logs which user updated the book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Custom hook: log updater
        print(f"Book updated by user: {self.request.user}")
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# ----------------------------
# BOOK VIEWS USING GENERIC VIEWS
# ----------------------------

class BookListView(generics.ListAPIView):
    """
    Retrieves all books (Read-only).
    Unauthenticated users: can view
    Authenticated users: can view
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Unauthenticated users: can view
    Authenticated users: can view
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom hook: log creator
        print(f"Book created by user: {self.request.user}")
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Custom hook: log updater
        print(f"Book updated by user: {self.request.user}")
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes an existing book.
    Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
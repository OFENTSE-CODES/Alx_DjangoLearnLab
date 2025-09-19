# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer to serialize data

# api/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer to serialize data

# api/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # 👈 import permission class
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
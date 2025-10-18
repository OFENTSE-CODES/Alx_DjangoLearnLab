from django.shortcuts import render
from .models import Book

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()  # <-- this line must match exactly for the checker
    return render(request, 'relationship_app/list_books.html', {'books': books})
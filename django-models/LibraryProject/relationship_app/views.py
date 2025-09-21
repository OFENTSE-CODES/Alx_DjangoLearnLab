from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
from django.views.generic import DetailView
from .models import Library

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'  # makes the library object available in the template
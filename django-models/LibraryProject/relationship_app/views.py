from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library  
from .models import Book  # Needed for the FBV

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View to show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library'  
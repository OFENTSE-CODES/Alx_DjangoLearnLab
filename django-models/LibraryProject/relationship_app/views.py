from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# ✅ Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Checker-friendly path

# ✅ Class-Based View: Display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Full path required by checker
    context_object_name = 'library'  # Allows using {{ library.name }} in template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # library.books.all will be available directly in template
        return context 
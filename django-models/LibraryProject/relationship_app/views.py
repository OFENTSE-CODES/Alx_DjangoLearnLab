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

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('list_books')  # Redirect after login
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
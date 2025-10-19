from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # create this form as needed


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'form': form})


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

from django.shortcuts import render
from .models import Book
from django.db.models import Q
from .forms import SearchForm  # Defined below

def search_books(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    return render(request, 'bookshelf/book_list.html', {
        'form': form,
        'books': books
    })

from django.shortcuts import render, redirect
from .forms import ExampleForm
from django.contrib import messages

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For ModelForm, you can save directly:
            form.save()
            messages.success(request, 'Form submitted successfully.')
            return redirect('example-form')  # Replace with the name of your URL
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
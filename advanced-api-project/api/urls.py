from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # GET /api/books/ - list all books
    path('books/', BookListView.as_view(), name='book-list'),

    # GET /api/books/1/ - retrieve book with id=1
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # POST /api/books/create/ - create new book (auth only)
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # PUT /api/books/1/update/ - update book with id=1 (auth only)
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # DELETE /api/books/1/delete/ - delete book with id=1 (auth only)
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
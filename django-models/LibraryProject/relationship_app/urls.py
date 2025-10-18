from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  #  This line is required to allow views.register to work

urlpatterns = [
    # Function-Based and Class-Based Views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    #  Authentication URLs (with required string patterns)
    path('register/', views.register, name='register'),  #  views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  #  LoginView.as_view(template_name=
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  #  LogoutView.as_view(template_name=
]

from django.urls import path
from . import views  # Required to access views like views.admin_view

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Existing views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    #  Role-based access control views
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),
]

from . import views

urlpatterns = [
    # Existing
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-based access views
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),

    #  Book management with custom permissions
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Existing views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-based access views
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),

    
    path('add_book/', views.add_book, name='add_book'),                # Required for "add_book/"
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Required for "edit_book/"
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
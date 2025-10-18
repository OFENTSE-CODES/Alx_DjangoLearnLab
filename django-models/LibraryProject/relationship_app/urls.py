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

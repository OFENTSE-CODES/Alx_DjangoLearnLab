# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Initialize the router and register the viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Include the router's URLs in the app's URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Includes all routes registered with the router
]
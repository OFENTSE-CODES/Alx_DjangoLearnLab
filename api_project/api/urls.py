from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize DRF router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Keep the basic ListAPIView (optional)
    path('books/', BookList.as_view(), name='book-list'),

    # Add router-generated URLs
    path('', include(router.urls)),
] 
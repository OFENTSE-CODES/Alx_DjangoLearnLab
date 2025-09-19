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
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='api_token_auth'),  #  Token auth endpoint
    path('', include(router.urls)),
]
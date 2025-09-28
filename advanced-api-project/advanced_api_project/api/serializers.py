from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # Custom validation: publication_year must not be in the future
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model with nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested relationship

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
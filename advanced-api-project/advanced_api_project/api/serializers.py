from rest_framework import serializers
from .models import Author, Book
import datetime


# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes: id, title, publication_year, author

    # Custom validation: publication year cannot be in the future
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model with nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Author info + related books

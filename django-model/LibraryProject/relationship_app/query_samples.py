# relationship_app/query_samples.py

import django
from django.conf import settings
from relationship_app.models import Author, Book, Library, Librarian

# Set up Django settings to run the script
settings.configure(default_settings=None, DEBUG=True)
django.setup()

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(f"{book.title} by {book.author.name}")

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"{book.title} by {book.author.name}")

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")

if __name__ == "__main__":
    # Example Queries (You can modify these based on actual data in your DB)
    print("Books by Author 'John Doe':")
    get_books_by_author('John Doe')

    print("\nBooks in Library 'Central Library':")
    get_books_in_library('Central Library')

    print("\nLibrarian for 'Central Library':")
    get_librarian_for_library('Central Library')
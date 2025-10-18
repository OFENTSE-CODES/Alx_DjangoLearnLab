import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # REQUIRED
        books = Book.objects.filter(author=author)     # REQUIRED
        return books
    except Author.DoesNotExist:
        return []

# 2. List all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Uses OneToOneField reverse relation
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    print("\n Books by 'Jane Austen':")
    for book in books_by_author("Jane Austen"):
        print("-", book.title)

    print("\n Books in 'Central Library':")
    for book in books_in_library("Central Library"):
        print("-", book.title)
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # REQUIRED
        books = Book.objects.filter(author=author)     # REQUIRED
        return books
    except Author.DoesNotExist:
        return []

# 2. List all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Uses OneToOneField reverse relation
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    print("\n Books by 'Jane Austen':")
    for book in books_by_author("Jane Austen"):
        print("-", book.title)

    print("\n Books in 'Central Library':")
    for book in books_in_library("Central Library"):
        print("-", book.title)

    print("\n Librarian of 'Central Library':")
    librarian = librarian_for_library("Central Library")
    if librarian:
        print("Name:", librarian.name)
    else:
        print("No librarian assigned.")
    print("\n Librarian of 'Central Library':")
    librarian = librarian_for_library("Central Library")
    if librarian:
        print("Name:", librarian.name)
    else:
        print("No librarian assigned.")
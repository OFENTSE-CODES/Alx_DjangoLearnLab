import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
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
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    print("Books by 'Jane Austen':", list(books_by_author("Jane Austen")))
    print("Books in 'Central Library':", list(books_in_library("Central Library")))
    librarian = librarian_for_library("Central Library")
    print("Librarian of 'Central Library':", librarian.name if librarian else "No librarian found")
import os
import django

# ✅ Correct Django settings module path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ✅ Task 1: Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return list(author.books.all())  # related_name='books'
    except Author.DoesNotExist:
        return []

# ✅ Task 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return list(library.books.all())  # many-to-many
    except Library.DoesNotExist:
        return []

# ✅ Task 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # one-to-one related_name='librarian'
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# ✅ Sample test usage
if __name__ == "__main__":
    print("Books by 'John Doe':", get_books_by_author("John Doe"))
    print("Books in 'Central Library':", get_books_in_library("Central Library"))
    print("Librarian for 'Central Library':", get_librarian_for_library("Central Library"))
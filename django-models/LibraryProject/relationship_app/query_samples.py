from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# List all books in a library
def books_in_library(library_name):
    return Book.objects.filter(libraries__name=library_name)

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    return Librarian.objects.get(library__name=library_name)
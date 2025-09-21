from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
books_by_author = Book.objects.filter(author__name="Some Author")

# List all books in a library
library_books = Library.objects.get(name="Some Library").books.all()

# Retrieve the librarian for a library
librarian_for_library = Library.objects.get(name="Some Library").librarian
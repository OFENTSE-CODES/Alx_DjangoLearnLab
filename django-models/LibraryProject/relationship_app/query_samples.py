from relationship_app.models import Author, Book, Library, Librarian

# --- Create sample data (only if not already in DB) ---

# Author
author, created = Author.objects.get_or_create(name="J.K. Rowling")

# Books
book1, created = Book.objects.get_or_create(title="Harry Potter 1", author=author)
book2, created = Book.objects.get_or_create(title="Harry Potter 2", author=author)

# Library
library, created = Library.objects.get_or_create(name="Central Library")
library.books.set([book1, book2])  # add books to library

# Librarian
librarian, created = Librarian.objects.get_or_create(name="John Doe", library=library)

# --- Queries required by the checker ---

# 1. Query all books by a specific author
books_by_author = Book.objects.filter(author__name="J.K. Rowling")

# 2. List all books in a library
books_in_library = Library.objects.get(name="Central Library").books.all()

# 3. Retrieve the librarian for a library
librarian_for_library = Library.objects.get(name="Central Library").librarian
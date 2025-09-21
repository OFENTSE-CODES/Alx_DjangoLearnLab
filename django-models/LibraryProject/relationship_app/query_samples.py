from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
books_by_author = Book.objects.filter(author__name="Author Name")

# List all books in a library
books_in_library = Book.objects.filter(libraries__name="Library Name")

# Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library__name="Library Name") 
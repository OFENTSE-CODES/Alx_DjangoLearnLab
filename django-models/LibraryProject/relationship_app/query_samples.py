import os
import django

# Setup Django environment for standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author named {author_name} found.")

    # List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library named {library_name} found.")

    # Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"\nLibrarian of {library_name}: {librarian.name}")
    except Exception as e:
        print(f"No librarian assigned to {library_name}: {e}")

if __name__ == "__main__":
    run_queries()
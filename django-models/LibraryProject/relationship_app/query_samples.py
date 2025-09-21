import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library

def run_queries():
    #  1. Query all books by a specific author
    try:
        author = Author.objects.get(name="J.K. Rowling")
        books_by_author = author.books.all()
        print(f"\nBooks by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("❌ Author not found.")

    #  2. List all books in a library
    try:
        library = Library.objects.get(name="Central Library")
        books_in_library = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(" Library not found.")

    #  3. Retrieve the librarian for a library
    try:
        librarian = library.librarian  # Using related_name from OneToOneField
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Exception:
        print("Librarian not found.")

if __name__ == "__main__":
    run_queries()
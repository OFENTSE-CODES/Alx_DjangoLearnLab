from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_all_books_by_author(author_name):
    try:
        # Ensure the author exists first
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Using related_name 'books' to query the author's books
        if books.exists():
            print(f"Books by {author_name}:")
            for book in books:
                print(book.title)
        else:
            print(f"No books found for {author_name}")
    except Author.DoesNotExist:
        print(f"Author {author_name} does not exist.")

# List all books in a library
def list_all_books_in_library(library_name):
    try:
        # Ensure the library exists first
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using related_name 'libraries' to query the books in the library
        if books.exists():
            print(f"Books in {library_name} library:")
            for book in books:
                print(book.title)
        else:
            print(f"No books found in {library_name}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")

# Retrieve the librarian for a specific library
def retrieve_librarian_for_library(library_name):
    try:
        # Ensure the library exists first
        library = Library.objects.get(name=library_name)
        # If a librarian exists for the library, this will return the librarian's name
        librarian = library.librarian  # Using related_name 'librarian' to get the librarian
        print(f"Librarian for {library_name} library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library {library_name} does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name} library.")

# Main entry point for running the queries
if __name__ == '__main__':
    # Sample queries (feel free to change or add more)
    query_all_books_by_author('J.K. Rowling')
    list_all_books_in_library('Central Library')
    retrieve_librarian_for_library('Central Library')
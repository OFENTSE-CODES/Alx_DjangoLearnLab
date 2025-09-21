from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    print(f"Books by {author_name}:")
    for book in books:
        print(book.title)

def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name} library:")
    for book in books:
        print(book.title)

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name} library: {librarian.name}")

if __name__ == '__main__':
    # Example queries
    query_all_books_by_author('J.K. Rowling')
    list_all_books_in_library('Central Library')
    retrieve_librarian_for_library('Central Library') 
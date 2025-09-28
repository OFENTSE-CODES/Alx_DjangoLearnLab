from django.db import models

# Author model represents writers who can have multiple books
class Author(models.Model):
    name = models.CharField(max_length=100)  # Stores author's name

    def __str__(self):
        return self.name


# Book model represents a published book
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year published
    author = models.ForeignKey(
        Author,
        related_name="books",  # Allows reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

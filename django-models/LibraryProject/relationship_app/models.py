from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    # Added library field with default=1
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='books',
        default=1
    )

    def __str__(self):
        return self.title
from django.db import models
class Author(models.Model)
"name", 
"publication_year",
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    

    def __str__(self):
        return self.title

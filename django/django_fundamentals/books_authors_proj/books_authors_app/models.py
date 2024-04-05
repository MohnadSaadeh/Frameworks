from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Author(models.Model):
    first_name  = models.CharField(max_length= 45)
    last_name = models.CharField(max_length= 45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_a_book(book_title,book_description):
    return Book.objects.create(title=book_title , desc=book_description)

def Desplay_Books():
    return Book.objects.all()

def get_Book(id):
    return Book.objects.get(id=id)

def get_author(id):
    the_book = Book.objects.get(id=id)
    the_authors = the_book.authors.all()
    return the_authors
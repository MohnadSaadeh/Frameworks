from django.db import models
import re

# Create your models here.



class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['book_title']) < 3:
            errors["title"] = "Title should be at least 3 characters"
        if len(postData['book_description']) < 3:
            errors["desc"] = "Description should be at least 3 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()







class AuthorManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # add keys and values to errors dictionary for each invalid field
        if len(postData['author_first_name']) < 3  :
            errors["author_first_name"] = "first name should be at least 3 characters"
        if Author.objects.filter (first_name = postData['author_first_name']):
            errors["author_first_name"] = "this author is already exist"
        if len(postData['author_last_name']) < 3:
            errors["author_last_name"] = "last name should be at least 3 characters"
        if not EMAIL_REGEX.match(postData['author_notes']):
            errors["author_notes"] = "the note shuld be an E-mail"
        return errors


class Author(models.Model):
    first_name  = models.CharField(max_length= 45)
    last_name = models.CharField(max_length= 45)
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()


def create_a_book(book_title,book_description):
    return Book.objects.create(title=book_title , desc=book_description)

def create_an_author(author_first_name ,author_last_name, author_notes):
    return Author.objects.create(first_name=author_first_name, last_name =author_last_name , notes=author_notes)



def Desplay_Books():
    return Book.objects.all()

def Desplay_Authors():
    return Author.objects.all()

def get_Book(id):
    return Book.objects.get(id=id)

def get_author(id):
    return Author.objects.get(id=id)

def get_book_authors(id):
    the_book = Book.objects.get(id=id)
    the_authors = the_book.authors.all()
    return the_authors

def get_auther_books(id):
    the_author = Author.objects.get(id=id)
    the_books = the_author.books.all()
    return the_books

def delete_book(id):
    a_book = Book.objects.get(id=id)
    return a_book.delete()








def add_author_to_book(the_author , the_book):
    a_author = Author.objects.get(first_name=the_author)
    a_book = Book.objects.get(id = the_book)
    return a_book.authors.add(a_author)
    
def add_book_to_author(the_book , the_author_id):
    a_book = Book.objects.get(title=the_book)
    a_author = Author.objects.get(id = the_author_id)
    return a_author.books.add(a_book)
    

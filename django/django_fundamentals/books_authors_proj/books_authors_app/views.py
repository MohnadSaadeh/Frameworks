from django.shortcuts import render ,redirect
from . import models

# Create your views here.
def home(request):
    all_books = models.Desplay_Books()
    context = {
        "all_books" : all_books
    }
    return render(request, 'index.html' , context)

def get_the_book(request):
    book_title = request.POST['book_title']
    book_description = request.POST['book_description']
    models.create_a_book(book_title,book_description)
    return redirect('/')

def book(request ,id):
    the_book = models.get_Book(id)
    the_book_authers = models.get_author(id)
    context = {
        "the_book" : the_book ,
        "the_book_authers" : the_book_authers
    }
    return render(request , 'books.html' , context)

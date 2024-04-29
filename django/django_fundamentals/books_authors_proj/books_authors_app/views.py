from django.shortcuts import render ,redirect
from . import models
from django.contrib import messages

from django.http import JsonResponse

# Create your views here.
def home(request):
    all_books = models.Desplay_Books()
    context = {
        "all_books" : all_books ,
        
        
    }
    return render(request, 'index.html' , context)



#desplays all the authors
def authors_page(request):
    all_authors = models.Desplay_Authors()
    context = {
        "all_authors" : all_authors
    }
    return render(request, 'authors.html' , context)


# this method for adding a book to database
def get_the_book(request):
    if request.method == 'POST':
        errors = models.Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            book_title = request.POST['book_title']
            book_description = request.POST['book_description']
            models.create_a_book(book_title,book_description)
            messages.success(request, "Blog successfully updated")
            return redirect('/')
# method to view a spcifc book by its id

def get_the_author(request):
    errors = models.Author.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/authors_page')
    else:
        author_first_name  = request.POST['author_first_name']
        author_last_name = request.POST['author_last_name']
        author_notes = request.POST['author_notes']
        models.create_an_author(author_first_name ,author_last_name, author_notes)
        return redirect('/authors_page')



def book(request ,id):
    the_book = models.get_Book(id)
    the_book_authers = models.get_book_authors(id)
    all_authors = models.Desplay_Authors()
    context = {
        "the_book" : the_book ,
        "the_book_authers" : the_book_authers,
        "all_authors" : all_authors
    }
    return render(request , 'book.html' , context)
    
# method to view a spcifc auther by its id
def author(request ,id):
    the_author = models.get_author(id)
    the_auther_books = models.get_auther_books(id)
    all_books = models.Desplay_Books()
    context = {
        "the_author" : the_author ,
        "the_auther_books" : the_auther_books,
        "all_books" : all_books
    }
    return render(request , 'author.html' , context)

# add a author to the book
def get_author_and_book(request ,id ): #get 
    the_author = request.POST['select_an_author']
    the_book_id = id
    models.add_author_to_book(the_author , the_book_id )
    return redirect(f'/view_book/{id}') 

# add a book to the author
def add_book_to_autho(request ,id ): #get 
    the_book = request.POST['select_a_book']
    the_author_id = id
    models.add_book_to_author(the_book , the_author_id )
    return redirect(f'/view_author/{id}') 

def delete_book(request, id):
    models.delete_book(id)
    return redirect('/')
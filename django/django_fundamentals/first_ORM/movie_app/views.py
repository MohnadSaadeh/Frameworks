from django.shortcuts import render , redirect
from . import models # acsess every thing in models

# Create your views here.
def index(request):
    #models.create_movie()
    #models.update_movie()
    #models.remove_movie_by_id(4)
    #models.remove_movie_by_name("Sweet November")
    
    movie = models.get_all_movies()
    users =  models.get_all_users()
    books = models.get_all_books()
    
    context =  {
        "all_movies" : movie,
        "all_users" : users,
        "all_books" : books
    }
    return render(request , 'index.html' , context)

def get_user(request):
    # f = request.session["f_name"] =  request.POST["first_name"]
    # l =request.session["l_name"] =  request.POST["last_name"]
    # e =request.session["email"] =  request.POST["email"]
    # a =request.session["age"] =  request.POST["age"]

    firstName   = request.POST["first_name"]
    lastName    = request.POST["last_name"]
    eMail       = request.POST["email"]
    aGe         = request.POST["age"]

    models.add_user(firstName,lastName,eMail,aGe)

    return redirect('/')

# def create_auther():
#     models.create_auther()

def add_book(request):
    bookName   = request.POST["book_name"]
    autherName    = request.POST["auther_name"]
    models.create_book(bookName, autherName)
    return redirect('/')

def delete_author(request):
    id    = request.POST["auther_name"]
    models.delete_author(id)
    return redirect('/')

def delete_book(request):
    id   = request.POST["book_name"]
    models.delete_book(id)
    return redirect('/')
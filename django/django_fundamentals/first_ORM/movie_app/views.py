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
    
    context =  {
        "all_movies" : movie,
        "all_users" : users
    }
    return render(request , 'index.html' , context)

def add_user(request):
    f = request.session["f_name"] =  request.POST["first_name"]
    l =request.session["l_name"] =  request.POST["last_name"]
    e =request.session["email"] =  request.POST["email"]
    a =request.session["age"] =  request.POST["age"]

    models.add_user(f,l,e,a)

    return redirect('/')
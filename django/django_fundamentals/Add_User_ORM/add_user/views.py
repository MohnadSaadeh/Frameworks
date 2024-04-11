from django.shortcuts import render , redirect
from . import models # acsess every thing in models

# Create your views here.
def index(request):

    users =  models.get_all_users()
    context =  {
        "all_users" : users
    }
    return render(request , 'index.html' , context)

def get_user(request):
    firstName =  request.POST["first_name"]
    lastName = request.POST["last_name"]
    email = request.POST["email"]
    age = request.POST["age"]
    
    models.save_user_date_to_session(request,firstName,lastName,email,age)

    models.add_user(firstName,lastName,email,age)

    return redirect('/')



# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is the first function in Django")

def some_function(request , memoi):
    return HttpResponse("this is the other functoin " + memoi)

def login(request):

    context = {
        "name": "Mohannad",
        "favorite_color": "Blue",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }

    return render( request , "index.html" , context)

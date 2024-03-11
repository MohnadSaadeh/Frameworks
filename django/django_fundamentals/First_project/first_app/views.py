from django.shortcuts import render ,HttpResponse ,redirect

# Create your views here.


def root(request):
    return redirect("/blogs")  # redirects you tho another method or function

def index(request):
    return HttpResponse("placeholder to a later display alist of all blogs")

def new(request):
    return HttpResponse("placeholder to a later display new form to create new blogs")

def create(request):
    return redirect("/")

def show(request , number):
    return HttpResponse("placeholder to display blog number " + number)
    
def edit(request , number):
    return HttpResponse("placeholder to edit blog " + number)

def destroy(request ,number):
    return redirect("/blogs")

from django.shortcuts import render ,redirect
from . import models
from django.contrib import messages

# Create your views here.

def shows(request):
    all__the_shows = models.all_shows()
    context = {
        "all_shows" : all__the_shows
    }
    return render(request, 'shows.html' , context)

def tv_shows(request):
    return redirect('/shows')

def add_show_page(request):
    return render(request, 'add_show.html')

def get_show(request):
    errors = models.Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/new')
    else:
        show_title = request.POST['title'] 
        show_network = request.POST['network']
        show_release_date = request.POST['release_date']
        show_description = request.POST['description']
        models.create_a_show(show_title, show_network, show_release_date , show_description)
        return redirect('/new')

def view_a_show(request, id):
    the_show = models.view_a_show(id)
    context = {
        "a_show" : the_show
    }
    return render(request, 'view_a_show.html', context)

def edit_a_show(request, id):
    the_show = models.view_a_show(id)
    context = {
        "a_show" : the_show
    }
    return render(request, 'edit_a_show.html', context)

def update_a_show(request, id):
    errors = models.Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/edit_a_show/{id}' )
    else:
        show_title = request.POST['title']
        show_network = request.POST['network']
        show_release_date = request.POST['release_date']
        show_description = request.POST['description']
        models.update_a_show(id, show_title, show_network, show_release_date, show_description)
        return redirect(f'/shows/{id}')

def delete_a_show(request, id):
    models.delete_a_show(id)
    return redirect('/shows')
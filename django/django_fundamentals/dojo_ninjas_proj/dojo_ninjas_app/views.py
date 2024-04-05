from django.shortcuts import render , redirect
from . import models

# Create your views here.

#This function will do ...
# Input:
# Outputs:
# Developer Name:
# Date Time:
# 
def homepage(request):

    ninjas = models.get_all_ninjas()
    dojos = models.get_all_dojos()
    context ={
        "all_ninjas" : ninjas ,
        "all_dojos" : dojos ,
    }

    return render(request ,'index.html', context )


def get_the_dojo(request):
    if request.POST['dojo_or_ninja'] == 'dojo':
        # dojo_name = request.POST['dojo_name']
        # dojo_city = request.POST['dojo_city']
        # dojo_state = request.POST['dojo_state']
        # dojo_desc = request.POST['dojo_discription']
        models.add_dojo_(request.POST)
        # models.add_dojo(dojo_name,dojo_city,dojo_state,dojo_desc)

    elif request.POST['dojo_or_ninja'] == 'ninja':
        ninja_first_name = request.POST['ninja_first_name']
        ninja_last_name = request.POST['ninja_last_name']
        ninja_dojo = request.POST['selected_dojo']

        models.add_ninja(ninja_first_name ,ninja_last_name,ninja_dojo)

    
    return redirect('/')

def delete_ninja(request):
    
    if request.POST['delete_record'] == "ninja" :
        ninja_id = request.POST['ninja_to_delete']
        models.delete_a_ninja(ninja_id)

    elif request.POST['delete_record'] == "dojo" :
        dojo_id = request.POST['ninja_to_delete']
        models.delete_a_dojo(dojo_id)


    return redirect('/')
    

def delete_ninja_by_anchor(req,id):  # Only for using <a> anchor to delete
    models.anchor_delete_ninja(id)

    return redirect('/')
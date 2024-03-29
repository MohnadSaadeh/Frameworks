from django.shortcuts import render
from . import models

# Create your views here.
def homepage(request):

    ninjas = models.get_all_ninjas()
    dojos = models.get_all_dojos()
    context ={
        "all_ninjas" : ninjas ,
        "all_dojos" : dojos ,
    }

    return render(request ,'index.html', context )
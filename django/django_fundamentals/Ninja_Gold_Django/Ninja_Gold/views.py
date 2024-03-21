from django.shortcuts import render , redirect
import random
from time import gmtime, strftime


# Create your views here.

def index(request):
    request.session['yourgold'] = 0
    request.session['commints_list'] = {}  #Dict
    return render(request , 'index.html')
    
def earn_take(request):
    
    if request.POST['which_form'] == 'farm':
        request.session['random'] = int(random.randint(10, 20))
        request.session['yourgold'] += request.session['random']

    elif request.POST['which_form'] == 'cave':
        request.session['random'] = int(random.randint(10, 20))
        request.session['yourgold'] += request.session['random']

    elif request.POST['which_form'] == 'house':
        request.session['random'] = int(random.randint(10, 20))
        request.session['yourgold'] += request.session['random']

    elif request.POST['which_form'] == 'quest':
        request.session['random'] = int(random.randint(-50, 50))
        request.session['yourgold'] += request.session['random']

    request.session['commints_list'].update({ request.POST['which_form'] : request.session['random']}   )
    return redirect("/earn")

def earn(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p , %H:%M:%S ", gmtime())
    }
    return render(request , 'index.html' ,context)
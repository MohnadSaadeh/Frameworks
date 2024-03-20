from django.shortcuts import render
import random                # import the random module
	# random number between 1-100

# Create your views here.

def index(request):
    request.session['yourgold'] = 0
    request.session['commints_list'] = []



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


    request.session['commints_list'].append(  request.session['random'])
    return render(request , 'index.html')

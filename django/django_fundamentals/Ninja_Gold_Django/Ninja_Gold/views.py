# 3

# Create your views here.

# def index(request):
#     request.session['yourgold'] = 0
#     request.session['commints_list'] = {}  #Dict
#     request.session['earn_gold'] = [] 
#     return render(request , 'index.html')
    
# def earn_take(request):
    
#     if request.POST['which_form'] == 'farm':
#         request.session['random'] = int(random.randint(10, 20))
#         request.session['yourgold'] += request.session['random']

#     elif request.POST['which_form'] == 'cave':
#         request.session['random'] = int(random.randint(10, 20))
#         request.session['yourgold'] += request.session['random']

#     elif request.POST['which_form'] == 'house':
#         request.session['random'] = int(random.randint(10, 20))
#         request.session['yourgold'] += request.session['random']

#     elif request.POST['which_form'] == 'quest':
#         request.session['random'] = int(random.randint(-50, 50))
#         request.session['yourgold'] += request.session['random']

#     request.session['commints_list'].update({ request.POST['which_form'] : request.session['random']}   )
#     request.session['earn_gold'].append()
#     return redirect("/earn")

# def earn(request):
#     context = {
#         "time": strftime("%Y-%m-%d %H:%M %p , %H:%M:%S ", gmtime())
#     }
#     return render(request , 'index.html' ,context)
#------------------------------------------------

from django.shortcuts import render, redirect
import random
from time import gmtime, strftime


#Create your views here.
def index(request):
    request.session['yourgold'] = 0
    request.session['log_list'] = []  # Dict
    return render(request, 'index.html')


def earn_take(request):
    money_earned = 0
    if request.POST['which_form'] == 'farm':
            money_earned = int(random.randint(10, 20))

    elif request.POST['which_form'] == 'cave':
            money_earned = int(random.randint(10, 20))

    elif request.POST['which_form'] == 'house':
            money_earned = int(random.randint(10, 20))

    elif request.POST['which_form'] == 'quest':
            money_earned = int(random.randint(-50, 50))
            request.session['random'] = money_earned
            request.session['yourgold'] += money_earned
    time = strftime("%Y-%m-%d %H:%M %p , %H:%M:%S ", gmtime())
    if money_earned < 0:
        deal = 'lost'
        session_string = f'you lost {money_earned} in {time}'
    else:
        deal = 'win'
        session_string = f'you won {money_earned} in {time}'
    request.session['log_list'] += [{'deal': deal, 'session_string': session_string}]
    print(request.session['log_list'])
    return redirect("/earn")


def earn(request):
    print(request.session['log_list'])
    return render(request, 'index.html')
from django.shortcuts import render ,HttpResponse 
import random
# Create your views here.

def theroot1(request):
    request.session['rand'] =  int(random.randint(1,100))
    request.session['theGuessed'] = 0
    request.session['attempts'] = 0
    request.session['attemptsUser'] = 5

    return render(request , "index.html" )

def yourguess(request):
    request.session['yournu_num'] =   request.POST['yournu_num']
    request.session['attempts'] += 1
    request.session['attemptsUser'] -= 1
    grater = "helper_color"
    less = "helper_color2"
    equal = "helper_color3"

    messegBIG = "Too High"
    messegLESS = "Too Low"
    messegEQUAL = "Is True"
    if (request.session['attemptsUser'] == 0):
        return render(request , "loose.html")
    elif (int(request.session['yournu_num']) > request.session['rand']):
        request.session['color'] = grater
        request.session['resultMesseg'] = messegBIG
        return render(request , "index.html")
    elif (int(request.session['yournu_num']) < request.session['rand']):
        request.session['color'] = less
        request.session['resultMesseg'] = messegLESS
        return render(request , "index.html")
    elif (int(request.session['yournu_num']) == request.session['rand']):
        request.session['color'] = equal
        request.session['resultMesseg'] = messegEQUAL
        return render(request , "index.html")
    
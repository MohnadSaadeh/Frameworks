from django.shortcuts import render ,HttpResponse ,redirect
import random
import . from models
# Create your views here.

def theroot1(request):
    request.session['rand'] =  models.get_random_num()
    request.session['attempts'] = 0
    request.session['attemptsUser'] = 10
    return render(request , "index.html" )

def yourguess(request):
    request.session['yournu_num'] = request.POST['yournu_num']
    request.session['attempts'] += 1
    request.session['attemptsUser'] -= 1

    if (request.session['attemptsUser'] == 0 and int(request.session['yournu_num']) != request.session['rand']):
        return redirect("/loose")
    elif (int(request.session['yournu_num']) > request.session['rand']):
        request.session['result'] = "grater"
        return redirect("/samapage")
    elif (int(request.session['yournu_num']) < request.session['rand']):
        request.session['result'] = "less"
        return redirect("/samapage")
    elif (int(request.session['yournu_num']) == request.session['rand']):
        request.session['result'] = "equal"
        return redirect("/winpage")



def lose_page(request):
    return render(request , "loose.html")

def same_page(request):
    return render(request , "index.html")

def win_page(request):
    return render(request , "win.html")
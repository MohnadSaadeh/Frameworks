from django.shortcuts import render ,HttpResponse ,redirect
import random
# import . from models
# Create your views here.

def theroot1(request):
    if not 'rand' in request.session:
        request.session['rand'] = int(random.randint(1, 100))
        request.session['attempts'] = 0
        request.session['attemptsUser'] = 10
    return render(request, "index.html")

def yourguess(request):
    request.session['yournu_num'] = request.POST['yournu_num']
    request.session['attempts'] += 1
    request.session['attemptsUser'] -= 1
    redirect_url = "/"

    if int(request.session['yournu_num']) > request.session['rand']:
        request.session['result'] = "grater"
    elif int(request.session['yournu_num']) < request.session['rand']:
        request.session['result'] = "less"
    elif int(request.session['yournu_num']) == request.session['rand']:
        request.session['result'] = "equal"
        redirect_url = "/winpage"
    elif request.session['attemptsUser'] == 0:
        redirect_url = "/loose"
    return redirect(redirect_url)

def lose_page(request):
    return render(request, "loose.html")

def win_page(request):
    return render(request, "win.html")
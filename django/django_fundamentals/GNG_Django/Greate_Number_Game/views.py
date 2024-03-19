from django.shortcuts import render ,HttpResponse ,redirect
import random
# Create your views here.

def theroot1(request):
    request.session['rand'] =  int(random.randint(1,100))
    request.session['attempts'] = 0
    request.session['attemptsUser'] = 7

    return render(request , "index.html" )

def yourguess(request):
    request.session['yournu_num'] = request.POST['yournu_num']
    request.session['attempts'] += 1
    request.session['attemptsUser'] -= 1
    grater = "helper_color"
    less = "helper_color2"
    equal = "helper_color3"

    messegBIG = "Too High"
    messegLESS = "Too Low"
    messegEQUAL = "Is True"
    if (request.session['attemptsUser'] == 0 and int(request.session['yournu_num']) != request.session['rand']):
        return redirect("/loose")

    elif (int(request.session['yournu_num']) > request.session['rand']):
        request.session['color'] = grater
        request.session['resultMesseg'] = messegBIG
        return redirect("/samapage")

    elif (int(request.session['yournu_num']) < request.session['rand']):
        request.session['color'] = less
        request.session['resultMesseg'] = messegLESS
        return redirect("/samapage")

    elif (int(request.session['yournu_num']) == request.session['rand']):
        request.session['color'] = equal
        request.session['resultMesseg'] = messegEQUAL
        return render(request , "win.html")
    
def lose_page(request):
    return render(request , "loose.html")

def same_page(request):
    return render(request , "index.html")
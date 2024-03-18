from django.shortcuts import render ,HttpResponse 
import random
# Create your views here.

def theroot1(request):
    request.session['rand'] =  int(random.randint(1,100))
    request.session['theGuessed'] = 0
    request.session['attempts'] = 0
    request.session['attemptsUser'] = 10
    # print(request.session['rand'])
    
    context = {
        "rand" : request.session['rand'],
        "theGuessed" : request.session['theGuessed'],
        "attempts" : request.session['attempts'] ,
        "attemptsUser" : request.session['attemptsUser']
    }
    return render(request , "index.html" , context)

def yourguess(request):
    request.session['yournu_num'] =   request.POST['yournu_num']
    
    if (int(request.session['yournu_num']) > request.session['rand']):
        return render(request , "high.html")
    elif (int(request.session['yournu_num']) < request.session['rand']):
        return render(request , "low.html")
    elif (int(request.session['yournu_num']) == request.session['rand']):
        return render(request , "equal.html")
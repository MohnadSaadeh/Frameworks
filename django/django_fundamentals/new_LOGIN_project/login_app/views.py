from django.shortcuts import render , redirect 

# Create your views here.
def index(request):
    return render(request , "index.html")


def login(request):
    return render(request , "login.html")

def check_login(request):
    user_name = request.POST['username']
    password = request.POST['password']
    wichform = request.POST['saadeh']

    if (wichform == "form1"): 
        request.session['theName'] = user_name
        request.session['thePass'] = password
        return redirect ("/hompage")   
    else:
        return render(request, "index.html")

    # if (user_name == "mohannad" and password == "123456"):
    #     return redirect ("/hompage")    #redirect to a route
    # else:
    #     return render(request, "index.html")

def home(request):
    return render(request , "home.html")
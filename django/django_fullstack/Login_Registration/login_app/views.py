from django.shortcuts import render ,redirect 
from . import models
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    return render(request, 'log_reg_page.html')


def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        first_name = request.POST['firstname'] 
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        conferm_password = request.POST['Confirm_PW']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash for the password
        conf_pw_hash = bcrypt.hashpw(conferm_password.encode(), bcrypt.gensalt()).decode() #create the hash to conferm password
        models.create_a_user(first_name, last_name, email, pw_hash, conf_pw_hash)
        
        return redirect('/')

def login(request):
    errorslogin = models.User.objects.basic_validator(request.POST)
    if len(errorslogin) > 0:
        for key, value in errorslogin.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        user = models.User.objects.filter(email=request.POST['email'])
        if user: #if True , if user exists
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/success')
            else:
                messages.error(request, "Invalid Password")
        else:
            messages.error(request, "Invalid email you have to register")
        return redirect('/')

def success(request):
    if 'user_id' not in request.session:  # if user is not logged in (not in the session)
        return redirect('/')
    context = {
        'user': models.User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')
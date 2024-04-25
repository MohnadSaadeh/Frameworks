from django.shortcuts import render , redirect
from . import models
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request): # the main page for all
    if 'admin_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'index.html')

def dashboard(request): #the page only for the ADMIN
    if 'admin_id' not in request.session:
        return redirect('/')
    return render(request, 'dashboard.html')

def register(request): # to register as Admin
    return render(request, 'admin_register.html')

def login(request):# to log in as Admin
    return render(request, 'admin_login.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def add_doctor_page(request): # open the page to add doctor
    if 'admin_id' not in request.session:
        return redirect('/')
    context = {
        'clinics': models.Clinic.objects.all()
    }
    return render(request, 'add_doctor.html' ,context)

def add_clinic_page(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    return render(request, 'add_clinic.html')

def add_pacient_page(request):
    if 'admin_id' not in request.session:
        return redirect('/')
    return render(request, 'add_pacient.html')



# --------------------------------------------------------------------

def admin_register(request):
    errors = models.Admin.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value , extra_tags = 'admin_registration' )
            
        return redirect('/registr_admin')
    else:
        admin_first_name = request.POST['admin_first_name']
        admin_last_name = request.POST['admin_last_name']
        admin_email = request.POST['admin_email']
        admin_phone = request.POST['admin_phone']
        admin_password = request.POST['admin_password']
        admin_repete_password = request.POST['admin_repete_password']
        #hash------------
        pw_hash = bcrypt.hashpw(admin_password.encode(), bcrypt.gensalt()).decode()
        pw_hash_confirm = bcrypt.hashpw(admin_repete_password.encode(), bcrypt.gensalt()).decode()
        #hash------------
        models.create_admin(admin_first_name, admin_last_name, admin_email, admin_phone,  pw_hash, pw_hash_confirm) 
        messages.success(request, "You have successfully registered as Admin!")
        return redirect('/registr_admin')


def admin_login(request):
    errors = models.Admin.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login_admin')
    else:
        admin_email = request.POST['admin_email'] # here we get the email thet ENSERTED
        admin_password = request.POST['admin_password'] # here we get the password thet ENSERTED
        admin = models.Admin.objects.get(email=admin_email) # here we get the admin by the email from DB
        if bcrypt.checkpw(admin_password.encode(), admin.admin_password.encode()): # here we chick the password 
            request.session['admin_id'] = admin.id
            return redirect('/dashboard')
        else:
            messages.error(request, "Email or Password is incorrect")
        return redirect('/login_admin')


def add_clinic(request):
    errors = models.Clinic.objects.clinic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add_clinic_page')
    else:
        clinic_name = request.POST['the_clinic_name']
        clinic_specialty = request.POST['clinic_specialty']
        clinic_details = request.POST['clinic_details']
        clinic = models.create_a_clinic(clinic_name=clinic_name, clinic_specialty=clinic_specialty, clinic_details=clinic_details)
        messages.success(request, "You have successfully added a clinic!")
        return redirect('/add_clinic_page')

def add_doctor(request):
    errors = models.Doctor.objects.doctor_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add_doctor_page')
    else:
        doctor_first_name = request.POST['doctor_first_name']
        doctor_last_name = request.POST['doctor_last_name']
        doctor_specialty = request.POST['doctor_specialty']
        doctor_phone = request.POST['doctor_phone_number']
        clinic_name = request.POST['clinic_name']
        doctor = models.create_a_doctor(doctor_first_name=doctor_first_name, doctor_last_name=doctor_last_name, doctor_specialty=doctor_specialty, doctor_phone=doctor_phone, clinic_name=clinic_name)
        messages.success(request, "You have successfully added a doctor!")
        return redirect('/add_doctor_page')

def add_pacient(request):
    errors = models.Pacient.objects.pacient_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request.value )
        return redirect('/add_pacient_page')
    else:
        pacient_first_name = request.POST['added_first_name']
        pacient_last_name = request.POST['added_last_name']
        patient_phone_number = request.POST['added_phone_number']
        pacient_identity_number = request.POST['added_identity_number']
        pacient_details = request.POST['added_details']
        pacient = models.create_a_pacient(first_name=pacient_first_name,last_name=pacient_last_name,phone_number=patient_phone_number,identity_number=pacient_identity_number,pacient_details=pacient_details)
        messages.success(request, "You have successfully added a pacient!")
        return redirect('/add_pacient_page')
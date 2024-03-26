from django.db import models
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add=True    >>> adds the current date/time when an object is created    
    updated_at =models.DateTimeField(auto_now=True)       # updates any time the object is modified


def save_user_date_to_session(request,firstName,lastName,email,age):
    request.session["f_name"]   = firstName
    request.session["l_name"] = lastName
    request.session["email"] = email
    request.session["age"] = age

def add_user(firstName,lastName,email,age):
    User.objects.create(first_name = firstName , last_name = lastName , email_address = email , age =age )

def get_all_users():
    return User.objects.all()
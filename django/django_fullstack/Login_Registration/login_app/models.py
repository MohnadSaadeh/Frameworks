from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #DATE_REGEX = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # using regex to validate email
        # add keys and values to errors dictionary for each invalid field
        if len(postData['firstname']) < 2  :
            errors["firstname"] = "First Name should be at least 3 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "last Name should be at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']): # using regex to validate email
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8: 
            errors["password"] = "a password should be at least 8 characters"
        if postData['password'] != postData['Confirm_PW']:
            errors["password"] = "passwords should match"
        return errors
    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # using regex to validate email
        if not EMAIL_REGEX.match(postData['email']): # using regex to validate email
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors["password"] = "a password should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    conferm_password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

def create_a_user(first_name, last_name, email, pw_hash, conf_pw_hash):
    return User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash, conferm_password=conf_pw_hash)
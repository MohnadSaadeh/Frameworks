from django.db import models

# Create your models here.
class Movie(models.Model):                      #model is a table in DB
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "Title: {}".format(self.title)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add=True    >>> adds the current date/time when an object is created    
    updated_at =models.DateTimeField(auto_now=True)       # updates any time the object is modified
    # fields removed for brevity
    
    def __str__(self):
        return f"<User object: {self.first_name} ({self.id})>"

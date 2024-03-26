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

def create_movie():
    Movie.objects.create(title="game of thrones", description="a good movie", release_date = "2015-10-10" , duration = 120 )


def update_movie(id):      #give an id as parameter
    movie = Movie.objects.get(id=id)       #get the instance of tje movie that i womt to update
    movie.title = "Sweet November"
    movie.description = "Romance"
    movie.save()


def remove_movie_by_id(id):
    movie = Movie.objects.get(id= id)
    movie.delete()

def remove_movie_by_name(name):
    movie = Movie.objects.get(title = name)
    movie.delete()

def get_all_movies():
    return Movie.objects.all()




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

def add_user(f,l,e,a):
    User.objects.create(first_name = f , last_name = l , email_address = e , age = a )

def get_all_users():
    return User.objects.all()
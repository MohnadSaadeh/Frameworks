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
    
def add_user(firstName,lastName,eMail,aGe):
    User.objects.create(first_name = firstName , last_name = lastName , email_address = eMail , age = aGe )

def get_all_users():
    return User.objects.all()


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_auther():
    Author.objects.create(name = autherName)

def create_book(bookName , autherName):
    #create_auther()
    our_auther = Author.objects.get(name = autherName)
    Book.objects.create(title=bookName,author=our_auther)

def get_all_books():
    return Book.objects.all()

def delete_author(id):
    del_author = Author.objects.get(id = id)
    del_author.delete()

def delete_book(id):
    del_book = Book.objects.get(id = id)
    del_book.delete()



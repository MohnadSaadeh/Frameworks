from django.db import models
import re
# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        DATE_REGEX = re.compile(r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$')
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 3  :
            errors["title"] = "title should be at least 3 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) < 3:
            errors["description"] = "a Description should be at least 3 characters"
        if not DATE_REGEX.match(postData['release_date']):
            errors["release_date"] = "the Date shuld be like YYYY-MM-DD"
        return errors


class Show(models.Model):
    title  = models.CharField(max_length= 45)
    network = models.CharField(max_length= 45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


def create_a_show(show_title, show_network, show_release_date , show_description ):
    return Show.objects.create(title=show_title , network=show_network , release_date=show_release_date , description=show_description )

def all_shows():
    return Show.objects.all()

def view_a_show(id):
    return Show.objects.get(id = id)


def update_a_show(id, show_title, show_network, show_release_date, show_description):
    show = Show.objects.get(id = id)
    show.title = show_title
    show.network = show_network
    show.release_date = show_release_date
    show.description = show_description
    show.save()
    return show

def delete_a_show(id):
    show = Show.objects.get(id = id)
    return show.delete()
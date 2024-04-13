from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 3  :
            errors["title"] = "title should be at least 3 characters"
        if Show.objects.filter (title = postData['title']):
            errors["title"] = "this show is already exist"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) < 3:
            errors["description"] = "a Description should be at least 3 characters"
        # if not EMAIL_REGEX.match(postData['author_notes']):
        #     errors["author_notes"] = "the note shuld be an E-mail"
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

def delete_a_show(id):
    show = Show.objects.get(id = id)
    return show.delete()


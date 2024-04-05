from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ninjas = list of ninjas associated with a givin dogo
    def __repr__(self):
        return "Dojo_name: {}".format(self.name)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE) #prtect ///////////  set null
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return "first_name: {}".format(self.first_name)

def get_all_ninjas():
    return Ninja.objects.all()
    
def get_all_dojos():
    return Dojo.objects.all()

def add_dojo(dojo_name,dojo_city,dojo_state,dojo_desc):
    return Dojo.objects.create(name=dojo_name, city=dojo_city , state = dojo_state ,desc=dojo_desc)

def add_ninja(ninja_first_name ,ninja_last_name,ninja_dojo):
    return Ninja.objects.create(first_name=ninja_first_name ,last_name=ninja_last_name , dojo=(Dojo.objects.get(name=ninja_dojo)))

def delete_a_ninja(ninja_id):
    a_ninja = Ninja.objects.get(id = ninja_id)
    return a_ninja.delete()

def delete_a_dojo(dojo_id):
    a_dojo = Dojo.objects.get(id = dojo_id)
    return a_dojo.delete()


def anchor_delete_ninja(id):          #using <a> anchor to delete
    a_ninja = Ninja.objects.get(id = id)
    return a_ninja.delete()

def add_dojo_(post_data):
    return Dojo.objects.create(name=post_data['dojo_name'], city=post_data['dojo_city'] , state = post_data['dojo_state'] ,desc=post_data['dojo_discription'])
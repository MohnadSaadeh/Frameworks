from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepage),
    path('add_method', views.get_the_dojo),
]

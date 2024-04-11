from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_user', views.get_user),
    path('addBook', views.add_book),
    path('delauthor', views.delete_author),
    path('delabook', views.delete_book),
    ]
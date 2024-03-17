from django.urls import path     
from . import views
urlpatterns = [ 
        path('', views.index),   
        path('login', views.login), 
        path('checklogin', views.check_login), 
        path('hompage', views.home),
        ]
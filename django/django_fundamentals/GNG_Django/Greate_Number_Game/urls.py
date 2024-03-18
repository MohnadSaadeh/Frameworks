from django.urls import path     
from . import views
urlpatterns = [
        path('', views.theroot1),
        path('yourguess', views.yourguess),
    ]
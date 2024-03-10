from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),      # the name of the function
    path('next/<str:memoi>', views.some_function),
    path('login', views.login ),
]

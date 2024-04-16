from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('log_in', views.login),
    path('success', views.success),
    path('logout', views.logout),
]

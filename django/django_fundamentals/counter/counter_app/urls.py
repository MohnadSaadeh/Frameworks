from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('destroy_session', views.the_new_route),
    path('plus2', views.theplus2),
]

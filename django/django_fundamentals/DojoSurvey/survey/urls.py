from django.urls import path     
from . import views
urlpatterns = [ 
        path('', views.first),
        path('result', views.theresult),
    ]
from django.urls import path     
from . import views
urlpatterns = [
        path('', views.theroot1),
        path('yourguess', views.yourguess),
        path('loose', views.lose_page),
        path('winpage', views.win_page)
    ]
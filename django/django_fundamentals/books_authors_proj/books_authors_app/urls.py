from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('add_book', views.get_the_book),
    path('view_book/<int:id>', views.book),
]
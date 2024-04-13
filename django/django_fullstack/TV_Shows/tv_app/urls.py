from django.urls import path     
from . import views
urlpatterns = [
    path('', views.tv_shows ),
    path('shows', views.shows ),
    path('shows/<int:id>', views.view_a_show ), # go to a show by id
    path('new', views.add_show_page ),
    path('add_show', views.get_show ),
    
]

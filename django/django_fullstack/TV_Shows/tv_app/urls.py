from django.urls import path     
from . import views
urlpatterns = [
    path('', views.tv_shows ),
    path('shows', views.shows ),
    path('shows/<int:id>', views.view_a_show ), # go to a show by id
    path('edit_a_show/<int:id>', views.edit_a_show ), # Edit a show by id
    path('update_a_show/<int:id>', views.update_a_show ), # Update a show by id
    path('delete_a_show/<int:id>', views.delete_a_show), # Delete a show by id
    path('new', views.add_show_page ),
    path('add_show', views.get_show ),
    
]

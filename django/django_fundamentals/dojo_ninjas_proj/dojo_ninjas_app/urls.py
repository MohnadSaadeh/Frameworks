from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.homepage),
    path('add_method', views.get_the_dojo),
    path('delete_ninja', views.delete_ninja),
    path('delete_ninja/<int:id>', views.delete_ninja_by_anchor), # using <a> anchor to delete
]

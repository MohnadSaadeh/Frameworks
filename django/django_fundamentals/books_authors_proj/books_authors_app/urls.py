from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('add_book', views.get_the_book),
    path('add_author', views.get_the_author),

    path('view_book/<int:id>', views.book),
    path('add_author_to_book/<int:id>', views.get_author_and_book),
    path('authors_page', views.authors_page),
    path('view_author/<int:id>', views.author),
    path('add_book_to_author/<int:id>', views.add_book_to_autho),
]
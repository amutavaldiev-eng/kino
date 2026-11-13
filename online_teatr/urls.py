from django.urls import path
from .views import *

urlpatterns = [
    path('',movie_list, name='movie_list'),
    path('movies/',movie_list, name='movies'),
    path('genres/',genres, name='genres'),
    path('genre/<int:id>/',genre_movies, name='genre_movies'),
    path('movie/<int:id>/',movie_detail, name='movie_detail'),
    path('movie/<int:id>/comment/', add_comment, name='add_comment'),
    path('comments/', my_comments, name='my_comments'),
    path('create_genre/', create_genre, name='create_genre'),
    path('create_movie/',create_movie, name='create_movie'),
    path('update_movie/<int:id>/', update_movie, name='update_movie'),
    path('delete_movie/<int:id>/', delete_movie, name='delete_movie'),
]
from django.urls import path
from movie.views import homepage_view, movie_list_view, movie_detail_view, genre_detail_view, testing_cheatsheet_view, \
    genre_list_view

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('movies/list/', movie_list_view, name='movie-list'),
    path('movie/<int:pk>/', movie_detail_view, name='movie-detail'),
    path('genre/<int:pk>/', genre_detail_view, name='genre-detail'),
    path('genre/list/', genre_list_view, name='genre-list'),
    path('testing_data_types_in_templates', testing_cheatsheet_view, name='data-types-testing')
]

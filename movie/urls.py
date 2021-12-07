from django.urls import path, include

from movie.views.cinema import CinemaListView, CinemaDetailView, ShowingDetailView
from movie.views.generic import DislikeMovieView, homepage_view, TestingCheatSheetView, DummyFormView
from movie.views.movie import MovieListView, MovieDetailView, MovieDeleteView, MovieUpdateView, MovieCreateView, \
    GenreDetailView, GenreListView, ActorDetailView, ActorListView, ActorDeleteView, ActorUpdateView, ActorCreateView, \
    DirectorListView, DirectorDetailView

movie_urlpatterns = (
    [
        path('list/', MovieListView.as_view(), name='list'),
        path('detail/<int:pk>', MovieDetailView.as_view(), name='detail'),
        path('dislike/<int:pk>', DislikeMovieView.as_view(), name='dislike'),
        path('create/', MovieCreateView.as_view(), name='create'),
        path('update/<int:pk>/', MovieUpdateView.as_view(), name='update'),
        path('delete/<int:pk>/', MovieDeleteView.as_view(), name='delete'),
    ], 'movie'
)

genre_urlpatterns = (
    [
        path('detail/<int:pk>/', GenreDetailView.as_view(), name='detail'),
        path('list/', GenreListView.as_view(), name='list'),

    ], 'genre'
)

actor_urlpatterns = (
    [
        path('detail/<int:pk>/', ActorDetailView.as_view(), name='detail'),
        path('list/', ActorListView.as_view(), name='list'),
        path('create/', ActorCreateView.as_view(), name='create'),
        path('update/<int:pk>/', ActorUpdateView.as_view(), name='update'),
        path('delete/<int:pk>/', ActorDeleteView.as_view(), name='delete'),
    ], 'actor'
)

director_urlpatterns = (
    [
        path('list/', DirectorListView.as_view(), name='list'),
        path('detail/<int:pk>/', DirectorDetailView.as_view(), name='detail'),
    ], 'director'
)

cinema_urlpatterns = (
    [
        path('list/', CinemaListView.as_view(), name='list'),
        path('detail/<int:pk>/', CinemaDetailView.as_view(), name='detail'),
    ], 'cinema'
)

showing_urlpatterns = (
    [
        path('detail/<int:pk>/', ShowingDetailView.as_view(), name='detail'),
    ], 'showing'
)

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('testing_data_types_in_templates/', TestingCheatSheetView.as_view(), name='data-types-testing'),
    path('dummy_forms/', DummyFormView.as_view(), name='dummy-form'),
    path('movie/', include(movie_urlpatterns)),
    path('genre/', include(genre_urlpatterns)),
    path('actor/', include(actor_urlpatterns)),
    path('director/', include(director_urlpatterns)),
    path('cinema/', include(cinema_urlpatterns)),
    path('showing/', include(showing_urlpatterns)),
]



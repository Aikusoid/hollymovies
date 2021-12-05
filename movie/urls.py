from django.urls import path
from movie.views import homepage_view, MovieListView, GenreListView, ActorListView, \
    DirectorListView, MovieDetailView, GenreDetailView, DirectorDetailView, ActorDetailView, DislikeMovieView, \
    TestingCheatSheetView, CinemaListView, CinemaDetailView, ShowingDetailView, DummyFormView, CreateMovieView, \
    CreateActorView, UpdateMovieView

urlpatterns = [
    path('homepage/', homepage_view, name='homepage'),
    path('movies/list/', MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
    path('genre/list/', GenreListView.as_view(), name='genre-list'),
    path('actors/list/', ActorListView.as_view(), name='actor-list'),
    path('directors/list/', DirectorListView.as_view(), name='director-list'),
    path('actor/<int:pk>/', ActorDetailView.as_view(), name='actor-detail'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('dislike_movie/<int:pk>/', DislikeMovieView.as_view(), name='dislike-movie'),
    path('testing_data_types_in_templates/', TestingCheatSheetView.as_view(), name='data-types-testing'),
    path('cinema/list/', CinemaListView.as_view(), name='cinema-list'),
    path('cinema/<int:pk>/', CinemaDetailView.as_view(), name='cinema-detail'),
    path('showing/<int:pk>/', ShowingDetailView.as_view(), name='showing-detail'),
    path('dummy_forms/', DummyFormView.as_view(), name='dummy-form'),
    path('create/movie/', CreateMovieView.as_view(), name='create-movie'),
    path('create/actor/', CreateActorView.as_view(), name='create-actor'),
    path('update/movie/<int:pk>/', UpdateMovieView.as_view(), name='update-movie'),
]



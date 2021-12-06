from django.urls import path, include
from movie.views import homepage_view, MovieListView, GenreListView, ActorListView, \
    DirectorListView, MovieDetailView, GenreDetailView, DirectorDetailView, ActorDetailView, DislikeMovieView, \
    TestingCheatSheetView, CinemaListView, CinemaDetailView, ShowingDetailView, DummyFormView, CreateMovieView, \
    CreateActorView, UpdateMovieView, MovieDeleteView, UpdateActorView, ActorDeleteView

movie_urlpatterns = (
    [
        path('list/', MovieListView.as_view(), name='list'),
        path('detail/<int:pk>', MovieDetailView.as_view(), name='detail'),
        path('dislike/<int:pk>', DislikeMovieView.as_view(), name='dislike'),
        path('create/', CreateMovieView.as_view(), name='create'),
        path('update/<int:pk>/', UpdateMovieView.as_view(), name='update'),
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
        path('create/', CreateActorView.as_view(), name='create'),
        path('update/<int:pk>/', UpdateActorView.as_view(), name='update'),
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



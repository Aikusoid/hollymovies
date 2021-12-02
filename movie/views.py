from django.shortcuts import render, resolve_url, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectTemplateResponseMixin, BaseDetailView, DetailView

from movie.models import Movie, Genre, MovieLikeRegister, Actor, Director, Cinema, CinemaMovieShowings


def homepage_view(request):
    context = {
        'number_of_movies': Movie.objects.all().count(),
        'number_of_genres': Genre.objects.all().count(),
        'number_of_actors': Actor.objects.all().count(),
        'number_of_directors': Director.objects.all().count(),
        'most_liked_movie': Movie.objects.all().order_by('-likes').first(),
        'best_rated_movie': Movie.objects.all().order_by('-rating').first(),
    }
    return TemplateResponse(request, 'homepage.html', context=context)

# def movie_list_view(request):
#     context = {
#         'movies': Movie.objects.all().order_by('-likes', '-rating'),
#
#     }
#     return TemplateResponse(request, 'movieList.html', context=context)


class MovieListView(ListView):
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         'movies': Movie.objects.all().order_by('-likes', '-rating'),
    #     }
    # return TemplateResponse(request, 'movieList.html', context=context)
    queryset = Movie.objects.all().order_by('-likes', '-rating')
    template_name = 'movieList.html'

# def genre_list_view(request):
#     context = {
#         'genres': Genre.objects.all(),
#     }
#     return TemplateResponse(request, 'genreList.html', context=context)


class GenreListView(View):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        context = {
            'genres': Genre.objects.all(),
        }
        return TemplateResponse(request, 'genreList.html', context=context)

# def actor_list_view(request):
#     return TemplateResponse(request, 'actorList.html')


class ActorListView(TemplateView):
    template_name = 'actorList.html'

# def director_list_view(request):
#     return TemplateResponse(request, 'directorList.html')


class DirectorListView(TemplateView):
    template_name = 'directorList.html'

# def movie_detail_view(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#
#     if request.user.is_authenticated:
#         user_liked_movie = MovieLikeRegister.objects.filter(user=request.user, movie=movie).exists()
#     else:
#         user_liked_movie = False
#
#     if request.method == 'POST' and request.user.is_authenticated and not user_liked_movie:
#         movie.likes += 1
#         movie.save(update_fields=['likes'])
#         MovieLikeRegister.objects.create(
#             user=request.user,
#             movie=movie,
#         )
#         user_liked_movie = True
#
#     context = {
#         'movie': movie,
#         'already_liked': user_liked_movie,
#     }
#     return TemplateResponse(request, 'movieDetail.html', context=context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movieDetail.html'

    @property
    def user_already_liked(self):
        if self.request.user.is_authenticated:
            user_liked_movie = MovieLikeRegister.objects.filter(user=self.request.user, movie=self.object).exists()
        else:
            user_liked_movie = False
        return user_liked_movie

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context.update({
            'already_liked': self.user_already_liked,
        })
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.user_already_liked:
            return self.get(request, *args, **kwargs)
        else:
            self.object.likes += 1
            self.object.save(update_fields=['likes'])
            MovieLikeRegister.objects.create(
                user=request.user,
                movie=self.object,
            )
            return self.get(request, *args, **kwargs)

# def genre_detail_view(request, pk):
#     context = {
#         'genre': get_object_or_404(Genre, pk=pk),
#     }
#     return TemplateResponse(request, 'genreDetail.html', context=context)


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genreDetail.html'

# def director_detail_view(request, pk):
#     context = {
#         'director': get_object_or_404(Director, pk=pk),
#     }
#     return TemplateResponse(request, 'directorDetail.html', context=context)


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'directorDetail.html'

# def actor_detail_view(request, pk):
#     context = {
#         'actor': get_object_or_404(Actor, pk=pk),
#     }
#     return TemplateResponse(request, 'actorDetail.html', context=context)


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'actorDetail.html'

# def dislike_movie_view(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     movie.dislikes += 1
#     movie.save(update_fields=['dislikes'])
#     return redirect('movie-detail', pk=pk)


class DislikeMovieView(DetailView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        movie = get_object_or_404(Movie, pk=pk)
        movie.dislikes += 1
        movie.save(update_fields=['dislikes'])
        return redirect('movie-detail', pk=pk)

# def testing_cheatsheet_view(request):
#     # python list[0]
#     # template language jinja2 list.0
#
#     # python dict['key']
#     # template language jinja2 dict.key
#     context = {
#         'list': ['index0', 'index1'],
#         'dict': {
#             'key': 'value',
#             'key2': 'value2',
#         }
#     }
#     return TemplateResponse(request, 'dataTypesTesting.html', context=context)


class TestingCheatSheetView(TemplateView):
    template_name = 'dataTypesTesting.html'

    # python list[0]
    # template language jinja2 list.0

    # python dict['key']
    # template language jinja2 dict.key
    extra_context = {
        'list': ['index0', 'index1'],
        'dict': {
            'key': 'value',
            'key2': 'value2',
        }
    }


class CinemaListView(ListView):
    model = Cinema
    template_name = 'cinemaList.html'


class CinemaDetailView(DetailView):
    model = Cinema
    template_name = 'cinemaDetail.html'

    def get_context_data(self, **kwargs):
        context = super(CinemaDetailView, self).get_context_data(**kwargs)
        showings = self.object.showings.all()

        active_showings = []

        for showing in showings:
            if showing.closed:
                continue
            elif showing.sold_out:
                continue
            active_showings.append(showing)

        context.update({
            'showings': active_showings
        })
        return context

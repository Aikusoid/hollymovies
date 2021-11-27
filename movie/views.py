from django.shortcuts import render, resolve_url, get_object_or_404
from django.http import HttpResponse
from django.template.response import TemplateResponse

from movie.models import Movie, Genre


def homepage_view(request):
    context = {
        'number_of_movies': Movie.objects.all().count(),
        'number_of_genres': Genre.objects.all().count(),
        'most_liked_movie': Movie.objects.all().order_by('-likes').first(),
        'best_rated_movie': Movie.objects.all().order_by('-rating').first(),
    }
    return TemplateResponse(request, 'homepage.html', context=context)


def movie_list_view(request):
    context = {
        'movies': Movie.objects.all().order_by('-likes', '-rating'),

    }
    return TemplateResponse(request, 'movieList.html', context=context)


def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    context = {
        'movie': movie,
    }
    return TemplateResponse(request, 'movieDetail.html', context=context)


def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    context = {
        'movie': genre,
    }
    return TemplateResponse(request, 'genreDetail.html', context=context)


def testing_cheatsheet_view(request):
    # python list[0]
    # template language jinja2 list.0

    # python dict['key']
    # template language jinja2 dict.key
    context = {
        'list': ['index0', 'index1'],
        'dict': {
            'key': 'value',
            'key2': 'value2',
        }
    }
    return TemplateResponse(request, 'dataTypesTesting.html', context=context)

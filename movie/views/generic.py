from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views.generic import DetailView, FormView, TemplateView
from django.urls import reverse_lazy

from movie.forms import DummyForm
from movie.models import Movie, Genre, Actor, Director


#########################
# Function based views #
#########################

def homepage_view(request):
    context = {
        'number_of_movies': Movie.objects.all().count(),
        'number_of_genres': Genre.objects.all().count(),
        'number_of_actors': Actor.objects.all().count(),
        'number_of_directors': Director.objects.all().count(),
        'most_liked_movie': Movie.objects.all().order_by('-likes').first(),
        'best_rated_movie': Movie.objects.all().order_by('-rating').first(),
    }
    return TemplateResponse(request, 'generic/homepage.html', context=context)


def dislike_movie_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.dislikes += 1
    movie.save(update_fields=['dislikes'])
    return redirect('movie-detail', pk=pk)


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
    return TemplateResponse(request, 'generic/data_types_testing.html', context=context)


######################
# Class based views #
######################


class DislikeMovieView(DetailView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        movie = get_object_or_404(Movie, pk=pk)
        movie.dislikes += 1
        movie.save(update_fields=['dislikes'])
        return redirect('movie:detail', pk=pk)


class TestingCheatSheetView(TemplateView):
    template_name = 'generic/data_types_testing.html'

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


class DummyFormView(FormView):
    form_class = DummyForm
    template_name = 'generic/dummy_forms.html'
    success_url = reverse_lazy('dummy-form')
    initial = {'username': 'Honza'}

    def get_form(self, form_class=None):
        return DummyForm(10, **self.get_form_kwargs())

    def form_valid(self, form):
        int_field = form.cleaned_data['int_field']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        datetime_test = form.cleaned_data['datetime_test']
        movie = form.cleaned_data['movie']
        movies = form.cleaned_data['movies']
        difficulty = form.cleaned_data['difficulty']
        print(int_field)
        print(username)
        print(email)
        print(datetime_test)
        print(movie)
        print(movies)
        print(difficulty)

        return super(DummyFormView, self).form_valid(form)

    def form_invalid(self, form):
        print('Form is invalid!')
        return super(DummyFormView, self).form_invalid(form)



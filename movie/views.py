from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import ListView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from movie.forms import DummyForm, MovieForm, ActorForm
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
    return TemplateResponse(request, 'generic/homepage.html', context=context)


# def movie_list_view(request):
#     context = {
#         'movies': Movie.objects.all().order_by('-likes', '-rating'),
#
#     }
#     return TemplateResponse(request, 'list.html', context=context)


class MovieListView(ListView):
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         'movies': Movie.objects.all().order_by('-likes', '-rating'),
    #     }
    # return TemplateResponse(request, 'list.html', context=context)
    queryset = Movie.objects.all().order_by('-likes', '-rating')
    template_name = 'movies/list.html'


# def genre_list_view(request):
#     context = {
#         'genres': Genre.objects.all(),
#     }
#     return TemplateResponse(request, 'list.html', context=context)


class GenreListView(View):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        context = {
            'genres': Genre.objects.all(),
        }
        return TemplateResponse(request, 'genres/list.html', context=context)


# def actor_list_view(request):
#     return TemplateResponse(request, 'list.html')


class ActorListView(TemplateView):
    template_name = 'actors/list.html'


# def director_list_view(request):
#     return TemplateResponse(request, 'list.html')


class DirectorListView(TemplateView):
    template_name = 'directors/list.html'


class CinemaListView(ListView):
    model = Cinema
    template_name = 'cinemas/list.html'

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
#     return TemplateResponse(request, 'detail.html', context=context)


# def genre_detail_view(request, pk):
#     context = {
#         'genre': get_object_or_404(Genre, pk=pk),
#     }
#     return TemplateResponse(request, 'detail.html', context=context)


# def director_detail_view(request, pk):
#     context = {
#         'director': get_object_or_404(Director, pk=pk),
#     }
#     return TemplateResponse(request, 'detail.html', context=context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/detail.html'

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


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genres/detail.html'

# def actor_detail_view(request, pk):
#     context = {
#         'actor': get_object_or_404(Actor, pk=pk),
#     }
#     return TemplateResponse(request, 'detail.html', context=context)


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'actors/detail.html'


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'directors/detail.html'

# def dislike_movie_view(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     movie.dislikes += 1
#     movie.save(update_fields=['dislikes'])
#     return redirect('movie-detail', pk=pk)


class CinemaDetailView(DetailView):
    model = Cinema
    template_name = 'cinemas/detail.html'

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


class ShowingDetailView(DetailView):
    model = CinemaMovieShowings
    template_name = 'cinemas/showing_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.sold_tickets += 1
        self.object.save(update_fields=['sold_tickets', ])
        return self.get(request, *args, *kwargs)


class DislikeMovieView(DetailView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        movie = get_object_or_404(Movie, pk=pk)
        movie.dislikes += 1
        movie.save(update_fields=['dislikes'])
        return redirect('movie:detail', pk=pk)

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
#     return TemplateResponse(request, 'data_types_testing.html', context=context)


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

# class DummyFormView(View):
# 
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': DummyForm()
#         }
#         return TemplateResponse(request, 'dummy_forms.html', context=context)
# 
#     def post(self, request, *args, **kwargs):
#         bounded_form = DummyForm(data=request.POST)
# 
#         if not bounded_form.is_valid():
#             context = {'form': bounded_form}
#             return TemplateResponse(request, 'dummy_forms.html', context=context)
# 
#         int_field = bounded_form.cleaned_data['int_field']
#         username = bounded_form.cleaned_data['username']
#         email = bounded_form.cleaned_data['email']
#         datetime_test = bounded_form.cleaned_data['datetime_test']
#         movie = bounded_form.cleaned_data['movie']
#         movies = bounded_form.cleaned_data['movies']
#         difficulty = bounded_form.cleaned_data['difficulty']
#         print(int_field)
#         print(username)
#         print(email)
#         print(datetime_test)
#         print(movie)
#         print(movies)
#         print(difficulty)
#         return self.get(request, *args, **kwargs)


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


class DeleteSuccessMixin:
    success_message = ''

    def get_success_message(self):
        return self.success_message

    def delete(self, request, *args, **kwargs):
        super(DeleteSuccessMixin, self).delete(request, *args, **kwargs)

        messages.success(request, self.get_success_message())

        return HttpResponseRedirect(self.get_success_url())


class CreateMovieView(SuccessMessageMixin, CreateView):
    template_name = 'movies/create.html'
    form_class = MovieForm
    success_message = 'Successfully created!'

    def get_success_url(self):
        return reverse('movie:detail', args=[self.object.id])


class UpdateMovieView(SuccessMessageMixin, UpdateView):
    template_name = 'movies/update.html'
    form_class = MovieForm
    model = Movie
    success_message = 'Successfully updated!'

    def get_success_url(self):
        return reverse('movie:detail', args=[self.object.id])


class MovieDeleteView(DeleteSuccessMixin, DeleteView):
    model = Movie

    def get_success_message(self):
        return f'{self.object.name} successfully deleted!'

    def get_success_url(self):
        return reverse('movie:list')


class CreateActorView(SuccessMessageMixin, CreateView):
    template_name = 'actors/create.html'
    form_class = ActorForm
    success_message = 'Successfully created!'

    def get_success_url(self):
        return reverse('actor:detail', args=[self.object.id])


class UpdateActorView(SuccessMessageMixin, UpdateView):
    template_name = 'actors/update.html'
    form_class = ActorForm
    model = Actor
    success_message = 'Successfully updated!'

    def get_success_url(self):
        return reverse('actor:detail', args=[self.object.id])


class ActorDeleteView(DeleteSuccessMixin, DeleteView):
    model = Actor

    def get_success_message(self):
        return f'{self.object.full_name} successfully deleted!'

    def get_success_url(self):
        return reverse('actor:list')

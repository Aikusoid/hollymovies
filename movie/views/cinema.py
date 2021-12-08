from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from movie.forms import CinemaForm
from movie.models import Cinema, CinemaMovieShowings


######################
# Class based views #
######################
from movie.views.mixins import DeleteSuccessMixin


class CinemaListView(ListView):
    model = Cinema
    template_name = 'cinemas/list.html'


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


class CinemaCreateView(SuccessMessageMixin, CreateView):
    template_name = 'cinemas/create.html'
    form_class = CinemaForm
    success_message = 'Successfully created!'

    def get_success_url(self):
        return reverse('cinema:detail', args=[self.object.id])


class CinemaUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'cinemas/update.html'
    form_class = CinemaForm
    model = Cinema
    success_message = 'Successfully updated!'

    def get_success_url(self):
        return reverse('cinema:detail', args=[self.object.id])


class CinemaDeleteView(DeleteSuccessMixin, DeleteView):
    model = Cinema

    def get_success_message(self):
        return f'{self.object.full_name} successfully deleted!'

    def get_success_url(self):
        return reverse('cinema:list')


class ShowingDetailView(DetailView):
    model = CinemaMovieShowings
    template_name = 'cinemas/showing_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.sold_tickets += 1
        self.object.save(update_fields=['sold_tickets', ])
        return self.get(request, *args, *kwargs)

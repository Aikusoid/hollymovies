from django.views.generic import ListView, DetailView

from movie.models import Cinema, CinemaMovieShowings


######################
# Class based views #
######################


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


class ShowingDetailView(DetailView):
    model = CinemaMovieShowings
    template_name = 'cinemas/showing_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.sold_tickets += 1
        self.object.save(update_fields=['sold_tickets', ])
        return self.get(request, *args, *kwargs)

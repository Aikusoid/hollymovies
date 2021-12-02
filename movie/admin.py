from datetime import timedelta

from django.contrib import admin
from django.utils import timezone

from movie.models import Movie, Genre, Actor, Director, Cinema, CinemaMovieShowings


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'rating', 'created']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age']


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age']


class CinemaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']


class CinemaMovieShowingsAdmin(admin.ModelAdmin):

    @staticmethod
    def is_closed(obj):
        return obj.is_closed

    @staticmethod
    def sold_out(obj):
        return obj.sold_out

    list_display = ['cinema', 'movie', 'showing_time', 'duration', 'sold_out', 'sales_open', 'closed']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(CinemaMovieShowings, CinemaMovieShowingsAdmin)

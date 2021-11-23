from django.contrib import admin
from movie.models import Movie, Genre


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'rating', 'created']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)

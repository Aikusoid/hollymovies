from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    modified = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True


class Genre(BaseModel):
    name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return f'{self.name}'


class Movie(BaseModel):
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True, default='')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.FloatField(validators=[
        MaxValueValidator(10),
        MinValueValidator(0),
    ], default=0)

    def __str__(self):
        return f'{self.name} : {self.id}'

    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='movie')


class Person(BaseModel):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.pk}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Actor(Person):
    movies = models.ManyToManyField(Movie, related_name='actors')

    def get_detail_url(self):
        return reverse('actor-detail', args=[self.pk])


class Director(Person):
    movies = models.ManyToManyField(Movie, related_name='directors')

    def get_detail_url(self):
        return reverse('director-detail', args=[self.pk])


class MovieLikeRegister(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Cinema(BaseModel):
    name = models.CharField(max_length=512)
    location = models.CharField(max_length=512)
    movie_showings = models.ManyToManyField(Movie, related_name='cinemas', through='movie.CinemaMovieShowings')

    class Meta:
        unique_together = ('name', 'location')

    def __str__(self):
        return f'{self.name} : {self.location}'


class CinemaMovieShowings(BaseModel):
    showing_time = models.DateTimeField()
    duration = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showings')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='showings')
    numbers_of_tickets = models.IntegerField()
    ticket_price = models.FloatField()
    sold_tickets = models.IntegerField(default=0)
    sales_open = models.BooleanField(default=True)

    @property
    def available_tickets(self):
        return self.numbers_of_tickets - self.sold_tickets

    @property
    def sold_out(self):
        return self.available_tickets <= 0

    @property
    def closed(self):
        now = timezone.now()
        closed = now > (self.showing_time + timedelta(minutes=self.duration))
        return closed

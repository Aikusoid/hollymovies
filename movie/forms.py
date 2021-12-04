from django import forms

from movie.models import Movie


class CustomDatetimeInput(forms.DateTimeInput):
    input_type = 'date'


DIFFICULTY_CHOICES = (
    (1, 'Easy'),
    (2, 'Medium'),
    (3, 'Hard'),
    (4, 'Insane'),
)


class DummyForm(forms.Form):
    int_field = forms.IntegerField(required=False, min_value=5, max_value=10)
    username = forms.CharField(required=False, empty_value='unknown', label='Dummy username')
    email = forms.EmailField(required=False)
    datetime_test = forms.DateTimeField(widget=CustomDatetimeInput)
    # alternative:
    # datetime_test = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)


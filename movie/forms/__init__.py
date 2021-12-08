from django import forms

from movie import choices
from movie.forms.validators import validate_capitalized, validate_username_is_not_aigerim
from movie.forms.widgets import CustomDatetimeInput, BootstrapEmailWidget
from movie.models import Movie, Actor, Genre, Director, Cinema


class DummyForm(forms.Form):
    int_field = forms.IntegerField(required=False, min_value=5, max_value=10)
    username = forms.CharField(validators=[validate_username_is_not_aigerim],
                               required=False, empty_value='unknown',
                               label='Dummy username')
    email = forms.EmailField(required=False, widget=BootstrapEmailWidget)
    datetime_test = forms.DateTimeField(widget=CustomDatetimeInput)
    # alternative:
    # datetime_test = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())
    difficulty = forms.ChoiceField(choices=choices.DIFFICULTY_CHOICES,
                                   initial=choices.DIFFICULTY_CHOICE_HARD)

    def clean_username(self):
        return self.cleaned_data['username'].capitalize()

    def __init__(self, min_likes, *args, **kwargs):
        super(DummyForm, self).__init__(*args, **kwargs)
        queryset = Movie.objects.filter(likes__gte=min_likes)
        self.fields['movie'].queryset = queryset
        self.fields['movies'].queryset = queryset


# class MovieForm(forms.Form):
#     name = forms.CharField(max_length=512)
#     description = forms.CharField(widget=forms.Textarea)
#     likes = forms.IntegerField(default=0)
#     dislikes = forms.IntegerField(default=0)
#     rating = forms.FloatField(max_value=10, min_value=0, default=0)
#     genre = forms.ModelChoiceField(required=False, queryset=Genre.objects.all())


class MovieForm(forms.ModelForm):
    name = forms.CharField(max_length=512, validators=[validate_capitalized])

    class Meta:
        model = Movie
        fields = ['name', 'description', 'rating', 'genre']
        # fields = '__all__'


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'


class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=512)

    class Meta:
        model = Genre
        fields = '__all__'


class DirectorForm(forms.ModelForm):
    name = forms.CharField(max_length=512)

    class Meta:
        model = Director
        fields = '__all__'


class CinemaForm(forms.ModelForm):
    name = forms.CharField(max_length=512)

    class Meta:
        model = Cinema
        fields = '__all__'

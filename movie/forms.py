from django import forms
from django.core.exceptions import ValidationError
from django.forms import EmailInput

from movie.models import Movie, Genre, Actor


class CustomDatetimeInput(forms.DateTimeInput):
    input_type = 'date'


DIFFICULTY_CHOICES = (
    (1, 'Easy'),
    (2, 'Medium'),
    (3, 'Hard'),
    (4, 'Insane'),
)


def validate_username_is_not_aigerim(value):
    if value == 'Aigerim':
        raise ValidationError("Username cannot be 'Aigerim'")


def validate_capitalized(value):
    if value[0].islower():
        raise ValidationError('First letter must be uppercase')


class BootstrapEmailWidget(EmailInput):
    def __init__(self, attrs={}):
        attrs.update({'class': 'form-control'})
        super(BootstrapEmailWidget, self).__init__(attrs=attrs)


class DummyForm(forms.Form):
    int_field = forms.IntegerField(required=False, min_value=5, max_value=10)
    username = forms.CharField(validators=[validate_username_is_not_aigerim], required=False, empty_value='unknown',
                               label='Dummy username')
    email = forms.EmailField(required=False, widget=BootstrapEmailWidget)
    datetime_test = forms.DateTimeField(widget=CustomDatetimeInput)
    # alternative:
    # datetime_test = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    movies = forms.ModelMultipleChoiceField(queryset=Movie.objects.all())
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES)

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


# class MovieForm(forms.ModelForm):
#     class Meta:
#         model = Movie
#         # fields = '__all__'
#         fields = ['name', 'description', 'rating', 'genre']
#
#
# class ActorForm(forms.ModelForm):
#     class Meta:
#         model = Actor
#         fields = '__all__'

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


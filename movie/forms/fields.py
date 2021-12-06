from django import forms
from django.core.exceptions import ValidationError


class UsernameNotAigerimField(forms.CharField):
    def validate(self, value):
        if value == 'Aigerim':
            raise ValidationError('Username cannot be Aigerim')
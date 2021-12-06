from django.core.exceptions import ValidationError


def validate_username_is_not_aigerim(value):
    if value == 'Aigerim':
        raise ValidationError("Username cannot be 'Aigerim'")


def validate_capitalized(value):
    if value[0].islower():
        raise ValidationError('First letter must be uppercase')
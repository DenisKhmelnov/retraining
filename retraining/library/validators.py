from django.core.exceptions import ValidationError
from django.forms import forms
from rest_framework import serializers


class PhoneValidator:
    def __init__(self):
        pass
    def __call__(self, value: str):
        print("Call value")
        errors = []
        if len(value) < 12:
            message = 'Phone number should not be less than 11 digits'
            errors.append(forms.ValidationError(message))

        if not value.startswith('+7'):
            message = 'Phone should start with +7 code'
            errors.append(forms.ValidationError(message))

        if errors:
            raise ValidationError(errors)
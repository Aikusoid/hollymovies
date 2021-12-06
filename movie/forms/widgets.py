from django import forms


class CustomDatetimeInput(forms.DateTimeInput):
    input_type = 'date'


class BootstrapEmailWidget(forms.EmailInput):
    def __init__(self, attrs={}):
        attrs.update({'class': 'form-control'})
        super(BootstrapEmailWidget, self).__init__(attrs=attrs)


from django import forms
from .models import FormModel


class Forms(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = {'name', 'address', 'date',}
        order_field = ['name', 'address', 'date']
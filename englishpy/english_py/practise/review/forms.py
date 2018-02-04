from django import forms

from ..models import Verb


class VerbForm(forms.ModelForm):
    class Meta:
        model = Verb
        fields = ('present',)
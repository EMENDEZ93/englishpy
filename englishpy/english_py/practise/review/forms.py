from django import forms

from ..models.models import Present


class VerbForm(forms.ModelForm):
    class Meta:
        model = Present
        fields = ('verb',)
from django import forms
from django.utils.html import strip_tags
from .models import Djeet


class DjeetForm(forms.ModelForm):
    body = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                                attrs={
                                    'placeholder': 'Djeet',
                                    'class': 'form-control'
                                }))

    class Meta:
        model = Djeet
        exclude = ('user', )

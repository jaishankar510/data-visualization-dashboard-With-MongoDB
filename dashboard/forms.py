
from django import forms
from .models import  Blackcoffer


class BlackcofferForm(forms.ModelForm):
    class Meta:
        model = Blackcoffer()
        fields = ['end_year', 'intensity', 'sector','topic', 'insight','title']
        
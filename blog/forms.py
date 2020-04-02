import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import CATEGORIES


class new_project_form(forms.ModelForm):
    project_title = forms.CharField(widget=forms.TextInput())
    project_text = forms.CharField(widget=forms.Textarea())
    project_video = forms.FileField()
    project_category = forms.ChoiceField(choices=CATEGORIES, required=True)
    # key = forms.CharField(widget=forms.TextInput())
